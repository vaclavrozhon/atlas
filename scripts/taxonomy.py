"""Publish the categories explicitly assigned in canonical problem cards."""

import collections

from categories import BIG, SMALL, NAMES, CATEGORIES, BY_KEY
from card_activity import read_inactive
from benchmark_selection import GOAL


def apply_taxonomy(data):
    inactive = read_inactive()
    data['cards'] = [card for card in data['cards'] if card['id'] not in inactive]
    counts, adds, reviewed = (collections.Counter() for _ in range(3))
    for card in data['cards']:
        area = card['area']
        if area not in BY_KEY:
            raise ValueError(f"{card['id']}: unknown category {area}")
        if card.get('scope_exclusion'):
            raise ValueError(f"{card['id']}: archive this card with scripts/archive_cards.py")
        definition = BY_KEY[area]
        card.setdefault('original_area', area)
        card.setdefault('category_assignment', {'method': 'editorial_topic', 'reason': 'Assigned in the canonical card.'})
        card.update(selection_group=definition['group'], selection_target=definition['target'])
        counts[area] += 1
        adds[area] += bool(card.get('is_new'))
        reviewed[area] += card['evidence'] == 'reviewed'
    total = len(data['cards'])
    data['areas'] = [dict(category, count=counts[category['area']],
        reviewed=reviewed[category['area']], before=counts[category['area']]-adds[category['area']],
        added=adds[category['area']], after_pct=100*counts[category['area']]/total if total else 0)
        for category in CATEGORIES]
    assigned = sum(category['target'] for category in CATEGORIES)
    reserved = max(0, 1000-assigned)
    data['meta']['taxonomy'] = dict(version='selection-v11', large_groups=len(BIG),
        small_groups=len(SMALL), vacant_small_groups=reserved//20,
        assigned_target=assigned, reserved_target=reserved, target_total=assigned+reserved,
        target_status='legacy_view',
        candidate_count=total, inactive_count=len(inactive),
        assignment_counts=dict(collections.Counter(c['category_assignment']['method'] for c in data['cards'])))
    methodology = [p for p in data['meta'].get('methodology', []) if not p.startswith('Selection groups follow')]
    methodology.append(
        f'Selection groups follow the agreed {len(BIG)} large and {len(SMALL)} small categories. '
        + GOAL + ' '
        'The respective prefixes are 5/2, 25/10 and 50/20 problems per large/small category. '
        f'The legacy Top 1000 view has {assigned} assigned places '
        f'and {reserved} reserved places. '
        'Each card records its category explicitly. These counts describe saved candidates; '
        'classification does not verify a statement or its current open status. '
        'Inactive records are archived outside the catalogue, exports and editorial work. '
        'Their content, stable IDs and reasons are retained; imports cannot reactivate them. '
        'Final quota selection and a comprehensive deduplication audit remain pending.')
    data['meta']['methodology'] = methodology
    return data
