"""Catalogue regressions for importance ordering, preservation, and exports."""
import copy
import csv
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from importance import apply_importance

data = json.loads((BASE / 'site/catalog.json').read_text())
original = copy.deepcopy(data)
apply_importance(data)
assert data == original, 'Reapplying the ranking must be idempotent'
assert len(data['areas']) == 35
assert sum(a['target'] for a in data['areas']) == 1000
assert all(a['importance_assessed'] >= 0 for a in data['areas'])
assert all(c['importance']['method'] == 'unassessed' for a in data['areas']
           if not a['importance_assessed'] for c in data['cards'] if c['area'] == a['area'])
ids = [c['id'] for c in data['cards']]
assert len(ids) == len(set(ids))
for area in data['areas']:
    cards = [c for c in data['cards'] if c['area'] == area['area']]
    assert len(cards) == area['count']
    assert [c['importance_rank'] for c in cards] == list(range(1, len(cards) + 1))
    assert all(c['importance_count'] == len(cards) for c in cards)
    assert area['importance_assessed'] + area['importance_provisional'] == len(cards)
    resolved = False
    previous = {}
    for card in cards:
        if card['status'] == 'resolved':
            resolved = True
        else:
            assert not resolved, 'A remaining candidate follows a resolved record'
        status_group = card['status'] == 'resolved'
        score = card['importance']['score']
        assert score <= previous.get(status_group, 100)
        previous[status_group] = score

heads = {a['area']: next(c['id'] for c in data['cards'] if c['area'] == a['area']) for a in data['areas']}
# Approved additions can outrank the historical category leaders. Among cards
# tied for the best active score, the lowest stable ID must come first.
for area in data['areas']:
    candidates = [c for c in data['cards'] if c['area'] == area['area']]
    active = [c for c in candidates if c['status'] != 'resolved'] or candidates
    best_score = max(c['importance']['score'] for c in active)
    assert heads[area['area']] == min(c['id'] for c in active if c['importance']['score'] == best_score)

csv_rows = list(csv.DictReader((BASE / 'site/importance-ranking.csv').open(encoding='utf-8-sig')))
assert [r['id'] for r in csv_rows] == ids
for row, card in zip(csv_rows, data['cards']):
    assert int(row['position']) == card['importance_rank']
    assert row['reason'] == card['importance']['reason']
assert [r['id'] for r in csv.DictReader((BASE / 'site/catalog.csv').open(encoding='utf-8-sig'))] == ids
assert (BASE / 'site/importance-overview.md').read_text().count('\n## ') == 35
wrapper = (BASE / 'site/data.js').read_text()
offline = json.loads(wrapper[len('window.TCS_ATLAS='):-2].replace('<\\/', '</'))
assert offline == original

# Neither card age nor the older publication priority may affect importance.
changed = copy.deepcopy(data)
for card in changed['cards']:
    card['year'] = 1900 + int(card['id'].split('-')[1]) % 127
    card['rank'] = -card.get('rank', 0)
    card['updated_at'] = '2099-01-01'
apply_importance(changed)
assert [(c['id'], c['importance_rank']) for c in changed['cards']] == [(c['id'], c['importance_rank']) for c in data['cards']]

# A newly published, fully detailed but narrow question must not displace a landmark.
changed = copy.deepcopy(data)
example = copy.deepcopy(next(c for c in changed['cards'] if c['id'] == 'TCS-6498'))
example.update(id='TCS-999998', rank=10**30, importance=dict(score=55, method='editorial', reason='Focused test question.'))
changed['cards'].append(example)
retired = copy.deepcopy(example)
retired.update(id='TCS-999999', status='resolved', importance=dict(score=100, method='editorial', reason='Historical landmark test.'))
changed['cards'].append(retired)
next(a for a in changed['areas'] if a['area'] == example['area'])['count'] += 2
apply_importance(changed)
cards = [c for c in changed['cards'] if c['area'] == example['area']]
assert cards[0]['id'] == 'TCS-6498'
assert cards[-1]['status'] == 'resolved'
assert next(c for c in cards if c['id'] == retired['id'])['importance']['score'] == 100
assert all(c['status'] == 'resolved' for c in cards if c['importance_rank'] > retired['importance_rank'])

print(json.dumps(dict(categories=35, records=len(ids), assessed=data['meta']['importance']['assessed'],
    checks=['idempotent ranking', 'all category positions', 'new categories preserve provisional assessments',
            'date-independent importance', 'new detailed cards do not jump the queue',
            'resolved records last without losing historical score', 'CSV and offline parity', 'all-category overview'])))
