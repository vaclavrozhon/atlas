"""Parse cached primary proceedings metadata; never execute publisher JavaScript."""
import json, re, sys
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
sys.path.insert(0, str(BASE.parent / 'expand'))
from taxonomy import classify, RULES

records, excluded, sources = [], [], []
def clean(s):
    return re.sub(r'\s+', ' ', BeautifulSoup(s, 'html.parser').get_text(' ', strip=True)).strip()

for src in json.loads((BASE / 'discovery.json').read_text()):
    m = re.search(r'stoc(202[2-6])/toc', src['url'])
    if not m: continue
    year = int(m[1])
    soup = BeautifulSoup((ROOT / src['file']).read_text(), 'html.parser')
    n = 0
    for a in soup.select('a.DLtitleLink'):
        h = a.find_parent('h3')
        section = h.find_previous('h2').get_text(' ', strip=True)
        if re.search(r'keynote|invited talk', section, re.I):
            excluded.append(dict(venue='STOC', year=year, title=clean(a.get_text(' ')), reason=section))
            continue
        n += 1
        siblings = []
        for s in h.next_siblings:
            if getattr(s, 'name', '') in ('h2','h3'): break
            siblings.append(str(s))
        block = BeautifulSoup(''.join(siblings), 'html.parser')
        ab = block.select_one('.DLabstract')
        authors = [e.get_text(' ',strip=True) for e in block.select('li.nameList')]
        doi = a['href'].split('/doi/')[-1]
        records.append(dict(id=f'STOC-{year}-{n:03d}',venue='STOC',year=year,title=clean(a.get_text(' ')),authors='; '.join(authors),abstract=clean(str(ab)) if ab else '',doi=doi,url='https://doi.org/'+doi,source_url=src['url'],metadata_url=src['url'],session=section))
    sources.append(dict(venue='STOC',year=year,url=src['url'],metadata_url=src['url'],count=n,cache_file=src['file']))

for name in ['discovery_data.json','discovery_data_more.json']:
    for src in json.loads((BASE / name).read_text()):
        m = re.search(r'FOCS-(202[1-5])-Papers/data/data.js',src['url'])
        if not m: continue
        year = int(m[1])
        raw = (ROOT / src['file']).read_text()
        data, _ = json.JSONDecoder().raw_decode(raw.split('data:',1)[1].lstrip())
        conf = data['conferences'][0]
        assert int(conf['year']) == year
        n = 0
        source = f'https://ieee-focs.org/FOCS-{year}-Papers/'
        for section in conf['sections']:
            for item in section['lineItems']:
                if item.get('type') != 'authorPaper':
                    excluded.append(dict(venue='FOCS',year=year,title=item.get('text',''),reason=item.get('type','')))
                    continue
                n += 1
                doi = re.search(r'10\.1109/[A-Za-z0-9./_-]+', item.get('searchText',''))
                doi = doi[0].rstrip('.') if doi else ''
                records.append(dict(id=f'FOCS-{year}-{n:03d}',venue='FOCS',year=year,title=clean(item['text']),authors=clean(item.get('authorNames','')),abstract=clean(item.get('abstract','')),doi=doi,url='https://doi.org/'+doi if doi else urljoin(source,item['articleLocation']),source_url=source,metadata_url=src['url'],session=section['title']))
        sources.append(dict(venue='FOCS',year=year,url=source,metadata_url=src['url'],count=n,cache_file=src['file']))

records.sort(key=lambda x:(x['venue'],x['year'],x['id']))
assert len({r['id'] for r in records}) == len(records)
assert len({r['doi'] for r in records if r['doi']}) == sum(bool(r['doi']) for r in records)
for r in records:
    r['initial_area'] = classify(dict(paper_title=r['title'],selected_sentence='',classifications=[],venue=r['venue']))
    r['title_matches'] = [a for a,p in RULES if re.search(p,r['title'],re.I)]
    r['area'] = r['initial_area']
    r['classification_method'] = 'title_heuristic'
    r['classification_note'] = ''

(BASE/'papers_internal.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
(BASE/'sources.json').write_text(json.dumps(sorted(sources,key=lambda x:(x['venue'],x['year'])),indent=2))
(BASE/'excluded.json').write_text(json.dumps(excluded,ensure_ascii=False,indent=2))
print('COUNTS',sorted(Counter((r['venue'],r['year']) for r in records).items()))
print('TOTAL',len(records),'abstracts',sum(bool(r['abstract']) for r in records),'doi',sum(bool(r['doi']) for r in records))
print('EXCLUDED',excluded)
print('INITIAL AREAS',Counter(r['area'] for r in records).most_common())
