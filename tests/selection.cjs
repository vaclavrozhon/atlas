const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const http=require('node:http');

(async()=>{
  const {default:worker}=await import('../services/notes/worker.mjs');
  const {database}=await import('../services/notes/test/sqlite.mjs');
  const {selectionManifest:manifest}=await import('../services/notes/selection-manifest.mjs');
  const initialGreens=Object.values(manifest.cards).filter(c=>c.color==='green').length;
  const initialReds=Object.keys(manifest.cards).length-initialGreens;
  const areaGreens=area=>Object.values(manifest.cards).filter(c=>c.color==='green'&&c.area===area).length;
  const target=area=>manifest.targets[manifest.categories[area].group];
  const db=database(),root=path.resolve(__dirname,'../build'),errors=[],posts=[];
  const server=http.createServer((req,res)=>{
    const file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));
    const target=file===root?path.join(root,'index.html'):file;
    if(!target.startsWith(root+path.sep)||!fs.existsSync(target)||!fs.statSync(target).isFile()){res.writeHead(404);res.end();return;}
    res.setHeader('content-type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json'})[path.extname(target)]||'application/octet-stream');fs.createReadStream(target).pipe(res);
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base=`http://127.0.0.1:${server.address().port}/`,env={DB:db,NOTES_ALLOWED_ORIGINS:new URL(base).origin};
  const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  let lost=false,offline=false,pauseReads=false,legacyMismatch=false,feedbackRequests=0;
  async function routes(context){
    await context.route('https://api.github.com/**',route=>{feedbackRequests++;return route.fulfill({json:[]});});
    await context.route('**/api/notes**',route=>{feedbackRequests++;return route.fulfill({json:{notes:[],next:null}});});
    await context.route('**/api/votes',route=>route.fulfill({json:{votes:[],mine:[]}}));
    await context.route('**/version.json',route=>route.fulfill({json:{version:JSON.parse(fs.readFileSync(root+'/version.json')).version}}));
    await context.route('**/api/selection**',async route=>{
      if(offline||(pauseReads&&route.request().method()==='GET'))return route.fulfill({status:503,json:{error:'Offline fixture'}});
      const req=route.request();
      assert.equal(req.headers().authorization,undefined,'Selection requests need no credentials');
      assert(!req.url().endsWith('/auth'),'The reader does not ask to authenticate');
      if(req.method()==='POST'&&legacyMismatch){
        legacyMismatch=false;manifest.version='legacy-service-rollout';posts.push(req.postDataJSON());
        return route.fulfill({status:409,json:{error:'The catalogue has changed.',version:manifest.version}});
      }
      const response=await worker.fetch(new Request(req.url(),{method:req.method(),headers:req.headers(),...(req.postData()?{body:req.postData()}:{} )}),env);
      if(req.method()==='POST'&&!req.url().endsWith('/auth')){
        posts.push(req.postDataJSON());
        if(lost){lost=false;return route.fulfill({status:503,json:{error:'Response lost after save'}});}
      }
      return route.fulfill({status:response.status,headers:Object.fromEntries(response.headers),body:await response.text()});
    });
  }
  const ready=p=>p.waitForFunction(()=>window.ATLAS_DEBUG&&window.ATLAS_SELECTION?.loaded);
  const revision=async(p,id,n)=>{
    await p.waitForFunction(({id,n})=>ATLAS_SELECTION.choice(id).revision===n,{id,n});
    // The reader refreshes category counts on the next animation frame.
    await p.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
  };
  async function click(p,id,action){
    await p.bringToFront();await p.evaluate(id=>ATLAS_DEBUG.go(id),id);
    await p.locator(`#${id} [data-selection-action="${action}"]`).click();
  }
  const greenCount=p=>p.evaluate(()=>TCS_ATLAS.cards.filter(c=>ATLAS_SELECTION.color(c)==='green').length);
  try{
    const owner=await browser.newContext({viewport:{width:1440,height:1000}});await routes(owner);
    await owner.addInitScript(()=>sessionStorage.setItem('tcs-atlas-selection-editor-v1','obsolete-editor-key'));
    const page=await owner.newPage();page.on('pageerror',e=>errors.push(e.message));await page.goto(base);await ready(page);
    assert.equal(await greenCount(page),initialGreens);
    assert.equal(await page.locator('#areas .count').count(),35);
    assert.equal(await page.locator('#selection-total').innerText(),`${initialGreens} green / target 500`);
    assert.equal(await page.locator('[data-selection-action="color"]').count(),await page.locator('.problem-card').count(),'Every card immediately offers a color change');
    assert.equal(await page.locator('[data-public-note],.public-notes').count(),0);
    assert(await page.locator('#community').isHidden());assert.equal(feedbackRequests,0);
    assert(await page.evaluate(()=>TCS_ATLAS.cards.every(c=>c.selection&&['green','red'].includes(c.selection.color))));
    await page.locator('#selection-filter').selectOption('green');
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),initialGreens);
    assert((await page.locator('.problem-card').first().getAttribute('class')).includes('selection-green'));
    await page.locator('#selection-filter').selectOption('red');
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),initialReds);
    await page.evaluate(()=>ATLAS_DEBUG.go('TCS-6168'));
    assert((await page.locator('#TCS-6168 .selection-exception').innerText()).includes('TCS-4786'));
    await page.locator('#clear').click();
    const [id,initial]=Object.entries(manifest.cards).find(([,c])=>c.color==='green'&&c.area_options.length===2&&manifest.categories[c.area].group==='small');
    await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
    assert.equal(await page.locator('#edit-selection,#selection-login').count(),0,'No edit mode or login dialog');
    assert.equal(await page.evaluate(()=>sessionStorage.getItem('tcs-atlas-selection-editor-v1')),null,'Obsolete editor credentials are removed');
    await click(page,id,'color');await revision(page,id,1);
    assert.equal(await greenCount(page),initialGreens-1);assert((await page.locator(`#${id}`).getAttribute('class')).includes('selection-red'));
    assert.equal(await page.locator(`#areas input[value="${initial.area}"]`).locator('..').locator('.count').innerText(),`${areaGreens(initial.area)-1} / ${target(initial.area)}`);
    await click(page,id,'move');await revision(page,id,2);
    assert.equal(await page.evaluate(id=>ATLAS_SELECTION.color(TCS_ATLAS.cards.find(c=>c.id===id)),id),'red');
    assert.equal(await page.evaluate(id=>TCS_ATLAS.cards.find(c=>c.id===id).area,id),initial.area_options[1]);
    assert.equal(await page.locator(`#${id} .card-area`).innerText(),manifest.categories[initial.area_options[1]].label);
    await click(page,id,'color');await revision(page,id,3);
    assert.equal(await page.locator(`#areas input[value="${initial.area_options[1]}"]`).locator('..').locator('.count').innerText(),`${areaGreens(initial.area_options[1])+1} / ${target(initial.area_options[1])}`);
    assert.equal(await greenCount(page),initialGreens);
    await page.reload();await ready(page);
    await revision(page,id,3);
    const visitor=await browser.newContext();await routes(visitor);const fresh=await visitor.newPage();fresh.on('pageerror',e=>errors.push(e.message));
    await fresh.goto(base+'#'+id);await ready(fresh);await revision(fresh,id,3);
    assert.equal(await fresh.evaluate(id=>TCS_ATLAS.cards.find(c=>c.id===id).area,id),initial.area_options[1]);
    assert(await fresh.locator(`#${id} [data-selection-action="color"]`).isEnabled(),'An independent visitor can edit without signing in');
    const map=await visitor.newPage();map.on('pageerror',e=>errors.push(e.message));
    await map.goto(base+'map.html');await map.waitForFunction(()=>window.ATLAS_MAP?.ready);
    await map.evaluate(()=>ATLAS_MAP.refreshSelection());
    await map.waitForFunction(({id,area})=>ATLAS_MAP.nodes.find(n=>n.id===id)?.card.area===area,{id,area:initial.area_options[1]});
    await map.evaluate(id=>ATLAS_MAP.focusProblem(id),id);
    assert.equal(await map.locator('#map-preview-selection').innerText(),'Green · selected');
    await map.close();await fresh.bringToFront();
    // Another editor changes the card after this reader's last refresh.
    const newer={problem_id:id,color:'red',area:initial.area_options[1],revision:4,version:manifest.version};
    const response=await worker.fetch(new Request('https://notes.example/api/selection',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(newer)}),env);
    assert.equal(response.status,200);
    await click(fresh,id,'move');await revision(fresh,id,4);
    assert.equal(await fresh.evaluate(id=>ATLAS_SELECTION.choice(id).area,id),initial.area_options[1]);
    assert((await fresh.locator(`#${id} .selection-card-status`).innerText()).includes('another editor'));
    pauseReads=true;lost=true;await click(fresh,id,'color');await fresh.locator(`#${id} [data-selection-action="retry"]`).waitFor();
    manifest.version='service-published-after-lost-response';
    await click(fresh,id,'retry');await revision(fresh,id,5);
    assert.deepEqual(posts.at(-1),posts.at(-2),'Retry across a service publication is the exact same edit');pauseReads=false;
    await page.bringToFront();await page.evaluate(()=>ATLAS_SELECTION.refresh());await revision(page,id,5);
    await page.evaluate(async id=>{
      const copy=JSON.parse(JSON.stringify(TCS_ATLAS));
      copy.cards.find(c=>c.id===id).selection.color='red';
      copy.meta.final_selection.version='reader-published-before-service';
      await ATLAS_DEBUG.applyPublication({...copy,version:copy.meta.version,snapshot:true});
    },id);
    assert.equal(await page.evaluate(id=>ATLAS_SELECTION.choice(id).color,id),'green','Publication does not overwrite a manual choice');
    assert.equal(await page.evaluate(id=>TCS_ATLAS.cards.find(c=>c.id===id).area,id),initial.area_options[1]);
    await page.evaluate(()=>ATLAS_SELECTION.refresh());
    assert(await page.locator(`#${id} [data-selection-action="color"]`).isEnabled(),'Version skew must not disable editing');
    await click(page,id,'color');await revision(page,id,6);
    legacyMismatch=true;await click(page,id,'color');await revision(page,id,7);
    const {version:beforeVersion,...beforeEdit}=posts.at(-2),{version:afterVersion,...afterEdit}=posts.at(-1);
    assert.notEqual(beforeVersion,afterVersion);assert.deepEqual(beforeEdit,afterEdit,'An older service gets one version-only retry');
    const during=await browser.newContext();await routes(during);const duringPage=await during.newPage();
    duringPage.on('pageerror',e=>errors.push(e.message));await duringPage.goto(base+'#'+id);await ready(duringPage);await revision(duringPage,id,7);
    assert(await duringPage.locator(`#${id} [data-selection-action="color"]`).isEnabled(),'A new visitor can edit while versions differ');
    const duringMap=await during.newPage();duringMap.on('pageerror',e=>errors.push(e.message));await duringMap.goto(base+'map.html');
    await duringMap.waitForFunction(()=>window.ATLAS_MAP?.ready);await duringMap.evaluate(()=>ATLAS_MAP.refreshSelection());
    await duringMap.waitForFunction(({id,area})=>ATLAS_MAP.nodes.find(n=>n.id===id)?.card.area===area,{id,area:initial.area_options[1]});
    await duringMap.evaluate(id=>ATLAS_MAP.focusProblem(id),id);
    assert.equal(await duringMap.locator('#map-preview-selection').innerText(),'Green · selected');
    await during.close();await page.bringToFront();
    await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
    await page.locator('#view').selectOption('full');await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
    assert(await page.locator(`#${id} [data-selection-action="move"]`).count());
    await page.locator('#view').selectOption('compact');await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
    const artifact=process.env.ATLAS_TEST_ARTIFACT_DIR||path.resolve(__dirname,'../research/public-selection-20261105/ui');fs.mkdirSync(artifact,{recursive:true});
    await page.screenshot({path:artifact+'/desktop.png'});
    for(const width of [320,390,768,1440]){
      await page.setViewportSize({width,height:844});await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
      assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`Overflow at ${width}`);
      if(width===390)await page.screenshot({path:artifact+'/mobile.png'});
    }
    offline=true;await page.evaluate(()=>ATLAS_SELECTION.refresh());
    assert((await page.locator('#selection-status').innerText()).includes('last loaded'));
    assert.equal(await page.evaluate(id=>ATLAS_SELECTION.choice(id).color,id),'green');offline=false;
    assert(await page.locator(`#${id} [data-selection-action="color"]`).isEnabled());
    assert.equal(await page.evaluate(()=>sessionStorage.getItem('tcs-atlas-selection-editor-v1')),null);
    assert.equal(errors.length,0,errors.join('\n'));
    const report={initialGreens,initialReds,checks:['complete green/red proposal','current green count and 35 category counters','all/green/red filters','upvoted red explanation','immediate anonymous editing without login or editor mode','shared color and two-way category edits','quota deviations','reload persistence','independent visitors','stale edit conflict','lost-response retry across publication','manual choice survives publication','reader/service version skew','older service retries without changing edit intent','new visitor and map during publication','map shows shared colors and category moves','full and compact controls','320–1440px layout','outage preservation','feedback not loaded or rendered'],errors};
    fs.writeFileSync(artifact+'/checks.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
  }finally{await browser.close();await new Promise(resolve=>server.close(resolve));db.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
