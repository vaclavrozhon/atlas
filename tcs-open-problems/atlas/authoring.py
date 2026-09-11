"""Small authoring helpers; finished English cards remain plain JSON in cards/."""
import json
from pathlib import Path
from publish import publish

def ref(id,title,authors,year,url,locator=''):
    return dict(id=id,title=title,authors=authors,year=year,url=url,locator=locator)
def step(date,text,citation):return dict(date=date,text=text,citation=citation)
def paragraph(text,citation=None):return dict(text=text,**({'citation':citation} if citation else {}))
def dispose(id, *, kind, reason, formal, context, why, progress, references, duplicate_of=None):
    """Publish one individually justified non-question disposition, keeping its ID."""
    base=Path(__file__).parent
    catalogue=json.loads((base/'site/catalog.json').read_text())
    old=next(c for c in catalogue['cards'] if c['id']==id)
    if old['evidence']=='reviewed':raise ValueError('Use an explicit reviewed-card revision')
    if not all([kind,reason,formal,context,why,progress,references]):raise ValueError('Incomplete disposition')
    refs={r['id'] for r in references}
    if any(p['citation'] not in refs for p in progress):raise ValueError('Unknown disposition citation')
    if duplicate_of is not None:
        target=next((c for c in catalogue['cards'] if c['id']==duplicate_of),None)
        if duplicate_of==id or not target or target['evidence']!='reviewed':
            raise ValueError('Duplicate disposition needs a different completed canonical card')
    path=base/'record_corrections.json';patches=json.loads(path.read_text())
    patches[id]={**patches.get(id,{}),**dict(status='excluded',formal=formal,context=context,why=why,
        status_note=reason,progress=progress,references=references,
        review_note='Individually reviewed on 10 September 2026. This is a completed editorial disposition; the original ID and primary bibliography are retained.',
        review_outcome=dict(complete=True,kind=kind,reason=reason,reviewed_on='2026-09-10',citations=sorted(refs)))}
    if duplicate_of is not None:
        patches[id]['review_outcome']['duplicate_of']=duplicate_of
    path.write_text(json.dumps(patches,ensure_ascii=False,indent=2))
    path=base/'importance_overrides.json';overrides=json.loads(path.read_text())
    overrides[id]=dict(score=0,method='editorial',assessed_on='2026-09-10',reason='Retired from open-problem selection. '+reason)
    path.write_text(json.dumps(overrides,ensure_ascii=False,indent=2))
    publish()
def finish(key,**c):
    c['key']=key
    if isinstance(c['context'],list):
        c['context_blocks']=c['context'];c['context']='\n\n'.join(b['text'] for b in c['context_blocks'])
    path=Path(__file__).parent/'cards'/(key+'.json')
    if path.exists():
        old=json.loads(path.read_text())
        for k in ['id','rank','published_at','updated_at','is_new']: 
            if k in old:c.setdefault(k,old[k])
    path.write_text(json.dumps(c,ensure_ascii=False,indent=2))
    publish()
