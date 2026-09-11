const {chromium}=require('playwright');
const assert=require('assert'),fs=require('fs'),path=require('path');
(async()=>{
  const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
  try{
    const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    await page.route('**/version.json',r=>r.fulfill({json:{version:JSON.parse(fs.readFileSync(path.join(__dirname,'../site/catalog.json'))).meta.version}}));
    await page.goto('http://127.0.0.1:8766/?view=compact');
    await page.waitForFunction(()=>window.ATLAS_DEBUG);
    // Disable network polling for this deterministic whole-catalogue fixture.
    await page.route('**/version.json',r=>r.fulfill({json:{version:'bulk-test'}}));
    const report=await page.evaluate(async()=>{
      const d=ATLAS_DEBUG.data;
      const first=document.querySelector('.problem-card');
      await ATLAS_DEBUG.go(first.id);
      first.querySelector('details').open=true;
      const note=first.querySelector('textarea');note.value='Keep my draft note';note.dispatchEvent(new Event('input',{bubbles:true}));note.focus({preventScroll:true});note.setSelectionRange(4,4);
      const beforeCount=document.querySelectorAll('.problem-card').length;
      const beforeTop=first.getBoundingClientRect().top;
      const oldId=first.id,noteId=note.id;
      const changed=d.cards.map(c=>({...c,importance_count:(c.importance_count||0)+1}));
      // Re-ranking the reading card near the end must not render the prefix
      // of thousands of cards before it.
      const reading=changed.find(c=>c.id===oldId);reading.importance={...reading.importance,score:0};
      let ticks=0;const timer=setInterval(()=>ticks++,10);
      const longTasks=[];const observer=new PerformanceObserver(list=>longTasks.push(...list.getEntries().map(e=>e.duration)));
      observer.observe({type:'longtask'});
      const start=performance.now();
      await ATLAS_DEBUG.applyPublication({version:'bulk-test',cards:changed,meta:d.meta,areas:d.areas});
      await new Promise(r=>setTimeout(r,100));
      const duration=performance.now()-start;clearInterval(timer);observer.disconnect();
      const now=document.getElementById(oldId),editing=document.getElementById(noteId);
      return {updated:changed.length,beforeCount,afterCount:document.querySelectorAll('.problem-card').length,durationMs:Math.round(duration),eventLoopTicks:ticks,maxLongTaskMs:Math.round(Math.max(0,...longTasks)),note:editing.value,focus:document.activeElement===editing&&editing.selectionStart===4,open:now.querySelector('details').open,scrollDelta:Math.abs(now.getBoundingClientRect().top-beforeTop),candidateCount:ATLAS_DEBUG.state.matches.length,rankPosition:ATLAS_DEBUG.state.matches.findIndex(c=>c.id===oldId)};
    });
    assert(report.updated>6500);
    assert(report.rankPosition>0.9*report.candidateCount);
    assert(report.afterCount<=report.beforeCount+17,JSON.stringify(report));
    assert(report.eventLoopTicks>5,JSON.stringify(report));
    assert(report.maxLongTaskMs<1000,JSON.stringify(report));
    assert.equal(report.note,'Keep my draft note');assert(report.focus&&report.open);
    assert(report.scrollDelta<3,JSON.stringify(report));
    assert.deepEqual(errors,[]);
    fs.writeFileSync(path.join(__dirname,'bulk-updates-results.json'),JSON.stringify({...report,errors},null,2));
    console.log(JSON.stringify({...report,errors},null,2));
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
