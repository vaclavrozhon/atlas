"""Import completeness, review preservation, and publication isolation checks."""
import copy
import csv
import gzip
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from source_imports import read_imports, seed_imports, annotate_imports
from taxonomy import editorial_card

research = BASE / 'research/import-source-problems-20260910'
original = json.loads((research / 'source-library-input.json').read_text())
baseline = json.loads(gzip.decompress((research / 'baseline-catalog.json.gz').read_bytes()))
data = json.loads((BASE / 'site/catalog.json').read_text())
registry = json.loads((BASE / 'id_registry.json').read_text())
batches = read_imports()
report = json.loads((BASE / 'site/textbook-additions.json').read_text())
cards = {c['id']: c for c in data['cards']}
entries = {e['entry_key']: e for e in report['entries']}
assert len(cards) == len(data['cards'])
assert len(entries) == 555 and report['meta']['new_cards'] == 472
assert report['meta']['existing_cards'] == 75
assert report['meta']['annotated_cards'] == 547
assert set(c['id'] for c in baseline['cards']) <= set(cards)
assert sum(len(s['problems']) for s in original['sources']) == len(entries)
for source in original['sources']:
    for entry in source['problems']:
        result = entries[entry['entry_key']]
        assert result['summary'] == entry['summary']
        for identifier in result['card_ids']:
            note = next(n for n in cards[identifier]['textbook_notes'] if n['key'].endswith(':' + entry['entry_key']))
            assert note['summary'] == entry['summary']
            assert note['kind'] == entry['kind']
            assert note['reference']['url'] == source['source_url']
            assert note['reference']['pdf_url'] == entry['source_pdf_url']
            assert note['caution'] == source['caution']
            assert note['reference']['year'] == source['year']
            if result['disposition'] == 'new_draft' and cards[identifier]['evidence'] != 'reviewed':
                assert cards[identifier]['evidence'] == 'source'
                assert cards[identifier]['model_self_contained'] is False
                assert cards[identifier]['importance']['method'] == 'unassessed'
                assert cards[identifier]['importance']['score'] == 50

# Re-import does not change IDs, source notes, or existing reviewed card content.
working = copy.deepcopy(data)
registry_before = copy.deepcopy(registry)
seed_imports(working, registry, 'later-publication', batches)
assert annotate_imports(working, registry, batches) == report
assert working == data and registry == registry_before

# A subsequent canonical review replaces a draft, but its dated annotations
# return without overriding the newer resolution or personal-note identity.
identifier = next(e['card_ids'][0] for e in report['entries'] if e['disposition']=='new_draft')
replacement = next(c for c in working['cards'] if c['id']==identifier)
expected_notes = replacement.pop('textbook_notes')
replacement.update(evidence='reviewed', status='resolved', formal='Later reviewed statement',
                   review_note='Later reviewed resolution', model_self_contained=True)
expected_review = copy.deepcopy(replacement)
seed_imports(working, registry, 'still-later', batches)
annotate_imports(working, registry, batches)
assert replacement['textbook_notes'] == expected_notes
assert {k:v for k,v in replacement.items() if k!='textbook_notes'} == expected_review
assert 'textbook_notes' not in editorial_card(replacement)

site = BASE / 'site'
assert not (site/'library').exists()
assert not list(site.rglob('*.pdf'))
for path in site.rglob('*'):
    assert path.resolve().is_relative_to(site.resolve()), 'Symlink escapes document root'
for name in ['catalog.json','data.js','updates.json','updates-delta.json','textbook-additions.json','textbook-additions.csv']:
    text = (site/name).read_text()
    for forbidden in ['local_pdf_url', 'tcs-source-library', 'library/summary.js', 'library/open-problems', 'file:///']:
        assert forbidden not in text, (name, forbidden)
assert 'source_library' not in (BASE/'publish.py').read_text()
csv_cards = {c['id']:c for c in csv.DictReader((site/'catalog.csv').open(encoding='utf-8-sig'))}
for identifier, card in cards.items():
    assert json.loads(csv_cards[identifier]['textbook_notes']) == card.get('textbook_notes',[])
print(json.dumps(dict(**report['meta'], checks=['all 555 source entries retained', 'dated caveats and external citations', 'existing IDs preserved', 'repeat-import idempotence', 'later review survives re-import', 'JSON and CSV annotations agree', 'no library or PDF in document root'])))
