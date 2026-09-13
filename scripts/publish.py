"""Build the reader from complete canonical cards; generated files are outputs."""

import argparse
import collections
import datetime
import fcntl
import hashlib
import json
import re
import shutil
from pathlib import Path

from paths import ROOT, DATA, WEB, BUILD
from card_schema import reader_record
from categories import BY_KEY
from catalog_exports import atomic, jsdump, write_catalog_exports, write_live_updates
from importance import apply_importance, validate_importance
from taxonomy import apply_taxonomy
from card_activity import read_inactive, active_card_paths
from related_problems import apply_related_problems

BASE, SITE, CARDS = ROOT, BUILD, DATA / 'cards'


def validate_card(card, path, criteria):
    for field in [
        'title', 'area', 'formal', 'context', 'why', 'progress', 'references',
        'criterion', 'question_type', 'answer_criterion',
    ]:
        if not card.get(field):
            raise ValueError(f'{path.name}: missing {field}')
    if card['question_type'] not in {'yes_no', 'asymptotic_complexity', 'exact_value',
                                    'numerical_value', 'function'}:
        raise ValueError(f'{path.name}: unsupported question type; see docs/RULES.md')
    if not isinstance(card['answer_criterion'], str):
        raise ValueError(f'{path.name}: answer criterion must be text')
    statement_review = card.get('statement_review')
    if statement_review:
        if statement_review.get('status') not in {'revised', 'needs_specification'}:
            raise ValueError(f'{path.name}: unknown statement review status')
        if not card.get('definitions'):
            raise ValueError(f'{path.name}: statement review requires definitions')
        if statement_review['status'] == 'needs_specification' and not statement_review.get('remaining_issue'):
            raise ValueError(f'{path.name}: unfinished formulation must identify its gap')
    if card['area'] not in BY_KEY:
        raise ValueError('Unknown area ' + card['area'])
    if card['criterion'] not in criteria:
        raise ValueError('Unknown criterion')
    validate_importance(card.get('importance'))
    refs = {ref['id'] for ref in card['references']}
    for ref in card['references']:
        if not ref.get('title') or not ref.get('url', '').startswith(('https://', 'http://')):
            raise ValueError('Invalid reference')
    for step in card['progress']:
        if step['citation'] not in refs:
            raise ValueError('Unknown progress citation')
    for block in card.get('context_blocks', []):
        if block.get('citation') and block['citation'] not in refs:
            raise ValueError('Unknown context citation')
    if card.get('context_blocks') and card['context'] != '\n\n'.join(
        block['text'] for block in card['context_blocks']
    ):
        raise ValueError('Context paragraphs and search text differ')


def validate_record(card, path, criteria):
    identifier = card.get('id', '')
    if not re.fullmatch(r'TCS-\d{4,}', identifier) or path.stem != identifier:
        raise ValueError(f'{path.name}: card ID must match its filename')
    for field in ['title', 'area', 'formal', 'context', 'why', 'references',
                  'criterion', 'evidence', 'status', 'importance']:
        if not card.get(field):
            raise ValueError(f'{identifier}: missing {field}')
    if card['area'] not in BY_KEY or card['criterion'] not in criteria:
        raise ValueError(f'{identifier}: unknown category or selection criterion')
    if card['evidence'] not in {'reviewed', 'source', 'index'}:
        raise ValueError(f'{identifier}: invalid evidence level')
    if card['status'] not in {'open', 'source_open', 'uncertain', 'resolved', 'excluded'}:
        raise ValueError(f'{identifier}: invalid status')
    if card['status'] in {'resolved', 'excluded'} or card.get('scope_exclusion'):
        raise ValueError(f'{identifier}: archive this inactive card with scripts/archive_cards.py')
    importance = card['importance']
    if importance.get('method') == 'editorial':
        validate_importance(importance)
    elif (importance.get('method') != 'unassessed' or importance.get('score') != 50
          or not importance.get('reason', '').strip()):
        raise ValueError(f'{identifier}: invalid saved importance assessment')
    refs = {ref['id'] for ref in card['references']}
    if len(refs) != len(card['references']):
        raise ValueError(f'{identifier}: duplicate reference ID')
    if card['evidence'] == 'reviewed':
        validate_card(card, path, criteria)
    summary = card.get('working_summary')
    if summary:
        sentences = summary.get('sentences', [])
        if len(sentences) != 5 or any(not isinstance(s, str) or not s.strip() for s in sentences):
            raise ValueError(f'{identifier}: expected five summary sentences')
        if not set(summary.get('source_refs', [])) <= refs:
            raise ValueError(f'{identifier}: unknown summary reference')
        datetime.date.fromisoformat(summary['written_on'])


