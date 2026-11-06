"""Validate explicitly assessed historical metadata, independently of source dates."""
import datetime


def validate_origin(origin):
    if not isinstance(origin, dict):
        raise ValueError('problem_origin must be an object')
    precision = origin.get('precision')
    if precision not in {'year', 'circa', 'range', 'by', 'unknown'}:
        raise ValueError('invalid problem origin precision')
    reviewed = datetime.date.fromisoformat(origin['reviewed_on'])
    year = origin.get('year')
    if precision == 'unknown':
        if year is not None:
            raise ValueError('unknown origin cannot assert a year')
    elif type(year) is not int or not 1000 <= year <= reviewed.year:
        raise ValueError('invalid problem origin year')
    end = origin.get('end_year')
    if precision == 'range':
        if type(end) is not int or not year <= end <= reviewed.year:
            raise ValueError('invalid problem origin range')
    elif end is not None:
        raise ValueError('end_year requires range precision')
    if not isinstance(origin.get('note'), str) or not origin['note'].strip():
        raise ValueError('problem origin requires an explanation')
    refs = origin.get('references')
    if not isinstance(refs, list) or (not refs and precision != 'unknown'):
        raise ValueError('dated problem origin requires sources')
    for ref in refs:
        if not isinstance(ref, dict) or not ref.get('title') or not ref.get('url', '').startswith(('https://', 'http://')):
            raise ValueError('invalid problem origin reference')
