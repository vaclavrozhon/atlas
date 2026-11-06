import json,sys
from pathlib import Path
here=Path(__file__).resolve().parent
root=here.parents[1]
g=next(g for g in json.loads((here/'categories.json').read_text()) if g['id']==sys.argv[1])
for row in g['cards']:
 c=json.loads((root/'data/cards'/(row['id']+'.json')).read_text())
 print(c['id'][4:],row['color'][0],c['title'])
 print(' | '.join(f"{r['id']}:{r.get('year')} {r['title']}" for r in c['references']))
