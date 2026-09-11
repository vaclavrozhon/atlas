const {chromium}=require('playwright');
const assert=require('assert'),fs=require('fs'),path=require('path');
const root='http://127.0.0.1:8766/';
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[],requests=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('request',r=>requests.push(r.url()));
  await page.goto(root+'?collection=textbooks');
  await page.waitForFunction(()=>window.ATLAS_DEBUG);
  assert.equal(await page.locator('#textbook-only').isChecked(),true);
  assert.equal(await page.evaluate(()=>ATLAS_DEBUG.state.matches.length),547);
  assert(await page.evaluate(()=>ATLAS_DEBUG.state.matches.every(c=>c.textbook_notes?.length)));
  assert.equal(await page.locator('header a').filter({hasText:/Source library/i}).count(),0);
  const identifier=await page.evaluate(()=>ATLAS_DEBUG.data.cards.find(c=>c.textbook_import&&c.formal==='Does P=RP?').id);
  await page.fill('#search',identifier);await page.waitForTimeout(250);
  assert.equal(await page.locator('.problem-card').count(),1);
  await page.locator('#'+identifier+' [data-action="note"]').click();
  assert((await page.locator('#'+identifier+' .textbook-notes').innerText()).includes('Open Problem 2.10'));
  for(const href of await page.locator('.textbook-notes a').evaluateAll(as=>as.map(a=>a.getAttribute('href')))){
   assert(/^https?:\/\//.test(href));assert(!href.includes('127.0.0.1'));
  }
  await page.fill('#note-'+identifier,'Check the exact definitions in the original source.');
  await page.locator('#'+identifier+' [data-action="save"]').click();
  await page.reload();await page.fill('#search',identifier);await page.waitForTimeout(250);
  await page.locator('#'+identifier+' [data-action="note"]').click();
  assert.equal(await page.locator('#note-'+identifier).inputValue(),'Check the exact definitions in the original source.');
  assert.equal(await page.locator('#'+identifier+' [data-action="save"]').getAttribute('aria-pressed'),'true');
  const pending=page.waitForEvent('download');await page.locator('#export').click();
  const download=await pending;const exported=JSON.parse(fs.readFileSync(await download.path(),'utf8'));
  assert.equal(exported.cards.length,1);assert(exported.cards[0].textbook_notes.length);
  assert.equal(exported.cards[0].personal_note,'Check the exact definitions in the original source.');
  await page.locator('#clear').click();
  assert.equal(await page.locator('#textbook-only').isChecked(),false);
  await page.check('#textbook-only');
  await page.fill('#search','Open Problem 2.10');await page.waitForTimeout(250);
  assert(await page.locator('#'+identifier).count(),'Search must find the added source locator');
  await page.goto(root+'?collection=textbooks&view=full#TCS-0001');
  await page.locator('#TCS-0001 details').evaluate(e=>e.open=true);
  assert((await page.locator('#TCS-0001 .textbook-notes').innerText()).includes('Pseudorandomness')===false);
  assert((await page.locator('#TCS-0001 .textbook-notes').innerText()).includes('P equal NP'));
  assert.equal(await page.locator('#TCS-0001 .textbook-notes li').count(),5);
  await page.screenshot({path:path.join(__dirname,'textbook-desktop.png')});
  await page.goto(root+'?collection=textbooks#TCS-1012');
  await page.locator('#TCS-1012 details').evaluate(e=>e.open=true);
  assert((await page.locator('#TCS-1012 .textbook-notes').innerText()).includes('inequality inconsistent'));
  await page.setViewportSize({width:390,height:844});
  await page.goto(root+'?collection=textbooks#'+identifier);
  await page.locator('#'+identifier+' details').evaluate(e=>e.open=true);
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await page.screenshot({path:path.join(__dirname,'textbook-mobile.png')});
  for(const forbidden of ['library/','library/library.json','library/open-problems.json','library/pdf/vadhan2012.pdf','tcs-source-library/library.json','research/retired-library-ui-20260910/site/library/','%2e%2e/tcs-source-library/library.json']){
   const response=await page.request.get(root+forbidden);assert.equal(response.status(),404,forbidden);
  }
  assert(!requests.some(url=>/^https?:/.test(url)&&new URL(url).pathname.startsWith('/library/')));
  const offline=await browser.newPage();
  offline.on('pageerror',e=>errors.push(e.message));
  await offline.goto('file://'+path.resolve(__dirname,'../site/index.html')+'?collection=textbooks');
  await offline.waitForFunction(()=>window.ATLAS_DEBUG);
  assert.equal(await offline.evaluate(()=>ATLAS_DEBUG.state.matches.length),547);
  assert.equal(await offline.locator('script[src*="library"]').count(),0);
  assert.deepEqual(errors,[]);
  const report={annotatedCards:547,checks:['main catalogue filter','search includes added source locators','new and reused card source notes','external references only','source caveats visible','personal notes and saved state persist','selection export includes annotations','mobile layout','library paths return 404','no library requests','offline catalogue works'],errors};
  fs.writeFileSync(path.join(__dirname,'textbook-results.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify(report,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
