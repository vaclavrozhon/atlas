const {chromium} = require('playwright');
const assert = require('assert');
const fs = require('fs');
const path = require('path');

(async () => {
  const root = path.resolve(__dirname, '..');
  const library = JSON.parse(fs.readFileSync(path.join(root, 'site/library/library.json')));
  const areas = JSON.parse(fs.readFileSync(path.join(root, 'site/library/area-coverage.json'))).areas;
  const browser = await chromium.launch({executablePath:'/home/vasek/.cache/ms-playwright/chromium-1228/chrome-linux64/chrome',headless:true,args:['--no-sandbox']});
  try {
    const context = await browser.newContext({viewport:{width:1440,height:1000}});
    const page = await context.newPage(), errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto('http://127.0.0.1:8766/');
    await page.waitForFunction(() => window.ATLAS_DEBUG);
    assert.equal(await page.locator('#coverage-table tbody a[href^="library/"]').count(), 35);
    const cardId = await page.locator('.problem-card').first().getAttribute('id');
    await page.locator('#'+cardId+' [data-action="note"]').click();
    await page.locator('#note-'+cardId).fill('Keep this note while browsing the source library.');
    await page.locator('header a[href="library/index.html"]').click();
    await page.waitForURL('**/library/index.html');
    assert.equal(await page.locator('.source-card:not([hidden])').count(), library.sources.length);
    assert.equal(await page.locator('.source-entries li').count(), library.meta.annotated_entries);
    assert.equal(await page.locator('.source-entries[open]').count(), 0);
    const filterResults = [];
    for (const area of areas) {
      await page.selectOption('#category', area.id);
      const ids = await page.locator('.source-card:not([hidden])').evaluateAll(els => els.map(el => el.id).sort());
      assert.deepEqual(ids, area.source_ids.slice().sort());
      const entries = await page.locator('.source-card:not([hidden]) li').count();
      assert.equal(entries, library.sources.filter(s => area.source_ids.includes(s.id)).reduce((n,s) => n+s.problems.length,0));
      assert.equal(new URL(page.url()).searchParams.get('category'), area.id);
      filterResults.push({category:area.id,sources:ids,entries});
    }
    await page.reload();
    assert.equal(await page.locator('#category').inputValue(), 'S25');
    await page.locator('#library-reset').click();
    await page.fill('#library-search', 'Szykula');
    assert.equal(await page.locator('.source-card:not([hidden])').count(),1);
    await page.fill('#library-search', 'Boson Sampling');
    assert.equal(await page.locator('.source-card:not([hidden])').count(),1);
    assert.equal(await page.locator('#quantum_algorithms .source-entries').getAttribute('open'),'');
    await page.fill('#library-search', 'zzznoresultsxyz');
    assert(await page.locator('#library-empty').isVisible());
    await page.locator('#empty-reset').click();
    await page.selectOption('#source-type','book');
    assert.equal(await page.locator('.source-card:not([hidden])').count(),library.sources.filter(s=>s.kind.includes('book')).length);
    await page.goto('http://127.0.0.1:8766/library/index.html?category=L01#vadhan2012--01');
    assert(await page.locator('#vadhan2012--01').isVisible());
    assert.equal(await page.locator('#category').inputValue(),'');
    const pdfHref = await page.locator('#vadhan2012--01 .entry-links a').first().getAttribute('href');
    assert.equal(pdfHref,'pdf/vadhan2012.pdf#page=22');
    const pdf = await context.request.get('http://127.0.0.1:8766/library/'+pdfHref.split('#')[0]);
    assert.equal(pdf.status(),200); assert((await pdf.body()).subarray(0,5).equals(Buffer.from('%PDF-')));
    await page.locator('header a[href="../index.html"]').filter({hasText:'Problems'}).click();
    await page.waitForFunction(() => window.ATLAS_DEBUG);
    await page.goto('http://127.0.0.1:8766/#'+cardId);
    await page.locator('#'+cardId+' [data-action="note"]').click();
    assert.equal(await page.locator('#note-'+cardId).inputValue(),'Keep this note while browsing the source library.');
    await page.locator('header a[href="#coverage"]').click();
    await page.locator('#coverage-table a[href="library/index.html?category=S11"]').click();
    await page.waitForURL('**/library/index.html?category=S11');
    assert.equal(await page.locator('.source-card:not([hidden])').first().getAttribute('id'),'repetitive_strings');
    await page.goto('http://127.0.0.1:8766/library/index.html');
    await page.screenshot({path:path.join(__dirname,'source-library-desktop.png')});
    await page.setViewportSize({width:390,height:844});
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
    await page.selectOption('#category','S06');
    await page.locator('#raoyehudayoff .source-entries > summary').click();
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
    await page.screenshot({path:path.join(__dirname,'source-library-mobile.png')});
    await page.goto('http://127.0.0.1:8766/');
    await page.waitForFunction(() => window.ATLAS_DEBUG);
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
    // The complete section must work directly from a portable file snapshot.
    await context.setOffline(true);
    await page.goto('file://'+path.join(root,'site/library/index.html')+'?category=L09');
    assert.equal(await page.locator('.source-card:not([hidden])').count(),2);
    await page.locator('#loop_termination h2 a').click();
    assert(await page.locator('#loop_termination .source-entries li').first().isVisible());
    await page.locator('#library-reset').click();
    const links = await page.locator('a[href]').evaluateAll(els => els.map(el => el.getAttribute('href')));
    for (const href of links) {
      if (/^(https?:|#|\?)/.test(href)) continue;
      assert(fs.existsSync(path.resolve(root,'site/library',href.split('#')[0].split('?')[0])),href);
    }
    assert.deepEqual(errors,[]);
    const report = {sources:library.sources.length,entries:library.meta.annotated_entries,categoryFilters:filterResults,
      checks:['main navigation','35 links from atlas categories','all source entries preserved','URL filters and reload','question search','accent-insensitive author search','empty state','type filter','source and entry permalinks','local PDF delivery','catalogue personal-note preservation','mobile atlas and library width','offline file reader','local links'],errors};
    fs.writeFileSync(path.join(__dirname,'source-library-results.json'),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify({sources:report.sources,entries:report.entries,categories:filterResults.length,checks:report.checks,errors}));
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode=1; });
