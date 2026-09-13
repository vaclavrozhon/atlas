"""Render an editorial proposal; never edit or remove canonical records."""
import csv
import hashlib
import html
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MERGES = {
    '5845': '0771', '5926': '0771', '5314': '0163', '3484': '0163',
    '7135': '0306', '5453': '2680', '5034': '7215', '5246': '7222',
    '5312': '4786', '5501': '4786', '2356': '0331', '4972': '7294',
    '4577': '5773', '5737': '0913', '3324': '7230', '6319': '5158',
    '5770': '2783', '0308': '6712',
}
MERGES = {'TCS-' + k: 'TCS-' + v for k, v in MERGES.items()}
SCOPE_CHECK = {'TCS-0308', 'TCS-6319'}
LABELS = {
    'model_variant': 'Additional model or representation',
    'quantitative_refinement': 'Quantitative refinement',
    'method_specific': 'Specific method or reduction',
    'construction_variant': 'Specific construction or family',
    'consolidation': 'Consolidate with retained card',
    'specialized_target': 'Specialized target',
    'bundled_direction': 'Unselected bundle of directions',
    'cluster_overlap': 'Lower marginal value within a cluster',
}
BASELINE = json.loads((HERE / 'baseline.json').read_text())['cards']
LEDGER = json.loads((HERE / 'read-ledger.json').read_text())
raw_cards = {p.stem: p.read_bytes() for p in (ROOT / 'data/cards').glob('*.json')}
cards = {i: json.loads(raw) for i, raw in raw_cards.items()}
hashes = {i: hashlib.sha256(raw).hexdigest() for i, raw in raw_cards.items()}
with (HERE / 'candidates.tsv').open() as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
# The matching-on-the-line sources need an explicit randomness-convention check.
for r in rows:
    if r['id'] in SCOPE_CHECK:
        r['confidence'] = 'medium'
rows.sort(key=lambda r: (r['confidence'] != 'high', r['id']))
selected = {r['id'] for r in rows}
assert len(rows) == len(selected) == 300
assert selected <= cards.keys()
assert not selected.intersection(MERGES.values())
assert {r['id'] for r in rows if r['type'] == 'consolidation'} == MERGES.keys()
assert all(cards[i]['status'] != 'resolved' for i in selected)
assert 'TCS-0464' not in selected
for r in rows:
    i = r['id']
    assert any('working_summary' in read['fields'] and read['sha256'] == hashes[i]
               for read in LEDGER[i]['reads']), f'Stale or missing detailed read: {i}'
    assert r['reason'] and r['type'] in LABELS
    for mentioned in re.findall(r'TCS-\d{4}', r['reason']):
        assert mentioned in cards, f'Missing comparator: {mentioned}'
        assert mentioned not in selected, f'Selected comparator: {mentioned}'

changed = [c['id'] for c in BASELINE if hashes.get(c['id']) != c['sha256']]
added = sorted(cards.keys() - {c['id'] for c in BASELINE})
reviewed_additions = [i for i in added if i in LEDGER and any(
    'working_summary' in r['fields'] and r['sha256'] == hashes[i]
    for r in LEDGER[i]['reads'])]
counts = Counter(r['confidence'] for r in rows)
types = Counter(r['type'] for r in rows)
statuses = Counter(c['status'] for c in cards.values())
records = []
for n, r in enumerate(rows, 1):
    i = r['id']; c = cards[i]
    records.append({
        'review_order': n, **r, 'title': c['title'], 'area': c['area'],
        'status_at_review': c['status'], 'sha256': hashes[i],
        'action': 'consolidate_then_remove' if i in MERGES else 'propose_removal',
        'retain_id': MERGES.get(i), 'scope_alignment_required': i in SCOPE_CHECK,
        'canonical_path': 'data/cards/' + i + '.json',
        'reader_url': 'https://vaclavrozhon.github.io/atlas/#' + i,
        'references': [{k: ref[k] for k in ('title', 'url', 'locator') if k in ref}
                       for ref in c.get('references', [])],
    })
