"""Review the selected VNP-family semantic multilinear lower-bound target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6893';claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user’s explicit choice of some multilinear family in VNP over C rather than specifically the permanent.',
 'Defined VNP using polynomially many Boolean summation variables and a polynomial-size, polynomial-degree arithmetic circuit family; arbitrary unconstrained coefficient tables do not suffice.',
 'Retained the survey’s semantic gatewise multilinearity, with unrestricted sharing, depth and complex constants; did not weaken the target to syntactic multilinearity.',
 'Made superpolynomial mean absence of every polynomial family-size bound, with explicit arbitrarily-large-index quantifiers and no stronger eventual condition.',
 'Separated this VNP lower-bound target from TCS-6883, which additionally requires small unrestricted circuits for the same outputs.',
 'Read the source VNP definition and lower-bound context, checked the syntactic near-quadratic theorem and January 2026 discussion, and excluded the explicitly withdrawn April rank-barrier claim.',
 'Individually assessed importance and required complete Lean-checked membership and lower-bound proofs or the precise negation.',
]
sources=[
 'Read Shpilka–Yehudayoff, Arithmetic Circuits: A Survey of Recent Results and Open Questions, §1.2 Definitions 1.2–1.3 pp.3–4; semantic and syntactic definitions p.7; §3.6 Theorems 3.10–3.12 and Open Problem 13 pp.36–37 (Open Problem 13 on PDF p.42). The surrounding explicit lower-bound example is in VNP with 0/1 coefficients. The user selected VNP over C as the precise family requirement; 0/1 coefficients and efficient coefficient generation are not additional requirements of this card.',
 'Read Alon–Kumar–Volk, Unbalancing Sets and an Almost Quadratic Lower Bound for Syntactically Multilinear Arithmetic Circuits, author manuscript abstract, §1.1 and Theorem 1.1 pp.1–2. The lower bound is Omega(n^2/log^2 n) against syntactically multilinear circuits, with the semantic distinction explicitly discussed.',
 'Read Fabris–Limaye–Srinivasan–Yehudayoff, ECCC TR26-001, 1 January 2026, abstract and Introduction p.1 including footnote 1. It retains explicit superpolynomial branching-program lower bounds as open, describes the circuit lower-bound frontier as nearly quadratic in the syntactic setting, and does not claim a semantic circuit lower bound.',
 'Read the April 2026 Kush rank-barrier claim and then its primary withdrawal notice at arXiv:2604.00746v2, dated 11 May 2026. The author identifies a missing conditional-probability bound in Lemma 4.1 and says every result depends on it. No polynomial full-rank construction or resulting unconditional method barrier from that withdrawn manuscript is used as a theorem.',
 'Bounded primary-source searches through 17 September 2026 found no resolution of the selected multilinear-VNP versus semantic multilinear circuit target over C. This is not an exhaustive current-status certification or independent verification of all cited proofs.',
]
complete(identifier,dict(
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a family of multilinear polynomials \(f_n\in\mathbb C[x_1,\ldots,x_n]\), \(n\ge2\), belonging to \(\mathrm{VNP}_{\mathbb C}\), such that
\[
\forall k\ge1\ \forall N\ge2\ \exists n\ge N:
\operatorname{MC}(f_n)>n^k?
\]
All three quantified parameters are integers, and \(\operatorname{MC}(f_n)\) denotes the minimum size of a semantically multilinear arithmetic circuit over \(\mathbb C\) computing \(f_n\). Thus the target is a VNP family for which no polynomial-size family of gatewise multilinear circuits exists. The family is not required to be the permanent.''',
 definitions=r'''An arithmetic circuit over \(\mathbb C\) is a finite directed acyclic graph with one output gate. Input gates are variables or arbitrary complex constants. Every internal gate adds or multiplies two supplied predecessor values; a predecessor can supply both operands. Gate values are formal polynomials in commuting variables. There are no division gates, tests, approximations or limit operations. Output correctness is exact coefficientwise polynomial equality. The size is the total number of gates, including inputs. Depth and fan-out are unrestricted, and intermediate computations may be shared. A complex constant costs one gate, with no bound on its description length. These are nonuniform algebraic size measures, not bit-operation counts.

A polynomial is multilinear if every variable has exponent at most one in each monomial with nonzero coefficient. Constants and zero are multilinear. A circuit is semantically multilinear when the actual polynomial computed at every gate has this property. Merely having a multilinear output is insufficient. Conversely, semantic multilinearity does not require the variable labels appearing in the two input subcircuits of a multiplication gate to be disjoint: intermediate cancellation can remove a variable’s dependence. Syntactic multilinearity imposes that extra disjointness condition and is a separate restriction.

For a multilinear polynomial \(f\), \(\operatorname{MC}(f)\) is the smallest gate count of any semantically multilinear circuit computing it. It is finite because a finite sum of multilinear monomials can be evaluated by such a circuit. The definition permits every possible circuit with the stated properties, not just a particular normal form or depth.

For this card, \((f_n)\in\mathrm{VNP}_{\mathbb C}\) means that there are an integer \(b\ge1\), integers \(0\le m(n)\le n^b\), and polynomials
\[
g_n\in\mathbb C[x_1,\ldots,x_n,y_1,\ldots,y_{m(n)}]
\]
such that every \(g_n\) has total degree at most \(n^b\), is computable by an unrestricted arithmetic circuit of size at most \(n^b\), and
\[
f_n(x)=\sum_{u\in\{0,1\}^{m(n)}}g_n(x,u)
\qquad(n\ge2).
\]
For \(m(n)=0\), the sum has one term. The witness bits \(u\) are substituted by the corresponding elements 0 and 1 of \(\mathbb C\). The circuits for \(g_n\) need not be multilinear. Requiring these polynomial size and degree bounds rules out arbitrary unstructured families; merely counting hard coefficient tables does not establish VNP membership.

The VNP representation and the circuits may be chosen separately at each length. No uniform algorithm for generating them or their complex constants is additionally required. Both the representation and the lower bound use the fixed field \(\mathbb C\). The lower-bound quantifiers mean that every proposed exponent fails at arbitrarily large indices. They do not require an eventual lower bound at all sufficiently large indices. Membership in VNP alone does not assert that the outputs themselves have small unrestricted circuits.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the existence statement or its logical negation. A positive answer must rigorously define a family, prove its multilinearity and its VNP representation with the stated polynomial bounds, and prove the superpolynomial lower bound against every semantically multilinear circuit over \(\mathbb C\).

A negative answer must show that every multilinear family in \(\mathrm{VNP}_{\mathbb C}\) has a polynomial-size family of semantically multilinear circuits. Showing that one candidate has small circuits does not refute the existential target. A counting argument without the VNP membership proof, or a lower bound only for formulas, branching programs, bounded-depth circuits or syntactically multilinear circuits, is insufficient. Unlike the separate unrestricted-versus-multilinear comparison, a positive answer here need not prove a polynomial-size unrestricted circuit upper bound for the chosen outputs.''',
 why='Unbounded-depth multilinear circuits form a major frontier between successful restricted algebraic lower bounds and general circuit complexity. Requiring a VNP family makes the target a lower bound for algebraically structured polynomials, rather than the nonconstructive existence of hard coefficient tables.',
 importance=dict(score=89,method='editorial',assessed_on='2026-09-17',reason='A central unrestricted-depth algebraic lower-bound target for structured polynomial families, beyond known formula, depth-restricted and polynomial syntactic-circuit bounds.'),
 source_formulation=dict(text='The survey asks for a superpolynomial multilinear circuit lower bound. Its preceding theorem concerns an explicit family in VNP. The user selected some multilinear VNP family over the complex numbers as the precise target, without fixing the permanent.',caption='Shpilka–Yehudayoff, §3.6, Theorem 3.12 and Open Problem 13, printed p.37 (PDF p.42); VNP definition in §1.2, pp.3–4.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Arithmetic Circuits: A Survey of Recent Results and Open Questions','Amir Shpilka; Amir Yehudayoff',2010,'https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf','§1.2 pp.3–4; multilinear definitions p.7; §3.6 Theorem 3.12 and Open Problem 13, printed p.37 (PDF p.42)'),
 ref('quadratic','Unbalancing Sets and an Almost Quadratic Lower Bound for Syntactically Multilinear Arithmetic Circuits','Noga Alon; Mrinal Kumar; Ben Lee Volk',2020,'https://web.math.princeton.edu/~nalon/PDFS/mult2.pdf','Combinatorica paper; author manuscript abstract, §1.1 and Theorem 1.1, printed pp.1–2'),
 ref('rank','Multilinear Algebraic Branching Programs and the Min-Partition Rank Method','Théo Borém Fabris; Nutan Limaye; Srikanth Srinivasan; Amir Yehudayoff',2026,'https://eccc.weizmann.ac.il/report/2026/001/','1 January 2026; abstract and Introduction p.1, including footnote 1'),
 ref('withdrawal','Withdrawal: An Unconditional Barrier for Proving Multilinear Algebraic Branching Program Lower Bounds','Deepanshu Kush',2026,'https://arxiv.org/abs/2604.00746v2','11 May 2026 withdrawal notice and Comments; theorem claims not used as established results'),
 ],
 context_blocks=[
 block('Multilinearity limits the exponent of each variable at every gate, but a circuit can still reuse values many times. This sharing makes unbounded-depth circuit lower bounds substantially different from formula lower bounds.'),
 block('The VNP condition expresses each output as a sum of a polynomial-size computation over polynomially many Boolean witness coordinates. It gives a precise algebraic restriction on the family while allowing the output sum itself to contain exponentially many terms.'),
 block(r'The published almost-quadratic lower bound is \(\Omega(n^2/\log^2 n)\) for syntactically multilinear circuits. Its size growth remains polynomial, and its circuit model imposes an additional syntactic restriction. Both distinctions matter for this target.','quadratic'),
 block('The January 2026 rank-method paper retains related lower-bound questions for multilinear branching programs and explicitly uses syntactic models. The later April claim of a polynomial-size full-rank construction was withdrawn in May and supplies no established resolution.','withdrawal'),
 block('TCS-6883 asks for a separation using outputs that already have small unrestricted circuits. This card permits any multilinear VNP family, so it seeks a general lower-bound milestone without that additional upper-bound requirement.'),
 ],
 progress=[progress('2010','The survey formulates the multilinear circuit lower-bound question next to a VNP-family syntactic lower bound.'),progress('2020','The syntactic lower bound improves to the almost-quadratic scale in the published Alon–Kumar–Volk result.','quadratic'),progress('2026-01-01','The rank-method paper retains the related branching-program frontier and explicitly states the syntactic scope of its models.','rank'),progress('2026-05-11','The proposed unconditional barrier paper is withdrawn after a proof gap is identified.','withdrawal')],
),notes,sources,'Source-open for the user-selected multilinear VNP family target over C. The January 2026 primary discussion retains related weaker-model lower-bound frontiers. The April proposed rank-method barrier is explicitly withdrawn as of 11 May 2026 and is not treated as a theorem. No resolution of the precise semantic multilinear target was identified in bounded searches through 17 September 2026.',summary=[
 'The target is a multilinear polynomial family in VNP over the complex numbers.',
 'VNP membership is specified by a bounded-degree polynomial-size circuit summed over polynomially many Boolean witness coordinates.',
 'The family must require more than every polynomial size bound for circuits whose every intermediate polynomial is multilinear.',
 'No particular family such as the permanent is prescribed, and no small unrestricted output circuits are required.',
 'The answer must include complete Lean-checked membership and lower-bound proofs or prove that all such families have polynomial-size semantic multilinear circuits.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
