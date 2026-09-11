const {chromium}=require('../../qa/node_modules/playwright');
const assert=require('assert'),fs=require('fs'),path=require('path'),zlib=require('zlib');
const base=path.resolve(__dirname,'../..');
const current=JSON.parse(fs.readFileSync(path.join(base,'site/catalog.json')));
const before=JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(__dirname,'catalog-before.json.gz'))));
const manifest=JSON.parse(fs.readFileSync(path.join(__dirname,'manifest.json')));
const removedId='TCS-1165';
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.route('**/version.json',r=>r.fulfill({contentType:'application/json',body:JSON.stringify({version:current.meta.version})}));
  await page.goto('http://127.0.0.1:8766/');
  await page.waitForFunction(()=>window.ATLAS_DEBUG);
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),current.meta.taxonomy.candidate_count);
  await page.locator('#advanced-filters > summary').click();
  await page.selectOption('#group','small');
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),manifest.small_remaining);
  // Reproduce the real bulk pruning in an isolated browser, while editing a note.
  await page.evaluate(async data=>ATLAS_DEBUG.applyPublication({version:'small-pruning-before-fixture',...data}),{cards:before.cards,meta:before.meta,areas:before.areas});
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),manifest.reviewed_small_count);
  await page.evaluate(id=>ATLAS_DEBUG.go(id),removedId);
  await page.locator(`#${removedId} [data-action=note]`).click();
  await page.locator(`#note-${removedId}`).fill('Keep this note through preliminary removal.');
  const started=Date.now();
  await page.evaluate(async data=>ATLAS_DEBUG.applyPublication({version:data.meta.version,...data}),{cards:current.cards,meta:current.meta,areas:current.areas});
  const updateMs=Date.now()-started;
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),manifest.small_remaining);
  assert.equal(await page.locator(`#note-${removedId}`).inputValue(),'Keep this note through preliminary removal.');
  assert.equal(await page.evaluate(()=>document.activeElement.id),`note-${removedId}`);
  const rendered=await page.locator('.problem-card').count();assert(rendered<=18,`Unbounded DOM: ${rendered}`);
  assert((await page.locator(`#${removedId}`).innerText()).includes('Preliminarily removed'));
  assert((await page.locator(`#${removedId}`).innerText()).includes(manifest.records[removedId].category));
  await page.click('#clear');
  await page.selectOption('#scope','archived');
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.filter(c=>c.scope_exclusion.review_id==='small-buckets-20260910').length),manifest.provisional_removed);
  await page.goto('http://127.0.0.1:8766/#'+removedId);
  await page.waitForSelector(`#${removedId}`);
  await page.locator(`#${removedId} [data-action=note]`).click();
  assert.equal(await page.locator(`#note-${removedId}`).inputValue(),'Keep this note through preliminary removal.');
  await page.goto('http://127.0.0.1:8766/#TCS-6685');
  await page.waitForSelector('#TCS-6685');
  assert(await page.evaluate(()=>ATLAS_DEBUG.state.matches.some(c=>c.id==='TCS-6685'&&!c.scope_exclusion)));
  await page.setViewportSize({width:390,height:844});
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  // The portable reader uses the same candidate/archive filters without a server.
  const offline=await browser.newPage();offline.on('pageerror',e=>errors.push(e.message));
  await offline.goto('file://'+path.join(base,'site/index.html'));
  await offline.waitForFunction(()=>window.ATLAS_DEBUG);
  assert.equal(await offline.evaluate(()=>ATLAS_DEBUG.state.matches.length),current.meta.taxonomy.candidate_count);
  await offline.locator('#advanced-filters > summary').click();
  await offline.selectOption('#group','small');
  assert.equal(await offline.evaluate(()=>ATLAS_DEBUG.state.matches.length),manifest.small_remaining);
  assert.deepEqual(errors,[]);
  const report={candidateTotal:current.meta.taxonomy.candidate_count,smallBefore:manifest.reviewed_small_count,smallAfter:manifest.small_remaining,quarantined:manifest.provisional_removed,bulkUpdateMs:updateMs,renderedCardsAfterBulkUpdate:rendered,checks:['small candidate count','archive reason and previous category','actual bulk-pruning payload preserves editing focus and note','bounded DOM','note survives reload and stable link','BB(6) remains active','mobile width','offline reader'],errors};
  fs.writeFileSync(path.join(__dirname,'browser-validation.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
