"""Check exact preservation and independent restoration of all three review batches."""
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
from importance import apply_importance

ARCHIVE = BASE/'to_delete/large-buckets-second-20260910'
BATCHES = ['PRELIMINARY_PATH', 'SMALL_PRELIMINARY_PATH', 'SECOND_LARGE_PRELIMINARY_PATH']
DERIVED = taxonomy.ASSIGNMENT_FIELDS | {'area', 'importance', 'importance_rank', 'importance_count'}


def content(card):
    return {k: v for k, v in card.items() if k not in DERIVED}


def main():
    current = json.loads((BASE/'site/catalog.json').read_text())
    before = json.load(gzip.open(ARCHIVE/'catalog-before.json.gz', 'rt'))
    manifest = json.loads((ARCHIVE/'manifest.json').read_text())
    category_corrections = {r['id']: r for r in manifest.get('category_corrections', [])}
    snapshot = json.loads((ARCHIVE/'records.json').read_text())
    old = {c['id']: c for c in before['cards']}
    cards = {c['id']: c for c in current['cards']}
    removed = set(manifest['records'])
    saved = {c['id']: c for c in snapshot}
    assert len(removed) == 543 and saved.keys() == removed
    assert hashlib.sha256((ARCHIVE/'records.json').read_bytes()).hexdigest() == manifest['archive_sha256']
    assert all(saved[i] == old[i] for i in removed), 'Snapshots must be full exact copies'
    assert old.keys() <= cards.keys(), 'A stable ID disappeared'
    for path, digest in manifest['previous_manifest_hashes'].items():
        assert hashlib.sha256((BASE/path).read_bytes()).hexdigest() == digest, path
    manifests = {attr: json.loads(getattr(taxonomy, attr).read_text()) for attr in BATCHES}
    active_ids = {attr: {i for i, d in m['records'].items() if d['state']=='quarantined'}
                  for attr, m in manifests.items()}
    all_removed = set.union(*active_ids.values())
    actual = {i for i, c in cards.items() if c.get('scope_exclusion', {}).get('kind')=='preliminary_quality'}
    assert actual == all_removed
    changes = []
    for i, c in old.items():
        if content(cards[i]) != content(c):
            assert i not in removed
            assert cards[i]['evidence']=='reviewed' or cards[i].get('review_outcome', {}).get('complete'), i
            changes.append(i)
        if i not in removed:
            assert cards[i].get('scope_exclusion') == c.get('scope_exclusion'), i
            assert cards[i]['area'] == category_corrections.get(i, {}).get('after', c['area']), i
        assert cards[i].get('textbook_notes') == c.get('textbook_notes'), i
    for i in removed:
        c, d = cards[i], manifest['records'][i]
        assert old[i]['selection_group']=='large' and old[i]['evidence']!='reviewed'
        assert content(c) == content(saved[i])
        assert c['scope_exclusion']['review_id'] == manifest['review_id']
        assert c['scope_exclusion']['previous_area'] == d['category']
        assert c['scope_exclusion']['reason'] == d['reason']
        assert c['selection_group']=='excluded' and c['selection_target']==0
        for target in d['related_retained_ids']:
            assert not cards[target].get('scope_exclusion'), (i, target)
        if d.get('duplicate_of'):
            assert c['scope_exclusion']['duplicate_of']==d['duplicate_of']
            assert not cards[d['duplicate_of']].get('scope_exclusion')
    repeated = copy.deepcopy(current)
    taxonomy.apply_taxonomy(repeated)
    apply_importance(repeated)
    assert repeated == current, 'Publication overlay must be idempotent'
    restoration_counts = {}
    # Temporary manifests are inside the workspace so their archive paths remain
    # valid. No live state is changed, even for full old-batch restoration.
    with tempfile.TemporaryDirectory(dir=HERE) as temp:
        for lifted in [[attr] for attr in BATCHES] + [BATCHES]:
            original_paths = {attr: getattr(taxonomy, attr) for attr in lifted}
            try:
                for attr in lifted:
                    m = copy.deepcopy(manifests[attr])
                    for d in m['records'].values():
                        d['state']='retained'
                    path = Path(temp)/attr/'manifest.json'
                    path.parent.mkdir(exist_ok=True)
                    path.write_text(json.dumps(m))
                    setattr(taxonomy, attr, path)
                restored = copy.deepcopy(current)
                taxonomy.apply_taxonomy(restored)
                apply_importance(restored)
            finally:
                for attr, path in original_paths.items():
                    setattr(taxonomy, attr, path)
            expected = all_removed - set.union(*(active_ids[attr] for attr in lifted))
            back = {c['id']: c for c in restored['cards']}
            assert {i for i, c in back.items() if c.get('scope_exclusion', {}).get('kind')=='preliminary_quality'} == expected
            assert all(content(back[i])==content(cards[i]) for i in cards), 'Restore overwrote current authored content'
            if lifted==['SECOND_LARGE_PRELIMINARY_PATH']:
                assert all(back[i]['area']==category_corrections.get(i, {}).get('after', old[i]['area']) for i in old)
                assert all(back[i].get('scope_exclusion')==old[i].get('scope_exclusion') for i in old)
            restoration_counts['+'.join(lifted)] = len(expected)
    csv_rows = list(csv.DictReader((BASE/'site/catalog.csv').open(encoding='utf-8-sig')))
    assert {r['id'] for r in csv_rows} == cards.keys()
    assert {r['id'] for r in csv_rows if r['scope_exclusion_kind']=='preliminary_quality'} == all_removed
    ledger = list(csv.DictReader((ARCHIVE/'decisions.csv').open()))
    assert len(ledger)==543 and {r['id'] for r in ledger}==removed
    assert len({r['reason'] for r in ledger})==543, 'Reasons must be individual, not repeated templates'
    assert [int(r['sequence']) for r in ledger]==list(range(1,544))
    text = (ARCHIVE/'DECISIONS.md').read_text()
    assert all(f"{r['sequence']}. **{r['id']} —" in text for r in ledger)
    offline_text = (BASE/'site/data.js').read_text()
    offline = json.loads(offline_text[len('window.TCS_ATLAS='):-2].replace('<\\/', '</'))
    assert offline == current
    updates = json.loads((BASE/'site/updates.json').read_text())
    assert updates['cards']==current['cards'] and updates['meta']==current['meta']
    assert {c['id'] for c in json.loads((BASE/'site/scope-excluded.json').read_text())} == {i for i,c in cards.items() if c.get('scope_exclusion')}
    counts = collections.Counter(c['selection_group'] for c in current['cards'])
    assert counts['large']==1591 and counts['small']==1104 and len(cards)==7156
    assert all(a['count']>=50 for a in current['areas'] if a['group']=='large')
    report = dict(version=current['meta']['version'],large_before=2134,removed=543,large_remaining=counts['large'],
                  small_preserved=counts['small'],all_saved=len(cards),candidate_count=counts['large']+counts['small'],
                  archive_total=counts['excluded'],previous_manifests_unchanged=True,exact_archive=True,
                  individual_reasons=543,source_annotations_preserved=True,all_ids_preserved=True,
                  idempotent=True,restoration_remaining_quarantines=restoration_counts,
                  concurrent_authored_changes=changes,export_parity=True)
    report['category_corrections'] = list(category_corrections.values())
    (HERE/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return report


if __name__=='__main__':
    main()
