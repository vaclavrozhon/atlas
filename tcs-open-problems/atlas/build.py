"""Build a portable, auditable reading catalogue without overwriting the old index.

Source cards are explicitly incomplete dossiers. Automatic extraction is never
promoted to the individually reviewed tier. Source excerpts are capped per paper.
"""
import collections,csv,hashlib,html,importlib.util,json,re,sys,unicodedata
from pathlib import Path
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parent/'expand'))
from select_expansion import norm as oldnorm,choose
from profiles import AREAS,CRITERIA
from reviewed import CARDS as REVIEWED
import english_content  # Applies the user's English-only preference to editorial copy.
spec=importlib.util.spec_from_file_location('confclassify',BASE.parent/'stoc-focs-comparison/classify.py')
cl=importlib.util.module_from_spec(spec);spec.loader.exec_module(cl)
DATE='2026-09-10'
TARGET=2600
def clean(s):
    s=html.unescape(str(s or ''))
    s=re.sub(r'<[^>]+>',' ',s)
    s=unicodedata.normalize('NFKC',s).replace('\u00ad','')
    return re.sub(r'\s+',' ',re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]','',s)).strip()
def year(s):
    m=re.search(r'(?:19|20)\d{2}',str(s));return int(m[0]) if m else None
def norm(s):return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',clean(s)).encode('ascii','ignore').decode().lower())
def author(s):return '; '.join(s) if isinstance(s,list) else clean(s)
def source_key(s):return clean(s).lower().replace('http://','https://').rstrip('/')
def classify(x):
    if x['venue']=='Quantum':return 'Quantum computation'
    t=clean(x['selected_sentence'])+' '+clean(x['paper_title'])
    if re.search(r'average.case|planted clique|planted dense|low.degree method|pessiland|spiked|statistical.computational',t,re.I):return 'Average-case complexity'
    for area,rx in cl.RULES:
        if re.search(rx,t,re.I):return cl.AREAS[area]
    for tag in x.get('classifications',[]):
        for area,rx in cl.RULES:
            if re.search(rx,tag,re.I):return cl.AREAS[area]
    return {'Cryptology ePrint':'Cryptography','FORC':'Differential privacy','TQC':'Quantum computation','ITC':'Cryptography','CCC':'Computational and circuit complexity','COLT':'Learning theory','ALT':'Learning theory','SoCG':'Computational geometry','IPEC':'Parameterized and exact algorithms'}.get(x['venue'],'General algorithm design')
def criterion(text):
    return next((key for key,v in CRITERIA.items() if re.search(v['pattern'],text,re.I)),None)
def quoted(s,n=25):
    w=clean(s).split();return ' '.join(w[:n])+(' […]' if len(w)>n else '')
def write_csv(path,rows,fields):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)

