"""Build the atlas's offline source-library section without changing problem cards.

The original sibling library is the authoring input. The published snapshot is
self-contained and can also be rebuilt when that sibling directory is absent.
The normal publisher calls this while holding its publication lock.
"""
import datetime
import fcntl
import hashlib
import html
import json
import re
import shutil
from pathlib import Path

from taxonomy import BIG, SMALL

BASE = Path(__file__).resolve().parent
SITE = BASE / 'site'
UI = BASE / 'library_ui'
ORIGINAL = BASE.parent.parent / 'tcs-source-library'
KINDS = {'question': 'Question', 'conjecture': 'Conjecture', 'research_direction': 'Research direction'}
esc = html.escape


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text() == content:
        return
    temporary = path.with_name(path.name + '.publishing')
    temporary.write_text(content, encoding='utf-8')
    temporary.replace(path)


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def relative_file(root, name):
    path = (root / name).resolve()
    if root.resolve() not in path.parents or not path.is_file():
        raise ValueError(f'Invalid or missing library file: {name}')
    return path


def copy_file(source, target):
    if source.resolve() == target.resolve():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and (target.stat().st_size, target.stat().st_mtime_ns) == (source.stat().st_size, source.stat().st_mtime_ns):
        return
    temporary = target.with_name(target.name + '.publishing')
    shutil.copy2(source, temporary)
    temporary.replace(target)


def source_card(source, categories):
    key = source['id']
    rows = []
    for i, problem in enumerate(source['problems'], 1):
        entry_id = f'{key}--{i:02}'
        rows.append(f'''<li id="{entry_id}" data-entry-key="{esc(problem['entry_key'])}">
<span class="entry-kind">{KINDS[problem['kind']]}</span> {esc(problem['summary'])}
<div class="entry-links"><a href="{esc(problem['local_pdf_url'])}">{esc(problem['locator'])} · PDF p. {problem['pdf_page']} ↗</a>
<a href="#{entry_id}" aria-label="Direct link to entry {i}">#</a></div></li>''')
    selected = [a for a in categories if key in a['source_ids']]
    selected_links = ' · '.join(f'<a data-category="{a["id"]}" href="?category={a["id"]}">{a["id"]} {esc(a["title"])}</a>' for a in selected)
    if not selected_links:
        selected_links = 'Background reference · original selective inventory'
    caution = f'<p class="source-caution">{esc(source["caution"])}</p>' if source['caution'] else ''
    content = '<ol>' + ''.join(rows) + '</ol>' if rows else '<p>No explicit unresolved question was identified in the reviewed material.</p>'
    count = len(rows)
    return f'''<article id="{key}" class="source-card" data-categories="{' '.join(a['id'] for a in selected)}" data-kind="{source['kind']}" data-count="{count}">
<div class="source-meta">{source['year'] or 'Undated draft'} · {source['download']['pages']} PDF pages · {esc(source['area'])}</div>
<h2><a href="#{key}">{esc(source['title'])}</a></h2>
<p class="source-authors">{esc(source['authors'])}</p><p class="source-categories">{selected_links}</p>
<p class="source-reason">{esc(source['selection_reason'])}</p>
<nav class="source-links" aria-label="Files for {esc(source['title'])}"><a href="{source['pdf']}">Read PDF ↗</a><a href="{source['text']}">Full text</a><a href="{source['note']}">Reading note</a><a href="{esc(source['source_url'])}">Original source ↗</a></nav>
<details class="source-entries"><summary>{count} annotated {'entry' if count == 1 else 'entries'} <span>· open in this source version</span></summary>{content}</details>
<details class="source-scope"><summary>Version & reading scope</summary><p>{esc(source['edition_note'])}</p><p>{esc(source['coverage'])}</p>{caution}<p>Current open status has not been checked. Summaries may group variants; use the PDF for exact definitions. Whole-work exhaustiveness is not certified.</p></details>
</article>'''


