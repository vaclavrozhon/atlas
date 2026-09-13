"""Recover the five scanned or badly encoded books for passage screening."""
import concurrent.futures
import json
import os
from pathlib import Path
import subprocess
import tempfile

from extract import ROOT, TEXT, process

TESSERACT = '/tmp/atlas-library-ocr/runtime/usr/bin/tesseract'
ENV = dict(os.environ, TESSDATA_PREFIX='/tmp/atlas-library-ocr/runtime/usr/share/tesseract-ocr/5/tessdata', OMP_THREAD_LIMIT='1')
CACHE = ROOT / 'ocr-pages'
CACHE.mkdir(exist_ok=True)
sources = [s for s in json.loads((ROOT.parent / 'local-sources.json').read_text())
           if s['inventory_index'] in [10, 11, 26, 33, 127]]


def page_text(job):
    source, page = job
    directory = CACHE / source['id']
    directory.mkdir(exist_ok=True)
    saved = directory / f'{page:04d}.txt'
    if saved.exists():
        return
    with tempfile.TemporaryDirectory(prefix='atlas-ocr-') as tmp:
        image = Path(tmp) / 'page'
        subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-r', '130', '-singlefile', '-png', source['local_path'], str(image)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
        result = subprocess.run([TESSERACT, str(image)+'.png', 'stdout', '-l', 'eng'], env=ENV, capture_output=True, check=True, timeout=90)
        saved.write_bytes(result.stdout)


if __name__ == '__main__':
    jobs = [(s, p) for s in sources for p in range(1, s['pages'] + 1)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for n, _ in enumerate(pool.map(page_text, jobs), 1):
            if n % 100 == 0:
                print(f'{n}/{len(jobs)} OCR pages complete', flush=True)
    results = []
    for source in sources:
        text = '\f'.join((CACHE / source['id'] / f'{p:04d}.txt').read_text() for p in range(1, source['pages']+1)) + '\f'
        (TEXT / (source['id']+'.txt')).write_text(text)
        result = process(source)
        result['text_method'] = 'tesseract_5.3.4_english_130dpi'
        results.append(result)
    (ROOT / 'ocr-audit.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print('OCR complete', flush=True)
