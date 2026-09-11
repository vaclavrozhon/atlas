"""Conservative extraction of source-stated unresolved questions for review."""
from pathlib import Path
import collections,hashlib,json,re,sys,unicodedata
ROOT=Path(__file__).resolve().parent
NAMED=re.compile(r'^(?:[▶▷▸◀◆■]\s*)?((?:Open\s+(?:Problem|Question)|Research\s+Problem|Conjecture|Question)\s+[A-Z]?\d+(?:\.\d+)*)(?:[.:\s(]|$)',re.I)
EXPLICIT=re.compile(r'\b(?:remain(?:s)?\s+(?:an?\s+)?open|(?:we\s+)?leave\b.{0,110}\bopen|is\s+(?:still\s+)?(?:an?\s+)?open\s+(?:problem|question)|we\s+conjecture|we\s+do\s+not\s+know|it\s+is\s+(?:still\s+)?unknown)\b',re.I)
FINAL=re.compile(r'^(?:\d+(?:\.\d+)*\s+)?(?:Conclu(?:sion|ding)|Open\s+(?:Problems|Questions)|Future\s+(?:Work|Directions)|Discussion|Outlook)',re.I)
STRUCT=re.compile(r'^(?:[▶▷▸◀◆■]\s*)?(?:Theorem|Lemma|Proposition|Corollary|Observation|Definition|Example|Remark|Proof|Fact|Claim)\b',re.I)
RESOLVED=re.compile(r'\b(?:we\s+(?:resolve|answer|settle|disprove|refute|prove)|(?:is|was|has been|have been|were)\s+(?:recently\s+)?(?:solved|settled|resolved|disproved|refuted))\b',re.I)

def normalize(t):
    # Repair PDF typography, without changing words or mathematical claims.
    t=t.replace('\ufb01','fi').replace('\ufb02','fl').replace('\ufb00','ff').replace('\ufb03','ffi').replace('\ufb04','ffl')
    t=re.sub(r'(?<=[a-z])-\s*\n\s*(?=[a-z])','',t)
    return re.sub(r'\s+',' ',t).strip()

def blocks(pages):
    result=[]
    for pn,page in enumerate(pages,1):
        lines=[re.sub(r'[ \t]{3,}','   ',l) if len(l)>600 else l for l in page.splitlines()]
        if pn>1:
            for j,l in enumerate(lines):
                if not l.strip():continue
                if re.match(r'^\s*\d+:\d+\s',l) or re.search(r'\s{3,}\d+:\d+\s*$',l):lines[j]=''
                break
        # Remove conference running footers, but keep displayed mathematics.
        for j,l in enumerate(lines):
            if re.fullmatch(r'[A-Z /-]{3,35}2\s*0\s*2\s*\d',l.strip()):lines[j]=''
        indents=collections.Counter(len(l)-len(l.lstrip()) for l in lines if len(l.strip())>60 and len(l)-len(l.lstrip())<20)
        base=indents.most_common(1)[0][0] if indents else 0
        separated=[]
        for l in lines:
            st=l.strip();indent=len(l)-len(l.lstrip())
            if (indent==base+4 and re.match(r'[A-Z][a-z]+\b',st) and len(st.split())>=4) or (FINAL.match(st) and len(st)<110) or re.fullmatch(r'(?:\d+\s+)?References',st):
                separated.append('')
                separated.append(l)
                if FINAL.match(st) and len(st)<110:separated.append('')
            else:separated.append(l)
        raw='\n'.join(separated)
        chunks=re.split(r'\n[ \t]*\n+',raw)
        for chunk in chunks:
            if not chunk.strip():continue
            # A named statement can follow a prose paragraph without a blank line.
            subs=re.split(r'\n(?=[ \t]*(?:[▶▷▸◀◆■][ \t]*)?(?:Open (?:Problem|Question)|Conjecture|Question|Theorem|Lemma|Proposition|Proof|Remark)\b)',chunk)
            for sub in subs:
                text=normalize(sub)
                if text:result.append(dict(page=pn,text=text,raw=sub.strip()))
    return result

