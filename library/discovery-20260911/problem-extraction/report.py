"""Build the readable source inventory without exposing the library in the UI."""
import collections
import csv
import io
import json
from pathlib import Path
from review_inventory import finish

ROOT = Path(__file__).resolve().parent
DISCOVERY = ROOT.parent
ATLAS = ROOT.parents[2]


def write_json(name, obj):
    (ROOT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')


if __name__=='__main__':
    finish()
    entries=json.loads((ROOT/'reviewed-entries.json').read_text())
    sources=json.loads((DISCOVERY/'local-sources.json').read_text())+json.loads((DISCOVERY/'web-sources.json').read_text())
    audit={s['id']:s for s in json.loads((ROOT/'extraction-audit.json').read_text())}
    ocr=ROOT/'ocr-audit.json'
    if ocr.exists():
        audit.update({s['id']:s for s in json.loads(ocr.read_text())})
    groups=collections.defaultdict(list)
    for e in entries: groups[e['source_id']].append(e)
    coverage=[]
    for s in sources:
        a=audit[s['id']]
        selected=groups[s['id']]
        coverage.append(dict(source_id=s['id'],title=s['title'],text_status=a['status'],
                             pages=a.get('pages'),marker_passages=a.get('marker_passages',0),
                             text_method=a.get('text_method','embedded_text_or_metadata_only'),
                             inventoried_entries=len(selected),
                             status_checked_entries=sum('status_checked_on' in e for e in selected),
                             review_scope='selected passages only' if selected else 'automatic screening only; no human question inventory'))
    for c in coverage:
        if c['source_id']=='personal-234':c['review_scope']='complete 75-item Survey of Problems, Questions, and Conjectures'
        if c['source_id']=='personal-283':c['review_scope']='complete 17-item Chapter 11 open-problem list'
        if c['source_id']=='canonne_distribution_testing':c['review_scope']='complete nine numbered open questions in Chapters 2–4'
    write_json('source-coverage.json',coverage)
    counts=dict(source_entries=len(entries),sources_with_entries=sum(bool(es) for es in groups.values()),
                all_discovered_sources=len(sources),local_documents_screened=sum(a['status']!='no_local_text' for a in audit.values()),
                metadata_or_html_only=sum(a['status']=='no_local_text' for a in audit.values()),
                automatic_marker_passages=sum(a.get('marker_passages',0) for a in audit.values()),
                ocr_complete=ocr.exists(),ocr_pages=3152 if ocr.exists() else None,
                status_checked_entries=sum('status_checked_on' in e for e in entries),
                individual_dispositions=sum(e['selection']!='not_imported' for e in entries),
                current_status=dict(collections.Counter(e['current_status'] for e in entries)),
                selection=dict(collections.Counter(e['selection'] for e in entries)))
    write_json('summary.json',counts)
    output=io.StringIO()
    fields=['id','source_id','source_title','source_locator','source_pages','title','question','kind','current_status','selection','catalogue_ids','verification_note','selection_note','verification_urls']
    writer=csv.DictWriter(output,fieldnames=fields);writer.writeheader()
    by_source={s['id']:s for s in sources}
    for e in entries:
        row={k:e.get(k,'') for k in fields};row['source_title']=by_source[e['source_id']]['title']
        for k in ['source_pages','catalogue_ids','verification_urls']:
            row[k]='; '.join(map(str,row[k])) if isinstance(row[k],list) else row[k]
        writer.writerow(row)
    (ROOT/'questions.csv').write_text(output.getvalue())
    lines=['# Questions found in the expanded library', '',
           'Source-era questions and research directions, with separate present-day checks. These are paraphrases, not quotations or a claim that every listed question remains open. File page numbers are one-based; printed page numbers may differ.', '',
           'The three complete numbered lists are Schrijver (75), Barenboim–Elkin (17), and Canonne (9). Other books have selected passages. An unchecked entry is a research lead and was not imported as a reviewed problem.', '']
    for s in sources:
        if not groups[s['id']]:continue
        lines += [f"## {s['title']}", '', f"{s.get('authors','')} · source `{s['id']}`", '']
        for e in groups[s['id']]:
            pages=', '.join(map(str,e['source_pages']))
            ids=', '.join(e['catalogue_ids'])
            lines += [f"- **{e['title']}** — {e['question']}",
                      f"  Source: {e['source_locator']}; file p. {pages}. Status: `{e['current_status']}`. Selection: `{e['selection']}`."+(f' Catalogue: {ids}.' if ids else '')]
            if e.get('corrected_question'):lines.append('  Corrected target: '+e['corrected_question'])
            if e.get('verification_note'):lines.append('  Verification: '+e['verification_note'])
            if e.get('selection_note'):lines.append('  Decision: '+e['selection_note'])
            if e.get('verification_urls'):lines.append('  Sources: '+', '.join(f'[primary {i+1}]({u})' for i,u in enumerate(e['verification_urls']))+'.')
            lines.append('')
    (ROOT/'questions.md').write_text('\n'.join(lines))
    registry=json.loads((ATLAS/'data/id_registry.json').read_text())
    publication=[json.loads((ATLAS/'data/cards'/(registry['reviewed:'+key]+'.json')).read_text()) for key in ['linear-size-boolean-integer-multiplication', 'polynomial-time-exact-addition-chain-length', 'perfect-versus-statistical-zero-knowledge', 'woodall-dijoin-packing-conjecture', 'conforti-cornuejols-packing-mfmc-conjecture']]
    additions='\n'.join(f"- **{p['id']} — {p['title']}**" for p in publication)
    missing='\n'.join('- '+c['title'] for c in coverage if c['text_status']=='no_local_text')
    resolved=sum(n for k,n in counts['current_status'].items() if k.startswith('resolved') or k=='reported_negative_resolution')
    readme=f'''# Library problem inventory and selection review — 11 September 2026

The expanded library yielded **{len(entries)} manually written source entries from {counts['sources_with_entries']} sources**. These include historical questions, repeated formulations across books and broader research directions. They are not {len(entries)} distinct, currently open benchmark problems.

Read the [complete question inventory](questions.md), or use [CSV](questions.csv) / [JSON](reviewed-entries.json). Each entry retains its book, section or problem number, file page, status and selection decision.

## Results

- {counts['status_checked_entries']} source entries have an explicit dated status check; {resolved} have a resolution or reported resolution recorded.
- {counts['individual_dispositions']} entries have an individual status or selection disposition. Other entries remain source leads and were not added to the dataset.
- Five significant, individually formulated problems were added as reviewed cards. Existing and archived catalogue records were included in the novelty search.

{additions}

The Fourier-transform candidate was not added because TCS-7175 already covers the target. The new Boolean multiplication card differs from the machine-time question TCS-7174. Exact computation of an addition-chain length differs from Scholz–Brauer (TCS-7170). These distinctions are recorded in the [dataset review](../../../research/library-problems-20260911/README.md).

## Extraction coverage and limits

All {counts['local_documents_screened']} available local documents (91 personal-library files and ten downloaded documents) underwent full-document text extraction and keyword screening. {counts['automatic_marker_passages']} merged marker passages are candidate contexts, not verified questions. {'Five scanned or poorly encoded books also underwent OCR of all 3,152 pages.' if ocr.exists() else 'OCR of five scanned or poorly encoded books is still in progress.'} OCR can miss or corrupt mathematical notation, so its output was not promoted automatically.

The inventory includes three complete numbered lists: 75 Schrijver survey items, 17 Barenboim–Elkin Chapter 11 problems, and all nine Canonne open questions. Other sources received selective passage review, not an exhaustive reading of every exercise or conjecture. Zero selected entries does not mean a book has no open problems. See [per-source coverage](source-coverage.json).

Ten discovered sources had no local full text for this pass. Software Foundations is available as an online series but was not downloaded or inventoried here; the other nine remained bibliographic discoveries:

{missing}

## Verification and publication

Status checks use primary papers and author corrections, as linked beside each checked question. “Resolved reported” records an author’s report without claiming an independent proof check. Recent preprint claims are identified as such. The new cards contain precise mathematical statements, model definitions, acceptance criteria, significance judgments and dated progress. Their editorial review is not a formal verification of the cited proofs.

`review_inventory.py` contains the human-authored paraphrases. `review_decisions.py` and `decisions.json` contain individual decisions. `extract.py` and `ocr.py` produce the screening audit; `report.py` builds this report. Raw book text and OCR caches are ignored by git. Originals in the personal library were not modified.

The library and this extraction workspace remain outside `web/`. The reader receives the five normal problem cards with public bibliographic references, without access to private book paths or PDFs.
'''
    (ROOT/'README.md').write_text(readme)
    print(json.dumps(counts,ensure_ascii=False,indent=2))
