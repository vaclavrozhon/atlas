"""Read-only source collection and repeatable novelty snapshot for the second pass."""
import concurrent.futures, hashlib, json, pathlib, subprocess, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(__file__).resolve().parent
SOURCES = {
    'median-new': 'https://people.idsia.ch/~grandoni/Pubblicazioni/CGLSS25stoc.pdf',
    'median-old': 'https://drops.dagstuhl.de/storage/00lipics/lipics-vol132-icalp2019/LIPIcs.ICALP.2019.42/LIPIcs.ICALP.2019.42.pdf',
    'frege': 'https://mathweb.ucsd.edu/~sbuss/ResearchWeb/hardFrege/cameraready.pdf',
    'gotsman': 'https://dspace.mit.edu/server/api/core/bitstreams/7f2e32fd-d615-4dba-97be-f26cd30ca234/content',
    'alignment': 'https://i.cs.hku.hk/~chin/paper/encycl_msa-1.pdf',
    'euler-old': 'https://drops.dagstuhl.de/storage/00lipics/lipics-vol045-fsttcs2015/LIPIcs.FSTTCS.2015.246/LIPIcs.FSTTCS.2015.246.pdf',
    'testing': 'https://www.wisdom.weizmann.ac.il/~oded/R1/open.pdf',
    'dp-old': 'https://proceedings.mlr.press/v247/cohen24b/cohen24b.pdf',
    'scheduling-truthful': 'https://ora.ox.ac.uk/objects/uuid%3A814fc511-99e2-47cb-b06a-f472630996dc/files/r9593tw016',
    'monadic-old': 'https://ieee-focs.org/FOCS-2023-Papers/pdfs/FOCS2023-35YPEGokY3iqqos5xlCDsn/189400a663/189400a663.pdf',
    'monadic-new': 'https://mccarty.math.gatech.edu/McCarty-2025-Oberwolfach.pdf',
    'turing': 'https://preprint.math.uni-hamburg.de/public/papers/hbm/hbm770.pdf',
    'dnf': 'https://capelli.me/publi/hdr.pdf',
    'sroiq': 'https://ceur-ws.org/Vol-2373/paper-25.pdf',
    'rip': 'https://users.math.msu.edu/users/iwenmark/Teaching/MTH994/Holger_Simon_book.pdf',
    'svg-algorithms': 'https://repository.gatech.edu/server/api/core/bitstreams/cef65e25-7827-4bfc-9148-dc1b4c35c618/content',
}

def fetch(item):
    key, url = item
    pdf = OUT / 'sources' / (key + '.pdf')
    txt = pdf.with_suffix('.txt')
    try:
        if not pdf.exists():
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=45) as response:
                data = response.read()
            if not data.startswith(b'%PDF'):
                return {'key': key, 'url': url, 'error': 'Response was not a PDF'}
            pdf.write_bytes(data)
        subprocess.run(['pdftotext', '-layout', str(pdf), str(txt)], check=True, capture_output=True)
        return {'key': key, 'url': url, 'text': str(txt.relative_to(OUT))}
    except Exception as e:
        return {'key': key, 'url': url, 'error': str(e)}

if __name__ == '__main__':
    (OUT / 'sources').mkdir(exist_ok=True)
    raw = (ROOT / 'site/catalog.json').read_bytes()
    catalog = json.loads(raw)
    prior_small = json.loads((ROOT / 'research/fundamental-small-20260910/shortlist.json').read_text())
    prior_large = json.loads((ROOT / 'research/fundamental-additions-20260910/candidates.json').read_text())
    snapshot = {'as_of': '2026-09-10', 'catalog_sha256': hashlib.sha256(raw).hexdigest(),
                'catalog_meta': catalog['meta'], 'catalog_count': len(catalog['cards']),
                'prior_small_count': len(prior_small), 'prior_large_count': len(prior_large['entries']),
                'prior_large_titles': [e['title'] for e in prior_large['entries']],
                'prior_small_titles': [e['title'] for e in prior_small]}
    (OUT / 'baseline.json').write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(fetch, SOURCES.items()))
    (OUT / 'source-downloads.json').write_text(json.dumps(results, indent=2) + '\n')
    for result in results:
        print(json.dumps(result))
