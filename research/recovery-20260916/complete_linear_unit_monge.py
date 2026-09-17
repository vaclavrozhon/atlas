"""Complete implicit simple unit-Monge distance multiplication."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7372';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the exact linear-time target rather than an exponent infimum or an almost-linear bound.',
 'Made the simple unit-Monge counting convention, min-plus product, boundary entries and permutation input/output explicit.',
 'Specified one deterministic uniform word-RAM program with all preprocessing and output charged and linear working memory.',
 'Checked closure and implicit representation against Tiskin’s definitions and Theorem 3, and the algorithmic statement against Theorem 5.',
 'Updated the core-sparse progress to the July 2025 revised theorem and distinguished constant MPC rounds from linear sequential work.',
 'Preserved importance 84, algebraic-computation placement and the complete Lean-checked binary answer criterion.',
]
sources=[
 'Read Tiskin, Fast Distance Multiplication of Unit-Monge Matrices, full primary Springer HTML, Algorithmica 71, 859–888 (2015), online 19 September 2013: abstract, Introduction, definitions of distribution, density and simple unit-Monge matrices, Theorem 3 (closure) and Theorem 5 (implicit multiplication). The source explicitly attributes the linear-time question to Landau and establishes O(n log n) time. The all-suffix/all-prefix counting convention on this card translates its half-integer permutation indices into ordinary zero-based arrays.',
 'Read Gawrychowski–Gorbachev–Kociumaka, arXiv:2408.04613v2, revised 7 July 2025: abstract, Introduction and Theorems 1.1–1.2. The deterministic bound is O(p+q+r+(delta(A)+delta(B))*log(1+delta(A)+delta(B))) on condensed input. For simple unit-Monge matrices the cores are permutations, so this retains the O(n log n) bound. Checked the ESA 2025 primary metadata, Article 74, published 1 October 2025. The live arXiv history still lists v2 as latest.',
 'Read the primary abstract of Koo, arXiv:2404.13486v1, 20 April 2024, SPAA 2024 DOI 10.1145/3626183.3659974: its O(1) bound counts fully scalable MPC rounds. That result is not a claim of O(n) deterministic sequential RAM instructions. No full parallel-to-sequential implementation audit was performed.',
 'Bounded primary-source searches through 17 September 2026 located no verified linear-time sequential algorithm or unconditional superlinear lower bound for this precise permutation-input problem. The review checks statements and representation scope, not complete proofs of all cited papers.',
]
complete(identifier,dict(
 title='Linear-time unit-Monge distance multiplication',criterion='resources',question_type='yes_no',
 formal=r'''Do there exist absolute constants \(K,C>0\), an integer \(B\ge8\), and one uniform deterministic word-RAM algorithm which, for every integer \(n\ge2\) and all permutations \(\pi,\tau\) of \(\{0,\ldots,n-1\}\), outputs a permutation \(\rho\) of that set in at most \(Kn\) instructions using at most \(Cn\) working words, such that
\[
 A_\rho(i,j)=\min_{0\le h\le n}
 \bigl(A_\pi(i,h)+A_\tau(h,j)\bigr)
 \qquad(0\le i,j\le n),
\]
where
\[
 A_\nu(i,j)=|\{t\in\{i,\ldots,n-1\}:\nu(t)<j\}|?
\]
The input and output are permutation arrays, not explicitly written dense matrices. The word length is \(B\lceil\log_2(n+2)\rceil\).''',
 definitions=r'''A permutation array contains exactly once each of the integers from zero to \(n-1\). Each input array has \(n\) entries, with one entry per word, and the output consists of the \(n\) entries of \(\rho\). The input size parameter is this permutation length. No data structure answering arbitrary matrix-entry queries is supplied for free.

The displayed formula defines an \((n+1)\)-by-\((n+1)\) integer matrix from a permutation \(\nu\). For each row boundary \(i\) and column boundary \(j\), it counts the permutation points strictly below that column boundary and at or after that row boundary. In particular,
\[
 A_\nu(i,0)=A_\nu(n,j)=0,
 \quad A_\nu(0,j)=j,
 \quad A_\nu(i,n)=n-i.
\]
All entries lie between zero and \(n\). Its discrete density satisfies
\[
 A_\nu(i+1,j)+A_\nu(i,j+1)-A_\nu(i,j)-A_\nu(i+1,j+1)
 =\mathbf 1_{\{\nu(i)=j\}}
 \qquad(0\le i,j<n).
\]
This fixes the orientation of the simple unit-Monge representation without relying on an unstated convention. Here the indicator is one if its condition holds and zero otherwise.

For equally sized matrices, their distance product, or min-plus product, has entry \((i,j)\) equal to the minimum over \(h\) of the sum of entry \((i,h)\) in the first and entry \((h,j)\) in the second. It is neither ordinary matrix multiplication nor composition of the two input permutations. The class of matrices defined above is closed under this product, so a suitable output permutation exists; its density determines it uniquely. The task is to compute that permutation, not to prove closure alone or output the quadratic array of product entries.

The RAM is sequential and executes a fixed finite program independent of \(n,\pi,\tau\). Allowed unit-cost instructions are word reads and writes, copying, comparison, branching, Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and integer quotient and remainder with a nonzero divisor. Shifts by at least \(w\) return zero. Stored values and addresses fit in words; multiword operations pay for their constituent instructions. There is no randomness, advice, external oracle, uncharged preprocessing or free size-dependent lookup table. All initialization, intermediate representations, arithmetic, input access and output writes are included in the \(Kn\) bound. Working memory includes registers and temporary tables but excludes the supplied input arrays and the output array. Including those arrays changes the space bound only by a constant factor.

The constants and word-size factor are chosen once for the algorithm. Every valid input must satisfy the same worst-case time and space bounds. Expected time, amortization over a batch of products and constant-round massively parallel computation are different requirements.''',
 answer_criterion=r'''Give a complete mathematically correct proof checked in Lean of the stated existence proposition or its logical negation. A positive result must specify the uniform algorithm and prove exact correctness of all product entries through the output permutation, as well as the linear worst-case resource bounds in the stated model.

An \(O(n\log n)\), \(n^{1+o(1)}\), or other superlinear algorithm does not meet the target. Neither approximate multiplication, a restricted family of permutations, a dense-input model nor a parallel round bound suffices. An assumed conjecture can justify a conditional lower bound only; it cannot serve as an unconditional refutation. There is no additive numerical tolerance on this exact existence question.''',
 source_formulation=dict(text='Tiskin asks whether implicit distance multiplication of simple unit-Monge matrices can be performed in linear time, attributing the question to Landau. The input and output density matrices are permutations. The explicit counting convention here states that implicit problem with zero-based array indices.',caption='Tiskin, Introduction, Theorem 3 and Theorem 5; permutation representation and linear-time question.',citation='primary',format='editorial_paraphrase'),
 why='This compact matrix operation combines many sequence-comparison values and is reused in alignment, subsequence and compressed-string algorithms. Removing its logarithmic overhead would improve an underlying primitive while matching the linear size of its representation.',
 references=[
 ref('primary','Fast Distance Multiplication of Unit-Monge Matrices','Alexander Tiskin',2015,'https://doi.org/10.1007/s00453-013-9830-z','Algorithmica 71:859–888; online 19 September 2013; Introduction, distribution/density definitions and Theorems 3 and 5'),
 ref('core','Core-Sparse Monge Matrix Multiplication: Improved Algorithm and Applications','Paweł Gawrychowski; Egor Gorbachev; Tomasz Kociumaka',2025,'https://arxiv.org/abs/2408.04613v2','7 July 2025 revision; Introduction and Theorems 1.1–1.2; ESA 2025 Article 74'),
 ref('parallel','An Optimal MPC Algorithm for Subunit-Monge Matrix Multiplication, with Applications to LIS','Jaehyun Koo',2024,'https://arxiv.org/abs/2404.13486v1','20 April 2024; primary abstract, constant-round MPC guarantee; SPAA DOI 10.1145/3626183.3659974'),
 ],
 context_blocks=[
 block('Dense matrices have quadratic output size, but a simple unit-Monge matrix is represented by one permutation. The implicit representation makes a genuinely linear-time multiplication question meaningful.'),
 block('The simple boundary convention and permutation density are part of the problem. General Monge matrices have different representation costs and need not admit a permutation-sized description.'),
 block('Tiskin proves closure under distance multiplication and an O(n log n)-time algorithm. His source explicitly identifies the remaining linear-time question.'),
 block('The 2025 core-sparse algorithm broadens the matrix class and refines its complexity in terms of the number of nonzero density entries. In the permutation case it matches the earlier logarithmic overhead.','core'),
 block('The separate constant-round MPC result measures distributed rounds. Such a bound does not establish that the same product can be computed using only linearly many sequential instructions.','parallel'),
 ],
 progress=[progress('2015','The journal treatment establishes exact implicit multiplication in O(n log n) time and records the linear-time question.'),progress('2024-04-20','A constant-round massively parallel multiplication algorithm is reported in a different computational model.','parallel'),progress('2025-07-07','The revised core-sparse theorem generalizes multiplication while retaining O(n log n) time for permutation-density matrices.','core')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified resolution of the exact linear-time deterministic sequential target. The latest checked core-sparse theorem retains the logarithmic factor for this special case, and the MPC theorem concerns round complexity. The review verifies statement and representation scope without independently certifying full cited proofs.',summary=[
 'Two permutations implicitly encode simple unit-Monge counting matrices.',
 'Their exact min-plus product is again encoded by a unique permutation.',
 'The question asks for one deterministic algorithm taking only linear worst-case time and space.',
 'The checked sequential algorithms retain a logarithmic factor, while constant-round parallel results use a different model.',
 'A complete Lean-checked answer must prove or refute the linear-time proposition for every pair of input permutations.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
