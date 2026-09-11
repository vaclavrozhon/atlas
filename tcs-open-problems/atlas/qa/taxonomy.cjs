const {chromium}=require('playwright');
const assert=require('assert');
const fs=require('fs'),path=require('path');

(async()=>{
  const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
  try{
    const page=await browser.newPage({viewport:{width:1440,height:1000},acceptDownloads:true});
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.goto('http://127.0.0.1:8766/');
    await page.waitForFunction(()=>window.ATLAS_DEBUG);
    const areas=await page.evaluate(()=>ATLAS_DEBUG.data.areas);
    assert.equal(areas.length,35);
    assert.equal(areas.filter(a=>a.group==='large').length,10);
    assert.equal(areas.filter(a=>a.group==='small').length,25);
    assert.equal(areas.reduce((n,a)=>n+a.target,0),1000);
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.data.meta.taxonomy.reserved_target),0);
    assert.equal(await page.locator('.area-group[data-group="large"] input').count(),10);
    assert.equal(await page.locator('.area-group[data-group="small"] input').count(),25);
    assert.equal(await page.locator('#coverage-table .category-link').count(),35);
    assert.equal(areas[1].area,'Computational geometry and metric spaces');
    assert.equal(areas[1].target,50);
    assert.equal(areas[10].area,'Approximation algorithms and hardness of approximation');
    assert.equal(areas[10].target,20);
    assert.equal(areas[6].area,'Distributed, parallel and sublinear algorithms');
    assert.equal(areas[9].area,'Optimization and numerics');
    assert.equal(areas[32].area,'Structural graph theory');
    assert.equal(areas[34].area,'Miscellaneous');
    assert(!areas.some(a=>a.area==='Combinatorics and graph polynomials'));
    for(const a of areas){
      await page.locator('.area-option input').evaluateAll((els,area)=>{
        for(const el of els){el.checked=el.value===area;el.dispatchEvent(new Event('change',{bubbles:true}));}
      },a.area);
      assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),a.count,a.area);
      assert(await page.evaluate(area=>ATLAS_DEBUG.state.matches.every(c=>c.area===area),a.area));
    }
    await page.click('#clear');
    await page.locator('#advanced-filters > summary').click();
    await page.selectOption('#group','large');
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),areas.filter(a=>a.group==='large').reduce((n,a)=>n+a.count,0));
    assert.equal(await page.locator('.area-option:visible').count(),10);
    await page.selectOption('#group','small');
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),areas.filter(a=>a.group==='small').reduce((n,a)=>n+a.count,0));
    assert.equal(await page.locator('.area-option:visible').count(),25);
    await page.selectOption('#group','large');
    await page.fill('#area-search','metric');
    assert.equal(await page.locator('.area-option:visible').count(),1);
    await page.locator('.area-option:visible input').check();
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),areas[1].count);
    const downloadPromise=page.waitForEvent('download');await page.click('#export');
    const download=await downloadPromise;
    const file=path.join(__dirname,'taxonomy-selection.json');await download.saveAs(file);
    const exported=JSON.parse(fs.readFileSync(file));
    assert(exported.cards.every(c=>c.original_area&&c.selection_group==='large'&&c.selection_target===50));
    assert.equal(exported.cards.length,areas[1].count);
    await page.click('#clear');
    assert.equal(await page.locator('.area-group:visible').count(),2);
    assert.equal(await page.locator('.area-option:visible').count(),35);
    // Archives preserve IDs and notes but do not inflate category counts.
    const archived=await page.evaluate(()=>ATLAS_DEBUG.data.cards.filter(c=>c.scope_exclusion));
    assert.equal(archived.length,await page.evaluate(()=>ATLAS_DEBUG.data.meta.taxonomy.scope_excluded_count));
    assert.equal(archived.filter(c=>c.scope_exclusion.kind!=='preliminary_quality').length,14);
    const removed=archived.filter(c=>c.scope_exclusion.kind==='preliminary_quality');
    assert.equal(removed.length,await page.evaluate(()=>ATLAS_DEBUG.data.meta.taxonomy.preliminary_removal_count));
    assert(removed.every(c=>c.scope_exclusion.previous_area&&c.scope_exclusion.reason));
    await page.selectOption('#scope','archived');
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),archived.length);
    assert(await page.evaluate(()=>ATLAS_DEBUG.state.matches.every(c=>c.selection_group==='excluded')));
    const archivedId=archived[0].id;
    await page.evaluate(id=>ATLAS_DEBUG.go(id),archivedId);
    await page.locator(`#${archivedId} [data-action=note]`).click();
    await page.locator(`#note-${archivedId}`).fill('Preserved archive note');
    await page.selectOption('#scope','all');
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),await page.evaluate(()=>ATLAS_DEBUG.data.cards.length));
    await page.click('#clear');
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),areas.reduce((n,a)=>n+a.count,0));
    await page.evaluate(id=>ATLAS_DEBUG.go(id),archivedId);
    await page.locator(`#${archivedId} [data-action=note]`).click();
    assert.equal(await page.locator(`#note-${archivedId}`).inputValue(),'Preserved archive note');
    assert(!(await page.evaluate(()=>ATLAS_DEBUG.state.matches.some(c=>c.scope_exclusion))));
    await page.click('#clear');
    await page.screenshot({path:path.join(__dirname,'taxonomy-desktop.png')});
    await page.locator('header a[href="#coverage"]').click();
    await page.locator('.category-link').filter({hasText:'Miscellaneous'}).click();
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),areas[34].count);
    assert(await page.locator('.filter-chip[data-area="Miscellaneous"]').count());
    // Metadata-only live publication must rebuild counts and retain working
    // filter handlers without clearing selected categories or the area search.
    await page.fill('#area-search','misc');
    await page.evaluate(async()=>{
      const d=ATLAS_DEBUG.data;
      await ATLAS_DEBUG.applyPublication({version:'taxonomy-metadata-fixture',cards:[],meta:d.meta,areas:d.areas.map(a=>({...a,count:a.count+1}))});
    });
    assert.equal(await page.locator('.area-option:visible').count(),1);
    assert(await page.locator('.area-option:visible input').isChecked());
    await page.locator('.area-option:visible input').uncheck();
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.areas.size),0);
    await page.setViewportSize({width:390,height:844});
    await page.goto('http://127.0.0.1:8766/');
    await page.click('#filters-toggle');
    await page.locator('#advanced-filters > summary').click();
    await page.selectOption('#group','small');
    await page.selectOption('#group','large');
    await page.fill('#area-search','metric');
    await page.locator('.area-option:visible input').check();
    assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),areas[1].count);
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await page.locator('#group').scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(__dirname,'taxonomy-mobile.png')});
    assert.deepEqual(errors,[]);
    const report={groups:35,assignedTarget:1000,reservedTarget:0,target:1000,candidates:areas.reduce((n,a)=>n+a.count,0),metric:areas[1].count,misc:areas[34].count,checks:['all 35 individual filters','10/25 grouping and ordering','archive filters and original IDs/notes preserved','large/small filters','category search','exported assignments and original areas','reset restores group visibility','selection table navigation','metadata-only live updates preserve filters and handlers','mobile filters and width'],errors};
    fs.writeFileSync(path.join(__dirname,'taxonomy-results.json'),JSON.stringify(report,null,2));
    console.log(JSON.stringify(report,null,2));
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
