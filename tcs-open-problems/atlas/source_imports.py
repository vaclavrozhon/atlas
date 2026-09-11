"""Publish frozen question imports; never access the independent source library.

Seeds create stable IDs once. Bibliographic question notes are an overlay applied
after canonical card reviews, so an import cannot reset a later editorial review.
"""
import collections
import copy
import json
from pathlib import Path
from urllib.parse import urlsplit

from taxonomy import NAMES

IMPORTS = Path(__file__).with_name('imports')

def external_url(value):
    parsed = urlsplit(value)
    return parsed.scheme in {'http', 'https'} and bool(parsed.netloc)

def read_imports(directory=IMPORTS):
    batches = []
    keys = set()
    for path in sorted(directory.glob('*.json')):
        batch = json.loads(path.read_text())
        if not batch.get('approved_on') or not batch.get('approval_basis'):
            raise ValueError(f'{path}: missing import authorization')
        draft_keys = {c['key'] for c in batch['cards']}
        if len(draft_keys) != len(batch['cards']):
            raise ValueError(f'{path}: duplicate draft key')
        for card in batch['cards']:
            for field in ['title', 'formal', 'context', 'why', 'status_note', 'review_note', 'references', 'textbook_import']:
                if not card.get(field): raise ValueError(f'{path}: missing {field}')
            if card['area'] not in NAMES or card['textbook_import']['category'] != card['area']:
                raise ValueError(f'{path}: invalid source topic')
            if card['evidence'] != 'source' or card['model_self_contained'] is not False or card.get('importance'):
                raise ValueError(f'{path}: imports must be unassessed source drafts')
            if any(not r.get('title') or not external_url(r['url']) or not external_url(r['pdf_url']) for r in card['references']):
                raise ValueError(f'{path}: only external bibliographic references are allowed')
        for entry in batch['entries']:
            note, target = entry['note'], entry['target']
            if note['key'] in keys: raise ValueError(f'{path}: duplicate annotation key')
            keys.add(note['key'])
            if note['batch'] != batch['id'] or note['kind'] not in {'question', 'conjecture', 'research_direction'}:
                raise ValueError(f'{path}: invalid annotation')
            if not note['summary'] or not note['status_note']:
                raise ValueError(f'{path}: missing annotation content')
            ref = note['reference']
            if not ref.get('title') or not external_url(ref['url']) or not external_url(ref['pdf_url']):
                raise ValueError(f'{path}: invalid external annotation reference')
            if bool(target.get('existing_ids')) == bool(target.get('draft_key')):
                raise ValueError(f'{path}: an annotation needs exactly one target type')
            if target.get('draft_key') and target['draft_key'] not in draft_keys:
                raise ValueError(f'{path}: unknown new draft target')
        if {e['target'].get('draft_key') for e in batch['entries']} - {None} != draft_keys:
            raise ValueError(f'{path}: a draft lacks its source annotation')
        batches.append(batch)
    return batches

def seed_imports(data, registry, now, batches):
    existing = {c['id']: c for c in data['cards']}
    maximum = max(int(i.split('-')[-1]) for i in list(existing) + list(registry.values()))
    for batch in batches:
        for draft in batch['cards']:
            registry_key = 'source-import:' + draft['key']
            if draft['criterion'] not in data['criteria']:
                raise ValueError(f'{registry_key}: unknown selection criterion')
            if registry_key not in registry:
                maximum += 1
                registry[registry_key] = f'TCS-{maximum:04d}'
            identifier = registry[registry_key]
            if identifier in existing:
                continue
            card = copy.deepcopy(draft)
            card.update(id=identifier, is_new=True, published_at=now, updated_at=now,
                        rank=20000 + int(identifier.split('-')[-1]),
                        criterion_label=data['criteria'][card['criterion']]['label'])
            data['cards'].append(card)
            existing[identifier] = card

def annotate_imports(data, registry, batches):
    existing = {c['id']: c for c in data['cards']}
    notes = collections.defaultdict(list)
    report = []
    for batch in batches:
        for entry in batch['entries']:
            target = entry['target']
            ids = target.get('existing_ids') or [registry['source-import:' + target['draft_key']]]
            for identifier in ids:
                if identifier not in existing:
                    raise ValueError('Import targets an unknown card: ' + identifier)
                notes[identifier].append(copy.deepcopy(entry['note']))
            note = entry['note']
            report.append(dict(entry_key=entry['entry_key'], card_ids=ids,
                               disposition=entry['disposition'], kind=note['kind'],
                               summary=note['summary'], source=note['reference']['title'],
                               year=note['reference']['year'], locator=note['reference']['locator'],
                               url=note['reference']['url'], pdf_url=note['reference']['pdf_url']))
    managed = {b['id'] for b in batches}
    for card in data['cards']:
        retained = [n for n in card.get('textbook_notes', []) if n.get('batch') not in managed]
        combined = retained + notes.get(card['id'], [])
        if combined: card['textbook_notes'] = combined
        else: card.pop('textbook_notes', None)
    metadata = dict(source_entries=len(report), new_cards=sum(len(b['cards']) for b in batches),
                    existing_cards=len({i for e in report if e['disposition']=='existing_card' for i in e['card_ids']}),
                    annotated_cards=len(notes), sources=len({e['url'] for e in report}),
                    kinds=dict(collections.Counter(e['kind'] for e in report)))
    data['meta']['textbook_questions'] = metadata
    methodology = data['meta'].get('methodology', [])
    old_policy = 'Automatic selection allows at most one new card per paper title'
    methodology = [
        'The earlier automatic paper screen allowed at most one new card per paper title and rejected identical formulations and close duplicates within a source. Approved textbook and survey imports retain multiple distinct questions per publication. Confirmed overlaps supplement existing cards; collection-wide semantic deduplication remains incomplete.'
        if text.startswith(old_policy) else text for text in methodology
    ]
    prefix = 'Textbook and survey questions are dated paraphrases'
    if report:
        explanation = prefix + '; source locations, conjectures, research directions and caveats are preserved on the problem cards. These annotations do not establish current open status or change a later card review. New source drafts remain unassessed for importance. The reader contains the imported questions and external bibliographic references only; source files are not bundled.'
        if any(text.startswith(prefix) for text in methodology):
            methodology = [explanation if text.startswith(prefix) else text for text in methodology]
        else:
            methodology.append(explanation)
    data['meta']['methodology'] = methodology
    return dict(meta=metadata, entries=report)
