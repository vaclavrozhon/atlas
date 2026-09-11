from collect import *
import collections

rows=[];excluded=[]
def add(title,area,url,collection,year='',locator='',authors='',status='source_open_unverified',note='',kind='focused',**extra):
    rows.append(dict(title=title,area=area,source_url=url,source_collection=collection,source_year=str(year),source_locator=locator,authors=authors,status=status,status_note=note,scope=kind,accessed='2026-09-09',**extra))

def exclude(x,reason,solution=''):
    excluded.append(dict(title=x['title'],source_url=x['source_url'],reason=reason,solution_url=solution))

def unmojibake(s):
    try:return s.encode('latin1').decode('utf8')
    except:return s

# The same subject can appear in several collections. Keep one record per source
# question here, then perform cross-source review in the final builder.
SUB_EXCLUDE={10:'Resolved in the source update (Chakrabarti–Regev).',23:'Resolved in the source update (Andoni–Nguyen).',25:'The implication is settled positively for norms and negatively for general metrics in the source update.',29:'The source update supplies the requested multipass lower bounds.',31:'Linear information lower bound supplied in the source update.',39:'Source update explicitly reports a negative resolution (FOCS 2023).',40:'Source update explicitly reports a positive resolution.',47:'Source update reports an affirmative answer (Thaler).',65:'Source update reports a resolution (Yu, 2021).',100:'Source update reports a resolution (Narayanan–Tětek, 2022).',60:'The one-pass cardinality approximation barrier was resolved in 2026; remaining variants need separate formulations.',38:'Polynomial-query partition oracles were subsequently obtained; stale formulation excluded.',54:'Later fast Johnson–Lindenstrauss results supersede this old target; excluded pending exact comparison.',64:'Turnstile matching lower bounds and algorithms have since changed substantially; excluded pending exact comparison.',67:'Streaming Max-Cut hard-instance question has since had substantial resolutions; excluded pending exact comparison.'}
RTA_EXCLUDE={5:'The source comment reports a positive solution for the stated calculus.',56:'Decreasing diagrams characterize confluence for countable abstract reduction systems; stale question excluded.',90:'Context unification was proved decidable/in PSPACE; mixed original record excluded.',94:'Higher-order matching was proved decidable by Stirling; stale record excluded.'}
TOPP_EXCLUDE={52:'Planar graphs have bounded queue-number (Dujmović et al., 2020).',51:'Linear-volume 3D grid drawings follow from subsequent bounded queue-number results.',70:'The general Yao–Yao spanner question has subsequent resolutions; old unspecific formulation excluded.',35:'The cited NP-hardness question was subsequently resolved; extensions need separate statements.'}

for x in json.loads((ROOT/'harvested.json').read_text()):
    if x['http_status']!=200:
        exclude(x,'Primary page could not be retrieved.');continue
    k=x['collection'];t=x['text'];s=soup(fetch(x['source_url']));title=unmojibake(x['title']);year='';author='';locator=x.get('locator','');note='The source presents this as open; no exhaustive search for later resolutions was performed.'
    if k=='automata':
        if title.startswith('23.5 '):exclude(x,'Duplicate of Automata Exchange 23.8.');continue
        if title.startswith('20.6 '):exclude(x,'Broad application agenda, not a sufficiently specific open mathematical problem.');continue
        locator=title.split(' ')[0];title=title.split(' ',1)[1];year='20'+locator[:2]
        b=s.select_one('.article-entry') or s.select_one('.post-body') or s.body
        area='Automata and formal languages'
        if re.search(r'game|strateg|equilibr',title,re.I):area='Games, synthesis and verification'
        elif re.search(r'VASS|VAS\b|Petri|reachability|counter|linear loop|positivity|Matric',title,re.I):area='Infinite-state systems and verification'
        elif 'learning' in title.lower():area='Learning theory'
        a=s.select_one('.article-author');author=txt(a)
    elif k=='sublinear':
        n=int(re.search(r'Problem (\d+)',title).group(1));locator='Problem '+str(n);title=title.split(': ',1)[1]
        if n in SUB_EXCLUDE:exclude(x,SUB_EXCLUDE[n]);continue
        m=re.search(r'Source .*?(20\d\d)',t);year=m.group(1) if m else ''
        m=re.search(r'Suggested by (.*?) Source ',t);author=m.group(1) if m else ''
        area='Streaming and sketching'
        if re.search(r'testing|test|distribution|samples|Hellinger|support size',title,re.I):area='Property testing and distribution learning'
        if re.search(r'communication|information cost|Cryptogenography|Merlin',title,re.I):area='Communication complexity'
        if re.search(r'LOCAL|Local Computation',title):area='Distributed and local algorithms'
    elif k=='rta':
        n=int(re.search(r'Problem (\d+)',locator).group(1))
        if '[Solved]' in title or n in RTA_EXCLUDE:
            exclude(x,RTA_EXCLUDE.get(n,'Marked solved in the RTA source.'));continue
        m=re.search(r'Date: .*?(\d{4})',t);year=m.group(1) if m else ''
        m=re.search(r'Originator: (.*?) Date:',t);author=m.group(1) if m else ''
        area='Rewriting, lambda calculus and semantics'
        if re.search(r'unification|matching|constraint',title,re.I):area='Automated reasoning and unification'
        if re.search(r'^Design a notion|^Design pattern|^Give a definition|^Investigate|^Design a framework|^Extend|^Develop',title):
            exclude(x,'Research programme or underspecified request, rather than one clearly delimited problem.');continue
    else:
        n=int(re.search(r'Problem\s*(\d+)',title).group(1));locator='Problem '+str(n);title=re.sub(r'\s*\(Problem\s*\d+\)','',title)
        st=re.search(r'Status/Conjectures (.*?)(?:Partial and Related Results|Motivation|Appearances|Categories)',t)
        st=st.group(1) if st else ''
        if re.search(r'solved|settled|closed',st,re.I) or n in TOPP_EXCLUDE:
            exclude(x,TOPP_EXCLUDE.get(n,'Source status: '+st[:220]));continue
        rev=re.search(r'Entry Revision History (.*?)(?:Bibliography|$)',t)
        yy=re.findall(r'\b(?:19|20)\d\d\b',rev.group(1)) if rev else [];year=max(yy) if yy else ''
        author='Erik D. Demaine; Joseph S. B. Mitchell; Joseph O’Rourke (editors)';area='Computational geometry'
        if n==11:title='Truly subquadratic algorithms for 3SUM';area='Fine-grained complexity'
        if n==8:area='Optimization and mathematical programming'
        if n==33:area='Algebraic and numerical computation'
    add(title,area,x['source_url'],k,year,locator,author,note=note)

