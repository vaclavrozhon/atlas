"""Read-only coverage audit of this explicitly approved import and archival move."""
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
result = json.loads((HERE/'import-result.json').read_text())
before = json.loads((HERE/'before.json').read_text())
registry = json.loads((ROOT/'data/id_registry.json').read_text())
catalog = json.loads((ROOT/'build/catalog.json').read_text())
published = {card['id']:card for card in catalog['cards']}
mapping = result['proposal_to_card']
assert len(mapping)==len(set(mapping.values()))==32
assert len(result['assignments'])==22
assert sum(len(a['card_ids']) for a in result['assignments'])==45
for a in result['assignments']:
    assert len(a['card_ids'])==(3 if a['researcher']=='Tomasz Kociumaka' else 2)
areas = collections.Counter()
developed = set(result['new_import']['imported']) | set(result['mathematical_updates'])
inherited_model_gaps = []
for pid,identifier in mapping.items():
    card = json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
    assert identifier in published
    assert card['evidence']=='reviewed'
    if identifier in developed:
        assert card['model_self_contained'], identifier
    else:
        assert card.get('model_self_contained') == before[identifier].get('model_self_contained'), identifier
    if not card.get('model_self_contained'):
        inherited_model_gaps.append(identifier)
    associations = [a for a in card['author_problem_imports'] if a['batch']==result['batch']]
    assert len(associations)==1 and associations[0]['proposal_id']==pid
    assert associations[0]['researchers']==[a['researcher'] for a in result['assignments'] if pid in a['proposals']]
    for field in ['formal','definitions','question_type','answer_criterion','references','author_problem_imports']:
        assert card.get(field)==published[identifier].get(field),(identifier,field)
    if identifier in result['new_import']['imported']:
        assert registry['reviewed:'+card['key']]==identifier
    areas[card['area']]+=1
assert not (ROOT/'data/cards/TCS-5851.json').exists()
assert 'TCS-5851' not in published
assert json.loads((ROOT/'data/archive/cards/TCS-5851.json').read_text())==before['TCS-5851']
print(json.dumps(dict(unique_topics=32,researchers=22,assignments=45,
    new_cards=len(result['new_import']['imported']),existing_cards=len(result['existing_updated']),
    archived=['TCS-5851'],archive_preserved=True,all_active_and_published=True,
    inherited_model_gaps=inherited_model_gaps,
    categories=dict(areas),publication_version=catalog.get('meta',{}).get('version')),indent=2))
