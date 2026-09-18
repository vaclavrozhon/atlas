"""Consolidate the user-selected older RIP milestone into the completed optimal target."""
import collections,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import DATE,ref,CRITERIA
from review_queue import read_claims,read_queue,locked,require_claim,finish_claim
from catalog_exports import atomic
from archive_cards import change_activity
from card_schema import reader_record
from publish import validate_record
target='TCS-6662';duplicate='TCS-0987';claim=read_claims(ROOT)[duplicate]
target_hash='95e60591447dd30b83f824cd13a628dd5ce10ed615932e8a88ec0b96bbb9caaa'
reason=('Merged the RIP-construction branch into TCS-6662 by explicit user choice on 18 September 2026. '
 'The older m·polylog(d) row target is retained there as a weaker milestone of the active optimal-row deterministic RIP problem, with the Kanpur 2006 source. '
 'The generic multi-question record is archived as an editorial consolidation, not as a claim that RIP construction or arbitrary Fourier-submatrix multiplication is resolved.')
checked=[
 'Read Sublinear.info Problem 21 in the saved current source compilation: all three RIP questions and all three Fourier-submatrix multiplication variants.',
 'Inspected the completed TCS-6662 statement, exact rational output convention and its individually checked 2011–2026 references.',
 'Checked the implication from the active target to the old milestone: multiply by rational 3/2 to obtain squared-norm bounds between 1 and 4, and use ln(eN/s) <= 1+ln N.',
]
with locked(ROOT):
 require_claim(ROOT,duplicate,claim['token']);assert target not in read_claims(ROOT)
 p=ROOT/'data/cards'/f'{target}.json';original_target=p.read_bytes();assert hashlib.sha256(original_target).hexdigest()==target_hash
 original=(ROOT/'data/cards'/f'{duplicate}.json').read_bytes();assert hashlib.sha256(original).hexdigest()==claim['input_sha256']
 q=read_queue(ROOT);row=next(r for r in q['records'] if r['id']==target);assert row['state']=='completed' and row['output_sha256']==target_hash
 c=json.loads(original_target)
 c['references'].append(ref('strauss2006','Problem 21: Deterministic Heavy-Hitters & Fast Matrix Algorithms','Martin Strauss',2006,'https://sublinear.info/21','Kanpur 2006; first RIP construction question. Full source checked in the saved Sublinear.info compilation; the separate Fourier-multiplication questions are not adopted.'))
 c.setdefault('source_consolidations',[]).append(dict(from_id=duplicate,reviewed_on=DATE,note=reason))
 c['related_problem_ids']=[i for i in c.get('related_problem_ids',[]) if i!=duplicate]
 c.setdefault('context_blocks',[]).append(dict(text=r'''An older milestone, posed by Strauss at Kanpur 2006 and formerly indexed as TCS-0987, asks for a deterministic polynomial-time construction of a matrix with \(N\) columns and at most \(C s(\log_2(N+2))^a\) rows for fixed constants \(C,a\), preserving every \(s\)-sparse Euclidean norm within a factor of two after normalization. A precise rational-output specialization asks \(\|x\|_2\le\|Mx\|_2\le2\|x\|_2\) for every such vector. This card's optimal-row target implies that milestone: for its matrix \(A\), the rational scaling \(M=(3/2)A\) gives \((3/2)\|x\|_2^2\le\|Mx\|_2^2\le3\|x\|_2^2\), and \(\ln(eN/s)\le1+\ln N\). The weaker milestone does not conversely establish the optimal row count. The source also asks about certification and fast multiplication of Fourier submatrices; those separate questions are not additional requirements of the present construction target.''',citation='strauss2006'))
 c['statement_review']['notes'].append(reason);c['quality_review']['changes'].append(reason);c['quality_review']['checked_sources'].extend(checked)
 c['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
 validate_record(reader_record(c,CRITERIA),p,CRITERIA)
 out=json.dumps(c,ensure_ascii=False,indent=2)+'\n';row['output_sha256']=hashlib.sha256(out.encode()).hexdigest()
 atomic(p,out);atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as f:f.write(json.dumps(dict(id=target,date=DATE,outcome='source_consolidation_amendment',changes=[reason],sources_checked=checked,input_sha256=target_hash,output_sha256=row['output_sha256']),ensure_ascii=False)+'\n')
print(change_activity([duplicate],reason=reason))
with locked(ROOT):
 p=ROOT/'data/archive/cards'/f'{duplicate}.json';assert p.read_bytes()==original
 q=read_queue(ROOT);row=next(r for r in q['records'] if r['id']==duplicate);assert row['state']=='pending'
 row.update(state='completed',completed_on=DATE,review_input_sha256=claim['input_sha256'],output_sha256=hashlib.sha256(original).hexdigest(),output_path=str(p.relative_to(ROOT)),consolidated_into=target)
 q['counts']=dict(total=len(q['records']),**dict(collections.Counter(r['state'] for r in q['records'])))
 atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as f:f.write(json.dumps(dict(id=duplicate,date=DATE,outcome='merged_after_individual_review',consolidated_into=target,changes=[reason],sources_checked=checked,input_sha256=claim['input_sha256'],output_path=str(p.relative_to(ROOT))),ensure_ascii=False)+'\n')
 finish_claim(ROOT,duplicate,claim['token'],q);print(duplicate,q['counts'])
