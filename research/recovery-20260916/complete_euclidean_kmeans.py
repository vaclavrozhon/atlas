"""Complete the unrestricted Euclidean k-means approximation constant."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7353';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved determination of the full unrestricted approximation constant rather than turning the newest upper bound into an arbitrary barrier.',
 'Specified rational input and output, squared Euclidean cost, unrestricted dimension and cluster count, repeated points and exact center budget.',
 'Expanded the common polynomial bit-time, all-random-tapes feasibility and expected-cost quantifiers, including zero optimum.',
 'Kept the achievable-ratio infimum distinct from attainment and from a ratio analysis of one algorithm or relaxation.',
 'Checked the July 2026 continuous-center result, its strict-budget conclusion, and later parameterized and fair-clustering work.',
 'Preserved importance 91 and category and the unconditional Lean-checked absolute 1/100 acceptance target.',
]
sources=[
 'Read Anand–Charikar–Cohen-Addad–Gao–Grandoni–Lee–Sharma–van Wijland, arXiv:2607.14654v1, 16 July 2026: Introduction pp. 1–2, Theorems 1.1–1.5, and Appendix A p. 127. The Euclidean model permits arbitrary center locations, and Theorem 1.1 states (3+ln 2+epsilon)-approximation. Appendix A combines intermediate extra-center and stable-instance results to return a feasible strict-budget solution. Only v1 is listed as of the review date. This was a statement and scope review, not an independent audit of the long proof or its bit-level implementation.',
 'Read the author-hosted STOC 2026 paper Charikar–Cohen-Addad–Gao–Grandoni–Lee–van Wijland, A (4+epsilon)-Approximation for Euclidean k-Means via Non-Monotone Dual-Fitting, DOI 10.1145/3798129.3800894: Introduction and Theorems 1–3, including the distinction between intermediate extra centers and the final randomized strict-budget algorithm. Its introduction treats fixed-k and fixed-dimension schemes separately.',
 'Read the official SoCG 2026 Article 33 abstract of Cohen-Addad–Karthik–Saulpic–Schwiegelshohn, Near-Optimal Bounds for Parameterized Euclidean k-Means, published 27 May 2026. It concerns parameter-dependent running times and a conditional lower bound under the new XXH assumption, not determination of the unconditional unrestricted ratio.',
 'Read the primary arXiv abstract and history of Cheng–Mo–Song–Ding, arXiv:2609.07974v1, 7 September 2026, A Sub-4 Approximation for Fair k-Means. Its guarantee concerns fairness constraints, fractional solutions, conditional use of a supplied approximation subroutine and rounding with additive fairness violation. It does not determine the present strict unconstrained optimum ratio. No full proof audit of that preprint was performed.',
 'Did not copy numerical hardness ratios from the July introduction: the distinction between continuous and candidate-center Euclidean models matters, and a conditional hardness result in any event is not an unconditional lower bound for the randomized infimum defined here.',
 f'Bounded primary-source searches through {DATE} found improvements and related variants but no verified determination within 1/100 of this unconditional constant.',
]
complete(identifier,dict(
 title='Optimal polynomial-time approximation ratio for Euclidean k-means',criterion='tightness',question_type='numerical_value',
 formal=r'''Determine the real constant
\[
 \rho_{\mathrm{EucKM}}=
 \inf\left\{r\in[1,\infty):\begin{array}{l}
 \text{there is one uniform randomized polynomial-time algorithm }A\\
 \text{such that }\mathbb E[\operatorname{cost}_I(A(I))]
 \le r\operatorname{OPT}(I)\text{ for every valid instance }I
 \end{array}\right\}
\]
to absolute error at most \(1/100\), using the explicit rational-input, arbitrary-center and worst-case polynomial bit-time model below. Neither the number of clusters nor the dimension is fixed.''',
 definitions=r'''An instance \(I\) consists of integers \(n,d\ge1\), \(1\le k\le n\), and an explicitly listed sequence of points \(x_1,\ldots,x_n\in\mathbb Q^d\). Repeated points are allowed and contribute separately to the objective. Every integer is in binary, and each rational coordinate is represented by an integer numerator and a positive integer denominator in binary, with explicit delimiters. The full lengths of all \(nd\) coordinates and headers count toward the input length \(L\).

A feasible output is a list \(C=(c_1,\ldots,c_k)\in(\mathbb Q^d)^k\) of exactly \(k\) centers. Centers may be repeated and may lie anywhere in the space; they need not be input points or belong to a supplied candidate set. Its cost is
\[
 \operatorname{cost}_I(C)=
 \sum_{i=1}^n\min_{1\le j\le k}\|x_i-c_j\|_2^2,
 \qquad
 \|v\|_2^2=\sum_{t=1}^d v_t^2.
\]
Every point is assigned to a nearest center for purposes of this minimum; ties have no effect. There are no outliers, fairness constraints, capacities or permission to exceed the center budget. Returning fewer distinct centers can be represented by repeating entries in the length-\(k\) list.

The quantity \(\operatorname{OPT}(I)\) is the minimum of the same expression over \((\mathbb R^d)^k\). This minimum exists and has a rational attaining center list: for any nonempty cluster its mean is optimal, and only finitely many assignments of the \(n\) points to \(k\) labels need be considered. Empty clusters may use arbitrary repeated rational centers. Thus the rational-output convention does not increase the exact optimum.

An admissible algorithm is one finite classical multitape Turing program with independent fair random bits, no advice and no external oracle. There must be constants \(K>0\) and an integer \(b\ge1\) such that, for every valid input and every random tape, it halts within \(K(L+1)^b\) steps and outputs a feasible rational center list. All computation, random-bit generation and output bits are charged; exact real arithmetic is not a unit-cost primitive. The expectation in the formula is over the algorithm's own coins on each fixed input. It is a bound on expected cost, not merely a success probability or an expected running-time guarantee.

A ratio \(r\ge1\) is achievable precisely when some such algorithm satisfies the displayed inequality on every instance. Its algorithm and polynomial constants may depend on this fixed \(r\), but cannot depend on the input, \(k\), \(d\) or coordinate precision. If \(\operatorname{OPT}(I)=0\), the inequality requires zero cost almost surely; no division by zero defines the guarantee. Known constant-factor algorithms make the set of achievable ratios nonempty, and it is bounded below by one. The infimum need not itself be achieved by a single algorithm. No computational complexity hypothesis is included in this definition.''',
 answer_criterion=r'''Supply a real number \(a\) and a complete Lean-checked proof that
\[
 |a-\rho_{\mathrm{EucKM}}|\le\frac1{100}.
\]
A proved interval \([\ell,u]\) containing the defined constant with \(u-\ell\le1/50\) qualifies by taking its midpoint. A finite mathematical expression is allowed; a decimal expansion is not required. Merely renaming the defining infimum is not a determination.

The proof must concern the unrestricted randomized polynomial bit-time class above. An upper bound alone, a lower bound for one relaxation or method, a result for fixed dimension or fixed cluster count, or a solution using more than \(k\) centers does not determine the constant. A lower bound conditional on an unproved complexity assumption settles only that conditional statement. The benchmark tolerance applies to the supplied value, not to feasibility or to the meaning of the approximation ratio.''',
 source_formulation=dict(text='Recent work improves polynomial-time approximation algorithms for high-dimensional Euclidean k-means, whose centers may be arbitrary points. The card asks for the best achievable approximation ratio across all uniform randomized polynomial-time algorithms, not the ratio of a particular method.',caption='Editorial optimization target based on the unrestricted Euclidean model and approximation landscape in the STOC 2026 paper and the July 2026 spectral dual-fitting preprint.',citation='primary',format='editorial_paraphrase'),
 why='Locate the computational approximation limit of a central clustering objective when neither dimension nor cluster count is a fixed parameter. This separates what any efficient algorithm can achieve from the performance of the current best technique.',
 references=[
 ref('primary','Spectral Dual Fitting for k-Means','Aditya Anand; Moses Charikar; Vincent Cohen-Addad; Ruiquan Gao; Fabrizio Grandoni; Euiwoong Lee; Amatya Sharma; Ernest van Wijland',2026,'https://arxiv.org/abs/2607.14654v1','16 July 2026; Introduction pp. 1–2, Theorem 1.1 and Appendix A p. 127; arbitrary Euclidean centers and final strict budget'),
 ref('stoc','A (4 + epsilon)-Approximation for Euclidean k-Means via Non-Monotone Dual-Fitting','Moses Charikar; Vincent Cohen-Addad; Ruiquan Gao; Fabrizio Grandoni; Euiwoong Lee; Ernest van Wijland',2026,'https://people.idsia.ch/~grandoni/Pubblicazioni/CCGGLW26stoc.pdf','STOC 2026, DOI 10.1145/3798129.3800894; Introduction and Theorems 1–3'),
 ref('parameterized','Near-Optimal Bounds for Parameterized Euclidean k-Means','Vincent Cohen-Addad; Karthik C. S.; David Saulpic; Chris Schwiegelshohn',2026,'https://doi.org/10.4230/LIPIcs.SoCG.2026.33','Published 27 May 2026; primary abstract, parameterized scope and XXH-dependent lower bounds'),
 ],
 context_blocks=[
 block('Euclidean k-means minimizes the sum of squared distances. This differs both from k-median, which uses unsquared distances, and from a general finite metric problem with a supplied list of possible centers.'),
 block('Polynomial-time approximation schemes with a fixed dimension or fixed number of clusters do not give a scheme whose time is polynomial uniformly in both parameters.','parameterized'),
 block('The STOC 2026 result gives randomized ratios approaching four. Its final algorithm respects the center budget, although an intermediate result permits extra centers.','stoc'),
 block(r'The July 2026 preprint states a \((3+\ln 2+\varepsilon)\)-approximation for every fixed \(\varepsilon>0\). This improves algorithmic guarantees but does not prove a matching lower bound for all algorithms.'),
 block('Determining the infimum requires control from both sides in the stated bit model. A conditional hardness theorem has to retain its assumption; it cannot silently become an unconditional lower bound on this constant.','stoc'),
 ],
 progress=[progress('2026-05-27','The SoCG result studies parameter-dependent approximation time and lower bounds under a separate hypothesis.','parameterized'),progress('2026-06','The STOC randomized algorithm gives approximation ratios approaching four.','stoc'),progress('2026-07-16','The spectral dual-fitting preprint reports ratios approaching 3 + ln 2 for unrestricted Euclidean centers.')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified determination of the unconditional expected polynomial-time approximation constant within 1/100. The July preprint improves the stated algorithmic ratio; parameterized and fair-clustering results have different guarantees. This review checked statements, model distinctions and final budget scope, not complete proofs or every bit-level implementation detail.',summary=[
 'Euclidean k-means chooses k arbitrary centers to minimize the sum of squared distances from the input points.',
 'The dimension, number of clusters and rational coordinate lengths are all part of the input.',
 'The target is the infimum of expected ratios achievable by uniform randomized polynomial-time algorithms.',
 'The latest reviewed upper-bound improvement does not determine that unrestricted infimum.',
 'An accepted answer needs a complete Lean-checked value within 0.01, without silently assuming an unproved hardness hypothesis.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
