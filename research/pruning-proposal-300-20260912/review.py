"""Read current cards and record the exact scope of this editorial screen.

This helper never changes canonical cards and never selects or deletes them.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = HERE / 'baseline.json'
if not BASE.exists():
    cards = []
    for path in sorted((ROOT / 'data/cards').glob('*.json')):
        raw = path.read_bytes()
        card = json.loads(raw)
        cards.append({'id': card['id'], 'area': card['area'], 'status': card['status'],
                      'sha256': hashlib.sha256(raw).hexdigest()})
    cards.sort(key=lambda c: (c['area'], c['id']))
    BASE.write_text(json.dumps({'date': '2026-09-12', 'cards': cards}, indent=2) + '\n')
baseline = json.loads(BASE.read_text())['cards']
ledger_path = HERE / 'read-ledger.json'
ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else {}
mode = sys.argv[1]
if mode == 'range':
    ids = [c['id'] for c in baseline[int(sys.argv[2]):int(sys.argv[3])]]
else:
    ids = ['TCS-' + x.removeprefix('TCS-').zfill(4) for x in sys.argv[2:]]
area = None
for identifier in ids:
    path = ROOT / 'data/cards' / f'{identifier}.json'
    if not path.exists():
        print(identifier, 'REMOVED CONCURRENTLY')
        continue
    raw = path.read_bytes()
    c = json.loads(raw)
    if area != c['area']:
        area = c['area']
        print('\nAREA:', area)
    print(identifier, '|', c['title'], ('[RESOLVED]' if c['status'] == 'resolved' else ''))
    fields = ['title', 'formal', 'status']
    formal = c.get('formal', '')
    if formal and formal != c['title']:
        print('Q:', formal)
    if not formal or formal == c['title'] or formal.startswith(('A short source quotation', 'This record locates')):
        source = c.get('source_formulation', {}).get('text', '')
        if source:
            print('EXCERPT:', source)
            fields.append('source_formulation.text')
        print('TASK:', ' '.join(c.get('working_summary', {}).get('sentences', [])[:2]))
        fields.append('working_summary.sentences[:2]')
    if mode != 'range':
        print('SUMMARY:', ' '.join(c.get('working_summary', {}).get('sentences', [])))
        why = c.get('why', '')
        reason = c.get('importance', {}).get('reason', '')
        if not why.startswith('The significance of this particular question has not yet'):
            print('WHY:', why)
            fields.append('why')
        if not reason.startswith('Importance has not been individually assessed'):
            print('IMPORTANCE:', reason)
            fields.append('importance.reason')
        print('SOURCES:', '; '.join(r.get('title','') + ' / ' + r.get('locator','') for r in c.get('references', [])))
        fields += ['working_summary', 'references.title', 'references.locator']
    if mode == 'full':
        for key in ['definitions', 'answer_criterion', 'context', 'context_blocks', 'statement_review', 'quality_review', 'related_problem_ids']:
            if key in c:
                print(key.upper() + ':', json.dumps(c[key], ensure_ascii=False))
                fields.append(key)
    previous = ledger.get(identifier, {})
    history = previous.get('reads', [])
    history.append({'sha256': hashlib.sha256(raw).hexdigest(), 'fields': fields})
    ledger[identifier] = {'reads': history}
ledger_path.write_text(json.dumps(ledger, indent=2) + '\n')
