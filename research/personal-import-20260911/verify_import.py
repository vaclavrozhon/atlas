"""Read-only integrity audit of the personal import and its published cards."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
sys.path.insert(0,str(ROOT/'scripts'))
from card_schema import canonical_record

def read(path):
    return json.loads((ROOT/path).read_text())

payload=json.loads((B/'additions.json').read_text())
registry=read('data/id_registry.json')
deleted=read('data/deleted_records.json')
audit=json.loads((B/'dispositions.json').read_text())
pre=json.loads((B/'pre-import.json').read_text())['sha256']
ids=[]
mismatches=[]
missing_related=[]
for card in payload:
    identifier=registry['reviewed:'+card['key']]
    ids.append(identifier)
    actual=read(f'data/cards/{identifier}.json')
    expected=canonical_record(dict(card,id=identifier))
    for key,value in expected.items():
        if actual.get(key)!=value:
            mismatches.append([identifier,key])
    for related in card.get('related',[]):
        if not (ROOT/'data/cards'/f'{related}.json').exists():
            missing_related.append([identifier,related])
assert not mismatches,mismatches
assert not missing_related,missing_related
assert len(ids)==len(set(ids))==53
assert not set(ids)&set(deleted)
assert len(audit['dispositions'])==len({r['candidate'] for r in audit['dispositions']})==200
assert audit['counts']['added']==53

current={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'data/cards').glob('*.json')}
removed=[p for p in pre if p.startswith('data/cards/') and p not in current]
modified=[p for p in pre if p.startswith('data/cards/') and p in current and pre[p]!=current[p]]
other_new=[p for p in current if p not in pre and Path(p).stem not in ids]
for path in removed:
    assert Path(path).stem in deleted,path

catalog=read('build/catalog.json')
published={c['id']:c for c in catalog['cards']}
assert set(ids)<=set(published),'Missing imported cards in publication'
for identifier in ids:
    assert published[identifier]['formal']==read(f'data/cards/{identifier}.json')['formal']
    assert published[identifier]['references']==read(f'data/cards/{identifier}.json')['references']

result={
    'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'input_proposals':200,'counts':audit['counts'],'new_evidence':audit['new_evidence'],
    'imported_ids':ids,'payload_matches_canonical':True,'all_new_ids_published':True,
    'published_statements_and_references_match':True,'no_deleted_identity_imported':True,
    'own_edits':'53 new canonical cards and their new stable source-key mappings; one reference corrected on an own new card. No pre-existing card edits.',
    'commands':{
        'make publish':{'exit_code':0,'result':'reader and exports rebuilt'},
        'make check':{'exit_code':0,'result':'offline schema, categories, ranking, publication, deletion protection, import and isolated deployment checks passed'}
    },
    'concurrent_changes_since_pre_import':{'removed_cards':removed,'modified_cards':modified,'other_added_cards':other_new},
    'selection_sha256_unchanged_since_pre_import':hashlib.sha256((ROOT/'data/benchmark_selection.json').read_bytes()).hexdigest()==pre['data/benchmark_selection.json'],
    'deleted_registry_sha256_unchanged_since_pre_import':hashlib.sha256((ROOT/'data/deleted_records.json').read_bytes()).hexdigest()==pre['data/deleted_records.json'],
    'limits':[
        'Source and status review is bounded, not exhaustive mathematical verification.',
        '25 admitted source drafts have explicit remaining formulation issues.',
        'Other user-authorized repository edits occurred concurrently; differences listed above are not attributed to this import.'
    ]
}
(B/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'new':len(ids),'published':len(published),'counts':audit['counts'],'concurrent_removed':len(removed),'concurrent_modified':len(modified),'concurrent_added':len(other_new),'checks':'passed'}))
