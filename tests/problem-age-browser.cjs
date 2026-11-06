'use strict';
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');

(async () => {
  const site = path.resolve(__dirname, '../build');
  const catalog = JSON.parse(fs.readFileSync(path.join(site, 'catalog.json')));
  const live = process.argv[2];
  const errors = [], writes = [], checks = [];
  let server, browser;
  try {
    let base = live;
    if (!base) {
      server = http.createServer((req, res) => {
        const name = new URL(req.url, 'http://localhost').pathname;
        const file = path.resolve(site, '.' + (name === '/' ? '/index.html' : name));
        if (!file.startsWith(site + path.sep) || !fs.existsSync(file) || !fs.statSync(file).isFile()) { res.writeHead(404); res.end(); return; }
        res.setHeader('content-type', ({'.html':'text/html', '.js':'text/javascript', '.json':'application/json', '.css':'text/css', '.woff2':'font/woff2'})[path.extname(file)] || 'application/octet-stream');
        fs.createReadStream(file).pipe(res);
      });
      await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
      base = `http://127.0.0.1:${server.address().port}/`;
    }
    browser = await chromium.launch({executablePath:'/usr/bin/google-chrome', args:['--no-sandbox']});
    const context = await browser.newContext();
    let publishedVersion = catalog.meta.version;
    await context.route('**/api/**', async route => {
      const request = route.request();
      if (request.method() !== 'GET') { writes.push(request.method() + ' ' + request.url()); return route.abort(); }
      if (live) return route.continue();
      if (request.url().includes('/api/selection')) return route.fulfill({json:{version:catalog.meta.final_selection.version, choices:[]}});
      if (request.url().includes('/api/votes')) return route.fulfill({json:{votes:[], mine:[]}});
      return route.fulfill({json:{notes:[], next:null}});
    });
    if (!live) await context.route('**/version.json', route => route.fulfill({json:{version:publishedVersion}}));
    const page = await context.newPage();
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(base);
    await page.waitForFunction(() => window.ATLAS_DEBUG && window.ATLAS_SELECTION?.loaded && window.ATLAS_PROBLEM_AGE);
    const actualVersion = await page.evaluate(() => TCS_ATLAS.meta.version);
    assert.equal(actualVersion, catalog.meta.version, 'Test the intended reader publication');
    const expected = catalog.cards.filter(c => c.problem_origin).map(c => c.id);
    const covered = await page.evaluate(ids => ids.filter(id => !TCS_ATLAS.cards.find(c => c.id === id)?.problem_origin), expected);
    assert.deepEqual(covered, [], 'Every assessed origin is available in the reader');
    const samples = [
      ['TCS-0001', 'Origin: 1971'],
      ['TCS-7314', 'Origin: c. 1980'],
      ['TCS-6535', 'Origin: c. 1986–1990'],
      ['TCS-0164', 'Documented by 1966'],
      ['TCS-1338', 'Origin: 2026'],
      ['TCS-7529', 'Origin: 1994']
    ];
    for (const width of [320, 390, 1440]) {
      await page.setViewportSize({width, height:1000});
      for (const view of ['compact', 'full']) {
        await page.locator('#view').selectOption(view);
        for (const [id, prefix] of samples) {
          await page.evaluate(id => ATLAS_DEBUG.go(id), id);
          const card = page.locator('#' + id);
          const summary = card.locator('.problem-age > summary');
          await summary.waitFor({state:'visible'});
          const label = await summary.innerText();
          assert(label.startsWith(prefix), `${id}: ${label}`);
          assert(label.includes('year'), `${id}: missing age`);
          assert(await card.locator('[data-selection-action="color"]').isVisible(), 'Color control stays visible');
          await card.locator('.problem-age').evaluate(el => { el.open = true; });
          assert((await card.locator('.problem-age-body').innerText()).length > 80);
          assert(await card.locator('.problem-age-body a').count() > 0, 'Historical evidence is linked');
          assert.equal(await card.locator('.katex-error').count(), 0);
          assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 2), `${id}: horizontal overflow at ${width}`);
          checks.push({id, view, width, label});
        }
      }
    }
    if (!live) {
      await page.evaluate(() => ATLAS_DEBUG.go('TCS-0001'));
      await page.locator('#TCS-0001 .problem-age').evaluate(el => { el.open = true; });
      publishedVersion += '-age-state-test';
      await page.evaluate(async version => {
        const old = TCS_ATLAS.cards.find(c => c.id === 'TCS-0001');
        const card = {...old, title:old.title + ' (publication test)'};
        const meta = {...TCS_ATLAS.meta, version};
        await ATLAS_DEBUG.applyPublication({version, cards:[card], areas:TCS_ATLAS.areas, meta});
      }, publishedVersion);
      assert(await page.locator('#TCS-0001 .problem-age').evaluate(el => el.open), 'Origin explanation survives a live data update');
      await page.evaluate(() => document.dispatchEvent(new CustomEvent('atlas:selection', {detail:{problemId:'TCS-0001'}})));
      await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
      assert(await page.locator('#TCS-0001 .problem-age').evaluate(el => el.open), 'Origin explanation survives shared choice refresh');
    }
    assert.deepEqual(errors, []);
    assert.deepEqual(writes, [], 'No writes to the shared service');
    const result = {mode:live ? 'live' : 'local', version:actualVersion, covered:expected.length, layouts:checks.length, errors, writes, checks};
    const dir = process.env.ATLAS_TEST_ARTIFACT_DIR;
    if (dir) { fs.mkdirSync(dir, {recursive:true}); fs.writeFileSync(path.join(dir, live ? 'age-live.json' : 'age-local.json'), JSON.stringify(result, null, 2)); }
    console.log(JSON.stringify({mode:result.mode, version:actualVersion, covered:expected.length, layouts:checks.length, errors, writes}));
  } finally {
    if (browser) await browser.close();
    if (server) await new Promise(resolve => server.close(resolve));
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
