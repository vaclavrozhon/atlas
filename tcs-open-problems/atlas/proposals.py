"""Seed approved research drafts without overwriting subsequent card reviews."""
import copy
import json
from pathlib import Path

from importance import validate_importance
from taxonomy import NAMES

PROPOSALS = Path(__file__).with_name('proposals')


def apply_proposals(data, registry, now, directory=PROPOSALS):
    existing = {c['id']: c for c in data['cards']}
    maximum = max(int(value.split('-')[-1]) for value in
                  list(registry.values()) + list(existing))
    seen = set()
    for path in sorted(directory.glob('*.json')):
        batch = json.loads(path.read_text())
        if not batch.get('approved_on') or not batch.get('approval_basis'):
            raise ValueError(f'{path}: missing publication authorization')
        for draft in batch['cards']:
            key = 'proposal:' + draft['key']
            if key in seen:
                raise ValueError(f'Duplicate proposal key: {key}')
            seen.add(key)
            for field in ['title', 'formal', 'context', 'why', 'references',
                          'status_note', 'review_note', 'proposal_import']:
                if not draft.get(field):
                    raise ValueError(f'{key}: missing {field}')
            if draft.get('area') not in NAMES:
                raise ValueError(f'{key}: unknown proposal category')
            if draft.get('evidence') != 'source' or draft.get('model_self_contained') is not False:
                raise ValueError(f'{key}: proposals must remain unfinished source drafts')
            if draft.get('criterion') not in data['criteria']:
                raise ValueError(f'{key}: unknown criterion')
            validate_importance(draft.get('importance'))
            refs = draft['references']
            if len({r['id'] for r in refs}) != len(refs):
                raise ValueError(f'{key}: duplicate reference IDs')
            if any(not r.get('title') or not r.get('url', '').startswith('https://') for r in refs):
                raise ValueError(f'{key}: invalid reference')
            if key not in registry:
                maximum += 1
                registry[key] = f'TCS-{maximum:04d}'
            identifier = registry[key]
            # Canonical detailed cards and individual draft corrections may
            # already have developed this proposal. Never reset their content.
            if identifier in existing:
                continue
            card = copy.deepcopy(draft)
            card.update(id=identifier, is_new=True, published_at=now, updated_at=now,
                        rank=20000 + maximum,
                        criterion_label=data['criteria'][card['criterion']]['label'])
            data['cards'].append(card)
            existing[identifier] = card
    return data
