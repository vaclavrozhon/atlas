"""Individual review of the approved exact-bit-model cut-cone approximation."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6880'
claim=read_claims(ROOT)[identifier]
refs=[
 ref('primary','Expander Graphs and Their Applications','Shlomo Hoory; Nathan Linial; Avi Wigderson',2006,
 'https://www.math.ias.edu/avi/node/974',
 'May 2006 draft, §13.4.2, printed pp. 112–113; Open Problem 13.11 and the distinct negative-type Conjecture 13.12'),
 ref('draft','Expander Graphs and Their Applications — draft PDF','Shlomo Hoory; Nathan Linial; Avi Wigderson',2006,
 'https://www.math.ias.edu/~avi/BOOKS/expanderbookr1.pdf',
 'Draft dated 3 May 2006; §13.4.2, especially Open Problem 13.11 on printed p. 113'),
 ref('rounding','Optimal Rounding for Sparsest Cut','Alan Chang; Assaf Naor; Kevin Ren',2025,
 'https://web.math.princeton.edu/~naor/homepage%20files/local-growth-STOC.pdf',
 'STOC 2025, pp. 643–652; Theorem 1 and discussion of the negative-type relaxation; DOI 10.1145/3717823.3718285'),
]
notes=[
 'Fixed the original constant-distortion outer-cone target, separating it from the already refuted negative-type candidate.',
 'Defined cut vectors, their cone, semimetrics, the absolute distortion constant and all dimensional quantifiers.',
 'Applied the user’s exact membership and strong separation convention for rational input, with one uniform polynomial-bit-time algorithm.',
 'Specified rational separator output, strict separation and all real points of the cone; no weak tolerance or real-RAM model is substituted.',
 'Did not require an embedding algorithm, a short explicit inequality list or a fixed prescribed relaxation.',
 'Individually assessed the previously unassessed importance and added the complete Lean acceptance criterion.',
]
sources=[
 'Read Hoory–Linial–Wigderson’s May 2006 draft §13.4.2, printed pp. 112–113: cut cone, optimization motivation, membership hardness, Open Problem 13.11 and distinct Conjecture 13.12.',
 'The draft itself records the refutation of the negative-type candidate. This does not refute the quantified search for another efficient cone.',
 'Read Chang–Naor–Ren STOC 2025 Theorem 1 and introductory definitions: the Goemans–Linial relaxation for general capacities and demands has gap Theta(sqrt(log n)); the new contribution is the matching upper bound, not a newly proved lower bound.',
 'Checked current primary-source search results through 16 September 2026. The search found no constant-distortion cone with the approved exact rational membership/separation guarantees, nor a general impossibility theorem.',
]
status=('The source poses an efficiently separable cone approximation and separately proposes negative-type metrics. '
 'That particular proposal is already refuted in the source. '
 'The STOC 2025 theorem sharpens the performance of the Goemans–Linial relaxation to a growing square-root-logarithmic factor; it does not rule out every other cone. '
 'The user selected exact rational membership and separation in polynomial bit time on 16 September 2026. '
 'No resolution of this general target was found in the bounded review.')
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Do there exist an absolute constant \(C\ge1\), a family of closed convex cones
\[
K_n\subseteq\mathbb R^{\binom n2}\qquad(n\ge2),
\]
and one uniform deterministic algorithm for exact membership and strong separation, as defined below, satisfying both
\[
\mathrm{CUT}_n\subseteq K_n\subseteq\mathrm{MET}_n
\]
and
\[
\forall d\in K_n\quad\exists\rho\in\mathrm{CUT}_n
\quad\forall\,1\le i<j\le n,\qquad
d_{ij}\le\rho_{ij}\le C\,d_{ij}?
\]
The constant \(C\) is independent of \(n\) and \(d\). The membership/separation algorithm must run in polynomial bit time for every rational query point, with a single polynomial bound independent of \(n\).''',
 definitions=r'''Write \(V_n=\{1,\ldots,n\}\). Coordinates of a vector \(d\in\mathbb R^{\binom n2}\) are indexed by unordered pairs \(\{i,j\}\). Extend it by \(d_{ji}=d_{ij}\) and \(d_{ii}=0\). The semimetric cone is
\[
\mathrm{MET}_n=\{d:d_{ij}\ge0,\quad d_{ij}\le d_{ik}+d_{kj}
\text{ for all }i,j,k\in V_n\}.
\]
Distinct vertices may have zero distance. This convention includes the zero vector and degenerate cut metrics.

For every nonempty proper subset \(S\subset V_n\), let \((\delta_S)_{ij}=1\) when exactly one of \(i,j\) belongs to \(S\), and zero otherwise. The cut cone is
\[
\mathrm{CUT}_n=
\left\{\sum_{\varnothing\ne S\subsetneq V_n}\lambda_S\delta_S:
\lambda_S\in\mathbb R_{\ge0}\right\}.
\]
The sum is finite. Equivalently these are the pairwise distances of finite configurations in a real \(\ell_1\) space: \(\rho_{ij}=\|v_i-v_j\|_1=\sum_t |(v_i)_t-(v_j)_t|\), with no fixed restriction on the finite dimension.

A closed convex cone contains zero, is closed under nonnegative linear combinations, and is closed in the Euclidean topology. The coordinatewise inequalities in the question define multiplicative distortion after choosing an overall scale for the \(\ell_1\) distances. They also require \(\rho_{ij}=0\) whenever \(d_{ij}=0\). No algorithm for producing \(\rho\) or its cut coefficients is required.

The algorithm receives \(n\) and every coordinate of \(d\in\mathbb Q^{\binom n2}\), each represented by a signed integer numerator and a positive integer denominator in binary. Let \(L\) be the total bit length, including the parameter and delimiters in a fixed unambiguous encoding. The query may be outside \(\mathrm{MET}_n\). In at most \(B(L+1)^k\) Turing-machine steps, for constants \(B>0\) and integer \(k\ge1\), the algorithm must do exactly one of the following:

- If \(d\in K_n\), output the membership verdict IN.
- If \(d\notin K_n\), output a rational vector \(a\) such that \(\langle a,d\rangle<0\) and \(\langle a,z\rangle\ge0\) for every real \(z\in K_n\).

Here \(\langle a,z\rangle=\sum_{i<j}a_{ij}z_{ij}\). The output coordinates use the same binary rational convention, and writing them is included in the running time. The latter output is an exact separating hyperplane through the origin, appropriate for a cone. There is no precision parameter or permitted indeterminate boundary answer. The algorithm is uniform over \(n\), receives no advice and has no extra oracle. The cones need not have polynomially many defining inequalities or a prescribed semidefinite representation.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the displayed existence assertion. A positive answer must define the cones and the single algorithm, prove exact membership/separation and its bit-time bound, and prove the uniform distortion bound for all real semimetrics in every cone. A negative answer must rule out every family and algorithm meeting those conditions; disproving one candidate cone, or proving a lower bound for one representation format, is insufficient. This binary constant-factor target has no numerical \(1/100\) tolerance. Weak approximate separation or a distortion factor growing with \(n\) does not meet the requirement.''',
 source_formulation=dict(text='The source asks for a computationally tractable convex cone approximating the cut cone with a constant loss in metric distortion. The user chose exact membership and separation on rational inputs with polynomial bit complexity.',
 caption='Paraphrase of Open Problem 13.11; the computational convention was selected by the user on 16 September 2026.',citation='primary',format='editorial_paraphrase'),
 importance=dict(score=84,method='editorial',reason='A uniformly tractable constant-distortion outer approximation would improve a central geometric relaxation for cut optimization and clarify the algorithmic limits of finite metric embeddings.',basis='Individual review of cut-cone optimization, the general outer-cone target, and the known limitations of the negative-type relaxation.'),
 why='Cut metrics encode graph partitions, and their nonnegative combinations capture finite ℓ₁ distances. The question seeks a tractable convex domain that retains this geometry to constant distortion. It separates a broad algorithmic possibility from the limitations of the best-studied semidefinite candidate.',
 references=refs,
 context_blocks=[
 block('A single cut records which vertex pairs lie on opposite sides of a partition. Adding such cut vectors with nonnegative weights yields the cut cone. This connects geometric distances with linear objectives measuring capacities crossing graph cuts.'),
 block('The source describes cut optimization through convex optimization over a normalized section of this cone. It also records NP-hardness of exact cut-cone membership. This motivates a larger cone whose membership and separation are easier while its distances remain close to cut-cone distances.'),
 block('The whole semimetric cone is a simple outer relaxation, defined by nonnegativity and triangle inequalities. General finite-metric embedding bounds provide a logarithmic distortion scale, rather than the constant scale requested here. The gap is in the guarantee for every dimension.'),
 block('Negative-type semimetrics form the classical candidate relaxation: the square root of the distance admits a Euclidean realization. They contain cut-cone distances. The source already reports that a uniform constant-distortion embedding of every such metric into ℓ₁ is false, so that candidate cannot answer the broader question.'),
 block(r'Chang, Naor and Ren prove that the Goemans–Linial semidefinite relaxation for Sparsest Cut with general capacities and demands has integrality gap \(\Theta(\sqrt{\log n})\). Their 2025 contribution is the matching upper bound; the lower bound comes from prior work. This is sharp for that relaxation and still grows with dimension.','rounding'),
 block('The cone family in this card is unrestricted apart from its convexity, distortion and exact algorithmic guarantees. A limitation on negative-type metrics or on short linear formulations does not exclude other efficiently separable convex sets. Conversely, a fast optimizer without the required membership and separating outputs would not establish the user-selected formulation.'),
 ],
 progress=[
 progress('2006','The survey poses the general efficient cone question and distinguishes it from the already refuted negative-type conjecture.'),
 progress('2025-06-15','The STOC result gives the sharp square-root-logarithmic gap for the Goemans–Linial relaxation, without a constant-distortion replacement cone.','rounding'),
 progress('2026-09-16','The user selects exact rational membership and strong separation in polynomial bit time; individual review fixes the geometry and all quantifiers.'),
 ],
),notes,sources,status,summary=[
 'The cut cone consists of nonnegative sums of the distance vectors defined by graph cuts.',
 'The target is an outer convex cone whose every semimetric lies within one absolute distortion factor of a cut-cone semimetric.',
 'One uniform algorithm must decide exact membership and return exact rational separating hyperplanes in polynomial bit time.',
 'The negative-type candidate is known to fail at constant distortion, and its classical relaxation has a sharp square-root-logarithmic gap.',
 'The question permits other cone families and remains unresolved in the sources checked by this review.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
