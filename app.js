/* The public reader always browses the selected benchmark. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const math = window.ATLAS_MATH, definitions = window.ATLAS_DEFINITIONS;
  const batch = 24;
  const state = {matches: [], shown: 0};
  const statusLabels = {open: 'Likely open', solved: 'Public solution likely', uncertain: 'Uncertain'};
  let data, byId, labels, searchable, subsets, browsingOrder, fetching = false;
  const esc = text => String(text ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const normalize = text => math.plain(text).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const textOnlyLinks = text => text.replace(/\[([^\]]+)\]\(definitions\.html#[a-z-]+\)/g, '$1');
  function status(card) {
    const flag = card.solution_assessment?.solved;
    return flag === true ? 'solved' : flag === false ? 'open' : 'uncertain';
  }
  function summary(card) {
    const sentences = card.working_summary?.sentences || [];
    const text = sentences.length ? sentences.slice(0, /asks (whether|for)|\?$/.test(sentences[0]) ? 1 : 2).join(' ') : math.excerpt(card.formal, 205);
    return textOnlyLinks(text);
  }
  function urlLink(url, title) {
    try {
      const target = new URL(url);
      if (['https:', 'http:'].includes(target.protocol)) {
        return '<a href="' + esc(target.href) + '" target="_blank" rel="noopener noreferrer">' + esc(title) + '</a>';
      }
    } catch { /* A reference without a usable link still has a title. */ }
    return esc(title);
  }
  function assessment(card) {
    const a = card.solution_assessment;
    if (!a) return '';
    const percent = value => new Intl.NumberFormat('en', {style:'percent', maximumFractionDigits:2}).format(value);
    const probability = a.probability_solved_upper_bound != null ? '&lt;' + percent(a.probability_solved_upper_bound) :
      a.probability_solved != null ? percent(a.probability_solved) : '';
    let result = '<section><h3>Solution assessment</h3><p class="assessment-meta">' +
      (probability ? probability + ' probability that a public solution exists · ' : '') + esc(a.reviewed_on) + '</p>';
    if (a.solution_url) {
      result += '<p>' + urlLink(a.solution_url, 'Public solution') + ' · <time>' + esc(a.public_date) + '</time>' +
        (a.attribution?.credit ? ' · ' + esc(a.attribution.credit) : '') + '</p>';
    }
    if (a.reason) result += definitions.paragraphs(a.reason);
    const evidence = (a.sources || []).filter(r => r.url !== a.solution_url);
    if (evidence.length) result += '<ul class="source-list">' + evidence.map(r => '<li>' + urlLink(r.url, r.title) + '</li>').join('') + '</ul>';
    return result + '</section>';
  }
  function detail(card) {
    const refs = card.references || [];
    const related = (card.related_problem_ids || []).map(id => byId.get(id)).filter(Boolean);
    const technical = definitions.model(card) +
      (card.answer_criterion ? '<h3>What would settle it?</h3>' + definitions.paragraphs(card.answer_criterion) : '');
    const history = window.ATLAS_PROBLEM_AGE?.html(card) || '';
    const background = [card.why, card.context].filter(Boolean);
    const progress = (card.progress || []).map(p => '<li><strong>' + esc(p.date) + '</strong> ' + esc(p.text) + '</li>').join('');
    let html = '<section><h3>Problem statement</h3>' + definitions.paragraphs(card.formal, 'formal') + '</section>' + assessment(card);
    if (technical) html += '<details class="subdetail" data-section="definitions"><summary>Definitions &amp; proof criteria</summary><div>' + technical + '</div></details>';
    if (background.length || progress || history || refs.length) {
      html += '<details class="subdetail" data-section="background"><summary>Background &amp; references</summary><div>' +
        background.map(t => definitions.paragraphs(t)).join('') + history +
        (progress ? '<h3>Documented progress</h3><ul>' + progress + '</ul>' : '') +
        (refs.length ? '<h3>References</h3><ul class="source-list">' + refs.map(r =>
          '<li>' + urlLink(r.url, r.title) + (r.authors ? ' · ' + esc(r.authors) : '') + '</li>').join('') + '</ul>' : '') +
        '</div></details>';
    }
    if (related.length) html += '<details class="subdetail" data-section="related"><summary>Related problems (' + related.length + ')</summary><ul>' +
      related.map(r => '<li><a href="#' + encodeURIComponent(r.id) + '">' + esc(r.title) + '</a></li>').join('') + '</ul></details>';
    return html + '<div class="card-links"><a href="#' + encodeURIComponent(card.id) + '">Permalink</a><a href="map.html#' +
      encodeURIComponent(card.id) + '">View on map</a><span>' + esc(card.id) + '</span></div>';
  }
  function renderCard(card) {
    const id = esc(card.id), key = status(card);
    return '<article class="problem-card" id="' + id + '"><div class="card-meta"><span class="category">' +
      esc(labels.get(card.area) || card.area) + '</span><span class="status ' + key + '">' + statusLabels[key] +
      '</span></div><h2><button type="button" class="card-toggle" aria-label="' + esc(math.plain(card.title)) + '" aria-expanded="false" aria-controls="detail-' + id +
      '"><span>' + esc(card.title) + '</span><span class="toggle-icon" aria-hidden="true"></span></button></h2>' +
      '<div class="excerpt">' + math.paragraphs(summary(card)) + '</div><div class="card-detail" id="detail-' + id + '" hidden></div></article>';
  }
  function expand(el, opened) {
    const button = el.querySelector('.card-toggle'), body = el.querySelector('.card-detail');
    button.setAttribute('aria-expanded', String(opened));
    body.hidden = !opened;
    if (opened && !body.hasChildNodes()) {
      body.innerHTML = detail(byId.get(el.id));
      math.render(body);
    }
  }
  function appendTo(limit) {
    const count = Math.min(limit, state.matches.length);
    if (count > state.shown) {
      const range = document.createRange();
      const added = range.createContextualFragment(state.matches.slice(state.shown, count).map(renderCard).join(''));
      math.render(added);
      $('cards').appendChild(added);
      state.shown = count;
    }
    $('more').hidden = state.shown >= state.matches.length;
  }
  function replaceURL(url) {
    try { history.replaceState(null, '', url); }
    catch (error) { if (location.protocol !== 'file:' || error.name !== 'SecurityError') throw error; }
  }
  function updateURL() {
    const url = new URL(location.href);
    for (const [key, value] of [['q', $('search').value.trim()], ['area', $('area-filter').value], ['status', $('solution-filter').value], ['selection', $('selection-filter').value]]) {
      if (value) url.searchParams.set(key, value); else url.searchParams.delete(key);
    }
    url.searchParams.delete('benchmark');
    url.hash = '';
    replaceURL(url);
  }
  function filter(sync = true, limit = batch) {
    const query = normalize($('search').value.trim());
    const area = $('area-filter').value, solution = $('solution-filter').value, subset = subsets.get($('selection-filter').value);
    const terms = query.split(/\s+/).filter(Boolean);
    state.matches = browsingOrder.filter(c => (!area || c.area === area) && (!solution || status(c) === solution) &&
      (!subset || subset.has(c.id)) && terms.every(t => searchable.get(c.id).includes(t)));
    const count = [area, solution, subset].filter(Boolean).length;
    $('filter-count').textContent = count ? '(' + count + ')' : '';
    $('clear').hidden = !count && !query;
    $('result-count').parentElement.classList.toggle('unfiltered', !count && !query);
    $('result-count').textContent = state.matches.length.toLocaleString('en') + (state.matches.length === 1 ? ' problem' : ' problems');
    $('empty').hidden = Boolean(state.matches.length);
    $('cards').replaceChildren();
    state.shown = 0;
    appendTo(limit);
    if (sync) updateURL();
  }
  function clearFilters() {
    for (const id of ['search', 'area-filter', 'solution-filter', 'selection-filter']) $(id).value = '';
  }
  function readURL() {
    const params = new URLSearchParams(location.search);
    $('search').value = params.get('q') || '';
    for (const [id, key] of [['area-filter','area'], ['solution-filter','status'], ['selection-filter','selection']]) {
      const input = $(id), value = params.get(key);
      input.value = [...input.options].some(option => option.value === value) ? value : '';
    }
  }
  function go(id, scroll = true) {
    if (!byId.has(id)) return false;
    if (!state.matches.some(c => c.id === id)) {
      clearFilters(); filter(false);
      const hash = location.hash;
      updateURL();
      if (hash) replaceURL(location.pathname + location.search + hash);
    }
    const index = state.matches.findIndex(c => c.id === id);
    appendTo(Math.max(state.shown, index + 1));
    const el = $(id);
    expand(el, true);
    if (scroll) requestAnimationFrame(() => {
      el.scrollIntoView({block:'start'});
      el.querySelector('.card-toggle').focus({preventScroll:true});
    });
    return true;
  }
  function openHash(scroll = true) {
    const id = location.hash.slice(1);
    if (/^TCS-\d+$/.test(id) && !go(id, scroll)) {
      $('result-count').parentElement.classList.remove('unfiltered');
      $('result-count').textContent = 'This problem is outside the benchmark. Showing ' + state.matches.length + ' problems.';
    }
  }
  function applyCatalogue(next, initial = false) {
    if (next?.meta?.scope !== 'TCS500' || !Array.isArray(next.areas) || !Array.isArray(next.cards) ||
        !next.cards.length || next.cards.some(c => c.selection?.color !== 'green')) return false;
    const opened = new Map();
    if (!initial) {
      for (const button of document.querySelectorAll('.card-toggle[aria-expanded="true"]')) {
        const card = button.closest('article');
        opened.set(card.id, [...card.querySelectorAll('.subdetail[open]')].map(el => el.dataset.section));
      }
    }
    const shown = Math.max(batch, state.shown);
    const category = $('area-filter').value;
    data = next; window.TCS_ATLAS = next;
    byId = new Map(data.cards.map(c => [c.id, c]));
    labels = new Map(data.areas.map(a => [a.area, a.label]));
    // Show a problem from each area before starting the next round, retaining the original order within it.
    const groups = data.areas.map(a => data.cards.filter(c => c.area === a.area));
    browsingOrder = [];
    for (let i = 0; groups.some(group => group.length > i); i++) {
      for (const group of groups) if (group[i]) browsingOrder.push(group[i]);
    }
    subsets = new Map(Object.entries(data.meta.green_subsets.member_ids).map(([size, ids]) => ['top' + size, new Set(ids)]));
    searchable = new Map(data.cards.map(c => [c.id, normalize([c.id, c.title, labels.get(c.area), c.formal,
      ...(c.working_summary?.sentences || []), ...c.references.map(r => [r.title, r.authors].join(' '))].join(' '))]));
    const select = $('area-filter');
    select.replaceChildren(new Option('All categories', ''));
    [...data.areas].sort((a,b) => a.label.localeCompare(b.label)).forEach(a => select.add(new Option(a.label, a.area)));
    select.value = labels.has(category) ? category : '';
    if (initial) readURL();
    filter(false, shown);
    for (const [id, sections] of opened) {
      const el = $(id);
      if (!byId.has(id) || !el) continue;
      expand(el, true);
      for (const section of el.querySelectorAll('.subdetail')) section.open = sections.includes(section.dataset.section);
    }
    openHash(initial);
    return true;
  }
  async function checkUpdates() {
    if (fetching || document.hidden || location.protocol === 'file:') return;
    fetching = true;
    try {
      const response = await fetch('version.json', {cache:'no-store'});
      if (!response.ok) return;
      const marker = await response.json();
      if (!marker.version || marker.version === data?.meta.version) return;
      const full = await fetch('catalog.json', {cache:'no-store'});
      if (full.ok) {
        const next = await full.json();
        if (next.meta?.version === marker.version && applyCatalogue(next, !data)) $('load-error').hidden = true;
      }
    } catch { /* The bundled edition is available offline. */ }
    finally { fetching = false; }
  }
  $('cards').addEventListener('click', event => {
    const button = event.target.closest('.card-toggle');
    if (button) {
      const card = button.closest('article');
      const opening = button.getAttribute('aria-expanded') === 'false';
      expand(card, opening);
      if (!opening && location.hash === '#' + card.id) replaceURL(location.pathname + location.search);
    }
  });
  $('more').onclick = () => appendTo(state.shown + batch);
  $('search').addEventListener('input', () => filter());
  for (const id of ['area-filter', 'solution-filter', 'selection-filter']) $(id).addEventListener('change', () => filter());
  $('clear').onclick = $('empty-reset').onclick = () => { clearFilters(); filter(); $('search').focus(); };
  document.addEventListener('click', event => { if (!$('filters').contains(event.target)) $('filters').open = false; });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && $('filters').open) { $('filters').open = false; $('filters').querySelector('summary').focus(); }
    if (event.key === '/' && !event.metaKey && !event.ctrlKey && !event.altKey &&
        !event.target.closest('input, textarea, select, [contenteditable], dialog')) { event.preventDefault(); $('search').focus(); }
  });
  window.addEventListener('hashchange', () => openHash());
  window.addEventListener('popstate', () => { if (data) { readURL(); filter(false); openHash(); } });
  window.addEventListener('pageshow', checkUpdates);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) checkUpdates(); });
  $('load-error').hidden = applyCatalogue(window.TCS_ATLAS, true);
  setInterval(checkUpdates, 60000);
  checkUpdates();
  window.ATLAS_DEBUG = {get data() { return data; }, state, go, renderCard, detail, applyCatalogue, checkUpdates, math: math.render};
})();
