"""Collect primary-source papers, retaining full text privately for research."""
import argparse, concurrent.futures, hashlib, json, re, sys, time
from pathlib import Path
from urllib.parse import urljoin
import requests, subprocess
from bs4 import BeautifulSoup
BASE=Path(__file__).resolve().parent
for folder in ['cache','papers','pdfs','research','site']:(BASE/folder).mkdir(exist_ok=True)
def get(url,suffix='.html'):
    p=BASE/'cache'/(hashlib.sha256(url.encode()).hexdigest()[:24]+suffix)
    if p.exists():return p.read_bytes()
    for attempt in range(3):
        try:
            r=requests.get(url,timeout=45);r.raise_for_status()
            p.write_bytes(r.content);return r.content
        except Exception:
            if attempt==2:raise
            time.sleep(1+attempt)
def eprint_page(year,offset):
    url=f'https://eprint.iacr.org/{year}/?offset={offset}'
    s=BeautifulSoup(get(url),'html.parser');out=[]
    for ab in s.select('.paper-abstract'):
        m=re.fullmatch(r'abstract-(\d{4})-(\d+)',ab.get('id',''))
        if not m:continue
        parent=ab.parent.parent;title=parent.select_one('.papertitle');au=parent.select_one('.summaryauthors');cat=parent.select_one('.category')
        if not title:continue
        key=f'{m[1]}/{m[2]}'
        out.append(dict(key='eprint-'+key.replace('/','-'),doi='eprint:'+key,title=title.get_text(' ',strip=True),authors=au.get_text(' ',strip=True) if au else '',year=int(m[1]),venue='Cryptology ePrint',category=cat.get_text(' ',strip=True) if cat else '',abstract=ab.get_text(' ',strip=True),source_url='https://eprint.iacr.org/'+key,pdf_url='https://eprint.iacr.org/'+key+'.pdf',classifications=[]))
    offsets=[int(m[1]) for a in s.select('a[href]') if (m:=re.search(r'offset=(\d+)',a['href']))]
    return out,max(offsets,default=0)