metadata = {
    'created_at': datetime.now(timezone.utc).isoformat(),
    'purpose': 'Proposal for approximately 300 additional removals; no deletion authorized or performed in this report.',
    'scope': {
        'baseline_cards': len(BASELINE), 'current_cards': len(cards),
        'brief_screened_ids': len(LEDGER),
        'ids_with_detailed_reads': sum(any('working_summary' in r['fields'] for r in v['reads']) for v in LEDGER.values()),
        'proposed_cards': len(rows), 'status_counts': dict(statuses),
        'confidence_counts': dict(counts), 'reason_counts': dict(types),
        'proposed_consolidations': len(MERGES),
        'consolidations_requiring_scope_alignment': sorted(SCOPE_CHECK),
        'current_cards_if_all_accepted': len(cards) - len(rows),
        'nonresolved_cards_if_all_accepted': len(cards) - statuses['resolved'] - len(rows),
        'changed_since_initial_snapshot': changed, 'added_since_initial_snapshot': added,
        'additions_with_current_detailed_read': reviewed_additions,
    },
    'evidence_limit': 'Editorial review of current card statements, complete saved working summaries, substantive significance fields and reference titles/locators. This pass did not independently reread all cited papers or certify present open status.',
    'confidence_definition': {'high': 'Stronger editorial case for removal or consolidation.', 'medium': 'Defensible but judgment-sensitive; a serious case for keeping may exist.'},
    'ordering': 'High confidence first, then stable ID; not a scientific importance ranking.',
}
(HERE / 'decisions.json').write_text(json.dumps({'metadata': metadata, 'decisions': records}, ensure_ascii=False, indent=2) + '\n')
with (HERE / 'proposal.tsv').open('w') as f:
    keys = ['review_order', 'id', 'title', 'area', 'confidence', 'type', 'action', 'retain_id', 'scope_alignment_required', 'reason', 'sha256']
    w = csv.DictWriter(f, fieldnames=keys, delimiter='\t', extrasaction='ignore', lineterminator='\n')
    w.writeheader(); w.writerows(records)


def card_link(i):
    return f'[{i}](../../data/cards/{i}.json)'


def md_safe(s):
    return s.replace('|', '\\|').replace('\n', ' ')


intro = f'''# Proposal: 300 additional card removals

Prepared 12 September 2026. **Proposal only. No canonical card or selection registry was edited, and nothing was deleted or published.**

Open the [searchable review table](proposal.html), the [spreadsheet-ready list](proposal.tsv), or the [structured decisions](decisions.json). All 300 individual reasons also appear below.

The proposal contains **{counts['high']} stronger recommendations** and **{counts['medium']} judgment-sensitive recommendations**. It is an editorial selection for a smaller, more consequential TCS research benchmark, not a finding that all these questions lack scientific value. There are **18 proposed consolidations** and **282 other removals**. Two consolidations need an explicit scope check before removal: formula/circuit conventions in TCS-0308 and randomness conventions in TCS-6319.

The initial snapshot contained **{len(BASELINE):,} records**. At rendering, the catalogue contains **{len(cards):,} records**: {len(cards)-statuses['resolved']:,} not marked resolved and {statuses['resolved']} marked resolved. None of the latter are used to fill this batch. Accepting all 300 proposals would leave **{len(cards)-300:,} stored records**, including **{len(cards)-statuses['resolved']-300:,} not marked resolved**. These are catalogue status counts, not independent certifications of openness.

## Criteria and scope

The selection follows [Atlas rules](../../docs/RULES.md), [the project purpose](../../README.md), and the earlier [importance calibration](../importance-pruning-20260911/CALIBRATION.md), [fundamentality review](../fundamentality-second-300-20260911/README.md), and [specification cleanup](../specification-cleanup-20260912/README.md).

I screened all {len(BASELINE):,} cards by title and statement, expanding saved excerpts and opening summary sentences where needed. I read complete saved working summaries, substantive significance fields and source titles/locators for {metadata['scope']['ids_with_detailed_reads']} cards, including every proposed removal and the comparison cards used for consolidation. These were individual editorial decisions, not an automatic score, category-quota or keyword filter. The read ledger records the content hash and displayed fields; it does not claim that every external paper was read.

Of the {len(added)} records added after the initial snapshot, {len(reviewed_additions)} also received a detailed read matching their rendering-time content. Those additional reads are recorded separately from the initial screening.

The main considerations were narrower model variants, additional parameter regimes, particular constructions, and intermediate methods whose independent contribution to this smaller benchmark is less compelling. Logical dependence alone, difficult formalization, incomplete prose, age, source prestige, a high score and a previous formulation repair were not decision rules. No category-balancing target was used. The ordering is confidence followed by stable ID, not a scientific ranking of the 300 problems.

This pass is **not a fresh literature audit of open status**. Old bounds, claimed source resolutions and model ambiguities remain subject to the catalogue's separate status/formulation review. Reasons referring to a theorem or algorithm describe the saved source context. The current-card hashes in the decisions make later changes detectable. At rendering, {len(changed)} baseline records had changed during this review; every selected card has a detailed read matching its current hash.

## Calibration and reconsidered cases

- {card_link('TCS-0464')} stays: the two-bit OR information problem is a small canonical question, and the earlier user discussion did not establish an exclusion reason.
- {card_link('TCS-7196')} stays: polynomial-time exact EFX for three agents is a meaningful canonical computational frontier, despite its fixed population.
- {card_link('TCS-3689')} stays: the clarified non-clashing teaching conjecture is a general sharp relation for all finite concept classes. Its breadth outweighs the argument that it is just another teaching convention.
- {card_link('TCS-4110')} stays in this batch: the general real-stability recognition barrier deserves more careful significance review before treating it as merely an algorithmic follow-up.
- {card_link('TCS-3685')} is held for separate formulation/status review. The concurrent review identified a literal-statement inconsistency; it is not used to meet this 300-card importance cut.
- {card_link('TCS-0306')} and {card_link('TCS-7260')} both stay: polynomial-time negation and nonconstructive polynomial-size negation are different targets.
- {card_link('TCS-2783')} and {card_link('TCS-6500')} both stay: their saved girth and graph-size quantifiers differ. Only the redundant source occurrence TCS-5770 is proposed for consolidation.
- {card_link('TCS-7008')} and {card_link('TCS-7298')} both stay: relative-error approximation and a constant-factor guarantee with variable rank should not be called duplicates.

## Consolidations

These removals are conditional on preserving useful references and the stated target in the retained record. The proposal performs no transfer. Consolidation must not silently broaden a target or count a narrower result as solving a broader one. The four `cluster_overlap` entries elsewhere are lower-priority related questions, **not claims of mathematical equivalence**.

| Remove after consolidation | Retain | Review requirement |
| --- | --- | --- |
'''
lines = [intro]
for r in records:
    if r['retain_id']:
        lines.append(f"| {card_link(r['id'])} | {card_link(r['retain_id'])} | {md_safe(r['reason'])} |\n")
