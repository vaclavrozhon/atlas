"""One-time, explicitly requested recovery into the inactive archive only.

Historical content is copied without scientific review or schema upgrades.
This is not an import route or a routine editorial command.
"""

import collections
import fcntl
import io
import json
from pathlib import Path
import subprocess
import sys
import tarfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from paths import DATA, ARCHIVE, ARCHIVED_CARDS
from catalog_exports import atomic


def main():
    with (ROOT / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        legacy = DATA / 'deleted_records.json'
        if not legacy.exists() or (ARCHIVE / 'index.json').exists():
            raise SystemExit('Migration already applied or legacy index unavailable')
        inactive = json.loads(legacy.read_text())
        registry = json.loads((DATA / 'id_registry.json').read_text())
        revisions = [subprocess.check_output(['git', 'rev-parse', rev], cwd=ROOT,
                                            text=True).strip() for rev in ['HEAD', 'HEAD^']]
        recovered, provenance = {}, {}

        def save(card, source, content=None):
            identifier = card.get('id')
            if not identifier and card.get('key'):
                identifiers = {registry[prefix + card['key']] for prefix in
                    ['', 'reviewed:', 'source-import:', 'proposal:'] if prefix + card['key'] in registry}
                if len(identifiers) == 1:
                    identifier = identifiers.pop()
                    card = dict(card, id=identifier)
                    source = dict(source, identity_from='data/id_registry.json')
            if identifier not in inactive or identifier in recovered:
                return
            # An ID, title, excerpt or hash alone is not a recovered card.
            if not {'title', 'formal', 'area', 'references'} <= card.keys():
                return
            if 'context' not in card and 'context_blocks' not in card:
                return
            recovered[identifier] = content or (json.dumps(card, ensure_ascii=False, indent=2) + '\n').encode()
            provenance[identifier] = source

        raw = subprocess.check_output(['git', 'archive', revisions[0], 'data/cards'], cwd=ROOT)
        with tarfile.open(fileobj=io.BytesIO(raw)) as archive:
            for member in archive:
                if member.isfile() and member.name.endswith('.json'):
                    content = archive.extractfile(member).read()
                    save(json.loads(content), dict(revision=revisions[0], path=member.name), content)

        old_paths = ['tcs-open-problems/atlas/site/catalog.json'] + [
            f'tcs-open-problems/atlas/to_delete/{name}/records.json' for name in
            ['large-buckets-20260910', 'large-buckets-second-20260910', 'small-buckets-20260910']]
        for path in old_paths:
            value = json.loads(subprocess.check_output(['git', 'show', f'{revisions[1]}:{path}'], cwd=ROOT))
            for card in value['cards'] if isinstance(value, dict) else value:
                save(card, dict(revision=revisions[1], path=path))

        def walk(value, source):
            if isinstance(value, dict):
                save(value, source)
                for child in value.values():
                    if isinstance(child, (dict, list)):
                        walk(child, source)
            elif isinstance(value, list):
                for child in value:
                    walk(child, source)

        # Some later cards existed only in retained research import batches.
        for path in sorted((ROOT / 'research').rglob('*.json')):
            if 'sources' in path.parts or path.parent == Path(__file__).parent:
                continue
            try:
                value = json.loads(path.read_text())
            except (ValueError, UnicodeError):
                continue
            walk(value, dict(path=str(path.relative_to(ROOT)), kind='saved_research_snapshot'))

        ARCHIVED_CARDS.mkdir(parents=True, exist_ok=True)
        for identifier, content in recovered.items():
            path = ARCHIVED_CARDS / f'{identifier}.json'
            with path.open('xb') as stream:
                stream.write(content)
        missing = sorted(set(inactive) - recovered.keys())
        report = dict(date='2026-09-13', authorization='User requested active/inactive cards with full archival preservation.',
                      recovered=len(recovered), unavailable=len(missing), unavailable_ids=missing,
                      note='Recovered snapshots retain historical content and are not certified as the final pre-removal revision. '
                           'Unavailable IDs retain their existing reasons; no replacement mathematical content was invented.',
                      sources=provenance)
        atomic(ARCHIVE / 'recovery.json', json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + '\n')
        legacy.rename(ARCHIVE / 'index.json')
        print(json.dumps(dict(recovered=len(recovered), unavailable_ids=missing,
                              sources=dict(collections.Counter(p['path'] for p in provenance.values())))))

    # Existing resolved/excluded files already hidden by the reader move intact.
    from archive_cards import change_activity
    retired = []
    for path in sorted((DATA / 'cards').glob('*.json')):
        card = json.loads(path.read_text())
        if card['status'] in {'resolved', 'excluded'} or card.get('scope_exclusion'):
            retired.append(card['id'])
    if retired:
        print(json.dumps(change_activity(retired,
            reason='Archived on 13 September 2026 under the active/inactive policy: already resolved or excluded; '
                   'the complete saved scientific status, evidence and review remain in the card.')))


if __name__ == '__main__':
    main()
