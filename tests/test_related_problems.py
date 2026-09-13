"""Related links stay symmetric and safe across publication and retirement."""

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from related_problems import apply_related_problems


def card(identifier, targets=(), **extra):
    return dict(id=identifier, status='source_open', related_problem_ids=list(targets), **extra)


source = [card('TCS-0001', ['TCS-0002']), card('TCS-0002'), card('TCS-0003')]
reader = copy.deepcopy(source)
apply_related_problems(reader)
assert reader[1]['related_problem_ids'] == ['TCS-0001']
assert source[1]['related_problem_ids'] == []
assert reader[2]['related_problem_ids'] == []
again = copy.deepcopy(reader)
apply_related_problems(again)
assert again == reader

# Retirement and deletion work even when the source of an incoming edge is untouched.
reader[1]['status'] = 'resolved'
apply_related_problems(reader)
assert all(not c['related_problem_ids'] for c in reader)
reader = [copy.deepcopy(source[0])]
apply_related_problems(reader, {'TCS-0002'})
assert reader[0]['related_problem_ids'] == []
reader = [source[0], card('TCS-0002', scope_exclusion={'reason': 'fixture'})]
apply_related_problems(reader)
assert all(not c['related_problem_ids'] for c in reader)

for targets in [['TCS-9999'], ['TCS-0001'], ['TCS-0002', 'TCS-0002'], [None], [123]]:
    try:
        apply_related_problems([card('TCS-0001', targets), card('TCS-0002')])
    except ValueError:
        pass
    else:
        raise AssertionError(f'Invalid related IDs accepted: {targets}')

print('Related problems: symmetry, isolation, stable order, retirement, deletion, invalid targets')
