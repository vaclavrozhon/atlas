"""Check reversible small-bucket pruning against the frozen pre-publication data."""
import collections
import copy
import csv
import gzip
import hashlib
import json
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
sys.path.insert(0, str(BASE))
import taxonomy
from taxonomy import apply_taxonomy, editorial_card
from importance import apply_importance


def main():
    current = json.loads((BASE / 'site/catalog.json').read_text())
    before = json.loads(gzip.decompress((HERE / 'catalog-before.json.gz').read_bytes()))
    manifest = json.loads((HERE / 'manifest.json').read_text())
    snapshot = json.loads((HERE / 'records.json').read_text())
    large = json.loads(taxonomy.PRELIMINARY_PATH.read_text())
    removed = {i for i, d in manifest['records'].items() if d['state'] == 'quarantined'}
    removed_large = {i for i, d in large['records'].items() if d['state'] == 'quarantined'}
    saved = {c['id']: c for c in snapshot}
    old = {c['id']: c for c in before['cards']}
    cards = {c['id']: c for c in current['cards']}
    assert hashlib.sha256((HERE / 'records.json').read_bytes()).hexdigest() == manifest['archive_sha256']
    assert saved.keys() == manifest['records'].keys()
    assert all(saved[i] == old[i] for i in saved), 'Archive must contain exact, complete records'
    assert old.keys() == cards.keys(), 'A stable ID was changed'
    assert not removed.intersection(removed_large)
    assert {c['id'] for c in current['cards'] if c.get('scope_exclusion', {}).get('kind') == 'preliminary_quality'} == removed | removed_large
    assert all(old[i]['selection_group'] == 'small' for i in removed)
    large_before = {i for i, c in old.items() if c['selection_group'] == 'large'}
    large_now = {i for i, c in cards.items() if c['selection_group'] == 'large'}
    assert large_before == large_now
    assert all(cards[i]['area'] == old[i]['area'] for i in large_before)
    assert all(cards[i].get('textbook_notes') == old[i].get('textbook_notes') for i in old)
    assert all(cards[i]['original_area'] == old[i]['original_area'] for i in old)
    content_changes = [i for i in old if editorial_card(cards[i]) != editorial_card(old[i])]
    assert all(cards[i]['evidence'] == 'reviewed' or cards[i].get('review_outcome', {}).get('complete') for i in content_changes), content_changes
    assert not removed.intersection(content_changes), 'An archived record was overwritten'
    for i in removed:
        c, d = cards[i], manifest['records'][i]
        assert c['scope_exclusion']['review_id'] == manifest['review_id']
        assert c['scope_exclusion']['previous_area'] == d['category']
        assert c['scope_exclusion']['reason'] == d['reason']
        assert c['scope_exclusion']['archive'] == 'to_delete/small-buckets-20260910/records.json'
        assert c['selection_group'] == 'excluded' and c['selection_target'] == 0
    assert all(i not in removed for i, c in cards.items() if c.get('proposal_import') or c['evidence'] == 'reviewed')
    assert cards['TCS-6685']['selection_group'] == 'small'
    counts = collections.Counter(c['area'] for c in cards.values() if c['selection_group'] == 'small')
    for row in manifest['category_counts']:
        assert counts[row['category']] == row['remaining']
    assert sum(counts.values()) == manifest['small_remaining']
    repeated = copy.deepcopy(current)
    apply_taxonomy(repeated)
    apply_importance(repeated)
    assert repeated == current, 'Publication overlays are not idempotent'
    # Exercise every restoration in an isolated manifest under the atlas root.
    # Also ensure the restoration never copies old statement text over a later edit.
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        path = Path(temp) / 'manifest.json'
        restored = copy.deepcopy(manifest)
        for item in restored['records'].values():
            item['state'] = 'retained'
        path.write_text(json.dumps(restored))
        original_path = taxonomy.SMALL_PRELIMINARY_PATH
        try:
            taxonomy.SMALL_PRELIMINARY_PATH = path
            reverted = copy.deepcopy(current)
            apply_taxonomy(reverted)
            apply_importance(reverted)
        finally:
            taxonomy.SMALL_PRELIMINARY_PATH = original_path
    back = {c['id']: c for c in reverted['cards']}
    for i in old:
        if i not in content_changes:
            assert back[i]['area'] == old[i]['area'], ('restoration category', i)
        assert back[i].get('scope_exclusion') == old[i].get('scope_exclusion'), ('restoration scope', i)
        assert editorial_card(back[i]) == editorial_card(cards[i]), ('restoration replaced text', i)
        assert back[i].get('textbook_notes') == cards[i].get('textbook_notes')
    csv_rows = list(csv.DictReader((BASE / 'site/catalog.csv').open(encoding='utf-8-sig')))
    assert {r['id'] for r in csv_rows} == cards.keys()
    assert {r['id'] for r in csv_rows if r['scope_exclusion_kind'] == 'preliminary_quality'} == removed | removed_large
    assert {c['id'] for c in json.loads((BASE / 'site/scope-excluded.json').read_text())} == {i for i, c in cards.items() if c.get('scope_exclusion')}
    updates = json.loads((BASE / 'site/updates.json').read_text())
    assert updates['cards'] == current['cards'] and updates['areas'] == current['areas']
    script = (BASE / 'site/data.js').read_text()
    offline = json.loads(script[len('window.TCS_ATLAS='):-2].replace('<\\/', '</'))
    assert offline == current
    report = dict(version=current['meta']['version'], reviewed=manifest['reviewed_small_count'],
        removed=len(removed), retained=sum(counts.values()), large_unchanged=len(large_now),
        all_ids_preserved=len(cards), concurrent_review_changes=content_changes,
        source_annotations_preserved=True, exact_archive_and_hash=True,
        full_batch_restoration_verified=True, repeat_publication_idempotent=True,
        reviewed_and_approved_problems_preserved=True, bb6_retained=True,
        catalogue_csv_offline_and_update_exports_consistent=True)
    (HERE / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
