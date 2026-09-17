"""Complete the universal metric subtour-LP gap to the benchmark's numeric precision."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6589';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the numerical universal integrality-gap target and its absolute 1/100 Lean acceptance criterion, rather than replacing it by exact equality to four thirds.',
 'Wrote the full symmetric metric domain, Hamiltonian-tour optimum and subtour LP with all constraints and quantifiers explicitly.',
 'Distinguished the all-size supremum from a maximum attained by some finite instance, an algorithm’s ratio, and a restricted half-integral or support-size gap.',
 'Verified the LP denominator in the 2024 improvement and checked the September 2026 finite enumeration and newer universal-saving claim without treating either as a resolution.',
 'Preserved importance 95 and required certified upper and lower control of the unrestricted supremum; removed algorithmic construction details from the context.',
]
sources=[
 'Read Jin–Klein–Williamson, arXiv:2607.01536v2 of 3 July 2026, §1 pp. 1–2 including displayed subtour LP (1), and §1.1 Definition 1.1 and Theorem 1.2 p. 3. The ten-sevenths result concerns the maximum-entropy algorithm on half-integral cycle-cut instances, whose class gap is already at most four thirds.',
 'Read Karlin–Klein–Oveis Gharan, arXiv:2105.10043v3 of 11 April 2022, primary abstract: the expected-cost theorem is explicitly relative to the subtour LP, not merely the integral tour optimum.',
 'Read Gurvits–Klein–Leake, arXiv:2311.09072v2 of 9 May 2024, §4.2 Lemma 4.5 and Corollary 4.6 p. 10, and Appendix A.4 p. 26. The displayed guarantee is relative to c(x) for a feasible subtour vector; its recorded saving is 2.18*10^{-34}. The full inherited probability and payment proofs were not independently certified.',
 'Read Cook–Hougardy–Petrich, arXiv:2603.12995v5, submitted 8 September 2026 (PDF header 9 September): abstract and §§1–3, with general enumeration through n=16 and half-integral enumeration through n=18. Metadata has no later revision as checked on 17 September. The enumeration was not rerun.',
 'Read Song, Preprints.org 202609.0140/v1, posted 2 September 2026, abstract and Theorem 1 in the full HTML: claimed LP-relative saving greater than 2.05522*10^{-30}. The proof and numerical certificate were not audited. This tiny saving would not supply the 1/100 approximation even if confirmed.',
 f'Bounded searches through {DATE} also returned a September restricted-support n+8 claim; its indexed scope is still restricted and was not promoted to a general theorem. No verified all-metric determination within 1/100 was found.',
]
complete(identifier,dict(
 criterion='tightness',question_type='numerical_value',
 formal=r'''Determine, to absolute accuracy \(1/100\), the universal subtour-LP integrality gap for the symmetric metric traveling-salesperson problem:
\[
 \Gamma=\sup_{n\ge3}\ \sup_{c\in\mathcal M_n}
 \frac{\operatorname{OPT}_{\mathrm{TSP}}(c)}{\operatorname{OPT}_{\mathrm{LP}}(c)}.
\]
Here \(\mathcal M_n\) is the set of all metrics on \(n\) labeled vertices, and the two optima are defined below. The target is this one dimensionless real number over all finite sizes, not the gap for one fixed number of vertices or for a restricted metric family.''',
 definitions=r'''For an integer \(n\ge3\), put \(V=\{1,\ldots,n\}\) and let \(E\) contain one undirected edge \(\{u,v\}\) for each pair of distinct vertices. A metric \(c\in\mathcal M_n\) is a real matrix satisfying
\[
 c_{uu}=0,\qquad c_{uv}=c_{vu}>0\ (u\ne v),\qquad
 c_{uv}\le c_{uw}+c_{wv}\quad(u,v,w\in V).
\]
Costs may be arbitrary real numbers. No Euclidean embedding, graph-metric representation, sparsity or bound on the ratios of positive distances is assumed. Write \(c_{\{u,v\}}=c_{uv}\).

A tour is a Hamiltonian cycle of the complete undirected graph: it visits each vertex once and returns to its start. Its cost is the sum of its \(n\) edge costs. The quantity \(\operatorname{OPT}_{\mathrm{TSP}}(c)\) is the minimum of this cost over all such tours.

For a subset \(S\subseteq V\), let \(\delta(S)\) be the edges with exactly one endpoint in \(S\). For an edge set \(F\subseteq E\) and a real vector \(x\in\mathbb R^E\), write \(x(F)=\sum_{e\in F}x_e\). The fractional optimum is the finite-dimensional linear program
\[
\begin{aligned}
 \operatorname{OPT}_{\mathrm{LP}}(c)=\min\quad &\sum_{e\in E}c_e x_e\\
 \text{subject to}\quad &x(\delta(\{v\}))=2 &&(v\in V),\\
 &x(\delta(S))\ge2 &&(\varnothing\ne S\subsetneq V),\\
 &0\le x_e\le1 &&(e\in E).
\end{aligned}
\]
All cut constraints are included. They enforce connectivity conditions in addition to the degree equations; this is not merely a fractional cycle-cover relaxation. A tour's incidence vector is feasible, so the LP is nonempty. Its feasible region is closed and bounded, hence the optimum exists. Positivity of the metric and the degree equations make both optima positive and the ratio well-defined.

The supremum ranges over every integer \(n\ge3\) and every such metric. It need not be achieved by a single finite instance. Multiplying all distances by the same positive scalar leaves the ratio unchanged. The known general upper bounds make \(\Gamma\) finite.

This is a numerical extremal question, with no running-time requirement on evaluation of a submitted mathematical expression for the answer. It does not ask for a fast tour-finding algorithm or for the worst ratio attained by any particular algorithm. A ratio proved against the integral tour optimum is not automatically a ratio against the possibly smaller LP optimum. Half-integral LP vectors, cycle-cut instances, graph metrics, Euclidean metrics and bounded vertex counts are proper restrictions of the domain unless a separate theorem proves they suffice for this supremum.

The classical four-thirds conjecture proposes \(\Gamma=4/3\). That exact equality would answer this card, but a different certified approximation meeting the stated accuracy also answers it. The benchmark tolerance is absolute error in the ratio itself, not a relative error and not an additive error in tour cost.''',
 answer_criterion=r'''Supply a specified real number \(a\) and a complete Lean-checked proof that
\[
 |a-\Gamma|\le\frac1{100}.
\]
Equivalently, give explicit bounds \(L\le\Gamma\le U\) with \(U-L\le1/50\), proved in Lean, and take their midpoint. An exact value with a complete proof also qualifies. A certified finite expression can specify the answer; a decimal expansion or efficient evaluation algorithm is not required.

The upper control must cover every size and every metric in the domain. The lower control must establish an actual lower bound on the universal supremum; a family of increasingly large examples is allowed, and attainment is not required. An unevaluated restatement of the defining supremum, an unproved numerical estimate, a one-sided improvement, or finite enumeration without a theorem covering the remaining sizes is insufficient. Proving only the behavior of one rounding algorithm or one restricted family is insufficient unless accompanied by a reduction covering the full target. Accuracy within \(1/100\) does not by itself prove the exact four-thirds conjecture.''',
 source_formulation=dict(text='The source describes the four-thirds conjecture for the integrality gap of the symmetric metric subtour relaxation and writes the degree, cut and box constraints explicitly. This card retains the broader numerical task of determining that gap, with the project’s absolute 1/100 acceptance precision.',caption='Paraphrase of Jin–Klein–Williamson, arXiv:2607.01536v2, §1 pp. 1–2 and LP (1); numerical acceptance convention retained from the card and project rules.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary',r'Maximum Entropy is a \(10/7\)-Approximation Algorithm for the TSP on Half-Integral Cycle Cut Instances','Billy Jin; Nathan Klein; David P. Williamson',2026,'https://arxiv.org/abs/2607.01536v2','First posted 1 July, revised 3 July 2026; §1 pp. 1–2, LP (1); §1.1 Definition 1.1 and Theorem 1.2 p. 3'),
 ref('kko','A (Slightly) Improved Bound on the Integrality Gap of the Subtour LP for TSP','Anna R. Karlin; Nathan Klein; Shayan Oveis Gharan',2022,'https://arxiv.org/abs/2105.10043v3','Version 3, 11 April 2022; primary abstract explicitly states expected tour cost relative to the subtour-LP optimum'),
 ref('gkl','From Trees to Polynomials and Back Again: New Capacity Bounds with Applications to TSP','Leonid Gurvits; Nathan Klein; Jonathan Leake',2024,'https://arxiv.org/abs/2311.09072v2','Version 2, 9 May 2024; §4.2 Lemma 4.5 and Corollary 4.6 p. 10; Appendix A.4 p. 26, LP-relative guarantee'),
 ref('enumeration','Extending Exact Integrality Gap Computations for the Metric TSP','William Cook; Stefan Hougardy; Moritz Petrich',2026,'https://arxiv.org/abs/2603.12995v5','Version 5, submitted 8 September 2026; PDF header 9 September; §§1–3, general instances through n=16 and half-integral extreme points through n=18; enumeration not rerun'),
 ref('song','A Sharper Explicit Bound on the Subtour-LP Integrality Gap for Metric TSP','Zhao Song',2026,'https://www.preprints.org/manuscript/202609.0140/v1','Version 1, posted 2 September 2026; abstract and Theorem 1 checked in full HTML; proof and numerical certificate not independently audited'),
 ],
 context_blocks=[
 block(r'The classical general bounds put the gap between \(4/3\) and \(3/2\). The conjecture proposes the lower endpoint. The numerical benchmark still requires substantially tighter two-sided control than that interval.'),
 block(r'The 2022 improvement is explicitly LP-relative, so it bounds the integrality gap as well as an algorithmic approximation ratio. The distinction matters because the integral optimum and the LP optimum are different denominators.','kko'),
 block(r'The 2024 analysis records the universal bound \(\Gamma\le3/2-2.18\cdot10^{-34}\). This is progress below the historical threshold but does not determine the gap within \(1/100\).','gkl'),
 block(r'The July 2026 \(10/7\) theorem analyzes a particular algorithm on half-integral cycle-cut instances. That restricted class already has gap at most \(4/3\), so the new algorithmic theorem neither worsens that class gap nor determines the unrestricted gap.'),
 block(r'The September 2026 enumeration covers all metric instances through \(n=16\) and half-integral extreme points through \(n=18\). It supplies finite-size evidence; no reduction from all larger sizes is claimed here.','enumeration'),
 block(r'A September preprint claims a larger universal saving above \(2.05522\cdot10^{-30}\) below \(3/2\). Its theorem statement was checked, but its proof and certificate were not audited. Even the claimed improvement remains far short of the numerical precision required here.','song'),
 ],
 progress=[progress('2022','The general LP-relative guarantee improves strictly below three halves.','kko'),progress('2024','An improved explicit universal saving is established in the cited analysis.','gkl'),progress('2026-07-03','The revised source studies an algorithm on the restricted half-integral cycle-cut class.'),progress('2026-09-02','A preprint claims a larger, still very small, universal saving; not independently proof-audited.','song'),progress('2026-09-08','The revised computational study extends general finite-size coverage to sixteen vertices.','enumeration')],
),notes,sources,'The latest checked September 2026 primary sources still present the four-thirds gap as unresolved. The verified scopes of special-class results and finite enumeration do not yield a universal numerical determination within 1/100. The new explicit-saving preprint is recorded as an unaudited claim, and even its stated bound would not meet this card’s precision. Bounded checks through 17 September 2026 found no verified resolution.',summary=[
 'The metric traveling-salesperson problem asks for a cheapest tour through all vertices.',
 'Its subtour linear program permits fractional edges while retaining degree and connectivity constraints.',
 'The target is the supremum of the tour optimum divided by the LP optimum over every finite symmetric metric.',
 'The four-thirds conjecture proposes an exact value, but this benchmark accepts absolute error at most 1/100.',
 'A complete Lean-checked answer must control the unrestricted supremum from both sides, without assuming it is attained or restricting the number of vertices.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