def main():
    old=json.loads((BASE.parent/'output/catalog.json').read_text())
    registry_path=BASE/'id_registry.json'
    registry=json.loads(registry_path.read_text()) if registry_path.exists() else {}
    last=max([4695]+[int(v.split('-')[-1]) for v in registry.values()])
    def identifier(key):
        nonlocal last
        if key not in registry:last+=1;registry[key]=f'TCS-{last:04d}'
        return registry[key]
    conference=json.loads((BASE.parent/'stoc-focs-comparison/papers_classified_internal.json').read_text())
    confcounts=collections.Counter(x['area'] for x in conference);oldcounts=collections.Counter(x['area'] for x in old)
    deficit={a:confcounts[a]/len(conference)-oldcounts[a]/len(old) for a in AREAS}
    reviewed=[dict(x) for x in REVIEWED]
    # A source used in an authored dossier does not also become a mechanical card.
    reserved_sources={source_key(r['url']) for x in reviewed for r in x['references']}
    oldids={x.get('candidate_id') for x in old}
    oldexact={norm(x['title'].replace('[…]','')) for x in old}
    oldprefixes={norm(x['title'].replace('[…]','')) for x in old if '[…]' in x['title']}
    byoldsrc=collections.defaultdict(list)
    for x in old:
        byoldsrc[source_key(x['source_url'])].append(x)
    candidates=[];audit=[];paperkeys={};seen_candidates=set()
    for f in sorted((BASE/'research/extractions').glob('*.json')):
        for raw in json.loads(f.read_text()):
            cid=raw['candidate_id']
            if cid in oldids or cid in seen_candidates:continue
            seen_candidates.add(cid);x=choose(raw)
            if not x:continue
            s=clean(x['selected_sentence']);x['selected_sentence']=s;x['paper_title']=clean(x['paper_title']);x['area']=classify(x);why=criterion(s)
            reject=None
            qkey=norm(s)
            if qkey in oldexact or any(qkey.startswith(pref) for pref in oldprefixes if len(pref)>45):reject='same formulation as old index'
            if source_key(x['source_url']) in reserved_sources:reject='source handled in authored dossier'
            if not why:reject='no identifiable structural criterion'
            # Remove incomplete questions and evident references to a missing subject.
            if len(s.split())<7:reject='too short to identify a question'
            if re.search(r'\b(?:this (?:problem|question|result|setting|bound|issue|approach|gap)|these (?:results|bounds|questions)|our (?:algorithm|result|construction|bound|method)|such (?:a |an )?(?:algorithm|result|construction|bound|assumption)|the other direction|it (?:can|could) be (?:done|improved))\b',s,re.I):
                x['needs_context']=True
            if re.search(r'open (?:legs|wire)|we (?:resolve|settle|disprove|answer)|is (?:answered|resolved|settled)|remains? (?:to be )?seen|numerical (?:data|evidence)|experimental|experimentally|in practice|real.world|benchmark|future work.*implementation',s,re.I):reject='not a substantiated theoretical open question'
            if re.search(r'\b(?:we conjecture (?:this|the) (?:difference|scaling)|physical interpretation|what would be|to understand this issue)\b',s,re.I):reject='insufficient mathematical target'
            # Whole-paper duplicate across FOCS / ECCC / ePrint versions.
            x['paper_key']=norm(x['paper_title']);x['criterion']=why
            x['score']=(max(-.02,deficit[x['area']])*1300)+(x['year']-2010)*2+x.get('selection_score',0)+(25 if len(s.split())<=25 else 0)-(30 if x.get('needs_context') else 0)+(12 if x['venue'] in ['Quantum','Cryptology ePrint','ECCC','FORC','FOCS'] else 0)
            if reject:audit.append(dict(candidate_id=cid,decision='excluded',reason=reject));continue
            candidates.append(x)
    candidates.sort(key=lambda x:(-x['score'],x['candidate_id']))
    selected=[];seen_papers=set();seen_questions=set();near=collections.defaultdict(list)
    for x in candidates:
        q=norm(x['selected_sentence']);sk=x['paper_key']
        if sk in seen_papers or q in seen_questions:
            audit.append(dict(candidate_id=x['candidate_id'],decision='excluded',reason='same paper version or same question'));continue
        # Same-source near duplicates of legacy excerpts are dropped conservatively.
        words=set(re.findall(r'[a-z]{3,}',x['selected_sentence'].lower()))
        sim=False
        for prev in byoldsrc[source_key(x['source_url'])]:
            ow=set(re.findall(r'[a-z]{3,}',prev['title'].lower()))
            if ow and len(words&ow)/len(words|ow)>.62:sim=True;break
        if sim:audit.append(dict(candidate_id=x['candidate_id'],decision='excluded',reason='near-duplicate of legacy question in same source'));continue
        seen_papers.add(sk);seen_questions.add(q);selected.append(x)
        if len(selected)>=TARGET:break
    cards=[]
    for o in old:
        refs=[dict(id='primary',title=o.get('source_title') or o.get('source_collection') or o['title'],authors=o.get('authors',''),year=year(o.get('source_year')),url=o['source_url'],pdf_url=o.get('pdf_url',''),locator=o.get('source_locator',''))]
        a=o['area'];why=criterion(o['title']) or 'decision'
        cards.append(dict(id=o['id'],title=o['title'],area=a,year=year(o.get('source_year')),is_new=False,evidence='index',status='uncertain',formal=o.get('question_excerpt') or o['title'],context=AREAS[a][1],why='The significance of this particular question has not yet been individually assessed. '+CRITERIA[why]['why'],status_note='Imported from the previous catalogue. Current open status has not been established by a new review.',progress=[],references=refs,related=[],criterion=why,criterion_label=CRITERIA[why]['label'],review_note='Legacy index record, not a completed research card. Model definitions, a self-contained statement, and a progress review remain to be written.',rank=10+(year(o.get('source_year')) or 1900)/100,legacy=o))
    for x in selected:
        a=x['area'];id=identifier('source:'+x['candidate_id']);s=x['selected_sentence'];short=len(s.split())<=25
        incomplete=not short or x.get('needs_context',False)
        refs=[dict(id='primary',title=x['paper_title'],authors=author(x.get('authors','')),year=x['year'],url=x['source_url'],pdf_url=x['pdf_url'],locator=x['source_locator'])]
        formal=('A short source quotation appears below. ' if not incomplete else 'This record locates a question in the source; a complete self-contained statement has not yet been written. ')
        formal+=('The model definitions are on the linked page of the paper.' if short else 'The quotation is truncated. Missing quantifiers and parameters must be read in the linked original.')
        c=dict(id=id,title=x['paper_title']+' — '+x['source_locator'],area=a,year=x['year'],is_new=True,evidence='source',status='uncertain' if 'introductory_claim_requires_review' in x.get('flags',[]) else 'source_open',formal=formal,source_formulation=dict(text=quoted(s),caption=('Complete selected source sentence' if short else 'Truncated source excerpt (at most 25 words)')+f'; PDF p. {x["page"]}',citation='primary'),context=AREAS[a][1]+f'\n\nSource of the specific model: {x["paper_title"]} ({x["venue"]}, {x["year"]}). Question location: {x["source_locator"]}.',why=CRITERIA[x['criterion']]['why'],status_note=f'Question recorded in a source from {x["year"]}; subsequent results and present open status have not been individually checked.',progress=[dict(date=str(x['year']),text='The source contains an explicitly unresolved question or conjecture. This entry dates the formulation; it is not a newly verified upper or lower bound.',citation='primary')],references=refs,related=[],criterion=x['criterion'],criterion_label=CRITERIA[x['criterion']]['label'],review_note='Source note, not a completed research review. Topic and selection criterion are heuristic. An individual model explanation, problem-specific importance assessment, and review of later results remain to be completed.',rank=100+x['score'],candidate_id=x['candidate_id'],source_excerpt_complete=short,model_self_contained=False,classification_method='heuristic',importance_method='structural_keyword_screen',requires_context=bool(incomplete),source_file=str(Path(x['source_file']).relative_to(BASE.parent)) if x.get('source_file') and str(x['source_file']).startswith(str(BASE.parent)) else '')
        cards.append(c);audit.append(dict(candidate_id=x['candidate_id'],decision='source_card',id=id,area=a,criterion=x['criterion'],excerpt_complete=short))
    byid={x['id']:i for i,x in enumerate(cards)}
    for x in reviewed:
        id=x.get('existing_id') or identifier('reviewed:'+x['key']);x.update(id=id,is_new=not bool(x.get('existing_id')),criterion_label=CRITERIA[x['criterion']]['label'],related=[],model_self_contained=True,classification_method='individual_review',importance_method='individual_review')
        if id in byid:cards[byid[id]]=x
        else:cards.append(x)
    registry_path.write_text(json.dumps(registry,ensure_ascii=False,indent=2))
    counts=collections.Counter(x['area'] for x in cards);news=collections.Counter(x['area'] for x in cards if x['is_new']);levels=collections.Counter(x['evidence'] for x in cards)
    areas=[dict(area=a,label=AREAS[a][0],count=counts[a],added=news[a],before=oldcounts[a],conference_count=confcounts[a],before_pct=100*oldcounts[a]/len(old),after_pct=100*counts[a]/len(cards),conference_pct=100*confcounts[a]/len(conference),initial_deficit_pp=100*deficit[a]) for a in AREAS]
    areas.sort(key=lambda a:(-a['count'],a['label']))
    meta=dict(built=DATE,total=len(cards),added=sum(x['is_new'] for x in cards),baseline=len(old),evidence_counts=dict(levels),status_scope='No claim of exhaustive open-status verification',methodology=[
        'Detailed cards have individually written statements, context, significance, and documented results. Source notes are unfinished research records and do not yet meet that standard. The legacy index is retained for traceability.',
        'Open in the source means open at the date of that source. The build date, 10 September 2026, does not establish current open status. Old excerpts may omit conditions or subsequent results.',
        'New searches prioritize areas underrepresented relative to the last five completed STOC and FOCS editions. Conference shares guide collection; paper counts and open-problem counts are different quantities.',
        'Selection considers model power, necessary resources, sharp bounds, structural characterizations, explicit constructions, and minimal assumptions. Source notes use a heuristic screen; detailed cards give an individual explanation.',
        'Automatic selection allows at most one new card per paper title and rejects identical formulations and close duplicates within a source. Collection-wide semantic deduplication remains incomplete.',
        'Short quotations retain the source language. Later related literature, where listed, is a research aid rather than evidence of resolution. Personal notes and saved cards are stored locally in your browser.'
    ])
    out=dict(meta=meta,areas=areas,criteria={k:dict(label=v['label']) for k,v in CRITERIA.items()},cards=cards)
    (BASE/'research/selected_internal.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2))
    (BASE/'research/selection_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
    (BASE/'site/catalog.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    # JS wrapper intentionally supports file://, without fetch or a backend.
    (BASE/'site/data.js').write_text('window.TCS_ATLAS='+json.dumps(out,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+';\n')
    write_csv(BASE/'site/catalog.csv',[dict(**{k:x.get(k,'') for k in ['id','title','area','year','is_new','evidence','status','formal','context','why','status_note','criterion']},question_excerpt=x.get('source_formulation',{}).get('text',''),references=' | '.join(r['url'] for r in x['references']),progress=' | '.join(p['date']+': '+p['text'] for p in x['progress'])) for x in cards],['id','title','area','year','is_new','evidence','status','formal','question_excerpt','context','why','status_note','criterion','progress','references'])
    sources={source_key(r['url']):r for x in cards for r in x['references']}
    write_csv(BASE/'site/sources.csv',sources.values(),['title','authors','year','url','pdf_url','locator'])
    write_csv(BASE/'site/areas.csv',areas,['area','label','before','added','count','before_pct','after_pct','conference_count','conference_pct','initial_deficit_pp'])
    (BASE/'site/coverage.json').write_text(json.dumps(dict(meta=meta,areas=areas,sources=len(sources),candidate_pool=len(candidates),downloaded_new_papers=len(list((BASE/'papers').glob('*.json')))),ensure_ascii=False,indent=2))
    print(json.dumps(dict(meta=meta,sources=len(sources),candidates=len(candidates),selected=len(selected)),ensure_ascii=False,indent=2))
    if list((BASE/'cards').glob('*.json')):
        from publish import publish
        publish()

if __name__=='__main__':main()
