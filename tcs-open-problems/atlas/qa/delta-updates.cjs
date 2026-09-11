const {chromium}=require('playwright');
const assert=require('assert'),fs=require('fs'),path=require('path');
(async()=>{
  const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
  try{
    const page=await browser.newPage(),errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    await page.goto('http://127.0.0.1:8766/');await page.waitForFunction(()=>window.ATLAS_DEBUG);
    const fixture=await page.evaluate(()=>({base_version:ATLAS_DEBUG.data.meta.version,version:'delta-one',cards:[{...ATLAS_DEBUG.data.cards[0],status_note:'Delta update fixture'}],meta:{...ATLAS_DEBUG.data.meta,version:'delta-one'},areas:ATLAS_DEBUG.data.areas}));
    let published={version:fixture.version,delta:true},delta=fixture,full=fixture,deltaRequests=0,fullRequests=0;
    await page.route('**/version.json',r=>r.fulfill({json:published}));
    await page.route('**/updates-delta.json',r=>{deltaRequests++;return r.fulfill({json:delta});});
    await page.route('**/updates.json',r=>{fullRequests++;return r.fulfill({json:full});});
    await page.evaluate(()=>ATLAS_DEBUG.checkUpdates());
    await page.waitForFunction(id=>ATLAS_DEBUG.data.cards.find(c=>c.id===id)?.status_note==='Delta update fixture',fixture.cards[0].id);
    assert(deltaRequests>=1);assert.equal(fullRequests,0);
    delta={...fixture,base_version:'a-missed-publication',version:'delta-two',cards:[]};
    full={...fixture,version:'delta-two',meta:{...fixture.meta,version:'delta-two'},cards:[{...fixture.cards[0],status_note:'Full fallback fixture'}]};
    published={version:'delta-two',delta:true};
    await page.evaluate(()=>ATLAS_DEBUG.checkUpdates());
    await page.waitForFunction(id=>ATLAS_DEBUG.data.cards.find(c=>c.id===id)?.status_note==='Full fallback fixture',fixture.cards[0].id);
    assert(fullRequests>=1);assert.deepEqual(errors,[]);
    const report={checks:['matching-base delta applied without full download','missed-publication delta rejected','full snapshot fallback applied'],deltaRequests,fullRequests,errors};
    fs.writeFileSync(path.join(__dirname,'delta-updates-results.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
