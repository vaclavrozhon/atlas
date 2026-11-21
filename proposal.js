/* Reader suggestions are drafted locally and submitted on GitHub. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const dialog = $('contribution-dialog');
  const form = $('contribution-form');
  const fields = ['title', 'category', 'statement', 'sources'];
  const labels = {statement:'Problem statement', definitions:'Definitions and model', answer:'What would settle it?', why:'Why it matters', sources:'Sources'};
  const key = 'tcs-atlas-problem-proposal';
  function read(key) {
    try { return JSON.parse(localStorage.getItem(key)); } catch { return null; }
  }
  function values() {
    return Object.fromEntries(fields.map(name => [name, $('proposal-' + name).value]));
  }
  function save(draft) {
    try { localStorage.setItem(key, JSON.stringify(draft)); return true; } catch { return false; }
  }
  function issueURL(title, body) {
    const url = new URL('https://github.com/vaclavrozhon/atlas/issues/new');
    url.searchParams.set('title', '[Problem] ' + title.trim());
    if (body) url.searchParams.set('body', body);
    return url.href;
  }
  $('new-problem').onclick = () => {
    const draft = read(key) ?? read('tcs-atlas-contribution-drafts')?.problem ?? {};
    const extra = ['definitions','answer','why'].filter(name => draft[name]).map(name => labels[name] + ':\n' + draft[name]);
    const category = $('proposal-category');
    category.replaceChildren(new Option('Choose a category…',''));
    for (const area of window.TCS_ATLAS.areas) category.add(new Option(area.label, area.id));
    for (const name of fields) $('proposal-' + name).value = draft[name] || '';
    $('proposal-statement').value = [draft.statement, ...extra].filter(Boolean).join('\n\n');
    $('contribution-result').textContent = '';
    $('long-contribution').hidden = true;
    $('contribution-draft-status').textContent = draft.title ? 'Your saved draft has been restored.' : '';
    dialog.showModal();
    $('proposal-title').focus();
  };
  form.addEventListener('input', event => {
    event.target.setCustomValidity?.('');
    $('contribution-draft-status').textContent = save(values()) ? 'Draft saved in this browser.' : 'Copy your draft before closing this page.';
    $('long-contribution').hidden = true;
    $('contribution-result').textContent = '';
  });
  form.addEventListener('submit', event => {
    event.preventDefault();
    for (const name of ['title','statement']) {
      const field = $('proposal-' + name);
      field.setCustomValidity(field.value.trim() ? '' : 'Please enter some text.');
    }
    if (!form.reportValidity()) return;
    const draft = values();
    save(draft);
    const sections = ['statement','sources'].filter(name => draft[name].trim()).map(name => '### ' + labels[name] + '\n\n' + draft[name].trim());
    const body = '<!-- atlas-problem:v1 ' + draft.category + ' -->\n\n' + sections.join('\n\n');
    const url = issueURL(draft.title, body);
    if (url.length > 7500) {
      $('contribution-copy-text').value = body;
      $('open-long-contribution').href = issueURL(draft.title);
      $('long-contribution').hidden = false;
      $('long-contribution').scrollIntoView({block:'nearest'});
      return;
    }
    window.open(url, '_blank', 'noopener,noreferrer');
    $('contribution-result').textContent = 'Finish submitting your suggestion on GitHub.';
  });
  $('copy-contribution').onclick = async () => {
    const text = $('contribution-copy-text');
    try { await navigator.clipboard.writeText(text.value); $('contribution-result').textContent = 'Copied. Paste the text into the GitHub issue.'; }
    catch { text.focus(); text.select(); $('contribution-result').textContent = 'Copy the selected text and paste it into the GitHub issue.'; }
  };
  $('close-contribution').onclick = () => dialog.close();
  $('discard-contribution').onclick = () => {
    if (confirm('Discard this saved draft?') && save({})) dialog.close();
  };
})();
