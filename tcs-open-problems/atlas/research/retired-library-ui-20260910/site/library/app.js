(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const norm = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[łŁ]/g, 'l').toLowerCase();
  const cards = [...document.querySelectorAll('.source-card')].map(el => ({el, text:norm(el.textContent), count:Number(el.dataset.count)}));
  const categoryNames = new Map([...$('category').options].map(o => [o.value, o.textContent]));
  function updateAddress() {
    const url = new URL(location.href);
    for (const [key, id] of [['category','category'],['q','library-search'],['type','source-type']]) {
      const value = $(id).value;
      if (value) url.searchParams.set(key, value); else url.searchParams.delete(key);
    }
    // A filter change should not leave an unrelated source fragment in the URL.
    url.hash = '';
    try { history.replaceState(null, '', url); } catch (_) { /* Some file readers restrict history. */ }
  }
  function filter(address = true) {
    const terms = norm($('library-search').value).trim().split(/\s+/).filter(Boolean);
    const category = $('category').value, type = $('source-type').value;
    let sources = 0, entries = 0;
    for (const c of cards) {
      const visible = (!category || c.el.dataset.categories.split(' ').includes(category)) &&
        (!type || (type === 'book' ? c.el.dataset.kind.includes('book') : c.el.dataset.kind === type)) &&
        terms.every(term => c.text.includes(term));
      c.el.hidden = !visible;
      c.el.classList.remove('has-target');
      if (visible) {
        sources++; entries += c.count;
        if (terms.length) c.el.querySelector('.source-entries').open = true;
      }
    }
    $('library-count').textContent = `${sources} sources · ${entries} entries in these sources`;
    $('library-empty').hidden = sources > 0;
    $('category-context').hidden = !category;
    $('category-context').textContent = category ? `${categoryNames.get(category)}. All entries from the selected sources are included, also on other topics.` : '';
    if (address) updateAddress();
  }
  function clear(address = true) {
    for (const id of ['library-search','category','source-type']) $(id).value = '';
    filter(address);
  }
  function revealHash() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
    const el = $(id);
    if (!el) return;
    if (el.matches('details.methodology')) { el.open = true; el.scrollIntoView(); return; }
    const source = el.closest('.source-card');
    if (!source) return;
    if (source.hidden) clear(false);
    source.querySelector('.source-entries').open = true;
    source.classList.add('has-target');
    el.scrollIntoView();
  }
  function readAddress() {
    const params = new URLSearchParams(location.search);
    $('category').value = categoryNames.has(params.get('category')) ? params.get('category') : '';
    $('library-search').value = params.get('q') || '';
    $('source-type').value = ['book','monograph','survey'].includes(params.get('type')) ? params.get('type') : '';
    filter(false); revealHash();
  }
  $('library-search').addEventListener('input', () => filter());
  for (const id of ['category','source-type']) $(id).addEventListener('change', () => filter());
  for (const id of ['library-reset','empty-reset']) $(id).addEventListener('click', () => clear());
  $('collapse-entries').addEventListener('click', () => document.querySelectorAll('.source-entries[open]').forEach(el => el.open = false));
  document.addEventListener('click', event => {
    const link = event.target.closest('a[data-category]');
    if (!link || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    clear(false); $('category').value = link.dataset.category; filter();
    $('source-list').scrollIntoView();
  });
  document.addEventListener('keydown', event => {
    if (event.key === '/' && !['INPUT','SELECT','TEXTAREA'].includes(document.activeElement.tagName)) {
      event.preventDefault(); $('library-search').focus();
    }
  });
  window.addEventListener('hashchange', revealHash);
  window.addEventListener('popstate', readAddress);
  readAddress();
})();
