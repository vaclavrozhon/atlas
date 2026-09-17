const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const http=require('node:http');
const path=require('node:path');

(async()=>{
  const site=path.resolve(__dirname,'../build');
  let server,browser;
  try{
    let base=process.argv[2];
    if(!base){
      const mime={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.woff2':'font/woff2','.woff':'font/woff','.ttf':'font/ttf'};
      server=http.createServer((request,response)=>{
        const pathname=new URL(request.url,'http://localhost').pathname;
        const name=decodeURIComponent(pathname.slice('/atlas/'.length))||'index.html';
        const file=path.resolve(site,name);
        if(!pathname.startsWith('/atlas/')||!file.startsWith(site+path.sep)||!fs.existsSync(file)||!fs.statSync(file).isFile()){
          response.writeHead(404);response.end();return;
        }
        response.writeHead(200,{'content-type':mime[path.extname(file)]||'text/plain'});
        fs.createReadStream(file).pipe(response);
      });
      await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
      base=`http://127.0.0.1:${server.address().port}/atlas/`;
    }
    browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
    const page=await browser.newPage({viewport:{width:1440,height:1000},acceptDownloads:true});
    await page.route('https://api.github.com/**', route=>route.fulfill({json:[]}));
    await page.route('https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/notes**', route=>route.fulfill({json:{notes:[],next:null}}));
    await page.route('https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/votes', route=>route.fulfill({json:{votes:[],mine:[]}}));
    const errors=[],failures=[];
    page.on('pageerror',error=>errors.push(error.message));
    page.on('response',response=>{if(response.status()>=400)failures.push(`${response.status()} ${response.url()}`);});
    const initialSelection=await (await page.request.get(base+'top100.json')).json();
    const testId=initialSelection.cards[0].id;
    await page.goto(base+'?benchmark=top100#'+testId);
    await page.waitForFunction(()=>window.ATLAS_DEBUG);
    assert.equal(await page.locator('#benchmark').inputValue(),'top100');
    const data=await page.evaluate(()=>({version:ATLAS_DEBUG.data.meta.version,total:ATLAS_DEBUG.data.meta.benchmarks.top100.total,categories:ATLAS_DEBUG.data.areas.length}));
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),data.total);
    assert(await page.locator('#'+testId).count());
    assert(await page.evaluate(()=>typeof ATLAS_COMMUNITY?.refresh==='function'));
    await page.locator('#'+testId+' [data-public-note]').click();
    assert(await page.locator('#contribution-dialog').isVisible());
    assert((await page.locator('#contribution-target').innerText()).startsWith(testId));
    await page.locator('#close-contribution').click();
    await page.locator('#new-problem').click();
    assert.equal(await page.locator('#proposal-category option').count(),data.categories+1);
    await page.locator('#close-contribution').click();
    for(const name of ['version.json','top100.json','top500.json','top1000.json','benchmark-selection.md','community.js','.nojekyll']){
      const response=await page.request.get(base+name);assert.equal(response.status(),200,name);
    }
    const selections={};
    const categoryOrder=await page.locator('#areas input').evaluateAll(inputs=>inputs.map(input=>input.value));
    for(const name of ['top100','top500','top1000']){
      await page.locator('#benchmark').selectOption(name);
      const exported=await (await page.request.get(base+name+'.json')).json();
      selections[name]=await page.evaluate(()=>ATLAS_DEBUG.state.matches.map(c=>c.id));
      assert.deepEqual(new Set(selections[name]),new Set(exported.cards.map(c=>c.id)));
      for(const area of exported.areas){
        const ordered=exported.cards.filter(c=>c.area===area.area).map(c=>c.id),ids=new Set(ordered);
        assert.deepEqual(selections[name].filter(id=>ids.has(id)),ordered);
      }
      assert.deepEqual(await page.locator('#areas input').evaluateAll(inputs=>inputs.map(input=>input.value)),categoryOrder);
    }
    for(const [small,large] of [['top100','top500'],['top500','top1000']]){
      const ids=new Set(selections[small]);
      assert.deepEqual(selections[large].filter(id=>ids.has(id)),selections[small]);
    }
    await page.locator('#benchmark').selectOption('top500');
    await page.reload();await page.waitForFunction(()=>window.ATLAS_DEBUG);
    assert.equal(await page.locator('#benchmark').inputValue(),'top500');
    assert.deepEqual(await page.evaluate(()=>ATLAS_DEBUG.state.matches.map(c=>c.id)),selections.top500);
    await page.locator('#areas input').first().check();
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),25);
    const outside=await page.evaluate(()=>ATLAS_DEBUG.data.cards.find(c=>c.area===ATLAS_DEBUG.data.areas[0].area&&c.importance_rank===26)?.id);
    if(outside){await page.locator('#search').fill(outside);await page.waitForFunction(()=>ATLAS_DEBUG.state.matches.length===0);}
    await page.locator('#clear').click();
    await page.locator('#benchmark').selectOption('top500');
    const smallIndex=await page.evaluate(()=>ATLAS_DEBUG.data.areas.findIndex(a=>a.group==='small'&&a.count>=10));
    await page.locator('#areas input').nth(smallIndex).check();
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),10);
    await page.locator('#clear').click();
    await page.locator('#benchmark').selectOption('top100');
    assert.match(await page.locator('#benchmark-goal').textContent(), /primary goal is a benchmark of 500 problems.*Top 100 is a priority subset/);
    assert((await page.locator('#selection-plan').textContent()).includes('thumbs up minus thumbs down determines both order and selection'));
    assert.equal(await page.locator('#coverage-table thead th').count(),5);
    assert.equal(await page.locator('#export,#export-community,#live-status,#sort').count(),0);
    assert.equal(await page.locator('#problem-fields input,#problem-fields select,#problem-fields textarea').count(),4);
    await page.locator('#view').selectOption('full');
    assert.equal(await page.locator('.compact-card').count(),0);
    await page.locator('#view').selectOption('compact');
    // Related links navigate across filters and pagination, in both card layouts.
    // Editorial pruning may leave no related pair. Supply a browser-only fixture
    // so navigation coverage does not constrain which problems we retain.
    const relatedFixture=await page.evaluate(async()=>{
      const api=ATLAS_DEBUG,first=api.state.matches[0];
      const second=api.state.matches.find(c=>c.area!==first.area);
      const originals=structuredClone([first,second]);
      const cards=originals.map((c,i)=>({...c,related_problem_ids:[originals[1-i].id]}));
      await api.applyPublication({version:api.data.meta.version,cards,meta:api.data.meta,areas:api.data.areas});
      return {pair:cards.map(c=>c.id),originals};
    });
    const relatedPair=relatedFixture.pair;
    for(const view of ['compact','full']){
      await page.locator('#view').selectOption(view);
      await page.locator('#search').fill(relatedPair[0]);
      await page.waitForFunction(id=>ATLAS_DEBUG.state.matches.length===1&&ATLAS_DEBUG.state.matches[0].id===id,relatedPair[0]);
      const target=page.locator(`#${relatedPair[0]} .related-problem-link[href="#${relatedPair[1]}"]`);
      if(!await target.isVisible())await page.locator(`#${relatedPair[0]} .related-more`).evaluate(el=>el.open=true);
      await target.click();
      await page.waitForFunction(id=>location.hash==='#'+id&&document.getElementById(id),relatedPair[1]);
      assert.equal(await page.locator('#search').inputValue(),'');
      assert.equal(await page.locator(`#${relatedPair[1]} .related-problem-link[href="#${relatedPair[0]}"]`).count(),1);
    }
    await page.evaluate(async cards=>{
      const api=ATLAS_DEBUG;
      await api.applyPublication({version:api.data.meta.version,cards,meta:api.data.meta,areas:api.data.areas});
    },relatedFixture.originals);
    await page.locator('#view').selectOption('compact');
    await page.setViewportSize({width:390,height:844});
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    // A reader that missed the previous delta fetches the authoritative catalogue.
    // A version mismatch during publication must leave the current reader intact.
    const original=await page.evaluate(()=>structuredClone(ATLAS_DEBUG.data));
    const snapshot={...original,meta:{...original.meta,version:'full-snapshot-fixture'},cards:original.cards.filter(c=>c.id!==testId)};
    let ready=false,catalogueRequests=0;
    await page.evaluate(id=>ATLAS_DEBUG.go(id),testId);
    await page.locator('#'+testId+' [data-public-note]').click();
    await page.locator('#public-note-text').fill('Keep this draft during publication.');
    await page.route('**/updates-delta.json',route=>route.fulfill({json:{version:snapshot.meta.version,base_version:'missed-version',cards:[]}}));
    await page.route('**/catalog.json',route=>{catalogueRequests++;return route.fulfill({json:ready?snapshot:original});});
    await page.route('**/version.json',route=>route.fulfill({json:{version:snapshot.meta.version,delta:true}}));
    await page.evaluate(()=>ATLAS_DEBUG.checkUpdates());
    assert(catalogueRequests>0,'Missed delta fetches catalog.json');
    assert(await page.evaluate(id=>ATLAS_DEBUG.data.cards.some(c=>c.id===id),testId),'Mismatched publication cannot remove a card');
    ready=true;
    await page.evaluate(()=>ATLAS_DEBUG.checkUpdates());
    await page.waitForFunction(id=>!ATLAS_DEBUG.data.cards.some(c=>c.id===id),testId);
    assert.equal(await page.locator('#'+testId).count(),0);
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.data.cards.length),snapshot.cards.length);
    assert.equal(await page.locator('#public-note-text').inputValue(),'Keep this draft during publication.');
    assert.deepEqual(errors,[]);assert.deepEqual(failures,[]);
    console.log(JSON.stringify({base,...data,benchmarks:Object.fromEntries(Object.entries(selections).map(([name,ids])=>[name,ids.length])),community_status:await page.locator('#community-status').textContent(),checks:['project subdirectory asset loading','Top 100 and direct problem link','all three nested selections match exports and preserve order','Top 500 reload, large/small quotas and no search backfill','primary Top 500 goal and Top 100 subset wording','public note and new problem forms','static downloads','both layouts and simplified controls','mobile layout','missed delta uses full catalogue','incomplete publication retries without changing cards','snapshot deletion preserves contribution draft','no browser or HTTP errors']}));
  }finally{
    if(browser)await browser.close();
    if(server)await new Promise(resolve=>server.close(resolve));
  }
})().catch(error=>{console.error(error);process.exitCode=1});
