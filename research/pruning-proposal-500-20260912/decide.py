"""Persist explicitly authored decisions; never selects cards or edits the catalogue."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
path = HERE / 'decisions-draft.json'
decisions = json.loads(path.read_text()) if path.exists() else {}
old = json.loads((ROOT / 'research/pruning-proposal-300-20260912/decisions.json').read_text())['decisions']
old = {d['id']: d for d in old}
for line in sys.stdin:
    if not line.strip():
        continue
    identifier, reason = line.rstrip('\n').split('|', 1)
    identifier = 'TCS-' + identifier.removeprefix('TCS-').zfill(4)
    c = json.loads((ROOT / 'data/cards' / (identifier + '.json')).read_text())
    assert c['status'] != 'resolved', identifier
    if reason == 'RECONSIDER':
        decisions.pop(identifier, None)
    else:
        reused = reason == 'REAFFIRM'
        if reused:
            reason = old[identifier]['reason']
        decisions[identifier] = {'reason': reason, 'previous_proposal_reaffirmed': reused}
path.write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + '\n')
print('Proposed:', len(decisions))
