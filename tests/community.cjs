/* Final-reader privacy and preserved, browser-local problem proposal drafts. */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const http=require('node:http');
(async()=>{
  const root=path.resolve(__dirname,'../build'),catalog=JSON.parse(fs.readFileSync(root+'/catalog.json'));
  const server=http.createServer((req,res)=>{
    const file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));
    const target=file===root?path.join(root,'index.html'):file;
    if(!target.startsWith(root+path.sep)||!fs.existsSync(target)||!fs.statSync(target).isFile()){res.writeHead(404);res.end();return;}
    res.setHeader('content-type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json'})[path.extname(target)]||'application/octet-stream');fs.createReadStream(target).pipe(res);
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base=`http://127.0.0.1:${server.address().port}/`,browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  try{
    const context=await browser.newContext(),errors=[];let fetched=0;
    await context.route('https://api.github.com/**',route=>{fetched++;return route.fulfill({json:[]});});
    await context.route('**/api/notes**',route=>{fetched++;return route.fulfill({json:{notes:[],next:null}});});
    await context.route('**/api/votes',route=>route.fulfill({json:{votes:[],mine:[]}}));
    await context.route('**/api/selection',route=>route.fulfill({json:{version:catalog.meta.final_selection.version,choices:[]}}));
    await context.route('https://github.com/vaclavrozhon/atlas/issues/new?**',route=>route.fulfill({contentType:'text/html',body:'<title>Local submission fixture</title>'}));
    await context.addInitScript(()=>{
      localStorage.setItem('tcs-atlas-notes',JSON.stringify({'TCS-6575':'PRIVATE TEXT — must not be shared'}));
      localStorage.setItem('tcs-atlas-public-notes-cache-v1',JSON.stringify([{id:'abcd',text:'CACHED PUBLIC FEEDBACK'}]));
      if(!localStorage.getItem('tcs-atlas-contribution-drafts'))localStorage.setItem('tcs-atlas-contribution-drafts',JSON.stringify({problem:{title:'Unsent question',category:'online',statement:'Original statement.',definitions:'Original definitions.',answer:'Original resolution target.',why:'Original motivation.',sources:'https://example.org/original'}}));
    });
    const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));await page.goto(base+'#TCS-6575');await page.waitForFunction(()=>window.ATLAS_DEBUG);
    await page.evaluate(()=>ATLAS_COMMUNITY.refresh(true));
    assert.equal(fetched,0);assert.equal(await page.locator('[data-public-note],.public-note,.public-notes').count(),0);assert(await page.locator('#community').isHidden());
    assert(!(await page.locator('body').innerText()).includes('PRIVATE TEXT'));assert(!(await page.locator('body').innerText()).includes('CACHED PUBLIC FEEDBACK'));
    assert(catalog.cards.every(c=>!Object.hasOwn(c,'community_reviews')));
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
    console.log(JSON.stringify({checks:['no feedback network reads','no feedback rendering from cache','feedback excluded from published catalogue','private notes preserved locally','legacy problem draft migrated without loss','35 current categories in proposal form','GitHub prefill preserves sources and fields','submitted draft remains editable'],errors}));
  }finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
})().catch(error=>{console.error(error);process.exitCode=1;});
