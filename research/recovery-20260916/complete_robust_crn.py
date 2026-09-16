"""Individual source review of rate-constant-independent CRN classification."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1588'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the source’s joint classification conjecture, keeping its predicate and function clauses as one explicitly stated conjunction.',
 'Replaced the conclusion’s informal function-class name by the exact threshold-piecewise rational floor-affine definition in Definition 2.3.',
 'Defined the finite network, integer stoichiometry, nonnegative real concentrations, mass-action ODE and fixed arbitrary positive rate constants.',
 'Specified fixed real initial context independent of input and rate constants, global trajectories, voter liminf and output convergence, including boundary inputs.',
 'Distinguished clipping at zero from the integer floor operation, rational slopes from real offsets, and this model from stable and reverse-robust computation.',
 'Assessed importance individually and added complete Lean proof/refutation acceptance for the exact classification.',
]
sources=[
 'Read the published DISC 2025 paper, Article 19: Definitions 2.1–2.7 on pp. 19:5–19:8, Theorems 3.7 and 3.10, and §4 on pp. 19:15–19:16.',
 'Checked the original arXiv:2506.06590 record, version 1 of 6 June 2025. Its abstract states the constructive directions; the published conclusion still conjectures their necessity.',
 'Checked Doty’s current publication list and the primary arXiv:2604.14355 abstract, 15 April 2026. Reverse-robust computation concerns discrete molecule counts and temporary reversal of reactions, a different model.',
 'Bounded primary-source searches through 16 September 2026 found no classification theorem or counterexample resolving this mass-action conjecture. The constructive proofs were not independently re-proved in this editorial review.',
]
status=('The published DISC 2025 paper proves the sufficient directions and conjectures that they are necessary in §4. '
 'This review fixes the exact model from Definitions 2.1–2.7, with initial context and arbitrary fixed positive rate constants. '
 'The 2026 reverse-robust CRN result concerns a different discrete model. No resolution of the joint continuous-model classification was found in the bounded review.')
complete(identifier,dict(
 title='Classification of robust chemical computation',criterion='characterization',question_type='yes_no',
 formal=r'''Is the following classification true? For every integer \(k\ge1\), both equivalences hold:
\[
\begin{aligned}
&\forall\varphi:\mathbb R_{\ge0}^{k}\to\{0,1\},&
\varphi\text{ is robustly decidable}
&\iff \varphi\text{ is a multi-threshold predicate};\\
&\forall f:\mathbb R_{\ge0}^{k}\to\mathbb R_{\ge0},&
f\text{ is robustly computable}
&\iff f\text{ is threshold-piecewise rational floor-affine}.
\end{aligned}
\]
The terms on both sides are defined below. The question is the conjunction of the predicate and numerical-output classification clauses, in the continuous mass-action chemical reaction model with fixed initial context. Robustness quantifies over every assignment of positive rate constants that remain fixed throughout a trajectory.''',
 definitions=r'''A chemical reaction network has a finite species set \(\Lambda\) and finitely many reactions indexed by \(R\). Reaction \(r\) has reactant and product vectors \(a_r,b_r\in\mathbb N^\Lambda\), where \(\mathbb N=\{0,1,\ldots\}\), with \(a_r\ne b_r\). The vectors give integer stoichiometric multiplicities. Empty reactants or products are allowed; there is no restriction to reactions of a particular order.

Choose distinct input species \(X_1,\ldots,X_k\), with \(\Sigma=\{X_1,\ldots,X_k\}\), and a fixed initial context \(i\in\mathbb R_{\ge0}^{\Lambda\setminus\Sigma}\). For input \(x\in\mathbb R_{\ge0}^{k}\), the initial concentration is \(c_{X_j}(0)=x_j\) and \(c_S(0)=i_S\) for \(S\notin\Sigma\). The context can contain arbitrary nonnegative real constants. It is fixed as part of the computing network and depends neither on the input nor on the rate constants.

For each assignment \(\kappa\in\mathbb R_{>0}^{R}\), the mass-action trajectory solves
\[
\frac{dc_S}{dt}
=\sum_{r\in R}(b_r(S)-a_r(S))\kappa_r
\prod_{T\in\Lambda}c_T(t)^{a_r(T)}
\qquad(S\in\Lambda).
\]
An exponent-zero factor is one, including at zero concentration. Each \(\kappa_r\) is a finite positive real constant, independent of time, with no common upper or positive lower bound assumed. The polynomial vector field has a unique maximal solution from the initial state. A network used in either robust computation definition must have a nonnegative solution defined for every \(t\ge0\), for every input and every \(\kappa\); finite-time blowup does not qualify. Species other than the output need not converge or remain bounded over infinite time.

For predicate computation choose disjoint voter sets \(\Upsilon_0,\Upsilon_1\subseteq\Lambda\). The network robustly decides \(\varphi\) when, for every \(x\) and \(\kappa\), writing \(b=\varphi(x)\),
\[
\liminf_{t\to\infty}\sum_{S\in\Upsilon_b}c_S(t)>0,
\qquad
\forall S\in\Upsilon_{1-b},\quad\lim_{t\to\infty}c_S(t)=0.
\]
The positive lower limiting value may depend on \(x,\kappa\). It is the total correct-voter concentration that must stay away from zero; individual correct voters need not converge. For numerical computation choose one output species \(Y\in\Lambda\). The network robustly computes \(f\) when, for every \(x,\kappa\),
\[
\lim_{t\to\infty}c_Y(t)=f(x).
\]
Input and output species are not required to be disjoint. A predicate or function is called robustly decidable or computable if some finite network with the appropriate fixed data has this property. No bound on time, species, reactions or convergence rate is imposed. The network may depend on the entire predicate or function, but not on a particular input or rate assignment.

A threshold predicate has the form
\[
\theta(x)=\mathbf1\!\left\{\sum_{j=1}^k q_jx_j>h\right\},
\qquad q_j\in\mathbb Q,\quad h\in\mathbb R,
\]
where \(\mathbf1\) is one when its condition holds and zero otherwise. A multi-threshold predicate is a finite Boolean expression using such tests, constants, AND, OR and NOT. This defines boundary behavior at equality exactly.

A rational floor-affine function is
\[
g(x)=\max\!\left\{0,b+\sum_{j=1}^k q_jx_j\right\},
\qquad q_j\in\mathbb Q,\quad b\in\mathbb R.
\]
Here “floor” means clipping below zero, not rounding to an integer. A function \(f\) is threshold-piecewise rational floor-affine if there exist an integer \(\ell\ge1\), multi-threshold predicates \(\varphi_1,\ldots,\varphi_\ell\), and functions \(g_1,\ldots,g_\ell\) of the displayed form such that, for every \(x\), exactly one \(\varphi_j(x)\) equals one and \(f(x)=g_j(x)\) for that index. The partition is finite; continuity across its boundaries is not required. Slopes are rational, while thresholds and offsets may be arbitrary real constants.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the joint classification. A positive answer must establish both equivalences for every input dimension, with the exact dynamics and convergence conventions stated here. A negative answer must prove the negation of at least one equivalence, for example by fully verifying a robustly computing network whose predicate or function lies outside the specified class. This is an exact yes/no classification, so the numerical \(1/100\) approximation convention does not replace equality of functions or exact Boolean decisions. A result for a single choice of rate constants, leaderless networks only, discrete molecule counts, or time-varying rate laws does not establish the claimed characterization.''',
 source_formulation=dict(text='The authors conjecture that the classes constructed in their positive results exhaust robust predicate and numerical-function computation. The function class is the one defined in Definition 2.3, despite a shortened name in the conclusion.',
 caption='Paraphrase of the joint tightness conjecture in §4, with terminology expanded from Definitions 2.1–2.7.',citation='primary',format='editorial_paraphrase'),
 importance=dict(score=72,method='editorial',
 reason='An exact classification would identify which analog computations can depend only on reaction stoichiometry and initial concentrations, despite arbitrary kinetic constants.',
 basis='Individual assessment of a broad model-characterization problem, its contrast with stable computation, and the published constructive classes.'),
 why='Chemical implementations often have uncertain reaction speeds. This question isolates what can be computed when every positive choice of fixed kinetic constants must lead to the same answer. A classification would distinguish robust computational content from behavior that depends on carefully selected reaction rates.',
 references=[
 ref('primary','Robust Predicate and Function Computation in Continuous Chemical Reaction Networks',
 'Kim Calabrese; David Doty; Mina Latifi',2025,'https://doi.org/10.4230/LIPIcs.DISC.2025.19',
 'DISC 2025, Article 19, pp. 19:1–19:23; Definitions 2.1–2.7, Theorems 3.7 and 3.10, and the joint conjecture in §4, p. 19:15'),
 ref('preprint','Robust predicate and function computation in continuous chemical reaction networks',
 'Kim Calabrese; David Doty; Mina Latifi',2025,'https://arxiv.org/abs/2506.06590v1',
 'Version 1, 6 June 2025; original preprint and constructive-result summary'),
 ref('reverse','Reverse-Robust Computation with Chemical Reaction Networks',
 'Ravi Kini; David Doty',2026,'https://arxiv.org/abs/2604.14355v1',
 'Version 1, 15 April 2026; abstract and model scope: discrete counts and reversals up to a cutoff'),
 ],
 context_blocks=[
 block('The continuous model represents molecular amounts by nonnegative real concentrations. Reactions give a polynomial differential equation. Different positive kinetic constants change trajectories, but robust computation requires their eventual output to agree for every such choice.'),
 block('Stable chemical computation allows a more powerful adversary controlling reaction progress beyond fixed mass-action laws. The paper shows that stable Boolean decisions can inspect which inputs are zero, but cannot in general distinguish arbitrary positive magnitudes. Fixed-constant mass-action robustness admits more predicates.'),
 block('Theorem 3.7 constructs robust deciders for every finite Boolean combination of rational-weight threshold tests. Initial context permits real threshold offsets. Exact behavior on the threshold itself is part of the predicate, even though the answer is obtained asymptotically.'),
 block('Theorem 3.10 constructs robust computers for the finite threshold-defined partitions and rational floor-affine pieces in the question. The resulting functions may be discontinuous. Their values are concentration limits, rather than integer molecule counts.'),
 block('The conclusion conjectures necessity of both constructed classes. It separately discusses removing initial context and representing signed inputs by differences of concentrations. Those alternatives are outside this card’s selected source conjecture.'),
 block('The 2026 reverse-robust result allows discrete reactions to run backward until a cutoff and then only forward. Its semilinear classification concerns that different execution model and does not establish the continuous mass-action classification here.','reverse'),
 ],
 progress=[
 progress('2025-06-06','The original preprint gives constructive robust computation results for threshold predicates and piecewise affine numerical outputs.','preprint'),
 progress('2025','The published paper states exact definitions, proves the sufficient directions in Theorems 3.7 and 3.10, and conjectures their necessity in §4.'),
 progress('2026-04-15','A new preprint studies reverse robustness for discrete CRNs; its model does not resolve the mass-action classification.','reverse'),
 progress('2026-09-16','Individual review recovers the complete joint conjecture and distinguishes all initial-context, rate and output conventions.'),
 ],
),notes,sources,status,summary=[
 'A continuous chemical reaction network computes through the evolution of nonnegative species concentrations.',
 'Robust computation requires the same limiting answer for every assignment of positive reaction-rate constants fixed over time.',
 'The conjecture characterizes robust predicates by finite Boolean combinations of rational-weight threshold tests.',
 'It simultaneously characterizes numerical outputs by finite threshold-defined partitions with rational affine pieces clipped at zero.',
 'The constructive directions are known, while necessity remains unresolved in the sources checked.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
