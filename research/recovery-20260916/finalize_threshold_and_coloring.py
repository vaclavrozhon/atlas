"""Apply the user's final PRG choice and correct seminar metadata before checkpointing."""
import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import DATE,ref,block,CRITERIA,reader_record,validate_record,atomic
from review_queue import locked
with locked(ROOT):
 qp=ROOT/'research/card-completion-20260913/queue.json';q=json.loads(qp.read_text());events=[]
 for identifier in ['TCS-3958','TCS-0597']:
  p=ROOT/'data/cards'/f'{identifier}.json';raw=p.read_bytes();before=hashlib.sha256(raw).hexdigest();c=json.loads(raw)
  row=next(r for r in q['records'] if r['id']==identifier);assert row['state']=='completed' and row['output_sha256']==before
  if identifier=='TCS-3958':
   c['title']='Polynomial-stretch PRGs for depth-two threshold circuits with superlinear gate count'
   c['formal']=r'''Do there exist a rational constant \(\delta\in(0,1)\), positive integers \(a,K,n_0\), and one deterministic algorithm \(G\) such that, for every integer \(n\ge n_0\), writing \(r(n)=\lfloor n^{1-\delta}\rfloor\), the map
\[
G_n:\{0,1\}^{r(n)}\longrightarrow\{0,1\}^n,\qquad G_n(s)=G(1^n,s),
\]
is computed in at most \(K(n+2)^a\) bit operations and, for every depth-at-most-two linear-threshold circuit \(C\) on \(n\) input bits with at most \(\lfloor n^{1+\delta}\rfloor\) gates,
\[
\left|\Pr[C(G_n(U_{r(n)}))=1]-\Pr[C(U_n)=1]\right|\le\frac1{10}?
\]
Here \(U_j\) is the uniform distribution on \(j\) independent fair bits. The size bound counts gates, with no separate restriction on their fan-in or the number of wires.'''
   old='The seed is exactly \\(n-1\\) bits; any uniformly computable generator using fewer bits can ignore padding bits, so this captures a saving of at least one bit.'
   assert old in c['definitions']
   c['definitions']=c['definitions'].replace(old,r'The seed has exactly \(r(n)=\lfloor n^{1-\delta}\rfloor\) bits; a generator using fewer bits can ignore padding. Since \(\delta\) is a fixed rational, the integer length function can be computed exactly in polynomial bit time. The same positive constant is used for the seed saving and the gate exponent; allowing two positive constants is equivalent after decreasing to their minimum and padding the seed.')
   c['answer_criterion']='Give a complete mathematically correct Lean-checked construction and proof of the displayed generator guarantee, or a complete Lean-checked refutation of its existence. Verify uniform polynomial bit time, a fixed positive superlinear gate exponent, polynomial seed stretch and the worst-circuit error bound. A generator saving only one bit, a result for a smaller wire-bounded class or an exponential-time acceptance estimator is insufficient.'
   c['source_formulation']['text']='The source asks for a nontrivial PRG for depth-two LTF circuits with a superlinear number of gates. The user’s final choice on 18 September 2026 fixes seed length at most n^(1−delta), at most n^(1+delta) gates, error 1/10 and polynomial bit time for a fixed delta>0. This explicitly supersedes the earlier one-bit-saving choice after the weaker target was identified as a consequence of the 2016 average-case lower bound. The source does not itself state these exact constants.'
   c['importance']['reason']='A standard shallow-circuit derandomization barrier with a consequential gate-versus-wire distinction; polynomial stretch against a superlinear number of arbitrary-weight gates would go beyond the elementary one-bit generator from average-case hardness.'
   c['references'].append(ref('onebit','Super-Linear Gate and Super-Quadratic Wire Lower Bounds for Depth-Two and Depth-Three Threshold Circuits','Daniel M. Kane; Ryan Williams',2016,'https://cseweb.ucsd.edu/~dakane/depth2LTF.pdf','§1.1, Theorem 1.1 and the Andreev-function definition, p.2'))
   c['context_blocks'].append(block(r'The 2016 theorem gives an efficiently computable function with small correlation against a superlinear number of depth-two threshold gates. The elementary hard-bit construction \(s\mapsto(s,h(s))\) therefore gives a one-bit generator: fixing the last input of a putative distinguisher to zero or one turns its advantage into a difference of correlations with \(h\). This observation is the editorial reason for replacing the initial one-bit milestone with polynomial stretch. It is not a claim that appending many such bits automatically preserves the two-layer circuit class.','onebit'))
   c['working_summary']['sentences']=['The circuit class has at most two layers of gates that compare weighted sums against thresholds.','The question allows a fixed superlinear number of gates with arbitrary real weights and unrestricted fan-in.','One uniform polynomial-time generator must produce n bits from at most n^(1−delta) random bits for a fixed positive delta.','Every circuit in the class must distinguish that output from uniform with advantage at most one tenth.','The target asks for polynomial stretch beyond the one-bit construction obtainable from known average-case hardness.']
   c['working_summary']['source_refs'].append('onebit')
   c['status_note']='Source-open as the superlinear-gate PRG program in the 2018 source. Bounded primary-source checks through 18 September 2026 found no verified resolution of the user-selected polynomial-stretch formulation. The initially proposed one-bit-saving target was corrected after checking Kane–Williams 2016; the user explicitly selected the stronger target, superseding the earlier choice. Sparse-wire PRGs and the 2026 acceptance estimator do not by themselves meet this formulation.'
   changes=['Applied the user’s final explicit polynomial-stretch choice, superseding the previously confirmed one-bit milestone.','Checked the 2016 average-case theorem and the hard-bit distinguisher calculation; kept the weak consequence as context, not as the active open target.']
   c['quality_review']['checked_sources'].append('Read Kane–Williams 2016 §1.1, the precise Andreev construction and Theorem 1.1; checked why the one-bit construction does not provide polynomial stretch.')
  else:
   r=next(r for r in c['references'] if r['id']=='later');r['authors']='Petr A. Golovach, open-problem contribution; Maria Chudnovsky, Neeldhara Misra, Daniel Paulusma, Oliver Schaudt and Akanksha Agrawal, report editors';r['year']=2023
   r['locator']='Seminar 22481 (2022), published 4 May 2023; §4.2 p.121 (standalone PDF p.13)'
   changes=['Corrected the later seminar report’s editors and publication year from the publisher’s metadata; the seminar took place in 2022 and the report was published in 2023.']
   c['quality_review']['checked_sources'].append('Checked the publisher record for DOI 10.4230/DagRep.12.11.109: publication 4 May 2023 and the complete editor list; the PDF abstract has a seminar-year typo.')
  c['statement_review']['notes'].extend(changes);c['quality_review']['changes'].extend(changes);c['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
  validate_record(reader_record(c,CRITERIA),p,CRITERIA)
  out=json.dumps(c,ensure_ascii=False,indent=2)+'\n';row['output_sha256']=hashlib.sha256(out.encode()).hexdigest();atomic(p,out)
  events.append(dict(id=identifier,date=DATE,outcome='post_review_scope_or_source_correction',changes=changes,input_sha256=before,output_sha256=row['output_sha256']))
 atomic(qp,json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (qp.parent/'reviews.jsonl').open('a') as f:
  for e in events:f.write(json.dumps(e,ensure_ascii=False)+'\n')
 print('Final PRG choice and coloring bibliographic correction recorded.')
