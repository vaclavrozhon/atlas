"""Publish the frozen, manually screened small-bucket decisions as a reversible archive.

This script applies editorial decisions; it does not infer importance from scores,
publication age, question length or keywords. Reinstatement uses the batch's restore.py.
"""
import collections
import datetime
import fcntl
import gzip
import hashlib
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from publish import _publish, atomic, csvtext
from taxonomy import BIG, SMALL

HERE = BASE / 'to_delete/small-buckets-20260910'
BASIS = ('Editorial triage of saved questions and source topics, with a second pass over '
         'ambiguous retained passages and landmark candidates; not a complete current-status '
         'review, semantic deduplication or final selection of 20 per category.')


def read(name):
    return json.loads((HERE / name).read_text())


def write_json(name, value):
    atomic(HERE / name, json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def target(card):
    formulation = card.get('source_formulation', {})
    if isinstance(formulation, dict) and formulation.get('text'):
        return formulation['text']
    return card.get('formal') or card['title']


def main():
    with (BASE / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if (HERE / 'manifest.json').exists():
            raise SystemExit('This batch already exists. Edit/reinstate its decisions explicitly; do not overwrite the frozen archive.')
        data = json.loads((BASE / 'site/catalog.json').read_text())
        current = {c['id']: c for c in data['cards']}
        original, late = read('review-input.json'), read('late-additions.json')
        reviewed = original + late
        reviewed_ids = {c['id'] for c in reviewed}
        assert len(reviewed_ids) == len(reviewed), 'Repeated review IDs'
        active_small = {c['id'] for c in data['cards'] if c.get('selection_group') == 'small'}
        assert active_small == reviewed_ids, dict(unreviewed=sorted(active_small-reviewed_ids),
                                                 moved=sorted(reviewed_ids-active_small))
        decisions = read('editorial-decisions.json')
        adjustments = read('adjustments.json')
        late_keep = set(read('late-decisions.json')['keep'])
        original_ids = {c['id'] for c in original}
        assert adjustments.keys() <= reviewed_ids
        # A concurrently completed canonical review may not have been published yet.
        protected = {json.loads(p.read_text()).get('id') for p in (BASE / 'cards').glob('*.json')}
        large_manifest = json.loads((BASE / 'to_delete/large-buckets-20260910/manifest.json').read_text())
        assert not reviewed_ids.intersection(large_manifest['records']), 'Overlapping pruning batches'

        all_rows, removed_cards, records = [], [], {}
        before, remaining, reasons = collections.Counter(), collections.Counter(), collections.Counter()
        concurrent_protected = []
        for snapshot in reviewed:
            card = current[snapshot['id']]
            identifier, category = card['id'], snapshot['area']
            assert card['area'] == category, (identifier, 'Category changed during review')
            plan = decisions[str(SMALL.index(category) + 1)]
            keep_ids = plan['keep'] if identifier in original_ids else late_keep
            keep = (str(int(identifier.split('-')[1])) in keep_ids or
                    snapshot.get('evidence') == 'reviewed' or bool(snapshot.get('proposal_import')))
            adjustment = adjustments.get(identifier)
            if adjustment:
                keep = adjustment['decision'] == 'keep'
            protect = card.get('evidence') == 'reviewed' or card.get('proposal_import') or identifier in protected
            if protect and not keep:
                concurrent_protected.append(identifier)
            keep = bool(keep or protect)
            before[category] += 1
            remaining[category] += keep
            if keep:
                code = 'retained_foundational_or_broad'
                reason = plan['focus']
                if protect:
                    code = 'retained_reviewed_or_approved'
                    reason = ('Preserve the individually reviewed card or previously approved fundamental '
                              'proposal. This pruning pass does not reverse its existing importance assessment.')
                elif adjustment:
                    code, reason = adjustment['reason_code'], adjustment['reason']
            elif adjustment:
                code, reason = adjustment['reason_code'], adjustment['reason']
            elif card.get('textbook_import', {}).get('kind') == 'research_direction':
                code = 'research_direction'
                reason = ('The dated source records a broad research direction or request to extend techniques. '
                          'It is lower priority than the retained concrete central problems. ' + plan['cut_reason'])
            else:
                code, reason = 'lower_editorial_priority', plan['cut_reason']
            saved = ' '.join(target(card).split())
            if not keep:
                reason += ' Saved target: “' + saved[:650] + ('…' if len(saved) > 650 else '') + '”.'
                entry = dict(state='quarantined', category=category, reason_code=code,
                             reason=reason, decided_on='2026-09-10', decision_basis=BASIS)
                for key in ('duplicate_of', 'decision_references'):
                    if adjustment and key in adjustment:
                        entry[key] = adjustment[key]
                records[identifier] = entry
                removed_cards.append(card)
                reasons[code] += 1
            reference = next((r for r in card.get('references', []) if r.get('id') == 'primary'),
                             next(iter(card.get('references', [])), {}))
            all_rows.append(dict(id=identifier, title=card['title'], category=category,
                decision='retained' if keep else 'quarantined', reason_code=code, reason=reason,
                saved_target=target(card), source_url=reference.get('url', ''),
                source_locator=reference.get('locator', ''), evidence=card.get('evidence', ''),
                importance_score=card.get('importance', {}).get('score', ''),
                review_cohort='original' if identifier in original_ids else 'concurrent_source_import',
                decision_references='; '.join((adjustment or {}).get('decision_references', []))))

        assert 900 <= sum(remaining.values()) <= 1200, 'Unexpected final candidate count'
        assert 'TCS-6685' not in records, 'BB(6) must remain a candidate'
        assert not set(records).intersection(protected), 'A completed review would be quarantined'
        for entry in records.values():
            duplicate = entry.get('duplicate_of')
            if duplicate:
                assert duplicate in current and duplicate not in records
                assert not current[duplicate].get('scope_exclusion')
        category_counts = [dict(category=b, before=before[b], removed=before[b]-remaining[b],
                                remaining=remaining[b]) for b in SMALL]
        fields = list(all_rows[0])
        # Archive and inspection files are committed before the manifest enables exclusion.
        snapshot_bytes = json.dumps(data, ensure_ascii=False, separators=(',', ':')).encode()
        (HERE / 'catalog-before.json.gz').write_bytes(gzip.compress(snapshot_bytes, mtime=0))
        write_json('records.json', removed_cards)
        atomic(HERE / 'all-reviewed.csv', csvtext(all_rows, fields))
        atomic(HERE / 'decisions.csv', csvtext([r for r in all_rows if r['decision'] == 'quarantined'], fields))
        manifest = dict(schema_version=1, review_id=HERE.name, date='2026-09-10',
            created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
            source_version=data['meta']['version'], source_total=len(data['cards']),
            reviewed_small_count=len(reviewed), baseline_small_count=len(original),
            concurrent_small_additions=len(late), provisional_removed=len(records),
            small_remaining=sum(remaining.values()), category_counts=category_counts,
            reason_counts=dict(reasons), concurrent_review_protection=concurrent_protected,
            archive_file='records.json',
            archive_sha256=hashlib.sha256((HERE / 'records.json').read_bytes()).hexdigest(),
            decision_basis=BASIS, records=records)
        write_json('summary.json', {k: v for k, v in manifest.items() if k != 'records'})
        lines = [
            '# Preliminary pruning of the 25 small categories — 10 September 2026', '',
            f'**{len(reviewed):,} candidates → {sum(remaining.values()):,} retained; '
            f'{len(records):,} provisionally quarantined.**', '',
            f'The first snapshot contained {len(original):,} small-category candidates. '
            f'A concurrent textbook/survey import added {len(late):,}; those questions were also screened. '
            'The final count refers to the candidate pool of all 25 small categories, not to the whole atlas. '
            'This pass does not change the decisions of the separate large-category batch.', '',
            'The review prioritizes central computational barriers, general decision problems, major conjectures '
            'and broad algorithmic primitives. Lower-priority variants, paper-specific follow-ups, requests for '
            'alternative methods, vague directions and extraction fragments were provisionally removed. '
            'Saved questions/source topics were read category by category, followed by an excerpt audit of '
            'ambiguous retained records and a rescue pass for landmark topics. Existing individually reviewed '
            'cards and approved fundamental proposals were preserved. There was no score cutoff, age cutoff '
            'or requirement to keep the same fraction of every category.', '',
            'These are editorial importance decisions, not completed open-status reviews or a guarantee that '
            'every survivor belongs in the final top 1,000. Quotas of 20 per small category have not been applied. '
            'A short card or an incomplete formulation alone was not a reason to discard a major problem. '
            'Semantic deduplication and exact comparisons between overlapping formulations remain incomplete.', '',
            '| Category | Before | Quarantined | Retained |',
            '|---|---:|---:|---:|',
        ]
        lines += [f"| {r['category']} | {r['before']} | {r['removed']} | {r['remaining']} |" for r in category_counts]
        lines += [f'| **Total** | **{len(reviewed)}** | **{len(records)}** | **{sum(remaining.values())}** |', '',
            '## Files and reversibility', '',
            '- `records.json`: full pre-removal records, including statements, references, source notes, stable IDs and original subjects.',
            '- `manifest.json`: live quarantine decisions with individual reasons and previous selection categories. Only `state: "quarantined"` excludes an entry.',
            '- `decisions.csv`: searchable removal ledger, including the saved target and source locator.',
            '- `all-reviewed.csv`: all retained and quarantined decisions, including the later source imports.',
            '- `catalog-before.json.gz`: complete catalogue immediately before this batch was applied.',
            '- `review-input.json`, `late-additions.json`, `editorial-decisions.json`, `late-decisions.json`, `adjustments.json` and audit text files: the frozen review inputs and reasoning.', '',
            'The default UI omits quarantined records. The Selection scope filter and direct stable-ID links '
            'still expose them with the removal reason. Full exports retain them, and browser notes/bookmarks '
            'remain attached to the same IDs. No source, canonical card, reference or mathematical status field '
            'was deleted or overwritten by the pruning mechanism.', '',
            'To restore one or more records without overwriting any later editorial improvements:', '',
            '```bash',
            'python3 atlas/to_delete/small-buckets-20260910/restore.py TCS-1165 --dry-run',
            'python3 atlas/to_delete/small-buckets-20260910/restore.py TCS-1165',
            'python3 atlas/to_delete/small-buckets-20260910/restore.py --all',
            '```', '',
            'Run from the repository root. The script updates this manifest and republishes under the shared '
            'publication lock; it does not copy stale text back from the snapshot. The table above records '
            'the original decision, while later restorations are recorded in the manifest.', '',
            '## Two individually checked historical targets', '',
            'TCS-6720 asks for a constant-factor approximation for asymmetric metric TSP; '
            '[Svensson, Tarnawski and Végh](https://arxiv.org/abs/1708.04215) supplied one. '
            'TCS-7115 states the finite-template CSP dichotomy; '
            '[Bulatov](https://arxiv.org/abs/1703.03021) proved it (independently also Zhuk). '
            'These dated source records were archived with explicit resolution references in the decision '
            'ledger; their original status fields remain preserved. This spot check is not an exhaustive '
            'audit of the present status of the other questions.', '',
        ]
        atomic(HERE / 'README.md', '\n'.join(lines))
        write_json('manifest.json', manifest)
        _publish()
        published = json.loads((BASE / 'site/catalog.json').read_text())
        after_small = {c['id'] for c in published['cards'] if c.get('selection_group') == 'small'}
        assert after_small == reviewed_ids-records.keys(), 'Published small pool differs from decisions'
        old_large = {c['id'] for c in data['cards'] if c.get('selection_group') == 'large'}
        new_large = {c['id'] for c in published['cards'] if c.get('selection_group') == 'large'}
        assert old_large == new_large, 'Large-category membership changed during publication'
        assert set(current) == {c['id'] for c in published['cards']}, 'Catalogue IDs changed'
        print(json.dumps(dict(before=len(reviewed), retained=len(after_small), quarantined=len(records),
                              large_unchanged=len(new_large), archive=str(HERE)), indent=2))


if __name__ == '__main__':
    main()
