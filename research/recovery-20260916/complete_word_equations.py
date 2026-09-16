"""Complete the approved NP target and archive its duplicate without byte changes."""
import collections
import hashlib
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims,read_queue,locked,require_claim,finish_claim
from catalog_exports import atomic
from archive_cards import change_activity
identifier='TCS-0163'
claims=read_claims(ROOT)
claim=claims[identifier]
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
duplicate='TCS-0171'
duplicate_claim=claims[duplicate]
refs=old['references']+[
 ref('rta92','RTA Open Problem 92: Complexity of word unification','Klaus Schulz',1998,
 'https://www.cs.tau.ac.il/~nachum/rtaloop/problems/92.html',
 'September 1998 historical formulation; source transferred from TCS-0171 on 16 September 2026; its old space bounds are superseded'),
 ref('linearspace','Word Equations in Nondeterministic Linear Space','Artur Jeż',2017,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2017.95',
 'ICALP 2017, 95:1–95:13; introduction and §2 encoding conventions, pp. 95:1–95:2'),
 ref('length2026','Algebraic Circuits Over Sum and Shift and Existential Presburger Arithmetic with Divisibility','Ignacio Barros; Michaël Cadilhac; Guillermo A. Pérez',2026,
 'https://arxiv.org/abs/2606.14167v1',
 'Version 1, 12 June 2026; abstract and introduction: the word-equation hardness claim includes length constraints and positive Boolean combinations'),
]
notes=[
 'Applied the user’s explicit merge decision: retain TCS-0163 and ask whether plain word-equation satisfiability belongs to NP.',
 'Defined equations over a finite free monoid, allowing empty substitutions and arbitrary variable reuse, with an explicit uncompressed bit encoding.',
 'Expanded NP membership into a uniform polynomial-time verifier with polynomial-size certificates and both soundness and completeness.',
 'Did not require explicit polynomial-length solution words or a particular compressed certificate format.',
 'Transferred the historical RTA source from TCS-0171; its complete original card is archived as a duplicate after the primary completion.',
 'Preserved all previously consolidated sources, the existing category and importance; separated constrained and restricted newer results.',
]
sources=[
 'Read Antoine Amarilli’s word-equation entry, including the finite-word substitution definition, the nondeterministic linear-space bound and the 2026 open-status reference.',
 'Read RTA Problem 92: the historical broad word-unification complexity question. Its exponential-space discussion is dated, not current evidence.',
 'Read Jeż ICALP 2017 introduction and §2: linear nondeterministic space in input bits; the formal equation and symbol-encoding convention allow empty substitutions and extra letters can be eliminated.',
 'Read Jeż CSL 2020 introduction, formal definition in §2 and the compressed-solution discussion. This is an invited survey with explicitly incomplete proofs.',
 'Read Saarela STACS 2026 introduction and preliminaries: it explicitly says NP membership remains open and studies constant-free three-variable parametric solutions. Checked the inherited ICALP 2020 source’s reduction scope.',
 'Read the June 2026 preprint abstract and introduction: its PP-hardness extension uses length constraints, which are absent from this card. Its full proof was not audited.',
 'A bounded primary-source search through 16 September 2026 found no solution of NP membership for unrestricted plain word equations. No complete reconstruction of the established space algorithms is claimed.',
]
status=('Ordinary word-equation satisfiability is NP-hard and decidable in nondeterministic linear space, hence in PSPACE. '
 'Saarela’s STACS 2026 introduction explicitly identifies membership in NP as open. '
 'The newer length-constraint hardness claim concerns a larger problem. '
 'The user selected NP membership and merged TCS-0171 into this card on 16 September 2026. '
 'No resolution was found in the bounded review through that date.')
