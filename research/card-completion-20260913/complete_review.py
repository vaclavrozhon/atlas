"""Record an individually authored completion after checking its current input."""
import collections
import fcntl
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'scripts'))
from card_schema import reader_record
from catalog_exports import atomic
from publish import validate_record

DATE = datetime.now(ZoneInfo('Europe/Prague')).date().isoformat()
CRITERIA = json.loads((ROOT / 'data/criteria.json').read_text())

def complete(identifier, fields, notes, sources, status_note, summary=None, expected_sha256=None, archive_reason=None):
    assert notes and sources and status_note, 'An individual review and checked sources are required.'
    retiring = fields.get('status') in {'resolved', 'excluded'}
    assert bool(archive_reason) == retiring, 'An inactive completion requires an explicit immediate archival reason.'
    with (ROOT / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        path = ROOT / 'data/cards' / f'{identifier}.json'
        queue = json.loads((HERE / 'queue.json').read_text())
        row = next(r for r in queue['records'] if r['id'] == identifier)
        assert row['state'] == 'pending', identifier
        input_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        assert input_hash == (expected_sha256 or row['input_sha256']), identifier
        card = json.loads(path.read_text())
        card.update(fields)
        if 'importance' in fields and card['importance']['method'] == 'editorial':
            card['importance'].setdefault('assessed_on', DATE)
        if fields.get('context_blocks'):
            card.pop('context', None)
        if summary is not None:
            assert len(summary) == 5
            card['working_summary'] = dict(sentences=summary, basis='saved_sources',
                source_basis='individual_source_review', written_on=DATE,
                source_refs=[r['id'] for r in card['references']])
        card.update(status=fields.get('status', 'source_open'), evidence='reviewed',
            model_self_contained=True, requires_context=False,
            formulation_reviewed_on=DATE, status_note=status_note,
            updated_at=datetime.now(timezone.utc).isoformat(timespec='seconds'))
        card['statement_review'] = dict(status='revised', reviewed_on=DATE,
            remaining_issue='', notes=notes,
            scope='Individual formulation and source review; current-status limits are recorded separately.')
        card['quality_review'] = dict(reviewed_on=DATE, reference_card='TCS-0001',
            state='revised', changes=notes, checked_sources=sources,
            scope='Checked target, definitions, quantifiers, answer criterion, context, significance and dated source claims. Bounded later-work checks do not independently certify every cited proof.')
        card['review_note'] = f'Completed individual review against P versus NP on {DATE}; see research/card-completion-20260913/reviews.jsonl.'
        validation_view = reader_record(card, CRITERIA)
        if retiring:
            # Check the complete schema without asking the active publisher to
            # accept an inactive record. The saved status remains unchanged.
            validation_view['status'] = 'uncertain'
        validate_record(validation_view, path, CRITERIA)
        output = json.dumps(card, ensure_ascii=False, indent=2) + '\n'
        atomic(path, output)
        row.update(state='completed', completed_on=DATE, review_input_sha256=input_hash,
            output_sha256=hashlib.sha256(output.encode()).hexdigest(),
            output_path=str(path.relative_to(ROOT)))
        queue['counts'] = dict(total=len(queue['records']),
            **dict(collections.Counter(r['state'] for r in queue['records'])))
        atomic(HERE / 'queue.json', json.dumps(queue, ensure_ascii=False, indent=2) + '\n')
        with (HERE / 'reviews.jsonl').open('a') as ledger:
            ledger.write(json.dumps(dict(id=identifier, date=DATE, outcome='completed',
                changes=notes, sources_checked=sources, status_review=status_note,
                input_sha256=input_hash), ensure_ascii=False) + '\n')
        print(identifier, queue['counts'])
    if retiring:
        from archive_cards import change_activity
        print(change_activity([identifier], reason=archive_reason))
        with (ROOT / '.publish.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            queue = json.loads((HERE / 'queue.json').read_text())
            row = next(r for r in queue['records'] if r['id'] == identifier)
            row['output_path'] = f'data/archive/cards/{identifier}.json'
            atomic(HERE / 'queue.json', json.dumps(queue, ensure_ascii=False, indent=2) + '\n')
            with (HERE / 'reviews.jsonl').open('a') as ledger:
                ledger.write(json.dumps(dict(id=identifier, date=DATE,
                    outcome='archived_after_completion', reason=archive_reason,
                    output_path=row['output_path']), ensure_ascii=False) + '\n')

def ref(identifier, title, authors, year, url, locator):
    return dict(id=identifier, title=title, authors=authors, year=year, url=url, locator=locator)

def block(text, citation='primary'):
    return dict(text=text, citation=citation)

def progress(date, text, citation='primary'):
    return dict(date=date, text=text, citation=citation)
