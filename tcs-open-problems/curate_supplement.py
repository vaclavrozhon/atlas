from curate_dagstuhl import make, ss, ROOT, json, re
rows=[]
x=next(x for x in ss if x['seminar']=='22301')
E={
'1.1':'Smaller shares for general secret sharing',
'1.2':'Abelian-group versus field secret sharing',
'1.3':'Information leakage in distributed OR',
'2.1':'The infimum of the Ingleton score',
'2.2':'Bounded-alphabet approximation of entropy-region faces',
'2.3':'Finite versus countable-support entropy regions',
'2.4':'Gaps on entropy-region boundary rays',
'2.5':'Non-entropic extreme entropy-cone rays',
'2.6':'Entropy profiles extending fixed distributions',
'3.1':'Maximizing conditional mutual information',
'3.2':'Interaction information for pairwise-factorized distributions',
'3.3':'Separating two common-information optimization bounds',
'3.4':'Entropy optimization underlying matrix multiplication',
'3.5':'Sharp thresholds for one-bottleneck information transmission',
'3.6':'Recovering higher entropy-extension profiles',
'4.2':'The fifth conditional Ingleton inequality',
'4.3':'Rational certificates for max-linear information inequalities',
'4.4':'Polyhedrality of linear-rank inequality cones',
'4.6':'Gaussian versus discrete multiinformation regions',
'4.7':'Separating entropy regions from group classes',
'5.1':'Recognizing entropic sparse paving matroids',
'5.2':'Entropic matroid approximations approaching unit ratio',
'6.2':'Coefficient bounds for independence-implication proofs',
'6.3':'Finite inference systems for structural semigraphoids',
'7.1':'Computability of entropic query-size bounds',
'7.2':'Complexity of polymatroid query-size bounds',
'7.5':'Proof length for Shannon-flow inequalities',
'8.2':'Deriving rank inequalities from entropy inequalities',
'8.3':'Field dependence of linear-rank inequalities',
'8.4':'Proof strength of bounded-copy entropy methods',
'8.5':'Maximum entropy versus the Copy lemma',
'8.6':'Explicit ternary functions resisting ten binary gates',
'9.2':'Complexity increase under independent bit noise',
'9.4':'Combinatorial forms of non-Shannon inequalities',
'9.5':'Combinatorial forms of conditional information inequalities'}
for num,title in E.items():
 marker='('+num+')';pos=x['text'].find(marker);assert pos>=0,num
 y=dict(x);y['pdf_page']=x['pdf_page']+x['text'][:pos].count('\f')
 r=make(y,title,'Problem '+marker);r['area']='Coding and information theory' if num[0] not in '17' else 'Cryptography' if num.startswith('1.') else 'Database theory and finite model theory'
 if num=='8.6':r['area']='Computational and circuit complexity'
 m=re.search(r'\[([^\[\]]+)\]',x['text'][pos:pos+1300]);r['authors']=m.group(1) if m and not re.fullmatch(r'\d+',m.group(1)) else ''
 rows.append(r)
# Individually numbered questions from a 2024 topology workshop, outside a main
# section literally named "Open Problems".
rs=json.loads((ROOT/'dagstuhl_reports.json').read_text());r=next(r for r in rs if r['seminar']=='24072')
T={3:'NP certificates for homeomorphism of three-manifolds',4:'coNP certificates for three-manifold homeomorphism',5:'NP-hardness of three-manifold homeomorphism',6:'Counting triangulations of the three-sphere',7:'Counting hyperbolic three-manifolds of bounded triangulation complexity',8:'Polynomial flip-distance bounds for three-manifold triangulations',9:'Manifold dependence of triangulation flip-distance growth',10:'Polynomial height paths between three-manifold triangulations',11:'NP recognition of small Seifert-fibred spaces',12:'NP recognition of closed hyperbolic three-manifolds',13:'Compact monodromy descriptions from triangulated surface bundles'}
for n,title in T.items():
 m=re.search(r'(?m)^\s*▶ Question '+str(n)+r'\.',r['text']);assert m,n
 y=dict(r,locator='3.4 (Homeomorphism)' ,section_title=title,pdf_page=r['pdf_page']+r['text'][:m.start()].count('\f'))
 z=make(y,title,'Question '+str(n));z['area']='Computational topology';z['authors']='Saul Schleimer';rows.append(z)
(ROOT/'supplement_rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print('SUPPLEMENT',len(rows))
