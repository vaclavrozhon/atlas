"""Materialize explicit, two-pass editorial decisions; never choose IDs by a score cut."""
import collections,csv,datetime,gzip,hashlib,io,json,sys
from pathlib import Path
BASE=Path(__file__).resolve().parents[2]
RESEARCH=Path(__file__).resolve().parent
DEST=BASE/'to_delete/large-buckets-20260910'
DATE='2026-09-10'

def dump(path,value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')

def csvfile(path,rows,fields):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)

TEMPLATES={
 'fragment': 'The saved passage does not identify a sufficiently independent research target: its meaning depends on surrounding proof, algorithm or source-specific context. Reinstatement needs a precise question and a case for its independent significance.',
 'followup': 'This is an extension or refinement of a particular construction, algorithm or analysis. The saved record does not establish consequences broad enough to prioritize it as a separate problem in the 1,000-problem atlas.',
 'specialized': 'This targets a restricted model or input family, a small parameter case, or a source-specific quantity. Its currently documented reach is too narrow relative to the retained foundational questions in the category.',
 'not_problem': 'This records a research direction, model proposal, technique-development request or implementation task, rather than a single new mathematical problem with a clear settlement criterion.',
 'resolved': 'The existing individual review already marks this question resolved. Its complete historical card is preserved in the archive, outside the pool for selecting open problems.',
 'duplicate': 'This passage restates a question retained in {duplicate_of}. Keep the retained statement as the candidate; preserve this source record here for traceability.'}
CUSTOM={
 'TCS-4834':'An extraction false positive: “open” refers to qubits left uncontracted in a tensor, not to an unresolved research problem.',
 'TCS-1579':'An extraction false positive: “open bisimilar” names an equivalence relation. The sentence describes a congruence proof obligation, not an independent frontier question.',
 'TCS-1721':'An extraction false positive: “requests remain open” describes pending requests at an algorithmic boundary.',
 'TCS-2099':'An extraction false positive: leaving assignments open is an algorithmic optimization inside a proof procedure.',
 'TCS-2844':'An extraction false positive: “leave losing trades open” describes a trading model.',
 'TCS-3125':'An extraction false positive: opening and traversing doors describes a motion-planning gadget.',
 'TCS-4304':'An extraction false positive: “remains open” refers to the state of an object in the current algorithm.',
 'TCS-4513':'The authors intentionally leave the components of a general model unspecified. This is a definition-design choice, not a stated open problem.',
 'TCS-5102':'An extraction false positive: an extremal port “remains open” in the normalization process.',
 'TCS-5763':'The text says participants do not know the dealer-selected configuration. That is a protocol information constraint, not an unresolved scientific question.',
 'TCS-5886':'The text explains how two formulations of a recovery problem are equivalent despite unknown inputs; it does not formulate an open problem.',
 'TCS-6086':'An extraction false positive: not knowing whether a variable will be needed explains non-strict evaluation.',
 'TCS-6355':'The text explains which execution data are unknown before a network runs. It does not pose an independent open problem.',
 'TCS-0473':'The existing disposition identifies a request for a simpler analysis of an established path-compression bound. A new exposition or proof would not resolve a new frontier problem.',
 'TCS-0476':'The existing disposition identifies a proposal for extending the word-RAM model. It does not state one sufficiently specified open problem.',
 'TCS-6462':'This asks whether eight uses of a particular native gate are optimal for Toffoli synthesis. It is a fixed-gate, fixed-size synthesis refinement, too narrow for this atlas.',
 'TCS-6463':'This asks for alternative filters improving one eigenvalue-estimation method. It is method development without a stated general complexity barrier.',
 'TCS-6464':'This asks which of the paper’s concentration inequalities performs better in a given setup, rather than stating a fundamental missing bound.',
 'TCS-6468':'This requests a tailored decoder for the paper’s concatenated code family. The record supplies no category-wide decoding barrier.',
 'TCS-1730':'The target is improving a specific minimal-perfect-hashing implementation to within 0.1 bits per key of its lower bound, with comparable speed. The performance-tuning scope is too narrow.',
 'TCS-3652':'The text reports that Qiskit was too slow to run a larger benchmark. Missing experimental measurements are not an open TCS problem.',
 'TCS-3796':'The text describes hiding correspondence information in a manifold-alignment experiment. It is an experimental procedure, not a conjecture.',
 'TCS-4845':'The saved passage itself reports that the conjecture has been proved. It supplies no remaining question; this is a source-extraction issue rather than a new status determination.',
 'TCS-4067':'The saved passage explicitly introduces a positive answer about TimSort. It is a statement of a result, not a newly unresolved question.',
 'TCS-6931':'Finding further practical quantum speedups is a broad research program. The record does not specify a problem, computational model and target bound whose resolution could be judged.',
 'TCS-6932':'Inventing new quantum algorithmic techniques is a research aspiration. This record has no individual mathematical question or settlement criterion.',
 'TCS-6972':'Integrating compact data structures into a SPARQL database engine is a software-development project, not a stand-alone foundational open problem.',
 'TCS-6992':'Implementing proposed cryptosystems in GAP is an engineering task. Preserve the source note, but remove it from the open-problem candidate pool.',
 'TCS-6778':'This asks for hardness classifications of eight residual bounded-degree spanner cases. These are follow-up cells in a classification table, rather than one broad new barrier.',
 'TCS-6997':'This is verification of synchronization and a claimed compression threshold for one explicitly constructed automaton family. The general synchronization questions remain represented.'}

