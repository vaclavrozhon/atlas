"""Import complete problem cards, reserving stable IDs and honoring deletions."""

import argparse
import datetime
import fcntl
import json
from pathlib import Path

from paths import ROOT, DATA
from deleted_records import read_deleted
from catalog_exports import atomic
from publish import validate_record
from card_schema import canonical_record, reader_record


def import_cards(records, replace=False):
    with (ROOT / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        registry_path = DATA / 'id_registry.json'
        original_registry = registry_path.read_text()
        registry = json.loads(original_registry)
        criteria = json.loads((DATA / 'criteria.json').read_text())
        deleted = read_deleted()
        cards = DATA / 'cards'
        reserved = set(registry.values()) | set(deleted) | {p.stem for p in cards.glob('*.json')}
        maximum = max((int(identifier.split('-')[-1]) for identifier in reserved), default=0)
        pending, seen, skipped = [], set(), []
        now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
        for record in records:
            card = dict(record)
            key = card.get('key')
            aliases = [prefix + key for prefix in ['', 'reviewed:', 'source-import:', 'proposal:']] if key else []
            known = {registry[alias] for alias in aliases if alias in registry}
            if len(known) > 1:
                raise ValueError(f'Ambiguous source key: {key}')
            known_id = next(iter(known), None)
            identifier = card.get('id') or known_id
            if known_id and identifier != known_id:
                raise ValueError(f'{key}: source key is already assigned to {known_id}')
            if identifier in deleted:
                raise ValueError(f'{identifier} was deleted: {deleted[identifier]}')
            if not identifier:
                maximum += 1
                identifier = f'TCS-{maximum:04d}'
            if identifier in seen:
                raise ValueError(f'Duplicate import ID: {identifier}')
            seen.add(identifier)
            # Explicit IDs are also reserved before assigning the next new ID.
            if not identifier.startswith('TCS-') or not identifier[4:].isdigit():
                raise ValueError(f'Invalid import ID: {identifier}')
            maximum = max(maximum, int(identifier[4:]))
            path = cards / f'{identifier}.json'
            if identifier in reserved and not path.exists():
                raise ValueError(f'{identifier}: historical ID is reserved and has no active card')
            if path.exists() and not replace:
                skipped.append(identifier)
                continue
            card['id'] = identifier
            card.setdefault('is_new', True)
            card.setdefault('progress', [])
            card.setdefault('published_at', now)
            card.setdefault('updated_at', now)
            card = canonical_record(card)
            validate_record(reader_record(card, criteria), path, criteria)
            # Deleted cards never reach this point; new source keys remain stable.
            if key and not known_id:
                registry['reviewed:' + key] = identifier
            pending.append((path, card))
        for path, card in pending:
            atomic(path, json.dumps(card, ensure_ascii=False, indent=2) + '\n')
        if registry != json.loads(original_registry):
            atomic(registry_path, json.dumps(registry, ensure_ascii=False, indent=2) + '\n')
        return dict(imported=[card['id'] for _, card in pending], skipped=skipped)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    parser.add_argument('--replace', action='store_true', help='Replace existing cards explicitly')
    args = parser.parse_args()
    value = json.loads(args.file.read_text())
    records = value if isinstance(value, list) else value.get('cards', [value])
    print(json.dumps(import_cards(records, replace=args.replace)))
