const { chromium } = require('playwright');
const assert = require('assert');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
  try {
    const page = await browser.newPage({viewport:{width:1440,height:1000}});
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto('http://127.0.0.1:8766/?view=compact');
    await page.waitForFunction(() => window.ATLAS_DEBUG);
    const imported = await page.evaluate(() => ATLAS_DEBUG.data.cards.filter(c => c.proposal_import?.batch === 'fundamental-20260910'));
    assert.equal(imported.length,144);
    assert.equal(new Set(imported.map(c=>c.id)).size,144);
    assert(imported.every(c=>c.evidence==='source' && !c.scope_exclusion && c.area===c.proposal_import.category));
    const selected = ['kls','cerny','li-li-network-coding','general-sparse-linear-systems','deterministic-static-dictionary','hadwiger','planted-clique'];
    for (const slug of selected) {
      const card = imported.find(c=>c.proposal_import.slug===slug);
      await page.fill('#search',card.id);
      await page.waitForFunction(id=>ATLAS_DEBUG.state.matches.length===1 && ATLAS_DEBUG.state.matches[0].id===id,card.id);
      const rendered = page.locator('#'+card.id);
      assert((await rendered.innerText()).includes(card.title));
      assert((await rendered.innerText()).includes('Short draft · research proposal'));
      assert(await rendered.locator('a[href="'+card.references[0].url+'"]').count());
    }
    const card = imported.find(c=>c.proposal_import.slug==='li-li-network-coding');
    await page.goto('http://127.0.0.1:8766/?view=compact#'+card.id);
    await page.locator('#'+card.id).waitFor();
    await page.locator('#'+card.id+' [data-action="note"]').click();
    await page.locator('#note-'+card.id).fill('Proposal import: keep this note.');
    await page.reload();
    await page.locator('#'+card.id+' [data-action="note"]').click();
    assert.equal(await page.locator('#note-'+card.id).inputValue(),'Proposal import: keep this note.');
    await page.setViewportSize({width:390,height:844});
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    assert.deepEqual(errors,[]);
    const report = {imported:144,checks:['unique IDs','approved categories','draft evidence labels','search in seven categories','source links','direct link','note persistence','mobile width'],errors};
    fs.writeFileSync(path.join(__dirname,'proposals-results.json'),JSON.stringify(report,null,2));
    console.log(JSON.stringify(report,null,2));
  } finally { await browser.close(); }
})().catch(error=>{console.error(error);process.exitCode=1;});
