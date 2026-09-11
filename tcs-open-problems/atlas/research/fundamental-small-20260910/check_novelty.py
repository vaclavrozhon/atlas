import json,re,unicodedata
from pathlib import Path
D=Path(__file__).resolve().parent
cards=json.loads((D/'baseline.json').read_text())['records']
def norm(s):
 s=unicodedata.normalize('NFKD',s).lower()
 return ''.join(c for c in s if not unicodedata.combining(c)).replace('–','-').replace('—','-').replace('−','-')
prepared=[]
for c in cards:
 l=c.get('legacy') or {};sf=c.get('source_formulation') or {}
 q=' '.join(str(x) for x in [c['title'],c.get('formal'),sf.get('text'),l.get('question_excerpt')] if x)
 prepared.append((c,norm(q),norm(' '.join(r['title'] for r in c['references'][:1]))))
rows=[]
for line in (D/'seeds.tsv').read_text().splitlines():
 if line.startswith('#') or not line:continue
 cat,slug,title,pattern=line.split('|',3);rx=re.compile(pattern,re.I)
 matches=[]
 for c,qs,refs in prepared:
  sf=c.get("source_formulation") or {}
  if rx.search(qs):matches.append(dict(id=c['id'],area=c['area'],title=c['title'],question=sf.get('text') or c.get('formal'),type='question'))
  elif rx.search(refs):matches.append(dict(id=c['id'],area=c['area'],title=c['title'],question=sf.get('text') or c.get('formal'),type='source_context'))
 rows.append(dict(category=int(cat),slug=slug,title=title,pattern=pattern,matches=matches))
(D/'novelty-screen.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('seeds',len(rows))
for row in rows:
 qs=[m for m in row['matches'] if m['type']=='question'];print(row['category'],row['slug'],len(qs),len(row['matches'])-len(qs),','.join(m['id'] for m in qs[:7]))
