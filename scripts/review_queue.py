"""List and atomically reserve unfinished active cards in a shared checkout."""

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
from pathlib import Path
import secrets
import sys

from catalog_exports import atomic


ROOT = Path(__file__).resolve().parents[1]
REVIEW = Path('research/card-completion-20260913')
CLAIMS = '.review-claims.json'


def read_queue(root):
    return json.loads((root / REVIEW / 'queue.json').read_text())


def read_claims(root):
    path = root / CLAIMS
    return json.loads(path.read_text()) if path.exists() else {}


@contextmanager
def locked(root):
    with (root / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def pending_rows(root, queue):
    # Directory placement alone determines activity. Never read archive bodies.
    active = {path.stem for path in (root / 'data/cards').glob('TCS-*.json')}
    return [row for row in queue['records']
            if row['state'] == 'pending' and row['id'] in active]


def require_claim(root, identifier, token):
    """Check ownership while the caller holds .publish.lock."""
    claim = read_claims(root).get(identifier)
    if claim is None:
        if token is not None:
            raise ValueError(f'{identifier}: reservation no longer exists; claim it again')
    elif token != claim['token']:
        raise ValueError(f"{identifier}: reserved by {claim['worker']} since "
                         f"{claim['claimed_at']}; the matching claim_token is required")
    return claim


def write_claims(root, claims):
    atomic(root / CLAIMS, json.dumps(claims, ensure_ascii=False, indent=2) + '\n')


def public_rows(root, queue, claims):
    result = []
    for row in pending_rows(root, queue):
        item = {key: row.get(key, '') for key in ('id', 'title', 'area', 'priority')}
        claim = claims.get(row['id'])
        item['claim'] = ({key: claim[key] for key in ('worker', 'claimed_at')}
                         if claim else None)
        result.append(item)
    return result


def markdown(text):
    return str(text).replace('\n', ' ').replace('|', '&#124;')


def refresh_list(root, queue=None):
    """Refresh the versioned inventory under the caller's publication lock."""
    rows = pending_rows(root, queue if queue is not None else read_queue(root))
    lines = [
        '# Unfinished active cards', '',
        'Generated from [queue.json](queue.json); archived cards are excluded.',
        'This inventory records pending reviews, including work already reserved.',
        'Use `python3 scripts/review_queue.py list --available` for the live unclaimed list.',
        'Reserve a card before editing; see [the workflow](README.md#parallel-review-workflow).',
        '', f'Pending active reviews: **{len(rows)}**.', '',
        '| Card | Title | Area | Queue priority |',
        '| --- | --- | --- | --- |',
    ]
    for row in rows:
        identifier = row['id']
        lines.append(f'| [{identifier}](../../data/cards/{identifier}.json) | '
                     + ' | '.join(markdown(row.get(key, ''))
                                  for key in ('title', 'area', 'priority')) + ' |')
    atomic(root / REVIEW / 'unfinished.md', '\n'.join(lines) + '\n')
    return len(rows)


def finish_claim(root, identifier, token, queue):
    """Release a completed review and refresh its inventory under the same lock."""
    require_claim(root, identifier, token)
    claims = read_claims(root)
    if identifier in claims:
        del claims[identifier]
        write_claims(root, claims)
    refresh_list(root, queue)


def reserve(root, worker, identifier=None, area=None, priority=None):
    if not worker.strip():
        raise ValueError('worker must be a nonempty process name')
    with locked(root):
        queue, claims = read_queue(root), read_claims(root)
        rows = pending_rows(root, queue)
        if identifier is not None:
            rows = [row for row in rows if row['id'] == identifier]
            if not rows:
                raise ValueError(f'{identifier}: not a pending active card')
            require_claim(root, identifier, None)
        rows = [row for row in rows if row['id'] not in claims
                and (area is None or row.get('area') == area)
                and (priority is None or row.get('priority') == priority)]
        if not rows:
            raise ValueError('no unclaimed active card matches the selection')
        row = rows[0]
        path = root / 'data/cards' / (row['id'] + '.json')
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        claim = dict(worker=worker.strip(), token=secrets.token_hex(16),
                     claimed_at=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                     input_sha256=digest)
        claims[row['id']] = claim
        write_claims(root, claims)
        return dict(id=row['id'], title=row['title'], area=row.get('area', ''),
                    path=str(path.relative_to(root)), **claim,
                    baseline_changed=digest != row['input_sha256'])


def release(root, identifier, token):
    with locked(root):
        claim = require_claim(root, identifier, token)
        if claim is None:
            raise ValueError(f'{identifier}: reservation does not exist')
        claims = read_claims(root)
        del claims[identifier]
        write_claims(root, claims)
        return dict(id=identifier, released=True)


def main(argv=None, root=ROOT):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('status', help='show current active review and reservation counts')
    listing = commands.add_parser('list', help='list pending active cards in queue order')
    listing.add_argument('--available', action='store_true', help='omit reserved cards')
    listing.add_argument('--json', action='store_true', help='emit machine-readable rows')
    listing.add_argument('--area', help='exact area name')
    listing.add_argument('--priority', help='exact queue priority')
    claim = commands.add_parser('claim', help='atomically reserve one pending active card')
    claim.add_argument('--worker', required=True, help='distinct name for this process')
    claim.add_argument('--id', help='specific card; otherwise take first available match')
    claim.add_argument('--area', help='exact area name')
    claim.add_argument('--priority', help='exact queue priority')
    freeing = commands.add_parser('release', help='release an unfinished reservation')
    freeing.add_argument('--id', required=True)
    freeing.add_argument('--token', required=True, help='token returned by claim')
    commands.add_parser('export', help='refresh the human-readable unfinished.md inventory')
    args = parser.parse_args(argv)
    try:
        if args.command == 'claim':
            result = reserve(root, args.worker, args.id, args.area, args.priority)
        elif args.command == 'release':
            result = release(root, args.id, args.token)
        else:
            with locked(root):
                queue, claims = read_queue(root), read_claims(root)
                rows = public_rows(root, queue, claims)
                if args.command == 'export':
                    result = dict(path=str(REVIEW / 'unfinished.md'),
                                  pending_active=refresh_list(root, queue))
                elif args.command == 'status':
                    active = {path.stem for path in (root / 'data/cards').glob('TCS-*.json')}
                    reserved = sum(row['claim'] is not None for row in rows)
                    result = dict(active=len(active), pending_active=len(rows),
                                  reserved=reserved, available=len(rows) - reserved,
                                  completed_active_in_queue=sum(
                                      row['state'] == 'completed' and row['id'] in active
                                      for row in queue['records']),
                                  active_outside_queue=len(active - {
                                      row['id'] for row in queue['records']}))
                else:
                    rows = [row for row in rows
                            if (not args.available or row['claim'] is None)
                            and (args.area is None or row['area'] == args.area)
                            and (args.priority is None or row['priority'] == args.priority)]
                    if not args.json:
                        print('ID\tWORKER\tPRIORITY\tAREA\tTITLE')
                        for row in rows:
                            print('\t'.join([row['id'],
                                  row['claim']['worker'] if row['claim'] else '-',
                                  row['priority'], row['area'], row['title']]))
                        return 0
                    result = rows
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError) as error:
        print(f'review queue: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
