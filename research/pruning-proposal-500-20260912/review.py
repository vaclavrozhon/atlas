"""Read-only editorial viewer; records displayed fields and current input hashes."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
old = json.loads((ROOT / 'research/pruning-proposal-300-20260912/decisions.json').read_text())
old = {d['id']: d for d in old['decisions']}
paths = sorted((ROOT / 'data/cards').glob('*.json'))
cards = [json.loads(p.read_text()) for p in paths]
areas = sorted({c['area'] for c in cards})
if sys.argv[1] == 'areas':
    for i, area in enumerate(areas):
        print(i, area, sum(c['area'] == area and c['status'] != 'resolved' for c in cards))
    sys.exit()
ledger_path = HERE / 'read-ledger.json'
ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else {}
if sys.argv[1] == 'area':
    selected = [c for c in cards if c['area'] == areas[int(sys.argv[2])]]
    if len(sys.argv) > 3:
        selected = selected[int(sys.argv[3]):int(sys.argv[4])]
else:
    ids = {'TCS-' + x.removeprefix('TCS-').zfill(4) for x in sys.argv[2:]}
    selected = [c for c in cards if c['id'] in ids]
for c in selected:
    identifier = c['id']
    print(identifier[4:], c['title'], ('[RESOLVED]' if c['status'] == 'resolved' else ''))
    formal = c.get('formal', '')
    sentences = c.get('working_summary', {}).get('sentences', [])
    fields = ['title', 'status']
    if sys.argv[1] == 'full':
        for key in ['formal', 'definitions', 'answer_criterion', 'working_summary', 'why', 'importance', 'context_blocks', 'context', 'statement_review', 'quality_review', 'references', 'related_problem_ids']:
            if key in c:
                print(key + ':', json.dumps(c[key], ensure_ascii=False))
                fields.append(key)
    else:
        if formal and len(formal) < 600 and not formal.startswith(('A short source quotation', 'This record locates')) and formal != c['title']:
            print('Q:', formal)
            fields.append('formal')
        else:
            print('Q:', ' '.join(sentences[:2]))
            fields.append('working_summary.sentences[:2]')
        print('M:', sentences[3] if len(sentences) > 3 else c.get('why', ''))
        fields.append('working_summary.sentences[3]')
        if sys.argv[1] == 'detail':
            print('SUMMARY:', ' '.join(sentences))
            print('WHY:', c.get('why', ''))
            print('IMPORTANCE:', c.get('importance', {}).get('reason', ''))
            print('REF:', '; '.join(r.get('title','') + ' / ' + r.get('locator','') for r in c.get('references', [])))
            fields += ['working_summary', 'why', 'importance.reason', 'references.title', 'references.locator']
    if identifier in old:
        print('PREVIOUS PROPOSAL:', old[identifier]['reason'])
    raw = (ROOT / 'data/cards' / (identifier + '.json')).read_bytes()
    ledger.setdefault(identifier, []).append({'sha256': hashlib.sha256(raw).hexdigest(), 'fields': fields})
ledger_path.write_text(json.dumps(ledger, indent=2) + '\n')
