"""Editorial focus prefixes and nested benchmark exports."""

import json
from paths import DATA

BASE = DATA
QUOTAS = {'top100': {'large': 5, 'small': 2},
          'top500': {'large': 25, 'small': 10},
          'top1000': {'large': 50, 'small': 20}}
LABELS = {'top100': 'Top 100', 'top500': 'Top 500', 'top1000': 'Top 1000'}
GOAL = ('Our primary goal is a benchmark of 500 problems. Top 100 is a priority '
        'subset of those same 500, with secondary editorial attention. Both use '
        'the same category order and the same ranking within each category. '
        'The existing Top 1000 view is not an active benchmark goal.')


def eligible(card):
    return not card.get('scope_exclusion') and card['status'] not in ('resolved', 'excluded')


def read_selection():
    return json.loads((BASE / 'benchmark_selection.json').read_text())


def apply_focus(data):
    selection = read_selection()
    cards = {card['id']: card for card in data['cards']}
    areas = {area['area']: area for area in data['areas']}
    for card in cards.values():
        card.pop('benchmark_focus', None)
    seen, seen_areas, issues = set(), set(), []
    for review in selection['areas']:
        area = review['area']
        if area in seen_areas:
            raise ValueError(f'Duplicate focus category: {area}')
        seen_areas.add(area)
        if area not in areas:
            issues.append(f'Focus category no longer exists: {area}')
            continue
        limit = QUOTAS['top100'][areas[area]['group']]
        if len(review['selected']) > limit:
            raise ValueError(f'Too many focus selections in {area}')
        for position, entry in enumerate(review['selected'], 1):
            identifier = entry['id']
            if identifier in seen:
                raise ValueError(f'Duplicate focus ID: {identifier}')
            seen.add(identifier)
            if identifier not in cards:
                issues.append(f'Review focus replacement for removed {identifier} in {area}')
                continue
            if not entry['topic'].strip() or not entry['reason'].strip():
                raise ValueError(f'Missing focus rationale: {identifier}')
            card = cards[identifier]
            if card['area'] != area or not eligible(card):
                issues.append(f'Review focus replacement for {identifier} in {area}')
                continue
            card['benchmark_focus'] = dict(position=position, topic=entry['topic'],
                reason=entry['reason'], reviewed_on=selection['reviewed_on'])
        available = sum(c['area'] == area and eligible(c) for c in cards.values())
        selected = sum(c['area'] == area and 'benchmark_focus' in c for c in cards.values())
        if selected < min(limit, available):
            issues.append(f'Unreviewed focus places in {area}: {min(limit, available) - selected}')
    for area in areas.keys() - seen_areas:
        issues.append(f'Category needs focus review: {area}')
    data['meta']['benchmark_selection'] = dict(
        reviewed_on=selection['reviewed_on'], basis=selection['basis'],
        reviewed_categories=len(seen_areas & areas.keys()), issues=issues)


def members(data, name):
    areas = {area['area']: area for area in data['areas']}
    return [card for card in data['cards'] if eligible(card)
            and card['area'] in areas
            and card['importance_rank'] <= QUOTAS[name][areas[card['area']]['group']]]


def benchmark_summary(data, name):
    selected = members(data, name)
    quotas = QUOTAS[name]
    shortages = []
    for area in data['areas']:
        count = sum(card['area'] == area['area'] for card in selected)
        target = quotas[area['group']]
        if count < target:
            shortages.append(dict(area=area['area'], label=area['label'], target=target, selected=count,
                                  missing=target - count))
    assigned_target = sum(quotas[a['group']] for a in data['areas'])
    reserved_target = data['meta'].get('taxonomy', {}).get('vacant_small_groups', 0) * quotas['small']
    return dict(id=name, label=LABELS[name], tentative=name == 'top1000',
                quotas=quotas, total=len(selected),
                target=assigned_target + reserved_target,
                assigned_target=assigned_target, reserved_target=reserved_target,
                shortfalls=shortages)


def update_benchmarks(data):
    data['meta']['benchmarks'] = {name: benchmark_summary(data, name) for name in QUOTAS}


