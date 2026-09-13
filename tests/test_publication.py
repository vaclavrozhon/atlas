"""Rebuild active inputs and verify edits, imports and reversible archival."""

import copy
import hashlib
import json
import csv
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(path.read_text())


def assert_export_parity(site, payload, *, independent_build=False):
    data = read_json(site / 'catalog.json')
    assert data['cards'] == payload['cards']
    if independent_build:
        # A fresh CLI build gets its own publication timestamp. Content-derived
        # metadata must still agree, and its exports must agree with each other.
        assert {k: v for k, v in data['meta'].items() if k != 'updated_at'} == {
            k: v for k, v in payload['meta'].items() if k != 'updated_at'
        }
    else:
        assert data['meta'] == payload['meta']
    assert data['areas'] == payload['areas']
    wrapper = (site / 'data.js').read_text()
    offline = json.loads(wrapper[len('window.TCS_ATLAS='):-2].replace('<\\/', '</'))
    assert offline == data
    assert not (site / 'updates.json').exists()
    assert not (site / 'README.md').exists()
    for name in ['index.html', 'app.js', 'community.js', 'votes.js', 'math.js', 'style.css', '.nojekyll']:
        assert (site / name).read_bytes() == (SOURCE / 'web' / name).read_bytes()
    assert (site / 'vendor/katex.min.js').exists()
    assert read_json(site / 'version.json')['version'] == data['meta']['version']
    with (site / 'catalog.csv').open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    assert [row['id'] for row in rows] == [card['id'] for card in data['cards']]
    for row, card in zip(rows, data['cards']):
        assert row['why'] == card['why']
        assert row['statement_review_status'] == card.get('statement_review', {}).get('status', '')
        assert row['statement_review_issue'] == card.get('statement_review', {}).get('remaining_issue', '')
        assert json.loads(row['textbook_notes']) == card.get('textbook_notes', [])
        assert json.loads(row['related_problem_ids']) == card.get('related_problem_ids', [])
        summary = card.get('working_summary', {})
        assert row['working_summary'] == ' '.join(summary.get('sentences', []))
        assert row['working_summary_date'] == summary.get('written_on', '')
        assert json.loads(row['working_summary_source_refs']) == summary.get('source_refs', [])
    assert not (site / 'scope-excluded.json').exists()
    for name in ['top100', 'top500', 'top1000']:
        subset = read_json(site / (name + '.json'))
        assert subset['subbenchmark'] == data['meta']['benchmarks'][name]
        quotas = subset['subbenchmark']['quotas']
        assert subset['cards'] == [card for card in data['cards']
            if card['status'] not in ('resolved', 'excluded')
            and card['importance_rank'] <= quotas[card['selection_group']]]
    top = read_json(site / 'top100.json')
    statements = read_json(site / 'top100-statements.json')
    assert statements['subbenchmark'] == top['subbenchmark']
    assert [c['id'] for c in statements['cards']] == [c['id'] for c in top['cards']]
    for statement, card in zip(statements['cards'], top['cards']):
        assert set(statement) <= {'id','title','area','question_type','formal','definitions',
                                 'answer_criterion','status','status_note','statement_review','references'}
        for field in ('formal','definitions','answer_criterion','statement_review'):
            assert statement.get(field) == card.get(field)


