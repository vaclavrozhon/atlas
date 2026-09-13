"""Retrieve the three conference streams directly from the public DBLP graph."""
import collections
import concurrent.futures
import csv
import json
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent
ENDPOINT = 'https://sparql.dblp.org/sparql'


def fetch(venue):
    query = f'''PREFIX dblp: <https://dblp.org/rdf/schema#>
SELECT DISTINCT ?paper ?title ?toc ?author ?name WHERE {{
  ?paper a dblp:Inproceedings ;
    dblp:publishedInStream <https://dblp.org/streams/conf/{venue}> ;
    dblp:listedOnTocPage ?toc ; dblp:title ?title ; dblp:authoredBy ?author .
  ?author dblp:primaryCreatorName ?name .
}}'''
    (ROOT / 'sources' / f'{venue}.sparql').write_text(query)
    response = requests.get(ENDPOINT, params={'query': query, 'format': 'json'},
                            headers={'Accept': 'application/sparql-results+json'}, timeout=90)
    response.raise_for_status()
    data = response.json()
    (ROOT / 'sources' / f'{venue}-raw.json').write_text(json.dumps(data, ensure_ascii=False))
    out = {}
    for binding in data['results']['bindings']:
        row = {key: val['value'] for key, val in binding.items()}
        toc = row['toc'].rstrip('/').removesuffix('.html')
        tail = toc.rsplit('/', 1)[-1]
        if not tail.startswith(venue) or not tail[len(venue):].isdigit():
            continue
        year = int(tail[len(venue):])
        if not 2011 <= year <= 2026:
            continue
        entry = out.setdefault(row['paper'], dict(paper=row['paper'], title=row['title'],
                               venue=venue, year=year, toc=toc, authors={}))
        entry['authors'][row['author']] = row['name']
    print(venue, 'rows', len(data['results']['bindings']), 'metadata', data.get('meta'),
          'retained papers', len(out), flush=True)
    return list(out.values())


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(3) as pool:
        papers = [p for batch in pool.map(fetch, ['stoc', 'focs', 'soda']) for p in batch]
    (ROOT / 'papers.json').write_text(json.dumps(papers, ensure_ascii=False, indent=2))
    authors = {}
    counts = collections.Counter()
    for p in papers:
        counts[p['venue'], p['year']] += 1
        for pid, name in p['authors'].items():
            a = authors.setdefault(pid, dict(pid=pid, name=name, total=0, recent=0,
                                            stoc=0, focs=0, soda=0, papers_2026=0, fractional=0))
            if p['year'] == 2026:
                a['papers_2026'] += 1
                continue
            a['total'] += 1
            a[p['venue']] += 1
            a['recent'] += p['year'] >= 2021
            a['fractional'] += 1 / len(p['authors'])
    authors = sorted(authors.values(), key=lambda a: a['total'], reverse=True)
    (ROOT / 'authors.json').write_text(json.dumps(authors, ensure_ascii=False, indent=2))
    with (ROOT / 'conference-coverage.csv').open('w') as out:
        w = csv.writer(out)
        w.writerow(['venue', 'year', 'papers'])
        w.writerows((v, y, n) for (v, y), n in sorted(counts.items()))
    print('TOTAL', len(papers), 'AUTHORS', len(authors), 'VENUE YEARS', len(counts))
    print('COVERAGE', sorted(counts.items()))
    for i, a in enumerate(authors[:400], 1):
        print(i, a['name'], a['total'], a['stoc'], a['focs'], a['soda'],
              'recent', a['recent'], '2026', a['papers_2026'])
