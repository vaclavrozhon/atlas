/* Problem history is independent of the date and status of the latest source. */
(function (root) {
  'use strict';
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const safeURL = value => { try { const url = new URL(value); return ['https:', 'http:'].includes(url.protocol) ? url.href : '#'; } catch { return '#'; } };
  const years = n => n === 0 ? 'under 1 year' : `~${n} ${n === 1 ? 'year' : 'years'}`;
  function label(origin, asOf = new Date().getUTCFullYear()) {
    if (!origin) return '';
    if (origin.precision === 'unknown') return 'Origin date uncertain';
    const age = Math.max(0, asOf - origin.year);
    if (origin.precision === 'by') return `Documented by ${origin.year} · ${age ? 'at least ' + years(age) : 'documented this year or earlier'}`;
    if (origin.precision === 'range') {
      const recent = Math.max(0, asOf - origin.end_year);
      return `Origin: c. ${origin.year}–${origin.end_year} · ~${recent}–${age} years`;
    }
    return `Origin: ${origin.precision === 'circa' ? 'c. ' : ''}${origin.year} · ${years(age)}`;
  }
  function html(card, asOf = new Date().getUTCFullYear()) {
    const origin = card.problem_origin;
    if (!origin) return '';
    const refs = (origin.references || []).map(ref => `<li><a href="${esc(safeURL(ref.url))}" target="_blank" rel="noopener noreferrer">${esc(ref.title)}</a>${ref.locator ? ' · ' + esc(ref.locator) : ''}</li>`).join('');
    return `<details class="problem-age"><summary>${esc(label(origin, asOf))}</summary><div class="problem-age-body"><p>${esc(origin.note)}</p>${refs ? `<ul>${refs}</ul>` : ''}<p class="muted">Age estimated in calendar years, as of ${asOf}. Historical assessment: ${esc(origin.reviewed_on)}.</p></div></details>`;
  }
  const api = {label, html};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.ATLAS_PROBLEM_AGE = api;
})(typeof window !== 'undefined' ? window : globalThis);
