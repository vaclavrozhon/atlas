"""Check the editorial proposal independently of the reader and shared service."""
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from publish import load_catalog
from taxonomy import apply_taxonomy
from final_selection import apply_final_selection

data = load_catalog()
apply_taxonomy(data)
manifest = apply_final_selection(data)
areas = {a['area']: a for a in data['areas']}
assert collections.Counter(a['group'] for a in areas.values()) == {'large': 10, 'small': 25}
source = json.loads((ROOT / 'data/final_selection.json').read_text())
assert set(source['cards']) == {c['id'] for c in data['cards']}
counts = collections.Counter(c['area'] for c in data['cards'] if c['selection']['color'] == 'green')
# The user explicitly added green cards after the balanced 500-card proposal.
# Targets are not caps: additions must not silently turn another card red.
assert sum(counts.values()) == 504
for area, metadata in areas.items():
    target = 25 if metadata['group'] == 'large' else 10
    assert counts[area] == target + (area in {'Fine-grained complexity', 'Computational complexity', 'Graph algorithms', 'Distributed, parallel and sublinear algorithms'}), area
for c in data['cards']:
    selection = c['selection']
    assert selection['color'] in {'green', 'red'}
    assert selection['area'] == c['area']
    options = selection['area_options']
    assert len(set(options)) == len(options) and len(options) in {1, 2}
    assert all(a in areas for a in options)
    if len(options) == 2:
        assert {areas[a]['group'] for a in options} == {'large', 'small'}
    assert 'community_reviews' not in c
assert data['meta']['community_public'] is False
assert manifest['cards']['TCS-6511']['color'] == 'green'  # General Exact Matching.
assert manifest['cards']['TCS-0611']['color'] == 'red'  # Bipartite special case.
assert manifest['cards']['TCS-7376']['color'] == 'green'  # Existing streaming MST proposal.
assert manifest['cards']['TCS-7523'] == {
    'color': 'green', 'area': 'Fine-grained complexity',
    'area_options': ['Fine-grained complexity', 'Algorithms & data structures'],
}  # Explicit user addition: genuine subexponential Circuit-SAT.
assert manifest['cards']['TCS-7524'] == {
    'color': 'green', 'area': 'Computational complexity',
    'area_options': ['Computational complexity'],
}  # Explicit user addition: NEXP versus coNEXP.
assert manifest['cards']['TCS-6168']['color'] == 'red'
assert 'TCS-4786' in manifest['cards']['TCS-6168']['upvoted_red_reason']
assert any(c['status'] == 'resolved' and c['selection']['color'] == 'green' for c in data['cards'])
print(json.dumps({'green': sum(counts.values()), 'red': len(data['cards'])-sum(counts.values()),
    'categories': len(areas), 'paired_cards': sum(len(c['area_options'])==2 for c in manifest['cards'].values()),
    'manifest_version': manifest['version']}))
