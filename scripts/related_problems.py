"""Publish an undirected graph of editorially related active problems."""

import re


def is_active(card):
    return not card.get('scope_exclusion') and card['status'] not in {'resolved', 'excluded'}


def apply_related_problems(cards, deleted=()):
    by_id = {card['id']: card for card in cards}
    active = {identifier for identifier, card in by_id.items() if is_active(card)}
    neighbors = {identifier: set() for identifier in active}
    for card in cards:
        identifier = card['id']
        targets = card.get('related_problem_ids', [])
        if not isinstance(targets, list) or any(
            not isinstance(target, str) or not re.fullmatch(r'TCS-\d{4,}', target)
            for target in targets
        ):
            raise ValueError(f'{identifier}: related_problem_ids must be a list of problem IDs')
        if len(targets) != len(set(targets)) or identifier in targets:
            raise ValueError(f'{identifier}: duplicate or self-referencing related problem')
        for target in targets:
            if target not in by_id and target not in deleted:
                raise ValueError(f'{identifier}: unknown related problem {target}')
            # Deleting or retiring a card also removes every incoming reader link.
            if identifier in active and target in active:
                neighbors[identifier].add(target)
                neighbors[target].add(identifier)
    for card in cards:
        card['related_problem_ids'] = sorted(neighbors.get(card['id'], ()))