def load_catalog():
    inactive = read_inactive()
    data = dict(meta=json.loads((DATA / 'metadata.json').read_text()),
                criteria=json.loads((DATA / 'criteria.json').read_text()), cards=[])
    for path in active_card_paths():
        card = reader_record(json.loads(path.read_text()), data['criteria'])
        validate_record(card, path, data['criteria'])
        data['cards'].append(card)
    if not data['cards']:
        raise ValueError('No canonical cards found in data/cards/')
    apply_related_problems(data['cards'], inactive)
    return data


def textbook_report(data):
    """Derive the source-question index from annotations saved on the cards."""
    entries = {}
    new_ids = set()
    annotated = set()
    for card in data['cards']:
        for note in card.get('textbook_notes', []):
            annotated.add(card['id'])
            key = note['key']
            ref = note['reference']
            entry = entries.setdefault(key, dict(entry_key=key.split(':', 1)[-1], card_ids=[],
                disposition='existing_card', kind=note['kind'], summary=note['summary'],
                source=ref['title'], year=ref['year'], locator=ref['locator'],
                url=ref['url'], pdf_url=ref['pdf_url']))
            entry['card_ids'].append(card['id'])
            if card.get('key') == key:
                entry['disposition'] = 'new_draft'
                new_ids.add(card['id'])
    report = sorted(entries.values(), key=lambda entry: entry['entry_key'])
    for entry in report:
        entry['card_ids'].sort()
    metadata = dict(source_entries=len(report), new_cards=len(new_ids),
        existing_cards=len({i for e in report if e['disposition'] == 'existing_card' for i in e['card_ids']}),
        annotated_cards=len(annotated), sources=len({e['url'] for e in report}),
        kinds=dict(collections.Counter(e['kind'] for e in report)))
    data['meta']['textbook_questions'] = metadata
    return dict(meta=metadata, entries=report)


def update_metadata(data, now):
    levels = collections.Counter(card['evidence'] for card in data['cards'])
    completed = sum(
        card['evidence'] == 'reviewed' or card.get('review_outcome', {}).get('complete', False)
        for card in data['cards']
    )
    data['meta'].update(
        total=len(data['cards']), added=sum(card['is_new'] for card in data['cards']),
        evidence_counts=dict(levels), updated_at=now,
        completed_reviews=completed, remaining_reviews=len(data['cards']) - completed,
    )
    version_content = dict(cards=data['cards'], areas=data['areas'], taxonomy=data['meta']['taxonomy'],
                           benchmarks=data['meta']['benchmarks'], methodology=data['meta']['methodology'])
    data['meta']['version'] = hashlib.sha256(jsdump(version_content).encode()).hexdigest()[:20]


def publish(site=SITE):
    with (BASE / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        return _publish(site)


def _publish(site=SITE):
    site = Path(site)
    if site.resolve() == WEB.resolve():
        raise ValueError('web/ contains source assets; publish into build/ or another output directory')
    data = load_catalog()
    previous_path = site / 'catalog.json'
    previous = json.loads(previous_path.read_text()) if previous_path.exists() else {'meta': {}, 'cards': []}
    previous_version = previous['meta'].get('version', '')
    previous_cards = {card['id']: jsdump(card) for card in previous['cards']}
    apply_taxonomy(data)
    apply_importance(data)
    report = textbook_report(data)
    data['meta']['working_summary_count'] = sum(bool(c.get('working_summary')) for c in data['cards'])
    changed = [c['id'] for c in data['cards'] if previous_cards.get(c['id']) != jsdump(c)]
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    update_metadata(data, now)
    site.mkdir(parents=True, exist_ok=True)
    # A complete build works offline and needs no previously generated files.
    for name in ['index.html', 'app.js', 'community.js', 'votes.js', 'math.js', 'style.css',
                 'map.html', 'map.js', 'map.css', '.nojekyll']:
        atomic(site / name, (WEB / name).read_text())
    shutil.copytree(WEB / 'vendor', site / 'vendor', dirs_exist_ok=True)
    write_catalog_exports(site, data, report)
    for name in ['updates.json', 'scope-excluded.json', 'README.md']:
        (site / name).unlink(missing_ok=True)
    payload = write_live_updates(site, data, changed, previous_version, previous_cards.keys())
    print(jsdump(dict(published=changed if len(changed) < 50 else f'{len(changed)} records',
        total=len(data['cards']), detailed=data['meta']['evidence_counts'].get('reviewed', 0),
        version=data['meta']['version'])))
    return payload


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=SITE)
    publish(parser.parse_args().output)
