const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const http=require('node:http');

(async()=>{
  const {default:worker}=await import('../services/notes/worker.mjs');
  const {database}=await import('../services/notes/test/sqlite.mjs');
  const db=database(),root=path.resolve(__dirname,'../build');
  const server=http.createServer((req,res)=>{
    const file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));
    const target=file===root?path.join(root,'index.html'):file;
    if(!target.startsWith(root+path.sep)||!fs.existsSync(target)){res.writeHead(404);res.end();return;}
    res.setHeader('content-type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json'})[path.extname(target)]||'application/octet-stream');fs.createReadStream(target).pipe(res);
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base=`http://127.0.0.1:${server.address().port}/`,errors=[],posts=[];
  const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  let loseResponse=false,unavailable=false;
  async function routes(context){
    await context.route('https://api.github.com/**',route=>route.fulfill({json:[]}));
    await context.route('https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/notes**',route=>route.fulfill({json:{notes:[],next:null}}));
    await context.route('**/version.json',route=>route.fulfill({json:{version:JSON.parse(fs.readFileSync(root+'/version.json')).version}}));
    await context.route('https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/votes',async route=>{
      if(unavailable)return route.fulfill({status:503,json:{error:'Offline for test.'}});
      const req=route.request();
      const response=await worker.fetch(new Request(req.url(),{method:req.method(),headers:req.headers(),...(req.postData()?{body:req.postData()}:{} )}),{DB:db,NOTES_ALLOWED_ORIGINS:new URL(base).origin});
      if(req.method()==='POST'){
        posts.push(req.postDataJSON());
        if(loseResponse){loseResponse=false;return route.fulfill({status:503,json:{error:'Response lost after saving.'}});}
      }
      await route.fulfill({status:response.status,headers:Object.fromEntries(response.headers),body:await response.text()});
    });
  }
  const ready=page=>page.waitForFunction(()=>window.ATLAS_DEBUG&&window.ATLAS_VOTES?.loaded);
  const own=(page,id,value)=>page.waitForFunction(({id,value})=>ATLAS_VOTES.own.find(v=>v.problem_id===id)?.value===value,{id,value});
  async function click(page,id,direction){
    await page.waitForTimeout(550);await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
    await page.locator(`#${id} [data-vote="${direction}"]`).click();
  }
  try{
    const context=await browser.newContext({viewport:{width:1440,height:1000}});await routes(context);
    const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));await page.goto(base);await ready(page);
    const fixture=await page.evaluate(()=>{
      const d=ATLAS_DEBUG.data,area=d.areas.find(a=>a.group==='large'&&ATLAS_DEBUG.state.matches.filter(c=>c.area===a.area).length>30);
      const ordered=ATLAS_DEBUG.state.matches.filter(c=>c.area===area.area);
      return {area:area.area,original:ordered.map(c=>c.id),id:ordered[30].id};
    });
    const {id}=fixture;
    await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
    await page.locator(`#${id} .card-details`).evaluate(el=>el.open=true);
    await page.locator(`#${id} [data-vote="1"]`).dblclick();await own(page,id,1);
    await page.waitForFunction(({id,area})=>ATLAS_DEBUG.state.matches.find(c=>c.area===area)?.id===id,{id,area:fixture.area});
    assert.equal(posts.length,1,'Double-click neither duplicates nor cancels a vote');
    assert(await page.locator(`#${id} .card-details`).evaluate(el=>el.open),'Voting preserves open details');
    assert.equal(await page.locator(`#${id} [data-vote="1"]`).getAttribute('aria-pressed'),'true');
    await page.locator('#benchmark').selectOption('top100');
    assert(await page.evaluate(id=>ATLAS_DEBUG.state.matches.some(c=>c.id===id),id),'Voting promotes a previously unselected problem into Top 100');
    const top100=await page.evaluate(()=>ATLAS_DEBUG.state.matches.map(c=>c.id));
    await page.locator('#benchmark').selectOption('top500');
    const top500=await page.evaluate(()=>ATLAS_DEBUG.state.matches.map(c=>c.id));
    assert(top100.every(id=>top500.includes(id)),'Top 100 stays within Top 500');
    assert(await page.evaluate(()=>{
      const d=ATLAS_DEBUG.data,order=new Map(d.areas.map((a,i)=>[a.area,i]));
      return ATLAS_DEBUG.state.matches.every((c,i,list)=>!i||order.get(list[i-1].area)<=order.get(c.area));
    }),'Votes do not move a problem outside its category');
    await page.locator('#search').fill(id);
    // Full-text search can also match cards that mention the voted problem.
    await page.waitForFunction(({id,total})=>ATLAS_DEBUG.state.matches.length<total&&ATLAS_DEBUG.state.matches.some(c=>c.id===id),{id,total:top500.length});
    const searched=await page.evaluate(()=>ATLAS_DEBUG.state.matches.map(c=>c.id));
    assert(searched.includes(id),'Search retains the problem promoted by voting');
    assert(searched.every(match=>top500.includes(match)),'Search filters the selected benchmark without backfilling it');
    await page.locator('#search').fill('');await page.locator('#benchmark').selectOption('');
    await page.reload();await ready(page);await own(page,id,1);
    const token=await page.evaluate(()=>localStorage.getItem('tcs-atlas-voter-v1'));
    const visitor=await browser.newContext();await routes(visitor);const fresh=await visitor.newPage();fresh.on('pageerror',e=>errors.push(e.message));
    await fresh.goto(base+'#'+id);await ready(fresh);
    assert.notEqual(await fresh.evaluate(()=>localStorage.getItem('tcs-atlas-voter-v1')),token);
    assert.equal(await fresh.locator(`#${id} [data-vote="1"] .vote-count`).innerText(),'1');
    assert.equal(await fresh.locator(`#${id} [data-vote="1"]`).getAttribute('aria-pressed'),'false');
    await click(fresh,id,-1);await own(fresh,id,-1);
    await page.bringToFront();await page.evaluate(()=>ATLAS_VOTES.refresh());
    await page.waitForFunction(id=>ATLAS_VOTES.score(id)===0,id);
    await page.waitForFunction(({area,original})=>JSON.stringify(ATLAS_DEBUG.state.matches.filter(c=>c.area===area).map(c=>c.id))===JSON.stringify(original),fixture);
    assert.deepEqual(await page.evaluate(area=>ATLAS_DEBUG.state.matches.filter(c=>c.area===area).map(c=>c.id),fixture.area),fixture.original,'Equal vote scores restore the original catalogue priority');
    await page.locator('#benchmark').selectOption('top100');
    assert(!await page.evaluate(id=>ATLAS_DEBUG.state.matches.some(c=>c.id===id),id),'Changed votes update selection membership');
    await page.locator('#benchmark').selectOption('');
    await click(page,id,-1);await own(page,id,-1);
    assert.equal(await page.evaluate(id=>ATLAS_VOTES.score(id),id),-2,'Switching replaces the existing vote');
    await click(page,id,-1);await own(page,id,0);
    assert.equal(await page.evaluate(id=>ATLAS_VOTES.score(id),id),-1,'Clicking the selected thumb cancels it');
    loseResponse=true;await click(page,id,1);
    await page.locator(`#${id} [data-vote-retry]`).waitFor();
    await page.waitForTimeout(550);await page.locator(`#${id} [data-vote-retry]`).click();await own(page,id,1);
    assert.deepEqual(posts.at(-1),posts.at(-2),'Lost responses retry the identical request');
    assert.equal(await page.evaluate(id=>ATLAS_VOTES.score(id),id),0,'Retry does not add another vote');
    const tab=await context.newPage();await tab.goto(base+'#'+id);await ready(tab);await own(tab,id,1);
    await click(tab,id,-1);await own(tab,id,-1);
    await page.bringToFront();await page.evaluate(()=>ATLAS_VOTES.refresh());await own(page,id,-1);
    await page.locator('#view').selectOption('full');await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
    assert.equal(await page.locator(`#${id} [data-vote="-1"]`).getAttribute('aria-pressed'),'true');
    unavailable=true;await page.evaluate(()=>ATLAS_VOTES.refresh());
    assert((await page.locator('#voting-status').innerText()).includes('last loaded counts'));
    assert.equal(await page.evaluate(id=>ATLAS_VOTES.score(id),id),-2,'Outages preserve the last known score');unavailable=false;
    const artifact=fs.mkdtempSync(path.join(os.tmpdir(),'atlas-voting-'));
    await page.locator('#view').selectOption('compact');await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
    await page.screenshot({path:artifact+'/desktop.png'});
    await page.setViewportSize({width:390,height:844});await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await page.screenshot({path:artifact+'/mobile.png'});
    const blocked=await browser.newContext();await routes(blocked);
    await blocked.addInitScript(()=>{Storage.prototype.setItem=()=>{throw new Error('Storage blocked');};});
    const noStorage=await blocked.newPage();await noStorage.goto(base+'#'+id);await ready(noStorage);
    assert(await noStorage.locator(`#${id} [data-vote="1"]`).isDisabled());
    assert((await noStorage.locator(`#${id} .vote-status`).innerText()).includes('storage'));
    assert.equal(errors.length,0,errors.join('\n'));
    console.log(JSON.stringify({checks:['durable browser identity','double-click safety','shared counts between visitors','one vote with switching and cancellation','lost-response retry','same-browser tabs','score-first category ranking','vote-driven Top 100 and Top 500 with fixed quotas','editorial tie-break','search after selection','Compact and Full controls','outage and storage failures','mobile layout'],errors}));
  }finally{await browser.close();await new Promise(resolve=>server.close(resolve));db.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
