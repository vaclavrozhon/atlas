"""Build a provenance-preserving shortlist, not a certification of current openness.

One paper contributes at most one automatically selected question. Exported source
excerpts are limited to 25 words; complete extracted text stays in the research cache.
"""
from pathlib import Path
import collections, hashlib, json, re, unicodedata

ROOT=Path(__file__).resolve().parent
QWORD=re.compile(r'\b(?:Can|Could|Does|Do|Is|Are|What|Which|How|Would|Will)\b')
MARKER=re.compile(r'\b(?:remains? (?:an? )?open|leave.{0,100}open|is (?:still )?(?:an? )?open (?:problem|question)|we conjecture|we do not know|it is (?:still )?unknown)\b',re.I)
GENERIC=re.compile(r'\b(?:paper is organized|organization of the paper|section \d+ (?:defines|discusses|presents)|interesting problems that we leave|many questions.{0,30}remain open|several.{0,40}questions.{0,30}remain open|open problems in this area|future work would be|defer these investigations|more research is needed|we leave.{0,35}(?:proof|details).{0,60}(?:reader|appendix))',re.I)
SOLVED=re.compile(r'\b(?:we (?:show|prove|resolve|settle|answer|refute|disprove|establish)|(?:was|were|has been|have been|is) (?:recently )?(?:resolved|settled|solved|refuted|disproved))\b',re.I)
LABEL=re.compile(r'^(?:[▶▷▸◀◆■]\s*)?(?:Open (?:Problem|Question)|Research Problem|Conjecture|Question)\s+[A-Z]?\d+(?:\.\d+)*(?:\s*\([^)]*\))?\s*[:.]?\s*',re.I)

def norm(s):return re.sub(r'\W','',unicodedata.normalize('NFKC',s).casefold())

def clean(s):
    s=re.sub(r'[\x00-\x1f]',' ',s)
    return re.sub(r'\s+',' ',s).strip(' ▶▷▸◀◆■•')

def sentences(s):
    # Never reconstruct or guess mathematical symbols lost by PDF extraction.
    return [t.strip() for t in re.split(r'(?<=[.!?])\s+(?=[A-Z][a-z]|[A-Z]\b|\d+[.)]\s)',s) if t.strip()]

def choose(x):
    t=clean(x['statement']);named=x['extraction_kind'].startswith('numbered')
    if named:
        t=LABEL.sub('',t)
        if re.match(r'(?:is (?:equivalent|closely|related)|represents|would|was|has been|states|asks|of |in |from |and |can be proved)',t,re.I):return None
    if SOLVED.search(t) and '?' not in t:return None
    if 'resolution_language_after_passage' in x['flags'] and named:return None
    parts=sentences(t); opts=[]
    for j,s in enumerate(parts):
        if GENERIC.search(s):continue
        if re.match(r'^(?:Theorem|Lemma|Proof|Definition|Observation|Example|Proposition)\b',s):continue
        isq='?' in s and bool(re.search(r'(?:^|[:,;]\s*|^\d+[.)]\s*)(?:can|could|does|do|is|are|what|which|how|would|will)\b',s,re.I))
        explicit=bool(MARKER.search(s))
        if not (isq or explicit or (named and j==0)):continue
        if re.search(r'\b(?:we do not know (?:in advance|the value|which .{0,70}(?:need|will))|we leave this open for generality|leaves? open (?:many|several) directions|still remains largely unexplored|since we conjecture|there are still some parameters)\b',s,re.I):continue
        if re.search(r'\b(?:even if we do not know|these problems have particular importance|we conjecture.{0,100}(?:are explained by|relationship between))\b',s,re.I):continue
        if re.search(r'(?:\bof|!|=)\s*\?$',s):continue
        if re.match(r'^(?:Suppose|Assume|Let)\b',s) and not isq:continue
        if re.search(r'\b(?:the following holds|following statement holds)\b',s,re.I):continue
        if re.search(r'^We do not know (?:whether|if) the (?:upper )?bound (?:in|from) Theorem \d+ is tight\.?$',s,re.I):continue
        if s and s[0].islower():continue
        if isq:
            s=s[:s.index('?')+1]
            if re.search(r'(?:\bO|=|∈|φ|ψ)\s*\?$',s):continue
            # A paragraph can start with a numbered item or a brief topic heading.
            m=re.search(r'(?:^|:\s|\d+[.)]\s)(Can|Could|Does|Do|Is|Are|What|Which|How)\b',s)
            if m:s=s[m.start(1):]
        if SOLVED.search(s) and not re.search(r'\b(?:can|could|whether)\s+we\b',s,re.I):continue
        if len(re.findall(r'\b[a-zA-Z]{2,}\b',s))<5:continue
        if len(s.split())>140:continue
        if re.search(r'\b(?:why bother|can you find|as we will see|we discuss next|turns out|the answer is|answer to this question is)\b',s,re.I):continue
        if len(s.split())<12 and re.search(r'\b(?:this|these|it|our|them|same|following|such|imperfect privacy|results are obtained)\b',s,re.I):continue
        if re.search(r'\bwe do not know\b',s,re.I) and not isq and not re.search(r'\b(?:whether|if|how)\b',s,re.I):continue
        if re.search(r'\bwe do not know\b',s,re.I) and re.search(r'\b(?:but one can|but we can|approximate oracle|in advance)\b',s,re.I):continue
        if re.search(r'\bwe conjecture\b',s,re.I) and not named and not re.search(r'\b(?:open|future|conclu|question|interesting)\b',x['context'],re.I):continue
        if explicit and not isq and (len(s.split())<12 or re.search(r'\b(?:these|such|following) (?:interesting )?(?:questions|problems).{0,35}(?:open|future)',s,re.I)):continue
        if not isq and not named and re.search(r'^(?:We leave|We defer|We conjecture that (?:this|it)|It remains open|This remains)',s,re.I):
            if not re.search(r'\b(?:whether|complexity|polynomial|algorithm|conjecture|bound|class|graph|circuit|hardness|parameter|space|time)\b',s,re.I):continue
        score=({'numbered_open_question':80,'numbered_unresolved_statement':65,'explicit_unresolved_passage':55,'question_in_open_section':45}[x['extraction_kind']])
        score+=10*isq+10*explicit
        score-=8*bool(re.search(r'\b(?:this|these|our|above|aforementioned)\b',s,re.I))
        score-=15*bool(s and s[0].islower())
        score-=10*bool(s[-1:] not in '.?!')
        score+=5*(len(s.split())<=25)
        opts.append((score,-len(s),s))
    if not opts:return None
    score,_,s=max(opts)
    if score<35:return None
    return dict(**x,selected_sentence=s,selection_score=score)

