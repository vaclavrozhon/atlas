const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs/promises');
const path=require('node:path');
const base=process.env.ATLAS_URL||'http://127.0.0.1:8768/';
const dir=path.resolve(__dirname,'../research/ui-simplification-20260911');

(async()=>{
  await fs.mkdir(dir,{recursive:true});
  const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  try{
    const context=await browser.newContext({viewport:{width:1440,height:1000}});
    await context.route('https://api.github.com/**',route=>route.fulfill({json:[]}));
    await context.route('https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/votes',route=>route.fulfill({json:{votes:[],mine:[]}}));
    await context.addInitScript(()=>{
      if(!localStorage.getItem('tcs-atlas-notes'))localStorage.setItem('tcs-atlas-notes',JSON.stringify({'TCS-6575':'Keep this private text'}));
      if(!localStorage.getItem('tcs-atlas-saved'))localStorage.setItem('tcs-atlas-saved',JSON.stringify(['TCS-6575']));
      if(!localStorage.getItem('tcs-atlas-contribution-drafts'))localStorage.setItem('tcs-atlas-contribution-drafts',JSON.stringify({problem:{title:'An old unsent question',category:'online',statement:'Original statement.',definitions:'Original definitions.',answer:'Original resolution target.',why:'Original motivation.',sources:'https://example.org/original'}}));
    });
    const page=await context.newPage(),errors=[];page.on('pageerror',e=>errors.push(e.message));
    // Freeze background publication until the explicit live-update scenario below.
    await page.route('**/version.json',async r=>r.fulfill({json:{version:await page.evaluate(()=>TCS_ATLAS.meta.version)}}));
    await page.goto(base);
    await page.waitForFunction(()=>window.ATLAS_DEBUG);
    const inventory=await page.evaluate(()=>({
      active:ATLAS_DEBUG.data.cards.filter(c=>!c.scope_exclusion&&!['resolved','excluded'].includes(c.status)).map(c=>c.id),
      inactive:ATLAS_DEBUG.data.cards.filter(c=>c.scope_exclusion||['resolved','excluded'].includes(c.status)).map(c=>c.id),
      areas:ATLAS_DEBUG.data.areas.map(a=>a.label),
      top100:ATLAS_DEBUG.data.meta.benchmarks.top100.total,
      top500:ATLAS_DEBUG.data.meta.benchmarks.top500.total,
      top1000:ATLAS_DEBUG.data.meta.benchmarks.top1000.total
    }));
    const ids=()=>page.evaluate(()=>ATLAS_DEBUG.state.matches.map(c=>c.id));
    assert.deepEqual(new Set(await ids()),new Set(inventory.active));
    assert.equal(await page.locator('#areas .area-group').count(),0);
    assert.deepEqual(await page.locator('#areas label > span:nth-child(2)').allTextContents(),inventory.areas);
    assert.equal((await page.locator('#areas .count').allTextContents()).reduce((n,s)=>n+Number(s.replaceAll(',','')),0),inventory.active.length);
    const removed=['area-search','saved-only','advanced-filters','new-only','textbook-only','evidence','status','scope','group','reason','year','random','export','export-community','sort','live-status','benchmark-note','coverage'];
    for(const id of removed)assert.equal(await page.locator(`#${id}`).count(),0,id);
    assert.equal(await page.locator('.save,[data-note],.pill,[data-action="note"],[data-action="copy"]').count(),0);
    assert.equal(await page.locator('a[download]').count(),0);
    assert(!/editorial|provisional/.test((await page.locator('.importance-badge').allTextContents()).join(' ')));
    await page.screenshot({path:path.join(dir,'catalogue-desktop.png')});

    const completeOrder=await ids();
    await page.locator('#view').selectOption('full');
    assert.deepEqual(await ids(),completeOrder);assert.equal(await page.locator('.compact-card').count(),0);
    assert((await page.locator('.card-section h3').allTextContents()).includes('Why it matters'));
    assert(!(await page.locator('.card-details h3,.card-section h3').allTextContents()).some(x=>/Importance in this category|Top 100 selection/.test(x)));
    await page.reload();await page.waitForFunction(()=>window.ATLAS_DEBUG);
    assert.equal(await page.locator('#view').inputValue(),'full');
    await page.locator('#view').selectOption('compact');
    for(const selection of ['top100','top500','top1000']){
      await page.locator('#benchmark').selectOption(selection);
      assert.equal((await ids()).length,inventory[selection]);
      const original=await ids();
      const area=await page.locator('#areas input').first().getAttribute('value');
      await page.locator('#areas input').first().check();
      const narrowed=await ids();assert(narrowed.length>0);assert(narrowed.every(id=>original.includes(id)));
      const outside=await page.evaluate(({area,selection})=>ATLAS_DEBUG.data.cards.find(c=>c.area===area&&!['resolved','excluded'].includes(c.status)&&c.importance_rank>ATLAS_DEBUG.data.meta.benchmarks[selection].quotas.large)?.id,{area,selection});
      if(outside){await page.locator('#search').fill(outside);await page.waitForFunction(()=>ATLAS_DEBUG.state.matches.length===0);}
      await page.locator('#clear').click();
    }
    const uncertain=await page.evaluate(()=>ATLAS_DEBUG.data.cards.find(c=>c.status==='uncertain'&&!c.scope_exclusion).id);
    await page.locator('#search').fill(uncertain);await page.waitForFunction(id=>ATLAS_DEBUG.state.matches.length===1&&ATLAS_DEBUG.state.matches[0].id===id,uncertain);
    await page.locator('#clear').click();
    for(const id of inventory.inactive){await page.evaluate(id=>ATLAS_DEBUG.go(id),id);assert.equal(await page.locator(`#${id}`).count(),0);}
    if(inventory.inactive.length){
      await page.goto(base+'?scope=all&status=resolved&detail=reviewed&group=small&collection=textbooks&sort=oldest#'+inventory.inactive[0]);
      await page.waitForFunction(()=>window.ATLAS_DEBUG);
      assert.deepEqual(new Set(await ids()),new Set(inventory.active));
      assert.equal(new URL(page.url()).search,'');
      assert.equal(await page.locator('#'+inventory.inactive[0]).count(),0);
    }
    await page.locator('header a[href="#methodology"]').click();
    assert(await page.locator('#methodology').evaluate(el=>el.open));
    assert.equal(await page.locator('#methodology a').count(),0);
    assert.equal(await page.locator('#methodology #coverage-table tbody tr').count(),inventory.areas.length);
    assert((await page.locator('#selection-plan').textContent()).includes('same ranking within each category'));
    assert.match(await page.locator('#benchmark-goal').textContent(), /primary goal is a benchmark of 500 problems.*Top 100 is a priority subset/);

    await page.locator('#new-problem').click();
    assert.equal(await page.locator('#problem-fields input,#problem-fields select,#problem-fields textarea').count(),4);
    const restored=await page.locator('#proposal-statement').inputValue();
    for(const text of ['Original statement.','Original definitions.','Original resolution target.','Original motivation.'])assert(restored.includes(text));
    await page.locator('#proposal-title').fill('An old unsent question, revised');
    await page.locator('#close-contribution').click();await page.locator('#new-problem').click();
    assert.equal(await page.locator('#proposal-statement').inputValue(),restored,'Legacy draft migration must not duplicate text');
    await page.screenshot({path:path.join(dir,'form-desktop.png')});
    await page.locator('#close-contribution').click();
    for(const width of [320,390,768,1440]){
      await page.setViewportSize({width,height:844});await page.evaluate(()=>window.scrollTo(0,0));
      assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`Page overflow at ${width}`);
      if(width<720){await page.locator('#filters-toggle').click();assert(await page.locator('#filters').isVisible());await page.locator('#filters-toggle').click();}
      await page.locator('#new-problem').click();
      assert(await page.locator('#contribution-dialog').evaluate(el=>el.scrollWidth<=el.clientWidth));
      if(width===390)await page.screenshot({path:path.join(dir,'form-mobile.png')});
      await page.locator('#close-contribution').click();
      if(width===390)await page.screenshot({path:path.join(dir,'catalogue-mobile.png')});
    }

    // The actual polling path must preserve a public draft and remove a newly
    // resolved reading card even when its details were open before publication.
    await page.locator('#clear').click();
    const activeId=await page.locator('.problem-card').first().getAttribute('id');
    await page.locator(`#${activeId} .card-details > summary`).click();
    await page.locator(`#${activeId} [data-public-note]`).click();
    await page.locator('#public-note-text').fill('Public draft survives an update.');
    await page.locator('#public-note-text').evaluate(el=>el.setSelectionRange(6,6));
    const update=await page.evaluate(id=>({version:'simplified-live-fixture',cards:ATLAS_DEBUG.data.cards.map(c=>c.id===id?{...c,status:'resolved'}:c),areas:ATLAS_DEBUG.data.areas,meta:{...ATLAS_DEBUG.data.meta,version:'simplified-live-fixture'}}),activeId);
    await page.route('**/version.json',r=>r.fulfill({json:{version:update.version}}));
    await page.route('**/catalog.json',r=>r.fulfill({json:update}));
    await page.waitForFunction(id=>ATLAS_DEBUG.data.cards.find(c=>c.id===id).status==='resolved',activeId);
    await page.waitForFunction(id=>!document.getElementById(id),activeId);
    assert.equal(await page.locator('#public-note-text').inputValue(),'Public draft survives an update.');
    assert(await page.locator('#public-note-text').evaluate(el=>document.activeElement===el&&el.selectionStart===6));
    assert.equal(await page.locator('#live-status').count(),0);
    await page.locator('#close-contribution').click();
    assert(!(await ids()).includes(activeId));
    assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('tcs-atlas-notes'))['TCS-6575']),'Keep this private text');
    assert.deepEqual(errors,[]);
    const report={active:inventory.active.length,hidden_inactive:inventory.inactive,top100:inventory.top100,top1000:inventory.top1000,checks:['approved controls removed','private text retained','flat category registry and active counts','full and compact layouts','importance order independent of layout','nested benchmarks and filters without backfilling','unverified problems remain','retired/resolved problems blocked in direct and legacy links','About contains selection plan without downloads','four-field form with lossless legacy draft migration','320–1440px layouts','silent publication removes resolved reading card and preserves public draft/caret'],errors};
    await fs.writeFile(path.join(dir,'simplified-ui.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
