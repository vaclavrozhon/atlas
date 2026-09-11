"""Generate retrieval candidates for editorial duplicate checks, not automatic merges."""
import gzip,json,re,sys,unicodedata,hashlib
from pathlib import Path
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
HERE=Path(__file__).resolve().parent;ATLAS=HERE.parents[1]
LIB=ATLAS.parent.parent/'tcs-source-library'
sys.path.insert(0,str(ATLAS))
from taxonomy import BIG,SMALL
lib=json.loads((LIB/'library.json').read_text());areas=json.loads((LIB/'area-coverage.json').read_text())['areas']
cat=json.loads((ATLAS/'site/catalog.json').read_text())
with gzip.open(HERE/'baseline-catalog.json.gz','wt') as f:json.dump(cat,f)
(HERE/'source-library-input.json').write_text(json.dumps(lib,ensure_ascii=False,indent=2))
def normal(s):return re.sub(r'\W+',' ',unicodedata.normalize('NFKD',str(s)).lower()).strip()
def body(c):
 return ' '.join(str(s) for s in [c['title'],c.get('formal',''),c.get('source_formulation',{}).get('text',''),c.get('legacy',{}).get('question_excerpt','')] if s)
rows=[]
for s in lib['sources']:
 home=next((a['title'] for a in areas if s['id'] in a['source_ids']),None)
 for p in s['problems']:
  rows.append(dict(n=len(rows)+1,**p,source_title=s['title'],source_area=s['area'],home=home))
texts=[body(c) for c in cat['cards']];qs=[r['summary'] for r in rows]
vectorizer=TfidfVectorizer(strip_accents='unicode',stop_words='english',ngram_range=(1,2),sublinear_tf=True)
matrix=vectorizer.fit_transform(texts+qs);cm=matrix[:len(texts)];lm=matrix[len(texts):]
scores=(lm@cm.T).toarray();ls=(lm@lm.T).toarray();np.fill_diagonal(ls,0)
for i,r in enumerate(rows):
 top=np.argsort(scores[i])[-5:][::-1]
 r['candidates']=[dict(id=cat['cards'][int(j)]['id'],score=round(float(scores[i,j]),3),title=cat['cards'][int(j)]['title'],formal=cat['cards'][int(j)].get('source_formulation',{}).get('text') or cat['cards'][int(j)].get('formal'),evidence=cat['cards'][int(j)]['evidence'],status=cat['cards'][int(j)]['status'],refs=cat['cards'][int(j)]['references']) for j in top]
 top=np.argsort(ls[i])[-3:][::-1]
 r['library_candidates']=[dict(n=rows[int(j)]['n'],score=round(float(ls[i,j]),3),entry_key=rows[int(j)]['entry_key'],summary=rows[int(j)]['summary']) for j in top if ls[i,j]>.16]
(HERE/'screening.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(HERE/'input-fingerprints.json').write_text(json.dumps(dict(catalogue_version=cat['meta']['version'],catalogue_records=len(cat['cards']),library_sha256=hashlib.sha256((LIB/'library.json').read_bytes()).hexdigest(),source_entries=len(rows)),indent=2))
print('Indexed',len(rows),'source entries against',len(cat['cards']),'catalogue cards.')
