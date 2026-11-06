/* Public comments persist separately from internal feedback and private drafts. */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const http=require('node:http');
(async()=>{
  const root=path.resolve(__dirname,'../build'),catalog=JSON.parse(fs.readFileSync(root+'/catalog.json'));
  const {default:worker}=await import('../services/notes/worker.mjs');
  const {database}=await import('../services/notes/test/sqlite.mjs');
  const db=database(),targetId=catalog.cards[0].id,admin='a'.repeat(64);
  let lost=false,offline=false,legacyReads=0;
  const posts=[];
  async function routes(context){
    await context.route('https://api.github.com/**',route=>{legacyReads++;return route.fulfill({json:[]});});
    await context.route('**/api/notes**',route=>{legacyReads++;return route.fulfill({json:{notes:[],next:null}});});
    await context.route('**/api/comments**',async route=>{
      const req=route.request();
      if(offline)return route.fulfill({status:503,json:{error:'Comments temporarily unavailable.'}});
      const headers={...req.headers(),'cf-connecting-ip':'192.0.2.1'};
      const response=await worker.fetch(new Request(req.url(),{method:req.method(),headers,...(req.postData()?{body:req.postData()}: {})}),{DB:db,NOTES_ADMIN_TOKEN:admin,NOTES_ALLOWED_ORIGINS:new URL(base).origin});
      if(req.method()==='POST'){posts.push(req.postDataJSON());if(lost){lost=false;return route.abort('failed');}}
      return route.fulfill({status:response.status,headers:Object.fromEntries(response.headers),body:await response.text()});
    });
    await context.route('**/api/votes',route=>route.fulfill({json:{votes:[],mine:[]}}));
    await context.route('**/api/selection',route=>route.fulfill({json:{version:catalog.meta.final_selection.version,choices:[]}}));
    await context.route('**/version.json',route=>route.fulfill({json:{version:catalog.meta.version}}));
  }
  const server=http.createServer((req,res)=>{
    const file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));
    const target=file===root?path.join(root,'index.html'):file;
    if(!target.startsWith(root+path.sep)||!fs.existsSync(target)||!fs.statSync(target).isFile()){res.writeHead(404);res.end();return;}
    res.setHeader('content-type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json'})[path.extname(target)]||'application/octet-stream');fs.createReadStream(target).pipe(res);
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base=`http://127.0.0.1:${server.address().port}/`,browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  try{
    const context=await browser.newContext(),errors=[];await routes(context);
    await context.route('https://github.com/vaclavrozhon/atlas/issues/new?**',route=>route.fulfill({contentType:'text/html',body:'<title>Local submission fixture</title>'}));
    await context.addInitScript(targetId=>{
      localStorage.setItem('tcs-atlas-notes',JSON.stringify({'TCS-6575':'PRIVATE TEXT — must not be shared'}));
      localStorage.setItem('tcs-atlas-public-notes-cache-v1',JSON.stringify([{id:'12345678-1234-4234-8234-123456789abc',problem_id:targetId,author:'Internal',created_at:'2026-09-14T00:00:00Z',text:'CACHED INTERNAL FEEDBACK'}]));
      localStorage.setItem('tcs-atlas-community-cache-v1',JSON.stringify({loadedAt:Date.now(),issues:[{number:1,state:'open',body:'<!-- atlas-note:v1 '+targetId+' -->\nGITHUB INTERNAL FEEDBACK',user:{login:'Internal'}}]}));
      if(!localStorage.getItem('tcs-atlas-contribution-drafts'))localStorage.setItem('tcs-atlas-contribution-drafts',JSON.stringify({['note:'+targetId]:{text:'OLD PRIVATE DRAFT'},problem:{title:'Unsent question',category:'online',statement:'Original statement.',definitions:'Original definitions.',answer:'Original resolution target.',why:'Original motivation.',sources:'https://example.org/original'}}));
    },targetId);
    const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));await page.goto(base+'#'+targetId);await page.waitForFunction(()=>window.ATLAS_DEBUG&&ATLAS_COMMUNITY.loadedAt);
    assert.equal(legacyReads,0);assert(await page.locator('[data-public-note]').count()>0);assert(await page.locator('#community').isHidden());
    for(const sentinel of ['PRIVATE TEXT','CACHED INTERNAL FEEDBACK','GITHUB INTERNAL FEEDBACK','OLD PRIVATE DRAFT'])assert(!(await page.locator('body').innerText()).includes(sentinel));
    assert(catalog.cards.every(c=>!Object.hasOwn(c,'community_reviews')));
    const card=page.locator('#'+targetId);
    await card.locator('[data-public-note]').click();
    assert.equal(await page.locator('#public-note-text').inputValue(),'','Legacy drafts must never prefill a public comment');
    const postedText='Public comment: řetězec <img src=x onerror="window.commentXSS=1">';
    await page.locator('#public-note-text').fill(postedText);await page.locator('#public-note-author').fill('Test visitor');
    await page.locator('#close-contribution').click();await card.locator('[data-public-note]').click();
    assert.equal(await page.locator('#public-note-text').inputValue(),postedText,'New public drafts survive closing');
    lost=true;await page.locator('#submit-contribution').click();
    await page.waitForFunction(()=>document.getElementById('contribution-result').textContent.includes('Retry'));
    assert.equal(await page.locator('#public-note-text').inputValue(),postedText);
    await page.locator('#submit-contribution').click();await page.waitForFunction(()=>!document.getElementById('contribution-dialog').open);
    assert.equal(posts.length,2);assert.deepEqual(posts[0],posts[1],'A lost response retries the identical submission');
    assert.equal(await card.locator('.public-note').count(),1);assert.equal(await card.locator('.public-note-text').innerText(),postedText);
    assert.equal(await card.locator('.public-note img').count(),0);assert.equal(await page.evaluate(()=>window.commentXSS),undefined);
    assert(await card.locator('.community-thread').evaluate(el=>el.open));
    const other=await browser.newContext();await routes(other);const visitor=await other.newPage();
    await visitor.goto(base+'#'+targetId);await visitor.waitForFunction(()=>window.ATLAS_DEBUG&&ATLAS_COMMUNITY.loadedAt);
    assert.equal(await visitor.locator('#'+targetId+' .public-note').count(),1);assert.equal(await visitor.locator('[data-delete-note]').count(),0);
    await page.reload();await page.waitForFunction(()=>window.ATLAS_DEBUG&&ATLAS_COMMUNITY.loadedAt);
    assert.equal(await card.locator('.public-note').count(),1);assert.equal(await card.locator('[data-delete-note]').count(),1);
    for(const view of ['compact','full']){
      await page.locator('#view').selectOption(view);await page.evaluate(id=>ATLAS_DEBUG.go(id),targetId);
      assert(await card.locator('[data-public-note]').isVisible());
      await card.locator('.community-thread').evaluate(el=>el.open=true);
      for(const width of [320,390,1440]){await page.setViewportSize({width,height:1000});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'No comment overflow at '+width);}
    }
    await page.evaluate(async id=>{
      const api=ATLAS_DEBUG,c=api.data.cards.find(c=>c.id===id);
      await api.applyPublication({version:api.data.meta.version,cards:[{...c,title:c.title+' [publication test]'}],meta:api.data.meta,areas:api.data.areas});
    },targetId);
    assert(await card.locator('.community-thread').evaluate(el=>el.open),'Open comment thread survives publication');
    offline=true;await page.evaluate(()=>ATLAS_COMMUNITY.refresh(true));
    assert.match(await card.locator('.comment-status').innerText(),/unavailable/);assert.equal(await card.locator('.public-note').count(),1);
    offline=false;await page.evaluate(()=>ATLAS_COMMUNITY.refresh(true));
    page.once('dialog',dialog=>dialog.accept());await card.locator('[data-delete-note]').click();
    await page.waitForFunction(id=>!document.querySelector('#'+id+' .public-note'),targetId);
    await visitor.evaluate(()=>ATLAS_COMMUNITY.refresh(true));assert.equal(await visitor.locator('.public-note').count(),0);await other.close();
    assert.equal(legacyReads,0);
    await page.locator('#new-problem').click();
    assert.equal(await page.locator('#problem-fields input,#problem-fields select,#problem-fields textarea').count(),4);
    assert.equal(await page.locator('#proposal-category option').count(),36);
    const text=await page.locator('#proposal-statement').inputValue();
    for(const expected of ['Original statement.','Original definitions.','Original resolution target.','Original motivation.'])assert(text.includes(expected));
    await page.locator('#proposal-title').fill('Updated question');await page.locator('#close-contribution').click();await page.locator('#new-problem').click();
    assert.equal(await page.locator('#proposal-statement').inputValue(),text,'Migration must not duplicate optional fields');
    const popup=page.waitForEvent('popup');await page.locator('#submit-contribution').click();const submitted=await popup;await submitted.waitForLoadState();
    const url=new URL(submitted.url());assert.equal(url.searchParams.get('title'),'[Problem] Updated question');
    for(const expected of ['Original statement.','Original definitions.','Original resolution target.','Original motivation.'])assert(url.searchParams.get('body').includes(expected));
    assert(!url.searchParams.get('body').includes('PRIVATE TEXT'));await submitted.close();
    assert(await page.locator('#refresh-after-submission').isHidden());
    await page.reload();await page.waitForFunction(()=>window.ATLAS_DEBUG);await page.locator('#new-problem').click();
    assert.equal(await page.locator('#proposal-title').inputValue(),'Updated question');
    assert.equal(await page.locator('#proposal-statement').inputValue(),text);
    assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('tcs-atlas-notes'))['TCS-6575']),'PRIVATE TEXT — must not be shared');
    assert.equal(errors.length,0,errors.join('\n'));
    console.log(JSON.stringify({checks:['no legacy feedback reads or cache imports','new comment drafts isolated','shared comments across visitors','lost-response retry without duplication','author deletion','HTML escaping','both layouts at 320–1440px','open comments survive publication','outage preserves comments and drafts','feedback excluded from published catalogue','private notes preserved locally','legacy problem draft migrated without loss','35 current categories in proposal form','GitHub prefill preserves sources and fields','submitted draft remains editable'],errors}));
  }finally{await browser.close();db.close();await new Promise(resolve=>server.close(resolve));}
})().catch(error=>{console.error(error);process.exitCode=1;});
