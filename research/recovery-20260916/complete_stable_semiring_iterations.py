"""Review the universal linear synchronous-iteration bound and announcement limits."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0482';claim=read_claims(ROOT)[identifier]
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
notes=[
 'Retained the universal O((p+1)n) fixed-point bound for synchronous iteration of arbitrary polynomial systems over commutative p-stable semirings.',
 'Specified all semiring operations, finite polynomial syntax, zero starting vector, exact equality and a constant independent of degrees, coefficients and their number.',
 'Distinguished a p-stable semiring from a particular p-stable element and did not replace F by an inflationary or asynchronous evaluation rule.',
 'Read the original polynomial convergence theorem with its explicit coefficient-count and product-length dependencies; kept the 0-stable case separate.',
 'Rechecked three author-maintained listings of the announced Optimal Convergence paper; no theorem text was obtained and the listings disagree on the venue year.',
 'Retained uncertain current status, preserved importance and required a complete Lean-checked proof of the precise universal bound or its negation.',
]
sources=[
 'Read Ngo, Convergence rate of Datalogo over p-stable semirings, §4.2, printed p.105 of Dagstuhl Seminar 25081, DOI 10.4230/DagRep.15.2.89. The contribution proposes an O((p+1)n) convergence bound matching its stated lower-bound scale. The card retains the grounded polynomial-system formulation of this target.',
 'Read Im–Moseley–Ngo–Pruhs, Polynomial Time Convergence of the Iterative Evaluation of Datalogo Programs, arXiv:2312.14063v2, 21 February 2024: abstract, Theorem 1.1 printed p.2, §2.1 p.3 and grounding discussion §2.4. The theorem explicitly contains sigma (distinct referenced semiring elements) and lambda (maximum multiplicands). The Introduction separately states the O(n) result for 0-stable semirings. These dependencies are not silently suppressed as though the theorem already gave the proposed universal linear bound.',
 'Fetched Ngo’s publications page, Zhao’s homepage and Moseley’s by-topic publications page on 17 September 2026. Each lists Optimal Convergence of Iterative Methods for Datalogo by Frisk, Zhao, Ngo, Pruhs, Moseley, Im and Koutris. Ngo and Zhao label it PODS 2027; Moseley labels it PODS 2025. No linked manuscript or theorem statement for that entry was obtained from the inspected listings. Neither the title nor these inconsistent labels certifies its exact scope.',
 'Bounded primary-source searches through 17 September 2026 found no accessible theorem text establishing what the announced result proves for the selected all-polynomial-map, all-degree, synchronous-round target. The preserved status is uncertain rather than confirmed open or resolved. No contact with the authors or independent proof validation is claimed.',
]
complete(identifier,dict(
 status='uncertain',criterion='tightness',question_type='yes_no',
 formal=r'''Does there exist a universal real constant \(C\ge1\) such that, for every integer \(p\ge0\), integer \(n\ge1\), commutative \(p\)-stable semiring \(S\), and polynomial map \(F:S^n\to S^n\) with coefficients in \(S\), the synchronous sequence
\[
x^{(0)}=(0,\ldots,0),\qquad x^{(t+1)}=F(x^{(t)})
\]
satisfies \(x^{(t+1)}=x^{(t)}\) for some integer \(0\le t\le C(p+1)n\)? The constant must be independent of the semiring, coefficients, number of monomials and polynomial degrees. Only the number of rounds is measured.''',
 definitions=r'''A commutative semiring is a set \(S\) with binary operations \(\oplus,\otimes\) and elements \(0,1\) such that \((S,\oplus,0)\) and \((S,\otimes,1)\) are commutative monoids, multiplication distributes over addition, and \(0\otimes a=a\otimes0=0\). No additive inverses, additive idempotence, order, finiteness or effective encoding is assumed. The trivial semiring is allowed. All equalities are equalities of semiring elements.

For \(a\in S\), set \(a^0=1\) and \(a^{j+1}=a^j\otimes a\). The semiring is \(p\)-stable when
\[
\bigoplus_{j=0}^{p}a^j=\bigoplus_{j=0}^{p+1}a^j\qquad\text{for every }a\in S.
\]
The same integer \(p\) must work for every element, not merely for the coefficients appearing in one system. It need not be the smallest possible stability index. The case \(p=0\) means \(1\oplus a=1\) for all \(a\).

Each coordinate of \(F\) is given by a finite polynomial expression, equivalently
\[
F_i(x_1,\ldots,x_n)=\bigoplus_{j\in J_i}\left(a_{ij}\otimes\bigotimes_{r=1}^{n}x_r^{e_{ijr}}\right),
\]
where \(J_i\) is a finite index set, \(a_{ij}\in S\) and \(e_{ijr}\in\mathbb N\). An empty sum is 0 and an empty product is 1. Repeated monomials, arbitrary finite exponents and constant terms are allowed. There is no bound on the degrees or the number of terms, and no requirement of linearity. The coefficients remain fixed during iteration.

One round evaluates every \(F_i\) from the entire previous vector \(x^{(t)}\). Partially updated coordinates cannot be reused within that round. The rule is precisely \(F\), not a replacement such as \(x\mapsto x\oplus F(x)\), unless their iteration behavior is proved to agree for the system under consideration. The initial vector is always zero. Once two successive vectors are equal, all later vectors equal them because the map is fixed.

The dimension \(n\) counts all coordinates, including those that stay zero. In a grounded Datalog system they represent potential derived facts, each carrying a semiring annotation. The statement counts applications of the polynomial map, irrespective of the arithmetic work, representation size or equality-testing cost within a round. It therefore asks for an algebraic convergence theorem, not a fast implementation of one database operation.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the universal bound or its logical negation. A positive proof must use one constant valid simultaneously for every \(p,n,S,F\) in the definitions, including \(p=0\) and nonlinear systems of unbounded finite degree.

A negative proof must establish that, for every proposed constant \(C\), some allowed system has no fixed-point equality at any integer \(t\le C(p+1)n\). Equivalently, the first fixed-point times divided by \((p+1)n\) are unbounded, treating nonconvergence as infinite time. One example requiring more than \(n\) rounds does not refute an unspecified universal constant. A bound with an additional growing factor depending on degrees, coefficients or dimension, or a faster method using a different update rule, does not prove this exact synchronous-round target. A title announcing optimal convergence is not a substitute for a theorem with the required hypotheses and quantifiers.''',
 source_formulation=dict(text='The seminar proposes a convergence bound O((p+1)n), matching the scale of the stated lower bound, for iterative evaluation over p-stable semirings. This card expresses that proposal for grounded commutative-semiring polynomial systems.',caption='Ngo, Dagstuhl Seminar 25081, §4.2, printed p.105; polynomial-system and stability definitions in Im et al., arXiv:2312.14063v2, §2.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Semirings in Databases, Automata, and Logic — Convergence rate of Datalogo over p-stable semirings','Hung Q. Ngo (problem contributor)',2025,'https://doi.org/10.4230/DagRep.15.2.89','Dagstuhl Seminar 25081, §4.2, printed p.105'),
 ref('polynomial','Polynomial Time Convergence of the Iterative Evaluation of Datalogo Programs','Sungjin Im; Benjamin Moseley; Hung Q. Ngo; Kirk Pruhs',2024,'https://arxiv.org/abs/2312.14063v2','21 February 2024; Introduction, Theorem 1.1 p.2, §2.1 p.3 and §2.4'),
 ref('announcement','Publication listing: Optimal Convergence of Iterative Methods for Datalogo','Simon Frisk; Hangdong Zhao; Hung Ngo; Kirk Pruhs; Benjamin Moseley; Sungjin Im; Paraschos Koutris',2026,'https://hung-q-ngo.github.io/publications.html','Author-maintained listing inspected 17 September 2026; labeled PODS 2027; no linked theorem text obtained'),
 ref('listing','Publications by topic: Optimal Convergence of Iterative Methods for Datalogo','Benjamin Moseley (publication-page maintainer)',2026,'https://www.andrew.cmu.edu/user/moseleyb/bytopic.html','Inspected 17 September 2026; the listing labels the same title PODS 2025, unlike Ngo and Zhao; no theorem text obtained'),
 ],
 context_blocks=[
 block('A Boolean derived fact changes from absent to present at most once. A semiring annotation can change repeatedly, so counting facts alone no longer immediately bounds the number of rounds.'),
 block('Stability controls a truncated geometric sum for each individual semiring element. The target asks whether interactions among many nonlinear equations multiply this delay by only a linear factor in the number of coordinates.'),
 block(r'The inspected polynomial-convergence theorem has dependencies on the number \(\sigma\) of referenced coefficients and the maximum product length \(\lambda\), in addition to \(p\) and \(n\). Its separate 0-stable discussion gives linear convergence, but the general theorem does not give the universal bound stated here.','polynomial'),
 block('The authors now list a paper entitled Optimal Convergence of Iterative Methods for Datalogo. The inspected listings provide no theorem text for that entry, and their venue-year labels disagree. The catalogue therefore preserves uncertain current status while keeping the historical mathematical target precise.','announcement'),
 ],
 progress=[progress('2024-02-21','The revised preprint gives polynomial convergence with explicit coefficient-count and product-length dependencies, and separately recalls linear convergence for the 0-stable case.','polynomial'),progress('2025','The seminar proposes a universal linear-in-(p+1)n bound.'),progress('2026-09-17','The new Optimal Convergence title remains listed by its authors, but the inspected pages did not provide a theorem sufficient to verify the selected target.','announcement')],
),notes,sources,'Uncertain current status. The universal linear bound is open in the 2025 seminar, but a directly relevant Optimal Convergence paper is announced by its authors. On 17 September 2026, Ngo and Zhao label it PODS 2027 and Moseley labels it PODS 2025; no accessible theorem text for the entry was obtained. Its exact semiring assumptions, iteration rule and parameter bounds are therefore not verified here, and the card is not labeled confirmed open or resolved.',summary=[
 'The system consists of finitely many polynomial recurrences over a commutative semiring.',
 'Every round updates all coordinates from the previous vector, starting from zero.',
 'The question asks whether p-stability forces a fixed point within a universal constant times (p+1)n rounds.',
 'An announced optimal-convergence paper makes the current status uncertain because its precise theorem was not available in the inspected sources.',
 'The requested answer remains a complete Lean-checked universal convergence proof or refutation for the specified synchronous rule.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
