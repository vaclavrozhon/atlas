"""Topic boundaries, reversible exclusions and repeat-publication regressions."""
import copy
import json
import sys
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from taxonomy import *
from importance import apply_importance

data = json.loads((BASE / 'site/catalog.json').read_text())
original = copy.deepcopy(data)
apply_taxonomy(data)
apply_importance(data)
assert data == original, 'Taxonomy plus ranking must be idempotent'
assert len(NAMES) == 35 and len(BIG) == 10 and len(SMALL) == 25
assert sum(a['count'] for a in data['areas']) == data['meta']['taxonomy']['candidate_count']
assert sum(a['target'] for a in data['areas']) == 1000
assert data['meta']['taxonomy']['reserved_target'] == 0
by_id = {c['id']: c for c in data['cards']}
assert len(by_id) == len(data['cards'])
expected = {
    'TCS-0206': OUTSIDE, 'TCS-0342': STRUCTURAL, 'TCS-6500': STRUCTURAL,
    'TCS-0331': GEOMETRY, 'TCS-1212': GEOMETRY, 'TCS-2074': OPTIMIZATION,
    'TCS-1313': OPTIMIZATION, 'TCS-4986': OPTIMIZATION,
    'TCS-1913': ADS, 'TCS-1214': STRINGS, 'TCS-0079': STRINGS,
    'TCS-1765': LEARNING, 'TCS-3128': KNOWLEDGE, 'TCS-6371': KNOWLEDGE,
    'TCS-3873': KNOWLEDGE, 'TCS-5539': REASONING, 'TCS-4871': SAMPLING,
    'TCS-2942': RANDOMNESS, 'TCS-5591': PARALLEL, 'TCS-0498': DATABASE,
    'TCS-0767': PROOF, 'TCS-0771': PARAMETERIZED, 'TCS-0478': DYNAMIC,
}
for id, area in expected.items():
    # Quarantine preserves the reviewed subject routing separately.
    routed_area = by_id[id].get('scope_exclusion', {}).get('previous_area', by_id[id]['area'])
    assert routed_area == area, (id, routed_area, area)
for c in data['cards']:
    assert c['original_area'] in LEGACY_AREAS
    authored = editorial_card(c)
    assert authored['area'] == c['original_area']
    assert not ASSIGNMENT_FIELDS.intersection(authored)
    if c.get('scope_exclusion'):
        assert c['area'] == OUTSIDE and c['selection_target'] == 0
        assert c['scope_exclusion']['reason'] and c['selection_group'] == 'excluded'
    else:
        assert c['area'] in NAMES
        assert c['selection_target'] == (50 if c['area'] in BIG else 20)
# A fresh unknown subject stays in Misc, and generated boilerplate cannot route it.
unknown = dict(id='TCS-999999', area='General algorithm design',
               title='Unidentified question', formal='Can the bound be improved?',
               context='quantum sampling phylogenetic graph minors ontology',
               why='quantum algorithm applications', references=[])
assert classify(unknown)[0] == MISC
# Merely containing DNA/RNA letter sequences does not make a biological question.
unknown.update(area='Algorithms for biological structures', title='External-memory priority queues')
assert classify(unknown)[0] == ADS
print(json.dumps(dict(categories=35, candidates=data['meta']['taxonomy']['candidate_count'],
    exclusions=data['meta']['taxonomy']['scope_excluded_count'],
    checks=['idempotent routing and ranking', 'stable identity and original subjects',
            'quota and count totals', 'new subject boundaries',
            'auditable exclusions', 'unknown fallback and no boilerplate contamination'])))
