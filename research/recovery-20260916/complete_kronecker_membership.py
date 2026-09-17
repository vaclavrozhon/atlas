"""Review exact Kronecker-polytope membership with growing dimension and binary partitions."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0047';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Exact Kronecker-polytope membership in polynomial time',
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a deterministic polynomial-bit-time algorithm which, given three partitions \(\lambda,\mu,\nu\) of the same positive integer \(k\), each as a list of \(n\) nonnegative binary integers, decides whether
\[
\left(\frac{\lambda}{k},\frac{\mu}{k},\frac{\nu}{k}\right)\in\Delta_n,
\]
where \(\Delta_n\) is the Kronecker polytope defined below? The dimension \(n\) is part of the input, and membership is exact, including points on the boundary.''',
 definitions=r'''A partition in this representation is a list \(\lambda_1\ge\cdots\ge\lambda_n\ge0\) of integers with \(\sum_i\lambda_i=k\). Trailing zeros are allowed. The lists \(\mu\) and \(\nu\) obey the same conditions and have the same sum. Division by \(k\) is coordinatewise. All entries and list lengths use binary encoding with fixed length delimiters; the complete lists are given explicitly. Let \(L\) be the total input bit length. In particular the number of parts grows with the input, while \(k\) may be exponentially large relative to its bit length.

Here is a self-contained spectral definition of \(\Delta_n\). For an array \(z=(z_{abc})_{a,b,c=1}^n\in\mathbb C^{n\times n\times n}\) satisfying \(\sum_{a,b,c}|z_{abc}|^2=1\), form three \(n\times n\) matrices
\[
R^{(1)}_{aa'}=\sum_{b,c}z_{abc}\overline{z_{a'bc}},\quad
R^{(2)}_{bb'}=\sum_{a,c}z_{abc}\overline{z_{ab'c}},\quad
R^{(3)}_{cc'}=\sum_{a,b}z_{abc}\overline{z_{abc'}}.
\]
The bar denotes complex conjugation. These matrices are Hermitian positive semidefinite and have trace 1. Write \(\operatorname{spec}_{\downarrow}(R)\) for the length-\(n\) list of real eigenvalues, with multiplicity, in nonincreasing order. Define
\[
\Delta_n=\left\{
\bigl(\operatorname{spec}_{\downarrow}(R^{(1)}),
\operatorname{spec}_{\downarrow}(R^{(2)}),
\operatorname{spec}_{\downarrow}(R^{(3)})\bigr):
z\in\mathbb C^{n\times n\times n},\ \sum_{a,b,c}|z_{abc}|^2=1
\right\}.
\]
This is the usual rational convex Kronecker polytope. The spectral definition is equivalent to the representation-theoretic definition in the source and specifies the question without requiring a representation-theory oracle. The tensor \(z\) is existentially quantified in the definition; it is not part of the input, need not have rational coordinates and need not be output by the algorithm.

The target algorithm is one deterministic multi-tape Turing machine \(A\) with constants \(K>0\), \(d\in\mathbb N\), which halts on every valid input within \(K(L+1)^d\) steps and returns the exact membership bit. There is no advice, randomness, supplied list of facets, or oracle. All integer and rational arithmetic has its actual bit cost. No positive distance from the boundary is promised and no additive tolerance is allowed. A different precomputed algorithm for each fixed \(n\) is insufficient.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof that this exact membership language is in deterministic polynomial time, or a proof that it is not. A positive answer must establish the full variable-dimension bit bound and exact correctness on boundary points. An approximate tensor-scaling result polynomial in inverse error, a nondeterministic certificate bound, or a fixed-dimension polytope computation does not suffice.',
 why='Kronecker polytopes connect representation-theoretic multiplicities with possible spectra of quantum subsystems. Exact efficient membership would go beyond known certificate bounds and numerical scaling methods while avoiding the harder task of evaluating individual multiplicities.',
 source_formulation=dict(text='Bürgisser asks for polynomial-time membership when the three partitions have a varying number of binary-encoded parts. The source already records membership in NP and coNP.',caption='Dagstuhl Seminar 15242, §5.7, printed pp.45–46 (combined issue PDF pp.47–48).',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Complexity of Symbolic and Numerical Problems: Complexity of testing membership to Kronecker polytopes','Peter Bürgisser',2015,'https://doi.org/10.4230/DagRep.5.6.28','Seminar 15242, §5.7, printed pp.45–46; combined issue PDF pp.47–48'),
 ref('certificates','Membership in moment polytopes is in NP and coNP','Peter Bürgisser; Matthias Christandl; Ketan D. Mulmuley; Michael Walter',2017,'https://arxiv.org/abs/1511.03675','Revision v2, 24 June 2017; Theorem 1 and stretched-coefficient interpretation p.2; fixed-dimension observation p.4; §2.3 equations (4)–(5) pp.6–7; journal DOI 10.1137/15M1048859'),
 ref('recent','Computing moment polytopes — with a focus on tensors, entanglement and matrix multiplication','Maxim van den Berg; Matthias Christandl; Vladimir Lysikov; Harold Nieuwboer; Michael Walter; Jeroen Zuiddam',2025,'https://arxiv.org/abs/2510.08336','9 October 2025; §2.5 and Proposition 2.13 pp.16–17; §6.2, Theorems 6.2–6.3 p.48'),
 ],
 context_blocks=[
 block('The original question varies the number of parts. Fixing the dimension would permit precomputation of a single polytope and would miss the requested uniform complexity.'),
 block('The certificate theorem gives polynomially verifiable evidence for both membership and nonmembership. It does not supply a deterministic polynomial-time search for those certificates.','certificates'),
 block('Membership corresponds to positivity after some common positive integer stretching of the three partitions. Positivity of the single unstretched Kronecker coefficient is a different problem.','certificates'),
 block('The spectral model identifies the polytope with triples of reduced-state eigenvalue lists of a pure tripartite state. This gives an exact analytic formulation of the same input question.','certificates'),
 block('The 2025 treatment records tensor-scaling time polynomial in inverse tolerance and a separation bound involving the partition denominator and dimension-dependent facet sizes. Combining them does not yield a polynomial bound in the binary input length.','recent'),
 ],
 progress=[progress('2015','The Dagstuhl question asks for a polynomial-time algorithm beyond NP and coNP certificates.'),progress('2017','The revised certificate paper proves the NP and coNP upper bounds and the spectral membership formulation.','certificates'),progress('2025-10-09','The later computational treatment gives explicit polytope methods and explains scaling precision needed for exact certification.','recent')],
),[
 'Retained exact deterministic membership, growing partition length and binary parts; supplied a self-contained spectral definition of the Kronecker polytope.',
 'Included boundary points, arbitrary complex existential tensors and no tensor/facet oracle in the input.',
 'Separated stretched support from one coefficient, certificate complexity from algorithms, and inverse-precision scaling from polynomial bit time.',
 'Preserved the individual importance assessment and required a complete Lean-checked complexity answer.',
],[
 'Read Dagstuhl Seminar 15242 §5.7, including varying n and binary lists. Read arXiv:1511.03675v2 Theorem 1, the stretched-coefficient equivalence, fixed-dimension observation, and §2.3 spectral definition.',
 'Read the 9 October 2025 moment-polytope manuscript §2.5 Proposition 2.13 and §6.2 Theorems 6.2–6.3. The quoted scaling dependence is polynomial in inverse tolerance, not in its bit length.',
 'Checked current arXiv records and bounded primary-source searches through 17 September 2026; no exact variable-dimension deterministic polynomial-bit-time resolution was located.',
], 'Source-open for exact Kronecker-polytope membership with a varying number of binary parts. NP and coNP certificates are known; the inspected tensor-scaling and explicit-polytope results do not establish this deterministic polynomial-bit-time target. Bounded status review through 17 September 2026.',summary=[
 'The input consists of three integer partitions of the same size, written as binary lists whose length may grow.',
 'The task is to decide exact membership of their normalized triple in the Kronecker polytope.',
 'Equivalently, the three lists must occur as spectra of the reduced matrices of some unit complex three-dimensional array.',
 'The desired algorithm is deterministic and polynomial in the full bit length, including arbitrarily close boundary cases.',
 'A complete Lean-checked complexity proof must go beyond known certificates and algorithms whose time depends polynomially on inverse approximation error.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
