"""Review the Cayley-table dichotomy, including the September 2026 revision."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1544';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A qAC⁰ versus NL-complete dichotomy for Cayley semigroup membership',
 status='source_open',criterion='characterization',question_type='yes_no',
 formal=r'''For every pseudovariety \(\mathcal V\) of finite semigroups, does its Cayley-table membership promise problem \(\operatorname{Memb}_{\mathrm{CT}}(\mathcal V)\), defined below, satisfy at least one of these two alternatives?
\[
\operatorname{Memb}_{\mathrm{CT}}(\mathcal V)\in\mathrm{qAC}^{0}
\qquad\text{or}\qquad
\operatorname{Memb}_{\mathrm{CT}}(\mathcal V)\text{ is NL-complete under uniform AC}^{0}\text{ many-one reductions}.
\]
Use uniform circuit classes and reductions that always output valid promised instances. The pseudovariety is fixed separately for each problem, not part of the input.''',
 definitions=r'''A finite semigroup is a nonempty finite set \(S\) equipped with an associative binary operation \(\cdot:S\times S\to S\). An identity element or inverses are not required. A pseudovariety is a nonempty isomorphism-closed class of finite semigroups closed under nonempty subsemigroups, homomorphic images and finite nonempty direct products. A homomorphism preserves multiplication, and multiplication in a direct product is coordinatewise. No effective description of the class is assumed.

An instance gives the full multiplication table of \(S=\{1,\ldots,N\}\), a nonempty set of generators \(\Sigma\subseteq S\), and a target \(t\in S\). Table entries and the target are binary indices of the same fixed width \(\lceil\log_2(N+1)\rceil\); the generator set is given by its length-\(N\) incidence vector. Use a standard explicit length-delimited encoding of the dimension, table, vector and target, and let \(L\) be its total length. Thus the entire table, not a circuit or transformation representation of multiplication, is included in the input.

Write \(\langle\Sigma\rangle\) for all products \(s_1\cdots s_\ell\) with \(\ell\ge1\) and each \(s_i\in\Sigma\), allowing repetitions. The promise is that the supplied table is a semigroup and
\[
\langle\Sigma\rangle\in\mathcal V.
\]
The ambient semigroup \(S\) need not itself lie in \(\mathcal V\). A yes-instance has \(t\in\langle\Sigma\rangle\), and a no-instance satisfies the promise but has \(t\notin\langle\Sigma\rangle\). There is no required behavior on inputs violating the promise. Recognizing whether the generated semigroup belongs to \(\mathcal V\) is not part of this problem.

For this question, \(\mathrm{qAC}^{0}\) means Boolean circuits with unbounded-fan-in AND and OR gates, unary NOT gates, constant depth, and size at most
\[
2^{K(\log_2(L+2))^c}
\]
for some constants \(K,c\ge1\). They must be \(\mathrm{DTIME}(\operatorname{polylog}L)\)-uniform: a random-access deterministic Turing machine, given the binary input length and gate indices, determines gate types, input labels, output gates and wire incidence in time polynomial in \(\log(L+2)\). Circuit depth, size constants and the uniformity machine may depend on the fixed \(\mathcal V\), but not on an individual instance. The circuits must give the correct answer on every promised instance of length \(L\).

The class NL consists of languages decided by nondeterministic Turing machines with a read-only input and \(O(\log L)\) work space. NL membership for the promise problem requires correct acceptance and rejection on promised inputs. NL-hardness means that every NL language has a many-one reduction to it computed by \(\mathrm{DTIME}(\log L)\)-uniform, polynomial-size, constant-depth Boolean circuits with the same gate types. Each reduction outputs a promised instance on every source input and preserves its answer. Equivalently it suffices to reduce directed graph reachability, with a specified start and target, under these reductions. NL-complete means both membership and hardness. No logarithmic-space reduction is substituted for the finer circuit reduction.

The question asks for the dichotomy for all fixed pseudovarieties. It does not ask for an algorithm which, given a description of a pseudovariety, selects an alternative.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the dichotomy, including the promised-input interpretation and uniform complexity bounds, or a proof of its logical negation. An affirmative proof must cover every pseudovariety. A negative proof must establish a pseudovariety whose promise problem is neither in the stated uniform qAC⁰ class nor NL-complete under the stated promise-preserving reductions. Classifying only groups, inverse semigroups or efficient-compression classes is insufficient.',
 why='Finite semigroup membership ranges from very shallow parallel computation to directed reachability. A dichotomy would organize this complexity landscape by algebraic closure properties, extending the structural understanding beyond known compression-friendly classes.',
 importance=dict(score=81,method='editorial',reason='A broad algebraic complexity classification at the boundary of shallow circuits and nondeterministic logarithmic space, with a precise representation and fresh structural progress.'),
 source_formulation=dict(text='The selected target is Question 39 of the STACS 2026 source already consolidated into this record. The 14 September 2026 full revision retains it as Question 41. It is a precise Cayley-table target within the older broader classification request.',caption='Efficient Compression in Semigroups: STACS 2026 p.80:19; arXiv v2, Question 41 p.22.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Efficient Compression in Semigroups','Florian Stober; Alexander Thumm; Armin Weiß',2026,'https://arxiv.org/abs/2601.04747v2','Revision 2, 14 September 2026; Theorem 1 and Corollary 3 pp.2–3; §2 uniformity p.5; §11 promise model p.20; Question 41 p.22'),
 ref('conference','Efficient Compression in Semigroups','Alexander Thumm; Armin Weiß',2026,'https://doi.org/10.4230/LIPIcs.STACS.2026.80','Original two-author conference paper; §2 uniformity p.80:5, §10 promise and table model p.80:17, Question 39 p.80:19'),
 ref('original','Membership and Conjugacy in Inverse Semigroups','Lukas Fleischer; Florian Stober; Alexander Thumm; Armin Weiß',2025,'https://doi.org/10.4230/LIPIcs.ICALP.2025.156','Conclusion and Open Problem 33, p.156:16; broader classification request, with representation-dependent problems'),
 ],
 context_blocks=[
 block('The Cayley table is an essential part of the target. Giving generators as transformations can succinctly describe a far larger semigroup and leads to a different complexity classification.','original'),
 block('The 2026 work classifies pseudovarieties admitting short straight-line descriptions of generated elements. This gives qAC⁰ upper bounds for those classes, but the paper leaves the full membership dichotomy open.'),
 block('General table membership is in NL: nondeterministically follow right multiplication by generators through the finite set of elements. The difficult classification distinguishes which promised classes also admit shallow quasipolynomial circuits.'),
 block('The September revision retains uniformity and promises membership of the generated subsemigroup, not of the ambient table semigroup. These conventions are part of the card.'),
 block('The older record also asked for a broad classification of arbitrary semigroup varieties. This card selects the concrete dichotomy rather than claiming to classify all representation models.','original'),
 ],
 progress=[progress('2025','The inverse-semigroup paper asks for a broader classification of finite semigroup varieties.','original'),progress('2026','The STACS paper supplies compression-based upper bounds and poses the Cayley-table dichotomy.','conference'),progress('2026-09-14','The expanded three-author revision retains the target as Question 41.')],
),[
 'Selected the consolidated source’s Cayley-table qAC⁰/NL dichotomy after the optional question received no reply; announced editorial default, not user confirmation.',
 'Defined pseudovarieties, nonempty products, full tables, and the promise on the generated subsemigroup rather than the ambient one.',
 'Specified polylog-time qAC⁰ uniformity and uniform AC⁰ promise-preserving reductions for NL completeness.',
 'Checked the new 14 September revision and retained its open Question 41, including the expanded author list.',
 'Individually assessed importance and required complete Lean-checked coverage or a counterexample to the dichotomy.',
],[
 'Read ICALP 2025 Open Problem 33 and the STACS 2026 model, uniformity definitions, structural Theorem 1, Corollary 2, and Question 39.',
 'Discovered and read the 14 September 2026 arXiv revision: Theorem 1/Corollary 3, uniformity paragraph, §11 generated-subsemigroup promise, and Question 41. The author list now includes Florian Stober.',
 'Status checked through 17 September 2026; the latest primary revision explicitly retains the selected dichotomy as open.',
], 'Source-open in the 14 September 2026 revision, Question 41. The selected target is the Cayley-table dichotomy with uniform qAC⁰ and promise-preserving uniform AC⁰ hardness, not the older unrestricted classification across representation models. The target selection was an announced editorial default after an unanswered optional question.',summary=[
 'The input gives a finite semigroup by its complete multiplication table, a generator set and a target element.',
 'The promise places the generated subsemigroup in one fixed pseudovariety, and the task is to test whether it contains the target.',
 'The question asks whether every such class has either uniform shallow quasipolynomial circuits or an NL-complete membership problem.',
 'Hardness uses uniform constant-depth polynomial-size reductions that preserve the input promise.',
 'The September 2026 source retains this dichotomy as open; a complete Lean-checked universal proof or counterexample is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