complete(identifier,dict(
 title='NP membership of word-equation satisfiability',
 criterion='decision',question_type='yes_no',
 formal=r'''Let \(\mathrm{WE}\) be the language of encodings of satisfiable word equations \(u=v\) over finite free monoids, as defined below. Is
\[
\mathrm{WE}\in\mathrm{NP}?
\]
Explicitly, do there exist a deterministic Turing machine \(V\), a constant \(C\ge1\) and an integer \(k\ge1\) such that \(V\) halts on every pair of bit strings \((e,w)\) within \(C(|e|+|w|+1)^k\) steps and, for every valid equation encoding \(e\) of length \(N\),
\[
e\in\mathrm{WE}
\quad\Longleftrightarrow\quad
\exists w\in\{0,1\}^{*}\ 
\bigl(|w|\le C(N+1)^k\ \text{and}\ V(e,w)=1\bigr)?
\]
The verifier rejects invalid equation encodings. The same machine and constants work for all alphabets, equations and variable sets.''',
 definitions=r'''For an integer \(a\ge1\), the constant alphabet is \(\Sigma=\{a_1,\ldots,a_a\}\). Its free monoid \(\Sigma^*\) is the set of finite words, including the empty word \(\varepsilon\), with concatenation as the operation. Concatenation is associative and \(\varepsilon\) is its identity; distinct letters do not commute by assumption.

The variable set is \(\mathcal X=\{X_1,\ldots,X_r\}\), disjoint from \(\Sigma\), where \(r\ge0\). An equation is a pair \(u,v\in(\Sigma\cup\mathcal X)^*\). Both sides are explicitly written token sequences. A solution assigns one word \(\sigma(X_i)\in\Sigma^*\) to each variable, fixes every constant letter, and extends by concatenation. The equation is satisfiable exactly when \(\sigma(u)=\sigma(v)\) for some assignment. All occurrences of a variable receive the same word. Empty words, repeated variables, variables on both sides, and equations with empty sides are allowed. There are no length constraints, regular-language restrictions, inverse symbols or inequalities.

One precise binary encoding is as follows. Write \(1^a0\,1^r0\,1^{\ell_u}0\,1^{\ell_v}0\), where \(\ell_u=|u|\) and \(\ell_v=|v|\) count tokens. Follow this header by all tokens of \(u\) and then all tokens of \(v\). Each token is encoded in \(b=\lceil\log_2(a+r+1)\rceil\) bits: code \(i\) for \(a_i\) and code \(a+j\) for \(X_j\). Codes outside \(1,\ldots,a+r\) are invalid. There must be exactly \(\ell_u+\ell_v\) token blocks and no trailing data. Thus
\[
N=a+r+\ell_u+\ell_v+4+b(\ell_u+\ell_v).
\]
This explicit encoding fixes bit complexity without allowing compressed input equations.

\(\mathrm{NP}\) is the class of languages with polynomial-length certificates accepted by a uniform deterministic polynomial-time verifier, with precisely the soundness and completeness quantified above. A certificate is any finite binary string. It need not contain the substituted words explicitly, and no particular compressed representation is prescribed. A satisfiable input must have some short accepting certificate; an unsatisfiable input must have none.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of \(\mathrm{WE}\in\mathrm{NP}\). A positive answer must specify the verifier and prove the polynomial time and certificate bounds together with soundness and completeness for every input. A negative answer must prove that no such verifier exists; failure of one certificate format or long explicit solutions is insufficient. This binary target has no numerical \(1/100\) tolerance. Results only for boundedly many variables, bounded occurrences, or added constraints do not decide the full statement.''',
 source_formulation=dict(text='The original sources ask for the complexity of satisfiability of equations between words with variables. The user selected the specific remaining question of NP membership and consolidated the overlapping word-unification record here.',
 caption='Paraphrase of the Amarilli entry and RTA Problem 92; explicit scope decision of 16 September 2026.',citation='primary',format='editorial_paraphrase'),
 why='Word equations are a basic model of string constraints and associative unification. Their decidability is established, but the gap between NP-hardness and polynomial-space algorithms leaves the complexity of short verifiable evidence unresolved. NP membership would place the unrestricted satisfiability problem at the familiar NP-complete boundary.',
 references=refs,
 source_consolidations=old.get('source_consolidations',[])+[dict(from_id=duplicate,reviewed_on=DATE,note='User explicitly merged the overlapping word-unification complexity question into the plain free-monoid NP-membership target. The historical RTA reference is retained here and the original duplicate card is archived intact.')],
 related_problem_ids=[x for x in old.get('related_problem_ids',[]) if x!=duplicate],
 context_blocks=[
 block('A variable stands for an entire finite word, not for one letter. For example, an equation can require two occurrences of the same unknown word to match material appearing at different positions on the other side. Concatenation couples the lengths and contents of all substitutions.'),
 block('Makanin established decidability, and later work reduced the space needed to decide satisfiability. The 1998 RTA question predates the polynomial-space improvement, so its much larger upper bound is historical provenance rather than the current frontier.','rta92'),
 block('Jeż’s 2017 theorem places satisfiability in nondeterministic linear space measured in input bits. This implies membership in PSPACE, the class decidable using polynomial working space. A space bound alone need not limit the number of computation steps to a polynomial, so it does not supply NP membership.','linearspace'),
 block('An explicit substitution may be much longer than the input equation. The NP question is therefore about succinct evidence that can be checked quickly, not about requiring a short fully expanded solution. Existing work on compressed solutions explains this distinction, but the card does not mandate any particular evidence format.','consolidated_5697_primary'),
 block('Saarela’s 2026 theorem simplifies parametric descriptions for constant-free equations on three variables. Its introduction still lists NP membership for general word equations as open. A result about the structure of that restricted solution set does not settle the unrestricted decision problem.','consolidated_5314_primary'),
 block('The June 2026 preprint claims stronger hardness for formulas that combine word equations with length constraints. Those extra arithmetic constraints change the input language. The claim therefore does not establish a lower bound excluding NP for plain equations, and its full proof was not independently audited in this review.','length2026'),
 block('The earlier two atlas records used different historical names for overlapping complexity questions. This card is now the single active NP-membership target. The duplicate’s source and provenance remain available, while the broader request for an exact complexity classification is no longer the benchmark question.'),
 ],
 progress=[
 progress('1998-09','RTA Problem 92 records the broad complexity question for word unification.','rta92'),
 progress('2017','Jeż proves a nondeterministic linear-space upper bound in the bit length of the input.','linearspace'),
 progress('2020','The recompression survey explains the gap between the known space upper bound and NP-hardness.','consolidated_5697_primary'),
 progress('2026','Saarela’s STACS paper explicitly retains the general NP-membership question as open.','consolidated_5314_primary'),
 progress('2026-06-12','A preprint claims PP-hardness after adding length constraints and positive Boolean combinations; that is a different input language.','length2026'),
 progress('2026-09-16','The user selects NP membership and merges the two overlapping atlas records; this review supplies the precise free-monoid and verifier formulation.'),
 ],
),notes,sources,status,summary=[
 'A word equation asks whether replacing each variable by a finite word can make its two sides identical.',
 'The selected target is whether satisfiability of unrestricted plain word equations belongs to NP.',
 'A positive answer needs polynomial-size certificates and one polynomial-time verifier, without prescribing how a solution is represented.',
 'The problem is NP-hard and has a nondeterministic linear-space algorithm, while a 2026 source still lists NP membership as open.',
 'The overlapping word-unification card is merged here, with its original record retained in the archive.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])

# Retire the duplicate byte-for-byte after checking its reservation and input.
reason='Merged into TCS-0163 by explicit user decision on 16 September 2026: one active NP-membership question for plain word-equation satisfiability; historical RTA source transferred.'
with locked(ROOT):
 require_claim(ROOT,duplicate,duplicate_claim['token'])
 original=(ROOT/'data/cards'/f'{duplicate}.json').read_bytes()
 assert hashlib.sha256(original).hexdigest()==duplicate_claim['input_sha256']
 assert next(r for r in read_queue(ROOT)['records'] if r['id']==duplicate)['state']=='pending'
print(change_activity([duplicate],reason=reason))
with locked(ROOT):
 archived=ROOT/'data/archive/cards'/f'{duplicate}.json'
 assert archived.read_bytes()==original
 queue=read_queue(ROOT)
 row=next(r for r in queue['records'] if r['id']==duplicate)
 row.update(state='completed',completed_on=DATE,
   review_input_sha256=duplicate_claim['input_sha256'],
   output_sha256=hashlib.sha256(original).hexdigest(),
   output_path=str(archived.relative_to(ROOT)),consolidated_into=identifier)
 queue['counts']=dict(total=len(queue['records']),**dict(collections.Counter(r['state'] for r in queue['records'])))
 atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as ledger:
  ledger.write(json.dumps(dict(id=duplicate,date=DATE,outcome='merged_after_individual_review',
    consolidated_into=identifier,changes=[reason],sources_checked=['RTA Problem 92; all source provenance transferred to the completed TCS-0163.'],
    input_sha256=duplicate_claim['input_sha256'],output_path=str(archived.relative_to(ROOT))),ensure_ascii=False)+'\n')
 finish_claim(ROOT,duplicate,duplicate_claim['token'],queue)
 print(duplicate,queue['counts'])
