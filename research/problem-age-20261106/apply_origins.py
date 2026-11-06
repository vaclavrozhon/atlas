"""Apply reviewed age annotations; preserve all other canonical card fields."""
import collections
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from problem_origin import validate_origin

origins = json.loads((HERE / 'origins.json').read_text())
targets = json.loads((HERE / 'targets.json').read_text())
if (HERE / 'current-targets.json').exists():
    targets += json.loads((HERE / 'current-targets.json').read_text())
assert {c['id'] for c in targets} <= origins.keys(), 'Missing historical assessments'
preserved = {}
for ident, origin in origins.items():
    validate_origin(origin)
    path = ROOT / 'data/cards' / (ident + '.json')
    card = json.loads(path.read_text())
    original = {k: v for k, v in card.items() if k != 'problem_origin'}
    preserved[ident] = hashlib.sha256(json.dumps(original, sort_keys=True).encode()).hexdigest()
    card['problem_origin'] = origin
    path.write_text(json.dumps(card, ensure_ascii=False, indent=2) + '\n')
    written = json.loads(path.read_text())
    assert {k: v for k, v in written.items() if k != 'problem_origin'} == original
result = {'annotated': len(origins), 'requested_union': len({c['id'] for c in targets}), 'precision_counts': dict(collections.Counter(o['precision'] for o in origins.values())), 'preserved_card_content_sha256': preserved}
(HERE / 'application.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'preserved_card_content_sha256'}))
