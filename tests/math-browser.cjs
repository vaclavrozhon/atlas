const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
  page.on('pageerror',error=>errors.push(error.message));
  await page.route('https://api.github.com/**',r=>r.fulfill({json:[]}));
  await page.route('https://atlas-public-notes.vaclavrozhon.chatgpt.site/**',r=>r.fulfill({json:{notes:[],next:null,votes:[],mine:[]}}));
  await page.goto(pathToFileURL(path.resolve(__dirname,'../build/index.html')).href);
  await page.waitForFunction(()=>window.ATLAS_DEBUG&&window.ATLAS_MATH);
  const audit=await page.evaluate(async()=>{
   const rows=ATLAS_DEBUG.data.cards.filter(ATLAS_DEBUG.isActive),failures=[],result={cards:rows.length,compact:0,full:0,expressions:0};
   const host=document.createElement('div');host.id='math-audit';document.body.append(host);
   for(const view of ['compact','full']){
    document.getElementById('view').value=view;
    for(let i=0;i<rows.length;i++){
     host.innerHTML=ATLAS_DEBUG.renderCard(rows[i]);ATLAS_DEBUG.math(host);result[view]++;
     result.expressions+=host.querySelectorAll('.katex').length;
     const broken=[...host.querySelectorAll('.katex-error')].map(el=>({text:el.textContent,error:el.title}));
     if(broken.length)failures.push({id:rows[i].id,view,broken});
     const walker=document.createTreeWalker(host,NodeFilter.SHOW_TEXT);let node;
     while(node=walker.nextNode()){
      if(node.parentElement.closest('.katex,.public-notes,.problem-votes'))continue;
      if(/\\[()[\]]|(?<!\\)\$/.test(node.textContent))failures.push({id:rows[i].id,view,unrendered:node.textContent.slice(0,180)});
     }
     if(i%25===0)await new Promise(resolve=>setTimeout(resolve,0));
    }
   }
   host.remove();return {...result,failures};
  });
  assert.deepEqual(audit.failures,[],'Every active card renders in both layouts');
  await page.evaluate(async()=>{
   document.getElementById('view').value='compact';ATLAS_DEBUG.filter();
   const base=ATLAS_DEBUG.data.cards.find(ATLAS_DEBUG.isActive);
   const fixture={...structuredClone(base),id:'TCS-99990',title:'Formula preview fixture',statement_review:null,working_summary:null,evidence:'source',formal:'Fallback.',source_formulation:{text:'A '.repeat(345)+'\\(\\frac{a+b}{c+d}\\) then a long tail '.repeat(10)},related_problem_ids:[],references:[{id:'fixture',title:'A bound of \\(n^{2}\\)',url:'https://example.org/'}]};
   await ATLAS_DEBUG.applyPublication({version:'math-fixture',cards:[fixture],meta:ATLAS_DEBUG.data.meta,areas:ATLAS_DEBUG.data.areas});
   await ATLAS_DEBUG.go(fixture.id);
  });
  assert(await page.locator('#TCS-99990>.source-statement .katex').count(),'Source excerpts render math');
  assert.equal(await page.locator('#TCS-99990 .katex-error').count(),0,'Long previews retain a whole formula');
  await page.locator('#TCS-99990 .card-details').evaluate(el=>el.open=true);
  assert(await page.locator('#TCS-99990 .references .katex').count(),'Reference titles render math');
  await page.locator('#view').selectOption('full');await page.evaluate(()=>ATLAS_DEBUG.go('TCS-99990'));
  assert(await page.locator('#TCS-99990 .source-statement .katex').count());
  for(const id of ['TCS-0001','TCS-0305','TCS-6523','TCS-6575']){
   if(!await page.evaluate(id=>ATLAS_DEBUG.data.cards.some(c=>c.id===id),id))continue;
   await page.locator('#view').selectOption('compact');await page.evaluate(id=>ATLAS_DEBUG.go(id),id);
   await page.setViewportSize({width:390,height:844});await page.waitForTimeout(80);
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'Inline math must not widen a mobile page');
  }
  const dir=path.resolve(__dirname,'../research/latex-formatting-20260912');fs.mkdirSync(dir,{recursive:true});
  await page.locator('#view').selectOption('full');await page.evaluate(()=>ATLAS_DEBUG.go('TCS-6523'));
  await page.screenshot({path:dir+'/mobile.png'});
  await page.setViewportSize({width:1440,height:1000});await page.evaluate(()=>ATLAS_DEBUG.go('TCS-6523'));await page.screenshot({path:dir+'/desktop.png'});
  assert.deepEqual(errors,[]);fs.writeFileSync(dir+'/browser-audit.json',JSON.stringify({...audit,errors},null,2)+'\n');console.log(JSON.stringify({...audit,errors}));
 }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
