"""Print compact source evidence for one category's requested cards."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
groups = json.loads((HERE / 'categories.json').read_text())
group = next(g for g in groups if g['id'] == sys.argv[1])
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
count = int(sys.argv[3]) if len(sys.argv) > 3 else len(group['cards'])
for row in group['cards'][start:start+count]:
    c = json.loads((ROOT / 'data/cards' / (row['id'] + '.json')).read_text())
    print('\n', c['id'], row['color'], c['title'])
    print('TARGET:', c['formal'][:500].replace('\n', ' '))
    print('SOURCES:', ' | '.join(f"{r['id']} [{r.get('year')}] {r['title']}" for r in c['references']))
    text = '\n'.join(b['text'] for b in c.get('context_blocks', []))
    if not text:
        text = c.get('context', '')
    for sentence in re.split(r'(?<=[.!?])\s+|\n\n', text):
        if re.search(r'\b(?:1[0-9]{3}|20[0-2][0-9])\b', sentence) and re.search(r'conjectur|propos|introduc|formulat|ask|open|histor|origin|problem|first', sentence, re.I):
            print('DATED:', sentence[:1000])

