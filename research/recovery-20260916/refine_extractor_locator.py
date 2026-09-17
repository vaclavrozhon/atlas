"""Correct a source page locator and clarify the summary's entropy parentheses."""
import fcntl,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import DATE,CRITERIA,reader_record,validate_record,atomic
identifier='TCS-5202'
note='Corrected the operator-space open-problems section locator from p. 10 to p. 9 after checking PDF page boundaries; clarified the summary that C multiplies the entire entropy sum. The formal statement is unchanged.'
with (ROOT/'.publish.lock').open('a') as lock:
 fcntl.flock(lock,fcntl.LOCK_EX)
 p=ROOT/'data/cards'/f'{identifier}.json';data=p.read_bytes();c=json.loads(data)
 assert '§III p. 10' in json.dumps(c,ensure_ascii=False)
 c=json.loads(json.dumps(c,ensure_ascii=False).replace('§III p. 10','§III p. 9'))
 c['working_summary']['sentences'][1]='The selected target increases required min-entropy to C times the sum of k and log base two of one over epsilon, and allows trace-distance error at most C times m times the square root of epsilon.'
 c['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
 c['quality_review']['changes'].append(note)
 c['statement_review']['notes'].append(note)
 validate_record(reader_record(c,CRITERIA),p,CRITERIA)
 output=json.dumps(c,ensure_ascii=False,indent=2)+'\n'
 qpath=ROOT/'research/card-completion-20260913/queue.json';q=json.loads(qpath.read_text())
 r=next(r for r in q['records'] if r['id']==identifier)
 assert r['state']=='completed' and r['output_sha256']==hashlib.sha256(data).hexdigest()
 r['output_sha256']=hashlib.sha256(output.encode()).hexdigest()
 atomic(p,output);atomic(qpath,json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (qpath.parent/'reviews.jsonl').open('a') as f:
  f.write(json.dumps(dict(id=identifier,date=DATE,outcome='locator_and_summary_correction',changes=[note],input_sha256=hashlib.sha256(data).hexdigest(),output_sha256=r['output_sha256']),ensure_ascii=False)+'\n')
 print(identifier,'locator and summary corrected; completion counts unchanged')