COLT_EXCLUDE={21:'The COLT 2023 multidistribution sample-complexity question was resolved by later work (COLT 2024).',48:'First-order contextual-bandit regret bounds were subsequently obtained.',55:'Subsequent parameter-free / scale-free online-learning results supersede the old formulation.',70:'Limited-advice adversarial-bandit question has subsequent resolutions; excluded pending exact comparison.',71:'Fast stochastic exp-concave rates have subsequent resolutions; excluded pending exact comparison.',73:'Thompson-sampling regret bounds were subsequently proved.',74:'Improper online logistic regression subsequently achieved improved logarithmic regret.',77:'Optimal last-iterate SGD results address the old averaging question.'}
for i,x in enumerate(json.loads((ROOT/'colt.json').read_text())):
    if i in COLT_EXCLUDE:exclude(x,COLT_EXCLUDE[i]);continue
    if x['http_status']!=200:exclude(x,'Individual primary publication page could not be retrieved.');continue
    title=re.sub(r'^(?:Invited )?Open [Pp]roblem:\s*','',x['title']).strip()
    yy=re.search(r'(\d\d)[a-z]\.html$',x['source_url']);year='20'+yy.group(1) if yy else x['source_year']
    area='Learning theory'
    if re.search(r'bandit|reinforcement|regret|online|experts|portfolio',title,re.I):area='Online algorithms, bandits and reinforcement learning'
    if re.search(r'privacy|private',title,re.I):area='Differential privacy'
    if re.search(r'optimization|gradient|SGD|SGD|loss surfaces|Eigenvalue|Langevin',title,re.I):area='Optimization and mathematical programming'
    if re.search(r'Tensor|tensor|Quantum',title):area='Algebraic and numerical computation' if 'Quantum' not in title else 'Quantum computation'
    add(title,area,x['source_url'],'COLT / PMLR',year,'Open-problem paper','; '.join(x.get('authors',[])),note='Published as an open-problem contribution; later resolution has not been exhaustively checked.',pdf_url=x.get('pdf_url',''))

for x in json.loads((ROOT/'crypto.json').read_text()):
    if x['http_status']==200:
        add(x['title'],'Cryptography',x['source_url'],'0xPARC research workshops',x['source_year'],'Problem page','0xPARC workshop contributors',note='Listed without the solved marker on the workshop problem index; later literature not exhaustively checked.')

if __name__=='__main__':
    (ROOT/'base_rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
    (ROOT/'base_excluded.json').write_text(json.dumps(excluded,ensure_ascii=False,indent=2))
    print('BASE',len(rows),'EXCLUDED',len(excluded),collections.Counter(x['source_collection'] for x in rows))
