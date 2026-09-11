"""Editorial importance, independent of publication date and review status."""
import collections
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
METHOD = ('Importance ordering is an editorial assessment of foundational significance, '
          'breadth of consequences, and influence on other questions. Each assessed '
          'card gives a reason. The category-wide review also uses shared priority '
          'bands for questions of comparable scope; it does not claim that these '
          'ties have a scientifically meaningful internal order. Unassessed drafts '
          'share a provisional score of 50; '
          'their relative order is only an ID tie-break, not an importance judgment. '
          'Category positions include all candidates and remain fixed when filtering. '
          'Publication date, source date, and card detail do not increase importance. '
          'Records marked resolved are placed after the remaining candidates, '
          'without changing their historical importance score. Importance review '
          'does not establish that a saved question is still open.')


def importance_key(card):
    return (card.get('status') == 'resolved', -card['importance']['score'], card['id'])


def validate_importance(value):
    if not isinstance(value, dict):
        raise ValueError('Missing individual importance assessment')
    score = value.get('score')
    if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 100:
        raise ValueError('Importance score must be an integer from 0 to 100')
    if value.get('method') != 'editorial' or not value.get('reason', '').strip():
        raise ValueError('Completed cards need an editorial importance reason')


def apply_importance(data):
    category_path = BASE / 'importance_category_review.json'
    overrides = json.loads(category_path.read_text()) if category_path.exists() else {}
    overrides_path = BASE / 'importance_overrides.json'
    # Specific follow-up assessments supersede the category-wide scope review;
    # canonical detailed cards take precedence over both draft overlays.
    if overrides_path.exists():
        overrides.update(json.loads(overrides_path.read_text()))
    ids = {c['id'] for c in data['cards']}
    if overrides.keys() - ids:
        raise ValueError('Importance override targets an unknown record')
    groups = collections.defaultdict(list)
    for card in data['cards']:
        if card['evidence'] == 'reviewed':
            validate_importance(card.get('importance'))
        elif card['id'] in overrides:
            validate_importance(overrides[card['id']])
            card['importance'] = dict(overrides[card['id']])
        elif card.get('proposal_import'):
            validate_importance(card.get('importance'))
        else:
            card['importance'] = dict(score=50, method='unassessed',
                reason='Importance has not been individually assessed. This draft '
                       'shares the provisional midpoint with other unassessed drafts; '
                       'its position is not evidence that the question is less important.')
        groups[card['area']].append(card)
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
    data['meta']['importance'] = dict(version=2, default_sort='importance',
        categories=len(data['areas']), resolved_last=True,
        assessed=sum(c['importance']['method'] == 'editorial' for c in data['cards']),
        provisional=sum(c['importance']['method'] == 'unassessed' for c in data['cards']))
    data['meta']['methodology'] = [p for p in data['meta'].get('methodology', [])
        if not p.startswith('Importance ordering is')]
    data['meta']['methodology'].append(METHOD)


def ranking_exports(data):
    """A compact full ranking and a human-readable review of all named categories."""
    rows = [dict(area=c['area'], position=c['importance_rank'], id=c['id'],
        title=c['title'], score=c['importance']['score'],
        assessment=c['importance']['method'], status=c['status'],
        reason=c['importance']['reason']) for c in data['cards']]
    lines = [f"# Importance order in all {len(data['areas'])} categories", '', METHOD, '',
        f"{data['meta']['importance']['assessed']:,} records have an editorial importance "
        f"assessment; {data['meta']['importance']['provisional']:,} remain provisional.", '',
        'The full ordered candidate list, with reasons and statuses, is in '
        '[importance-ranking.csv](importance-ranking.csv). Below are the first '
        'ten assessed candidates in each category. Selection targets are unchanged.', '']
    def md(text):
        return str(text).replace('\\', '\\\\').replace('|', '\\|').replace('[', '\\[').replace(']', '\\]').replace('\n', ' ')
    for area in data['areas']:
        lines.extend([f"## {area['position']}. {area['area']} ({area['group']})", '',
            f"Target: {area['target']}; candidates: {area['count']}; importance assessed: "
            f"{area['importance_assessed']}; provisional: {area['importance_provisional']}.", '',
            '| Category position | Problem | Editorial priority |', '| --- | --- | --- |'])
        selected = [c for c in data['cards'] if c['area'] == area['area']
                    and c['importance']['method'] == 'editorial' and c['status'] != 'resolved'][:10]
        for c in selected:
            lines.append(f"| {c['importance_rank']} | [{md(c['title'])}](index.html#{c['id']}) | {c['importance']['score']} |")
        lines.append('')
    return rows, '\n'.join(lines)
