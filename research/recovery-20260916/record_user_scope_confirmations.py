"""Record received scope choices without recounting already completed reviews."""
import fcntl, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import CRITERIA,reader_record,validate_record,atomic
DATE='2026-09-18'
CHOICES={
'0560':'Logarithmic-dimension Hitting Set with one source exponent saving common to all fixed dimension constants.',
'6946':'The randomized integer APSP-to-3SUM direction, transferring any fixed subquadratic saving to a fixed subcubic saving.',
'6025':'Existence of an unbounded-treewidth class of easier patterns with host-size exponent o(tw(H)), instead of the broad classification request.',
'6885':'Archive the original constant-overhead second-derivative question with the distinct-output product-polynomial counterexample.',
'6903':'Deterministic noncommutative PIT with polynomial dependence on circuit size and a supplied degree bound D.',
'6890':'Some explicit polynomial-degree family with efficiently computable rational word coefficients, against circuits with arbitrary complex constants.',
'6914':'Retain factorization-to-PIT over Q with the usual univariate factoring operation and archive the resolved reduction question.',
'3318':'No degree restriction; for each fixed prime p, require root-circuit size polynomial in s+n over the algebraic closure of F_p.',
'0010':'One fixed degree and efficiently outputtable rational coefficient lists, against unrestricted complex-constant circuits.',
'1058':'One family and one positive epsilon working for every fixed rank-scale constant c>0, over F_2.',
'5260':'One family and one positive epsilon working for every fixed rank-scale constant c>0, over C with entries in a polynomial-degree number field.',
'0095':'Both the rational recurrence and binary index are input to one uniform deterministic polynomial-bit-time algorithm.',
'4490':'A deterministic polynomial-bit-time algorithm for every fixed matrix dimension, with exponent allowed to depend on dimension.',
'1544':'The qAC^0 versus NL-completeness dichotomy for Cayley-table semigroup membership.',
'1069':'Membership in existential real arithmetic for finite binary inputs to real Zariski-closure membership.',
'5240':'The stated multivariate-to-univariate explicit hardness implication over F_2 with exact finite-field arithmetic.',
'7082':'The source candidate of minimal dominating-set enumeration in K_t-free graphs for some fixed t, outside IncP assuming TFNP differs from FP.',
'7084':'The implication from P differing from NP to both polynomial-space enumeration separations.',
'0659':'The classical SIS reduction from GapSVP with approximation factor O(n^(1-epsilon)) for some fixed positive epsilon.',
'0656':'Classical randomized reduction of factoring a product of two distinct primes to decision GapSVP at the stated n^(2+epsilon) scale.',
'0657':'coNP membership for Euclidean GapSVP at C times sqrt(n/log_2(n+2)).',
'0655':'Retain Euclidean p=2 and the assumption NP is not contained in RP; the separate August 2026 p>2 result does not close this selected question.',
'6868':'Retain the original general NTRU-like reduction question and archive its known positive specialization; do not substitute the narrower unchanged-distribution ternary target.',
'0653':'Quantum SETH with the exact Euclidean SVP lower-bound exponent 0.2075.',
'6861':'Classical same-dimension SIVP-to-LWE with polynomial modulus and the soft-O(n/alpha) approximation scale.',
'6864':'Classical reduction for ideal lattices in power-of-two cyclotomic rings in the stated quantum-reduction parameter range.',
'0187':'For every fixed rational linear-rank inequality, the valid prime characteristics form a finite or cofinite set.',
'0178':'One finite alphabet bound K must work for the entire specified beta=0 entropy face.',
'4802':'Constant positive rate: O(n) total communicated binary bits with a predetermined speaking order and a joint error budget.',
'4968':'A strict asymptotic rate advantage for general binary codes over linear codes at some fixed relative distance, with any positive gap.',
'6738':'Retain the linear-length proof branch after resolution of the locally testable-code branch.',
'6739':'Use a constant alphabet with whole-symbol queries and archive the proved length separation.',
'5189':'Circuit input and PSPACE-hardness of distinguishing exact decision-tree depth at most k from depth greater than 2k.',
}
with (ROOT/'.publish.lock').open('a') as lock:
 fcntl.flock(lock,fcntl.LOCK_EX)
 qp=ROOT/'research/card-completion-20260913/queue.json';q=json.loads(qp.read_text());updates=[];events=[]
 for number,choice in CHOICES.items():
  identifier='TCS-'+number;p=ROOT/'data/cards'/f'{identifier}.json'
  if not p.exists():p=ROOT/'data/archive/cards'/f'{identifier}.json'
  raw=p.read_bytes();c=json.loads(raw)
  note=f'User explicitly confirmed the selected scope on {DATE}: {choice}'
  if note in c['statement_review']['notes']:continue
  row=next(r for r in q['records'] if r['id']==identifier)
  before=hashlib.sha256(raw).hexdigest()
  assert row['state']=='completed' and row['output_sha256']==before,identifier
  c['statement_review']['notes'].append(note);c['quality_review']['changes'].append(note)
  c['status_note']+=' '+note
  if 'source_formulation' in c:c['source_formulation']['text']+=' '+note
  c['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
  v=reader_record(c,CRITERIA)
  if c['status'] in {'resolved','excluded'}:v['status']='uncertain'
  validate_record(v,p,CRITERIA)
  output=json.dumps(c,ensure_ascii=False,indent=2)+'\n';after=hashlib.sha256(output.encode()).hexdigest()
  row['output_sha256']=after;updates.append((p,output))
  events.append(dict(id=identifier,date=DATE,outcome='user_scope_confirmation',changes=[note],input_sha256=before,output_sha256=after,output_path=str(p.relative_to(ROOT))))
 for p,output in updates:atomic(p,output)
 atomic(qp,json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (qp.parent/'reviews.jsonl').open('a') as f:
  for event in events:f.write(json.dumps(event,ensure_ascii=False)+'\n')
 print(f'{len(events)} user confirmations recorded; unique completion counts unchanged.')
