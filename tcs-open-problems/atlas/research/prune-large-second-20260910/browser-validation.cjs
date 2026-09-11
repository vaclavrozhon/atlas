const path=require('path'),fs=require('fs'),zlib=require('zlib'),assert=require('assert');
const BASE=path.resolve(__dirname,'../..');
const {chromium}=require(path.join(BASE,'qa/node_modules/playwright'));
(async()=>{
 const before=JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(BASE,'to_delete/large-buckets-second-20260910/catalog-before.json.gz'))));
 const current=JSON.parse(fs.readFileSync(path.join(BASE,'site/catalog.json')));
 const manifest=JSON.parse(fs.readFileSync(path.join(BASE,'to_delete/large-buckets-second-20260910/manifest.json')));
 const removed=new Set(Object.keys(manifest.records));
 const beforeLarge=before.cards.filter(c=>c.selection_group==='large').length;
 const afterLarge=current.cards.filter(c=>c.selection_group==='large').length;
 const archived=current.meta.taxonomy.scope_excluded_count;
 const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1000},acceptDownloads:true}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  // A real pre-pruning snapshot exercises the large live classification update.
  await page.route('**/data.js',r=>r.fulfill({contentType:'text/javascript',body:'window.TCS_ATLAS='+JSON.stringify(before).replace(/<\//g,'<\\/')+';'}));
  await page.route('**/version.json',r=>r.fulfill({json:{version:before.meta.version}}));
  await page.goto('http://127.0.0.1:8766/');await page.waitForFunction(()=>window.ATLAS_DEBUG);
  await page.locator('#advanced-filters > summary').click();
  await page.selectOption('#group','large');
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),beforeLarge);
  await page.fill('#search','TCS-0032');await page.waitForFunction(()=>ATLAS_DEBUG.state.matches.length===1);
  await page.locator('#TCS-0032 [data-action="note"]').click();
  await page.locator('#note-TCS-0032').fill('Preserve this note across the preliminary removal.');
  const report=await page.evaluate(async snapshot=>{
   const note=document.querySelector('#note-TCS-0032');note.focus();note.setSelectionRange(9,9);
   let ticks=0;const timer=setInterval(()=>ticks++,10);const start=performance.now();
   await ATLAS_DEBUG.applyPublication({version:snapshot.meta.version,cards:snapshot.cards,meta:snapshot.meta,areas:snapshot.areas});
   clearInterval(timer);
   const now=document.querySelector('#note-TCS-0032');
   return {durationMs:Math.round(performance.now()-start),eventLoopTicks:ticks,note:now.value,focus:document.activeElement===now&&now.selectionStart===9,domCards:document.querySelectorAll('.problem-card').length,matches:ATLAS_DEBUG.state.matches.length};
  },current);
  assert.equal(report.matches,0);assert(report.focus);assert(report.domCards<=17);assert(report.eventLoopTicks>5);
  assert.equal(report.note,'Preserve this note across the preliminary removal.');
  assert((await page.locator('#TCS-0032').innerText()).includes('Preliminarily removed'));
  assert((await page.locator('#TCS-0032').innerText()).includes('Quantum computation'));
  assert((await page.locator('#TCS-0032').innerText()).includes(manifest.records['TCS-0032'].reason));
  await page.click('#clear');await page.selectOption('#group','large');
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),afterLarge);
  assert(!(await page.evaluate(()=>ATLAS_DEBUG.state.matches.some(c=>c.scope_exclusion))));
  const downloadWait=page.waitForEvent('download');await page.click('#export');
  const download=await downloadWait;const exported=path.join(__dirname,'retained-large-export.json');await download.saveAs(exported);
  const selection=JSON.parse(fs.readFileSync(exported));assert.equal(selection.cards.length,afterLarge);assert(selection.cards.every(c=>!removed.has(c.id)));
  await page.click('#clear');await page.selectOption('#scope','archived');
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),archived);
  await page.fill('#search','TCS-0032');await page.waitForFunction(()=>ATLAS_DEBUG.state.matches.length===1);
  await page.locator('#TCS-0032 [data-action="note"]').click();assert.equal(await page.locator('#note-TCS-0032').inputValue(),report.note);
  await page.screenshot({path:path.join(__dirname,'preliminary-archive.png')});
  await page.fill('#search','TCS-5489');await page.waitForFunction(()=>ATLAS_DEBUG.state.matches.length===1);
  await page.locator('#TCS-5489 .canonical-card-link').click();await page.waitForSelector('#TCS-3105');
  assert((await page.locator('#TCS-3105').innerText()).includes('unit interval'));
  // A current offline reader must honor the same quarantine without any server.
  const offline=await browser.newPage({viewport:{width:390,height:844}});offline.on('pageerror',e=>errors.push(e.message));
  await offline.goto('file://'+path.join(BASE,'site/index.html'));await offline.waitForFunction(()=>window.ATLAS_DEBUG);
  assert.equal(await offline.evaluate(()=>ATLAS_DEBUG.data.cards.filter(c=>c.selection_group==='large').length),afterLarge);
  assert(await offline.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  assert.equal(await offline.locator('a[href*="library/"]').count(),0);
  assert.deepEqual(errors,[]);
  const result={...report,largeBefore:beforeLarge,largeAfter:afterLarge,quarantined:removed.size,archiveTotal:archived,checks:['real pre-pruning live update','editing focus and note retained on quarantine','bounded DOM and responsive event loop','correct new badge/reason/previous category','retained-only export','archive filter and retained counterpart link','offline and mobile filtering','independent library absent from UI'],errors};
  fs.writeFileSync(path.join(__dirname,'browser-validation.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
