"""Display current cards for editorial screening without changing catalogue data."""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
baseline = json.loads((HERE / 'baseline.json').read_text())['cards']
active = [c for c in baseline if c['active']]
mode = sys.argv[1]
if mode == 'range':
    ids = [c['id'] for c in active[int(sys.argv[2]):int(sys.argv[3])]]
else:
    ids = ['TCS-' + x.removeprefix('TCS-').zfill(4) for x in sys.argv[2:]]
ledger_path = HERE / 'read-ledger.json'
ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else {}
area = None
for identifier in ids:
    path = ROOT / 'data/cards' / f'{identifier}.json'
    if not path.exists():
        print(identifier, 'REMOVED DURING REVIEW')
        continue
    raw = path.read_bytes()
    c = json.loads(raw)
    if c['area'] != area:
        area = c['area']
        print('\nAREA:', area)
    print(identifier[4:], c['title'])
    fields = ['title', 'area', 'status']
    if mode == 'range':
        sentences = c.get('working_summary', {}).get('sentences', [])
        if len(sentences) > 1:
            print('Q:', sentences[1])
            fields.append('working_summary.sentences[1]')
        else:
            print('Q:', c.get('formal', ''))
            fields.append('formal')
    elif mode == 'assess':
        formal = c.get('formal', '')
        ss = c.get('working_summary', {}).get('sentences', [])
        if formal and formal != c['title'] and not formal.startswith(('A short source quotation', 'This record locates')):
            print('TARGET:', formal)
            fields.append('formal')
        else:
            print('TARGET:', ' '.join(ss[:3]))
            fields.append('working_summary.sentences[:3]')
        print('MOTIVATION:', ' '.join(ss[3:]))
        fields.append('working_summary.sentences[3:]')
        why = c.get('why', '')
        if why and not why.startswith('The significance of this particular question has not yet'):
            print('WHY:', why)
            fields.append('why')
        print('SOURCE:', '; '.join(r.get('title', '') + ' / ' + r.get('locator', '') for r in c.get('references', [])[:2]))
        fields.append('references[:2].title,locator')
        if c.get('retention_review') or c.get('restoration_review'):
            print('PRIOR RETENTION:', json.dumps(c.get('retention_review') or c.get('restoration_review'), ensure_ascii=False))
            fields += ['retention_review', 'restoration_review']
    else:
        for key in ['formal', 'definitions', 'answer_criterion', 'why', 'working_summary', 'importance', 'source_formulation', 'statement_review', 'status_note', 'references', 'retention_review', 'restoration_review', 'source_consolidations']:
            if key in c:
                print(key + ':', json.dumps(c[key], ensure_ascii=False))
                fields.append(key)
        if mode == 'full':
            for key in ['context_blocks', 'context', 'progress', 'problem_relations']:
                if key in c:
                    print(key + ':', json.dumps(c[key], ensure_ascii=False))
                    fields.append(key)
    ledger.setdefault(identifier, []).append({'sha256': hashlib.sha256(raw).hexdigest(), 'mode': mode, 'fields': fields})
ledger_path.write_text(json.dumps(ledger, indent=2) + '\n')
