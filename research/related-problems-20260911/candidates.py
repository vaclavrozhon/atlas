"""Suggest unlinked neighbors for editorial inspection; never writes card data."""
import collections,itertools,json,sys,numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from review import CARDS,normid
edges=set()
for line in open(__file__.replace('candidates.py','groups.tsv')):
    if line.startswith('#') or not line.strip():continue
    mode,label,ids=map(str.strip,line.split('|'));ids=[normid(x) for x in ids.split()]
    edges.update(tuple(sorted(e)) for e in (itertools.combinations(ids,2) if mode=='C' else ((ids[0],x) for x in ids[1:])))
deg=collections.Counter(x for e in edges for x in e)
cs=list(CARDS.values());ids=[c['id'] for c in cs]
def document(c):
    t=c['title'];raw=c.get('source_formulation',{}).get('text','')
    summary=' '.join(c.get('working_summary',{}).get('sentences',[]))
    formal=c.get('formal','')
    if formal.startswith(('This record locates','A short source quotation')):formal=''
    return ' '.join([t,t,raw,formal,summary])
x=TfidfVectorizer(stop_words='english',ngram_range=(1,2),max_df=.25,min_df=2,sublinear_tf=True).fit_transform([document(c) for c in cs])
scores=(x@x.T).toarray();np.fill_diagonal(scores,0)
chosen=sys.argv[1:]
if chosen and chosen[0]=='pairs':
    seen=set()
    for i,c in enumerate(cs):
        if deg[c['id']]:continue
        for j in scores[i].argsort()[-2:][::-1]:
            pair=tuple(sorted((ids[i],ids[j])))
            if scores[i,j]>=.20 and pair not in seen:
                print(f"{scores[i,j]:.2f} {ids[i][4:]} {c['title']} => {ids[j][4:]} {cs[j]['title']}")
                seen.add(pair)
    sys.exit()
elif chosen and chosen[0]=='zero':
    low,high=map(int,chosen[1:]);selected=[i for i,c in enumerate(cs) if not deg[c['id']]][low:high]
elif chosen:selected=[ids.index(normid(s)) for s in chosen]
else:selected=[i for i,c in enumerate(cs) if not deg[c['id']]]
for i in selected:
    c=cs[i];print('\n'+c['id'][4:]+' '+c['title'])
    for j in scores[i].argsort()[-4:][::-1]:
        if tuple(sorted((ids[i],ids[j]))) not in edges:print(f"  {scores[i,j]:.2f} {ids[j][4:]} {cs[j]['title']}")
