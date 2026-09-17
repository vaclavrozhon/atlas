"""Complete the strict-budget metric k-means approximation constant."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7354';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the full approximation-infimum target and the explicit candidate-center model with every client eligible as a center.',
 'Specified a genuine rational metric, squared objective, all-input expected-cost guarantee and exact center budget on every execution.',
 'Expanded polynomial bit-complexity quantifiers, zero-optimum behavior and the distinction between infimum and attainment.',
 'Checked the 2026 rounding and spectral results through their final strict-budget statements, not only their intermediate expected-budget guarantees.',
 'Kept the July ratio as progress rather than automatically converting it into a binary benchmark barrier.',
 'Preserved importance 88 and category and required unconditional Lean-checked absolute accuracy 1/100.',
]
sources=[
 'Read Anand–Charikar–Cohen-Addad–Gao–Grandoni–Lee–Sharma–van Wijland, arXiv:2607.14654v1, 16 July 2026: Introduction, Theorem 1.2, the D subset F convention, Theorems 1.3–1.4 and Appendix A p. 127. The final metric guarantee is 4.9+epsilon with at most k centers, distinct from the extra-center intermediate result; exactly k can be obtained by adding unused permitted centers. The live history still lists v1. This is a statement/scope review, not an independent full proof or bit-implementation audit.',
 'Read Byrka–Guo–Hu–Li–Wan–Wang, arXiv:2604.06046v1, 7 April 2026: abstract, Introduction, Theorem 1.1 and Corollary 1.3 p. 3. The initial LMP result opens k centers only in expectation, while the later conversion gives a true (5+epsilon)-approximation. The distinction is essential because the card requires feasibility on every execution. The live history lists only v1.',
 'Read the primary abstract of Charikar–Cohen-Addad–Gao–Grandoni–Lee–van Wijland, An Improved Greedy Approximation for (Metric) k-Means, arXiv:2605.29165, posted 27 May 2026; the author-hosted publisher copy identifies FOCS 2025 publication. It records the earlier 3+2*sqrt(2)+epsilon ratio. The later repository posting date is not a later improvement over the April result.',
 'Checked primary later-work searches through 17 September 2026. Results on Euclidean geometry, fixed-parameter running time, fairness, weak distance-comparison oracles and faster implementations do not determine this unrestricted metric ratio. No matching unconditional lower bound for the defined randomized algorithm class was located.',
]
complete(identifier,dict(
 title='Optimal polynomial-time approximation ratio for metric k-means',criterion='tightness',question_type='numerical_value',
 formal=r'''Determine, to absolute error at most \(1/100\), the constant
\[
 \rho_{\mathrm{MetKM}}=
 \inf\left\{r\in[1,\infty):\begin{array}{l}
 \text{some uniform randomized polynomial-time algorithm }A\text{ always returns}\\
 \text{a feasible solution and satisfies }
 \mathbb E[\operatorname{cost}_I(A(I))]\le r\operatorname{OPT}(I)\\
 \text{for every valid explicitly encoded metric instance }I
 \end{array}\right\}.
\]
The metric, squared cost, candidate-center constraint and worst-case polynomial bit-time model are defined below.''',
 definitions=r'''An instance contains a nonempty finite labelled set \(U\), its full rational distance matrix \(d:U\times U\to\mathbb Q_{\ge0}\), nonempty subsets \(D,F\subseteq U\) with \(D\subseteq F\), and an integer \(1\le k\le|F|\). The distance function satisfies \(d(x,y)=0\) exactly when \(x=y\), symmetry, and \(d(x,z)\le d(x,y)+d(y,z)\) for all triples. Thus it is a genuine metric, not merely a squared-distance table or an arbitrary cost matrix. The sets are explicitly listed; each rational distance has a binary integer numerator and positive binary denominator. All matrix entries, labels and headers count toward the input bit length \(L\).

The elements of \(D\) are distinct unweighted clients, each counted once; the elements of \(F\) are the allowed center locations. The inclusion \(D\subseteq F\) is part of this card's model, so every client is itself eligible to be a center. Points of \(U\) outside these sets carry no demand and cannot be selected unless they belong to \(F\). A feasible solution is a set \(S\subseteq F\) of exactly \(k\) distinct centers. Its cost and optimum are
\[
 \operatorname{cost}_I(S)=\sum_{x\in D}\min_{s\in S}d(x,s)^2,
 \qquad
 \operatorname{OPT}(I)=\min_{\substack{S\subseteq F\\ |S|=k}}
 \operatorname{cost}_I(S).
\]
The minimum exists because the feasible family is finite and nonempty. Squared distances need not themselves satisfy a triangle inequality. An output lists the center labels, not a fractional solution or a distribution over center sets. Selecting fewer centers can be padded with unused eligible locations without increasing cost, but opening more than \(k\) centers is never feasible.

The metric is unrestricted and fully supplied. No Euclidean embedding, bounded dimension, geometric coordinates, shortest-path oracle or input distribution is assumed. The parameter \(k\) is part of the input and has no fixed upper bound. There are no fairness constraints, capacities, client weights, outliers or facility-opening charges.

An admissible algorithm is one finite classical multitape Turing program with independent fair random bits, no advice and no external oracle. It has constants \(K>0\) and integer \(b\ge1\) such that, on every valid input and every random tape, it halts within \(K(L+1)^b\) steps and returns a feasible set. Reading, rational arithmetic, random-bit generation, auxiliary computation and output are all charged. Expected polynomial time or unit-cost arithmetic on arbitrary reals is not this model.

A fixed real \(r\ge1\) is achievable when some admissible algorithm satisfies the displayed expected-cost bound for every fixed input. The program and polynomial constants may depend on \(r\), but not on the input, its center count or its coordinate bit lengths. Expectation is over internal randomness. Zero optimum requires zero expected cost, hence zero cost almost surely; no cost ratio with a zero denominator is used. Known constant-factor algorithms make the set of achievable ratios nonempty. The infimum need not be attained by one algorithm. The definition is unconditional and assumes no unproved complexity hypothesis.''',
 answer_criterion=r'''Supply a real number \(a\) and a complete Lean-checked proof that
\[
 |a-\rho_{\mathrm{MetKM}}|\le\frac1{100}.
\]
A proved containing interval \([\ell,u]\) of width at most \(1/50\) qualifies through its midpoint. A finite mathematical expression is acceptable; a decimal expansion is not required. Merely restating the defining infimum is insufficient.

The result must concern all admissible algorithms on the full metric input class with \(D\subseteq F\). A guarantee opening \(k\) centers only in expectation, a larger center budget, one algorithm's ratio, a relaxation gap, or a geometric or fixed-parameter special case does not determine this constant. Conditional hardness must retain its assumption and is not an unconditional lower bound. The \(1/100\) tolerance concerns the supplied value, not feasibility or distance preservation.''',
 source_formulation=dict(text='Metric k-means minimizes squared distances to a fixed number of centers from an explicitly given candidate set. Recent primary work improves approximation ratios; this card asks for the infimum across all uniform randomized polynomial-time algorithms, with the source-compatible convention that clients are eligible centers.',caption='Editorial optimum-ratio target based on Spectral Dual Fitting for k-Means, Introduction and Theorem 1.2, with its D subset F convention retained.',citation='primary',format='editorial_paraphrase'),
 why='Determine the computational approximation limit of squared-distance clustering in general finite metrics. This isolates the cost of clustering without geometric assumptions while requiring an exact center budget on every execution.',
 references=[
 ref('primary','Spectral Dual Fitting for k-Means','Aditya Anand; Moses Charikar; Vincent Cohen-Addad; Ruiquan Gao; Fabrizio Grandoni; Euiwoong Lee; Amatya Sharma; Ernest van Wijland',2026,'https://arxiv.org/abs/2607.14654v1','16 July 2026; Introduction, Theorem 1.2, D subset F convention and Appendix A p. 127'),
 ref('rounding','k-Clustering via Iterative Randomized Rounding','Jarosław Byrka; Yuhao Guo; Yang Hu; Shi Li; Chengzhang Wan; Zaixuan Wang',2026,'https://arxiv.org/abs/2604.06046v1','7 April 2026; abstract, Theorem 1.1 and Corollary 1.3 p. 3, conversion from an expected center budget'),
 ],
 context_blocks=[
 block('The objective squares the underlying metric distances. This is different from k-median, whose objective uses the unsquared distances, and from a continuous Euclidean model with freely chosen center coordinates.'),
 block('A solution using too many centers may have artificially low cost. The exact budget must hold on every execution; an expected count of k centers is not enough.','rounding'),
 block('The April 2026 iterative-rounding paper explicitly converts an intermediate expected-budget result into a true approximation and reports ratios approaching five.','rounding'),
 block('The July 2026 spectral paper reports ratios approaching 4.9. Its final theorem respects the center budget even though parts of the construction temporarily use additional centers.'),
 block('A best-known algorithmic ratio is an upper-bound contribution to the approximation landscape. Determining this infimum to a narrow interval also requires an appropriate lower bound for the full randomized class, without silently assuming a hardness conjecture.'),
 ],
 progress=[progress('2026-04-07','Iterative randomized rounding gives a true approximation with ratio 5 + epsilon after converting the intermediate expected-budget guarantee.','rounding'),progress('2026-07-16','Spectral dual fitting reports the improved metric ratio 4.9 + epsilon.')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified determination within 1/100 of the unconditional expected polynomial-time approximation infimum. The April and July papers improve algorithmic guarantees without a matching unconditional lower bound. This review checked model and final feasibility scope, not complete proofs or every bit-level implementation detail.',summary=[
 'Metric k-means chooses exactly k distinct centers from an explicit candidate set that includes every client.',
 'Its objective is the sum of squared metric distances to the nearest selected center.',
 'The target is the infimum of expected ratios achievable by uniform randomized polynomial-time algorithms.',
 'The July 2026 result reports an improved algorithmic ratio approaching 4.9 without determining the infimum.',
 'Acceptance requires a complete unconditional Lean-checked approximation to that constant within 0.01.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
