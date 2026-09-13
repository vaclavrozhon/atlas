"""Apply the explicitly reviewed groups to current cards, preserving other edits."""

import collections
import datetime
import hashlib
import itertools
import json
import pathlib
import sys

from review import ROOT, normid

HERE = pathlib.Path(__file__).resolve().parent


def active(card, deleted):
    return (card['id'] not in deleted and not card.get('scope_exclusion')
            and card['status'] not in {'resolved', 'excluded'})


def main():
    previous = json.loads((HERE / 'audit.json').read_text()) if (HERE / 'audit.json').exists() else {}
    deleted = json.loads((ROOT / 'data/deleted_records.json').read_text())
    paths = {p.stem: p for p in (ROOT / 'data/cards').glob('*.json')}
    cards = {identifier: json.loads(p.read_text()) for identifier, p in paths.items()}
    ids = {identifier for identifier, c in cards.items() if active(c, deleted)}
    edges = set()
    groups = []
    removed_during_review = set()
    for line in (HERE / 'groups.tsv').read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        mode, topic, raw = map(str.strip, line.split('|'))
        members = [normid(x) for x in raw.split()]
        assert mode in {'C', 'S'} and len(set(members)) == len(members)
        removed_during_review.update(set(members) - ids)
        pairs = (itertools.combinations(members, 2) if mode == 'C'
                 else ((members[0], target) for target in members[1:]))
        accepted = sorted({tuple(sorted(pair)) for pair in pairs if set(pair) <= ids})
        edges.update(accepted)
        groups.append(dict(topic=topic, mode=mode, ids=members, active_edges=len(accepted)))
    # Preserve any independently authored links already using the canonical field.
    for identifier in ids:
        for target in cards[identifier].get('related_problem_ids', []):
            if target in ids and target != identifier:
                edges.add(tuple(sorted((identifier, target))))
    rejected_path = HERE / 'rejected_pairs.json'
    rejected = json.loads(rejected_path.read_text()) if rejected_path.exists() else []
    edges.difference_update(tuple(sorted(pair)) for pair in rejected)
    neighbors = {identifier: set() for identifier in ids}
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    legacy = []
    for identifier in ids:
        c = cards[identifier]
        for target in ([x for x in c.get('related', []) if isinstance(x, str)]
                       + c.get('related_catalogue_ids', [])
                       + [x['id'] for x in c.get('problem_relations', [])]):
            outcome = ('inactive_target' if target not in ids else
                       'retained' if tuple(sorted((identifier, target))) in edges else
                       'not_retained_after_review')
            legacy.append(dict(source=identifier, target=target, outcome=outcome))
    # Retain the original migration audit after legacy fields have been cleaned.
    known_legacy = {(x['source'], x['target']) for x in legacy}
    for entry in previous.get('legacy_links', []):
        if (entry['source'], entry['target']) not in known_legacy:
            outcome = ('inactive_target' if entry['target'] not in ids else
                       'retained' if tuple(sorted((entry['source'], entry['target']))) in edges else
                       'not_retained_after_review')
            legacy.append({**entry, 'outcome': outcome})
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    changed = []
    preserved = []
    deleted_path = ROOT / 'data/deleted_records.json'
    deleted_stamp = deleted_path.stat().st_mtime_ns
    for identifier in sorted(ids):
        path = paths[identifier]
        # Read immediately before writing: concurrent editorial changes own all
        # other fields, and a removed record must never be recreated.
        if not path.exists():
            raise RuntimeError('Active set changed; rerun before applying the review')
        raw = path.read_text()
        c = json.loads(raw)
        if deleted_path.stat().st_mtime_ns != deleted_stamp:
            deleted = json.loads(deleted_path.read_text())
            deleted_stamp = deleted_path.stat().st_mtime_ns
        if not active(c, deleted):
            raise RuntimeError('Active set changed; rerun before applying the review')
        before = {k: v for k, v in c.items()
                  if k not in {'related', 'related_catalogue_ids', 'related_problem_ids', 'updated_at'}}
        targets = sorted(neighbors[identifier])
        literature = [x for x in c.get('related', []) if not isinstance(x, str)]
        needs_change = (c.get('related_problem_ids', []) != targets
                        or c.get('related', []) != literature or 'related_catalogue_ids' in c)
        if not needs_change:
            continue
        c['related_problem_ids'] = targets
        if 'related' in c:
            c['related'] = literature
        c.pop('related_catalogue_ids', None)
        c['updated_at'] = now
        after = {k: v for k, v in c.items()
                 if k not in {'related', 'related_catalogue_ids', 'related_problem_ids', 'updated_at'}}
        assert before == after
        preserved.append(dict(id=identifier, content_sha256=hashlib.sha256(
            json.dumps(before, sort_keys=True).encode()).hexdigest()))
        if '--apply' in sys.argv:
            if path.read_text() != raw:
                raise RuntimeError(f'{identifier} changed concurrently; retry')
            temporary = path.with_suffix('.related-writing')
            temporary.write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
            temporary.replace(path)
        changed.append(identifier)
    histogram = collections.Counter(len(n) for n in neighbors.values())
    report = dict(
        reviewed_on=now, initial_active_count=1973, active_count=len(ids),
        scope='Catalogue-wide editorial screening of titles, available question text and summaries; '
              'selected definitions and source checks. Not a complete proof or open-status audit.',
        unique_edges=len(edges), mean_neighbors=2 * len(edges) / len(ids),
        linked_cards=sum(bool(n) for n in neighbors.values()),
        isolated_cards=histogram[0], degree_histogram=dict(sorted(histogram.items())),
        cross_category_edges=sum(cards[a]['area'] != cards[b]['area'] for a, b in edges),
        hubs=[dict(id=i, degree=len(neighbors[i])) for i in
              sorted(ids, key=lambda i: (-len(neighbors[i]), i))[:20]],
        screened_active_ids=sorted(ids),
        reviewed_group_ids_removed_during_work=sorted(removed_during_review),
        groups=groups, legacy_links=legacy,
        changed_ids=sorted(set(changed) | set(previous.get('changed_ids', []))),
        unchanged_content=list({x['id']: x for x in
            previous.get('unchanged_content', []) + preserved}.values()),
        rejected_pairs=rejected,
    )
    if '--apply' in sys.argv:
        (HERE / 'audit.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in (
        'active_count', 'unique_edges', 'mean_neighbors', 'linked_cards',
        'isolated_cards', 'cross_category_edges', 'degree_histogram')}, indent=2))
    print('Changed cards:', len(changed))


if __name__ == '__main__':
    main()
