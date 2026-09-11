"""Validate publication, refresh addition indexes, and package the offline atlas."""
import collections
import csv
import fcntl
import gzip
import io
import json
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ATLAS = HERE.parents[1]
SITE = ATLAS / 'site'
BATCH = 'fundamental-small-second-20260910'
sys.path.insert(0, str(ATLAS))
from publish import atomic, csvtext

def read(p):
    return json.loads(p.read_text())

def main():
    with (ATLAS / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        data = read(SITE / 'catalog.json')
        by_id = {c['id']: c for c in data['cards']}
        registry = read(ATLAS / 'id_registry.json')
        drafts = read(ATLAS / 'proposals' / (BATCH + '.json'))['cards']
        identifiers = [registry['proposal:' + c['key']] for c in drafts]
        imported = [by_id[i] for i in identifiers]
        assert len(identifiers) == len(set(identifiers)) == 26
        for draft, c in zip(drafts, imported):
            assert c['area'] == draft['area'] and not c.get('scope_exclusion')
            assert c['proposal_import']['batch'] == BATCH
            assert c['importance']['method'] == 'editorial' and c['importance']['reason']
            for field in ['title', 'formal', 'why', 'references', 'context', 'status_note']:
                assert c[field] == draft[field], (c['id'], field)
            assert c['evidence'] == 'source' and c['model_self_contained'] is False
        assert len({c['area'] for c in imported}) == 24
        assert all(c['area'] != 'Miscellaneous' for c in imported)

        with gzip.open(HERE / 'prepublication-catalog.json.gz', 'rt') as f:
            before = json.load(f)
        assert {c['id'] for c in before['cards']} <= set(by_id)
        fields = ['title', 'formal', 'context', 'why', 'references', 'status', 'evidence',
                  'source_formulation', 'legacy', 'review_outcome', 'proposal_import']
        concurrent = []
        canonical_by_id = {c['id']: c for p in (ATLAS / 'cards').glob('*.json')
                           if (c := read(p)).get('id')}
        for previous in before['cards']:
            current = by_id[previous['id']]
            changed = [k for k in fields if previous.get(k) != current.get(k)]
            if not changed:
                continue
            assert current['evidence'] == 'reviewed' and current['id'] in canonical_by_id, (current['id'], changed)
            authored = canonical_by_id[current['id']]
            assert all(current.get(k) == authored.get(k) for k in changed if k != 'evidence'), (current['id'], changed)
            concurrent.append(dict(id=current['id'], fields=changed, reason='Concurrent canonical review retained'))
        first = read(HERE / 'after-first-publication.json')
        first_cards = {c['id']: c for c in first['cards']}
        assert set(first_cards) == set(identifiers)
        assert all(all(c[k] == first_cards[c['id']][k] for k in ['key','formal','references','published_at']) for c in imported)

        offline = (SITE / 'data.js').read_text()
        offline_data = json.loads(offline[len('window.TCS_ATLAS='):].rstrip(';\n'))
        assert offline_data == data
        updates = read(SITE / 'updates.json')
        assert updates['cards'] == data['cards'] and updates['version'] == data['meta']['version']
        rows = {r['id']: r for r in csv.DictReader((SITE / 'catalog.csv').open(encoding='utf-8-sig'))}
        assert set(rows) == set(by_id)
        for c in imported:
            assert rows[c['id']]['formal'] == c['formal']
            assert rows[c['id']]['area'] == c['area']
            assert int(rows[c['id']]['importance_rank']) == c['importance_rank']

        seed_by_id = {}
        for path in sorted((ATLAS / 'proposals').glob('*.json')):
            for draft in read(path)['cards']:
                seed_by_id[registry['proposal:' + draft['key']]] = draft
        entries = []
        for c in data['cards']:
            if c['id'] not in seed_by_id:
                continue
            draft = seed_by_id[c['id']]
            provenance = draft['proposal_import']
            entries.append(dict(id=c['id'], key=draft['key'], title=c['title'],
                group=provenance['group'], category=c['area'], batch=provenance['batch'],
                proposal=provenance['source_file'], slug=provenance['slug']))
        new_entries = [e for e in entries if e['batch'] == BATCH]
        assert len(new_entries) == 26 and len(entries) == len(seed_by_id)

        def manifest(selected, batch):
            groups = collections.Counter(e['group'] for e in selected)
            return dict(batch=batch, published_on='2026-09-10', publication_level='short_source_drafts',
                large=groups['large'], small=groups['small'], total=len(selected),
                catalogue_total=len(data['cards']), catalogue_version=data['meta']['version'], entries=selected)

        publication = manifest(new_entries, BATCH)
        (HERE / 'publication.json').write_text(json.dumps(publication, ensure_ascii=False, indent=2) + '\n')
        all_manifest = manifest(entries, 'fundamental-20260910-all')
        all_manifest['batches'] = sorted({e['batch'] for e in entries})
        atomic(SITE / 'fundamental-additions.json', json.dumps(all_manifest, ensure_ascii=False, indent=2) + '\n')
        atomic(SITE / 'fundamental-additions.csv', csvtext(entries, ['id','title','group','category','batch','slug','proposal']))
        atomic(SITE / 'fundamental-small-second-additions.json', json.dumps(publication, ensure_ascii=False, indent=2) + '\n')
        atomic(SITE / 'fundamental-small-second-additions.csv', csvtext(new_entries, ['id','title','group','category','batch','slug','proposal']))

        def markdown(selected, title, intro):
            lines = ['# ' + title, '', intro, '', '| ID | Problem | Category |', '| --- | --- | --- |']
            for e in selected:
                safe = e['title'].replace('|', '\\|')
                lines.append(f"| [{e['id']}](index.html?view=compact#{e['id']}) | {safe} | {e['category']} |")
            return '\n'.join(lines) + '\n'
        atomic(SITE / 'fundamental-additions.md', markdown(entries,
            f"All {len(entries)} approved fundamental-problem additions",
            'Published as English research drafts with source links and editorial importance. Includes the earlier 144 proposals and the 26 additional small-category proposals. ' 
            '[View only the latest 26](fundamental-small-second-additions.md).'))
        atomic(SITE / 'fundamental-small-second-additions.md', markdown(new_entries,
            '26 additional fundamental problems in small categories',
            'The approved second-pass proposals are now available in the atlas, with stable IDs, source references, and importance ordering. They cover 24 small categories; Miscellaneous has no new proposal. ' 
            '[Browse all approved additions](fundamental-additions.md).'))
        readme = (SITE / 'README.md').read_text()
        paragraph = (f'## Approved fundamental-problem proposals\n\nAll {len(entries)} retained proposals from the September 2026 searches have been added: '
            f"{all_manifest['large']} in large categories and {all_manifest['small']} in small categories. "
            'This includes the latest 26 additions across 24 small categories. They carry English questions, primary-source links, editorial importance assessments and stable IDs; they remain short drafts until individually developed to the full research-card standard. Shared questions have only one card each.\n\n'
            '[Browse the latest 26](fundamental-small-second-additions.md) · '
            f'[Browse all {len(entries)} additions](fundamental-additions.md) · [JSON](fundamental-additions.json) · [CSV](fundamental-additions.csv).\n\n')
        assert '## Approved fundamental-problem proposals' in readme
        readme = re.sub(r'## Approved fundamental-problem proposals\n.*?(?=\nReview progress:|\Z)', paragraph, readme, flags=re.S)
        atomic(SITE / 'README.md', readme)

        validation = dict(imported=len(imported), categories=24, catalogue_total=len(data['cards']),
            catalogue_version=data['meta']['version'], existing_ids_preserved=True,
            original_approved_proposals_preserved=len(entries)-26, stable_ids_on_repeat=True,
            concurrent_authored_reviews=concurrent,
            checks=['all 26 prepared questions imported', '24 intended categories', 'English content and sources preserved',
                    'editorial importance and category ranks', 'existing content retained or upgraded by canonical review',
                    'catalogue JSON/CSV, offline data and live snapshot parity', 'stable proposal IDs', 'all-additions index updated'])
        (HERE / 'validation.json').write_text(json.dumps(validation, ensure_ascii=False, indent=2) + '\n')
        archive = ATLAS / 'tcs-atlas-demo.zip'
        temp = archive.with_suffix('.zip.packaging')
        with zipfile.ZipFile(temp, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for file in sorted(SITE.rglob('*')):
                if file.is_file() and not file.name.endswith('.publishing'):
                    z.write(file, 'tcs-atlas-demo/' + str(file.relative_to(SITE)))
        temp.replace(archive)
        with zipfile.ZipFile(archive) as z:
            assert z.testzip() is None
            assert json.loads(z.read('tcs-atlas-demo/catalog.json')) == data
        print(json.dumps({**validation, 'archive_bytes': archive.stat().st_size}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
