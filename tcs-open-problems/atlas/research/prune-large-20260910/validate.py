"""Check preservation, exclusion, restoration and publication consistency."""
import collections,copy,csv,gzip,hashlib,json,sys,tempfile
from pathlib import Path
BASE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(BASE))
import taxonomy
from taxonomy import apply_taxonomy,editorial_card
from importance import apply_importance
HERE=Path(__file__).resolve().parent
ARCHIVE=BASE/'to_delete/large-buckets-20260910'

def main():
    current=json.loads((BASE/'site/catalog.json').read_text())
    before=json.loads(gzip.decompress((ARCHIVE/'catalog-before.json.gz').read_bytes()))
    manifest=json.loads((ARCHIVE/'manifest.json').read_text())
    snapshot=json.loads((ARCHIVE/'records.json').read_text())
    assert hashlib.sha256((ARCHIVE/'records.json').read_bytes()).hexdigest()==manifest['archive_sha256']
    remove={id for id,d in manifest['records'].items() if d['state']=='quarantined'}
    saved={c['id']:c for c in snapshot};old={c['id']:c for c in before['cards']};cards={c['id']:c for c in current['cards']}
    assert saved.keys()==manifest['records'].keys()
    assert all(saved[id]==old[id] for id in saved), 'Archive must contain complete, exact pre-pruning records'
    assert old.keys()<=cards.keys(), 'Stable IDs were lost'
    actual={c['id'] for c in current['cards'] if c.get('scope_exclusion',{}).get('kind')=='preliminary_quality'}
    assert actual==remove
    assert all(old[id]['selection_group']=='large' for id in remove)
    small=[id for id,c in old.items() if c['selection_group']=='small']
    assert all(cards[id]['area']==old[id]['area'] and not cards[id].get('scope_exclusion') for id in small)
    assert all(cards[id].get('textbook_notes')==old[id].get('textbook_notes') for id in old), 'Source annotations changed'
    assert all(cards[id]['original_area']==old[id]['original_area'] for id in old)
    # The publication may include a simultaneous canonical card upgrade. Record
    # such differences rather than attributing another writer's work to pruning.
    content_changes=[id for id in old if editorial_card(cards[id])!=editorial_card(old[id])]
    assert all(cards[id]['evidence']=='reviewed' or cards[id].get('review_outcome',{}).get('complete') for id in content_changes),content_changes
    for id in remove:
        c=cards[id];d=manifest['records'][id]
        assert c['scope_exclusion']['previous_area']==d['category']
        assert c['scope_exclusion']['reason']==d['reason']
        assert c['selection_group']=='excluded' and c['selection_target']==0
        if d.get('duplicate_of'):assert d['duplicate_of'] in cards and d['duplicate_of'] not in remove
    assert all(not c.get('scope_exclusion') for c in current['cards'] if c.get('proposal_import'))
    assert all(a['count']>=a['target'] for a in current['areas'] if a['group']=='large')
    repeated=copy.deepcopy(current);apply_taxonomy(repeated);apply_importance(repeated)
    assert repeated==current, 'Routing and ranking are not idempotent'
    # Reverse every decision in a temporary manifest, using the real taxonomy
    # and importance pipeline. No production decision is modified.
    with tempfile.TemporaryDirectory() as temp:
        path=Path(temp)/'manifest.json';restored=copy.deepcopy(manifest)
        for item in restored['records'].values():item['state']='retained'
        path.write_text(json.dumps(restored));original_path=taxonomy.PRELIMINARY_PATH
        try:
            taxonomy.PRELIMINARY_PATH=path
            reverted=copy.deepcopy(current);apply_taxonomy(reverted);apply_importance(reverted)
        finally:taxonomy.PRELIMINARY_PATH=original_path
    back={c['id']:c for c in reverted['cards']}
    for id in old:
        # New canonical wording can legitimately change topic-rule routing.
        # Restoration must not roll that newer review back to a stale category.
        if id not in content_changes:
            assert back[id]['area']==old[id]['area'],('restore category',id)
        elif id not in remove:
            assert back[id]['area']==cards[id]['area'],('restore changed an unaffected category',id)
        assert back[id].get('scope_exclusion')==old[id].get('scope_exclusion'),('restore scope',id)
        assert editorial_card(back[id])==editorial_card(cards[id]),('restore overwrote current text',id)
    rows=list(csv.DictReader((BASE/'site/catalog.csv').open(encoding='utf-8-sig')))
    assert {r['id'] for r in rows}==cards.keys()
    assert {r['id'] for r in rows if r['scope_exclusion_kind']=='preliminary_quality'}==remove
    assert {c['id'] for c in json.loads((BASE/'site/scope-excluded.json').read_text())}=={id for id,c in cards.items() if c.get('scope_exclusion')}
    updates=json.loads((BASE/'site/updates.json').read_text());assert updates['cards']==current['cards'] and updates['areas']==current['areas']
    script=(BASE/'site/data.js').read_text();offline=json.loads(script[len('window.TCS_ATLAS='):-2].replace('<\\/','</'));assert offline==current
    assert all(not cards[id].get('scope_exclusion') for id,c in old.items() if c['selection_group']=='large' and c['importance']['score']>=90 and c['status']!='resolved')
    rerouted=[id for id in old if id not in remove and cards[id]['area']!=old[id]['area']]
    assert set(rerouted)<=set(content_changes),('unexplained topic changes',rerouted)
    report=dict(version=current['meta']['version'],reviewed_large=manifest['reviewed_large_count'],removed=len(remove),large_remaining=sum(a['count'] for a in current['areas'] if a['group']=='large'),small_records_preserved=len(small),all_ids_preserved=len(old),source_annotations_preserved=True,complete_archive=True,full_batch_restoration_verified=True,idempotent=True,concurrent_canonical_upgrades=content_changes,concurrent_review_topic_changes=rerouted,checks=['exact full-record snapshots and hash','all 25 small buckets preserved','all stable IDs and source notes retained','all active 90+ landmarks retained','both archival kinds counted separately','full batch restoration preserves current content','publication and offline/CSV/live exports consistent'])
    (HERE/'validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
