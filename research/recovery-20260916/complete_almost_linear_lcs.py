"""Complete the growing-alphabet almost-linear constant-factor LCS target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7371';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved one randomized almost-linear algorithm and one absolute approximation factor on explicit growing-alphabet strings.',
 'Specified total input length, empty-string and zero-optimum cases, valid output on every execution and the per-input success probability.',
 'Expanded the uniform word-RAM and all-executions time quantifiers; removed an unrelated copied static-index-space clause.',
 'Distinguished subsequences of both inputs from substring variants and a constant factor from a subpolynomial approximation factor.',
 'Checked the 2021 manuscript and the 2025 and 2026 primary results without treating their different guarantees as this endpoint.',
 'Preserved importance 91 and category, and required a complete Lean proof of the precise proposition or its negation.',
]
sources=[
 'Read Golan–Kraus–Porat–Shalom, CPM 2026 Article 27, Introduction, the paragraph on approximation versions of LCS and LCStr, and the LCSS results. Their near-linear high-accuracy LCSS result uses a subsequence of one string and a substring of the other, not a subsequence of both. The introduction describes the remaining growing-alphabet LCS approximation gap.',
 'Read Boneh–Golan–Kraus, arXiv:2507.22486v1, 30 July 2025, abstract, Introduction and Theorem 1 p. 3. The deterministic near-linear-time guarantee is a factor n^(3/4) log n, not an absolute constant. The discussion distinguishes fixed and growing alphabets. Only v1 was listed in the submission history on the review date.',
 'Read Mao–Rubinstein, arXiv:2603.29702v1, submitted 31 March 2026, abstract and Introduction pp. 1–2; also checked the STOC 2026 publication DOI 10.1145/3798129.3800789. The randomized (1-epsilon) LCS scheme has time n^2 / 2^(log^(Omega(1)) n). This guarantee is not an almost-linear bound. No full proof audit is claimed.',
 'Read the primary abstract and version history of Nosatzki, arXiv:2112.08454v1, 15 December 2021, still the only listed version on the review date. The manuscript states a linear-time randomized n^o(1)-factor approximation; the 2026 CPM source identifies it as unpublished. The full proof was not independently checked.',
 f'Bounded primary-source checks through {DATE} did not locate a constant-factor algorithm with the stated one-algorithm almost-linear guarantee on growing alphabets, or an unconditional impossibility proof. Restricted alphabets and substring problems were excluded from that conclusion.',
]
complete(identifier,dict(
 title='Almost-linear constant-factor approximation of LCS',criterion='resources',question_type='yes_no',
 formal=r'''Do there exist absolute real constants \(C\ge1\) and \(K>0\), an integer \(d\ge8\), a function \(h:\{2,3,\ldots\}\to[1,\infty)\) with
\[
 \lim_{n\to\infty}\frac{\log h(n)}{\log n}=0,
\]
and one uniform classical randomized word-RAM algorithm \(A\) such that, for every pair of explicitly given strings \(x,y\) of total length \(n=|x|+|y|\ge2\) over the integer alphabet \(\{0,\ldots,n^2-1\}\), every execution of \(A\) uses at most \(Knh(n)\) instructions, outputs a valid common subsequence \(z\) of \(x,y\), and satisfies
\[
 \Pr\bigl[|z|\ge \operatorname{LCS}(x,y)/C\bigr]\ge\frac23?
\]
The machine has word length \(w=d\lceil\log_2(n+2)\rceil\), and all input, initialization and output costs are charged as specified below.''',
 definitions=r'''A string is a finite sequence of alphabet symbols; the two lengths may differ and either input may be empty. A sequence \(z=(z_1,\ldots,z_\ell)\) is a common subsequence if there are strictly increasing indices \(i_1<\cdots<i_\ell\) in \(x\) and \(j_1<\cdots<j_\ell\) in \(y\) such that \(z_t=x_{i_t}=y_{j_t}\) for every \(t\). The quantity \(\operatorname{LCS}(x,y)\) is the maximum possible integer \(\ell\). Consecutive indices are not required in either input. The empty sequence is always permitted. If the maximum is zero, the output must therefore be empty.

The input consists of the two lengths and two explicit symbol arrays, one symbol per word. The output is an explicit symbol sequence; it is not merely a numerical estimate of the optimum or an implicit description whose expansion is free. A valid common subsequence must be returned on every random execution. Only the lower bound on its length may fail, with probability at most \(1/3\) on each fixed input.

The uniform sequential word RAM is one fixed finite program with no advice, external oracle or free precomputed table. Words are unsigned \(w\)-bit integers. Unit-cost instructions are reads, writes, copies, comparisons, branches, Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and integer quotient and remainder by a nonzero divisor. A shift by at least \(w\) yields zero. Memory addresses and values fit in words; multiword operations pay for their constituent instructions. A random instruction generates an independent uniform word and is charged one step. Every initialization, input access, auxiliary computation, constructed table and output write counts. There is no separate space bound beyond what this machine and its charged running time allow.

The displayed time bound is worst case over both inputs and all random executions, not expected time. Its asymptotic meaning is \(n^{1+o(1)}\): for every real \(\eta>0\), the same algorithm has time at most \(K_\eta n^{1+\eta}\) for all sufficiently large \(n\), with constants \(K_\eta\) and thresholds allowed to depend on \(\eta\). The algorithm, approximation factor \(C\) and word-size constant \(d\) cannot change with \(\eta\), input size, input strings or alphabet size. The function \(h\) is a running-time bound, not an additional input or oracle. Success probability is over the algorithm's internal randomness, with no distributional assumption on the input.''',
 answer_criterion=r'''Give a complete Lean-checked proof that the stated constants, bound and uniform algorithm exist, or a complete Lean-checked proof of the logical negation with the same machine model and quantifiers.

A positive answer must construct an actual common subsequence with the claimed validity, constant ratio, probability and all-executions time guarantee. A factor growing with \(n\) or alphabet size, a numerical estimate alone, or a separate algorithm for each fixed exponent slack does not establish the proposition. A conditional fine-grained lower bound or a deterministic-only obstruction does not establish its unconditional negation. No numerical approximation tolerance applies to this existence question.''',
 source_formulation=dict(text='Recent primary comparisons of general-alphabet LCS approximation leave a gap between fast algorithms with growing approximation factors and more accurate algorithms with much larger time bounds. The card isolates the endpoint of one almost-linear randomized algorithm with an absolute constant approximation factor.',caption='Editorial endpoint based on the approximation discussion in CPM 2026 Article 27, with the 2025 deterministic and STOC 2026 approximation results distinguished below.',citation='primary',format='editorial_paraphrase'),
 why='Determine whether a basic sequence-similarity measure admits a constant-quality witness in time close to reading the input, even when the alphabet grows. The combined approximation and time target separates the general problem from easy fixed-alphabet guarantees.',
 references=[
 ref('primary','Exploring the Gap Between LCS and LCStr','Shay Golan; Matan Kraus; Ely Porat; B. Riva Shalom',2026,'https://doi.org/10.4230/LIPIcs.CPM.2026.27','Introduction, approximation versions of LCS and LCStr; distinction between LCS and LCSS'),
 ref('subpoly','Approximating the Longest Common Subsequence problem within a sub-polynomial factor in linear time','Negev Shekel Nosatzki',2021,'https://arxiv.org/abs/2112.08454v1','15 December 2021; primary abstract, stated randomized linear-time subpolynomial-factor result'),
 ref('deterministic','Deterministic Longest Common Subsequence Approximation in Near-Linear Time','Itai Boneh; Shay Golan; Matan Kraus',2025,'https://arxiv.org/abs/2507.22486v1','Introduction and Theorem 1, p. 3; growing approximation factor'),
 ref('schemes','Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time','Xiao Mao; Aviad Rubinstein',2026,'https://arxiv.org/abs/2603.29702v1','31 March 2026 version, abstract and Introduction pp. 1–2; STOC 2026 DOI 10.1145/3798129.3800789'),
 ],
 context_blocks=[
 block('LCS permits deletions from both strings while preserving order. Requiring a consecutive block in either string defines a different objective, even when similar terminology is used.'),
 block('For a fixed alphabet of size s, taking the most frequent usable symbol gives a factor depending on s. The present alphabet grows quadratically with total length, so this observation does not provide the required absolute constant.','deterministic'),
 block('The 2021 manuscript states a randomized linear-time approximation with a subpolynomial factor. A factor n^o(1) may still grow without bound and therefore does not by itself supply a constant ratio. This review records the stated result without independently certifying its proof.','subpoly'),
 block('The 2025 deterministic algorithm gives near-linear time with an approximation factor n^(3/4) log n. Its speed does not supply the constant approximation required here.','deterministic'),
 block(r'The STOC 2026 scheme obtains a \((1-\varepsilon)\) fraction of LCS in time \(n^2/2^{\log^{\Omega(1)}n}\) for fixed accuracy. Its stated bound does not reach the almost-linear endpoint.','schemes'),
 ],
 progress=[progress('2021-12-15','A manuscript states linear-time randomized approximation with a subpolynomial, potentially unbounded factor.','subpoly'),progress('2025-07-30','The deterministic near-linear-time result has an approximation factor growing with input size.','deterministic'),progress('2026-03-31','A high-accuracy randomized approximation scheme achieves quasi-strongly subquadratic time.','schemes'),progress('2026','The CPM comparison distinguishes the LCS approximation gap from faster results for substring-related variants.')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified resolution of the combined growing-alphabet, constant-factor, one-algorithm almost-linear target. The cited subpolynomial-factor manuscript and high-accuracy scheme have different guarantees; their complete proofs were not independently audited.',summary=[
 'LCS is the longest sequence obtainable by deleting symbols from each input while preserving their order.',
 'The card asks for an explicit common subsequence within one absolute constant factor of optimum.',
 'One randomized algorithm must work on every growing-alphabet input in almost-linear worst-case time.',
 'Known guarantees with a growing factor or a much larger time bound do not settle this endpoint.',
 'A complete Lean-checked answer must prove the precise existence claim or its unconditional negation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
