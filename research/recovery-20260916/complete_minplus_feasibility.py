"""Review exact integer min-plus feasibility with binary coefficient cost."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0046';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Polynomial-time feasibility of integer min-plus linear systems',
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a deterministic algorithm that, given arbitrary integer matrices \(A=(a_{ij}),B=(b_{ij})\in\mathbb Z^{m\times n}\), with \(m,n\ge1\) and all entries in binary, decides in polynomial bit time whether there is \(x\in\mathbb Z^n\) satisfying
\[
\min_{1\le j\le n}(a_{ij}+x_j)
=\min_{1\le j\le n}(b_{ij}+x_j)
\qquad(1\le i\le m)?
\]''',
 definitions=r'''The additions and the order used in each minimum are ordinary integer addition and order. Each row imposes equality of its two minimum values; a minimum may be attained at one or several indices. This is the min-plus equality presentation of the source question. It does not impose the different tropical convention that each single minimum be attained at least twice.

All coefficients and all solution coordinates must be finite integers. The value \(+\infty\) is not an allowed coefficient or solution coordinate. Both matrix dimensions vary with the input. Matrices are given explicitly by all their entries, each as a signed binary integer, with fixed length delimiters for the entries and dimensions. Let \(L\) denote the total input bit length.

The target is one deterministic multi-tape Turing machine \(D\) and constants \(K>0\), \(a\in\mathbb N\) such that every valid input is processed within \(K(L+1)^a\) steps, and the output is 1 exactly when an integer solution exists. There is no randomness, advice or oracle. The machine and constants are independent of \(m,n,A,B\). Arithmetic is charged at its actual bit cost, not as unit-cost operations on unbounded integers.

Equivalently for these dense inputs, the time must be polynomial in \(m,n,\log_2(H+2)\), where \(H=\max_{i,j}\{|a_{ij}|,|b_{ij}|\}\). A time bound polynomial in \(H\) itself is not sufficient. No strongly polynomial bound independent of coefficient bit length is requested. The output is a feasibility decision; the full solution set, its dimension, or the number of solutions is not requested.

Adding a common integer to every coordinate of a solution preserves all equalities, so feasibility has no prescribed coordinate normalization. Negative coordinates are allowed. Unsatisfiable instances must be rejected within the same running-time bound.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof that the stated feasibility language is in deterministic polynomial time, or a proof that it is not. A positive answer must establish exact equivalence to integer feasibility, termination and the polynomial bit bound. Pseudopolynomial algorithms, a result with a fixed matrix dimension, or numerical approximate feasibility do not suffice.',
 why='Min-plus linear equations connect algebraic feasibility to two-player mean-payoff games. The challenge is to obtain a running time polynomial in the written input rather than in the magnitudes of its coefficients.',
 source_formulation=dict(text='Grigoriev asks for polynomial complexity in the two matrix dimensions and the logarithm of the integer coefficient bound, for min-plus equations over the integers.',caption='Dagstuhl Seminar 15242, §5.2, printed pp.43–44 (combined issue PDF pp.45–46).',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Complexity of Symbolic and Numerical Problems: Complexity of solving tropical or min-plus linear systems','Dima Grigoriev',2015,'https://doi.org/10.4230/DagRep.5.6.28','Seminar 15242, §5.2, printed pp.43–44; combined issue PDF pp.45–46'),
 ref('equivalence','Complexity of tropical and min-plus linear prevarieties','Dima Grigoriev; Vladimir V. Podolskii',2012,'https://arxiv.org/abs/1204.4578','Preprint v1, 20 April 2012; Introduction equation (2), pp.2–4; §3, Corollaries 8–9 and Lemma 11, pp.12–13; journal publication Computational Complexity 24 (2015), 31–64'),
 ref('recent','Set-defined graph classes: χ-boundedness meets tropical algebra','Sarosh Adenwalla; Samuel Braunfeld; Tomáš Hons; John Sylvester; Viktor Zamaraev',2026,'https://arxiv.org/abs/2607.23754','26 July 2026, §3.7.2 Algorithms, printed p.21/PDF p.23'),
 ],
 context_blocks=[
 block('The source distinguishes polynomial dependence on the numeric coefficient bound from polynomial dependence on its logarithm. Only the latter resolves the binary-input target.'),
 block('Integer min-plus feasibility, tropical linear solvability and mean-payoff games are polynomial-time equivalent in the cited work. Their syntactic definitions still differ.','equivalence'),
 block('The feasibility problem lies in NP and coNP. Those certificate bounds do not give the deterministic polynomial-time algorithm asked for.','equivalence'),
 block('The July 2026 account again states polynomial complexity in binary weight length as open. Its graph-class reduction transfers the problem instead of supplying the missing solver.','recent'),
 block('This card retains the source’s finite-integer equality model. The corresponding game formulation is recorded separately in TCS-6568; the connection is an equivalence of algorithmic questions.','equivalence'),
 ],
 progress=[progress('2012','The preprint relates integer tropical and min-plus feasibility to mean-payoff games.','equivalence'),progress('2015','The Dagstuhl question explicitly asks for polynomial dependence on coefficient bit length.'),progress('2026-07-26','The newer tropical-algebra account retains this algorithmic gap.','recent')],
),[
 'Replaced the index label by exact feasibility for the finite-integer min-plus equality system written in the source.',
 'Specified varying dimensions, signed binary coefficients, integer solution domain and deterministic bit complexity.',
 'Separated pseudopolynomial bounds, other tropical semantics and computation of the solution-space dimension.',
 'Retained the existing importance assessment and required a complete Lean-checked complexity answer.',
],[
 'Read the complete §5.2 question in Dagstuhl Seminar 15242, printed pp.43–44, including integer domain and logarithmic coefficient-size target.',
 'Read Grigoriev–Podolskii arXiv:1204.4578v1 Introduction and relevant equivalence statements. The downloaded version is the 2012 preprint, not the later journal typesetting.',
 'Read the July 2026 graph/tropical paper §3.7.2, which explicitly distinguishes pseudopolynomial and binary-input polynomial time. Bounded status checks through 17 September 2026 found no resolution.',
], 'Source-open for exact integer min-plus feasibility in deterministic polynomial bit time. The July 2026 primary source still identifies the corresponding tropical/mean-payoff binary-weight problem as open. Finite integers and the equality presentation are retained; pseudopolynomial algorithms do not answer this target. Checked through 17 September 2026.',summary=[
 'Each input row equates two minima of integer coefficients plus unknown integer coordinates.',
 'The question asks whether a single deterministic algorithm can decide feasibility in polynomial time.',
 'Time is measured in the full binary input length, with both matrix dimensions allowed to grow.',
 'The problem is polynomial-time equivalent to mean-payoff games, while known pseudopolynomial bounds depend on coefficient magnitudes.',
 'An answer must include a complete Lean-checked polynomial-bit-time decider or a proof that none exists.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
