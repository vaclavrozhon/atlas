"""Apply the approved author list using current locked canonical records."""
import datetime
import fcntl
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'scripts'))
from import_cards import import_cards
from archive_cards import change_activity
from card_schema import canonical_record, reader_record
from catalog_exports import atomic
from publish import validate_record

plan = json.loads((HERE/'import-plan.json').read_text())
before = json.loads((HERE/'before.json').read_text())
batch = plan['batch']
criteria = json.loads((ROOT/'data/criteria.json').read_text())

def validate_existing_patch(row):
    path = ROOT/'data/cards'/f'{row["existing_id"]}.json'
    latest = json.loads(path.read_text())
    base = before[row['existing_id']]
    for key,value in row['patch'].items():
        if latest.get(key) != base.get(key) and latest.get(key) != value:
            raise ValueError(f'{path.name}: concurrent change to {key}; reconcile before applying')
    updated = dict(latest)
    if row['patch'] and not any(h.get('batch')==batch for h in latest.get('formulation_history',[])):
        previous = {key:latest[key] for key in ['title','formal','definitions','question_type','answer_criterion','references','progress','evidence','status','status_note'] if key in latest}
        updated['formulation_history'] = list(latest.get('formulation_history',[])) + [dict(batch=batch,changed_on='2026-09-13',previous=previous,
            reason='User-approved author-list import: individual formulation development or explicit broadening, with the previous statement preserved.')]
    updated.update(row['patch'])
    if row['patch'].get('context_blocks'):
        updated.pop('context',None)
    imports = list(latest.get('author_problem_imports',[]))
    imports = [entry for entry in imports if entry.get('batch')!=batch]
    updated['author_problem_imports'] = imports + [row['association']]
    updated['updated_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    updated = canonical_record(updated)
    validate_record(reader_record(updated,criteria),path,criteria)
    return path,updated

# Check for changed mathematical fields before allocating any new identities.
with (ROOT/'.publish.lock').open('a') as lock:
    fcntl.flock(lock,fcntl.LOCK_EX)
    for row in plan['plans']:
        if 'existing_id' in row:
            validate_existing_patch(row)

new_result = import_cards([row['new_card'] for row in plan['plans'] if 'new_card' in row])
mapping = {}
with (ROOT/'.publish.lock').open('a') as lock:
    fcntl.flock(lock,fcntl.LOCK_EX)
    registry = json.loads((ROOT/'data/id_registry.json').read_text())
    pending = []
    for row in plan['plans']:
        if 'existing_id' in row:
            pending.append(validate_existing_patch(row))
            mapping[row['proposal_id']] = row['existing_id']
        else:
            mapping[row['proposal_id']] = registry['reviewed:'+row['new_card']['key']]
    for path,card in pending:
        atomic(path,json.dumps(card,ensure_ascii=False,indent=2)+'\n')

# Links record structural connections between questions, not mere shared authors.
edges = [
 ('P01','P02'), ('P01','P04'), ('P01','P31'),
 ('P03','P25'), ('P03','P31'), ('P09','P10'), ('P10','P21'),
 ('P11','P19'), ('P17','P23'), ('P18','P19'), ('P25','P27'),
]
with (ROOT/'.publish.lock').open('a') as lock:
    fcntl.flock(lock,fcntl.LOCK_EX)
    pending = {}
    for a,b in edges:
        # The publisher supplies the reverse relation without source duplication.
        identifier,target = mapping[a],mapping[b]
        path = ROOT/'data/cards'/f'{identifier}.json'
        card = pending.setdefault(path,json.loads(path.read_text()))
        links = card.setdefault('related_problem_ids',[])
        if target not in links:
            links.append(target)
    ted_path = ROOT/'data/cards'/f'{mapping["P30"]}.json'
    ted = pending.setdefault(ted_path,json.loads(ted_path.read_text()))
    if (ROOT/'data/cards/TCS-7179.json').exists() and 'TCS-7179' not in ted['related_problem_ids']:
        ted['related_problem_ids'].append('TCS-7179')
    for path,card in pending.items():
        validate_record(reader_record(card,criteria),path,criteria)
        atomic(path,json.dumps(canonical_record(card),ensure_ascii=False,indent=2)+'\n')

reason = (f'The user approved replacing the resolved first-truly-subcubic unweighted tree-edit-distance question with the almost-quadratic target in {mapping["P30"]}. '
          'The ICALP 2026 primary source https://arxiv.org/abs/2605.07150v2 records and derandomizes already subcubic bounds. '
          'The complete historical card is preserved; this is not an editorial removal for low importance.')
archive_result = change_activity(['TCS-5851'],reason=reason)
assignments = [dict(researcher=name,proposals=ps,card_ids=[mapping[p] for p in ps]) for name,ps in plan['assignments']]
result = dict(batch=batch,proposal_to_card=mapping,new_import=new_result,
              existing_updated=[row['existing_id'] for row in plan['plans'] if 'existing_id' in row],
              archive=archive_result,assignments=assignments,
              mathematical_updates=[row['existing_id'] for row in plan['plans'] if row.get('patch') and row['proposal_id']!='P09'])
(HERE/'import-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(new=len(new_result['imported']),existing=len(result['existing_updated']),archived=archive_result,unique=len(mapping),assignments=sum(len(a['card_ids']) for a in assignments))))
