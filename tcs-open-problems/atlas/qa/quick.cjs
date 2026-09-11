const {chromium}=require('playwright');
const assert=require('assert'),fs=require('fs'),path=require('path');
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.goto('http://127.0.0.1:8766/?view=compact');
  await page.waitForFunction(()=>window.ATLAS_DEBUG);
  const counts=await page.evaluate(()=>({total:ATLAS_DEBUG.data.cards.filter(c=>!c.scope_exclusion).length,drafts:ATLAS_DEBUG.data.cards.filter(c=>!c.scope_exclusion&&c.evidence!=='reviewed'&&!c.review_outcome?.complete).length,detailed:ATLAS_DEBUG.data.cards.filter(c=>c.evidence==='reviewed').length}));
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),counts.total);
  assert.equal(await page.locator('#view').inputValue(),'compact');
  assert(await page.locator('.compact-card').count()>0);
  await page.locator('#advanced-filters > summary').click();
  await page.selectOption('#evidence','drafts');
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),counts.drafts);
  assert(await page.evaluate(()=>ATLAS_DEBUG.state.matches.every(c=>!c.review_outcome?.complete)));
  await page.fill('#search','Micali');await page.waitForTimeout(250);
  assert(await page.locator('#TCS-4696').count(),'Search must include the saved question excerpt');
  assert((await page.locator('#TCS-4696').innerText()).includes('Is there an analog'));
  assert(!(await page.locator('#TCS-4696').innerText()).includes('A short source quotation appears below'));
  await page.locator('#TCS-4696 [data-action="note"]').click();
  await page.locator('#note-TCS-4696').fill('Check this question and its model.');
  await page.reload();await page.fill('#search','TCS-4696');await page.waitForTimeout(250);
  await page.locator('#TCS-4696 [data-action="note"]').click();
  assert.equal(await page.locator('#note-TCS-4696').inputValue(),'Check this question and its model.');
  // A reviewed replacement must retain the same personal note and compact layout.
  await page.evaluate(async()=>{const c=ATLAS_DEBUG.data.cards.find(c=>c.id==='TCS-4696');await ATLAS_DEBUG.applyPublication({version:'quick-upgrade-test',cards:[{...c,evidence:'reviewed',formal:'Reviewed statement fixture',answer_criterion:'A proof or refutation.',question_type:'yes_no'}],meta:ATLAS_DEBUG.data.meta,areas:ATLAS_DEBUG.data.areas});});
  assert.equal(await page.locator('#note-TCS-4696').inputValue(),'Check this question and its model.');
  assert(await page.locator('#TCS-4696.compact-card').count());
  await page.goto('http://127.0.0.1:8766/?view=compact#TCS-0473');await page.waitForTimeout(400);
  assert((await page.locator('#TCS-0473').innerText()).includes('Retired after review'));
  assert((await page.locator('#TCS-0473').innerText()).includes('Reviewed disposition'));
  const labelId=await page.evaluate(()=>ATLAS_DEBUG.data.cards.find(c=>c.evidence==='index'&&c.legacy?.statement_form==='index_label').id);
  await page.goto('http://127.0.0.1:8766/?view=compact#'+labelId);await page.waitForTimeout(500);
  const box=await page.locator('#'+labelId).boundingBox();assert(box.y>=100&&box.y<180);
  assert((await page.locator('#'+labelId).innerText()).includes('Topic label'));
  await page.screenshot({path:path.join(__dirname,'quick-desktop.png')});
  await page.setViewportSize({width:390,height:844});await page.goto('http://127.0.0.1:8766/?view=compact');
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await page.screenshot({path:path.join(__dirname,'quick-mobile.png')});
  assert.deepEqual(errors,[]);
  const report={counts,checks:['all records available','draft filter','excerpt search','no placeholder in closed card','note persistence','note preserved on review upgrade','direct link','topic label marked','mobile width','no browser errors'],errors};
  fs.writeFileSync(path.join(__dirname,'quick-results.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
