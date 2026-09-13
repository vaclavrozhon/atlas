"""Brief reading and hash ledger; editorial decisions are written separately."""
import hashlib
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
baseline = json.loads((HERE / 'baseline.json').read_text())
ledger_path = HERE / 'read-ledger.json'
ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else {}
if sys.argv[1] == 'range':
    ids = list(baseline['cards'])[int(sys.argv[2]):int(sys.argv[3])]
else:
    ids = ['TCS-' + i.removeprefix('TCS-').zfill(4) for i in sys.argv[2:]]
for identifier in ids:
    path = ROOT / 'data/cards' / (identifier + '.json')
    if not path.exists():
        print(identifier, 'REMOVED CONCURRENTLY')
        continue
    raw = path.read_bytes()
    c = json.loads(raw)
    print(identifier + ' | ' + c['title'])
    if sys.argv[1] == 'assess':
        print('SUMMARY:', ' '.join(c.get('working_summary', {}).get('sentences', [])))
        reason = c.get('importance', {}).get('reason', '')
        if reason and not reason.startswith('Importance has not been individually assessed'):
            print('IMPORTANCE:', reason)
    elif c.get('formal','').startswith(('A short source quotation', 'This record locates')):
        print('SOURCE QUESTION:', c.get('source_formulation', {}).get('text', ''))
        print('CONTEXT:', ' '.join(c.get('working_summary', {}).get('sentences', [])[:2]))
    elif c.get('formal') != c['title']:
        print('Q:', c.get('formal', ''))
    fields = ['title', 'formal']
    if sys.argv[1] == 'assess':
        fields = ['title', 'working_summary', 'importance.reason']
    if c.get('formal','').startswith(('A short source quotation', 'This record locates')):
        fields += ['source_formulation.text', 'working_summary.sentences[:2]']
    if sys.argv[1] == 'detail':
        print('WHY:', c.get('why', ''))
        print('SUMMARY:', ' '.join(c.get('working_summary', {}).get('sentences', [])))
        print('IMPORTANCE:', c.get('importance', {}).get('reason', ''))
        print('SOURCE:', '; '.join(r['title']+' ('+r.get('locator','')+')' for r in c.get('references', [])[:2]))
        fields += ['why', 'working_summary', 'importance.reason', 'first two source titles and locators']
    previous = ledger.get(identifier, {})
    ledger[identifier] = {'sha256': hashlib.sha256(raw).hexdigest(),
        'fields': sorted(set(fields + previous.get('fields', [])))}
tmp = ledger_path.with_suffix('.tmp')
tmp.write_text(json.dumps(ledger, indent=2)+'\n')
os.replace(tmp, ledger_path)
