"""Helpers for individually assessed problem origins; no inferred default dates."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RECORDS = HERE / 'origins.json'
origins = json.loads(RECORDS.read_text()) if RECORDS.exists() else {}
targets = {c['id']: c for c in json.loads((HERE / 'targets.json').read_text())}
if (HERE / 'current-targets.json').exists():
    targets.update({c['id']: c for c in json.loads((HERE / 'current-targets.json').read_text())})

def card(identifier):
    identifier = identifier if identifier.startswith('TCS-') else 'TCS-' + identifier
    return json.loads((ROOT / 'data/cards' / (identifier + '.json')).read_text())

def add(identifier, year, precision, note, refs=(), *, end_year=None, sources=()):
    c = card(identifier)
    assert c['id'] in targets, c['id']
    assert precision in {'year', 'circa', 'range', 'by', 'unknown'}, precision
    assert note.strip()
    assert (year is None) == (precision == 'unknown')
    if year is not None:
        assert isinstance(year, int) and 1000 <= year <= 2026
    assert (end_year is not None) == (precision == 'range')
    if end_year is not None:
        assert year <= end_year <= 2026
    references = []
    for ident in refs:
        found = [r for r in c['references'] if r['id'] == ident]
        assert len(found) == 1, (c['id'], ident)
        references.append({k: found[0][k] for k in ('title', 'url', 'locator') if found[0].get(k)})
    for source in sources:
        assert source.get('title') and source.get('url', '').startswith(('https://', 'http://'))
        references.append(source)
    assert references or precision == 'unknown', c['id']
    result = {'year': year, 'precision': precision, 'note': note,
              'references': references, 'reviewed_on': '2026-11-06'}
    if end_year is not None:
        result['end_year'] = end_year
    origins[c['id']] = result

def save():
    RECORDS.write_text(json.dumps(dict(sorted(origins.items())), ensure_ascii=False, indent=2) + '\n')
    print(f'Individually assessed origins: {len(origins)}/{len(targets)}')

