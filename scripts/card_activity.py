"""Active cards are editable inputs; inactive cards are preserved in the archive.

Ordinary consumers read only the small archive index and filenames, never the
archived card contents. Directory placement is the activity state; a card's
scientific status (open, uncertain, resolved, etc.) is a separate property.
"""

import json
import re
import datetime

from paths import CARDS, ARCHIVE, ARCHIVED_CARDS

INDEX = ARCHIVE / 'index.json'


def eligible_candidate(card):
    """Scientific resolution after the benchmark cutoff does not retire a card."""
    if card.get('scope_exclusion') or card.get('status') == 'excluded':
        return False
    if card.get('status') != 'resolved':
        return True
    record = card.get('benchmark_eligibility', {})
    if record.get('cutoff') != '2026-01-01' or record.get('open_at_cutoff') is not True:
        return False
    try:
        date = datetime.date.fromisoformat(record.get('resolution_first_public_on', ''))
    except (TypeError, ValueError):
        return False
    return (date >= datetime.date(2026, 1, 1)
            and date <= datetime.date.today()
            and bool(record.get('source_url', '').startswith(('https://', 'http://')))
            and bool(record.get('reason', '').strip()))


def read_inactive():
    records = json.loads(INDEX.read_text())
    if not isinstance(records, dict) or any(
        not re.fullmatch(r'TCS-\d{4,}', identifier)
        or not isinstance(reason, str) or not reason.strip()
        for identifier, reason in records.items()
    ):
        raise ValueError('Inactive records must map stable IDs to nonempty reasons')
    # An archived file also reserves its identity if an index entry is missing.
    # Do not open it: old content need not satisfy today's authoring schema.
    for path in ARCHIVED_CARDS.glob('TCS-*.json'):
        if not re.fullmatch(r'TCS-\d{4,}', path.stem):
            raise ValueError(f'Invalid archived card filename: {path.name}')
        records.setdefault(path.stem, 'Archived card; disposition not recorded in the index.')
    return records


def active_card_paths():
    inactive = read_inactive()
    return [path for path in sorted(CARDS.glob('*.json')) if path.stem not in inactive]
