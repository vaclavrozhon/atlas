"""Distinguish all-length fixed-modulus certification from selected comparisons."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0466';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the selected O(n log n) target and the supplied polynomially bounded prime and alphabet base.',
 'Specified all positive substring lengths, overlapping occurrences and the distinction between unequal strings and unequal starting positions.',
 'Made the uniform quantifiers, worst-case bound on every random execution, one-sided acceptance guarantee and working-space allowance explicit.',
 'Included small primes and primes dividing the base; the input promises primality but not a good modulus or coprimality.',
 'Separated verification of selected power-of-two comparisons from collision freedom for every length under this one supplied fingerprint.',
 'Read the 2015 LCE verification scope and the 2026 compressed-index discussion; neither is asserted to solve the all-length target.',
 'Preserved importance, added dated progress and required a complete Lean-checked answer in the same model.',
]
sources=[
 'Read Adaptive and Scalable Data Structures, Dagstuhl Seminar 25191, DOI 10.4230/DagRep.15.5.1, Section 5.5, pp.17–18, Martin Farach-Colton: fixed string and prime, alphabet-base polynomial fingerprints, collisions between unequal substrings of the same length, quadratic suffix-tree baseline, linear or O(n log n) target and permission for small-probability false rejection. The seminar ran 4–9 May 2025. The card retains its already selected O(n log n) bound and explicit success probability.',
 'Read Bille–Gørtz–Knudsen–Lewenstein–Vildhøj, Longest Common Extensions in Sublinear Space, arXiv:1504.02671v1, 10 April 2015, Section 3.5. Verification concerns the pairs actually compared by the query procedure: lengths 2^l tau and a sampled starting position. The text invokes earlier verification for small tau and resamples a fingerprint on finding a collision. Section 4, Lemma 6 constructs a tuple of fingerprints with selected positions and lengths. Neither is an all-length certificate for the unchanged single supplied prime and base in this card.',
 'Read Kosolobov, Compressed Index with Construction in Compressed Space, CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.25, published 8 June 2026, full primary HTML abstract and Introduction. It reports an O(n log n)-time, O(n)-space verification bound for power-of-two substring lengths, citing the 2015 LCE paper as reference 10. Its new compressed index avoids Karp–Rabin fingerprints entirely; expected randomized construction uses dictionaries instead. This is a different guarantee from certifying all lengths for the input modulus.',
 'Bounded primary-source checks through 17 September 2026 found no verified resolution of this fixed-fingerprint, all-length, one-sided target. Related constructions of a chosen good fingerprint, multiple-fingerprint representations and selected-comparison verification were not treated as solutions.',
]
complete(identifier,dict(
 formal=r'''For every fixed integer \(c\ge2\), do there exist a constant \(K\ge1\) and one uniform randomized algorithm \(A\) with this guarantee? Its input is \(n\ge2\), an alphabet size \(2\le\sigma\le n^c\), a string \(T\in\{0,\ldots,\sigma-1\}^n\) and a supplied prime \(2\le p\le n^c\). Every execution takes at most \(Kn\log_2(n+2)\) word-RAM instructions. It outputs CERTIFIED or REJECT for the single fingerprint
\[
h_p(T[i..i+\ell-1])=\sum_{a=0}^{\ell-1}T[i+a]\sigma^a\pmod p.
\]
If any two unequal equal-length substrings collide, every execution must output REJECT. If no such pair exists, the probability of CERTIFIED must be at least \(2/3\). All lengths \(1\le\ell\le n\) are included; the supplied base and prime remain fixed.''',
 definitions=r'''Positions of \(T\) are numbered \(0,\ldots,n-1\). For each \(1\le\ell\le n\), the valid starts are \(0\le i\le n-\ell\). A collision is a triple \((i,j,\ell)\) of valid starts and a length such that the strings \(T[i..i+\ell-1]\) and \(T[j..j+\ell-1]\) are unequal but have equal displayed fingerprints. Overlapping occurrences are included. Distinct starting positions that spell the same string are not a collision. Equal fingerprints of different-length strings are irrelevant. Collision-free means there is no collision at any valid length and pair of starts.

The base is exactly the supplied alphabet size \(\sigma\), not a new random evaluation point. The modulus is exactly the supplied prime \(p\). There is no promise that \(p>\sigma\), that \(p\) is coprime to \(\sigma\), or that this fingerprint is good. Primality is an input promise. Internal auxiliary fingerprints or indexes are allowed if their construction is charged, but their validity cannot replace certification of the specified \(h_p\). A REJECT output does not have to contain a collision witness.

Use a uniform sequential word RAM with \(w=\lceil(4c+10)\log_2(n+2)\rceil\)-bit unsigned words, a fixed finite program and word-addressed memory. Unit-cost instructions are reads, writes, comparisons, branches, addition, subtraction and multiplication modulo \(2^w\), integer quotient and remainder with nonzero divisor, bitwise Boolean operations and logical shifts; shifts by at least \(w\) yield zero. An independent uniform random word may be generated in one step. Addresses must fit a word. No unbounded-integer primitive, advice, external oracle or quantum operation is provided.

The input is a read-only array containing \(n,\sigma,p\) and the \(n\) symbols, one per word. All input-dependent computation, preprocessing, table construction and auxiliary representations count toward the time bound. Initially there is no supplied suffix index or other precomputed information. Apart from the input and a fixed number of registers, at most \(Kn\log_2(n+2)\) working words may be used, after increasing the same constant \(K\) if necessary. This is the ordinary space allowance implied by the time budget, not a separate linear-space target.

The quantifier order is \(\forall c\,\exists(K,A)\,\forall(n,\sigma,p,T)\) satisfying the promises. The program and constant may depend on \(c\) but not on the input length, string, base or prime. The instruction bound holds for every random execution, not merely in expectation. For each fixed collision-free input, probability is taken only over the algorithm's independent random words. False rejection has probability at most \(1/3\); false certification is never allowed. Checking only a prescribed family of lengths or only the pairs queried by some other algorithm is a different task.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the existence proposition or its logical negation. A positive proof must establish the uniform algorithm, the bound on every execution, and both one-sided correctness requirements for every allowed input. A negative proof must rule out the full stated proposition unconditionally; a conditional lower bound is only a conditional result.

Finding a different good modulus, selecting another base, or constructing a tuple of fingerprints does not certify the input fingerprint. A result limited to power-of-two lengths, sampled positions, a restricted class of strings or only the comparisons made by an index is insufficient. The stricter linear-time alternative mentioned by the source is not required here.''',
 source_formulation=dict(text='Farach-Colton asks how quickly a supplied prime can be checked for collisions between unequal, equal-length substrings of a supplied string. The source seeks linear time or at least n log n time, and permits small-probability false rejection. This card retains the latter time target with an explicit one-sided probability and word-RAM model.',caption='Adaptive and Scalable Data Structures, Seminar 25191 (May 2025), §5.5, pp.17–18; explicit constants and model are editorial specifications.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Adaptive and Scalable Data Structures','Martin Farach-Colton (problem contributor); Michael A. Bender, John Iacono, László Kozma and Eva Rotenberg (editors)',2025,'https://doi.org/10.4230/DagRep.15.5.1','Seminar 25191, 4–9 May 2025; §5.5, Detecting collisions in Karp-Rabin fingerprinting, pp.17–18'),
 ref('lce','Longest Common Extensions in Sublinear Space','Philip Bille; Inge Li Gørtz; Mathias Bæk Tejs Knudsen; Moshe Lewenstein; Hjalte Wedel Vildhøj',2015,'https://arxiv.org/abs/1504.02671v1','10 April 2015; §3.5, verification of query comparisons; §4, Lemma 6, constructed fingerprint tuples'),
 ref('index','Compressed Index with Construction in Compressed Space','Dmitry Kosolobov',2026,'https://doi.org/10.4230/LIPIcs.CPM.2026.25','Published 8 June 2026; abstract and Introduction, power-of-two verification and construction without Karp–Rabin fingerprints'),
 ],
 context_blocks=[
 block('A fingerprint speeds up equality tests by replacing a string with a small residue. This question concerns a guarantee about every equal-length comparison inside one text, even if no particular index ever makes that comparison.'),
 block('The original problem records a quadratic-time baseline and asks for a linear or n log n bound. Allowing false rejection means the procedure may occasionally decline to certify a good input; it may never approve a collision.'),
 block('The 2015 LCE construction verifies selected pairs required by its query procedure and can choose another fingerprint when verification fails. Its deterministic construction also permits tuples of fingerprints. Those scope choices differ from this fixed single-fingerprint task.','lce'),
 block('The 2026 compressed-index paper explicitly discusses n log n verification for power-of-two lengths. Its own new index avoids Karp–Rabin fingerprints. Neither statement establishes all-length certification for the supplied base and modulus.','index'),
 ],
 progress=[progress('2015-04-10','LCE structures verify selected comparisons and construct suitable fingerprints or fingerprint tuples.','lce'),progress('2025-05','The seminar asks for faster certification over all substring lengths with one supplied prime and allows one-sided false rejection.'),progress('2026-06-08','A new compressed index avoids Karp–Rabin fingerprints; its background discussion still distinguishes verification for power-of-two lengths.','index')],
),notes,sources,'Open in the May 2025 seminar source. Bounded primary-source checks through 17 September 2026 found no verified resolution of the all-length fixed-base, fixed-prime target. The reviewed selected-comparison verification and 2026 compressed-index construction have different guarantees; this review is not an exhaustive certification of current openness.',summary=[
 'The input is a string, its alphabet size and a fixed prime modulus.',
 'The algorithm must certify that unequal substrings of every common length have different polynomial fingerprints.',
 'The target is worst-case n log n time with all preprocessing included.',
 'A bad fingerprint must always be rejected, while every good fingerprint must be certified with probability at least two thirds.',
 'Verification of selected lengths or construction of a different fingerprint does not settle the target; a complete Lean-checked answer is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
