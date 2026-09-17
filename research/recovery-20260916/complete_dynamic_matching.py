"""Complete explicit near-optimal dynamic matching with fixed accuracy."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6627'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved all fixed rational accuracies, explicit matching maintenance, expected amortized polylogarithmic updates and an oblivious adversary.',
 'Specified finite polynomial update horizons, simultaneous high-probability correctness after every update, and linear initialization within total expected cost.',
 'Expanded the mate-array representation, graph update validity and constant-time access requirements; all representation changes count.',
 'Specified the finite-word RAM instruction set and random-word cost without adding a stronger space or worst-case-update requirement.',
 'Checked the fixed-accuracy versus inverse-polynomial-accuracy distinction in the ORS and OMv sources, and estimator versus explicit-matching distinction.',
 'Added complete Lean-checked probability and resource criteria, recorded the limited scope of the 2026 maximal-matching result and preserved importance 95.',
]
sources=[
 'Read the inherited MPI Sixteenth Biennial Scientific Report, §27.5.1, Dynamic Matching, printed p. 123. It calls a (1+epsilon)-approximate explicit matching with polylogarithmic updates the ultimate goal and explicitly distinguishes size estimation. Verified a working primary PDF URL through the repository REST endpoint.',
 'Read Assadi–Khanna–Kiss, arXiv:2406.13573v2 (18 October 2024), abstract and §1–1.1 pp. 1–2, Definition 1.1, Result 1 and its parameter footnote, including the explicit discussion of fixed epsilon versus epsilon shrinking with n. Checked the arXiv history and SODA 2025 metadata, pp. 2971–2990, DOI 10.1137/1.9781611978322.96. Full algorithmic proof was not certified.',
 'Read the publisher abstract of Azarmehr–Behnezhad–Roghani, SODA 2024 pp. 3040–3061, DOI 10.1137/1.9781611977912.109, published 4 January 2024. The claimed polylogarithmic algorithm estimates matching size rather than maintaining its edges.',
 'Read Liu, arXiv:2403.02582v1 (5 March 2024; cover 6 March), abstract and §1 pp. 3–4. Its fine-grained connections include polynomial inverse-accuracy dependence and distinguish vertex cover, matching, and advance access to the update sequence. Checked FOCS 2024 metadata, pp. 228–243, DOI 10.1109/FOCS61266.2024.00006.',
 'Read Pratt, arXiv:2502.02455v1 (4 February 2025; cover 5 February), §1 pp. 1–2, Definitions 1.1–1.2 and Theorem 1.3. Checked SOSA 2026 publication, pp. 352–354, DOI 10.1137/1.9781611978964.27. Its ORS-to-RS comparison is not an unconditional polylogarithmic dynamic algorithm.',
 'Read Chuzhoy–Khanna–Song, arXiv:2605.00797v1 (1 May 2026; cover 4 May), abstract and the statement of its maximal-matching target. Checked the STOC publisher abstract, published 9 June 2026, pp. 1604–1615, DOI 10.1145/3798129.3800868. Maximality alone does not give arbitrarily close approximation to maximum size.',
 f'Bounded primary-source searches through {DATE} also checked the ICALP 2026 Dynamic Rank, Basis, and Matching abstract, which concerns a size-maintenance bound. No algorithm satisfying the full explicit fixed-accuracy target was found.',
]
status='The checked work distinguishes matching-size estimation, maximal matching, fixed-accuracy explicit approximation and algorithms given the full update sequence in advance. ORS-dependent bounds and the 2026 deterministic maximal-matching improvement do not give the selected polylogarithmic expected amortized explicit-matching guarantee. No resolution was found in the bounded later-work search.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',year=2026,
 formal=r'''For every fixed rational \(\varepsilon\in(0,1)\) and every fixed integer \(a\ge1\), do there exist a uniform randomized fully dynamic algorithm \(A_{\varepsilon,a}\) and constants \(K,d,B\ge1\) with the following guarantees?

For every \(n\ge2\) and every valid oblivious sequence of \(T\le n^a\) edge insertions and deletions starting from the empty graph on \([n]\), the expected total initialization and update cost is at most
\[
K\left[n+T\bigl(\log_2(n+2)\bigr)^d\right].
\]
With probability at least \(1-n^{-3}\), after every update the algorithm maintains an explicit matching \(M\) in the current graph \(G\) such that
\[
|M|\ge\frac{\nu(G)}{1+\varepsilon},
\]
where \(\nu(G)\) is the maximum matching cardinality. The same constants apply to every \(n,T\) and sequence for the fixed \(\varepsilon,a\).''',
 definitions=r'''At all times the graph is simple, undirected and unweighted, with the fixed vertex set \([n]=\{1,\ldots,n\}\). An edge is an unordered pair of distinct vertices. Initially there are no edges. One update inserts an absent edge or deletes a present edge; only valid update sequences are required to be handled. The graph need not be bipartite or have bounded degree.

A matching is a subset of the current edges in which no vertex belongs to more than one edge. The integer \(\nu(G)\) is the maximum possible number of edges in a matching, and it is zero for an edgeless graph. The algorithm stores a mate array \(\operatorname{mate}[1..n]\): zero means unmatched, while a nonzero value \(\operatorname{mate}[v]=u\) must have \(u\ne v\), \(\operatorname{mate}[u]=v\) and \(\{u,v\}\in E(G)\). Together with its stored cardinality, this explicitly represents \(M\). A size estimate or a fractional assignment to edges is not this representation.

After each completed update, reading the mate of any specified vertex or reading \(|M|\) takes at most a fixed constant number of word operations. Listing the full matching may scan the array in \(O(n)\) time, and need not be performed after every update. All work needed to modify the representation, including every changed array entry and the cardinality, counts toward update cost. External requests to read or list the maintained matching are charged their stated query costs separately; they do not excuse extra update work.

The update sequence is oblivious: for each guarantee it is any fixed sequence independent of the algorithm’s random bits. Updates are delivered one at a time, and the algorithm must finish processing one before seeing the next. It knows \(n\) and has the fixed parameters \(\varepsilon,a\), but the future sequence and its actual length are not supplied in advance. This is distinct from a computation receiving all updates at once, and it makes no guarantee against an adversary choosing updates from observed random-dependent outputs.

Use a word-RAM with word length \(w=B\lceil\log_2(n+2)\rceil\) bits, with \(B\) a fixed positive integer for the algorithm. Memory cells have word addresses and initially contain zero; every access or write costs an operation, and untouched cells require no initialization work. The instruction set consists of word reads and writes, indirect addressing, comparisons, conditional branches, addition, subtraction and multiplication modulo \(2^w\), integer quotient and remainder with a nonzero divisor, bitwise Boolean operations and shifts. A shift by at least \(w\) returns zero. A fresh independent uniform \(w\)-bit random word costs one operation. Stored random words and intermediate values use ordinary memory. Larger integers must use multiple words, with all operations charged; no arbitrary-precision operation, graph oracle or precomputed instance advice is available. No additional linear-space restriction is imposed.

Expectation is over the algorithm’s private randomness on each fixed sequence and includes the entire initialization and all \(T\) updates. The bound is amortized over that sequence, not a worst-case bound on each individual update. The required finite expectation includes termination with probability one. Separately, one event of probability at least \(1-n^{-3}\) must ensure the valid mate representation and approximation inequality after every update in the sequence simultaneously. A separate probability bound at each time without this joint guarantee is insufficient.

The parameters \(\varepsilon\) and \(a\) are fixed independently of \(n\). The machine and constants may depend on both; no polynomial dependence on \(1/\varepsilon\) and no uniform compiler taking \(\varepsilon,a\) as inputs is required. Integer \(a\) covers every polynomial sequence-length regime. There is no demand for an infinite update sequence with one global success event. This is an exact existence proposition for the stated approximation scheme and resources, not a numerical question about \(\nu(G)\).''',
 answer_criterion=r'''Supply algorithms and a complete Lean-checked proof covering every fixed rational \(\varepsilon\), every fixed polynomial horizon, every \(n\), and every valid oblivious sequence, including the expected total cost, representation-access costs and simultaneous success event. Alternatively, give a complete Lean-checked refutation of these quantified guarantees; failure for one fixed accuracy and one fixed horizon exponent, for every admissible algorithm and constants, suffices.

An estimator without explicit matching edges, a fixed approximation factor bounded away from one, a partially dynamic algorithm, an algorithm receiving future updates, or an update bound larger than every fixed power of \(\log n\) does not prove the proposition. A lower bound requiring accuracy to shrink with \(n\), polynomial dependence on \(1/\varepsilon\), or an adaptive adversary does not by itself refute this weaker stated target. Conditional lower bounds require their hypotheses and are not unconditional negative answers.''',
 source_formulation=dict(text='The inherited Dynamic Matching section describes maintaining a (1+epsilon)-approximate matching with polylogarithmic update time as a central long-term objective and distinguishes it from maintaining only an estimate of the optimum size. This card retains its previously selected fixed-accuracy, oblivious-adversary, randomized expected-amortized version.',caption='Paraphrase of the MPI Sixteenth Biennial Scientific Report, §27.5.1, Dynamic Matching, printed p. 123.',citation='primary',format='editorial_paraphrase'),
 why='A single insertion or deletion can change which edges should be used together in a large matching. The question asks whether a near-optimal explicit solution can be kept current at a cost that grows only polylogarithmically with graph size, combining approximation quality with efficient dynamic maintenance.',
 references=[
 ref('primary','Sixteenth Biennial Scientific Report: March 2021–March 2023','Max Planck Institute for Informatics',2023,'https://pure.mpg.de/rest/items/item_3527212_4/component/file_3527885/content','§27.5.1, Dynamic Matching, printed p. 123; repository REST download verified during this review'),
 ref('estimate',r'Fully Dynamic Matching: \((2-\sqrt2)\)-Approximation in Polylog Update Time','Amir Azarmehr; Soheil Behnezhad; Mohammad Roghani',2024,'https://epubs.siam.org/doi/10.1137/1.9781611977912.109','SODA 2024, 3040–3061; published 4 January 2024; publisher abstract explicitly specifies estimation of maximum-matching size'),
 ref('ors','Improved Bounds for Fully Dynamic Matching via Ordered Ruzsa-Szemerédi Graphs','Sepehr Assadi; Sanjeev Khanna; Peter Kiss',2025,'https://arxiv.org/abs/2406.13573v2','Author v2 posted 18 October 2024; §1–1.1 pp. 1–2, Definition 1.1, Result 1 and parameter footnote; SODA 2025, 2971–2990, DOI 10.1137/1.9781611978322.96'),
 ref('liu','On Approximate Fully-Dynamic Matching and Online Matrix-Vector Multiplication','Yang P. Liu',2024,'https://arxiv.org/abs/2403.02582v1','Version 1, 5 March 2024; §1 pp. 3–4, distinctions between matching and vertex cover, online and offline input, and inverse-accuracy dependence; FOCS 2024, 228–243, DOI 10.1109/FOCS61266.2024.00006'),
 ref('pratt','A note on Ordered Ruzsa-Szemerédi graphs','Kevin Pratt',2026,'https://arxiv.org/abs/2502.02455v1','Author v1 posted 4 February 2025; §1 pp. 1–2, Theorem 1.3; SOSA 2026, 352–354, DOI 10.1137/1.9781611978964.27'),
 ref('maximal','A Faster Deterministic Algorithm for Fully Dynamic Maximal Matching','Julia Chuzhoy; Sanjeev Khanna; Junkai Song',2026,'https://arxiv.org/abs/2605.00797v1','Version 1, 1 May 2026; abstract; STOC 2026, 1604–1615, published 9 June 2026, DOI 10.1145/3798129.3800868'),
 ],
 context_blocks=[
 block('The maintained object must contain compatible graph edges. Reporting a good estimate of how many such edges could be chosen leaves a separate search and maintenance task, which the source explicitly distinguishes.'),
 block('Azarmehr, Behnezhad and Roghani improve the approximation achievable in polylogarithmic update time for estimating matching size. Their result does not maintain the mate array required here.','estimate'),
 block('Assadi, Khanna and Kiss obtain explicit near-optimal matching bounds governed by the density of ordered Ruzsa–Szemerédi graphs. Those graphs decompose into ordered matchings, each induced in the union of itself and the later matchings. The resulting structural dependence does not supply a universal polylogarithmic bound.','ors'),
 block('Pratt relates the density of those ordered graphs to the older unordered variant. The theorem resolves a comparison between two combinatorial quantities, rather than completing the dynamic matching algorithm target.','pratt'),
 block('The fixed-accuracy convention matters: an algorithm may have very large dependence on the chosen accuracy. Lower bounds that require one polynomial dependence as accuracy shrinks with graph size cannot simply be transferred to this formulation.','liu'),
 block('A maximal matching cannot be extended by adding another edge, but it may be much smaller than a maximum matching. The 2026 deterministic maximal-matching result improves a different maintenance guarantee and does not yield approximation arbitrarily close to one.','maximal'),
 ],
 progress=[
 progress('2023','The inherited report distinguishes explicit matching from size estimation and identifies the near-optimal polylogarithmic-update objective.'),
 progress('2024-01-04','A stronger constant approximation for matching-size estimation is published with polylogarithmic updates.','estimate'),
 progress('2024-10-18','The revised ORS-based algorithm gives improved structural bounds for explicit matching at fixed accuracy; published at SODA 2025.','ors'),
 progress('2025–2026','The ORS–RS density comparison appears as a 2025 preprint and a SOSA 2026 paper.','pratt'),
 progress('2026-06-09','The STOC maximal-matching algorithm improves deterministic update time for its distinct target.','maximal'),
 ],
),notes,sources,status,summary=[
 'The graph undergoes online edge insertions and deletions, and the algorithm must maintain the actual edges of a near-maximum matching.',
 'For every fixed accuracy it must have polylogarithmic expected amortized update time, including linear initialization in the total cost.',
 'The sequence is fixed independently of the algorithm’s randomness, and one high-probability event must guarantee correctness throughout each polynomial-length sequence.',
 'The matching is stored explicitly with constant-time mate and cardinality access, and every change to that representation is charged.',
 'A complete Lean-checked solution must establish all these guarantees or refute them; size estimation and maximal matching solve different tasks.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