with tempfile.TemporaryDirectory(prefix='atlas-publication-') as directory:
    base = Path(directory)
    shutil.copytree(SOURCE / 'scripts', base / 'scripts', ignore=shutil.ignore_patterns('__pycache__'))
    shutil.copytree(SOURCE / 'data', base / 'data',
                    ignore=lambda directory, names: ['cards']
                    if Path(directory) == SOURCE / 'data/archive' else [])
    shutil.copytree(SOURCE / 'web', base / 'web')
    site = base / 'build'
    sys.path.insert(0, str(base / 'scripts'))
    import publish
    import import_cards
    import catalog_exports
    import archive_cards
    from card_activity import INDEX, ARCHIVED_CARDS, read_inactive
    from card_schema import canonical_record, reader_record, OBSOLETE_FIELDS, DERIVED_FIELDS

    def hashes():
        return {str(p.relative_to(base)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in (base / 'data').rglob('*') if p.is_file()}

    original_hashes = hashes()
    original = read_json(SOURCE / 'build/catalog.json')
    first = publish.publish()
    assert first['cards'] == original['cards']
    assert first['areas'] == original['areas']
    assert first['version'] == original['meta']['version']
    assert hashes() == original_hashes, 'Publishing must not rewrite canonical inputs'
    assert_export_parity(site, first)
    repeated = publish.publish()
    assert repeated['changed_ids'] == [] and repeated['version'] == first['version']

    # A plan-only update must reach open readers even if no card changes.
    plan_update = copy.deepcopy(first)
    plan_update['meta']['benchmarks']['top500']['tentative'] = True
    publish.update_metadata(plan_update, first['meta']['updated_at'])
    assert plan_update['meta']['version'] != first['version']

    # Statement and summary edits in the same source file both reach the reader.
    card = copy.deepcopy(next(c for c in first['cards'] if c['evidence'] == 'reviewed' and c.get('working_summary')))
    path = base / 'data/cards' / (card['id'] + '.json')
    authored = read_json(path)
    compact = canonical_record(card)
    assert not (OBSOLETE_FIELDS | DERIVED_FIELDS) & compact.keys()
    assert 'context' not in compact and compact['context_blocks'] == card['context_blocks']
    assert reader_record(compact, original['criteria'])['context'] == card['context']
    try:
        canonical_record({**compact, 'context': 'Conflicting duplicate context'})
    except ValueError:
        pass
    else:
        raise AssertionError('Conflicting context was silently discarded')
    authored['why'] += '\n\nPublication regression fixture.'
    authored['working_summary']['sentences'][0] += ' (Summary edit fixture.)'
    path.write_text(json.dumps(authored))
    edited = publish.publish()
    assert edited['changed_ids'] == [card['id']]
    delta = read_json(site / 'updates-delta.json')
    assert delta['base_version'] == first['version']
    assert delta['cards'][0]['why'] == authored['why']
    assert delta['cards'][0]['working_summary'] == authored['working_summary']
    assert hashes()[str(path.relative_to(base))] == hashlib.sha256(path.read_bytes()).hexdigest()
    assert_export_parity(site, edited)

    unchanged = {name: (site / name).read_bytes() for name in ['catalog.json', 'version.json']}
    authored['progress'][0]['citation'] = 'missing-regression-reference'
    path.write_text(json.dumps(authored))
    try:
        publish.publish()
    except ValueError as error:
        assert str(error) == 'Unknown progress citation'
    else:
        raise AssertionError('Invalid citation was published')
    assert all((site / name).read_bytes() == content for name, content in unchanged.items())
    path.write_text(json.dumps(compact))
    publish.publish()

    # Existing cards are preserved by default during import.
    registry_before = (base / 'data/id_registry.json').read_bytes()
    assert import_cards.import_cards([card]) == {'imported': [], 'skipped': [card['id']]}
    assert (base / 'data/id_registry.json').read_bytes() == registry_before
    deleted_path = INDEX
    deleted = read_json(deleted_path)
    retired_id = next(iter(deleted))
    registry = read_json(base / 'data/id_registry.json')
    retired_key, keyed_id = next((key, identifier) for key, identifier in registry.items()
                                if identifier in deleted and key.startswith(('reviewed:', 'source-import:', 'proposal:')))
    for fixture in [{**card, 'id': retired_id, 'key': 'deletion-test'},
                    {key: value for key, value in {**card, 'key': retired_key.split(':', 1)[1]}.items() if key != 'id'}]:
        try:
            import_cards.import_cards([fixture], replace=True)
        except ValueError as error:
            assert 'is inactive' in str(error)
        else:
            raise AssertionError('Deleted identity was imported')
    assert not (base / 'data/cards' / (retired_id + '.json')).exists()
    # A copied stale source file and a stale generated snapshot cannot revive it.
    (base / 'data/cards' / (retired_id + '.json')).write_text(json.dumps({**card, 'id': retired_id}))
    stale = read_json(site / 'catalog.json')
    stale['cards'].append({**card, 'id': retired_id})
    (site / 'catalog.json').write_text(json.dumps(stale))
    resurrected = publish.publish()
    assert retired_id not in {c['id'] for c in resurrected['cards']}

    # Highest retired IDs stay reserved, even without an ID-registry mapping.
    deleted['TCS-999999'] = 'Regression fixture: reserved deleted identity.'
    deleted_path.write_text(json.dumps(deleted))
    fresh = {key: value for key, value in card.items() if key not in {'id', 'key'}}
    fresh['key'] = 'regression-new-question'
    fresh.update(rank=123, classification_method='legacy', importance_method='legacy')
    imported = import_cards.import_cards([fresh])
    assert imported['imported'] == ['TCS-1000000']
    imported_source = read_json(base / 'data/cards/TCS-1000000.json')
    assert not (OBSOLETE_FIELDS | DERIVED_FIELDS | {'context'}) & imported_source.keys()
    added = publish.publish()
    assert 'TCS-1000000' in {c['id'] for c in added['cards']}

    # Archival preserves complete bytes, removes focus membership and incoming
    # related links, and emits the same removal delta as a former deletion.
    fresh_id = 'TCS-1000000'
    fresh_path = base / 'data/cards' / f'{fresh_id}.json'
    fresh_bytes = fresh_path.read_bytes()
    selection_path = base / 'data/benchmark_selection.json'
    selection = read_json(selection_path)
    area = next(area for area in selection['areas'] if area['area'] == card['area'])
    area['selected'] = [dict(id=fresh_id, topic='Fixture', reason='Archival focus fixture')]
    selection_path.write_text(json.dumps(selection))
    linked = read_json(path)
    linked.setdefault('related_problem_ids', []).append(fresh_id)
    path.write_text(json.dumps(linked))
    publish.publish()
    assert archive_cards.change_activity([fresh_id], reason='Regression fixture: deactivate.') == {'archive': [fresh_id]}
    archived_path = ARCHIVED_CARDS / fresh_path.name
    assert not fresh_path.exists() and archived_path.read_bytes() == fresh_bytes
    assert all(entry['id'] != fresh_id for area in read_json(selection_path)['areas'] for entry in area['selected'])
    removed = publish.publish()
    assert fresh_id not in {c['id'] for c in removed['cards']}
    assert all(fresh_id not in c['related_problem_ids'] for c in removed['cards'])
    assert read_json(site / 'updates-delta.json')['removed_ids'] == [fresh_id]
    assert archived_path.read_bytes() == fresh_bytes
    assert_export_parity(site, removed)
    assert publish.publish()['changed_ids'] == []

    # Neither explicit replacement nor a keyed import can reactivate it.
    for fixture in [read_json(archived_path), fresh]:
        try:
            import_cards.import_cards([fixture], replace=True)
        except ValueError as error:
            assert 'is inactive' in str(error)
        else:
            raise AssertionError('Ordinary import reactivated a card')

    # Restoration is explicit, preserves the file and does not restore focus.
    archive_cards.change_activity([fresh_id], restore=True, reason='Regression fixture: reconsider.')
    assert fresh_path.read_bytes() == fresh_bytes and not archived_path.exists()
    assert fresh_id not in read_inactive()
    restored = publish.publish()
    assert fresh_id in {c['id'] for c in restored['cards']}
    assert fresh_id in next(c for c in restored['cards'] if c['id'] == card['id'])['related_problem_ids']
    assert all(entry['id'] != fresh_id for area in read_json(selection_path)['areas'] for entry in area['selected'])
    events = [json.loads(line) for line in (INDEX.parent / 'activity.jsonl').read_text().splitlines()]
    assert [event['action'] for event in events[-2:]] == ['archive', 'restore']
    assert events[-1]['previous_reasons'][fresh_id] == 'Regression fixture: deactivate.'

    # Invalid batches and destination collisions never destroy existing data.
    before = hashes()
    for identifiers in [[fresh_id, fresh_id], [fresh_id, 'TCS-9999999'], ['../../invalid']]:
        try:
            archive_cards.change_activity(identifiers, reason='Invalid batch fixture')
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid archival batch accepted')
        assert hashes() == before
    archived_path.write_bytes(b'Historical content must not be overwritten')
    try:
        archive_cards.change_activity([fresh_id], reason='Collision fixture')
    except ValueError as error:
        assert 'destination already exists' in str(error)
    else:
        raise AssertionError('Archive was overwritten')
    assert fresh_path.read_bytes() == fresh_bytes
    archived_path.unlink()

    archive_cards.change_activity([fresh_id], reason='Regression fixture: final archive.')
    archived_path.write_text('{ invalid historical JSON is deliberately outside active validation')
    before = hashes()
    removed = publish.publish()
    assert hashes() == before, 'Publication must not inspect or repair archived contents'
    try:
        archive_cards.change_activity([fresh_id], restore=True, reason='Invalid restoration fixture')
    except ValueError:
        pass
    else:
        raise AssertionError('Invalid archive content was reactivated')
    assert hashes() == before

    # A file in the archive reserves its ID even before indexing, without parsing
    # old content, and must be excluded even if a stale active copy appears.
    unindexed_id = 'TCS-1000001'
    (ARCHIVED_CARDS / f'{unindexed_id}.json').write_text('unparsed historical fixture')
    stale_path = base / 'data/cards' / f'{unindexed_id}.json'
    stale_path.write_text('unparsed stale active fixture')
    assert unindexed_id not in {c['id'] for c in publish.publish()['cards']}
    try:
        import_cards.import_cards([{**card, 'id': unindexed_id, 'key': 'unindexed-archive'}], replace=True)
    except ValueError as error:
        assert 'is inactive' in str(error)
    else:
        raise AssertionError('Unindexed archived identity was imported')
    removed = publish.publish()

    # The standalone command rebuilds every generated file into an empty directory.
    clean = base / 'clean-output'
    subprocess.run([sys.executable, str(base / 'scripts/publish.py'), '--output', str(clean)],
                   cwd=directory, check=True, stdout=subprocess.DEVNULL)
    assert read_json(clean / 'catalog.json')['cards'] == removed['cards']
    assert not (clean / 'scope-excluded.json').exists()
    assert_export_parity(clean, removed, independent_build=True)

print(json.dumps({'records': len(original['cards']), 'checks': [
    'clean rebuild with no previous catalogue or research dependencies',
    'canonical inputs are never rewritten by publication', 'repeat publication stability',
    'JSON, CSV, offline JavaScript and benchmark export parity',
    'single-file statement and summary edits', 'invalid content cannot publish',
    'existing-card import protection', 'deleted IDs and source keys cannot return',
    'stale source files and outputs cannot resurrect deletions',
    'inactive IDs stay reserved', 'archival removal deltas', 'lossless archival and restoration',
    'focus and related links follow activity', 'archive contents bypass ordinary validation',
    'invalid batches and archive collisions preserve data']}))