def build():
    DEST.mkdir(parents=True,exist_ok=True)
    if (DEST/'manifest.json').exists():raise SystemExit('Archive already exists; edit its states rather than overwriting the frozen snapshot.')
    raw=(BASE/'site/catalog.json').read_bytes();data=json.loads(raw)
    cards={c['id']:c for c in data['cards']}
    baseline=json.loads(gzip.decompress((RESEARCH/'catalog-before.json.gz').read_bytes()))
    baseline_ids={c['id'] for c in baseline['cards']}
    decisions=json.loads((RESEARCH/'decisions.json').read_text())
    group_names={f"{a['position']:02d}":a['area'] for a in data['areas'] if a['group']=='large'}
    removals={}
    for group,labels in decisions.items():
        for code,values in labels.items():
            for short_id in (values if isinstance(values,dict) else values.split()):
                id='TCS-'+short_id
                assert id not in removals,id
                c=cards[id]
                assert c.get('selection_group')=='large' and c['area']==group_names[group],(id,c['area'],group)
                mate='TCS-'+values[short_id] if isinstance(values,dict) else None
                q=c.get('source_formulation',{}).get('text') or c.get('legacy',{}).get('question_excerpt') or c.get('formal') or c['title']
                anchor=' '.join(q.split()[:24])
                reason=CUSTOM.get(id,TEMPLATES[code].format(duplicate_of=mate))
                if id not in CUSTOM and code not in {'resolved','duplicate'}:reason+=' Saved target: “'+anchor+(' …' if len(q.split())>24 else '')+'”.'
                removals[id]=dict(state='quarantined',category=c['area'],reason_code=code,reason=reason,decided_on=DATE,decision_basis='Two-pass editorial triage of saved formulations, titles and source context; provisional selection, not a fresh proof or open-status review.')
                if mate:removals[id]['duplicate_of']=mate
    for id,item in removals.items():
        if item.get('duplicate_of'):assert item['duplicate_of'] in cards and item['duplicate_of'] not in removals,(id,item['duplicate_of'])
    removed_cards=[cards[id] for id in sorted(removals)]
    raw_archive=json.dumps(removed_cards,ensure_ascii=False,indent=2)+'\n'
    (DEST/'records.json').write_text(raw_archive,encoding='utf8')
    (DEST/'catalog-before.json.gz').write_bytes(gzip.compress(raw))
    reviewed=[c for c in data['cards'] if c.get('selection_group')=='large']
    counts=[]
    for a in data['areas']:
        if a['group']!='large':continue
        n=sum(v['category']==a['area'] for v in removals.values())
        counts.append(dict(category=a['area'],before=a['count'],removed=n,remaining=a['count']-n))
    manifest=dict(schema_version=1,review_id='large-buckets-20260910',date=DATE,
        source_version=data['meta']['version'],source_total=len(cards),reviewed_large_count=len(reviewed),
        baseline_large_count=sum(c.get('selection_group')=='large' for c in baseline['cards']),
        concurrent_large_additions=sum(c['id'] not in baseline_ids for c in reviewed),
        provisional_removed=len(removals),large_remaining=len(reviewed)-len(removals),
        category_counts=counts,reason_counts=dict(collections.Counter(x['reason_code'] for x in removals.values())),
        archive_file='records.json',archive_sha256=hashlib.sha256(raw_archive.encode()).hexdigest(),
        records=removals)
    dump(DEST/'manifest.json',manifest)
    csvfile(DEST/'decisions.csv',[dict(id=id,title=cards[id]['title'],**item,source=cards[id]['references'][0]['url'] if cards[id]['references'] else '') for id,item in removals.items()],['id','title','category','state','reason_code','reason','duplicate_of','source'])
    restored=json.loads((RESEARCH/'second-pass-retained.json').read_text());restored={f'TCS-{i}' for ids in restored.values() for i in ids}
    csvfile(DEST/'all-reviewed.csv',[dict(id=c['id'],title=c['title'],category=c['area'],decision='quarantine' if c['id'] in removals else 'retain',basis=removals[c['id']]['reason_code'] if c['id'] in removals else ('retain after second look: significant or uncertain boundary' if c['id'] in restored else 'retain: independent barrier, broad question or insufficient grounds to discard'),concurrent_addition=c['id'] not in baseline_ids) for c in reviewed],['id','title','category','decision','basis','concurrent_addition'])
    print(json.dumps({k:manifest[k] for k in ['reviewed_large_count','concurrent_large_additions','provisional_removed','large_remaining','reason_counts','category_counts']},ensure_ascii=False,indent=2))

if __name__=='__main__':build()
