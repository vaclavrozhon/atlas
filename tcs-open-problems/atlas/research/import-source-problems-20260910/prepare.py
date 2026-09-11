"""Freeze the reviewed import decisions into a standalone atlas input.

Run explicitly to update the batch. Publication never reads the separate library.
Only bibliographic metadata and question paraphrases enter the atlas input.
"""
import collections
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
sys.path.insert(0, str(BASE))
from taxonomy import DIRECT, NAMES
from decisions import REUSE, MERGE, CATEGORIES, REASONS

BATCH = 'textbook-surveys-20260910'
DATE = '2026-09-10'
rows = json.loads((HERE / 'screening.json').read_text())
source_input = (HERE / 'source-library-input.json').read_bytes()
sources = {s['id']: s for s in json.loads(source_input)['sources']}
background = {
    'odonnell2021': 'Communication complexity and Boolean function analysis',
    'bandit_algorithms': 'Optimization and numerics',
    'expanders': 'Structural graph theory',
    'watrous': 'Quantum computation',
    'wigderson': 'Computational complexity',
    'algorithmic_game_theory': 'Algorithmic game theory, mechanism design and fair division',
}

def root(n):
    seen = set()
    while n in MERGE:
        assert n not in seen, 'Cyclic merge decision'
        seen.add(n)
        n = MERGE[n]
    return n

def criterion(text):
    if re.search(r'construct|explicit|pseudorandom', text, re.I): return 'construction'
    if re.search(r'lower bound|space|communication|time lower', text, re.I): return 'resources'
    if re.search(r'tight|optimal|threshold|approximation|approximate', text, re.I): return 'tightness'
    if re.search(r'characteriz|classify|dichotomy', text, re.I): return 'characterization'
    if re.search(r'reduction|imply|equivalent', text, re.I): return 'reductions'
    if re.search(r'assumption|hypothesis', text, re.I): return 'assumptions'
    return 'decision'

def reference(row):
    source = sources[row['source_id']]
    return dict(id='primary', title=source['title'], authors=source['authors'],
                year=source['year'], url=source['source_url'],
                pdf_url=row['source_pdf_url'],
                locator=f"{row['locator']}; PDF page {row['pdf_page']}")

def key(row): return BATCH + ':' + row['entry_key']

drafts = []
entries = []
for row in rows:
    n = row['n']
    source = sources[row['source_id']]
    origin = rows[root(n)-1]
    assert origin['n'] == root(n)
    target = dict(existing_ids=REUSE[root(n)]) if root(n) in REUSE else dict(draft_key=key(origin))
    note = dict(key=key(row), batch=BATCH, kind=row['kind'], summary=row['summary'],
                reference=reference(row), edition_note=source['edition_note'],
                caution=source['caution'],
                status_note=f"Presented in the cited {source['year']} source version. The import does not verify present open status; this dated note does not override a later card review.")
    entries.append(dict(entry_key=row['entry_key'], target=target, note=note,
                        disposition='existing_card' if root(n) in REUSE else 'same_new_question' if n in MERGE else 'new_draft',
                        reason=REASONS.get(n, 'No confirmed identical target in the inspected catalogue candidates; retained as an unfinished source draft.')))
    if n in REUSE or n in MERGE:
        continue
    area = CATEGORIES.get(n) or row['home'] or background.get(row['source_id']) or DIRECT.get(row['source_area'])
    assert area in NAMES, (n, area)
    drafts.append(dict(
        key=key(row), title=row['summary'], area=area, formal=row['summary'],
        context=f"Paraphrase of a {row['kind'].replace('_', ' ')} in {source['title']} ({source['year']}), {row['locator']}. The exact definitions, parameters and assumptions must be read at the cited location. This short draft has not been developed into a self-contained research card.",
        why='Source selection: ' + source['selection_reason'],
        evidence='source', status='source_open',
        status_note=f"Recorded as a question, conjecture or research direction in the cited {source['year']} source version. Present open status has not been checked; the import date is not an open-status review.",
        review_note='Imported as a dated paraphrase. Some entries group related variants or describe research directions rather than a single formal problem. The source caveats are preserved below. Importance and the full problem formulation remain unassessed.',
        progress=[], references=[reference(row)], related=[],
        criterion=criterion(row['summary']), model_self_contained=False,
        requires_context=True, classification_method='source_import_topic',
        year=source['year'],
        textbook_import=dict(batch=BATCH, category=area, kind=row['kind']),
    ))

batch = dict(id=BATCH, approved_on=DATE,
             approval_basis='User: "knihovnu nech samostatne, ale problemy z ni pridej do atlasu"; "atlas UI nemá mít pristup ke knihovne".',
             input_sha256=hashlib.sha256(source_input).hexdigest(),
             description='Dated source questions only. The independent source collection is not a publication dependency and is not served by the atlas.',
             cards=drafts, entries=entries)
assert len(entries) == 555
assert len({e['entry_key'] for e in entries}) == 555
assert not any(x in json.dumps(batch) for x in ['local_pdf_url', 'tcs-source-library', 'source-library-input.json'])
destination = BASE / 'imports' / (BATCH + '.json')
destination.parent.mkdir(exist_ok=True)
destination.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(entries=len(entries), new_cards=len(drafts), dispositions=dict(collections.Counter(e['disposition'] for e in entries)), existing_ids=len({i for e in entries for i in e['target'].get('existing_ids', [])}))))
