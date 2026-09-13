"""Local reading aid and checked application of individually authored removals."""
import argparse
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CARDS = ROOT / 'data/cards'


def dump(path, value):
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    os.replace(temporary, path)


def read_cards():
    return {p.stem: json.loads(p.read_text()) for p in CARDS.glob('*.json')}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['start', 'read', 'apply'])
    parser.add_argument('ids', nargs='*')
    args = parser.parse_args()
    if args.action == 'start':
        if (HERE / 'baseline.json').exists():
            raise SystemExit('Baseline already exists')
        catalogue = json.loads((ROOT / 'build/catalog.json').read_text())
        dump(HERE / 'baseline.json', {
            'date': '2026-09-11',
            'count': len(list(CARDS.glob('*.json'))),
            'scope': 'First batch toward approximately 800 candidates; no category quotas or rank immunity.',
            'cards': {c['id']: {'rank': c['importance_rank'], 'area': c['area'],
                'score': c['importance']['score'], 'focus': bool(c.get('benchmark_focus'))}
                for c in catalogue['cards']},
        })
        return
    if args.action == 'read':
        path = HERE / 'read-ledger.json'
        ledger = json.loads(path.read_text()) if path.exists() else {}
        for raw in args.ids:
            identifier = raw if raw.startswith('TCS-') else 'TCS-' + raw.zfill(4)
            p = CARDS / (identifier + '.json')
            if not p.exists():
                print(identifier, 'MISSING')
                continue
            payload = p.read_bytes()
            c = json.loads(payload)
            print('\n' + identifier + ' | ' + c['title'])
            if c.get('formal') != c.get('title'):
                print('Q:', c.get('formal', ''))
            if c.get('definitions'):
                print('D:', c.get('definitions', '')[:800])
            if c.get('why') and not c['why'].startswith('The significance of this particular'):
                print('WHY:', c['why'])
            reason = c.get('importance', {}).get('reason', '')
            if reason and not reason.startswith('Importance has not') and reason != c.get('why'):
                print('IMPORTANCE:', reason)
            print('SUMMARY:', ' '.join(c.get('working_summary', {}).get('sentences', [])))
            refs = c.get('references', [])
            print('SOURCE:', '; '.join(str(r.get('title', '')) + ' ' + str(r.get('locator', '')) for r in refs[:2]))
            ledger[identifier] = {'sha256': hashlib.sha256(payload).hexdigest(),
                'date': '2026-09-11', 'read_fields': ['title', 'formal', 'definitions (first 800 characters)',
                    'why', 'importance.reason', 'working_summary', 'first two source titles and locators']}
        dump(path, ledger)
        return
    ledger = json.loads((HERE / 'read-ledger.json').read_text())
    decisions = {}
    for line in (HERE / 'decisions.tsv').read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        identifier, reason = line.split('\t', 1)
        if identifier in decisions or len(reason) < 50:
            raise ValueError('Duplicate ID or insufficient reason: ' + identifier)
        decisions[identifier] = reason
    applied_path = HERE / 'applied.json'
    prior = json.loads(applied_path.read_text()) if applied_path.exists() else {'removals': {}, 'focus_removed': [], 'batches': []}
    decisions = {i: r for i, r in decisions.items() if i not in prior['removals']}
    if not decisions:
        raise SystemExit('No pending removals')
    deleted_path = ROOT / 'data/deleted_records.json'
    deleted = json.loads(deleted_path.read_text())
    selection_path = ROOT / 'data/benchmark_selection.json'
    selection = json.loads(selection_path.read_text())
    for identifier in decisions:
        p = CARDS / (identifier + '.json')
        if identifier in deleted:
            raise ValueError('Already deleted: ' + identifier)
        if hashlib.sha256(p.read_bytes()).hexdigest() != ledger[identifier]['sha256']:
            raise ValueError('Changed since reading: ' + identifier)
    for identifier, reason in decisions.items():
        deleted[identifier] = ('Removed on 2026-09-11 in the user-authorized interest screen '
            'toward approximately 800 candidates. ' + reason +
            ' Editorial selection judgment, not a claim of resolution.')
    changed_focus = []
    for area in selection['areas']:
        removed = [e['id'] for e in area['selected'] if e['id'] in decisions]
        if removed:
            changed_focus.extend(removed)
            area['selected'] = [e for e in area['selected'] if e['id'] not in decisions]
            area['rationale'] += (' The September 11 interest screen removed ' + ', '.join(removed)
                + '; replacement focus choices remain unreviewed.')
    dump(deleted_path, deleted)
    if changed_focus:
        dump(selection_path, selection)
    for identifier in decisions:
        (CARDS / (identifier + '.json')).unlink()
    removals = prior['removals'] | {i: deleted[i] for i in decisions}
    dump(applied_path, {'date': '2026-09-11', 'count': len(removals),
        'focus_removed': prior['focus_removed'] + changed_focus, 'removals': removals,
        'batches': prior.get('batches', []) + [{'count': len(decisions), 'ids': list(decisions)}]})
    print('Removed', len(decisions), 'cards; focus removals:', changed_focus)


if __name__ == '__main__':
    main()
