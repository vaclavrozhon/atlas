"""Make the finite small-input part of the saved HS RAM convention well-defined."""
import fcntl,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import DATE,CRITERIA,reader_record,validate_record,atomic
identifier='TCS-6599'
old=r'Use a word RAM with word length \(w=\lceil4\log_2(n+2)\rceil\).'
new=r'''Use a word RAM with word length
\[
w=\max\!\left\{\lceil4\log_2(n+2)\rceil,\ \lceil\log_2(2nd+n+d+8)\rceil\right\}.
\]
The second term ensures that the full explicit input and its headers fit in the address universe even for small \(n\) and a large fixed dimension constant \(c\). For every fixed \(c\), it is eventually dominated by the first term, so this finite-input correction leaves the stated asymptotic time hypothesis unchanged.'''
note='Corrected a finite-input address issue: for very large fixed c and small n, 4 log(n+2)-bit addresses could not hold the supplied vectors or dimension header. Word length now also covers the explicit input size. For each fixed c this extra term disappears for all sufficiently large n, so no asymptotic bound, dimension quantifier or algorithmic target is changed.'
with (ROOT/'.publish.lock').open('a') as lock:
 fcntl.flock(lock,fcntl.LOCK_EX)
 p=ROOT/'data/cards'/f'{identifier}.json';data=p.read_bytes();c=json.loads(data)
 assert old in c['definitions']
 c['definitions']=c['definitions'].replace(old,new,1)
 c['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
 c['formulation_reviewed_on']=DATE
 c['quality_review']['changes'].append(note)
 c['quality_review']['reviewed_on']=DATE
 c['statement_review'].setdefault('notes',[]).append(note)
 c['statement_review']['reviewed_on']=DATE
 validate_record(reader_record(c,CRITERIA),p,CRITERIA)
 output=json.dumps(c,ensure_ascii=False,indent=2)+'\n'
 qpath=ROOT/'research/card-completion-20260913/queue.json';q=json.loads(qpath.read_text())
 r=next(r for r in q['records'] if r['id']==identifier)
 assert r['state']=='completed' and r['output_sha256']==hashlib.sha256(data).hexdigest()
 r['output_sha256']=hashlib.sha256(output.encode()).hexdigest()
 atomic(p,output);atomic(qpath,json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (qpath.parent/'reviews.jsonl').open('a') as f:
  f.write(json.dumps(dict(id=identifier,date=DATE,outcome='finite_input_model_correction',changes=[note],input_sha256=hashlib.sha256(data).hexdigest(),output_sha256=r['output_sha256']),ensure_ascii=False)+'\n')
 print(identifier,'finite-input address correction; completion counts unchanged')
