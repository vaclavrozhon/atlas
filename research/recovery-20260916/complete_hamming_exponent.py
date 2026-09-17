"""Complete the fixed polynomial improvement for all exact alignment distances."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7367';claim=read_claims(ROOT)[identifier]
notes=[
 'Kept any one fixed positive saving below the square-root exponent, uniform over both input lengths.',
 'Specified all exact Hamming distances in alignment order over the explicit polynomial-size integer alphabet.',
 'Expanded Las Vegas correctness, almost-sure termination and per-input expected time in a uniform charged word-RAM model.',
 'Distinguished unrestricted algorithms from combinatorial conditional barriers and the range-restricted counting equivalence from ordinary 3SUM.',
 'Checked later approximate algorithms and Hamming-distance oracles without promoting them to exact all-alignment breakthroughs.',
 'Preserved importance 89 and required a complete Lean-checked proof of the proposition or its negation.',
]
sources=[
 'Read Chan–Jin–Vassilevska Williams–Xu, Faster Algorithms for Text-to-Pattern Hamming Distances, arXiv:2310.13174v3, revised 19 December 2024: abstract, Introduction, Theorems 1.1–1.3, Problems 1–2 and Theorem 1.6. The exact Las Vegas bound removes logarithmic factors but retains the square-root exponent; the sublinear inverse-accuracy exponent concerns approximation. The counting equivalence uses a consecutive-range target set C=[N] and comparable text/pattern lengths, not unrestricted decision 3SUM. The live history still lists v3 as latest.',
 'Read Fischer–Jin–Xu, New Applications of 3SUM-Counting in Fine-Grained Complexity and Pattern Matching, arXiv:2410.20764v1, posted 28 October 2024, primary abstract/history. Its Hamming-distance algorithm is a (1+epsilon) approximation with n^(1+o(1))/epsilon time; it does not state the exact fixed-exponent improvement. The separate deterministic equivalence between unrestricted counting 3SUM and decision 3SUM does not remove the range restriction from the target paper by itself.',
 'Read Boneh–Fried–Golan–Kraus–Porat, Hamming Distance Oracles, CPM 2026 Article 1, primary abstract and publication metadata. Its model preprocesses two strings and answers substring-distance queries, with explicit preprocessing/query tradeoffs and a separate approximate guarantee. It does not state the all-alignments exact Las Vegas bound requested here.',
 'Checked primary author publication lists and bounded later-work searches through 17 September 2026. No verified exact algorithm crossing the fixed square-root exponent barrier was located. No full proof audit or execution of the cited algorithms was performed.',
]
complete(identifier,dict(
 title='Text-to-pattern Hamming distances below the square-root barrier',criterion='resources',question_type='yes_no',
 formal=r'''Do there exist absolute constants \(\varepsilon\in(0,1/2)\), \(K>0\), an integer \(B\ge8\), and one uniform classical Las Vegas word-RAM algorithm \(A\) such that, for all integers \(n\ge2\), \(1\le m\le n\), every text \(T\in\{0,\ldots,n^2-1\}^{n}\) and pattern \(P\in\{0,\ldots,n^2-1\}^{m}\), it outputs every exact distance
\[
 h_i=|\{j\in\{0,\ldots,m-1\}:T[i+j]\ne P[j]\}|
 \quad (i=0,\ldots,n-m)
\]
and satisfies
\[
 \mathbb E[\operatorname{time}_A(T,P)]
 \le Knm^{1/2-\varepsilon}?
\]
The expectation is over internal randomness for each fixed input. The word length is \(w=B\lceil\log_2(n+2)\rceil\), and correctness is required on every terminating execution.''',
 definitions=r'''The text and pattern are explicit arrays with one integer symbol per word. Hamming distance between equal-length strings counts unequal coordinates; only substitutions matter, and there are no insertions, deletions, wildcards or symbol weights. Alignment \(i\) compares the entire pattern to the consecutive length-\(m\) substring of the text starting at zero-based position \(i\). Every permitted alignment is included, even if its distance is large.

The output is the array \((h_0,\ldots,h_{n-m})\), in increasing alignment order, with one integer in \(\{0,\ldots,m\}\) per word. It is not enough to identify zero distances, report only alignments below a threshold, return one best alignment or approximate the distances. No text index or auxiliary preprocessing is supplied for free. Both strings may be accessed throughout the computation, and the time includes reading, initialization, preprocessing, all intermediate work and output writes.

The sequential word RAM has a fixed finite program. Allowed unit-cost instructions are word reads and writes, copying, comparison, branching, Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), integer quotient and remainder with a nonzero divisor, and generation of an independent uniformly random \(w\)-bit word. Shifts by at least \(w\) return zero. Values and addresses fit in words, and multiword operations are charged by their constituent instructions. There are no arbitrary-precision unit-cost arithmetic operations, advice, external oracles or free size-dependent lookup tables. Workspace is limited by this address model but has no separate linear-space requirement.

Las Vegas means that every execution which terminates has the correct entire output, and termination occurs with probability one on every fixed valid input. The expected instruction count has the displayed bound; no worst-case cap on every random tape is required. A Monte Carlo algorithm with a small chance of incorrect output is not sufficient. A deterministic algorithm is allowed as a special case. There is no restriction to methods described informally as combinatorial; algebraic computation and fast matrix multiplication are permitted if implemented in the stated model and charged for their actual instructions.

The same \(\varepsilon,K,B\) and program work for all lengths and strings. The saving is chosen once and may be arbitrarily small but positive. It may not tend to zero with the input size, depend on the ratio of the two lengths, or apply only to a selected length regime. The target has no additional hidden logarithmic factor in \(n\); all costs must fit the explicit bound. Restricting to a fixed-size alphabet changes the problem because it enables faster special-case algorithms.''',
 answer_criterion=r'''Give a complete mathematically correct proof checked in Lean of the stated existence proposition or its logical negation. A positive answer must establish exact Las Vegas correctness, almost-sure termination and the uniform expected bound for some fixed positive \(\varepsilon\), over the full input domain.

Removing logarithmic factors while retaining \(m^{1/2}\), a saving that vanishes with input size, approximate distances, or a faster algorithm on a constant alphabet does not meet this target. Conditional hardness under a matrix-multiplication or arithmetic conjecture establishes only a conditional conclusion. A restriction to combinatorial algorithms cannot refute existence in the unrestricted RAM class. No minimum saving such as \(1/100\) is imposed.''',
 source_formulation=dict(text='The revised FOCS 2023 paper removes the logarithmic overhead in exact text-to-pattern Hamming distances and studies the remaining arithmetic and combinatorial barriers. This card asks for a fixed polynomial improvement in the pattern-length exponent beyond one half, with unrestricted Las Vegas algorithms.',caption='Chan–Jin–Vassilevska Williams–Xu, Introduction, Theorem 1.2 and Theorem 1.6; fixed-exponent target retained.',citation='primary',format='editorial_paraphrase'),
 why='Computing exact mismatch counts at every alignment is a basic string-processing task with a long-standing square-root dependence on the pattern length. A fixed exponent saving would also advance closely related restricted arithmetic-counting computations.',
 references=[
 ref('primary','Faster Algorithms for Text-to-Pattern Hamming Distances','Timothy M. Chan; Ce Jin; Virginia Vassilevska Williams; Yinzhan Xu',2024,'https://arxiv.org/abs/2310.13174v3','19 December 2024 revision of the FOCS 2023 paper; Introduction, Theorems 1.1–1.3, Problems 1–2 and Theorem 1.6'),
 ref('counting','New Applications of 3SUM-Counting in Fine-Grained Complexity and Pattern Matching','Nick Fischer; Ce Jin; Yinzhan Xu',2024,'https://arxiv.org/abs/2410.20764v1','28 October 2024; primary abstract, deterministic approximation and counting equivalence'),
 ref('oracles','Hamming Distance Oracles','Itai Boneh; Dvir Fried; Shay Golan; Matan Kraus; Ely Porat',2026,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.1','CPM 2026, Article 1; primary abstract, preprocessing/query tradeoffs and approximation'),
 ],
 context_blocks=[
 block('The exact all-alignment problem must distinguish every possible integer mismatch count. A thresholded or approximate computation can discard information that this output requires.'),
 block('The checked Las Vegas algorithm attains O(n times the square root of m), eliminating an earlier logarithmic overhead. This improves the running time without crossing the fixed exponent barrier.'),
 block('The source relates the comparable-length case to counting pairs of integers whose sums lie in a specified consecutive interval. Its precise restriction matters; an ordinary 3SUM hardness assumption is not an established lower bound for this target merely because 3SUM appears in the discussion.'),
 block('A later deterministic approximation result and a separate equivalence for unrestricted 3SUM counting concern related tasks, but do not establish the exact fixed-exponent improvement.','counting'),
 block('The 2026 distance-oracle work separates preprocessing from individual substring queries. Its tradeoffs and approximate guarantees must not be confused with an uncharged index for this all-alignments task.','oracles'),
 ],
 progress=[progress('2024-12-19','The checked revision gives exact Las Vegas O(n times the square root of m) time and a fine-grained equivalence to range-restricted counting 3SUM.'),progress('2026','Hamming-distance oracles provide new substring-query tradeoffs in a different preprocessing model.','oracles')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified fixed positive exponent saving for exact unrestricted-alphabet Las Vegas all-alignment computation. The checked exact theorem retains the square-root factor. Approximation, restricted counting equivalences and distance-oracle results have been separated by scope; full cited proofs were not independently certified.',summary=[
 'The input is an explicit text and pattern over a polynomial-size integer alphabet.',
 'The output contains the exact number of mismatches at every alignment, in order.',
 'The target improves the square-root dependence on pattern length by one fixed positive exponent.',
 'Randomness may affect running time but must never produce an incorrect terminating answer.',
 'Acceptance requires a complete Lean-checked proof or refutation in the stated uniform word-RAM model.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
