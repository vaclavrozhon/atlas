"""Complete constant additive offline bin packing for explicit item lists."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6640'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the approved randomized offline OPT+C target, where one constant applies to every explicitly listed rational instance.',
 'Made rational encoding, indivisible item assignment, nonempty-bin count and integral optimum precise.',
 'Specified polynomial bit time on every random tape, unconditional feasibility and per-input success probability at least two thirds.',
 'Distinguished the algorithmic additive guarantee from a configuration-LP integrality-gap theorem, multiplicative approximation and high-multiplicity input.',
 'Checked the expected-time scope of the logarithmic algorithm and the exact separate support and compressed-input results from ESA 2025 and ICALP 2026.',
 'Replaced generic acceptance with complete Lean-checked correctness, probability and resource requirements; preserved importance 95.',
]
sources=[
 'Read Bansal, New Developments in Iterated Rounding, FSTTCS 2014, §2.3 p. 5: positive item sizes at most one and the explicit OPT+O(1), or even OPT+1, algorithm question. Checked the publisher date, 12 December 2014. The source’s historical NP-completeness wording was not copied as a classification of the optimization output problem.',
 'Read Hoberg–Rothvoss, arXiv:1503.08796v1 (30 March 2015; cover 31 March), abstract and §1 pp. 1–3, §1.1 Theorem 2 and §2 p. 4 explicit total-item-count time convention. Theorem 2 is randomized expected polynomial time and compares to the fractional optimum. Checked the unchanged arXiv version and SODA 2017 metadata, pp. 2616–2625, DOI 10.1137/1.9781611974782.172. A polynomial cutoff with a singleton-packing fallback converts an always-correct expected-time packing algorithm to the card’s bounded-time constant-success convention.',
 'Read Jansen–Pirotton–Tutas, ESA 2025 Art. 48, abstract and §1 pp. 48:1–48:3. The exponential support lower bound concerns distinct bin configurations; the cited OPT+1 algorithm has nonpolynomial dependence on the number of item types. Checked publication date, 1 October 2025.',
 'Read Jansen–Ohnesorge–Pirotton, ICALP 2026 Art. 116, abstract and §1 pp. 116:1–116:2, Definition 1 and compressed input-length convention. Its ETH lower bound concerns exact high-multiplicity bin packing. Checked publication date, 1 July 2026, and author full-version arXiv:2512.02691v3 (18 May 2026). The lower-bound proof was not independently certified.',
 f'Bounded primary-source searches through {DATE} found recent restricted packing variants, high-multiplicity lower bounds and parameter-dependent algorithms, but no resolution of universal constant-additive polynomial-time packing for explicit lists. The acceptance target is not changed to the fractional integrality gap or a compressed representation.',
]
status='The inherited constant-additive algorithm question remains unresolved in the checked sources. The logarithmic additive randomized result does not give a constant loss. The ESA 2025 support theorem and ICALP 2026 exact high-multiplicity lower bound concern different targets and do not rule out the explicitly listed randomized formulation here.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',year=2026,
 formal=r'''Do there exist an integer \(C\ge0\), a uniform randomized algorithm \(A\), and absolute integers \(K,d\ge1\) such that every explicitly listed one-dimensional bin-packing instance \(I\), of binary input length \(L\), satisfies all three conditions below?

Every execution of \(A(I)\) takes at most \(K(L+1)^d\) bit operations and outputs a feasible packing into bins of capacity one; and, writing \(B_A(I)\) for its number of nonempty bins,
\[
\Pr[B_A(I)\le\operatorname{OPT}(I)+C]\ge\frac23.
\]
The constants do not depend on the number of items, their sizes or precision, the number of distinct sizes, or the optimum. The entire input is available before any packing decisions are made.''',
 definitions=r'''An instance is a finite list \(I=(s_1,\ldots,s_n)\), with \(n\ge1\) and rational sizes \(0<s_i\le1\). Write each size as \(s_i=a_i/b_i\), where \(1\le a_i\le b_i\) are positive integers given in canonical binary. The numerator and denominator need not be relatively prime. A fixed unambiguous encoding includes \(n\) and every pair \((a_i,b_i)\); \(L\) is its full bit length, including boundaries. Repeated items are separate entries. Binary multiplicities, an oracle, a circuit or a program generating a larger item list are not alternative input encodings. Malformed strings may be rejected in polynomial time.

A packing assigns each item to exactly one bin, without splitting or discarding any item. It is output as a list \(b(1),\ldots,b(n)\) of labels in \(\{1,\ldots,n\}\). Its nonempty-bin count is \(B=|\{b(i):1\le i\le n\}|\); unused labels do not count. It is feasible if
\[
\forall j\in\{1,\ldots,n\},\qquad
\sum_{i:b(i)=j}s_i\le1.
\]
All these inequalities use the exact rational input values. Define \(\operatorname{OPT}(I)\) as the minimum of \(B\) over all feasible assignments. A singleton bin for each item is feasible, so \(1\le\operatorname{OPT}(I)\le n\).

The algorithm is a single classical multitape Turing machine that may read independent fair random bits. Reading random bits, reading the input, arithmetic on binary integers and rationals, preprocessing and writing every output label count toward bit time. The polynomial time bound must hold on every random tape for every valid input. Feasibility must also hold on every tape. Only the additive-quality bound is probabilistic, and its probability must be at least \(2/3\) separately for every fixed input, not merely on average over an input distribution. On unsuccessful tapes the algorithm may use more than \(\operatorname{OPT}(I)+C\) bins, but must still produce a feasible assignment.

The algorithm is offline and can inspect all sizes before assigning any item. Bins all have exactly capacity one; there is no augmentation of capacity, additional cardinality constraint, packing order requirement, restriction on the number of item types or lower bound on item size beyond positivity. It cannot call an optimum oracle or use uncharged instance-dependent advice. A deterministic algorithm is allowed as a special case.

The additive constant \(C\) is existentially chosen once for all instances. The question does not require \(C=1\), a prescribed value of \(C\), or finding the smallest possible constant. The benchmark \(\operatorname{OPT}\) is the integral packing optimum, not the value of a fractional relaxation. This is an exact algorithm-existence proposition; the numerical tolerance for a separate value-estimation problem does not alter the displayed approximation guarantee.''',
 answer_criterion=r'''Supply \(A,C,K,d\) and complete Lean-checked proofs of worst-case bit time, feasibility on every random tape and the per-input probability bound. Alternatively, supply a complete Lean-checked proof that no choices of a uniform randomized algorithm and such absolute constants meet these conditions.

An additive loss growing with the instance or optimum, a fixed multiplicative approximation ratio, increased bin capacity, a guarantee only for a restricted family, or an existential fractional integrality-gap bound without the required algorithm does not settle the question. Impossibility of one rounding method is not impossibility of all algorithms. A negative answer restricted to deterministic algorithms would not exclude the permitted randomized algorithms.''',
 source_formulation=dict(text='Bansal asks whether ordinary one-dimensional bin packing admits a polynomial-time algorithm using OPT+O(1) bins, and separately mentions the stronger OPT+1 target. This card retains the constant-additive alternative and its previously selected explicit rational input and randomized guarantee.',caption='Paraphrase of New Developments in Iterated Rounding, FSTTCS 2014, §2.3 p. 5.',citation='primary',format='editorial_paraphrase'),
 why='The question asks whether the absolute loss in a basic packing problem can be bounded independently of instance scale. Such a result would go beyond a ratio tending to one by controlling the number of extra bins itself, and would sharpen a longstanding boundary in approximation algorithms.',
 references=[
 ref('primary','New Developments in Iterated Rounding (Invited Talk)','Nikhil Bansal',2014,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2014.1','FSTTCS 2014, 1–10; published 12 December 2014; §2.3 p. 5, constant-additive algorithm question'),
 ref('loggap','A Logarithmic Additive Integrality Gap for Bin Packing','Rebecca Hoberg; Thomas Rothvoss',2017,'https://arxiv.org/abs/1503.08796v1','SODA 2017, 2616–2625, DOI 10.1137/1.9781611974782.172; author v1 posted 30 March 2015; §1.1 p. 3 Theorem 2 and §2 p. 4 total-item-count convention'),
 ref('support','The Support of Bin Packing Is Exponential','Klaus Jansen; Lis Pirotton; Malte Tutas',2025,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.48','ESA 2025, LIPIcs 351, 48:1–48:16; published 1 October 2025; abstract and §1 pp. 48:1–48:3, support and type-dependent algorithms'),
 ref('highmultiplicity','A Tight Double-Exponential Lower Bound for High-Multiplicity Bin Packing','Klaus Jansen; Felix Ohnesorge; Lis Pirotton',2026,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.116','ICALP 2026, LIPIcs 374, 116:1–116:20; published 1 July 2026; abstract and §1 pp. 116:1–116:2, Definition 1 and exact compressed-input target'),
 ],
 context_blocks=[
 block('Every item must fit completely in one bin, and feasibility can be checked from the output assignment. The unknown optimum is only the comparison benchmark; it is not supplied to the algorithm.'),
 block(r'A guarantee of \((1+\varepsilon)\operatorname{OPT}+C_\varepsilon\) can still waste an unbounded number of bins as the optimum grows. The requested \(\operatorname{OPT}+C\) guarantee instead limits the absolute loss by one universal constant.'),
 block('Hoberg and Rothvoss obtain a logarithmic additive guarantee with a randomized expected-polynomial-time algorithm. Their comparison is even to the fractional configuration optimum, obtained by allowing nonnegative fractional weights on feasible bin patterns. The logarithmic loss still grows.','loggap'),
 block('A constant integrality gap for a relaxation would be a structural statement about fractional and integral optima. The card asks for a polynomial-time algorithm outputting the near-optimal assignment itself. Neither statement should be substituted for the other without the needed algorithmic argument.','loggap'),
 block('The 2025 support theorem bounds how many different bin patterns some solutions need. Its introduction also records an OPT+1 algorithm whose dependence on the number of item types is not polynomial. These address other aspects of the problem.','support'),
 block('High-multiplicity input stores large numbers of equal items by binary counts. The 2026 lower bound concerns exact optimization measured in that compressed length. Here every item is listed and the algorithm is allowed a fixed additive loss.','highmultiplicity'),
 ],
 progress=[
 progress('2014-12-12','The invited source explicitly states the constant-additive and stronger additive-one algorithm questions.'),
 progress('2015–2017','Hoberg–Rothvoss obtain a logarithmic additive randomized algorithm; author preprint in 2015, SODA publication in 2017.','loggap'),
 progress('2025-10-01','The support of bin-packing solutions is shown to require exponential dependence on the number of types in certain instances.','support'),
 progress('2026-07-01','A conditional tight lower bound is published for exact high-multiplicity packing, a different input and approximation target.','highmultiplicity'),
 ],
),notes,sources,status,summary=[
 'The input explicitly lists rational item sizes, and each item must be assigned whole to a unit-capacity bin.',
 'The question asks for a polynomial-time algorithm using at most a fixed constant more bins than the optimal integral packing.',
 'Randomization is allowed, but every output must be feasible and the quality guarantee must hold with probability at least two thirds on every input.',
 'All computation uses counted bit operations, and repeated items are listed rather than encoded by compressed multiplicities.',
 'A complete Lean-checked proof must establish the uniform algorithmic guarantee or rule it out; logarithmic losses and compressed-input lower bounds do not settle it.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
