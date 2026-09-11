"""Publish individually completed cards atomically to the local reader.

The full legacy collection is left intact. cards/*.json is the canonical English
editorial layer. version.json is committed last, so a reader never sees a partial
publication. No external service is involved.
"""
import argparse,collections,csv,datetime,fcntl,hashlib,io,json,re
from pathlib import Path
from taxonomy import apply_taxonomy, editorial_card, LEGACY_AREAS
from importance import apply_importance, validate_importance, ranking_exports
from proposals import apply_proposals
from source_imports import read_imports, seed_imports, annotate_imports
BASE=Path(__file__).resolve().parent
SITE=BASE/'site'
CARDS=BASE/'cards'
def atomic(path,text):
    tmp=path.with_name(path.name+'.publishing');tmp.write_text(text,encoding='utf8');tmp.replace(path)
def jsdump(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def csvtext(rows,fields):
    f=io.StringIO();f.write('\ufeff');w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows);return f.getvalue()
def publish():
    # Multiple research sessions can publish to the same local atlas.
    with (BASE/'.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        return _publish()

def _publish():
    CARDS.mkdir(exist_ok=True)
    data=json.loads((SITE/'catalog.json').read_text())
    previous_version=data['meta'].get('version','')
    previous_cards={c['id']:jsdump(c) for c in data['cards']}
    # Bootstrap the existing, English demo cards exactly once.
    if not list(CARDS.glob('*.json')):
        for c in data['cards']:
            if c['evidence']=='reviewed':atomic(CARDS/(c['id']+'.json'),json.dumps(c,ensure_ascii=False,indent=2))
    registry_path=BASE/'id_registry.json';registry=json.loads(registry_path.read_text())
    now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    apply_proposals(data, registry, now)
    question_imports = read_imports()
    seed_imports(data, registry, now, question_imports)
    maximum=max(int(x.split('-')[-1]) for x in list(registry.values())+[c['id'] for c in data['cards']])
    index={c['id']:i for i,c in enumerate(data['cards'])};authored=[];seen=set();changed=[]
    for f in sorted(CARDS.glob('*.json')):
        c=json.loads(f.read_text())
        for field in ['title','area','formal','context','why','progress','references','criterion','question_type','answer_criterion']:
            if not c.get(field):raise ValueError(f'{f.name}: missing {field}')
        if c['question_type'] not in {'yes_no','asymptotic_complexity','exact_value'}:raise ValueError(f'{f.name}: unsupported question type; see EDITORIAL_STANDARD.md')
        if not isinstance(c['answer_criterion'],str):raise ValueError(f'{f.name}: answer criterion must be text')
        if c['area'] not in LEGACY_AREAS:raise ValueError('Unknown area '+c['area'])
        if c['criterion'] not in data['criteria']:raise ValueError('Unknown criterion')
        validate_importance(c.get('importance'))
        if not c.get('id'):
            key='reviewed:'+c.get('key',f.stem)
            if key not in registry:maximum+=1;registry[key]=f'TCS-{maximum:04d}'
            c['id']=registry[key]
        id=c['id']
        if not re.fullmatch(r'TCS-\d{4,}',id) or id in seen:raise ValueError('Invalid/duplicate card ID '+id)
        seen.add(id)
        refs={r['id'] for r in c['references']}
        for r in c['references']:
            if not r.get('title') or not r.get('url','').startswith(('https://','http://')):raise ValueError('Invalid reference')
        for p in c['progress']:
            if p['citation'] not in refs:raise ValueError('Unknown progress citation')
        for b in c.get('context_blocks',[]):
            if b.get('citation') and b['citation'] not in refs:raise ValueError('Unknown context citation')
        if c.get('context_blocks') and c['context']!='\n\n'.join(b['text'] for b in c['context_blocks']):raise ValueError('Context paragraphs and search text differ')
        previous=editorial_card(data['cards'][index[id]]) if id in index else None
        c.setdefault('year',max(r['year'] for r in c['references'] if r.get('year')))
        c.setdefault('is_new',previous['is_new'] if previous else True)
        c.setdefault('status','source_open')
        c.setdefault('status_note','Checked through 10 September 2026; the dated results and remaining gap are stated below.')
        c.setdefault('review_note','Individually written from the cited primary sources. The importance assessment is editorial. New preprint proofs have not been independently verified.')
        c.setdefault('reviewed_on','2026-09-10')
        c.setdefault('published_at',now)
        c.setdefault('rank',20000+datetime.datetime.now(datetime.timezone.utc).timestamp())
        c.update(evidence='reviewed',criterion_label=data['criteria'][c['criterion']]['label'],classification_method='individual_review',importance_method='individual_review')
        c.setdefault('model_self_contained',True);c.setdefault('related',[])
        # Preserve bibliographic traceability when upgrading an existing note.
        if previous and previous['evidence']!='reviewed':
            c.setdefault('upgraded_from',dict(evidence=previous['evidence'],title=previous['title'],references=previous['references']))
        same=previous and jsdump(previous)==jsdump(c)
        if not same:
            c['updated_at']=now;changed.append(id)
        atomic(f,json.dumps(c,ensure_ascii=False,indent=2))
        if id in index:data['cards'][index[id]]=c
        else:index[id]=len(data['cards']);data['cards'].append(c)
        authored.append(c)
    # Dated corrections to unfinished records survive rebuilds without promoting
    # those records to the individually authored tier. Reviewed cards take priority.
    corrections_path=BASE/'record_corrections.json'
    corrections=json.loads(corrections_path.read_text()) if corrections_path.exists() else {}
    for id,patch in corrections.items():
        if id not in index:raise ValueError('Correction targets unknown record '+id)
        previous=data['cards'][index[id]]
        if previous['evidence']=='reviewed':continue
        if any(k in patch for k in ['id','evidence','is_new','legacy','candidate_id']):raise ValueError('Correction may not replace record identity or review level')
        c={**previous,**patch}
        if 'area' in patch:c['original_area']=patch['area']
        if jsdump(editorial_card(c))!=jsdump(editorial_card(previous)):c['updated_at']=now;changed.append(id)
        data['cards'][index[id]]=c;authored.append(c)
    textbook_report = annotate_imports(data, registry, question_imports)
    apply_taxonomy(data)
    apply_importance(data)
    changed=[c['id'] for c in data['cards'] if previous_cards.get(c['id'])!=jsdump(c)]
    levels=collections.Counter(c['evidence'] for c in data['cards'])
    data['meta'].update(total=len(data['cards']),added=sum(c['is_new'] for c in data['cards']),evidence_counts=dict(levels),updated_at=now)
    completed=sum(c['evidence']=='reviewed' or c.get('review_outcome',{}).get('complete',False) for c in data['cards'])
    data['meta'].update(completed_reviews=completed,remaining_reviews=len(data['cards'])-completed)
    version=hashlib.sha256(jsdump(dict(cards=data['cards'],areas=data['areas'],taxonomy=data['meta']['taxonomy'])).encode()).hexdigest()[:20]
    data['meta']['version']=version
    atomic(registry_path,json.dumps(registry,ensure_ascii=False,indent=2))
    atomic(SITE/'catalog.json',json.dumps(data,ensure_ascii=False,indent=2))
    atomic(SITE/'data.js','window.TCS_ATLAS='+jsdump(data).replace('</','<\\/')+';\n')
    fields=['id','title','area','original_area','selection_group','selection_target','scope_exclusion_reason','scope_exclusion_kind','preliminary_category','preliminary_duplicate_of','importance_rank','importance_count','importance_score','importance_method','importance_reason','year','is_new','evidence','status','question_type','formal','question_excerpt','definitions','answer_criterion','context','why','status_note','criterion','progress','references','textbook_notes']
    rows=[dict(**{k:c.get(k,'') for k in fields if k not in ['progress','references','question_excerpt']},question_excerpt=c.get('source_formulation',{}).get('text',''),progress=' | '.join(p['date']+': '+p['text'] for p in c['progress']),references=' | '.join(r['url'] for r in c['references'])) for c in data['cards']]
    for row,c in zip(rows,data['cards']):
        row.update(scope_exclusion_reason=c.get('scope_exclusion',{}).get('reason',''),scope_exclusion_kind=c.get('scope_exclusion',{}).get('kind','subject' if c.get('scope_exclusion') else ''),preliminary_category=c.get('scope_exclusion',{}).get('previous_area',''),preliminary_duplicate_of=c.get('scope_exclusion',{}).get('duplicate_of',''),importance_score=c['importance']['score'],importance_method=c['importance']['method'],importance_reason=c['importance']['reason'])
        row['textbook_notes']=jsdump(c.get('textbook_notes',[]))
    atomic(SITE/'catalog.csv',csvtext(rows,fields))
    atomic(SITE/'scope-excluded.json',json.dumps([c for c in data['cards'] if c.get('scope_exclusion')],ensure_ascii=False,indent=2))
    ranking, overview = ranking_exports(data)
    atomic(SITE/'importance-ranking.csv',csvtext(ranking,['area','position','id','title','score','assessment','status','reason']))
    atomic(SITE/'importance-overview.md',overview)
    sources={r['url']:r for c in data['cards'] for r in c['references']+[n['reference'] for n in c.get('textbook_notes',[])]}
    atomic(SITE/'sources.csv',csvtext(sources.values(),['title','authors','year','url','pdf_url','locator']))
    atomic(SITE/'textbook-additions.json',json.dumps(textbook_report,ensure_ascii=False,indent=2))
    atomic(SITE/'textbook-additions.csv',csvtext([{**e,'card_ids':' | '.join(e['card_ids'])} for e in textbook_report['entries']],['entry_key','card_ids','disposition','kind','summary','source','year','locator','url','pdf_url']))
    atomic(SITE/'areas.csv',csvtext(data['areas'],['area','label','group','position','target','count','reviewed','importance_assessed','importance_provisional','before','added','after_pct']))
    coverage=json.loads((SITE/'coverage.json').read_text());coverage.update(meta=data['meta'],areas=data['areas'],sources=len(sources));atomic(SITE/'coverage.json',json.dumps(coverage,ensure_ascii=False,indent=2))
    summary = ['# Current category sizes', '', 'Counts are saved candidate records, not verified distinct open problems.', '', '| Group | Category | Target | Candidates |', '| --- | --- | ---: | ---: |']
    summary.extend(f"| {a['group']} {a['position']} | {a['area']} | {a['target']} | {a['count']} |" for a in data['areas'])
    taxonomy=data['meta']['taxonomy']
    summary.extend(['',f"Candidate pool: {taxonomy['candidate_count']}. Archived: {taxonomy['scope_excluded_count']} ({taxonomy['preliminary_removal_count']} preliminary removals; {taxonomy['subject_exclusion_count']} subject exclusions). Total saved: {len(data['cards'])}.",'', f"Named targets total {taxonomy['assigned_target']}; reserved places: {taxonomy['reserved_target']}. Preliminary importance pruning is recorded in the manifests under to_delete/. Final quota selection and a comprehensive deduplication audit remain pending."])
    atomic(SITE/'category-sizes.md','\n'.join(summary)+'\n')
    readme_path=SITE/'README.md'
    if readme_path.exists():
        readme=readme_path.read_text()
        large_count=sum(a['count'] for a in data['areas'] if a['group']=='large')
        small_count=sum(a['count'] for a in data['areas'] if a['group']=='small')
        readme=re.sub(r'^Selection inventory:.*$',
                      f'Selection inventory: {large_count:,} large-category and {small_count:,} small-category candidates; '
                      f'{taxonomy["scope_excluded_count"]:,} archived records; {len(data["cards"]):,} saved in total.',
                      readme,flags=re.MULTILINE)
        for level,label in [('reviewed','detailed research cards'),('source','source notes'),('index','legacy index entries')]:
            readme=re.sub(r'\*\*[\d,]+ '+label+r'\*\*',f'**{levels[level]:,} {label}**',readme)
        readme=re.sub(r'\*\*[\d,]+ legacy index records\*\*',f'**{levels["index"]:,} legacy index records**',readme)
        readme=re.sub(r'The [\d,]+ source notes and [\d,]+ index records appear as \*\*[\d,]+ short drafts\*\*\.',
                      f'The {levels["source"]:,} source notes and {levels["index"]:,} index records appear as **{levels["source"]+levels["index"]:,} short drafts**.',readme)
        readme=re.sub(r'There are [\d,]+ additions to the original [\d,]+-record index\.',
                      f'There are {data["meta"]["added"]:,} additions to the original {data["meta"]["baseline"]:,}-record index.',readme)
        readme=re.sub(r'\*\*[\d,]+ records\*\* in \*\*\d+ selection categories\*\*',f"**{len(data['cards']):,} records** in **{len(data['areas'])} selection categories**",readme)
        readme=re.sub(r'\nReview progress:.*\n','\n',readme)
        readme+=f'\nReview progress: {completed:,} completed reviews; {len(data["cards"])-completed:,} remaining. Completed reviews include {completed-levels["reviewed"]} individually justified dispositions.\n'
        atomic(readme_path,readme)
    # A complete snapshot also catches reclassification and publications missed
    # while a reader was offline; the client applies only actual differences.
    payload=dict(version=version,published_at=now,changed_ids=changed,cards=data['cards'],meta=data['meta'],areas=data['areas'])
    atomic(SITE/'updates.json',jsdump(payload))
    changed_set=set(changed)
    delta=dict(version=version,base_version=previous_version,published_at=now,
               changed_ids=changed,cards=[c for c in data['cards'] if c['id'] in changed_set],
               meta=data['meta'],areas=data['areas'])
    atomic(SITE/'updates-delta.json',jsdump(delta))
    atomic(SITE/'version.json',jsdump(dict(version=version,published_at=now,delta=True)))
    print(jsdump(dict(published=changed if len(changed)<50 else f'{len(changed)} records',total=len(data['cards']),detailed=levels['reviewed'],version=version)))
    return payload
if __name__=='__main__':publish()
