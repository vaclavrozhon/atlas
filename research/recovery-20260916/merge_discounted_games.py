"""Consolidate exact discounted stochastic-game solving into the SSG card."""
import collections,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import DATE,CRITERIA,ref
from review_queue import read_claims,read_queue,locked,require_claim,finish_claim
from catalog_exports import atomic
from archive_cards import change_activity
from card_schema import reader_record
from publish import validate_record
target='TCS-6567';duplicate='TCS-2427';claim=read_claims(ROOT)[duplicate]
target_hash='5679b7dc1f6dc1ebb2181f2c7d8bd49ada8abcbf93ecc05fc639a730e4176353'
reason=('Consolidated the exact polynomial-time solution branch for rational turn-based zero-sum discounted stochastic games into TCS-6567. '
 'With the common discount factor and all game data encoded in binary, exact value and optimal-strategy computation are polynomial-time equivalent to solving simple stochastic games. '
 'The approximate branch was not assigned an unstated error tolerance. This is the announced editorial default after an unanswered optional scope/merge question. '
 'Archival removes a duplicate complexity target and does not assert a polynomial-time algorithm is known.')
checked=['Read Jin–Muthukumar–Sidford ITCS 2023.76 pp.76:15–16, including the distinction between constant and input-dependent discount factors.',
 'Checked Andersson–Miltersen ISAAC 2009 publication metadata and the indexed primary abstract listing binary discounted games in the polynomial-time equivalence. The original full chapter could not be retrieved (publisher 503; former author links 404), so no full-proof audit is claimed.',
 'Read Chatterjee et al. IJCAI 2024 §3.3 p.6711, explicitly reporting the polynomial reduction of discounted TBSG optimal values and policies to SSGs; read Berthon–Katoen–Zhou CONCUR 2025 §1 and §4.3 on the standard reductions and encodings.',
 'Compared the completed TCS-6567 exact threshold definition and bit-time quantifiers. For finite rational SSGs, positional values have polynomial-bit rational descriptions, so exact threshold access, exact values and optimal strategies have polynomial-time interreductions.']
def add(mapping,key,value):
 old=mapping.get(key,[]);mapping[key]=old+[value] if isinstance(old,list) else old+' '+value
with locked(ROOT):
 require_claim(ROOT,duplicate,claim['token']);assert target not in read_claims(ROOT)
 p=ROOT/'data/cards'/f'{target}.json';before=p.read_bytes();assert hashlib.sha256(before).hexdigest()==target_hash
 original=(ROOT/'data/cards'/f'{duplicate}.json').read_bytes();assert hashlib.sha256(original).hexdigest()==claim['input_sha256']
 q=read_queue(ROOT);row=next((r for r in q['records'] if r['id']==target),None)
 if row is not None:assert row['state']=='completed' and row['output_sha256']==target_hash
 c=json.loads(before)
 c.setdefault('source_consolidations',[]).append(dict(from_id=duplicate,reviewed_on=DATE,note=reason))
 c['related_problem_ids']=[i for i in c.get('related_problem_ids',[]) if i!=duplicate]
 c['references'].extend([
  ref('discounted_question','The Complexity of Infinite-Horizon General-Sum Stochastic Games','Yujia Jin; Vidya Muthukumar; Aaron Sidford',2023,'https://doi.org/10.4230/LIPIcs.ITCS.2023.76','Related work, zero-sum case, pp.76:15–16; the input-dependent discount question'),
  ref('games_equivalence','The Complexity of Solving Stochastic Games on Graphs','Daniel Andersson; Peter Bro Miltersen',2009,'https://doi.org/10.1007/978-3-642-10631-6_13','ISAAC 2009, pp.112–121, Theorem 1; equivalence also reported in the checked IJCAI 2024 §3.3 and CONCUR 2025 §1'),
  ref('discounted_reduction','Solving Long-run Average Reward Robust MDPs via Stochastic Games','Krishnendu Chatterjee; Ehsan Kafshdar Goharshady; Mehrdad Karrabi; Petr Novotný; Đorđe Žikelić',2024,'https://www.ijcai.org/proceedings/2024/0741.pdf','§2 game and payoff definitions; §3.3 p.6711, efficient algorithms paragraph and Remark 1')])
 c.setdefault('context_blocks',[]).append(dict(text=r'''The exact branch formerly indexed as TCS-2427 asks for a deterministic polynomial-bit-time algorithm returning optimal positional strategies for a finite, explicitly given, two-player zero-sum turn-based game. Each state is owned by one player; every available action has a rational reward to Max and a rational probability distribution over successor states. Min receives the opposite reward. A common rational discount multiplier \(\gamma\in(0,1)\) is part of the binary input, and Max's objective is \(\mathbb E[\sum_{t\ge0}\gamma^t r_t]\). Multiplication by \(1-\gamma\) leaves optimal strategies unchanged. The factor is constant during a play but may approach one across inputs. Time must be polynomial in the complete encoding length, including \(\gamma\); polynomial dependence on \(1/(1-\gamma)\) alone is insufficient. Exact solving of this class and simple stochastic games are polynomial-time equivalent. The source's additional approximation branch has no precision selected here.''',citation='games_equivalence'))
 c['context_blocks'].append(dict(text='The 2023 source explicitly separates the known constant-discount algorithms from the input-dependent discount question. The checked 2024 paper invokes the reduction of discounted game values and optimal policies to SSGs. These connections motivate consolidating the exact branch into the present threshold problem; they do not establish that its polynomial-time target is solved.',citation='discounted_reduction'))
 add(c['statement_review'],'notes',reason);add(c['quality_review'],'changes',reason)
 c['quality_review']['checked_sources'].extend(checked)
 c['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
 validate_record(reader_record(c,CRITERIA),p,CRITERIA)
 out=json.dumps(c,ensure_ascii=False,indent=2)+'\n';output_hash=hashlib.sha256(out.encode()).hexdigest()
 if row is not None:row['output_sha256']=output_hash
 atomic(p,out);atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as f:f.write(json.dumps(dict(id=target,date=DATE,outcome='source_consolidation_amendment',changes=[reason],sources_checked=checked,input_sha256=target_hash,output_sha256=output_hash),ensure_ascii=False)+'\n')
print(change_activity([duplicate],reason=reason))
with locked(ROOT):
 p=ROOT/'data/archive/cards'/f'{duplicate}.json';assert p.read_bytes()==original
 q=read_queue(ROOT);row=next(r for r in q['records'] if r['id']==duplicate);assert row['state']=='pending'
 row.update(state='completed',completed_on=DATE,review_input_sha256=claim['input_sha256'],output_sha256=hashlib.sha256(original).hexdigest(),output_path=str(p.relative_to(ROOT)),consolidated_into=target)
 q['counts']=dict(total=len(q['records']),**dict(collections.Counter(r['state'] for r in q['records'])))
 atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as f:f.write(json.dumps(dict(id=duplicate,date=DATE,outcome='merged_after_individual_review',consolidated_into=target,changes=[reason],sources_checked=checked,input_sha256=claim['input_sha256'],output_path=str(p.relative_to(ROOT))),ensure_ascii=False)+'\n')
 finish_claim(ROOT,duplicate,claim['token'],q);print(duplicate,q['counts'])
