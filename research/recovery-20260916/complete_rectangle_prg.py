"""Individual review of optimal generators for combinatorial rectangles."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1124'
claim=read_claims(ROOT)[identifier]
refs=[
 ref('primary','Theory of Unconditional Pseudorandom Generators','Pooya Hatami; William M. Hoza',2023,
 'https://eccc.weizmann.ac.il/report/2023/019/revision/2/',
 'Revision 2, 14 April 2023; Definition 1.4.1 and §1.4.1; Definition 3.1.6, Corollary 3.1.8 and Open Problem 3.1.9, printed p. 47'),
 ref('rectangles','Concentration for Limited Independence via Inequalities for the Elementary Symmetric Polynomials','Parikshit Gopalan; Amir Yehudayoff',2020,
 'https://theoryofcomputing.org/articles/v016a017/',
 'Theory of Computing 16(17), 1–29; §1.3, Definition 1.8 and Theorem 1.9, pp. 6–7; source notation uses alphabet size m and dimension n'),
 ref('minwise','Explicit Min-wise Hash Families with Optimal Size','Xue Chen; Shengtang Huang; Xin Li',2025,
 'https://arxiv.org/abs/2510.10431v3',
 'Version 3, 9 November 2025; introduction preceding §1.1 and Theorem 1.1; accepted for SODA 2026'),
]
notes=[
 'Recovered the exact O(n/d + log(1/epsilon) + log log n) seed target with n total output bits and d equal consecutive blocks.',
 'Specified arbitrary subsets of an alphabet of size 2^(n/d), additive probability error and one generator independent of the rectangle.',
 'Used dyadic precision q up to n and explained its equivalence to all source error parameters via rounding and the identity generator.',
 'Required a single polynomial-time algorithm, with one absolute seed constant uniform in dimension, block size and accuracy.',
 'Separated the nearly optimal rectangle result from the newer optimal min-wise hashing result; preserved importance and category.',
]
sources=[
 'Read the April 2023 survey Definition 3.1.6, Corollary 3.1.8 and Open Problem 3.1.9, including n divisible by d, and its uniform explicitness convention.',
 'Read Gopalan–Yehudayoff’s published Definition 1.8 and Theorem 1.9. Translated alphabet m and coordinate count n to alphabet 2^b and dimension d without conflating either with total output length.',
 'Read Chen–Huang–Li arXiv 2510.10431v1 and the updated v3 introduction and result statement; checked revision history and SODA 2026 acceptance. The introduction explicitly distinguishes the unresolved rectangle generator from their min-wise hashing theorem.',
 'A bounded primary-source search through 16 September 2026 found no optimal generator for the full stated rectangle family and error range. Related complete proofs were not independently reconstructed.',
]
status=('The source asks for an absolute-constant optimal seed bound uniformly over block size, dimension and additive error. '
 'Gopalan–Yehudayoff’s published construction retains an additional logarithmic factor. '
 'The November 2025 revision of the SODA 2026 min-wise hashing paper still distinguishes the missing optimal rectangle generator from its hashing result. '
 'No resolution of the full target was found through 16 September 2026 in the bounded review.')
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Do there exist an absolute constant \(C>0\) and a uniform explicit family
\[
G_{n,d,q}:\{0,1\}^{s(n,d,q)}\longrightarrow\{0,1\}^{n}
\]
such that, for every integer \(n\ge1\), every positive divisor \(d\) of \(n\), and every integer \(1\le q\le n\),
\[
s(n,d,q)\le C\left(\frac nd+q+L(n)\right),
\qquad L(n)=1+\left\lceil\log_2\log_2(n+2)\right\rceil,
\]
and every \(d\)-dimensional combinatorial rectangle \(R\) on \(n\) bits satisfies
\[
\left|\Pr_{Y\sim U_{s(n,d,q)}}[G_{n,d,q}(Y)\in R]
-\Pr_{X\sim U_n}[X\in R]\right|\le 2^{-q}?
\]
The constant and the algorithms are independent of all parameters and of \(R\). This is the source’s seed target \(O(n/d+\log(1/\varepsilon)+\log\log n)\), with dyadic error \(\varepsilon=2^{-q}\).''',
 definitions=r'''Put \(b=n/d\). Split an \(n\)-bit string into its \(d\) consecutive, disjoint blocks \(x^{(1)},\ldots,x^{(d)}\), each with exactly \(b\) bits. A combinatorial rectangle is a product
\[
R=A_1\times\cdots\times A_d,\qquad A_i\subseteq\{0,1\}^{b}.
\]
Every subset \(A_i\), including the empty and full sets, is allowed. Membership in \(R\) means that every block lies in its corresponding set. Equivalently its Boolean indicator is \(\prod_{i=1}^d f_i(x^{(i)})\), where \(f_i\) is any Boolean function of \(b\) bits. No succinctness or computational restriction is imposed on these functions. Under uniform input the membership probability is \(\prod_i |A_i|/2^b\).

\(U_r\) denotes the uniform distribution on all \(r\)-bit strings, with the usual singleton convention for \(r=0\). A seed supplies exactly \(s(n,d,q)\) independent fair bits. The displayed error is additive, including for rectangles of very small or zero uniform measure.

Uniform explicitness requires fixed deterministic Turing machines \(S,G\), a constant \(B>0\), and an integer \(k\ge1\). On parameters \((1^n,d,q)\), with the latter two integers in binary, \(S\) computes \(s(n,d,q)\); on these parameters and a seed \(y\), \(G\) computes \(G_{n,d,q}(y)\). Both take at most \(Bn^k\) bit operations on valid inputs. Neither receives the sets \(A_i\), nonuniform advice or an oracle.

The dyadic convention loses no part of the source’s error range. For \(0<\varepsilon\le1/2\), take \(q=\lceil\log_2(1/\varepsilon)\rceil\). If \(q\le n\), the displayed error is at most \(\varepsilon\), with only a constant additive change in the seed expression. If \(q>n\), the identity generator on \(n\) seed bits has zero error and meets the required bound because \(n<q\). For larger errors use \(q=1\). The nonnegative function \(L\) only regularizes the small-\(n\) logarithms. The dimension may grow with \(n\); no parameter is treated as a fixed hidden constant.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the existence assertion. A positive answer must provide the uniform algorithms and establish their running time, the seed bound with one absolute constant, and the additive error for every allowed rectangle and parameter triple. A negative answer must refute this unrestricted construction target. A nearly optimal bound with an unbounded extra logarithmic factor does not suffice. Neither a hitting set nor a generator restricted to one fixed dimension or to special coordinate subsets meets the full assertion. This binary asymptotic target has no numerical \(1/100\) tolerance.''',
 source_formulation=dict(text=r'The source asks for an explicit generator fooling products of arbitrary tests on \(d\) equal blocks, with seed bounded by a constant times \(n/d+\log(1/\varepsilon)+\log\log n\).',
 caption='Paraphrase of Open Problem 3.1.9, using the block convention in Definition 3.1.6.',citation='primary',format='editorial_paraphrase'),
 why='Combinatorial rectangles express simultaneous constraints on separate blocks and occur in pseudorandomness, hashing and communication. The question asks for the full dependence on alphabet size, dimension and error, so removing an extra factor would improve a reusable construction across several parameter regimes.',
 references=refs,
 context_blocks=[
 block('The word rectangle denotes a Cartesian product of finite sets, not a geometric region with real coordinates. The tests on separate blocks are arbitrary. The generator must coordinate the blocks so that every such product has almost its uniform probability.'),
 block(r'The alphabet has \(2^{n/d}\) possible values per coordinate. Thus \(n/d\) is its logarithm, while \(d\) is the number of coordinates. Confusing alphabet size, dimension and total bit length changes the seed target substantially.'),
 block(r'For two blocks the source records seed \(n/2+O(\log(1/\varepsilon))\). The open problem asks for one guarantee valid in arbitrarily high dimension, with only a doubly logarithmic contribution from total length in addition to block size and error.'),
 block(r'Gopalan and Yehudayoff’s Theorem 1.9 gives seed \(O((\log\log d+\log(M/\varepsilon))\log\log(M/\varepsilon))\) for alphabet size \(M\) and \(d\) coordinates, with logarithms regularized at small parameters. Taking \(M=2^b\) and \(\varepsilon=2^{-q}\) leaves an extra factor of order \(\log(b+q+2)\) beyond the requested additive scale.','rectangles'),
 block('Min-wise hashing asks that each element of a selected set have approximately the right probability of receiving the smallest hash value. It is related to rectangles but is a different family of probability tests, with a relative-error requirement. The newer optimal-size hashing construction explicitly discusses the absence of an optimal general rectangle generator in the small-error regime. Its title does not settle this card.','minwise'),
 block('The guarantee is stronger than merely outputting some point in every sufficiently large rectangle. It controls the frequency of membership among all uniformly chosen seeds. Conversely, the card does not require relative accuracy for exponentially rare rectangles; its error is the specified additive quantity.'),
 ],
 progress=[
 progress('2020','The published rectangle construction approaches the additive seed scale but retains a logarithmic factor.','rectangles'),
 progress('2023-04-14','The survey states the uniform optimal seed target as Open Problem 3.1.9.'),
 progress('2025-11-09','The revised min-wise hashing paper, accepted for SODA 2026, separates its optimal hashing result from the missing optimal rectangle PRG.','minwise'),
 progress('2026-09-16','Individual review recovers all parameters, the explicitness convention and the precise additive-error guarantee; no resolution was found.'),
 ],
),notes,sources,status,summary=[
 'A combinatorial rectangle requires each of several disjoint input blocks to belong to an arbitrary chosen subset.',
 'The generator must preserve every rectangle’s probability to a prescribed additive error.',
 'The requested seed is proportional to block length plus logarithmic inverse error plus doubly logarithmic total length.',
 'The same polynomial-time algorithm and absolute seed constant must work in every dimension and accuracy regime.',
 'Checked near-optimal rectangle generators and recent optimal min-wise hashing results do not establish the full target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
