const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const http=require('node:http');
const os=require('node:os');
const path=require('node:path');
const {pathToFileURL}=require('node:url');

(async()=>{
  const site=path.resolve(__dirname,'../build'),screenshots=fs.mkdtempSync(path.join(os.tmpdir(),'atlas-map-'));
  let browser,server;
  try{
    const mime={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.woff2':'font/woff2'};
    server=http.createServer((req,res)=>{
      const pathname=new URL(req.url,'http://localhost').pathname;
      const filename=path.resolve(site,decodeURIComponent(pathname.slice('/atlas/'.length))||'index.html');
      if(!pathname.startsWith('/atlas/')||!filename.startsWith(site+path.sep)||!fs.existsSync(filename)||!fs.statSync(filename).isFile()){
        res.writeHead(404);res.end();return;
      }
      res.writeHead(200,{'content-type':mime[path.extname(filename)]||'text/plain'});fs.createReadStream(filename).pipe(res);
    });
    await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
    const base=`http://127.0.0.1:${server.address().port}/atlas/`;
    browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
    const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    await page.goto(base+'map.html');
    await page.waitForFunction(()=>window.ATLAS_MAP?.ready);
    await page.locator('#map-pause').click();
    assert.equal(await page.locator('#map-pause').getAttribute('aria-pressed'),'true');
    const graph=await page.evaluate(()=>{
      const m=ATLAS_MAP,active=m.data.cards.filter(c=>!c.scope_exclusion&&!['resolved','excluded'].includes(c.status));
      const ids=new Set(active.map(c=>c.id)),pairs=new Set();
      for(const c of active)for(const id of c.related_problem_ids||[])if(ids.has(id)&&id!==c.id)pairs.add([c.id,id].sort().join('|'));
      return {nodes:m.nodes.length,expected:active.length,edges:m.links.length,expectedEdges:pairs.size,
        unique:new Set(m.links.map(e=>[e.source.id,e.target.id].sort().join('|'))).size,
        finite:m.nodes.every(n=>Number.isFinite(n.x)&&Number.isFinite(n.y)),
        unchanged:m.data.cards.every(c=>(c.related_problem_ids||[]).every(id=>typeof id==='string')),
        first:active.find(c=>c.working_summary?.sentences?.length).id,
        summaries:active.every(c=>!c.working_summary?.sentences?.length||m.savedDescription(c).text===c.working_summary.sentences.join(' '))};
    });
    assert.equal(graph.nodes,graph.expected);assert.equal(graph.edges,graph.expectedEdges);assert.equal(graph.edges,graph.unique);
    assert(graph.finite&&graph.unchanged&&graph.summaries);assert(graph.nodes>500);
    await page.screenshot({path:path.join(screenshots,'desktop.png')});
    async function point(id,p=page){return p.evaluate(id=>{
      const n=ATLAS_MAP.nodes.find(n=>n.id===id),t=ATLAS_MAP.transform,b=document.getElementById('map-canvas').getBoundingClientRect();
      return {x:b.x+t.applyX(n.x),y:b.y+t.applyY(n.y),worldX:n.x,worldY:n.y};
    },id);}
    // Search moves to the actual node; hovering then displays the unchanged summary.
    await page.locator('#map-search').fill(graph.first);
    assert.equal(await page.locator('#map-results button').count(),1);
    await page.locator('#map-results button').click();
    assert.equal(await page.locator('#map-preview').getAttribute('data-id'),graph.first);
    await page.keyboard.press('Escape');
    const p=await point(graph.first);await page.mouse.move(p.x,p.y);
    await page.waitForFunction(()=>!document.getElementById('map-preview').hidden);
    const content=await page.evaluate(id=>({actual:document.getElementById('map-preview-text').textContent,
      expected:ATLAS_MAP.data.cards.find(c=>c.id===id).working_summary.sentences.join(' ')}),graph.first);
    assert.equal(content.actual,content.expected);
    assert.equal(await page.locator('#map-preview-link').getAttribute('href'),'index.html#'+graph.first);
    await page.screenshot({path:path.join(screenshots,'preview.png')});
    // Moving onto the preview must keep it readable; Escape always dismisses it.
    await page.locator('#map-preview-title').hover();await page.waitForTimeout(220);
    assert(await page.locator('#map-preview').isVisible());await page.keyboard.press('Escape');
    await page.mouse.move(p.x,p.y);await page.mouse.click(p.x,p.y);await page.mouse.move(1400,950);
    assert(await page.locator('#map-preview').isVisible());
    await page.keyboard.press('Escape');
    // Drag a real node, then zoom and pan the viewport without changing graph membership.
    const before=await point(graph.first);
    await page.mouse.move(before.x,before.y);await page.mouse.down();
    await page.mouse.move(before.x+75,before.y+40,{steps:8});await page.mouse.up();
    const after=await point(graph.first);assert(Math.hypot(after.worldX-before.worldX,after.worldY-before.worldY)>20);
    await page.keyboard.press('Escape');
    const scale=await page.evaluate(()=>ATLAS_MAP.transform.k);await page.locator('#map-zoom-in').click();
    assert((await page.evaluate(()=>ATLAS_MAP.transform.k))>scale);
    await page.locator('#map-fit').click();
    const transform=await page.evaluate(()=>({x:ATLAS_MAP.transform.x,y:ATLAS_MAP.transform.y}));
    const box=await page.locator('#map-canvas').boundingBox();
    await page.mouse.move(box.x+25,box.y+80);await page.mouse.down();await page.mouse.move(box.x+70,box.y+110,{steps:5});await page.mouse.up();
    const moved=await page.evaluate(()=>({x:ATLAS_MAP.transform.x,y:ATLAS_MAP.transform.y}));
    assert(Math.hypot(moved.x-transform.x,moved.y-transform.y)>20);
    await page.locator('#map-category').selectOption({index:1});
    assert.equal(await page.evaluate(()=>ATLAS_MAP.nodes.length),graph.nodes,'Highlighting preserves the complete graph');
    await page.locator('#map-search').fill('this-query-has-no-results-98765');
    assert.equal(await page.locator('#map-results button').count(),0);
    assert.match(await page.locator('#map-result-count').innerText(),/0 matching/);
    await page.locator('#map-clear').click();
    await page.locator('#map-canvas').focus();await page.keyboard.press('ArrowRight');
    assert(await page.locator('#map-preview').isVisible());await page.keyboard.press('Enter');
    assert.equal(await page.evaluate(()=>document.activeElement.id),'map-preview-link');
    await page.keyboard.press('Escape');assert(await page.locator('#map-preview').isHidden());
    // Snapshot fixtures exercise missing summaries, escaped text and live retirement.
    const original=await page.evaluate(()=>structuredClone(ATLAS_MAP.data));
    const fixture=structuredClone(original),a=structuredClone(original.cards.find(c=>c.id===graph.first)),b=structuredClone(a),retired=structuredClone(a);
    a.id='TCS-99991';b.id='TCS-99992';retired.id='TCS-99993';retired.status='resolved';
    a.title='Saved <img src=x onerror="window.UNSAFE_MAP=true"> question';a.working_summary=null;a.statement_review={status:'revised'};
    a.formal='Existing question: \\(x^2+1\\).';
    a.related_problem_ids=[b.id,b.id,retired.id,'TCS-88888',a.id];b.related_problem_ids=[a.id];
    fixture.cards=[a,b,retired];fixture.meta.version='map-fixture';
    await page.evaluate(c=>ATLAS_MAP.applyCatalogue(c),fixture);
    assert.equal(await page.evaluate(()=>ATLAS_MAP.nodes.length),2);assert.equal(await page.evaluate(()=>ATLAS_MAP.links.length),1);
    await page.locator('#map-search').fill(a.id);await page.locator('#map-results button').click();
    assert.equal(await page.locator('#map-preview-title').innerText(),a.title);assert.equal(await page.locator('#map-preview img').count(),0);
    assert.equal(await page.locator('#map-preview-text .katex').count(),1);assert.match(await page.locator('#map-preview-text').innerText(),/Saved question/i);
    assert(!(await page.evaluate(()=>window.UNSAFE_MAP)));
    const positions=await page.evaluate(()=>ATLAS_MAP.nodes.map(n=>[n.id,n.x,n.y]));
    const updated=structuredClone(fixture);updated.cards=[b];updated.meta.version='map-updated';
    await page.route('**/version.json',r=>r.fulfill({json:{version:'map-updated'}}));
    await page.route('**/catalog.json',r=>r.fulfill({json:fixture}));
    await page.evaluate(()=>ATLAS_MAP.checkUpdates());assert.equal(await page.evaluate(()=>ATLAS_MAP.nodes.length),2,'Reject mismatched snapshot');
    await page.unroute('**/catalog.json');await page.route('**/catalog.json',r=>r.fulfill({json:updated}));
    await page.evaluate(()=>ATLAS_MAP.checkUpdates());assert.equal(await page.evaluate(()=>ATLAS_MAP.nodes.length),1);
    assert.equal(await page.evaluate(()=>ATLAS_MAP.links.length),0);assert(await page.locator('#map-preview').isHidden());
    assert.deepEqual(await page.evaluate(()=>ATLAS_MAP.nodes.map(n=>[n.id,n.x,n.y])),positions.filter(p=>p[0]===b.id));
    await page.evaluate(c=>ATLAS_MAP.applyCatalogue({...c,cards:[]}),updated);
    assert.match(await page.locator('#map-loading').innerText(),/No active problems/);
    // Touch previews and a usable, bounded layout on a small screen.
    const mobile=await browser.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true,reducedMotion:'reduce'});
    mobile.on('pageerror',e=>errors.push(e.message));
    await mobile.goto(base+'map.html#'+graph.first);await mobile.waitForFunction(()=>window.ATLAS_MAP?.ready);
    assert.equal(await mobile.locator('#map-pause').getAttribute('aria-pressed'),'true');
    await mobile.locator('#map-preview-close').tap();
    const touch=await point(graph.first,mobile);await mobile.touchscreen.tap(touch.x,touch.y);
    assert(await mobile.locator('#map-preview').isVisible());
    const bounds=await mobile.locator('#map-preview').boundingBox();assert(bounds.x>=0&&bounds.x+bounds.width<=391);
    assert(await mobile.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
    await mobile.screenshot({path:path.join(screenshots,'mobile.png')});
    // All assets and existing descriptions also work under file://.
    const offline=await browser.newPage({reducedMotion:'reduce'});offline.on('pageerror',e=>errors.push(e.message));
    await offline.goto(pathToFileURL(path.join(site,'map.html')).href+'#'+graph.first);await offline.waitForFunction(()=>window.ATLAS_MAP?.ready);
    assert(await offline.locator('#map-preview').isVisible());assert.equal(await offline.evaluate(()=>ATLAS_MAP.nodes.length),graph.nodes);
    assert.deepEqual(errors,[]);
    console.log(JSON.stringify({nodes:graph.nodes,edges:graph.edges,screenshots,checks:['active graph and isolated nodes','deduplicated valid relationships','unchanged existing summaries','hover and pinned preview','node dragging','pan and zoom','search and category highlighting','keyboard navigation','formula fallback and escaped text','consistent live updates and deletions','empty graph','mobile touch','reduced motion','offline and project-prefix assets']}));
  }finally{await browser?.close();if(server)await new Promise(resolve=>server.close(resolve));}
})().catch(error=>{console.error(error);process.exitCode=1;});
