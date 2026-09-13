"""Minimal deletion history shared by publication and every import route."""

import json
import re
from paths import DATA

DELETED = DATA / 'deleted_records.json'


def read_deleted():
    records = json.loads(DELETED.read_text())
    if not isinstance(records, dict) or any(
        not re.fullmatch(r'TCS-\d{4,}', identifier)
        or not isinstance(reason, str) or not reason.strip()
        for identifier, reason in records.items()
    ):
        raise ValueError('Deleted records must map stable IDs to nonempty reasons')
    return records
