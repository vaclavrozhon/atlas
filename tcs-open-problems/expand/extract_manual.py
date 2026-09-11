from pathlib import Path
import json,re,hashlib,collections
from extract_candidates import extract,blocks,normalize
ROOT=Path(__file__).resolve().parent

def main():
    out=[]
    for f in sorted((ROOT/'manual').glob('*.json')):
        r=json.loads(f.read_text())
        if not r.get('pages'):continue
        r.update(doi='manual:'+r['key'],venue=r['kind'],classifications=[r['area']],source_file=str(f))
        rows=extract(r)
        for pn,p in enumerate(r['pages'],1):
            # Book-specific numbering and explicit unnumbered open-question fields.
            patterns=[]
            if r['key']=='jukna2012':patterns=[r'(?m)^\s*(\d+\.\d+)\s+Research Problem\b']
            if r['key']=='juknasergeev2013':patterns=[r'(?m)^\s*Problem (7\.\d+)\b']
            if r['key']=='etr2024':patterns=[r'(?m)^\s*(Open Questions):']
            for pat in patterns:
                for m in re.finditer(pat,p):
                    block=p[m.end():]
                    stop=re.search(r'\n\s*\n',block)
                    text=normalize(block[:stop.start() if stop else min(len(block),2400)])
                    if len(text.split())<5:continue
                    cid=hashlib.sha256((r['doi']+'|'+str(pn)+'|'+text).encode()).hexdigest()[:16]
                    rows.append(dict(candidate_id=cid,doi=r['doi'],paper_title=r['title'],authors=r.get('authors',''),year=r['year'],venue=r['kind'],classifications=[r['area']],source_url=r['source_url'],pdf_url=r['pdf_url']+f'#page={pn}',source_locator=m.group(0).strip(),page=pn,extraction_kind='explicit_open_book_or_survey_statement',statement=text,context=normalize(p[max(0,m.start()-1200):m.end()+2000]),flags=[],source_file=str(f)))
        for x in rows:x['manual_key']=r['key'];x['area']=r['area']
        out+=rows
    (ROOT/'manual_candidates.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    print('Candidates',len(out),'sources',len(set(x['manual_key'] for x in out)))
    print(json.dumps(dict(collections.Counter(x['manual_key'] for x in out)),indent=2))

if __name__=='__main__':main()
