"""Render an individually authored pruning proposal; never mutate atlas inputs."""
import csv
import hashlib
import html
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read_json(path):
    return json.loads(path.read_text())


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def write_json(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


baseline = {c['id']: c for c in read_json(HERE / 'baseline.json')['cards']}
ledger = read_json(HERE / 'read-ledger.json')
cards, hashes = {}, {}
for path in sorted((ROOT / 'data/cards').glob('*.json')):
    raw = path.read_bytes()
    card = json.loads(raw)
    cards[card['id']] = card
    hashes[card['id']] = digest(raw)
assert set(cards) == set(baseline), 'Card inventory changed during review; reconcile first.'
assert all(hashes[i] == baseline[i]['sha256'] for i in cards), 'A card changed; reread it first.'
active = {i: c for i, c in cards.items()
          if not c.get('scope_exclusion') and c['status'] not in {'resolved', 'excluded'}}
assert all(any(r['mode'] == 'range' and r['sha256'] == hashes[i]
               for r in ledger.get(i, [])) for i in active), 'Screen coverage is incomplete.'
with (HERE / 'candidates.tsv').open() as f:
    authored = list(csv.DictReader(f, delimiter='\t'))
selected = {d['id'] for d in authored}
assert len(authored) == len(selected) == 100
assert selected == set(read_json(HERE / 'selected-ids.json'))
assert selected <= set(active)
rescued = {c['id'] for c in read_json(ROOT / 'research/pruning-480-20260912/retained.json')}
assert not selected & rescued, 'Unexpected overlap with the previous rescue set.'
types = {
    'later_result': 'Later result answers the historical target',
    'duplicate': 'Duplicate target',
    'invalid_extraction': 'Invalid or non-independent extraction',
    'consolidation': 'Consolidation requiring scope alignment',
    'narrow_model': 'Specialized model or subcase',
    'specific_method': 'Specific method or construction',
    'quantitative_refinement': 'Secondary quantitative frontier',
}
category_labels = {
    c['key']: c.get('label', c['key'])
    for g in read_json(ROOT / 'data/categories.json')['groups'] for c in g['categories']
}
checks = {c['id']: c for c in read_json(HERE / 'source-checks.json')['checks']}
type_order = {t: n for n, t in enumerate(types)}
confidence_order = {'high': 0, 'medium': 1, 'borderline': 2}
authored.sort(key=lambda d: (type_order[d['type']], confidence_order[d['confidence']], d['id']))
decisions = []
for n, d in enumerate(authored, 1):
    identifier = d['id']
    c = active[identifier]
    assert any(r['mode'] != 'range' and r['sha256'] == hashes[identifier]
               for r in ledger.get(identifier, [])), f'Missing current assessment: {identifier}'
    retained = [i for i in d['retain_ids'].split(',') if i]
    assert set(retained) <= set(active) - selected, f'Invalid retained reference for {identifier}'
    summary = c.get('working_summary', {}).get('sentences', [])
    decisions.append({
        'review_order': n, 'id': identifier, 'title': c['title'],
        'area': c['area'], 'category': category_labels[c['area']],
        'type': d['type'], 'type_label': types[d['type']],
        'confidence': d['confidence'], 'reason': d['reason'],
        'condition': d['condition'], 'retain_ids': retained,
        'action': 'proposal_only', 'status_at_review': c['status'],
        'sha256': hashes[identifier], 'canonical_path': f'data/cards/{identifier}.json',
        'reader_url': f'https://vaclavrozhon.github.io/atlas/#{identifier}',
        'saved_target_summary': ' '.join(summary[:3]),
        'references': [{k: r[k] for k in ['title', 'url', 'pdf_url', 'locator'] if k in r}
                       for r in c.get('references', [])],
        'new_source_check': checks.get(identifier),
    })

now = datetime.now(timezone.utc).isoformat()
type_counts = dict(Counter(d['type'] for d in decisions))
confidence_counts = dict(Counter(d['confidence'] for d in decisions))
metadata = {
    'created_at_utc': now, 'canonical_cards': len(cards), 'active_screened': len(active),
    'inactive_excluded_from_screen': len(cards) - len(active),
    'cards_with_further_assessment': sum(any(r['mode'] != 'range' for r in ledger[i]) for i in active),
    'proposed_candidates': len(decisions), 'active_remaining_if_all_accepted': len(active) - len(decisions),
    'type_counts': type_counts, 'confidence_counts': confidence_counts,
    'scope': 'All active cards screened by title and saved target summary; candidates additionally assessed from their current target, full working summary, motivation and source locators. Full formulation and literature audits were not performed for every card.',
    'basis': 'Scientific significance and marginal benchmark contribution. Scores, rank, votes, category quotas and formalization cost were not selection rules.',
    'meaning_of_confidence': 'Strength of the editorial removal recommendation, not confidence that a problem is currently open or has been independently proved solved.',
    'authorization': 'Proposal only. No cards, statuses, scores, benchmark selections, reader assets or deployment changed.',
}
write_json('decisions.json', {'metadata': metadata, 'decisions': decisions})
with (HERE / 'proposal.tsv').open('w', newline='') as f:
    keys = ['review_order', 'id', 'title', 'category', 'type_label', 'confidence', 'reason', 'condition', 'retain_ids', 'reader_url']
    w = csv.DictWriter(f, fieldnames=keys, delimiter='\t', extrasaction='ignore')
    w.writeheader()
    for d in decisions:
        w.writerow({**d, 'retain_ids': ', '.join(d['retain_ids'])})
with (HERE / 'all-card-review.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['id', 'title', 'category', 'disposition', 'sha256'])
    for identifier, c in sorted(active.items()):
        w.writerow([identifier, c['title'], category_labels[c['area']],
                    'proposed_candidate' if identifier in selected else 'not_shortlisted', hashes[identifier]])

introduction = [
    '# 100 candidates for removal — 12 September 2026', '',
    f'**Screened all {len(active):,} active cards; selected exactly 100 candidates.** '
    f'The {len(cards)-len(active)} already inactive cards are outside the proposal. '
    'This is a review proposal; no catalogue data was changed.', '',
    '[Searchable table](proposal.html) · [Spreadsheet TSV](proposal.tsv) · [Detailed JSON](decisions.json) '
    '· [All-card screen](all-card-review.tsv) · [Source checks](source-checks.json)', '',
    'The list contains **4 historical targets answered by later work, 3 duplicate targets, '
    '6 conditional consolidations, 2 problematic extractions, and 85 editorial cuts**. '
    'The latter divide into 57 specialized models/subcases, 17 secondary quantitative frontiers '
    'and 11 specific methods/constructions.', '',
    '**13 high-confidence recommendations, 69 medium, 18 borderline.** Confidence describes '
    'the strength of the removal recommendation. The borderline cards have substantial scientific '
    'content and are the first recommendations I would reconsider if the proposed loss of coverage is too large. '
    'The order groups reasons and confidence; it is not a measured scientific ranking from 1 to 100.', '',
    'Selection follows the goal of a 500-problem benchmark. I compared scientific significance '
    'and the independent contribution of each target; score, ranking, focus membership, category sizes '
    'and formalization effort did not determine selection. A small canonical problem can be important, '
    'and being a draft or asking for a number/function is not a removal reason. '
    'None of the twenty cards retained in the preceding 480-removal review is proposed here.', '',
    'Every active card was screened using its current title and saved target summary. '
    f'{metadata["cards_with_further_assessment"]} cards then received a further target/motivation assessment, '
    'including all 100 selected cards and relevant alternatives. The exact displayed fields and current '
    'hashes are in [the read ledger](read-ledger.json). This is not a new full mathematical or open-status '
    'certification of all 1,066 problems. Targeted primary-source checks support the later-result cases; '
    'other priority judgments use the saved card and source material.', '',
    'The six conditional consolidations need scope alignment before deletion. In particular, '
    'the girth cards use different quantifiers, the APSP cards use different computational models, '
    'and the cryptography entry bundles different implications. Their shared subject is not a proof '
    'of equivalence. The proposed retained IDs remain active and are outside this list.', '',
    f'Accepting every recommendation would leave **{len(active)-100} active cards**. '
    'No category quota or benchmark selection has been changed.', '',
]
md = list(introduction)
for d in decisions:
    i = d['id']
    md += [f'{d["review_order"]}. **[{i}: {d["title"]}](../../data/cards/{i}.json)**', '',
           f'   {d["category"]} · {d["type_label"]} · **{d["confidence"]}**', '',
           f'   {d["reason"]}', '', f'   **Scope / condition:** {d["condition"]}', '']
    if d['retain_ids']:
        links = ', '.join(f'[{r}](../../data/cards/{r}.json)' for r in d['retain_ids'])
        md += [f'   **Keep / consult:** {links}.', '']
    if d['new_source_check']:
        check = d['new_source_check']
        md += [f'   **Evidence:** [{check["title"]}]({check["url"]}). {check["limit"]}', '']
(HERE / 'proposal.md').write_text('\n'.join(md))

esc = html.escape
rows = []
for d in decisions:
    retained = ' '.join(f'<a href="../../data/cards/{r}.json">{r}</a>' for r in d['retain_ids'])
    refs = [f'<a href="{esc(r["url"], quote=True)}">{esc(r.get("title", "Source"))}</a>'
            for r in d['references'] if r.get('url')]
    if d['new_source_check']:
        check = d['new_source_check']
        refs.insert(0, f'<a href="{esc(check["url"], quote=True)}">New check: {esc(check["title"])}</a>')
    search_text = ' '.join([d['id'], d['title'], d['category'], d['reason'], d['condition'], d['saved_target_summary']]).lower()
    rows.append(f'''<tr data-search="{esc(search_text, quote=True)}" data-type="{d['type']}" data-confidence="{d['confidence']}" data-area="{esc(d['category'], quote=True)}">
<td class="number">{d['review_order']}</td><td><a class="problem" href="../../data/cards/{d['id']}.json">{esc(d['title'])}</a><p class="meta">{d['id']} · {esc(d['category'])}</p><a class="reader" href="{d['reader_url']}">Open in atlas ↗</a></td>
<td><span class="badge {d['confidence']}">{d['confidence']}</span><p class="meta">{esc(d['type_label'])}</p></td>
<td><p>{esc(d['reason'])}</p><details><summary>Target, scope and evidence</summary><p><strong>Saved target context:</strong> {esc(d['saved_target_summary'])}</p><p><strong>Scope / condition:</strong> {esc(d['condition'])}</p>{'<p><strong>Keep / consult:</strong> '+retained+'</p>' if retained else ''}<p class="sources">{'<br>'.join(refs)}</p></details></td></tr>''')
options = lambda values: ''.join(f'<option value="{esc(k, quote=True)}">{esc(v)}</option>' for k, v in values)
page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>100 removal candidates · Atlas</title><link rel="stylesheet" href="../../web/vendor/katex.min.css">
<style>
:root{font:16px/1.55 system-ui,sans-serif;color:#172433;background:#f4f6f8}body{margin:0}main{max-width:1450px;margin:auto;padding:38px 24px}h1{font-size:clamp(1.8rem,3vw,2.7rem);line-height:1.15;margin:8px 0 18px}.eyebrow{font-size:.8rem;letter-spacing:.08em;color:#546172;text-transform:uppercase}a{color:#17569a;text-underline-offset:3px}.intro{max-width:960px}.intro p{margin:.8em 0}.counts{display:flex;gap:12px;flex-wrap:wrap;margin:22px 0}.counts span{padding:10px 16px;border:1px solid #d8e0e8;border-radius:8px;background:white}.filters{display:grid;grid-template-columns:2fr 2fr 2fr 1fr;gap:12px;margin:28px 0 8px}label{font-size:.82rem;font-weight:600}input,select{display:block;box-sizing:border-box;width:100%;font:inherit;background:white;border:1px solid #a7b4c3;border-radius:6px;padding:10px;margin-top:4px;color:inherit}#shown{font-size:.9rem;color:#546172;margin-bottom:14px}.table-wrap{overflow-x:auto;background:white;border:1px solid #d8e0e8;border-radius:8px}table{border-collapse:collapse;width:100%;min-width:880px}th{font-size:.8rem;letter-spacing:.025em;text-align:left;background:#eaf0f5;padding:14px;vertical-align:top}td{padding:18px 14px;border-top:1px solid #e3e8ee;vertical-align:top}td:nth-child(2){width:26%}td:nth-child(3){width:15%}.number{color:#738194;font-variant-numeric:tabular-nums}.problem{font-weight:650}.meta{color:#617084;font-size:.82rem;margin:.4em 0}.reader{font-size:.8rem}.badge{font-size:.75rem;padding:3px 8px;border-radius:4px;background:#e9eef5}.high{background:#e5f1eb;color:#22573e}.borderline{background:#fff0d6;color:#7a4a0d}td p{margin:0 0 .6em}details{font-size:.88rem}summary{cursor:pointer;color:#17569a}details[open] summary{margin-bottom:.7em}.sources{font-size:.82rem}tr[hidden]{display:none}footer{font-size:.84rem;color:#617084;margin-top:24px}input:focus,select:focus,summary:focus{outline:3px solid #6b9fcc;outline-offset:2px}@media(max-width:800px){main{padding:24px 14px}.filters{grid-template-columns:1fr 1fr}}@media print{.filters,#shown,.reader{display:none}body{background:white}main{padding:0}table{min-width:0}.table-wrap{overflow:visible}tr{break-inside:avoid}}
</style><main><div class="eyebrow">Atlas · Editorial review · 12 September 2026</div><h1>100 candidates for removal</h1>
<div class="intro"><p>Screened all <strong>1,066 active cards</strong>. The proposal compares scientific significance and independent contribution to the 500-problem benchmark. No cards have been removed.</p>
<p>Four historical questions have later answers, three repeat existing targets, six need consolidation with explicit scope checks, and two are problematic extractions. The other 85 are editorial priority judgments. <strong>18 are borderline</strong> and deserve particular scrutiny before removing their scientific coverage.</p>
<p>All cards received a title/target-summary screen; 150 received further assessment. This is not a fresh full formulation or literature audit of the entire catalogue. Confidence measures the recommendation, not proof verification.</p>
<p><a href="proposal.md">Full report</a> · <a href="proposal.tsv">Spreadsheet TSV</a> · <a href="decisions.json">Detailed JSON</a> · <a href="all-card-review.tsv">All-card screen</a> · <a href="source-checks.json">Source checks</a></p></div>
<div class="counts"><span><strong>13</strong> high confidence</span><span><strong>69</strong> medium</span><span><strong>18</strong> borderline</span><span><strong>966</strong> active if all accepted</span></div>
<div class="filters"><label>Search<input id="query" type="search" placeholder="Title, ID, reason or target"></label><label>Category<select id="area"><option value="">All categories</option>AREA_OPTIONS</select></label><label>Reason<select id="type"><option value="">All reasons</option>TYPE_OPTIONS</select></label><label>Confidence<select id="confidence"><option value="">All levels</option><option>high</option><option>medium</option><option>borderline</option></select></label></div>
<p id="shown" role="status" aria-live="polite">Showing 100 of 100 candidates</p><div class="table-wrap"><table><thead><tr><th scope="col">#</th><th scope="col">Problem</th><th scope="col">Recommendation</th><th scope="col">Individual reason</th></tr></thead><tbody>ROWS</tbody></table></div>
<footer>Proposal only. Stable IDs, card hashes and review scope are recorded in the accompanying JSON. The six consolidations are not claims of mathematical equivalence. Grouping does not impose category quotas or a numerical scientific ranking.</footer></main>
<script src="../../web/vendor/katex.min.js"></script><script src="../../web/vendor/contrib/auto-render.min.js"></script><script>
const controls=['query','area','type','confidence'].map(id=>document.getElementById(id));
const rows=[...document.querySelectorAll('tbody tr')];
function filter(){const [query,area,type,confidence]=controls.map(c=>c.value.toLowerCase());let shown=0;for(const row of rows){const ok=(!query||row.dataset.search.includes(query))&&(!area||row.dataset.area.toLowerCase()===area)&&(!type||row.dataset.type===type)&&(!confidence||row.dataset.confidence===confidence);row.hidden=!ok;if(ok)shown++;}document.getElementById('shown').textContent=`Showing ${shown} of ${rows.length} candidates`;}
controls.forEach(control=>control.addEventListener('input',filter));
if(window.renderMathInElement)renderMathInElement(document.querySelector('main'),{delimiters:[{left:'\\\\(',right:'\\\\)',display:false},{left:'\\\\[',right:'\\\\]',display:true},{left:'$',right:'$',display:false}],throwOnError:false,trust:false});
</script></html>'''
page = page.replace('AREA_OPTIONS', options((a, a) for a in sorted({d['category'] for d in decisions})))
page = page.replace('TYPE_OPTIONS', options(types.items())).replace('ROWS', '\n'.join(rows))
(HERE / 'proposal.html').write_text(page)
validation = {
    'checked_at_utc': now, 'active_cards_screened': len(active),
    'proposed_candidates': len(decisions), 'unique_active_candidate_ids': len(selected),
    'all_active_cards_have_current_screen_reads': True,
    'all_candidates_have_current_further_assessments': True,
    'all_candidate_hashes_match_current_cards': True,
    'all_canonical_card_bytes_unchanged_from_baseline': True,
    'all_retained_references_active_and_outside_proposal': True,
    'overlap_with_previous_twenty_rescues': sorted(selected & rescued),
    'type_counts': type_counts, 'confidence_counts': confidence_counts,
    'canonical_mutations_performed': 0,
}
write_json('validation.json', validation)
print(json.dumps(validation, ensure_ascii=False, indent=2))
