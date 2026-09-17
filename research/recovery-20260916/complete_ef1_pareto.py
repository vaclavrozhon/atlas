"""Complete the unrestricted additive-goods EF1 and PO computation question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-1115'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered nonnegative additive valuations and complete integral allocations from the survey’s global conventions.',
 'Specified explicit binary rational input and deterministic polynomial bit time, allowing arbitrary numbers of agents and goods.',
 'Defined EF1 with removal of at most one good, including empty bundles, and integral Pareto optimality over every complete allocation.',
 'Separated exact output guarantees from approximate fairness, fractional Pareto optimality, fixed-agent algorithms and pseudo-polynomial running times.',
 'Checked the May 2026 published fixed-agent result and the March 2026 balanced-allocation paper, which explicitly retain the general question.',
 'Preserved the existing individually assessed importance 82.',
]
sources=[
 'Read Amanatidis–Birmpas–Filos-Ratsikas–Voudouris, arXiv:2202.07551v2 (4 March 2022), course-hosted full PDF, §1.1 p. 2, §2 Definition 3 p. 3, and Open Problem 1 p. 4. The global setting is additive, normalized, nonnegative valuations and complete partitions.',
 'Read Mahara, arXiv:2411.01810v1 (4 November 2024), abstract, §§1–1.2 pp. 2–4, Theorem 1.1 p. 4, and §2 pp. 5–6. Checked the publisher abstract and metadata for the WINE 2025 proceedings chapter, LNCS 16266:413–430, first online 1 May 2026, DOI 10.1007/978-3-032-18660-7_22. The fixed-agent restriction is explicit, and footnote 3 addresses empty bundles in the EF1 definition.',
 'Read Kawase–Mahara, arXiv:2603.05956v1 (6 March 2026), abstract and §1 pp. 1–3, especially the explicit general-case open question on p. 2 and the restricted balanced-allocation results. Checked AAAI 2026 publisher metadata; the paper concerns additional balanced constraints and restricted valuation families.',
 'Read the abstract and introduction of Garg–Murhekar, arXiv:2204.14229v2 (15 October 2023). Mahara’s later paper explicitly disputes parts of its proof. Those contested pseudo-polynomial fPO claims were not promoted to established progress in this card; neither source claims a general polynomial-time EF1+PO algorithm.',
 f'Bounded primary-source searches through {DATE} found no resolution of the unrestricted additive-goods polynomial-time question. Results about chores, submodular valuations, constant numbers of agents, balanced allocations and approximate welfare were checked for scope rather than treated as resolutions.',
]
status='The 2022 survey asks for polynomial-time EF1 and PO allocation under additive goods valuations. The May 2026 publication of Mahara’s fixed-agent algorithm explicitly retains the general question, as does the March 2026 balanced-allocation paper. No unrestricted polynomial-time algorithm or unconditional impossibility theorem was found in the bounded later-work review.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Is there a uniform deterministic polynomial-time algorithm that, for every explicitly given instance of indivisible goods with nonnegative additive valuations, outputs an allocation that is both envy-free up to one good (EF1) and Pareto optimal (PO)?

Precisely, do there exist one algorithm \(A\) and integers \(C,c\ge1\) such that, for every \(n\ge1\), \(m\ge0\), and matrix
\[
(v_{ig})_{i\in[n],\,g\in[m]}\in\mathbb Q_{\ge0}^{n\times m},
\]
\(A\) outputs a complete integral allocation satisfying the two conditions below in at most \(C(L+1)^c\) bit steps, where \(L\) is the full binary input length? The same program, constant and exponent must work for every number of agents and goods.''',
 definitions=r'''Write \([q]=\{1,\ldots,q\}\), with \([0]=\varnothing\). There are \(n\) agents and \(m\) distinct goods. Each good is indivisible and must be assigned to exactly one agent. An allocation is a tuple \(X=(X_1,\ldots,X_n)\) of disjoint subsets of \([m]\) whose union is \([m]\). Empty bundles are permitted.

Agent \(i\)'s value for a bundle \(S\) is
\[
v_i(S)=\sum_{g\in S}v_{ig}.
\]
All entries are nonnegative; zero entries, zero-valued agents and goods valued at zero by everyone are allowed. Values depend only on the agent's own bundle. There are no monetary transfers, capacities, equal-bundle-size requirements, unequal entitlements or restrictions on which agent may receive which good.

The allocation \(X\) is EF1 when
\[
\forall i,j\in[n]\ \exists S\subseteq X_j,\quad
|S|\le1\quad\text{and}\quad v_i(X_i)\ge v_i(X_j\setminus S).
\]
The removal is only hypothetical and does not discard an allocated good. The set \(S\) may depend on the ordered pair \(i,j\). Allowing \(S=\varnothing\) covers the case of no envy and empty envied bundles. The condition asks for some removable good, rather than every removable good; the latter is a stronger fairness condition.

The allocation \(X\) is PO if there is no other complete integral allocation \(Y=(Y_1,\ldots,Y_n)\) such that
\[
\bigl(\forall i\in[n],\ v_i(Y_i)\ge v_i(X_i)\bigr)
\quad\text{and}\quad
\bigl(\exists j\in[n],\ v_j(Y_j)>v_j(X_j)\bigr).
\]
The competing allocation may reassign any number of goods, and need not be EF1. PO therefore excludes every integral Pareto improvement, not just a local exchange or another fair allocation. The target uses integral alternatives. Fractional Pareto optimality, which also excludes improvements obtained by splitting goods, is stronger and is not separately required.

The input explicitly lists \(n,m\) and every matrix entry in row-major order. Use unary headers \(1^n0\,1^m0\), followed by each rational as \(p_{ig}/q_{ig}\) with integers \(p_{ig}\ge0\), \(q_{ig}\ge1\). For a nonnegative integer \(a\), encode \(a+1\) by its \(b\)-bit binary representation preceded by \(1^b0\). Use this code for every numerator and denominator, requiring no trailing bits. Fractions need not be reduced. Let \(L\) be the total number of bits, including all headers and rational entries.

The algorithm is a deterministic multitape Turing machine with one fixed finite program, read-only input and initially blank work tapes. Each transition reads or writes the cells under its heads and moves each head by at most one cell. All parsing, arithmetic, preprocessing and output are charged; no valuation oracle, advice or randomness is available. The output lists the receiving agent for each good, in increasing good order, using \(\lceil\log_2(n+1)\rceil\) bits per label. For \(m=0\), the empty output denotes the unique allocation. Malformed inputs must be rejected within the same polynomial bound.

Polynomial time is measured in the bit length, not in the magnitudes of the values. A bound polynomial in a largest integer value can be exponential in \(L\). Conversely, the target does not demand strongly polynomial arithmetic complexity. Rational inputs do not add an essential promise: multiplying all values of an agent by the product of that agent's denominators produces nonnegative integers of polynomial bit length and preserves both EF1 and PO.

The requested output must satisfy both conditions exactly. This is an algorithm-existence proposition, not a numerical target, so absolute \(1/100\) accuracy does not allow an envy violation or a Pareto improvement.''',
 answer_criterion=r'''Supply a complete Lean-checked algorithm with the stated uniform polynomial bit-time bound and proofs that every output is a complete allocation satisfying EF1 and PO; or supply a complete Lean-checked proof that no such algorithm exists. An existence theorem for allocations without the running-time guarantee, a pseudo-polynomial algorithm, an algorithm for each fixed number of agents with a growing exponent, or an approximation to either output condition is insufficient. A conditional hardness theorem is only a conditional obstruction unless its required complexity separation is also proved. Hardness of maximizing Nash welfare or of verifying PO does not by itself prove hardness of finding some EF1 and PO allocation.''',
 source_formulation=dict(
 text='Open Problem 1 asks whether an EF1 and Pareto-optimal allocation can be computed in polynomial time. The survey’s global setting specifies complete allocations of indivisible goods and nonnegative additive valuations.',
 caption='Paraphrase of the 4 March 2022 survey version, §2, Open Problem 1, p. 4; input model from §1.1, p. 2.',
 citation='primary',format='editorial_paraphrase'),
 why='Fairness and efficiency can each be obtained quickly, and an allocation satisfying both always exists. The unresolved computational question asks whether the two can be reconciled without time proportional to numerical value magnitudes or an exponent growing with the number of participants. It is a basic boundary between existence and efficient construction in discrete fair division.',
 references=[
 ref('primary','Fair Division of Indivisible Goods: A Survey',
  'Georgios Amanatidis; Georgios Birmpas; Aris Filos-Ratsikas; Alexandros A. Voudouris',2022,
  'https://arxiv.org/abs/2202.07551v2',
  'Version 2, 4 March 2022; §1.1 p. 2, §2 Definition 3 p. 3 and Open Problem 1 p. 4; checked full course-hosted PDF'),
 ref('fixed','A Polynomial-Time Algorithm for Fair and Efficient Allocation with a Fixed Number of Agents',
  'Ryoga Mahara',2026,'https://doi.org/10.1007/978-3-032-18660-7_22',
  'WINE 2025 proceedings, LNCS 16266:413–430, first online 1 May 2026; checked full arXiv:2411.01810v1, 4 November 2024, §§1–1.2, Theorem 1.1 p. 4, §2 pp. 5–6'),
 ref('balanced','Fair and Efficient Balanced Allocation for Indivisible Goods',
  'Yasushi Kawase; Ryoga Mahara',2026,'https://arxiv.org/abs/2603.05956v1',
  'Version 1, 6 March 2026; abstract and §1 pp. 1–3, especially the general-case open question on p. 2; AAAI 2026 publication'),
 ],
 context_blocks=[
 block('The survey records existence of EF1 and PO allocations via Nash welfare and an earlier pseudo-polynomial-time algorithm. Neither establishes a polynomial bit-time bound for arbitrary binary values.'),
 block('An algorithm may return any allocation satisfying both conditions. It is not required to maximize Nash welfare, maximize total utility, or provide a separate efficiently checkable certificate of Pareto optimality. Hardness of these different tasks does not settle the requested search problem.','fixed'),
 block('Mahara’s result, published online in May 2026, finds an allocation satisfying EF1 and the stronger fractional Pareto optimality when the number of agents is fixed. The same publication explicitly retains the general polynomial-time question.','fixed'),
 block('The March 2026 balanced-allocation paper studies equal bundle sizes and restricted valuation families. Its introduction also states that the unrestricted general-case computation question remains open; those constrained special cases do not resolve the present all-matrices target.','balanced'),
 ],
 progress=[
 progress('2022-03-04','The checked survey version states the polynomial-time computation question after recalling existence and pseudo-polynomial algorithms.'),
 progress('2024-11-04','Mahara’s preprint gives a polynomial-time EF1 and fractional-PO algorithm for a fixed number of agents.','fixed'),
 progress('2026-03-06','The balanced-allocation preprint retains the unrestricted question while solving constrained special cases.','balanced'),
 progress('2026-05-01','The fixed-agent result is published online in the WINE 2025 proceedings.','fixed'),
 progress(DATE,'The review specifies binary rational values, complete allocations, exact EF1 and integral PO, and a uniform polynomial bound for arbitrary agent counts.'),
 ],
),notes,sources,status,summary=[
 'The task is to divide indivisible goods among agents whose nonnegative values add across goods.',
 'EF1 allows each agent’s envy of another bundle to disappear after the hypothetical removal of at most one good.',
 'Pareto optimality forbids any reassignment that improves one agent without hurting another.',
 'Allocations satisfying both properties exist, but the card asks for one polynomial-time algorithm on explicitly encoded rational values and arbitrary numbers of agents.',
 'Known pseudo-polynomial and fixed-agent algorithms do not settle this general bit-time requirement.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