def extract(r):
    bs=blocks(r['pages']); end=len(bs)
    for i,b in enumerate(bs):
        if re.match(r'^(?:\d+\s+)?(?:References|Bibliography)\b',b['text']) and i>5:end=i;break
    final=None
    for i,b in enumerate(bs[:end]):
        if FINAL.match(b['text']) and i>max(5,.45*end) and len(b['text'])<180:final=i
    out=[]; seen=set()
    for i,b in enumerate(bs[:end]):
        t=b['text']; named=NAMED.match(t);explicit=EXPLICIT.search(t)
        # Introductory questions commonly motivate results that the paper proves.
        tail=i>0.55*end
        in_final=final is not None and final<i<end
        kind=None
        if named:
            label=named.group(1)
            if label.lower().startswith(('open','research')):kind='numbered_open_question'
            elif in_final or (explicit or (i and EXPLICIT.search(bs[i-1]['text']))):kind='numbered_unresolved_statement'
        elif explicit and (tail or re.search(r'\bwe leave\b',t,re.I)):kind='explicit_unresolved_passage'
        elif in_final and '?' in t and re.search(r'\b(?:can|does|is|are|could|what|which|how|whether)\b',t,re.I):kind='question_in_open_section'
        if not kind:continue
        if len(t.split())<8 or len(t.split())>300:continue
        if STRUCT.match(t):continue
        if re.search(r'we (?:leave|defer).{0,70}(?:proof|details).{0,70}(?:appendix|full version|reader)',t,re.I):continue
        if re.search(r'open (?:problem|question)s? (?:session|mentioned|discussed|posed)\b',t,re.I) and '?' not in t and not named:continue
        if re.search(r'\b(?:many|several|these|some)\s+(?:interesting\s+)?(?:questions|problems)\s+(?:remain|are)\b',t,re.I) and '?' not in t and not named:continue
        label=named.group(1) if named else f'Unresolved-question passage on page {b["page"]}'
        # Retain flags for review; no risky semantic judgment is hidden.
        context=' '.join(x['text'] for x in bs[max(0,i-1):min(end,i+3)])
        flags=[]
        if RESOLVED.search(t):flags.append('resolution_language_in_passage')
        if RESOLVED.search(' '.join(x['text'] for x in bs[i+1:min(end,i+3)])):flags.append('resolution_language_after_passage')
        if re.search(r'\b(?:this|these|above|our results|the problem|the question)\b',t,re.I):flags.append('requires_source_context')
        if len(re.findall(r'\?',t))>1:flags.append('multiple_question_sentences')
        if t[-1:] not in '.?!:;)”:':flags.append('possible_continuation')
        key=re.sub(r'\W','',t.lower())
        if key in seen:continue
        seen.add(key)
        ident=hashlib.sha256((r['doi']+'|'+key).encode()).hexdigest()[:16]
        out.append(dict(candidate_id=ident,doi=r['doi'],paper_title=r['title'],authors=r.get('authors',[]),year=r['year'],venue=r['venue'],classifications=r.get('classifications',[]),source_url=r['source_url'],pdf_url=r['pdf_url']+f'#page={b["page"]}',source_locator=label,page=b['page'],extraction_kind=kind,statement=t,context=context,flags=flags,source_file=r.get('source_file','')))
    return out

def main():
    out=[];fs=sorted((ROOT/'papers').glob('*.json'))
    cache=ROOT/'extractions-v2';cache.mkdir(exist_ok=True)
    for fi,f in enumerate(fs,1):
        try:r=json.loads(f.read_text())
        except json.JSONDecodeError:continue
        r['source_file']=str(f)
        cp=cache/f.name
        if cp.exists():items=json.loads(cp.read_text())
        else:
            items=extract(r);cp.write_text(json.dumps(items,ensure_ascii=False))
        out+=items
        if fi%200==0:print('Parsed',fi,'/',len(fs),'candidates',len(out),flush=True)
    (ROOT/'lipics_candidates.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    print(json.dumps(dict(papers=len(fs),candidates=len(out),kinds=dict(collections.Counter(x['extraction_kind'] for x in out)),years=dict(collections.Counter(x['year'] for x in out)),flags=dict(collections.Counter(f for x in out for f in x['flags']))),indent=2))

if __name__=='__main__':main()
