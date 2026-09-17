"""Review fully explicit Valiant rigidity over polynomial-degree number fields."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-5260';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a deterministic polynomial-time construction of matrices \(A_n\in\mathbb C^{n\times n}\), for integers \(n\ge4\), whose entries lie in a common number field of degree polynomial in \(n\), together with a constant \(0<\varepsilon<1\) such that
\[
\forall c>0\ \exists N_c\ge4\ \forall n\ge N_c:
R_{A_n}^{\mathbb C}\!\left(
\min\!\left\{n,\left\lfloor\frac{cn}{\log_2\log_2 n}\right\rfloor\right\}
\right)\ge n^{1+\varepsilon}?
\]
The same construction and \(\varepsilon\) must work for every fixed real \(c>0\). Rigidity is measured against all low-rank complex replacement matrices. Polynomial-time construction and the common field are specified by the exact representation below.''',
 definitions=r'''For \(A\in\mathbb C^{n\times n}\) and an integer \(0\le r\le n\), ordinary complex rigidity is
\[
R_A^{\mathbb C}(r)=
\min\left\{
\bigl|\{(i,j):A_{ij}\ne B_{ij}\}\bigr|:
B\in\mathbb C^{n\times n},\ \operatorname{rank}_{\mathbb C}(B)\le r
\right\}.
\]
Rank means dimension of the column span over \(\mathbb C\). The cost counts changed positions over the whole matrix. Modified entries may be arbitrary complex numbers, even outside the field containing the original matrix. There is no row-wise budget, norm constraint or restriction on numerical magnitude. The zero matrix is admissible, so the minimum is a well-defined integer between 0 and \(n^2\).

The construction consists of one deterministic multi-tape Turing machine \(M\) and constants \(K>0\), \(b\in\mathbb N\). On input \(1^n\), the machine halts within \(Kn^b\) steps and prints a nonconstant polynomial \(P_n(t)\in\mathbb Z[t]\), irreducible over \(\mathbb Q\), and all \(n^2\) rational polynomials \(q_{n,i,j}(t)\) with
\[
1\le m_n:=\deg P_n\le Kn^b,
\qquad \deg q_{n,i,j}<m_n.
\]
Zero coordinate polynomials are allowed. The defining polynomial and all coordinate polynomials are output as dense coefficient lists. Integers use signed binary encoding; rational coefficients are reduced fractions with positive binary denominators. The running time includes writing every bit. No advice, randomness or oracle is available.

For any complex root \(\alpha_n\) of \(P_n\), let
\[
A_n(\alpha_n)_{ij}=q_{n,i,j}(\alpha_n),
\qquad K_n=\mathbb Q(\alpha_n).
\]
The rigidity requirement is imposed for every choice of such a root. Thus no root-selection oracle or approximate numerical embedding is hidden in the construction. Irreducibility gives \([K_n:\mathbb Q]=m_n\). All matrix entries lie in this same field, so their jointly generated field also has degree at most \(m_n\). Bounding the degree of each entry separately would not bound the degree of their joint field and is insufficient here. This exact dense presentation also rules out descriptions that conceal exponentially many bits in one large integer or in a primitive element's defining polynomial.

The machine is not required to compute rigidity or output a rigidity certificate. The algebraic numbers are specified exactly by the displayed polynomial data. The requirement for every root makes the representation independent of an embedding; conjugate embeddings also preserve rank and changed-position counts via field automorphisms of \(\mathbb C\).

All logarithms in the rank threshold have base 2. For \(n\ge4\), the iterated logarithm is positive; the minimum with \(n\) only handles initial dimensions before a fixed \(c\)'s eventual threshold. The integer \(N_c\) may depend on \(c\), whereas \(M,K,b,\varepsilon\) may not. The same matrix family must satisfy every fixed constant multiple of this rank scale. No fixed numerical lower bound on \(\varepsilon\) is prescribed. The use of number fields is a restriction on exact coefficient descriptions, not a restriction on the low-rank competitors.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the construction's existence or of its logical negation. A positive answer must verify the deterministic bit-time bound, irreducibility and degree of each defining polynomial, the exact coordinate representations, and the rigidity inequality for all complex low-rank replacements and every root of the defining polynomial. Random existence, an unselected list of candidates, exponentially large common field degree, or a rank bound only over the coefficient field is insufficient. A negative answer must rule out every construction meeting the stated requirements, rather than only showing nonrigidity of Fourier or other familiar matrices.''',
 why='Rigidity offers a route to lower bounds for linear computations of logarithmic depth. Allowing algebraic entries in small number fields relaxes the most restrictive coefficient choices while still demanding an efficient exact construction; known generic large-field constructions do not answer that challenge.',
 importance=dict(score=84,method='editorial',reason='A central explicit rigidity target that retains computationally manageable algebraic coefficients while relaxing the binary or rational entry restriction; closely tied to linear-circuit lower-bound methods.'),
 source_formulation=dict(text='Dvir and Liu state that constructing a Valiant-rigid matrix remains open even when entries may lie in a number field of polynomial dimension. Their preceding definition uses rigidity at rank O(n/log log n). This card supplies an exact polynomial-time common-field representation and quantifies the rank-scale constants.',caption='Fourier and Circulant Matrices Are Not Rigid, CCC 2019, Introduction, printed p.17:2 and footnote 1; §1.2 p.17:3 distinguishes ordinary and regular rigidity.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Fourier and Circulant Matrices Are Not Rigid','Zeev Dvir; Allen Liu',2019,'https://doi.org/10.4230/LIPIcs.CCC.2019.17','Introduction p.17:2, Valiant-rigidity definition and footnote 1; §1.2 p.17:3, complex field and ordinary versus regular rigidity'),
 ref('numberfields','Complexity Lower Bounds using Linear Algebra','Satyanarayana V. Lokam',2009,'https://www.cs.toronto.edu/~toni/Courses/CommComplexity/Papers/lokam-book.pdf','Foundations and Trends volume 4 (2008), copyright 2009; §8 “Rigid matrices over small number fields”, printed p.141/PDF p.144; this older passage asks the stronger linear-rank target'),
 ref('recent','Arithmetic circuit lower bounds from sumset expansion','Anand Kumar Narayanan',2026,'https://arxiv.org/abs/2607.15848','17 July 2026; §1.5 symbolic rigid matrices and conditional Theorem 4, printed p.6; §1.6 semi-explicit tensors and Theorem 5, printed p.7'),
 ],
 context_blocks=[
 block('The source singles out the common number-field degree as a meaningful relaxation of the coefficient problem. A collection of entries can each have low algebraic degree while together generating a much larger extension.'),
 block('Older algebraic constructions obtain strong rigidity from entries generating very large number fields. Lokam’s survey explicitly points out that exponential joint field degree leaves the small-number-field target unanswered. Its own displayed rank target is stronger than the near-linear rank scale used here.','numberfields'),
 block('Dvir and Liu prove nonrigidity for broad structured families including Fourier and circulant matrices. The fact that Fourier entries lie in a small cyclotomic field does not make those matrices a solution.'),
 block('The July 2026 sumset paper develops symbolic-matrix methods and a conditional lower-bound consequence from explicit expanding exponent matrices. It does not give the unconditional small-number-field rigid family requested here.','recent'),
 block('The same paper’s semi-explicit tensor constructions reduce certain large field-degree requirements but still use a large cyclotomic extension and concern tensor rank. They are not a polynomial-degree common-field matrix rigidity construction.','recent'),
 ],
 progress=[progress('2009','Lokam’s survey highlights polynomial joint number-field degree as an unresolved coefficient restriction for strong explicit rigidity.','numberfields'),progress('2019','Dvir and Liu retain the small-number-field Valiant-rigidity question and disprove several prominent structured candidates.'),progress('2026-07-17','The sumset-expansion preprint gives symbolic constructions and conditional connections, while its algebraic-number tensor construction has a different target and field-degree regime.','recent')],
),[
 'Defined rigidity over C against arbitrary complex changes, while restricting only the original entries to a polynomial-degree number field.',
 'Specified one polynomial-time Turing algorithm outputting a dense irreducible common-field polynomial and dense rational coordinates for all entries.',
 'Distinguished the joint field degree from the degree of each entry, and bounded coefficient description lengths through actual bit-time output.',
 'Used the announced recommended every-fixed-constant interpretation of the rank scale; the optional clarification had not been answered and is not recorded as user confirmation.',
 'Read the original footnote and the older number-field motivation, and checked that the July 2026 symbolic/tensor results do not provide this construction.',
 'Individually assessed importance and required complete Lean-checked representation, explicitness and rigidity proofs or the exact negation.',
],[
 'Read Dvir–Liu CCC 2019, Introduction p.17:2 including the O(n/log log n) Valiant-rigidity discussion and footnote 1 on polynomial number-field dimension. Read §1.2 p.17:3: the paper works over C and distinguishes ordinary from regular rigidity. This card uses ordinary rigidity with unrestricted complex perturbations.',
 'Read Lokam, Complexity Lower Bounds using Linear Algebra, §8 printed p.141/PDF p.144, “Rigid matrices over small number fields”. It explicitly requires the jointly generated field Q(a_ij) to have polynomial dimension and contrasts this with exponential-dimensional constructions. Its linear-rank epsilon*n target is not silently substituted for the CCC source’s n/log log n scale.',
 'Read Narayanan arXiv:2607.15848v1, 17 July 2026, §1.5 and conditional Theorem 4 printed p.6. The statement needs an explicit expanding exponent matrix and obtains a symbolic linear-transformation-related circuit bound, not the concrete number-field matrix family here. Read §1.6 and Theorem 5 p.7: the semi-explicit tensor theorem uses a cyclotomic field with a prime lower bound growing exponentially in the tensor-coordinate parameter, and does not establish polynomial common-field degree or the matrix rigidity target.',
 'Bounded primary-source checks through 17 September 2026 found no solution of the chosen fully explicit small-number-field target. The polynomial-time dense representation and quantifier choices are editorial precisifications of the imported source question.',
], 'Source-open for an unconditional polynomial-time exact construction of complex Valiant-rigid matrices in a common number field of polynomial degree. Rigidity is measured against arbitrary complex replacements. The original source footnote and the older joint-field-degree discussion are preserved; the July 2026 symbolic and semi-explicit tensor results do not resolve this target. Bounded status review through 17 September 2026.',summary=[
 'The target is a deterministic polynomial-time construction of rigid complex square matrices with algebraic entries.',
 'All entries must lie in one common number field of polynomial degree, supplied by an exact polynomial-size representation.',
 'Reducing rank to any fixed multiple of n divided by log log n must require at least n^(1+epsilon) changed entries for one fixed positive epsilon.',
 'The low-rank replacement may use arbitrary complex values, so its coefficients are not confined to the original number field.',
 'The answer must include complete Lean-checked construction, representation and rigidity proofs or prove the exact negation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
