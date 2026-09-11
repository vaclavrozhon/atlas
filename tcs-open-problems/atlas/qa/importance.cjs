const {chromium}=require('playwright');
const assert=require('assert');
const fs=require('fs'),path=require('path');
(async()=>{
  const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
  try{
    const page=await browser.newPage({viewport:{width:1440,height:1000},acceptDownloads:true});
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.route('**/version.json',r=>r.fulfill({json:{version:'hold'}}));
    await page.route('**/updates.json',r=>r.abort());
    await page.goto('http://127.0.0.1:8766/');await page.waitForFunction(()=>window.ATLAS_DEBUG);
    assert.equal(await page.locator('#sort').inputValue(),'importance');
    assert.equal(await page.locator('.problem-card').first().getAttribute('id'),'TCS-0001');
    const areas=await page.evaluate(()=>ATLAS_DEBUG.data.areas.map(a=>a.area));
    for(const area of areas){
      await page.locator('.area-option input').evaluateAll((els,area)=>{
        for(const el of els)if(el.checked!== (el.value===area)){el.checked=el.value===area;el.dispatchEvent(new Event('change',{bubbles:true}));}
      },area);
      assert(await page.evaluate(()=>ATLAS_DEBUG.state.matches.every((c,i,a)=>c.importance_rank===i+1&&(!i||(a[i-1].status!=='resolved'&&c.status==='resolved')||(a[i-1].status==='resolved')===(c.status==='resolved')&&a[i-1].importance.score>=c.importance.score))),area);
      assert(await page.evaluate(()=>{
        const cs=ATLAS_DEBUG.state.matches;
        return !cs.some(c=>c.status!=='resolved'&&c.importance.method==='editorial'&&c.importance.score>50)
          || cs[0].importance.method==='editorial';
      }),area+' places assessed priorities above provisional drafts');
    }
    assert(await page.evaluate(()=>ATLAS_DEBUG.data.meta.importance.assessed>1100));
    assert.equal(await page.locator('a[href="importance-ranking.csv"]').count(),1);
    await page.click('#clear');
    const splayArea=await page.evaluate(()=>ATLAS_DEBUG.data.cards.find(c=>c.id==='TCS-6498').area);
    await page.locator('.area-option input').evaluateAll((els,area)=>{const e=els.find(x=>x.value===area);e.checked=true;e.dispatchEvent(new Event('change',{bubbles:true}));},splayArea);
    assert.equal(await page.locator('.problem-card').first().getAttribute('id'),'TCS-6498');
    await page.locator('#advanced-filters > summary').click();
    await page.selectOption('#evidence','reviewed');
    const ranks=await page.evaluate(()=>ATLAS_DEBUG.state.matches.map(c=>c.importance_rank));
    assert(ranks.every((r,i)=>!i||r>ranks[i-1]));
    const id=await page.locator('.problem-card').first().getAttribute('id');
    await page.locator(`#${id} summary`).click();
    const note=page.locator(`#note-${id}`);await note.fill('Importance live update: keep my note.');
    await note.evaluate(el=>el.setSelectionRange(7,7));
    const before=await page.locator(`#${id}`).boundingBox();
    await page.evaluate(async()=>{
      const d=ATLAS_DEBUG.data,target=d.cards.find(c=>c.id==='TCS-6503');
      await ATLAS_DEBUG.applyPublication({version:'importance-fixture',cards:[{...target,importance:{...target.importance,score:99},importance_rank:1}],meta:d.meta,areas:d.areas});
    });
    const after=await page.locator(`#${id}`).boundingBox();
    assert.equal(await page.locator('.problem-card').first().getAttribute('id'),'TCS-6503');
    assert.equal(await note.inputValue(),'Importance live update: keep my note.');
    assert(await note.evaluate(el=>document.activeElement===el&&el.selectionStart===7));
    assert(Math.abs(before.y-after.y)<4,`reading anchor shifted ${before.y-after.y}`);
    assert.equal(await page.locator('#sort').inputValue(),'importance');
    const promise=page.waitForEvent('download');await page.click('#export');
    const download=await promise;const file=path.join(__dirname,'importance-selection.json');await download.saveAs(file);
    const exported=JSON.parse(fs.readFileSync(file));assert.equal(exported.cards[0].id,'TCS-6503');
    assert(exported.cards.every(c=>c.importance.reason&&c.importance_rank));
    await page.click('#clear');
    const sequence=await page.evaluate(()=>ATLAS_DEBUG.state.matches.map(c=>c.id));
    const distant=sequence.at(-1);
    await page.evaluate(id=>ATLAS_DEBUG.go(id),distant);
    assert.deepEqual(await page.evaluate(()=>ATLAS_DEBUG.state.matches.map(c=>c.id)),sequence,'Direct links preserve sorted results and export order');
    assert.equal(await page.locator(`[id="${distant}"]`).count(),1);
    const linkedDownload=page.waitForEvent('download');await page.click('#export');
    const linkedFile=path.join(__dirname,'importance-linked-selection.json');await (await linkedDownload).saveAs(linkedFile);
    assert.deepEqual(JSON.parse(fs.readFileSync(linkedFile)).cards.map(c=>c.id),sequence);
    await page.setViewportSize({width:390,height:844});await page.goto('http://127.0.0.1:8766/');
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await page.screenshot({path:path.join(__dirname,'importance-mobile.png')});
    await page.goto('file://'+path.resolve(__dirname,'../site/index.html'));
    assert.equal(await page.locator('.problem-card').first().getAttribute('id'),'TCS-0001');
    assert.deepEqual(errors,[]);
    console.log(JSON.stringify({categories:areas.length,checks:['importance default','all category positions and descending scores','filter-stable positions','live reorder','note and focus preservation','reading position preservation','sorted export with rationale','direct links preserve ranking and export order','mobile width','offline ordering'],errors},null,2));
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