def integrate_source_library():
    target = SITE / 'library'
    origin = ORIGINAL if (ORIGINAL / 'library.json').is_file() else target
    if not (origin / 'library.json').is_file():
        raise FileNotFoundError('Source-library input and published snapshot are both missing.')
    library = json.loads((origin / 'library.json').read_text())
    area_data = json.loads((origin / 'area-coverage.json').read_text())
    categories = area_data['areas']
    if [a['title'] for a in categories] != BIG + SMALL:
        raise ValueError('Library categories differ from the agreed atlas taxonomy.')
    sources = library['sources']
    by_id = {s['id']: s for s in sources}
    if len(by_id) != len(sources):
        raise ValueError('Duplicate source IDs.')
    for a in categories:
        if a['primary_source_id'] not in a['source_ids'] or not by_id[a['primary_source_id']]['problems']:
            raise ValueError('Missing annotated primary source: ' + a['id'])
        for key in a['source_ids']:
            if key not in by_id:
                raise ValueError('Unknown category source: ' + key)

    files = ['sources.json', 'sources.csv', 'open-problems.json', 'open-problems.csv', 'area-coverage.json']
    for source in sources:
        if not re.fullmatch(r'[a-z0-9_]+', source['id']):
            raise ValueError('Invalid source ID.')
        files += [source['pdf'], source['text'], source['note'], f'audit/{source["id"]}.json']
    source_files = [(name, relative_file(origin, name)) for name in files]
    signature = hashlib.sha256()
    for path in [Path(__file__), origin / 'library.json', origin / 'area-coverage.json', *sorted(UI.glob('*'))]:
        signature.update(path.read_bytes())
    for name, path in source_files:
        signature.update(f'{name}:{path.stat().st_size}:{path.stat().st_mtime_ns}'.encode())
    fingerprint = signature.hexdigest()
    manifest_path = target / 'integration.json'
    previous = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    generated = ['index.html', 'style.css', 'app.js', 'summary.js', 'library.json', 'README.md', 'AREA_COVERAGE.md']
    if previous.get('fingerprint') == fingerprint and all((target / name).is_file() for name in files + generated):
        return previous

    seen_entries = set()
    for source in sources:
        pdf = relative_file(origin, source['pdf'])
        if hashlib.sha256(pdf.read_bytes()).hexdigest() != source['download']['sha256']:
            raise ValueError('PDF checksum mismatch: ' + source['id'])
        for i, entry in enumerate(source['problems'], 1):
            if entry['entry_key'] in seen_entries or entry['source_id'] != source['id']:
                raise ValueError('Invalid entry identity: ' + entry['entry_key'])
            seen_entries.add(entry['entry_key'])
            if not 1 <= entry['pdf_page'] <= source['download']['pages'] or entry['kind'] not in KINDS:
                raise ValueError('Invalid entry page or kind: ' + entry['entry_key'])
            if entry['local_pdf_url'] != f'{source["pdf"]}#page={entry["pdf_page"]}':
                raise ValueError('Unexpected PDF link: ' + entry['entry_key'])
    for name, path in source_files:
        copy_file(path, target / name)

    summary = {'sources': len(sources), 'entries': len(seen_entries), 'categories': []}
    for a in categories:
        summary['categories'].append({**a, 'source_count': len(a['source_ids']),
            'entry_count': sum(len(by_id[k]['problems']) for k in a['source_ids']),
            'primary_source_title': by_id[a['primary_source_id']]['title']})
    write(target / 'summary.js', 'window.TCS_SOURCE_LIBRARY=' + json.dumps(summary, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';\n')
    library['meta']['scope'] = 'Source library in the local atlas. Category-to-source coverage; no matching or import into problem cards.'
    library['meta']['atlas_section'] = 'library/index.html'
    write(target / 'library.json', dump(library))

    coverage = []
    markdown = ['# Textbooks and surveys — category coverage', '',
        f'{len(categories)} categories · {len(sources)} downloaded sources · {len(seen_entries)} annotated source entries.', '',
        '[Open the library](index.html) · [Back to atlas problems](../index.html)', '',
        'Category membership selects a specialist source; every entry from that source remains available, including topics outside the selection category. Background references retain their original selective inventories. Statements are dated source notes, not a verification of current open status.', '',
        '| Category | Specialist source | Entries | Selection scope |', '| --- | --- | ---: | --- |']
    for a in categories:
        s = by_id[a['primary_source_id']]
        aux = ''.join(f'<br>Also: <a href="#{key}">{esc(by_id[key]["title"])}</a>' for key in a['source_ids'] if key != s['id'])
        count = sum(len(by_id[k]['problems']) for k in a['source_ids'])
        coverage.append(f'<tr><th scope="row"><a href="?category={a["id"]}" data-category="{a["id"]}">{a["id"]} {esc(a["title"])}</a></th><td><a href="#{s["id"]}">{esc(s["title"])}</a>{aux}</td><td>{count}</td></tr>')
        links = ' · '.join(f'[{by_id[k]["title"]}]({by_id[k]["note"]}) ([PDF]({by_id[k]["pdf"]}))' for k in a['source_ids'])
        markdown.append(f'| {a["id"]} {a["title"]} | {links} | {count} | {a["selection_note"]} |')
    markdown += ['', 'Miscellaneous uses domination reconfiguration as a concrete representative; this does not rename the category. One specialist reference does not cover every subfield of a broad category. The supplementary Regular Model Checking survey has no identified unresolved questions; Loop Termination is the annotated primary source for L09.', '']
    write(target / 'AREA_COVERAGE.md', '\n'.join(markdown))
    readme = ['# TCS Atlas — source library', '',
        f'**{len(sources)} downloaded titles · {len(seen_entries)} source entries · {len(categories)} covered categories.**', '',
        '[Browse the source library](index.html) · [Category coverage](AREA_COVERAGE.md) · [Atlas problems](../index.html)', '',
        'The library preserves the source inventories, PDF copies, extracted text, reading notes, version metadata and download hashes. It is a separate section of the atlas: entries are not assigned problem IDs, deduplicated against problem cards, or counted as reviewed catalogue problems.', '',
        'All located explicit unresolved statements from the selected specialist sources are retained, including subjects outside their selection category. Related variants and repeated statements may share an entry. Fourteen background references retain the original selective inventories. Read the scope and caveats for each work; whole-work exhaustiveness is not certified.', '',
        '“Open” means as presented in the downloaded version. Current status has not been reviewed. Statements resolved later in the same source are excluded where identified. Research directions are labeled separately from questions and conjectures.', '',
        '## Reading', '',
        '- Search source titles, authors and all annotated entries; filter by the 35 atlas categories and source type.',
        '- Open a source’s annotated entries to read its inventory. Every entry links to its PDF page and has a direct link.',
        '- Category links retain every entry of each selected source. Reset shows the complete library, including background references.',
        '- URLs support `?category=L01`, `?q=matching`, `?type=book`, source fragments such as `#vadhan2012`, and entry fragments such as `#vadhan2012--01`.',
        '- All local pages, PDFs, text and exports work offline. Original-source links need internet access.', '',
        '## Data', '',
        '[Full library JSON](library.json) · [Entries JSON](open-problems.json) · [Entries CSV](open-problems.csv) · [Bibliography CSV](sources.csv) · [Category coverage JSON](area-coverage.json)', '',
        'The per-source files in `audit/` record PDF provenance and SHA-256 hashes. PDF page numbers count from one, including front matter.', '',
        '## Updating', '',
        'The atlas publisher refreshes this section through `source_library.py` without changing problem identities or personal notes. The sibling `tcs-source-library` directory remains the authoring input; the published snapshot works independently when copied elsewhere.', '',
        'Local PDF copies are for personal research. Retain the original distribution terms; public availability does not grant redistribution rights.', '']
    write(target / 'README.md', '\n'.join(readme))
    page = (UI / 'index.html').read_text()
    replacements = {'@@SOURCE_COUNT@@': str(len(sources)), '@@ENTRY_COUNT@@': str(len(seen_entries)),
        '@@CATEGORY_COUNT@@': str(len(categories)),
        '@@CATEGORIES@@': ''.join(f'<option value="{a["id"]}">{a["id"]} — {esc(a["title"])}</option>' for a in categories),
        '@@CARDS@@': '\n'.join(source_card(s, categories) for s in sources),
        '@@COVERAGE@@': '\n'.join(coverage)}
    for marker, value in replacements.items():
        page = page.replace(marker, value)
    write(target / 'index.html', page)
    for name in ['app.js', 'style.css']:
        write(target / name, (UI / name).read_text())
    result = dict(fingerprint=fingerprint, integrated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        sources=len(sources), entries=len(seen_entries), categories=len(categories), pdfs=len(sources),
        pdf_sha256_verified=True, catalogue_problem_import=False,
        source_built_at=library['meta']['built_at'], files=files + generated)
    write(manifest_path, dump(result))
    return result


if __name__ == '__main__':
    with (BASE / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        result = integrate_source_library()
    print(json.dumps({k: result[k] for k in ['sources', 'entries', 'categories', 'pdfs', 'integrated_at']}))
