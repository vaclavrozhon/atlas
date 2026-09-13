"""Extract available source text and locate passages for human review.

Markers are research leads, never an automatically accepted problem inventory.
PDF page numbers count front matter. DjVu pages are extracted individually.
"""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
DISCOVERY = ROOT.parent
TEXT = ROOT / 'text'
TEXT.mkdir(exist_ok=True)
MARKERS = ROOT / 'markers'
MARKERS.mkdir(exist_ok=True)
PATTERN = re.compile(
    r'\b(?:open\s+(?:problems?|questions?|directions?)|research\s+problems?|'
    r'unsolved|unresolved|conjectur(?:e|es|ed)|not\s+known|'
    r'(?:remain(?:s)?|still)\s+(?:unknown|open)|unknown\s+whether|'
    r'we\s+do\s+not\s+know|not\s+yet\s+(?:known|solved|resolved))\b|'
    r'otevřen\w*\s+(?:problém|otáz)|nevyřešen\w*', re.I)


def process(source):
    result = {k: source.get(k) for k in ['id', 'title', 'kind', 'category_ids', 'local_path', 'pages']}
    if not source.get('local_path'):
        result.update(status='no_local_text', limitation=source.get('availability', ''))
        return result
    source_path = Path(source['local_path'])
    dest = TEXT / (source['id'] + '.txt')
    try:
        if not dest.exists():
            if source_path.suffix.lower() == '.djvu':
                chunks = []
                for page in range(1, source['pages'] + 1):
                    p = subprocess.run(['djvutxt', f'--page={page}', str(source_path)], capture_output=True, timeout=30)
                    if p.returncode:
                        raise RuntimeError(p.stderr.decode(errors='replace')[:300])
                    chunks.append(p.stdout.decode(errors='replace').rstrip('\f\n'))
                dest.write_text('\f'.join(chunks) + '\f')
            else:
                p = subprocess.run(['pdftotext', '-layout', str(source_path), str(dest)], capture_output=True, timeout=180)
                if p.returncode:
                    raise RuntimeError(p.stderr.decode(errors='replace')[:300])
        text = dest.read_text(errors='replace')
        pages = text.split('\f')
        if not pages[-1].strip():
            pages.pop()
        hits = []
        for page, content in enumerate(pages, 1):
            content = re.sub(r'\s+', ' ', content)
            intervals = []
            for match in PATTERN.finditer(content):
                start, end = max(0, match.start()-220), min(len(content), match.end()+850)
                if intervals and start <= intervals[-1][1]:
                    intervals[-1][1] = max(intervals[-1][1], end)
                    intervals[-1][2].append(match.group())
                else:
                    intervals.append([start, end, [match.group()]])
            for start, end, markers in intervals:
                hits.append(dict(key=f"{source['id']}-p{page}-{start}", page=page, offset=start,
                                 markers=markers, context=content[start:end], review_status='unreviewed_marker'))
        (MARKERS / (source['id'] + '.json')).write_text(json.dumps(hits, ensure_ascii=False, indent=2) + '\n')
        result.update(status='text_extracted', characters=len(text), extracted_pages=len(pages),
                      marker_passages=len(hits), text_sha256=hashlib.sha256(text.encode()).hexdigest(),
                      sparse_text_pages=sum(len(p.strip()) < 100 for p in pages))
        if len(text.strip()) < 30 * len(pages):
            result['status'] = 'needs_ocr'
    except Exception as exc:
        result.update(status='extraction_failed', error=str(exc))
    return result


if __name__ == '__main__':
    sources = json.loads((DISCOVERY / 'local-sources.json').read_text()) + json.loads((DISCOVERY / 'web-sources.json').read_text())
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for result in pool.map(process, sources):
            results.append(result)
            print(result['id'], result['status'], result.get('marker_passages', 0), flush=True)
    (ROOT / 'extraction-audit.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