def eprint_metadata():
    allrows=[];jobs=[]
    for year in [2026,2025,2024,2023]:
        rows,last=eprint_page(year,0);allrows+=rows
        jobs += [(year,o) for o in range(100,last+1,100)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        fs={ex.submit(eprint_page,*j):j for j in jobs}
        for i,f in enumerate(concurrent.futures.as_completed(fs),1):
            try:allrows+=f.result()[0]
            except Exception as e:print('metadata failed',fs[f],str(e),flush=True)
            if i%10==0:print('eprint pages',i,'/',len(jobs),'papers',len(allrows),flush=True)
    rows={r['doi']:r for r in allrows}
    (BASE/'eprint_metadata.json').write_text(json.dumps(list(rows.values()),ensure_ascii=False,indent=2))
    print('eprint metadata',len(rows),flush=True)
def focs_metadata():
    rows=[]
    for year in range(2021,2026):
        url=f'https://ieee-focs.org/FOCS-{year}-Papers/'
        txt=get(url+'data/data.js','.js').decode()
        d,_=json.JSONDecoder().raw_decode(txt.split('data:',1)[1].lstrip())
        for section in d['conferences'][0]['sections']:
            for item in section['lineItems']:
                if item.get('type')!='authorPaper':continue
                doi=re.search(r'10\.1109/[A-Za-z0-9./_-]+',item['searchText'])[0].rstrip('.')
                rows.append(dict(key='focs-'+str(year)+'-'+str(item['pageNumber']),doi=doi,title=item['text'],authors=item.get('authorNames',''),year=year,venue='FOCS',abstract=item.get('abstract',''),source_url='https://doi.org/'+doi,pdf_url=urljoin(url,item['articleLocation']),classifications=[]))
    (BASE/'focs_metadata.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print('FOCS metadata',len(rows),flush=True)
def quantum_metadata():
    url='https://api.crossref.org/journals/2521-327X/works?rows=1000&filter=from-pub-date:2021-01-01&sort=published&order=desc'
    data=json.loads(get(url,'.json'));rows=[]
    for x in data['message']['items']:
        date=x.get('published',{}).get('date-parts',[[0]])[0]
        if date>[2026,9,10]:continue
        doi=x['DOI'];url='https://doi.org/'+doi
        rows.append(dict(key='quantum-'+doi.split('-')[-1],doi=doi,title=' '.join(x.get('title',[])),authors='; '.join(a.get('given','')+' '+a.get('family','') for a in x.get('author',[])),year=date[0],venue='Quantum',abstract=BeautifulSoup(x.get('abstract',''),'html.parser').get_text(' ',strip=True),source_url=url,pdf_url='',classifications=['Quantum computation'],license=[v.get('URL','') for v in x.get('license',[])],crossref=x))
    (BASE/'quantum_metadata.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print('Quantum metadata',len(rows),'of',data['message']['total-results'],flush=True)
def download(r):
    out=BASE/'papers'/(r['key']+'.json')
    if out.exists():return 'cached'
    try:
        if r['venue']=='Cryptology ePrint':
            s=BeautifulSoup(get(r['source_url']),'html.parser');txt=s.get_text(' ',strip=True)
            r['license']=[a.get('href','') for a in s.select('a[href]') if 'creativecommons.org/licenses/' in a['href']]
            r['history']=txt[txt.find('History'):txt.find('Short URL')] if 'History' in txt else ''
            r['publication_info']=txt[txt.find('Publication info'):txt.find('Keywords')] if 'Publication info' in txt else ''
        elif r['venue']=='Quantum':
            s=BeautifulSoup(get(r['source_url']),'html.parser')
            m=s.find('meta',attrs={'name':'citation_pdf_url'})
            links=[a['href'] for a in s.select('a[href]') if re.search(r'\.pdf(?:$|\?)',a['href'])]
            r['pdf_url']=m['content'] if m else links[0] if links else ''
            if not r['pdf_url']:return 'no pdf'
        raw=get(r['pdf_url'],'.pdf')
        if not raw.startswith(b'%PDF'):return 'not pdf'
        converted=subprocess.run(['pdftotext','-layout','-','-'],input=raw,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=90,check=True)
        r['pages']=converted.stdout.decode('utf-8',errors='replace').split('\f')
        if r['pages'] and not r['pages'][-1].strip():r['pages'].pop()
        r['source_file']=str(out);r['retrieved']='2026-09-10'
        if not r.get('license'):
            r['license']=['https://creativecommons.org/licenses/by/4.0/'] if re.search(r'Creative Commons Attribution|CC.BY.4',r['pages'][0],re.I) else []
        out.write_text(json.dumps(r,ensure_ascii=False));return 'ok'
    except Exception as e:return str(e)[:200]
def download_batch(kind):
    rows=json.loads((BASE/f'{kind}_metadata.json').read_text())
    if kind=='eprint':
        # Theory first. Exclude application/hardware/security-evaluation categories.
        rows=[r for r in rows if r.get('category') in ['Foundations','Public-key cryptography','Secret-key cryptography','Protocols','Unknown'] or re.search(r'quantum|coding|list.decod|complexity|lower bound|obfuscat|zero.knowledge|succinct|randomness|one.way|information.theoretic',r['title'],re.I)]
    rows.sort(key=lambda r:-r['year']);audit=[]
    print('Downloading',kind,len(rows),flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        futures={ex.submit(download,r):r for r in rows}
        for i,f in enumerate(concurrent.futures.as_completed(futures),1):
            r=futures[f];status=f.result();audit.append(dict(doi=r['doi'],status=status))
            if i%50==0:print(kind,i,'/',len(rows),'ok',sum(x['status'] in ['ok','cached'] for x in audit),flush=True)
    (BASE/f'{kind}_download_audit.json').write_text(json.dumps(audit,indent=2))

def eccc_metadata():
    rows=[]
    for year in [2026,2025,2024,2023]:
        url=f'https://eccc.weizmann.ac.il/year/{year}/'
        s=BeautifulSoup(get(url),'html.parser')
        for box in s.find_all('div',id='box'):
            a=box.find('a',href=re.compile(r'/report/\d{4}/\d+'))
            if not a:continue
            key=a['href'].strip('/').replace('report/','')
            sm=box.find('small');au=sm.get_text(' ',strip=True) if sm else ''
            au=re.sub(r'^TR\d+-\d+.*?\d{4}\s*','',au)
            source='https://eccc.weizmann.ac.il/report/'+key+'/'
            rows.append(dict(key='eccc-'+key.replace('/','-'),doi='ECCC:'+key,title=a.get_text(' ',strip=True),authors=au,year=year,venue='ECCC',abstract='',source_url=source,pdf_url=source+'download/',classifications=[]))
        time.sleep(1)
    (BASE/'eccc_metadata.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print('ECCC metadata',len(rows),flush=True)
    # One request at a time with an explicit pause to respect the archive.
    audit=[]
    for i,r in enumerate(rows,1):
        result=download(r);audit.append(dict(doi=r['doi'],status=result))
        if '429' in result:
            print('Rate limit: stopping ECCC downloads.',flush=True);break
        if i%25==0:print('ECCC',i,'/',len(rows),'ok',sum(x['status'] in ['ok','cached'] for x in audit),flush=True)
        time.sleep(.8)
    (BASE/'eccc_download_audit.json').write_text(json.dumps(audit,indent=2))
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('task');a=parser.parse_args()
    if a.task=='eprint':eprint_metadata();download_batch('eprint')
    elif a.task=='focs':focs_metadata();download_batch('focs')
    elif a.task=='quantum':quantum_metadata();download_batch('quantum')
    elif a.task=='eccc':eccc_metadata()
