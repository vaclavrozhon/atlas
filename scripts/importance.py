"""Editorial importance, independent of publication date and review status."""
import collections
from benchmark_selection import QUOTAS, LABELS, apply_focus, update_benchmarks

METHOD = ('Importance ordering is an editorial assessment of foundational significance, '
          'breadth of consequences, and influence on other questions. Each assessed '
          'card gives a reason. The category-wide review also uses shared priority '
          'bands for questions of comparable scope; it does not claim that these '
          'ties have a scientifically meaningful internal order. Unassessed drafts '
          'share a provisional score of 50; '
          'their relative order is only an ID tie-break, not an importance judgment. '
          'The first 5/2 places in each large/small category are an explicit editorial '
          'focus selection balancing importance and topical diversity. Focus ordering '
          'does not alter importance scores; remaining candidates use score and ID order. '
          'The primary target is 500 problems; Top 100 is its priority subset '
          'with secondary editorial attention. '
          'Top 100, Top 500 and the legacy Top 1000 view use the first 5/2, 25/10 '
          'and 50/20 category places respectively, all from the same ranking. '
          'Category positions include all candidates and remain fixed when filtering. '
          'Publication date, source date, and card detail do not increase importance. '
          'Records marked resolved are placed after the remaining candidates, '
          'without changing their historical importance score. Importance review '
          'does not establish that a saved question is still open.')


def importance_key(card):
    return (card.get('status') == 'resolved',
            card.get('benchmark_focus', {}).get('position', float('inf')),
            -card['importance']['score'], card['id'])


def validate_importance(value):
    if not isinstance(value, dict):
        raise ValueError('Missing individual importance assessment')
    score = value.get('score')
    if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 100:
        raise ValueError('Importance score must be an integer from 0 to 100')
    if value.get('method') != 'editorial' or not value.get('reason', '').strip():
        raise ValueError('Completed cards need an editorial importance reason')


def apply_importance(data):
    groups = collections.defaultdict(list)
    for card in data['cards']:
        value = card.get('importance')
        if value and value.get('method') == 'editorial':
            validate_importance(value)
        elif (not isinstance(value, dict) or value.get('method') != 'unassessed'
              or value.get('score') != 50 or not value.get('reason', '').strip()
              or card['evidence'] == 'reviewed'):
            raise ValueError(f"{card['id']}: invalid saved importance assessment")
        groups[card['area']].append(card)
    apply_focus(data)
    for cards in groups.values():
        cards.sort(key=importance_key)
        for rank, card in enumerate(cards, 1):
            card['importance_rank'] = rank
            card['importance_count'] = len(cards)
    area_order = {a['area']: i for i, a in enumerate(data['areas'])}
    data['cards'].sort(key=lambda c: (area_order.get(c['area'], len(area_order)), c['importance_rank']))
    for area in data['areas']:
        area['importance_assessed'] = sum(c['importance']['method'] == 'editorial' for c in groups[area['area']])
        area['importance_provisional'] = area['count'] - area['importance_assessed']
    data['meta']['importance'] = dict(version=3, default_sort='importance',
        categories=len(data['areas']), resolved_last=True,
        assessed=sum(c['importance']['method'] == 'editorial' for c in data['cards']),
        provisional=sum(c['importance']['method'] == 'unassessed' for c in data['cards']))
    data['meta']['methodology'] = [p for p in data['meta'].get('methodology', [])
        if not p.startswith('Importance ordering is')]
    data['meta']['methodology'].append(METHOD)
    update_benchmarks(data)


def ranking_exports(data):
    """A compact full ranking and a human-readable review of all named categories."""
    area_labels = {a['area']: a.get('label', a['area']) for a in data['areas']}
    area_order = {a['area']: i for i, a in enumerate(data['areas'])}
    cards = sorted(data['cards'], key=lambda c: (
        area_order.get(c['area'], len(area_order)), c['importance_rank']))
    rows = [dict(area=c['area'], area_label=area_labels.get(c['area'], c['area']),
        position=c['importance_rank'], id=c['id'],
        title=c['title'], score=c['importance']['score'],
        assessment=c['importance']['method'], status=c['status'],
        reason=c['importance']['reason'], focus_topic=c.get('benchmark_focus', {}).get('topic', ''),
        focus_reason=c.get('benchmark_focus', {}).get('reason', '')) for c in cards]
    lines = [f"# Importance order in all {len(data['areas'])} categories", '', METHOD, '',
        f"{data['meta']['importance']['assessed']:,} records have an editorial importance "
        f"assessment; {data['meta']['importance']['provisional']:,} remain provisional.", '',
        'The full ordered candidate list, with reasons and statuses, is in '
        '[importance-ranking.csv](importance-ranking.csv). Below are the first '
        'ten candidates in each category. The focus prefix balances importance and '
        'diversity; full decisions are in [benchmark-selection.md](benchmark-selection.md).', '']
    def md(text):
        return str(text).replace('\\', '\\\\').replace('|', '\\|').replace('[', '\\[').replace(']', '\\]').replace('\n', ' ')
    for area in data['areas']:
        targets = '; '.join(f"{LABELS[name]}{' (legacy view)' if name == 'top1000' else ''}: {quotas[area['group']]}"
                            for name, quotas in QUOTAS.items())
        lines.extend([f"## {area['position']}. {area_labels[area['area']]} ({area['group']})", '',
            f"{targets}; candidates: {area['count']}; importance assessed: "
            f"{area['importance_assessed']}; provisional: {area['importance_provisional']}.", '',
            '| Category position | Problem | Editorial priority |', '| --- | --- | --- |'])
        selected = [c for c in cards if c['area'] == area['area']
                    and c['status'] != 'resolved'][:10]
        for c in selected:
            lines.append(f"| {c['importance_rank']} | [{md(c['title'])}](index.html#{c['id']}) | {c['importance']['score']} |")
        lines.append('')
    return rows, '\n'.join(lines)
