"""Load display names and order while preserving historical category keys.

Edit categories.json to rename or reorder a category. Published areas carry the
same labels for the browser and exports; source imports keep their stable keys.
"""
import json
from paths import DATA

REGISTRY_PATH = DATA / 'categories.json'


def read_categories(path=REGISTRY_PATH):
    registry = json.loads(path.read_text())
    if registry.get('version') != 1:
        raise ValueError('Unsupported category registry version')
    categories = []
    ids, keys, labels, groups = set(), set(), set(), set()
    for group in registry['groups']:
        name, target = group['id'], group['target']
        if name not in {'large', 'small'} or name in groups:
            raise ValueError('Invalid or duplicate category group')
        if isinstance(target, bool) or not isinstance(target, int) or target <= 0:
            raise ValueError('Category targets must be positive integers')
        groups.add(name)
        for position, category in enumerate(group['categories'], 1):
            identifier, key = category['id'], category['key']
            label = category.get('label', key)
            if any(not isinstance(value, str) or not value.strip()
                   for value in [identifier, key, label]):
                raise ValueError('Category IDs, keys and labels must be nonempty strings')
            if identifier in ids or key in keys or label in labels:
                raise ValueError('Duplicate category ID, key or display label')
            ids.add(identifier)
            keys.add(key)
            labels.add(label)
            categories.append(dict(id=identifier, area=key, label=label,
                group=name, target=target, position=position))
    if groups != {'large', 'small'}:
        raise ValueError('The category registry needs both selection groups')
    return categories


CATEGORIES = read_categories()
BY_ID = {category['id']: category for category in CATEGORIES}
BY_KEY = {category['area']: category for category in CATEGORIES}
BIG = [category['area'] for category in CATEGORIES if category['group'] == 'large']
SMALL = [category['area'] for category in CATEGORIES if category['group'] == 'small']
NAMES = [category['area'] for category in CATEGORIES]


def category_key(identifier):
    return BY_ID[identifier]['area']


def category_label(key):
    return BY_KEY.get(key, {}).get('label', key)
