"""Display all remaining summary and significance text for selected candidates."""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
decisions = json.loads((HERE / 'decisions-draft.json').read_text())
ledger_path = HERE / 'read-ledger.json'
ledger = json.loads(ledger_path.read_text())
ids = sorted(decisions)
for identifier in ids[int(sys.argv[1]):int(sys.argv[2])]:
    path = ROOT / 'data/cards' / (identifier + '.json')
    if not path.exists():
        print(identifier, 'REMOVED CONCURRENTLY')
        continue
    raw = path.read_bytes()
    c = json.loads(raw)
    print(identifier[4:], c['title'], '[' + c['status'] + ']')
    sentences = c.get('working_summary', {}).get('sentences', [])
    print('REMAINING SUMMARY:', ' '.join(sentences[i] for i in [2,4] if i < len(sentences)))
    why = c.get('why', '')
    imp = c.get('importance', {}).get('reason', '')
    if not why.startswith('The significance of this particular question has not yet'):
        print('WHY:', why)
    if not imp.startswith('Importance has not been individually assessed'):
        print('IMPORTANCE CASE:', imp)
    ledger.setdefault(identifier, []).append({'sha256': hashlib.sha256(raw).hexdigest(), 'fields': ['working_summary.sentences[2,4]', 'why (if substantive)', 'importance.reason (if assessed)']})
ledger_path.write_text(json.dumps(ledger, indent=2) + '\n')
