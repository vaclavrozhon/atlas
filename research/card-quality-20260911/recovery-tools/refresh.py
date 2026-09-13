"""Refresh review bookkeeping from canonical cards; preserve individual triage."""
import collections
import json
import re
import sys
from pathlib import Path

BASE=Path('/home/vasek/atlas')
DIRECTORY=BASE/'research/card-quality-20260911'
sys.path.insert(0,str(BASE/'scripts'))
from publish import load_catalog
from taxonomy import apply_taxonomy
from importance import apply_importance
from benchmark_selection import members

def refresh():
    data=load_catalog()
    apply_taxonomy(data)
    apply_importance(data)
    top100={c['id'] for c in members(data,'top100')}
    path=DIRECTORY/'queue.json'
    queue=json.loads(path.read_text())
    previous={r['id']:r for r in queue['records']}
    records=[]
    for c in data['cards']:
        if c['status'] in {'resolved','excluded'}:
            continue
        row=previous.get(c['id'],dict(id=c['id'],state='pending'))
        row.update(title=c['title'],area=c['area'],importance=c['importance']['score'],top100=c['id'] in top100,
                   position=c['importance_rank'],card=f"data/cards/{c['id']}.json")
        review=c.get('quality_review',{})
        if review.get('reference_card')=='TCS-0001':
            row.update(state=review['state'],reviewed_on=review['reviewed_on'],
                       notes=review['changes'],checked_sources=review['checked_sources'])
        records.append(row)
    old_order={r['id']:i for i,r in enumerate(queue['records'])}
    records.sort(key=lambda r:old_order.get(r['id'],len(old_order)))
    queue['records']=records
    queue['counts']=dict(collections.Counter(r['state']for r in records))
    for state in ['revised','skipped_reasonable','improved_unfinished','pending']:
        queue['counts'].setdefault(state,0)
    queue['top100_counts']=dict(collections.Counter(r['state']for r in records if r.get('top100')))
    marker=BASE/'build/version.json'
    if marker.exists():queue['catalogue_version']=json.loads(marker.read_text())['version']
    queue['last_continued_on']='2026-09-12'
    path.write_text(json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
    readme=DIRECTORY/'README.md'
    text=readme.read_text()
    for key,count in queue['counts'].items():
        text=re.sub(rf'^- {key}: \d+$',f'- {key}: {count}',text,flags=re.M)
    readme.write_text(text)
    print(json.dumps(queue['counts']))

if __name__=='__main__':refresh()