def main():
    raw=[]
    decisions={x['candidate_id']:x['reason'] for x in json.loads((ROOT/'review_decisions.json').read_text())}
    v1=json.loads((ROOT.parent/'output-v1-1003/catalog.json').read_text())
    previous_sources={x['source_url'].split('#')[0] for x in v1}
    for f in sorted((ROOT/'extractions-v2').glob('*.json')):
        try:raw+=json.loads(f.read_text())
        except json.JSONDecodeError:pass
    selected=[];rejected=[]
    for x in raw:
        if x['source_url'].split('#')[0] in previous_sources:
            rejected.append(dict(candidate_id=x['candidate_id'],source_url=x['source_url'],reason='This source paper already has a problem entry in v1; conservatively avoid re-indexing its questions.'));continue
        if x['candidate_id'] in decisions:
            rejected.append(dict(candidate_id=x['candidate_id'],source_url=x['source_url'],reason=decisions[x['candidate_id']]));continue
        y=choose(x)
        if y:selected.append(y)
        else:rejected.append(dict(candidate_id=x['candidate_id'],source_url=x['source_url'],reason='No sufficiently specific unresolved question sentence survived automatic screening.'))
    selected.sort(key=lambda x:(-x['selection_score'],-x['year'],x['candidate_id']))
    seen=set();papers=set();kept=[]
    for x in selected:
        key=norm(x['selected_sentence'])
        if key in seen:
            rejected.append(dict(candidate_id=x['candidate_id'],source_url=x['source_url'],reason='Exact repeated question sentence.'));continue
        if x['doi'] in papers:
            rejected.append(dict(candidate_id=x['candidate_id'],source_url=x['source_url'],reason='A stronger passage from this paper was selected; at most one automatic record per paper.'));continue
        seen.add(key);papers.add(x['doi']);kept.append(x)
    (ROOT/'selected_internal.json').write_text(json.dumps(kept,ensure_ascii=False,indent=2))
    (ROOT/'screening_audit.json').write_text(json.dumps(rejected,ensure_ascii=False,indent=2))
    print(json.dumps(dict(raw=len(raw),specific_passages=len(selected),unique_papers=len(kept),years=dict(collections.Counter(x['year'] for x in kept)),kinds=dict(collections.Counter(x['extraction_kind'] for x in kept))),indent=2))

if __name__=='__main__':main()
