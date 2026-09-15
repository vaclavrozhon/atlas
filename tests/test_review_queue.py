"""Concurrent workers must not receive or finish each other's active cards."""

from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
import json
import multiprocessing
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE / 'scripts'))
import review_queue

spec = importlib.util.spec_from_file_location(
    'completion_fixture', SOURCE / review_queue.REVIEW / 'complete_review.py')
completion = importlib.util.module_from_spec(spec)
spec.loader.exec_module(completion)


def claim_worker(root, barrier, results, number):
    barrier.wait(timeout=15)
    try:
        claim = review_queue.reserve(Path(root), f'worker-{number}')
        results.put(('claimed', claim['id'], claim['token']))
    except ValueError as error:
        results.put(('unavailable', str(error)))


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix='atlas-review-queue-')
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.cards = self.root / 'data/cards'
        self.cards.mkdir(parents=True)
        self.review = self.root / review_queue.REVIEW
        self.review.mkdir(parents=True)
        self.queue = dict(records=[])
        self.add_card('TCS-0001')
        self.add_card('TCS-0002')
        self.save()

    def add_card(self, identifier, state='pending', active=True):
        # Minimal card bodies suffice for reservation; the completion test below
        # uses a real valid active card and the real schema validator.
        content = json.dumps(dict(id=identifier)) + '\n'
        if active:
            (self.cards / (identifier + '.json')).write_text(content)
        self.queue['records'].append(dict(id=identifier, title='Fixture ' + identifier,
            area='Complexity theory', priority='top500', state=state,
            input_sha256=hashlib.sha256(content.encode()).hexdigest()))

    def save(self):
        (self.review / 'queue.json').write_text(json.dumps(self.queue))

    def test_simultaneous_processes_receive_distinct_cards(self):
        context = multiprocessing.get_context('fork')
        barrier, results = context.Barrier(6), context.Queue()
        workers = [context.Process(target=claim_worker,
                   args=(str(self.root), barrier, results, n)) for n in range(6)]
        for worker in workers:
            worker.start()
        received = [results.get(timeout=20) for _ in workers]
        for worker in workers:
            worker.join(timeout=20)
            self.assertEqual(worker.exitcode, 0)
        claimed = [item for item in received if item[0] == 'claimed']
        self.assertEqual({item[1] for item in claimed}, {'TCS-0001', 'TCS-0002'})
        self.assertEqual(len(claimed), 2)
        self.assertEqual(len({item[2] for item in claimed}), 2)
        self.assertEqual(len(review_queue.read_claims(self.root)), 2)
        self.assertEqual(review_queue.read_queue(self.root), self.queue)

    def test_active_only_inventory_and_no_automatic_expiration(self):
        self.add_card('TCS-0003', active=False)
        self.add_card('TCS-0004', state='completed')
        self.save()
        # An unreadable/non-JSON archive body must never be consulted.
        archived = self.root / 'data/archive/cards'
        archived.mkdir(parents=True)
        (archived / 'TCS-0003.json').write_text('not JSON: must not be read')
        claim = review_queue.reserve(self.root, 'slow-worker', 'TCS-0001')
        claims = review_queue.read_claims(self.root)
        claims['TCS-0001']['claimed_at'] = '2000-01-01T00:00:00+00:00'
        review_queue.write_claims(self.root, claims)
        with self.assertRaisesRegex(ValueError, 'reserved by slow-worker'):
            review_queue.reserve(self.root, 'new-worker', 'TCS-0001')
        rows = review_queue.public_rows(self.root, self.queue, claims)
        self.assertEqual([row['id'] for row in rows], ['TCS-0001', 'TCS-0002'])
        self.assertNotIn(claim['token'], json.dumps(rows))
        with review_queue.locked(self.root):
            self.assertEqual(review_queue.refresh_list(self.root), 2)
        inventory = (self.review / 'unfinished.md').read_text()
        self.assertNotIn('TCS-0003', inventory)
        self.assertNotIn('TCS-0004', inventory)

    def test_old_token_cannot_release_or_finish_reassigned_work(self):
        first = review_queue.reserve(self.root, 'one', 'TCS-0001')
        with self.assertRaises(ValueError):
            review_queue.release(self.root, 'TCS-0001', 'wrong')
        review_queue.release(self.root, 'TCS-0001', first['token'])
        second = review_queue.reserve(self.root, 'two', 'TCS-0001')
        with self.assertRaises(ValueError):
            review_queue.release(self.root, 'TCS-0001', first['token'])
        with self.assertRaises(ValueError):
            with review_queue.locked(self.root):
                review_queue.require_claim(self.root, 'TCS-0001', first['token'])
        self.assertEqual(review_queue.read_claims(self.root)['TCS-0001'],
                         {key: second[key] for key in
                          ('worker', 'token', 'claimed_at', 'input_sha256')})

    def test_completion_checks_ownership_hash_and_releases_only_after_success(self):
        path = self.cards / 'TCS-0001.json'
        path.write_bytes((SOURCE / 'data/cards/TCS-0001.json').read_bytes())
        self.queue['records'][0]['input_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.save()
        claim = review_queue.reserve(self.root, 'one', 'TCS-0001')
        arguments = dict(identifier='TCS-0001', fields={}, notes=['Test review'],
                         sources=['Test fixture'], status_note='Isolated test only.')
        with patch.multiple(completion, ROOT=self.root, HERE=self.review):
            for token in (None, 'wrong'):
                with self.assertRaises(ValueError):
                    completion.complete(**arguments, claim_token=token)
            original = path.read_bytes()
            path.write_bytes(original + b'\n')
            with self.assertRaises(AssertionError):
                completion.complete(**arguments, claim_token=claim['token'])
            self.assertIn('TCS-0001', review_queue.read_claims(self.root))
            self.assertEqual(review_queue.read_queue(self.root), self.queue)
            path.write_bytes(original)
            with redirect_stdout(io.StringIO()):
                completion.complete(**arguments, claim_token=claim['token'])
        saved = review_queue.read_queue(self.root)
        self.assertEqual(saved['records'][0]['state'], 'completed')
        self.assertEqual(saved['records'][0]['output_sha256'],
                         hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertNotIn('TCS-0001', review_queue.read_claims(self.root))
        self.assertNotIn('TCS-0001', (self.review / 'unfinished.md').read_text())
        self.assertEqual(len((self.review / 'reviews.jsonl').read_text().splitlines()), 1)

    def test_reservation_reports_changed_input_without_rewriting_baseline(self):
        (self.cards / 'TCS-0001.json').write_text('{"new": true}')
        before = (self.review / 'queue.json').read_bytes()
        claim = review_queue.reserve(self.root, 'one', 'TCS-0001')
        self.assertTrue(claim['baseline_changed'])
        self.assertEqual((self.review / 'queue.json').read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
