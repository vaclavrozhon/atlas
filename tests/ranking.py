"""Catalogue regressions for importance ordering, preservation, and exports."""
import copy
import csv
import json
import sys
from pathlib import Path
from unittest.mock import patch

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / 'scripts'))
from importance import apply_importance
from benchmark_selection import QUOTAS, eligible, members, read_selection

data = json.loads((BASE / 'build/catalog.json').read_text())
original = copy.deepcopy(data)
apply_importance(data)
assert data == original, 'Reapplying the ranking must be idempotent'
assert len(data['areas']) == data['meta']['taxonomy']['large_groups'] + data['meta']['taxonomy']['small_groups']
assert sum(a['target'] for a in data['areas']) == data['meta']['taxonomy']['assigned_target']
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
        if not card.get('benchmark_focus'):
            assert score <= previous.get(status_group, 100)
            previous[status_group] = score

heads = {a['area']: next((c['id'] for c in data['cards'] if c['area'] == a['area']), None) for a in data['areas']}
# The reviewed focus prefix precedes the score-ordered remainder.
selection = {a['area']: a for a in read_selection()['areas']}
for area in data['areas']:
    candidates = [c for c in data['cards'] if c['area'] == area['area']]
    if not candidates:
        assert area['count'] == 0 and heads[area['area']] is None
        continue
    active = [c for c in candidates if c['status'] != 'resolved'] or candidates
    expected = [entry['id'] for entry in selection[area['area']]['selected']]
    assert [c['id'] for c in candidates[:len(expected)]] == expected
    assert all(c.get('benchmark_focus') for c in candidates[:len(expected)])
    assert not any(c.get('benchmark_focus') for c in candidates[len(expected):])

# Editorial pruning may leave focus places unreviewed. Every surviving choice
# must still be valid, and the report must identify exactly the resulting gaps.
assert set(selection) == {a['area'] for a in data['areas']}
expected_focus_issues = []
for area in data['areas']:
    available = {c['id'] for c in data['cards'] if c['area'] == area['area'] and eligible(c)}
    chosen = [entry['id'] for entry in selection[area['area']]['selected']]
    assert len(chosen) == len(set(chosen)) and set(chosen) <= available
    missing = min(QUOTAS['top100'][area['group']], len(available)) - len(chosen)
    assert missing >= 0
    if missing:
        expected_focus_issues.append(f"Unreviewed focus places in {area['area']}: {missing}")
assert sorted(data['meta']['benchmark_selection']['issues']) == sorted(expected_focus_issues)
assert QUOTAS == {'top100': {'large': 5, 'small': 2},
                  'top500': {'large': 25, 'small': 10},
                  'top1000': {'large': 50, 'small': 20}}
for smaller, larger in [('top100', 'top500'), ('top500', 'top1000')]:
    prefix = members(data, smaller)
    prefix_ids = {c['id'] for c in prefix}
    assert prefix == [c for c in members(data, larger) if c['id'] in prefix_ids], \
        'Larger selections must preserve every smaller selection and its order'
for name, quotas in QUOTAS.items():
    exported = json.loads((BASE / 'build' / (name + '.json')).read_text())
    assert exported['cards'] == members(data, name)
    assert exported['subbenchmark'] == data['meta']['benchmarks'][name]
    assert exported['subbenchmark']['target'] == int(name.removeprefix('top'))
    assert exported['subbenchmark']['tentative'] == (name == 'top1000')
    assert exported['areas'] == data['areas'], 'All selections must share the category order'
    assert all(eligible(c) for c in exported['cards'])
    for area in data['areas']:
        available = sum(c['area'] == area['area'] and eligible(c) for c in data['cards'])
        assert sum(c['area'] == area['area'] for c in exported['cards']) == min(quotas[area['group']], available)
        expected = [c for c in data['cards'] if c['area'] == area['area'] and eligible(c)][:quotas[area['group']]]
        assert [c for c in exported['cards'] if c['area'] == area['area']] == expected

csv_rows = list(csv.DictReader((BASE / 'build/importance-ranking.csv').open(encoding='utf-8-sig')))
assert [r['id'] for r in csv_rows] == ids
for row, card in zip(csv_rows, data['cards']):
    assert int(row['position']) == card['importance_rank']
    assert row['reason'] == card['importance']['reason']
assert [r['id'] for r in csv.DictReader((BASE / 'build/catalog.csv').open(encoding='utf-8-sig'))] == ids
assert (BASE / 'build/importance-overview.md').read_text().count('\n## ') == len(data['areas'])
wrapper = (BASE / 'build/data.js').read_text()
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

# Formal resolution or an archive decision invalidates a focus choice without
# restoring it, changing its historical score or silently certifying a replacement.
for update in [dict(status='resolved'), dict(scope_exclusion={'reason': 'Fixture archive'})]:
    changed = copy.deepcopy(data)
    chosen = next(c for c in changed['cards'] if c['id'] == 'TCS-0001')
    previous_score = chosen['importance']['score']
    chosen.update(update)
    apply_importance(changed)
    assert 'benchmark_focus' not in chosen
    assert chosen['importance']['score'] == previous_score
    assert chosen['id'] not in {c['id'] for c in members(changed, 'top1000')}
    assert f"Review focus replacement for {chosen['id']} in {chosen['area']}" in changed['meta']['benchmark_selection']['issues']

# Removing an editorial choice clears a stale saved promotion on republication.
review = read_selection()
complexity = next(a for a in review['areas'] if a['area'] == 'Computational complexity')
removed = complexity['selected'].pop()
changed = copy.deepcopy(data)
with patch('benchmark_selection.read_selection', return_value=review):
    apply_importance(changed)
assert 'benchmark_focus' not in next(c for c in changed['cards'] if c['id'] == removed['id'])
assert f"Unreviewed focus places in {complexity['area']}: 1" in changed['meta']['benchmark_selection']['issues']

print(json.dumps(dict(categories=len(data['areas']), records=len(ids), assessed=data['meta']['importance']['assessed'],
    checks=['idempotent ranking', 'all category positions including empty categories', 'new categories preserve provisional assessments',
            'date-independent importance', 'new detailed cards do not jump the queue',
            'resolved records last without losing historical score', 'CSV and offline parity', 'all-category overview',
            'editorial focus prefixes and explicit unreviewed places', 'nested Top 100, Top 500 and possible Top 1000 exports',
            'shared category and problem order across all three targets', 'explicit quota shortfalls',
            'resolved and archived focus choices invalidated', 'removed choices clear stale promotions'])))
