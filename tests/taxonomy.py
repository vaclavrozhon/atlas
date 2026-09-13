"""Explicit category assignments, stable keys and count regressions."""
import copy
import json
import sys
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / 'scripts'))
from categories import BIG, SMALL, NAMES, CATEGORIES
from taxonomy import apply_taxonomy
from importance import apply_importance
from deleted_records import read_deleted

data = json.loads((BASE / 'build/catalog.json').read_text())
original = copy.deepcopy(data)
apply_taxonomy(data)
apply_importance(data)
assert data == original
assert len(BIG) == 10 and len(SMALL) == 25 and len(NAMES) == 35
assert len({a['id'] for a in CATEGORIES}) == len({a['label'] for a in CATEGORIES}) == len(NAMES)
assert sum(a['count'] for a in data['areas']) == len(data['cards'])
assert sum(a['target'] for a in data['areas']) == 1000
assert data['meta']['taxonomy']['reserved_target'] == 0
assert data['meta']['taxonomy']['deleted_count'] == len(read_deleted())
assert not {c['id'] for c in data['cards']} & read_deleted().keys()
assert not {p.stem for p in (BASE / 'data/cards').glob('*.json')} & read_deleted().keys()
for card in data['cards']:
    assert card['area'] in NAMES and not card.get('scope_exclusion')
    assert card['selection_group'] == ('large' if card['area'] in BIG else 'small')
    assert card['selection_target'] == (50 if card['area'] in BIG else 20)
fixture = copy.deepcopy(data)
card = fixture['cards'][0]
card['formal'] = 'Quantum, geometry, scheduling, graph algorithms.'
category = card['area']
apply_taxonomy(fixture)
assert card['area'] == category
card['area'] = 'Unknown category fixture'
try:
    apply_taxonomy(fixture)
except ValueError as error:
    assert 'unknown category' in str(error)
else:
    raise AssertionError('Unknown category was silently assigned')
print(json.dumps({'categories': len(NAMES), 'records': len(data['cards']),
    'checks': ['explicit editorial categories', 'stable keys and quotas',
               'no deleted records', 'idempotent counts and rankings', 'unknown categories rejected']}))