def selection_report(data):
    import re

    selection = read_selection()
    by_id = {card['id']: card for card in data['cards']}
    area_labels = {a['area']: a.get('label', a['area']) for a in data['areas']}
    area_order = {a['area']: i for i, a in enumerate(data['areas'])}
    reviews = {review['area']: review for review in selection['areas']}
    area_pattern = '|'.join(re.escape(key) for key in sorted(area_labels, key=len, reverse=True))
    def display_issue(issue):
        return re.sub(area_pattern, lambda match: area_labels[match.group()], issue) if area_pattern else issue
    def md(value):
        return str(value).replace('|', '\\|').replace('\n', ' ')
    lines = ['# Benchmark selection review', '',
        f"Reviewed on {selection['reviewed_on']} across {len(data['areas'])} categories.",
        '', GOAL, '', selection['basis'], '',
        'Top 100 takes the first 5/2 places in each large/small category. '
        'Top 500 takes the first 25/10 and the legacy Top 1000 view takes '
        'the first 50/20 places from the same order. Top 100 is contained in '
        'Top 500, which is contained in Top 1000. '
        'Focus places balance scientific importance and topical diversity; '
        'remaining places retain score order. None of these subsets certifies current open status.', '',
        '| Benchmark | Target | Available | Missing |', '| --- | ---: | ---: | ---: |']
    for name, summary in data['meta']['benchmarks'].items():
        label = LABELS[name] + (' (legacy view)' if summary['tentative'] else '')
        lines.append(f"| [{label}](index.html?benchmark={name}) | {summary['target']} | "
                     f"{summary['total']} | {summary['target'] - summary['total']} |")
    lines.extend(['', '## Unfilled places', ''])
    for name, summary in data['meta']['benchmarks'].items():
        if summary['reserved_target']:
            lines.append(f"- {name}: {summary['reserved_target']} places are reserved for future categories.")
        for gap in sorted(summary['shortfalls'], key=lambda gap: area_order.get(gap['area'], len(area_order))):
            lines.append(f"- {name}: {area_labels.get(gap['area'], gap['area'])} "
                         f"has {gap['selected']}/{gap['target']} places.")
    issues = data['meta']['benchmark_selection']['issues']
    if issues:
        lines.extend(['', '## Review needed after catalogue changes', ''])
        lines.extend('- ' + display_issue(issue) for issue in issues)
    focus = sorted(members(data, 'top100'), key=lambda card: card['importance_rank'])
    for area in data['areas']:
        review = reviews.get(area['area'])
        if review is None:
            continue
        lines.extend(['', '## ' + area_labels[area['area']], '', review['rationale'], '',
            'Previous prefix: ' + (', '.join(review['previous_ids']) or 'empty') + '.', '',
            '| Position | Problem | Topic | Saved importance score | Selection rationale |',
            '| ---: | --- | --- | ---: | --- |'])
        for card in focus:
            if card['area'] != review['area']:
                continue
            detail = card.get('benchmark_focus', {})
            lines.append(f"| {card['importance_rank']} | [{md(card['title'])}]"
                f"(index.html#{card['id']}) ({card['id']}) | {md(detail.get('topic', 'Needs review'))} | "
                f"{card['importance']['score']} | {md(detail.get('reason', 'Unreviewed replacement'))} |")
        considered = [identifier for identifier in review['considered_ids'] if identifier in by_id]
        lines.extend(['', 'Candidates considered: ' + ', '.join(considered) + '.'])
    return '\n'.join(lines) + '\n'


def write_exports(site, data, atomic):
    for name in QUOTAS:
        payload = dict(meta=data['meta'], areas=data['areas'], subbenchmark=data['meta']['benchmarks'][name],
                       cards=members(data, name))
        atomic(site / (name + '.json'), json.dumps(payload, ensure_ascii=False, indent=2))
    # Solver-facing statements keep definitions and unfinished-formulation flags,
    # without explanatory context, progress notes or research advice.
    fields = ('id', 'title', 'area', 'question_type', 'formal', 'definitions',
              'answer_criterion', 'status', 'status_note', 'statement_review', 'references')
    statements = [{key: card[key] for key in fields if key in card}
                  for card in members(data, 'top100')]
    atomic(site / 'top100-statements.json', json.dumps({
        'subbenchmark': data['meta']['benchmarks']['top100'],
        'scope': 'Statements and definitions. Formulation review does not certify current openness or proof-assistant formalization.',
        'cards': statements,
    }, ensure_ascii=False, indent=2))
    atomic(site / 'benchmark-selection.md', selection_report(data))
