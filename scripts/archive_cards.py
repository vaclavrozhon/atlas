"""Move complete cards between the active catalogue and the inactive archive."""

import argparse
import datetime
import fcntl
import json
import re

from paths import ROOT, DATA, CARDS, ARCHIVED_CARDS
from card_activity import INDEX, read_inactive
from catalog_exports import atomic


def change_activity(identifiers, *, restore=False, reason):
    if not isinstance(reason, str) or not reason.strip():
        raise ValueError('A specific editorial reason is required')
    if not identifiers or len(set(identifiers)) != len(identifiers):
        raise ValueError('Supply one or more distinct card IDs')
    with (ROOT / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        inactive = read_inactive()
        previous_reasons = {identifier: inactive[identifier] for identifier in identifiers if identifier in inactive}
        pending = []
        selection_path = DATA / 'benchmark_selection.json'
        selection = json.loads(selection_path.read_text())
        for identifier in identifiers:
            if not re.fullmatch(r'TCS-\d{4,}', identifier):
                raise ValueError(f'Invalid card ID: {identifier}')
            active = CARDS / f'{identifier}.json'
            archived = ARCHIVED_CARDS / f'{identifier}.json'
            source, destination = (archived, active) if restore else (active, archived)
            if not source.is_file():
                raise ValueError(f'{identifier}: no {"archived" if restore else "active"} card file')
            if destination.exists():
                raise ValueError(f'{identifier}: destination already exists; refusing to overwrite it')
            card = json.loads(source.read_text())
            if not isinstance(card, dict) or card.get('id') != identifier:
                raise ValueError(f'{source.name}: card ID must match its filename')
            if restore:
                # Restoration is explicit and must meet current active-card rules.
                from publish import validate_record
                from card_schema import reader_record
                criteria = json.loads((DATA / 'criteria.json').read_text())
                validate_record(reader_record(card, criteria), active, criteria)
                inactive.pop(identifier, None)
            else:
                inactive[identifier] = reason.strip()
            pending.append((source, destination))

        # Validate the entire batch before moving any files. Reserve IDs before
        # archival moves; release them only after successful restoration moves.
        # Interrupted operations therefore never publish an inactive identity.
        ARCHIVED_CARDS.mkdir(parents=True, exist_ok=True)
        def save_index():
            atomic(INDEX, json.dumps(inactive, ensure_ascii=False, indent=2, sort_keys=True) + '\n')
        if not restore:
            save_index()
        for source, destination in pending:
            source.rename(destination)  # preserve every byte, including historical fields
        if restore:
            save_index()
        else:
            changed_selection = False
            for area in selection['areas']:
                selected = [entry for entry in area['selected'] if entry['id'] not in identifiers]
                if selected != area['selected']:
                    area['selected'] = selected
                    changed_selection = True
            if changed_selection:
                atomic(selection_path, json.dumps(selection, ensure_ascii=False, indent=2) + '\n')
        # Retain the explicit decision even after the inactive index entry is removed.
        event = dict(action='restore' if restore else 'archive', ids=list(identifiers),
                     reason=reason.strip(),
                     recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'))
        if previous_reasons:
            event['previous_reasons'] = previous_reasons
        with (INDEX.parent / 'activity.jsonl').open('a') as stream:
            stream.write(json.dumps(event, ensure_ascii=False) + '\n')
        return {event['action']: list(identifiers)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ids', nargs='+', help='Stable IDs, for example TCS-0123')
    parser.add_argument('--reason', required=True, help='Specific reason for the editorial decision')
    parser.add_argument('--restore', action='store_true', help='Explicitly return archived cards to active work')
    args = parser.parse_args()
    try:
        print(json.dumps(change_activity(args.ids, restore=args.restore, reason=args.reason)))
    except (ValueError, OSError) as error:
        parser.exit(1, f'{error}\n')
