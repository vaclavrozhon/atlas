"""Apply explicit September 18 replies; retain incomplete research directions honestly."""
import collections, fcntl, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import CRITERIA,reader_record,validate_record,atomic,ref,block
from review_queue import read_claims,require_claim,finish_claim,refresh_list
from archive_cards import change_activity
DATE='2026-09-18'
ONLY=set(sys.argv[1:])
reasons={
 'TCS-2997':'Excluded at the user’s explicit request on 18 September 2026. This is an editorial removal, not a claim that CONGEST triangle detection has been resolved.',
 'TCS-6957':'Excluded at the user’s explicit request on 18 September 2026: the affine-maximizer domain classification does not specify a substantive new characterization criterion.',
 'TCS-7124':'Excluded at the user’s explicit request on 18 September 2026: the intended classification beyond the known SNP/finite-forbidden-pattern representation is unspecified.',
 'TCS-1251':'Excluded at the user’s explicit request on 18 September 2026: no precise output-sensitive running-time bound is selected for arbitrary cyclic queries.',
}
if ONLY: reasons={k:v for k,v in reasons.items() if k in ONLY}
gaps={
 'TCS-6957':'The source asks for a characterization of restricted valuation domains, but selects neither an intrinsic proposed criterion nor an effectiveness requirement. Merely restating implementability is circular, while recognition on explicitly finite rational type tables is decidable by enumeration and linear inequalities. Choosing a richer domain presentation or a new criterion would introduce a new target.',
 'TCS-1251':'The source’s second open question in §6 asks for output-sensitive evaluation of cyclic CRPQs, already open for cyclic CQs, without specifying the requested bound in database size, output size and query structure. For a fixed query, an unspecified polynomial bound follows by enumerating assignments. The separate acyclic result does not settle this cyclic direction.',
 'TCS-6958':'Specify an optimization domain and objective, finite representation or oracle access to valuations and strategies, the approximation improvement to separate, and any allowed complexity assumption for the lower bound against all efficient dominant-strategy mechanisms. The original definition supplies a solution concept but not these parameters. No particular auction domain or new separation conjecture is selected.',
}
with (ROOT/'.publish.lock').open('a') as lock:
 fcntl.flock(lock,fcntl.LOCK_EX)
 qp=ROOT/'research/card-completion-20260913/queue.json';q=json.loads(qp.read_text());events=[];updates=[];releases=[]
 for identifier in ['TCS-6157','TCS-7128','TCS-7290','TCS-6454','TCS-2997','TCS-6957','TCS-7124','TCS-1251','TCS-6958']:
  if ONLY and identifier not in ONLY:continue
  p=ROOT/'data/cards'/f'{identifier}.json'
  if not p.exists():p=ROOT/'data/archive/cards'/f'{identifier}.json'
  raw=p.read_bytes();before=hashlib.sha256(raw).hexdigest();c=json.loads(raw)
  row=next(r for r in q['records'] if r['id']==identifier)
  claim=read_claims(ROOT).get(identifier)
  if row['state']=='pending':
   assert claim and claim['input_sha256']==before
   require_claim(ROOT,identifier,claim['token'])
  else:assert row['output_sha256']==before,identifier
  notes=[];outcome='user_scope_confirmation'
  if identifier in ['TCS-6157','TCS-7128','TCS-7290']:
   choice={'TCS-6157':'Finite-database RPQ determinacy, archived with the known negative decidability result.','TCS-7128':'Unconditional lower bound for distinct endpoint-pair enumeration of the directed two-step query in the saved deterministic word-RAM model.','TCS-7290':'The binary sunflower conjecture with a constant exponential base for every fixed petal count.'}[identifier]
   notes=[f'User explicitly confirmed on {DATE}: {choice}']
   if identifier=='TCS-7290':
    c['source_formulation']['text']='Conjecture 1.3 asks for a constant-base exponential bound for each fixed number of petals. The user explicitly selected this binary source conjecture on 18 September 2026, superseding the September 12 broader optimal-function request retained in formulation history.'
  elif identifier=='TCS-6454':
   c.setdefault('formulation_history',[]).append(dict(recorded_on=DATE,formal=c['formal'],answer_criterion=c['answer_criterion'],reason='User replaced the weaker eventual-success exclusion by standard eventual negligible advantage.'))
   c['formal']=r'''Does the following implication hold?
\[
\operatorname{NCP}_2\notin\mathrm{BPP}\quad\Longrightarrow\quad
\forall D\in\mathrm{PPT}\ \forall c>0\ \exists n_0\ge9\ \forall n\ge n_0:
\quad n\text{ a square}\ \Longrightarrow\ \operatorname{Adv}_D(n)<n^{-c}.
\]
Here \(\operatorname{NCP}_2\) is the unrestricted binary Nearest Codeword decision problem defined below. The distinguisher receives either \((A,As+e)\) or \((A,u)\), with a uniform \(n^2\times n\) binary matrix, independent uniform secret and comparison vector, and independent noise bits of probability \(1/\sqrt n\). The conclusion requires negligible advantage at all sufficiently large square dimensions for every uniform classical probabilistic polynomial-time distinguisher.'''
   split='The displayed quantifier order retains the saved weaker asymptotic target:'
   assert split in c['definitions']
   c['definitions']=c['definitions'].split(split)[0]+r'''The conclusion is eventual negligible advantage along the square dimensions: for each fixed distinguisher and positive exponent there is a threshold beyond which every square dimension satisfies the displayed upper bound. Its failure means that some fixed distinguisher and exponent have inverse-polynomial advantage at arbitrarily large square dimensions. The user explicitly selected this stronger length convention on 18 September 2026. The unrestricted decision premise, exact sample count and exact noise rate remain editorial specifications of the broader source direction, rather than a theorem stated verbatim there.'''
   c['answer_criterion']=r'''Give a complete mathematically correct Lean-checked proof or refutation of the displayed implication. An affirmative proof must obtain eventual negligible advantage, including exclusion of a distinguisher that succeeds only on an unbounded subsequence of square dimensions. A sufficient route converts any such nonnegligible distinguisher into a BPP decider for the entire unrestricted Nearest Codeword language. A refutation must establish both the Nearest Codeword premise and a distinguisher violating the conclusion; an oracle separation or failure of a particular reduction is insufficient. An additional dual-code hardness assumption, a different sample/noise regime or only the exclusion of distinguishers successful at every sufficiently large length does not settle this target.'''
   c['source_formulation']['text']='Section 1.2 asks for standard worst-case foundations such as Nearest Codeword alone. The card specializes to the saved unrestricted decision premise and square-dimension, n-squared-sample, inverse-square-root-noise experiment. On 18 September 2026 the user explicitly chose the stronger standard conclusion of eventual negligible advantage.'
   c['context_blocks'][-1]=block('The card asks for standard negligible distinguishing advantage throughout all sufficiently large square dimensions. Success confined to an unbounded sparse sequence of dimensions must also be ruled out.','lpn')
   c['working_summary']['sentences'][3]='The conclusion requires negligible advantage at every sufficiently large square dimension, including exclusion of distinguishers useful on a sparse unbounded sequence.'
   notes=['User explicitly selected eventual negligible advantage on 18 September 2026, replacing the earlier weaker editorial default.','Reversed the length quantifiers to the selected universal eventual bound and updated the contrapositive and answer criterion.']
   outcome='user_scope_revision'
  elif identifier in reasons:
   c['status']='excluded';c['status_note']=reasons[identifier]
   notes=[reasons[identifier]];outcome='user_exclusion'
   if identifier!='TCS-2997':
    gap=gaps.get(identifier,c.get('statement_review',{}).get('remaining_issue',''))
    c.update(model_self_contained=False,requires_context=True,evidence='reviewed')
    c['statement_review']=dict(status='needs_specification',reviewed_on=DATE,remaining_issue=gap,notes=[gap],scope='Source-grounded exclusion of an unspecified target, not completion of a mathematical statement.')
    c['quality_review']=dict(reviewed_on=DATE,reference_card='TCS-0001',state='needs_specification',changes=[gap],checked_sources=[r['url'] for r in c['references']],scope='The user chose editorial exclusion; no resolution theorem is asserted.')
    c['review_note']='Source reviewed and excluded as too indefinite at the user’s request; not a completed self-contained benchmark question.'
    if identifier=='TCS-6957':
     c['context']='The textbook’s §12.4 ends by asking which restricted domains allow only affine-maximizing implementable allocation rules. An affine maximizer optimizes a fixed nonnegative weighted sum of reported valuations plus fixed outcome offsets. The source does not propose the necessary and sufficient domain criterion requested by a completed classification card.'
    if identifier=='TCS-1251':
     c['context']='A conjunctive regular path query joins path constraints whose edge-label words belong to specified regular languages. Its outputs are distinct assignments to its free variables. Section 6 asks whether output-sensitive techniques extend from acyclic to arbitrary cyclic queries, but does not choose a running-time target for this extension.'
   if row['state']=='pending':
    row.update(state='completed',completed_on=DATE,review_input_sha256=before,disposition='excluded_by_user',scope_note='Review disposition complete: excluded for insufficiently specified target; not a completed benchmark formulation.')
  else:
   gap=gaps[identifier]
   c.update(status='uncertain',evidence='reviewed',model_self_contained=False,requires_context=True,question_type='yes_no')
   c['formal']='Does some computationally specified optimization domain admit an efficient algorithmic implementation with a better approximation guarantee than every efficient dominant-strategy implementation? This retained research direction still requires the domain, representation, quantitative gap and allowed hardness assumption to be selected.'
   c['definitions']=r'''For a player with a fixed true type, write \(u_i(s_i,s_{-i})\) for the utility resulting from strategies \(s_i\) and \(s_{-i}\). The source calls one strategy a weak improvement of another when its utility is at least as high for every possible opposing strategy profile. An algorithmic implementation identifies acceptable strategy sets \(D_i\): every profile drawn from these sets must achieve the promised approximation in polynomial time, and from any strategy outside its acceptable set the player must be able to compute a dominating acceptable strategy in polynomial time. This is the framework of Definition 1.2, not a requirement that players converge through an arbitrary dynamics. Dominant-strategy implementation instead supplies a recommended strategy optimal against every opposing profile.

The source does not choose one problem family, its welfare or cost objective, how types and strategies are encoded or accessed, the input-length parameter for polynomial time, the approximation gap, or the assumption permitted to rule out all efficient dominant-strategy mechanisms. These are required specifications, not implicit free choices of this card.'''
   c['context_blocks']=[block('A weaker incentive requirement may permit approximation algorithms that cannot be implemented through dominant strategies. The source develops positive mechanisms and separately asks for a separation from every dominant-strategy implementation.','original'),block('A positive example for one domain does not itself establish that universal separation. The retained record records the missing comparison parameters instead of inventing a new auction-specific conjecture.','original')]
   c.pop('context',None)
   c['references'].append(ref('original','Single-Value Combinatorial Auctions and Implementation in Undominated Strategies','Moshe Babaioff; Ron Lavi; Elan Pavlov',2006,'https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/undominated.pdf','Definition 1.2 and Open question 2 in §1.3; the original comparison and improvement-step requirement.'))
   c['progress']=[dict(date='2006',text='Definition 1.2 formalizes algorithmic implementation, while Open question 2 asks for a strict advantage over dominant-strategy implementation.',citation='original')]
   c['why']='Separating computationally tractable incentive concepts would explain when stronger strategic guarantees impose an unavoidable approximation cost. The significance is clear even though the intended separating family is not yet fixed.'
   c['importance']=dict(score=79,method='editorial',assessed_on=DATE,reason=c['why'])
   c['answer_criterion']='This record is not ready for benchmark acceptance. First specify the domain, representation, target gap and allowed lower-bound assumption; then a complete mathematically correct Lean-checked proof of the resulting separation or its negation would be required. No particular precise conjecture is adopted here.'
   c['status_note']='The checked 2006 paper and 2007 textbook state a broad research direction. Their positive implementations do not alone prove the proposed separation from every efficient dominant-strategy mechanism. The user explicitly chose to retain this record as requiring specification on 18 September 2026; current openness of an as-yet-unselected precise proposition is not certified.'
   notes=['User explicitly retained this record as requiring specification on 18 September 2026.',gap,'Read the original Definition 1.2 and Open question 2; no unsupported separation or new domain is selected.']
   c['statement_review']=dict(status='needs_specification',reviewed_on=DATE,remaining_issue=gap,notes=[],scope='Source review with explicit unresolved target choices.')
   c['quality_review']=dict(reviewed_on=DATE,reference_card='TCS-0001',state='needs_specification',changes=[],checked_sources=[r['url'] for r in c['references']],scope='Read source definitions and comparison question; not a completed benchmark formulation.')
   c['review_note']='Retained pending specification by explicit user choice; not counted as a completed card.'
   c['working_summary']=dict(sentences=['Mechanism design asks for good outcomes when participants choose their own strategies.','Algorithmic implementation guarantees approximation for a collection of acceptable strategies.','A player can efficiently improve any strategy outside that collection to a dominating acceptable one.','The source asks whether this framework can outperform every efficient dominant-strategy implementation.','The user retains the direction pending a precise domain, representation, approximation gap and allowed hardness assumption.'],basis='saved_sources',source_basis='individual_source_review',written_on=DATE,source_refs=['primary','original'])
   row.update(last_source_review_on=DATE,remaining_issue=gap);outcome='needs_specification'
  c.setdefault('statement_review',{}).setdefault('notes',[]).extend(notes)
  c.setdefault('quality_review',{}).setdefault('changes',[]).extend(notes)
  if outcome in {'user_scope_revision','user_scope_confirmation'}:c['status_note']+=' '+notes[0]
  c['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
  if c['status'] not in {'resolved','excluded'}:validate_record(reader_record(c,CRITERIA),p,CRITERIA)
  output=json.dumps(c,ensure_ascii=False,indent=2)+'\n';after=hashlib.sha256(output.encode()).hexdigest()
  updates.append((p,output))
  if row['state']=='completed':row.update(output_sha256=after,output_path=str(p.relative_to(ROOT)))
  else:row.update(source_review_sha256=after,input_sha256=after)
  events.append(dict(id=identifier,date=DATE,outcome=outcome,changes=notes,input_sha256=before,output_sha256=after,output_path=str(p.relative_to(ROOT))))
  if claim:releases.append((identifier,claim['token']))
 for p,output in updates:atomic(p,output)
 for identifier,token in releases:finish_claim(ROOT,identifier,token,q)
 q['counts']=dict(total=len(q['records']),**collections.Counter(r['state'] for r in q['records']))
 atomic(qp,json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (qp.parent/'reviews.jsonl').open('a') as f:
  for e in events:f.write(json.dumps(e,ensure_ascii=False)+'\n')
for identifier,reason in reasons.items():print(change_activity([identifier],reason=reason))
with (ROOT/'.publish.lock').open('a') as lock:
 fcntl.flock(lock,fcntl.LOCK_EX)
 q=json.loads(qp.read_text())
 for row in q['records']:
  if row['id'] in reasons:row['output_path']=f"data/archive/cards/{row['id']}.json"
 atomic(qp,json.dumps(q,ensure_ascii=False,indent=2)+'\n');refresh_list(ROOT,q)
 with (qp.parent/'reviews.jsonl').open('a') as f:
  for identifier,reason in reasons.items():f.write(json.dumps(dict(id=identifier,date=DATE,outcome='archived_by_user',reason=reason,output_path=f'data/archive/cards/{identifier}.json'),ensure_ascii=False)+'\n')
print(f'Applied {len(events)} explicit replies and {len(reasons)} archival actions.')
