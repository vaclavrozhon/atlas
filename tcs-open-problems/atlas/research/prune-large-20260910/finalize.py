"""Publish and package a consistent local atlas under the existing writer lock."""
import fcntl,importlib.util,json,zipfile
from pathlib import Path
import sys
BASE=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE))
from publish import _publish,atomic
spec=importlib.util.spec_from_file_location('pruning_validation',HERE/'validate.py');validation=importlib.util.module_from_spec(spec);spec.loader.exec_module(validation)
with (BASE/'.publish.lock').open('a') as lock:
    fcntl.flock(lock,fcntl.LOCK_EX)
    payload=_publish()
    validation.main()
    data=json.loads((BASE/'site/catalog.json').read_text())
    assert sum(a['count'] for a in data['areas'] if a['group']=='large')==2134
    manifest=json.loads((BASE/'to_delete/large-buckets-20260910/manifest.json').read_text())
    report=json.loads((HERE/'validation.json').read_text())
    report['browser']=json.loads((HERE/'browser-validation.json').read_text())
    report['existing_suites']=['qa/taxonomy.py','qa/ranking.py','qa/taxonomy.cjs','qa/quick.cjs','qa/bulk-updates.cjs','qa/delta-updates.cjs']
    notes=("\n\n## 2026-09-10 — Preliminary pruning of the ten large categories completed\n\n"
        "User requested roughly 4,000 → 2,000 candidates, with reversible removals. "
        "Screened 4,098 initial candidates plus 105 concurrent textbook/survey imports. "
        "Archived 2,069; retained 2,134 across the ten large buckets. All 2,939 small-category "
        "records retain their categories. Complete archived cards, reasons, per-record decisions, "
        "the full pre-pruning catalogue and a restoration CLI are in `to_delete/large-buckets-20260910/`. "
        "`taxonomy.py` reads that manifest on every publication; `state=quarantined` removes a record "
        "from the candidate pool, `state=retained` restores it. Keep this overlay when importing or "
        "reviewing records. This is independent of current open status and individual review progress.\n\n"
        "Two-pass editorial triage used saved titles/formulations/source context, not a score cutoff. "
        "524 borderline candidates were retained on a second look. The final dispositions are "
        "1,013 paper-specific follow-ups, 668 fragments/background passages, 354 narrow cases, "
        "16 identified restatements, 14 non-problem tasks/directions and 4 already-resolved records. "
        "Malformed passages are excluded as entries; the underlying topics are not thereby declared "
        "unimportant. Fresh open-status verification was not part of this pass.\n\n"
        "Publication preserves all 7,156 IDs, current card content and source annotations. "
        "The two archive kinds are distinguished in badges and counts; previous selection categories "
        "and reasons appear on removed cards. Archive/all filters, direct links, counterpart links "
        "and browser notes remain usable. Full exports preserve archived data. A real 4,203 → 2,134 "
        "live update preserved editing focus and notes with bounded DOM work; offline and mobile checks "
        "also passed. Full-batch restoration was verified in a temporary manifest without changing "
        "production state. See `research/prune-large-20260910/validation.json` and "
        "`browser-validation.json`. The portable ZIP was rebuilt without the independent source library/PDFs.\n")
    with (BASE/'WORKING_NOTES.md').open('a') as f:f.write(notes)
    site=BASE/'site';archive=BASE/'tcs-atlas-demo.zip';tmp=archive.with_suffix('.zip.packaging')
    files=[p for p in site.rglob('*') if p.is_file() and not p.name.endswith('.publishing')]
    assert not any(p.suffix.lower()=='.pdf' or 'library' in p.relative_to(site).parts for p in files)
    with zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(files):z.write(p,'tcs-atlas-demo/'+str(p.relative_to(site)))
    tmp.replace(archive)
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert json.loads(z.read('tcs-atlas-demo/catalog.json'))==data
        assert z.read('tcs-atlas-demo/app.js')==(site/'app.js').read_bytes()
    report.update(offline_zip_bytes=archive.stat().st_size,offline_zip_version=data['meta']['version'],offline_zip_integrity=True)
    atomic(HERE/'completion.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    atomic(BASE/'to_delete/large-buckets-20260910/validation.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(version=data['meta']['version'],large_before=4203,removed=2069,large_remaining=2134,small_preserved=2939,all_saved=len(data['cards']),archive_bytes=archive.stat().st_size),indent=2))
