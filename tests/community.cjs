const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const http=require('node:http');

(async()=>{
  const {default:worker}=await import('../services/notes/worker.mjs');
  const {database}=await import('../services/notes/test/sqlite.mjs');
  const db=database(),root=path.resolve(__dirname,'../build');
  const server=http.createServer((req,res)=>{
    const file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));
    const target=file===root?path.join(root,'index.html'):file;
    if(!target.startsWith(root+path.sep)||!fs.existsSync(target)||!fs.statSync(target).isFile()){res.writeHead(404);res.end();return;}
    res.setHeader('content-type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json'})[path.extname(target)]||'application/octet-stream');fs.createReadStream(target).pipe(res);
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base=`http://127.0.0.1:${server.address().port}/`;
  const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
  try{
    const issue=(number,body,extra={})=>({number,state:'open',title:'Fixture',body,user:{login:'test-reader'},created_at:'2026-09-11T10:00:00Z',...extra});
    const legacy=issue(101,'<!-- atlas-note:v1 TCS-6575 -->\n\nLegacy note <script>window.injected=true</script>.');
    const proposal=issue(102,'<!-- atlas-problem:v1 online -->\n\n### Problem statement\n\nA community question.\n\n### Sources\n\nhttps://example.org/research',{title:'[Problem] A new <img src=x onerror=window.injected=true> question'});
    const reply=issue(103,'<!-- atlas-note:v1 GH-102 -->\n\nA legacy reply.');
    let githubDown=false,closed=false,loseResponse=false,notesDown=false;
    const submitted=[],errors=[];
    async function routes(context){
      await context.route('https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/votes',route=>route.fulfill({json:{votes:[],mine:[]}}));
      await context.route('https://api.github.com/repos/vaclavrozhon/atlas/issues?**',route=>{
        if(githubDown)return route.fulfill({status:403,json:{message:'API rate limit exceeded'}});
        return new URL(route.request().url()).searchParams.get('page')==='1'?
          route.fulfill({json:[closed?{...legacy,state:'closed'}:legacy],headers:{'access-control-expose-headers':'Link',link:'<https://api.github.com/repos/vaclavrozhon/atlas/issues?page=2>; rel="next"'}}):route.fulfill({json:[proposal,reply,issue(104,'Ordinary issue')]});
      });
      await context.route('https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/notes**',async route=>{
        const req=route.request();
        if(notesDown)return route.fulfill({status:503,json:{error:'Notes offline.'}});
        const request=new Request(req.url(),{method:req.method(),headers:req.headers(),...(req.postData()?{body:req.postData()}:{} )});
        const response=await worker.fetch(request,{DB:db,NOTES_ADMIN_TOKEN:'a'.repeat(64),NOTES_ALLOWED_ORIGINS:new URL(base).origin});
        if(req.method()==='POST'){
          submitted.push(req.postDataJSON());
          if(loseResponse){loseResponse=false;return route.fulfill({status:503,json:{error:'Connection interrupted after saving.'}});}
        }
        await route.fulfill({status:response.status,headers:Object.fromEntries(response.headers),body:await response.text()});
      });
      await context.route('https://github.com/vaclavrozhon/atlas/issues/new?**',route=>route.fulfill({contentType:'text/html',body:'<!doctype html><title>Local submission fixture</title>'}));
    }
    const context=await browser.newContext({viewport:{width:1440,height:1000}});await routes(context);
    await context.addInitScript(()=>localStorage.setItem('tcs-atlas-notes',JSON.stringify({'TCS-6575':'PRIVATE TEXT — must not be shared'})));
    const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
    await page.goto(base+'?benchmark=top100#TCS-6575');
    await page.waitForFunction(()=>ATLAS_COMMUNITY.contributions.length===3&&!document.getElementById('refresh-community').disabled);
    const total=await page.evaluate(()=>ATLAS_DEBUG.state.matches.length);
    assert.equal(await page.locator('#community-problems img,#community-problems script,.public-note script').count(),0);
    await page.locator('#TCS-6575 [data-public-note]').click();
    assert.equal(await page.locator('#submit-contribution').innerText(),'Post note');
    assert((await page.locator('#contribution-help').innerText()).includes('no account needed'));
    await page.locator('#public-note-text').fill('A public note: řetězec <script>window.injected=true</script>.');
    await page.locator('#public-note-author').fill('<img src=x onerror=window.injected=true>');
    await page.locator('#close-contribution').click();await page.locator('#TCS-6575 [data-public-note]').click();
    assert((await page.locator('#public-note-text').inputValue()).includes('řetězec'));
    loseResponse=true;await page.locator('#submit-contribution').click();
    await page.waitForFunction(()=>document.getElementById('contribution-result').textContent.includes('draft is kept'));
    await page.reload();await page.waitForFunction(()=>window.ATLAS_COMMUNITY);
    await page.locator('#TCS-6575 [data-public-note]').click();await page.locator('#submit-contribution').click();
    await page.waitForFunction(()=>!document.getElementById('contribution-dialog').open);
    assert.equal(context.pages().length,1,'Posting a note never opens a login or popup');
    assert.equal(submitted.length,2);assert.equal(submitted[0].id,submitted[1].id,'Lost-response retry uses the same identifier');
    assert.equal(submitted[0].edit_token,submitted[1].edit_token);
    assert(!JSON.stringify(submitted).includes('PRIVATE TEXT'));
    assert.equal(await page.locator('#TCS-6575 .public-note').count(),2,'Only one new note was created');
    assert.equal(await page.locator('#TCS-6575 .public-note img,#TCS-6575 .public-note script').count(),0);
    assert.equal(await page.evaluate(()=>window.injected),undefined);
    await page.locator('#TCS-6575 [data-public-note]').click();assert.equal(await page.locator('#public-note-text').inputValue(),'');
    await page.setViewportSize({width:390,height:844});
    assert(await page.locator('#contribution-dialog').evaluate(el=>el.scrollWidth<=el.clientWidth));
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await page.locator('#close-contribution').click();await page.setViewportSize({width:1440,height:1000});

    // A separate visitor reads the durable note with no account, draft or delete credential.
    const visitor=await browser.newContext();await routes(visitor);const fresh=await visitor.newPage();
    fresh.on('pageerror',e=>errors.push(e.message));await fresh.goto(base+'?benchmark=top100#TCS-6575');
    await fresh.waitForFunction(()=>ATLAS_COMMUNITY.contributions.length===4);
    assert.equal(await fresh.locator('#TCS-6575 .public-note').count(),2);
    assert.equal(await fresh.locator('[data-delete-note]').count(),0);
    assert.equal(await fresh.evaluate(()=>localStorage.getItem('tcs-atlas-contribution-drafts')),null);
    await fresh.locator('#TCS-6575 [data-public-note]').click();await fresh.locator('#public-note-text').fill('Anonymous observation.');
    githubDown=true;await fresh.locator('#submit-contribution').click();
    await fresh.waitForFunction(()=>!document.getElementById('contribution-dialog').open);
    await fresh.waitForFunction(()=>!document.getElementById('refresh-community').disabled);
    await fresh.evaluate(()=>ATLAS_COMMUNITY.refresh(true));
    assert((await fresh.locator('#community-status').textContent()).includes('GitHub contributions:'),await fresh.locator('#community-status').textContent());
    assert.equal(await fresh.evaluate(()=>ATLAS_COMMUNITY.contributions.filter(n=>n.source==='direct'&&n.author==='Anonymous').length),1);
    await page.evaluate(()=>ATLAS_COMMUNITY.refresh(true));
    assert.equal(await page.evaluate(()=>ATLAS_COMMUNITY.contributions.length),5,'Notes refresh independently of unavailable GitHub');
    notesDown=true;await page.evaluate(()=>ATLAS_COMMUNITY.refresh(true));
    assert.equal(await page.evaluate(()=>ATLAS_COMMUNITY.contributions.length),5,'Outage preserves previously loaded notes');notesDown=false;
    fresh.on('dialog',dialog=>dialog.accept());await fresh.locator('[data-delete-note]').click();
    await fresh.waitForFunction(()=>ATLAS_COMMUNITY.contributions.length===4);
    page.on('dialog',dialog=>dialog.accept());await page.locator('[data-delete-note]').click();
    await page.waitForFunction(()=>document.querySelectorAll('[data-delete-note]').length===0);
    await page.evaluate(()=>ATLAS_COMMUNITY.refresh(true));assert.equal(await page.evaluate(()=>ATLAS_COMMUNITY.contributions.length),3);
    await visitor.close();

    // Migrating a legacy proposal draft must not repeat its optional sections.
    await page.evaluate(()=>localStorage.setItem('tcs-atlas-contribution-drafts',JSON.stringify({problem:{title:'Legacy draft',category:'online',statement:'Question.',definitions:'A legacy definition.'}})));
    await page.reload();await page.waitForFunction(()=>window.ATLAS_COMMUNITY);
    await page.locator('#new-problem').click();
    assert.equal((await page.locator('#proposal-statement').inputValue()).split('A legacy definition.').length,2);
    await page.locator('#proposal-title').fill('Updated legacy draft');
    await page.locator('#close-contribution').click();await page.locator('#new-problem').click();
    assert.equal((await page.locator('#proposal-statement').inputValue()).split('A legacy definition.').length,2);
    await page.locator('#close-contribution').click();

    // Problem proposals keep the GitHub workflow and long-draft fallback.
    await page.locator('#new-problem').click();await page.locator('#proposal-title').fill('New question');
    await page.locator('#proposal-category').selectOption('online');await page.locator('#proposal-statement').fill('A precisely defined question.');
    assert.equal(await page.locator('#problem-fields input,#problem-fields select,#problem-fields textarea').count(),4);
    const opened=context.waitForEvent('page');await page.locator('#submit-contribution').click();const popup=await opened;await popup.waitForLoadState();
    const url=new URL(popup.url());assert.equal(url.origin,'https://github.com');assert(url.searchParams.get('body').startsWith('<!-- atlas-problem:v1 online -->'));await popup.close();
    await page.locator('#proposal-statement').fill('Dlouhé zadání αβγ '.repeat(700));await page.locator('#submit-contribution').click();
    assert(await page.locator('#long-contribution').isVisible());await page.locator('#close-contribution').click();
    await page.evaluate(()=>document.getElementById('community').open=true);
    await page.locator('#GH-102 [data-public-note]').click();assert((await page.locator('#contribution-target').innerText()).startsWith('GH-102'));await page.locator('#close-contribution').click();
    githubDown=false;closed=true;await page.evaluate(()=>ATLAS_COMMUNITY.refresh(true));
    assert.equal(await page.locator('#TCS-6575 .public-note').count(),0,'Deleted direct notes and closed legacy notes disappear');
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),total);
    const blocked=await browser.newContext();await routes(blocked);await blocked.addInitScript(()=>{Storage.prototype.setItem=()=>{throw new Error('Storage unavailable');};});
    const blockedPage=await blocked.newPage();await blockedPage.goto(base+'?benchmark=top100#TCS-6575');
    await blockedPage.locator('#TCS-6575 [data-public-note]').click();await blockedPage.locator('#public-note-text').fill('Keep this text');
    const before=submitted.length;await blockedPage.locator('#submit-contribution').click();
    assert((await blockedPage.locator('#contribution-result').innerText()).includes('Enable browser storage'));
    assert.equal(submitted.length,before);assert.equal(await blockedPage.locator('#public-note-text').inputValue(),'Keep this text');await blocked.close();
    assert.deepEqual(errors,[]);
    console.log(JSON.stringify({checks:['account-free notes with optional names','real worker and SQLite shared between independent visitors','lost-response retry without duplicates','draft persistence and storage failures','anonymous author','plain-text XSS protection','public reads without ownership credentials','owner deletion','independent GitHub and notes outages','legacy GitHub notes and problem proposals','mobile dialog','unchanged benchmark'],errors}));
  }finally{await browser.close();db.close();await new Promise(resolve=>server.close(resolve));}
})().catch(error=>{console.error(error);process.exitCode=1;});
