"""Package the latest authorized publication while preserving other authors' work."""
import fcntl
import hashlib
import json
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
sys.path.insert(0, str(BASE))
from publish import _publish, atomic

ARCHIVE = BASE/'to_delete/large-buckets-second-20260910'


def main():
    report = json.loads((HERE/'validation.json').read_text())
    browser = json.loads((HERE/'browser-validation.json').read_text())
    assert report['removed']==543 and browser['quarantined']==543 and not browser['errors']
    with (BASE/'.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        _publish()
        data = json.loads((BASE/'site/catalog.json').read_text())
        cards = {c['id']:c for c in data['cards']}
        m = json.loads((ARCHIVE/'manifest.json').read_text())
        assert len(cards)==7156 and data['meta']['taxonomy']['candidate_count']==2695
        assert sum(c['selection_group']=='large' for c in cards.values())==1591
        assert sum(c['selection_group']=='small' for c in cards.values())==1104
        assert all(cards[i]['scope_exclusion']['reason']==d['reason'] for i,d in m['records'].items())
        assert all(cards[i]['scope_exclusion']['review_id']==m['review_id'] for i in m['records'])
        assert hashlib.sha256((ARCHIVE/'records.json').read_bytes()).hexdigest()==m['archive_sha256']
        for path, digest in m['previous_manifest_hashes'].items():
            assert hashlib.sha256((BASE/path).read_bytes()).hexdigest()==digest
        site = BASE/'site'
        output = BASE/'tcs-atlas-demo.zip'
        temporary = output.with_suffix('.zip.packaging')
        files = [p for p in site.rglob('*') if p.is_file() and not p.name.endswith('.publishing')]
        assert not any(p.suffix.lower()=='.pdf' or 'library' in p.relative_to(site).parts for p in files)
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for p in sorted(files):
                z.write(p, 'tcs-atlas-demo/'+str(p.relative_to(site)))
        temporary.replace(output)
        with zipfile.ZipFile(output) as z:
            assert z.testzip() is None
            assert json.loads(z.read('tcs-atlas-demo/catalog.json'))==data
            assert z.read('tcs-atlas-demo/app.js')==(site/'app.js').read_bytes()
            assert z.read('tcs-atlas-demo/data.js')==(site/'data.js').read_bytes()
        report.update(restoration_test_version=report['version'],version=data['meta']['version'],
                      browser=browser,offline_zip_bytes=output.stat().st_size,
                      offline_zip_integrity=True,offline_zip_version=data['meta']['version'],
                      existing_suites=['qa/taxonomy.py','qa/ranking.py','qa/taxonomy.cjs'])
        atomic(ARCHIVE/'validation.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        atomic(HERE/'completion.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        notes = ('\n\n## 2026-09-10 — Second individual pruning of large categories completed\n\n'
                 'User requested another 500–1,000 removals, with every one listed and individually explained '
                 'in the conversation. Read all 2,134 remaining large candidates and selected 543; '
                 '1,591 large and 1,104 small candidates remain (2,695 total). All 543 were printed '
                 'in order with a concrete Czech rationale; `to_delete/large-buckets-second-20260910/DECISIONS.md` '
                 'preserves the same numbering and full individual reasons. English short names identify '
                 'the topic; CSV and full records preserve original titles, saved questions and sources.\n\n'
                 'The new manifest is an independent persistent overlay alongside the original large '
                 '(2,069) and small (1,835) batches. No score cutoff or equal bucket pruning rate was used. '
                 'No canonical reviewed card or approved fundamental proposal was selected. '
                 'This is editorial importance pruning, not current-open-status verification or the final quota selection. '
                 'All 7,156 IDs and latest authored content remain available; prior manifests are byte-for-byte unchanged.\n\n'
                 'A concurrent detailed review of TCS-6572 placed its smoothed-analysis reference first and '
                 'triggered a wrong move to Beyond worst-case. The explicit category override preserves the '
                 'approved Optimization and numerics placement of the worst-case polynomial simplex question. '
                 'This is documented separately in the new manifest; the immediate snapshot remains unaltered '
                 '(it captured 2,133 large and 1,105 small before that correction).\n\n'
                 'Validation covered exact archive copies and hash, all stable IDs and annotations, 543 unique '
                 'rationales, independent full restoration of each of the three batches and of all batches together, '
                 'idempotence, current CSV/offline/live publication parity, 35 category filters, archive and counterpart '
                 'links, and editing focus/notes across a real live pruning update. Portable ZIP regenerated '
                 'without the separate source library. Full reports are in the review and archive directories.\n')
        with (BASE/'WORKING_NOTES.md').open('a') as out:
            out.write(notes)
        print(json.dumps({k:report[k] for k in ['version','removed','large_remaining','small_preserved',
                         'candidate_count','all_saved','archive_total','offline_zip_bytes']},indent=2))


if __name__=='__main__':
    main()