lines.append('\n## Reasons across the proposal\n\nCounts describe the result; they were not quotas.\n\n| Reason | Cards |\n| --- | ---: |\n')
for key, count in types.most_common():
    lines.append(f'| {LABELS[key]} | {count} |\n')
lines.append('\n## Individual recommendations\n\n')
for r in records:
    lines.append(f"### {r['review_order']}. {r['id']} — {r['title']}\n\n")
    lines.append(f"{card_link(r['id'])} · {r['area']} · **{r['confidence']} confidence** · {LABELS[r['type']]}\n\n{r['reason']}\n\n")
    if r['retain_id']:
        lines.append(f"Retain: {card_link(r['retain_id'])}. Transfer and check scope before removal.\n\n")
    refs = r['references']
    if refs:
        lines.append('Saved sources: ' + '; '.join(md_safe(x.get('title', 'Untitled reference')) for x in refs) + '.\n\n')
(HERE / 'proposal.md').write_text(''.join(lines))

payload = json.dumps({'metadata': metadata, 'labels': LABELS, 'decisions': records}, ensure_ascii=False).replace('<', '\\u003c')
page = '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Atlas · 300 removal proposals</title>
<style>
:root{color-scheme:light;--ink:#203330;--muted:#5c6f6a;--line:#dae3dd;--accent:#146452}*{box-sizing:border-box}body{margin:0;background:#f5f7f2;color:var(--ink);font:16px/1.5 system-ui,sans-serif}header,main{max-width:1450px;margin:auto;padding:28px 30px}header{padding-bottom:8px}h1{font-size:clamp(28px,4vw,45px);letter-spacing:-.04em;margin:8px 0}p{max-width:1000px}a{color:var(--accent);text-underline-offset:3px}label{display:flex;flex-direction:column;gap:5px;font-size:13px;color:var(--muted)}input,select{font:inherit;font-size:15px;padding:11px;border:1px solid #b4c6bb;border-radius:5px;background:white;max-width:100%}.filters{display:grid;grid-template-columns:2fr 1fr 1.6fr 1.4fr;gap:12px;padding:18px;background:#e7eee4;border:1px solid var(--line);border-radius:8px}.stats{display:flex;gap:18px;flex-wrap:wrap;margin:22px 0}.stat{padding:12px 20px;border-left:3px solid #4c846c;background:#fff}.stat b{display:block;font-size:26px}.muted{color:var(--muted)}#count{margin:15px 0;font-weight:600}.table-scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;background:white}th{text-align:left;background:#e7eee4;font-size:13px;padding:12px}td{padding:16px 12px;border-bottom:1px solid var(--line);vertical-align:top}td:nth-child(1){width:32%}td:nth-child(2){width:15%}td:nth-child(3){width:53%}.id{font:13px ui-monospace,monospace}.title{display:block;font-weight:650;margin:5px 0}.area{font-size:12px;color:var(--muted)}.badge{display:inline-block;font-size:12px;font-weight:650;padding:3px 8px;border-radius:4px;background:#fff0d6;color:#695123;margin-bottom:7px}.high{background:#def0e3;color:#185d3a}.kind{font-size:13px;color:var(--muted)}details{font-size:13px;margin-top:10px}details ul{padding-left:19px}details li{margin-bottom:8px}.retain{margin-top:10px;font-size:14px;font-weight:600}footer{padding:30px;color:var(--muted);font-size:13px}.empty{padding:25px;background:white}noscript p{padding:20px;background:#fff0d6}@media(max-width:850px){.filters{grid-template-columns:1fr 1fr}header,main{padding:18px}td:nth-child(1){min-width:220px}td:nth-child(2){min-width:130px}td:nth-child(3){min-width:310px}}@media print{.filters,.stats,footer,details{display:none}body{background:white;font-size:10pt}header,main{padding:0}table{font-size:9pt}.table-scroll{overflow:visible}tr{break-inside:avoid}a{color:inherit}h1{font-size:24pt}}
</style>
<header><div class="id">ATLAS / EDITORIAL REVIEW / 12 SEPTEMBER 2026</div><h1>300 cards proposed for removal</h1><p>An initial review of __BASELINE_COUNT__ catalogue records, plus __ADDITIONAL_READ_COUNT__ later additions. Each row gives an individual editorial reason. <strong>Nothing has been deleted.</strong></p><p class="muted">High confidence means a stronger editorial case; medium confidence means the recommendation is judgment-sensitive. The list is not a claim that these questions have no scientific value. No category quotas or score cutoff were used.</p><div class="stats" id="stats"></div><p><a href="proposal.md">Complete report and criteria</a> · <a href="proposal.tsv" download>Download TSV</a> · <a href="decisions.json" download>Download decisions</a></p></header>
<main><div class="filters"><label>Search title, ID or reason<input id="search" type="search" placeholder="e.g. spanner, TCS-5312, coefficient"></label><label>Confidence<select id="confidence"><option value="">All recommendations</option><option value="high">High confidence first</option><option value="medium">Medium confidence</option></select></label><label>Area<select id="area"><option value="">All areas</option></select></label><label>Reason<select id="kind"><option value="">All reasons</option></select></label></div><p id="count" aria-live="polite"></p><noscript><p>JavaScript is disabled. Read the complete <a href="proposal.md">Markdown report</a> or <a href="proposal.tsv">TSV list</a>.</p></noscript><div class="table-scroll"><table><thead><tr><th>Card and area</th><th>Assessment</th><th>Reason to remove or consolidate</th></tr></thead><tbody id="rows"></tbody></table></div><p id="empty" class="empty" hidden>No recommendations match these filters.</p><p class="muted">Card links open local canonical JSON. The optional published-reader links may show an older deployment. Consolidations require preserving sources and checking the target before deletion; TCS-0308 and TCS-6319 have an explicit scope-alignment condition.</p></main><footer>Based on saved card statements, complete working summaries and reference metadata. This review does not independently certify current open status. Exact reviewed content hashes are in decisions.json.</footer>
<script id="data" type="application/json">__PAYLOAD__</script>
<script>
'use strict';
const data=JSON.parse(document.getElementById('data').textContent), rows=data.decisions;
const el=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const safeURL=u=>/^https?:\\/\\//i.test(u||'')?u:'';
const link=i=>'../../data/cards/'+encodeURIComponent(i)+'.json';
const s=data.metadata.scope;
el('stats').innerHTML=[[s.proposed_cards,'proposed removals'],[s.confidence_counts.high,'stronger cases'],[s.confidence_counts.medium,'judgment-sensitive'],[s.proposed_consolidations,'consolidations']].map(([n,t])=>'<div class="stat"><b>'+n+'</b>'+t+'</div>').join('');
for(const a of [...new Set(rows.map(r=>r.area))].sort()){const o=document.createElement('option');o.value=a;o.textContent=a;el('area').append(o)}
for(const [k,v] of Object.entries(data.labels)){const o=document.createElement('option');o.value=k;o.textContent=v;el('kind').append(o)}
function render(){const q=el('search').value.toLocaleLowerCase().trim(),c=el('confidence').value,a=el('area').value,k=el('kind').value;const visible=rows.filter(r=>(!c||r.confidence===c)&&(!a||r.area===a)&&(!k||r.type===k)&&(!q||[r.id,r.title,r.reason,r.area,r.retain_id].join(' ').toLocaleLowerCase().includes(q)));el('count').textContent=visible.length+' of '+rows.length+' recommendations · confidence, then stable ID';el('empty').hidden=visible.length!==0;
el('rows').innerHTML=visible.map(r=>'<tr data-id="'+esc(r.id)+'"><td><a class="id" href="'+link(r.id)+'">'+esc(r.id)+'</a><span class="title">'+esc(r.title)+'</span><span class="area">'+esc(r.area)+'</span><details><summary>Saved source references ('+r.references.length+')</summary><ul>'+r.references.map(x=>'<li>'+(safeURL(x.url)?'<a href="'+esc(x.url)+'" target="_blank" rel="noopener noreferrer">'+esc(x.title)+'</a>':esc(x.title))+(x.locator?'<br><span class="muted">'+esc(x.locator)+'</span>':'')+'</li>').join('')+'</ul><a href="'+esc(r.reader_url)+'" target="_blank" rel="noopener noreferrer">Open published reader</a></details></td><td><span class="badge '+(r.confidence==='high'?'high':'')+'">'+esc(r.confidence)+' confidence</span><div class="kind">'+esc(data.labels[r.type])+'</div></td><td>'+esc(r.reason)+(r.retain_id?'<div class="retain">Retain <a href="'+link(r.retain_id)+'">'+esc(r.retain_id)+'</a>'+(r.scope_alignment_required?' · scope check required':' · preserve sources')+'</div>':'')+'</td></tr>').join('');}
for(const id of ['search','confidence','area','kind'])el(id).addEventListener(id==='search'?'input':'change',render);
render();
</script></html>
'''
(HERE / 'proposal.html').write_text(page.replace('__PAYLOAD__', payload).replace('__BASELINE_COUNT__', f'{len(BASELINE):,}').replace('__ADDITIONAL_READ_COUNT__', str(len(reviewed_additions))))
(HERE / 'README.md').write_text('''# Editorial proposal for 300 removals

Start with the [searchable review table](proposal.html) or [complete report](proposal.md).
The [TSV](proposal.tsv) is suitable for a spreadsheet; [JSON](decisions.json) includes
retained IDs, current-card hashes and the review scope. No canonical data is changed.

`candidates.tsv` contains the individually authored editorial decisions.
`review.py` is a read-only card viewer that records fields and hashes in
`read-ledger.json`. `baseline.json` contains initial IDs, status and hashes only.
`pending-detail.json` is the larger screening shortlist, not an additional deletion list.
`build_report.py` renders the proposal and checks count, uniqueness, active status,
current detailed reads and retained-card references. It does not select candidates.

Regenerate with `python3 research/pruning-proposal-300-20260912/build_report.py`.
If a selected card has changed since its detailed read, regeneration stops until
that record is reviewed again. Approval and any later deletion are separate work.
''')
validation = {
    'result': 'passed', 'proposals': len(rows), 'unique_ids': len(selected),
    'all_selected_exist': True, 'no_selected_resolved': True,
    'all_selected_have_current_detailed_read': True,
    'all_consolidation_targets_retained': True,
    'all_reason_comparators_exist_and_are_retained': True,
    'canonical_writes_by_this_script': 0,
    'confidence_counts': dict(counts), 'reason_counts': dict(types),
}
(HERE / 'validation.json').write_text(json.dumps(validation, indent=2) + '\n')
print(json.dumps(validation))
