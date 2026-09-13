# Researcher–problem explanations and source locators

These are editorial research affinities. Status and evidence are snapshots of the canonical cards, not new certification of all reused entries. The [overview](README.md) explains the scope.

## 1. Ryan Williams

[Research bibliography](https://dblp.org/pid/w/RyanWilliams.html).

### 1. NEXP versus nonuniform \(\mathrm{TC}^{0}\)

[TCS-7161](../../data/cards/TCS-7161.json) · reused · status: `open` · evidence: `reviewed`.

Circuit lower bounds beyond the ACC frontier of his algorithms-to-lower-bounds program.

**Status scope:** No \(\mathrm{NEXP}\not\subset \mathrm{TC}^{0}\) resolution found through 11 September 2026. The checked March, July and September results retain different hard-language models or fixed depth and polynomial quantitative bounds. The September preprint has a source comment raising concerns and is recorded as an unverified claim.

Sources: [Non-Uniform ACC Circuit Lower Bounds](https://doi.org/10.1109/CCC.2011.36); [Wikipedia: Circuit complexity](https://en.wikipedia.org/wiki/Circuit_complexity); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1328197464); [Non-Uniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-ccc.pdf); [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/); [Almost-Everywhere Near-Cubic Wire Lower Bounds for SYM ∘ THR and \(\mathrm{THR} \circ  \mathrm{THR}\)](https://eccc.weizmann.ac.il/report/2026/167/); [Near-Maximum Circuit Lower Bounds for Exponential Time with Merlin-Arthur Queries](https://eccc.weizmann.ac.il/report/2026/118/).

### 2. Stronger log-space time lower bounds for SAT

[TCS-0303](../../data/cards/TCS-0303.json) · reused · status: `uncertain` · evidence: `index`.

Quantitative time-space lower bounds for SAT connect directly to his work on time and space.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf).

## 2. Irit Dinur

[Research bibliography](https://dblp.org/pid/18/3891.html).

### 1. Linear-length locally testable codes and proofs

[TCS-6738](../../data/cards/TCS-6738.json) · reused · status: `source_open` · evidence: `source`.

Linear-length local testability is a central frontier after her constructions of good locally testable codes.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2017 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html).

### 2. Sliding-scale PCP conjecture

[TCS-7268](../../data/cards/TCS-7268.json) · reused · status: `source_open` · evidence: `reviewed`.

PCP soundness and alphabet tradeoffs extend her foundational PCP work.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Polynomially Low Error PCPs with polyloglog n Queries via Modular Composition](https://arxiv.org/abs/1505.06362).

## 3. Avi Wigderson

[Research bibliography](https://dblp.org/pid/w/AviWigderson.html).

### 1. P versus BPP

[TCS-0003](../../data/cards/TCS-0003.json) · reused · status: `uncertain` · evidence: `reviewed`.

Derandomization is a central theme across his complexity and pseudorandomness work.

**Status scope:** \(\mathrm{P}=\mathrm{BPP}\) remains the target of mainstream derandomization work cited in May 2026. A July 2026 revision of a preprint claims separation; this review has not established its correctness or independent validation. The card is not marked resolved. Status search performed through 10 September 2026.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [\(\mathrm{P}=\mathrm{BPP}\) unless E has sub-exponential circuits: Derandomizing the XOR Lemma](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/IW97/proc.pdf); [Pseudorandomness Beating the Hybrid Argument for Insensitive Algorithms](https://eccc.weizmann.ac.il/report/2026/082/); [Probabilistic Computers (and Hence Quantum Computers) Are Rigorously More Powerful Than Classical Deterministic Computers, and Derandomization](https://arxiv.org/abs/2308.09549v9).

### 2. VP versus VNP

[TCS-0005](../../data/cards/TCS-0005.json) · reused · status: `source_open` · evidence: `reviewed`.

General arithmetic circuit lower bounds are a core target of his algebraic complexity program.

**Status scope:** The August 2026 primary paper still identifies the unrestricted VP-versus-VNP separation as open and explicitly limits its new constructions. No general resolution was located in the status search through 10 September 2026.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [Completeness Classes in Algebra](https://doi.org/10.1145/800135.804419); [Superpolynomial Lower Bounds Against Low-Depth Algebraic Circuits](https://eccc.weizmann.ac.il/report/2021/081/); [Arithmetic circuit lower bounds from sumset expansion](https://eccc.weizmann.ac.il/report/2026/138/).

## 4. Venkatesan Guruswami

[Research bibliography](https://dblp.org/pid/g/VenkatesanGuruswami.html).

### 1. Full-length Reed–Solomon list decoding beyond Johnson

[TCS-1011](../../data/cards/TCS-1011.json) · reused · status: `uncertain` · evidence: `index`.

Reed-Solomon list decoding beyond Johnson is directly in his coding research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

### 2. Constant-colour polynomial-time colouring of 3-colourable graphs

[TCS-6637](../../data/cards/TCS-6637.json) · reused · status: `source_open` · evidence: `reviewed`.

Coloring promised 3-colorable graphs connects his work on promise CSPs and inapproximability.

**Status scope:** No constant-colour algorithm or unrestricted all-constant hardness resolution found through 11 September 2026. The February 2026 primary paper retains the gap between five-colour NP-hardness and a growing \(O(n^{0.19539})\) algorithmic bound. The March logic result is restricted to fixed-point logic with counting. This card explicitly allows bounded-error randomized algorithms.

Sources: [Better coloring of 3-colorable graphs](https://arxiv.org/abs/2406.00357); [Algebraic Approach to Promise Constraint Satisfaction](https://arxiv.org/abs/1811.00970); [d-To-1 Hardness of Coloring 3-Colorable Graphs with \(O(1)\) Colors](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.62); [Improved SDP-Based Algorithm for Coloring 3-Colorable Graphs](https://arxiv.org/abs/2602.05904); [Undefinability of Approximation of 2-to-2 Games](https://arxiv.org/abs/2504.03523).

## 5. Daniel Spielman

[Research bibliography](https://dblp.org/pid/s/DanielASpielman.html).

### 1. Strongly explicit Ramanujan families for every degree

[TCS-7285](../../data/cards/TCS-7285.json) · reused · status: `source_open` · evidence: `reviewed`.

Strongly explicit Ramanujan families continue his spectral and interlacing-polynomial constructions.

**Status scope:** The primary source distinguishes available exact special-degree families from arbitrary-degree constructions with slack. The statement and a bounded later-work search were reviewed on 13 September 2026 without finding a general exact strongly explicit construction. This is not a claim of an exhaustive status audit.

Sources: [Explicit expanders of every degree and size](https://arxiv.org/abs/2003.11673).

### 2. Nearly linear-time solution of general sparse linear systems

[TCS-6585](../../data/cards/TCS-6585.json) · reused · status: `source_open` · evidence: `reviewed`.

General sparse linear systems extend the scope of his fast Laplacian-solving program.

**Status scope:** Checked through 10 September 2026. This is an editorial, fully specified near-linear target in the polynomial-conditioning and precision regime, not a named positive conjecture. The faster-than-matrix-multiplication problem has already been solved. The August 2026 report discusses broader scalable solvers but does not claim this universal guarantee; the simplicial-Laplacian reduction is not a general running-time lower bound.

Sources: [Solving Sparse Linear Systems Faster than Matrix Multiplication](https://arxiv.org/abs/2007.10254); [Nearly Linear Time Algorithms for Preconditioning and Solving Symmetric, Diagonally Dominant Linear Systems](https://epubs.siam.org/doi/10.1137/090771430); [Matrix anti-concentration inequalities with applications](https://arxiv.org/abs/2111.05553); [Hardness Results for Laplacians of Simplicial Complexes via Sparse-Linear Equation Complete Gadgets](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.53); [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394).

## 6. Nikhil Bansal

[Research bibliography](https://dblp.org/pid/69/5601.html).

### 1. Komlós conjecture

[TCS-7314](../../data/cards/TCS-7314.json) · reused · status: `source_open` · evidence: `reviewed`.

Algorithmic discrepancy places the Komlos bound at the center of his research.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. The companion Beck–Fiala target is a documented consequence, not a duplicate. No algorithmic construction requirement is added.

Sources: [Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk](https://arxiv.org/abs/2508.03961).

### 2. Randomized competitiveness of k-server

[TCS-7317](../../data/cards/TCS-7317.json) · reused · status: `source_open` · evidence: `reviewed`.

Randomized k-server connects his discrepancy, rounding and online-algorithm work.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. This is explicitly the polylogarithmic k-only question, not the false \(O(\log  k)\) conjecture or the resolved worst-case metrical-task-system ratio.

Sources: [Randomized k-server in polynomial time](https://arxiv.org/abs/2605.01497); [The Randomized k-Server Conjecture is False!](https://arxiv.org/abs/2211.05753).

## 7. Virginia Vassilevska Williams

[Research bibliography](https://dblp.org/pid/63/8319.html).

### 1. Matrix multiplication exponent

[TCS-0007](../../data/cards/TCS-0007.json) · reused · status: `source_open` · evidence: `reviewed`.

Fast matrix multiplication is a direct sustained research contribution.

**Status scope:** The latest primary upper bound located through 10 September 2026 is the reported omega<2.371177 from August 2026. It leaves the omega=2 question open. The model is exact arithmetic over C; the catalogue has not independently reproduced the numerical certificate. The 12 September 2026 edit adopts absolute 0.01 benchmark acceptance; the saved open-status evidence concerns the underlying exact question and does not independently certify openness at that tolerance.

Sources: [Gaussian elimination is not optimal](https://doi.org/10.1007/BF02165411); [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [Limits on the Universal Method for Matrix Multiplication](https://arxiv.org/abs/1812.08731); [More Asymmetry Yields Faster Matrix Multiplication](https://doi.org/10.1137/1.9781611978322.63); [Improving the matrix multiplication exponent with modern optimization and AlphaEvolve](https://arxiv.org/abs/2608.16884v1); [More Asymmetry Yields Faster Matrix Multiplication — August 2026 revision](https://arxiv.org/abs/2404.16349v3).

### 2. Truly subcubic APSP

[TCS-6510](../../data/cards/TCS-6510.json) · reused · status: `open` · evidence: `reviewed`.

Truly subcubic APSP is a central barrier in her fine-grained complexity program.

**Status scope:** Reviewed 10 September 2026. The target is a fixed exponent saving for arbitrary real edge weights; the 2026 node-weighted triangle result does not supply it.

Sources: [Subcubic Equivalences between Path, Matrix and Triangle Problems](https://doi.org/10.1109/FOCS.2010.67); [Faster all-pairs shortest paths via circuit complexity](https://arxiv.org/abs/1312.6680); [Node-Weighted Triangles: Faster and Simpler](https://arxiv.org/abs/2605.08588).

## 8. Mark Braverman

[Research bibliography](https://dblp.org/pid/16/6136.html).

### 1. Constant-factor randomized direct sums for total Boolean functions

[TCS-5892](../../data/cards/TCS-5892.json) · reused · status: `source_open` · evidence: `reviewed`.

Randomized direct sums for total functions concern the amortized cost of interaction in his information-complexity work.

**Status scope:** A user-authorized precise total-Boolean-function variant. The August 2026 primary preprint explicitly distinguishes relations from the remaining total-function question. Rechecked on 13 September 2026; its new theorem is a reported preprint claim, not an independently verified result or a refutation of this target.

Sources: [Lifting Theorems for Equality](https://doi.org/10.4230/LIPIcs.STACS.2019.50); [Efficient Communication Using Partial Information](https://eccc.weizmann.ac.il/report/2010/083/); [Zero-error information equals amortized communication complexity](https://arxiv.org/abs/2608.04141).

### 2. Real Grothendieck constant

[TCS-7352](../../data/cards/TCS-7352.json) · added · status: `source_open` · evidence: `reviewed`.

He coauthored the breakthrough disproving Krivine's proposed value of the real Grothendieck constant.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [The Grothendieck constant is strictly smaller than Krivine’s bound](https://arxiv.org/abs/1103.6161); [New Lower and Upper Bounds for the Grothendieck Constant](https://arxiv.org/abs/2608.11158).

## 9. Subhash Khot

[Research bibliography](https://dblp.org/pid/25/1492.html).

### 1. Unique Games Conjecture

[TCS-0006](../../data/cards/TCS-0006.json) · reused · status: `source_open` · evidence: `reviewed`.

He introduced the Unique Games conjecture.

**Status scope:** The 2025 journal account distinguishes the proved 2-to-2 theorem from full UGC. No resolution of the quantified near-one-completeness statement was located in the primary-source search through 10 September 2026.

Sources: [On the Unique Games Conjecture](https://cs.nyu.edu/~khot/papers/UGCSurvey.pdf); [Optimal Algorithms and Inapproximability Results for Every CSP?](https://www.cs.cornell.edu/~abrahao/tdg/papers/p245.pdf); [Subexponential Algorithms for Unique Games and Related Problems](https://www.boazbarak.org/Papers/ssesubexp.pdf); [On the Proof of the 2-to-2 Games Conjecture](https://cs.nyu.edu/~khot/PCP-Spring-20/2-to-2-Exposition.pdf); [Towards a Proof of the 2-to-1 Games Conjecture](https://theoryofcomputing.org/articles/v021a011/).

### 2. Small-Set Expansion Hypothesis

[TCS-7160](../../data/cards/TCS-7160.json) · reused · status: `open` · evidence: `reviewed`.

Small-set expansion is a closely connected central hardness and geometry frontier.

**Status scope:** No proof or refutation located through 11 September 2026. The original exact-size regular-graph promise was checked separately from later weighted, volume and randomized variants. The August 2026 least-squares result is conditional on such a variant.

Sources: [Graph expansion and the unique games conjecture](https://doi.org/10.1145/1806689.1806792); [Wikipedia: Small set expansion hypothesis](https://en.wikipedia.org/wiki/Small_set_expansion_hypothesis); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1368726535); [Graph Expansion and the Unique Games Conjecture](https://www.dsteurer.org/paper/expansion.pdf); [Reductions Between Expansion Problems](https://arxiv.org/abs/1011.2586); [The Condition-Number Barrier in Sparse Least Squares](https://arxiv.org/abs/2608.02588).

## 10. Vinod Vaikuntanathan

[Research bibliography](https://dblp.org/pid/v/VinodVaikuntanathan.html).

### 1. Unleveled fully homomorphic encryption from LWE alone

[TCS-6551](../../data/cards/TCS-6551.json) · reused · status: `source_open` · evidence: `reviewed`.

Removing the additional assumption from unbounded-depth FHE directly extends his lattice-based FHE work.

**Status scope:** No classical unleveled compact FHE construction from the specified ordinary LWE assumption alone was found through 11 September 2026. Functional-encryption constructions use additional assumptions. The inspected February and April 2026 no-circularity proposals retain explicit level bounds; the latter also uses quantum evaluation. This card fixes polynomial-modulus LWE, nonuniform classical security and fresh-input FHE correctness.

Sources: [Efficient Fully Homomorphic Encryption from (Standard) LWE](https://epubs.siam.org/doi/10.1137/120868669); [Quantum FHE (Almost) As Secure As Classical](https://www.iacr.org/archive/crypto2018/10993383/10993383.pdf); [Fully Homomorphic Encryption: definitional issues and open problems](https://cseweb.ucsd.edu/classes/wi23/cse208-a/FHEorg.pdf); [Bootstrapping Homomorphic Encryption via Functional Encryption](https://eprint.iacr.org/2023/1376.pdf); [Bootstrapping Homomorphic Encryption via Functional Encryption — conference version](https://drops.dagstuhl.de/storage/00lipics/lipics-vol251-itcs2023/LIPIcs.ITCS.2023.17/LIPIcs.ITCS.2023.17.pdf); [Dynamic multi-key FHE without CRS from LWE](https://link.springer.com/article/10.1186/s42400-025-00431-z); [Efficient Quantum Fully Homomorphic Encryption](https://arxiv.org/abs/2604.23490).

### 2. Circuit obfuscation from polynomial-hard LWE

[TCS-6550](../../data/cards/TCS-6550.json) · reused · status: `source_open` · evidence: `reviewed`.

Basing iO on polynomial-hardness LWE alone is central to his lattice-cryptography program.

**Status scope:** Checked through 10 September 2026. No construction from the plain polynomial-hard decisional-LWE assumption fixed here was identified. Existing multi-assumption and circular-security constructions do not settle it. Polynomial hardness, polynomial modulus/noise ratio, classical adversaries, arbitrary circuits and no auxiliary leakage are explicit choices that make the broad LWE-alone question unambiguous.

Sources: [On the \((Im)\)possibility of Obfuscating Programs](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html); [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); [Indistinguishability Obfuscation from Well-Founded Assumptions](https://doi.org/10.1145/3785007); [Indistinguishability Obfuscation from LPN over \(F_{p}\), DLIN, and PRGs in \(\mathrm{NC}^{0}\)](https://eprint.iacr.org/2021/1334); [Factoring and Pairings Are Not Necessary for IO: Circular-Secure LWE Suffices](https://doi.org/10.4230/LIPIcs.ICALP.2022.28).

## 11. Aaron Sidford

[Research bibliography](https://dblp.org/pid/125/2326.html).

### 1. Strongly polynomial linear programming

[TCS-0008](../../data/cards/TCS-0008.json) · reused · status: `uncertain` · evidence: `reviewed`.

Strongly polynomial LP continues his work on faster general optimization.

**Status scope:** The standard problem remains listed as open, but a direct claimed solution exists in Awoniyi’s July 2026 revision. This card records it without treating it as established: correctness, the iteration bound, and the full strongly polynomial guarantee have not been independently validated in this review. Checked through 10 September 2026.

Sources: [Problem 8: Linear Programming: Strongly Polynomial?](https://topp.openproblem.net/p8); [A Strongly Polynomial Algorithm to Solve Combinatorial Linear Programs](https://doi.org/10.1287/opre.34.2.250); [A strongly polynomial algorithm for linear programs with at most two non-zero entries per row or column](https://homepages.cwi.nl/~dadush/papers/genflow.pdf); [No self-concordant barrier interior point method is strongly polynomial](https://arxiv.org/abs/2201.02186); [Trust Region Interior Point Methods: Optimal l2- and Faster Wide-Neighborhood Path Following](https://homepages.cwi.nl/~dadush/papers/trust-region.pdf); [A strongly polynomial-time algorithm for the general linear programming problem](https://arxiv.org/abs/2503.12041v10).

### 2. Exact directed maximum flow in \(O((m+n) \operatorname{polylog} n)\) time

[TCS-7228](../../data/cards/TCS-7228.json) · reused · status: `source_open` · evidence: `reviewed`.

Near-linear exact directed flow extends his flow and interior-point breakthroughs.

**Status scope:** Primary-source check through 11 September 2026 found almost-linear bounds, not the fixed-polylogarithmic overhead required here. New preprint proofs were not independently verified.

Sources: [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://arxiv.org/abs/2203.00671); [Maximum Flow Without the Outer IPM](https://arxiv.org/abs/2608.17384).

## 12. Ankur Moitra

[Research bibliography](https://dblp.org/pid/04/952.html).

### 1. Efficient learning of well-separated Gaussian mixtures

[TCS-3391](../../data/cards/TCS-3391.json) · reused · status: `uncertain` · evidence: `index`.

Efficient learning of separated Gaussian mixtures connects to his mixture-learning work.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [The EM Algorithm gives Sample-Optimality for Learning Mixtures of Well-Separated Gaussians](https://proceedings.mlr.press/v125/kwon20a.html).

### 2. Planted clique conjecture

[TCS-6656](../../data/cards/TCS-6656.json) · reused · status: `source_open` · evidence: `reviewed`.

Planted clique captures the computational-statistical gaps studied in his inference research.

**Status scope:** Checked through 10 September 2026; no unrestricted polynomial-time solution below \(n^{1/2- \varepsilon}\) or unconditional hardness proof was identified. The exact formulation fixes constant-success detection and exactly k planted vertices. Low-degree and sum-of-squares bounds remain scoped to their models; the optimal-advantage result is conditional.

Sources: [Finding a Large Hidden Clique in a Random Graph](https://people.math.ethz.ch/~sudakovb/hidden-clique.pdf); [A Nearly Tight Sum-of-Squares Lower Bound for the Planted Clique Problem](https://doi.org/10.1137/17M1138236); [Finding planted cliques using gradient descent](https://arxiv.org/abs/2311.07540v2); [On optimal distinguishers for Planted Clique](https://arxiv.org/abs/2505.01990v2); [Robust Algorithms for Finding Cliques in Random Intersection Graphs via Sum-of-Squares](https://proceedings.mlr.press/v336/gobel26a.html).

## 13. Yin Tat Lee

[Research bibliography](https://dblp.org/pid/125/2145.html).

### 1. Kannan–Lovász–Simonovits conjecture

[TCS-6523](../../data/cards/TCS-6523.json) · reused · status: `source_open` · evidence: `reviewed`.

KLS is central to the geometry behind his sampling and optimization work.

**Status scope:** The full KLS conjecture is explicitly open in the primary sources, including Letwin’s July 2026 preprint. Research through 10 September 2026 found no dimension-free general-function resolution. The recent quadratic-form and thin-shell results are not treated as proofs of the full conjecture; the July bound is labeled as a preprint result.

Sources: [The KLS Conjecture (problem 30)](https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/); [The Kannan–Lovász–Simonovits Conjecture](https://faculty.cc.gatech.edu/~vempala/papers/kls_survey.pdf); [Bourgain’s slicing problem and KLS isoperimetry up to polylog](https://arxiv.org/abs/2203.15551); [Logarithmic bounds for isoperimetry and slices of convex sets](https://www.weizmann.ac.il/math/klartag/sites/math.klartag/files/uploads/root_log.pdf); [Thin-shell bounds via parallel coupling](https://arxiv.org/abs/2507.15495v2); [The KLS constant is \(O(\log ^{1/4} n)\)](https://arxiv.org/abs/2607.24164v1).

### 2. Strongly polynomial linear programming

[TCS-0008](../../data/cards/TCS-0008.json) · reused · status: `uncertain` · evidence: `reviewed`.

Strongly polynomial LP is a fundamental frontier for his optimization algorithms.

**Status scope:** The standard problem remains listed as open, but a direct claimed solution exists in Awoniyi’s July 2026 revision. This card records it without treating it as established: correctness, the iteration bound, and the full strongly polynomial guarantee have not been independently validated in this review. Checked through 10 September 2026.

Sources: [Problem 8: Linear Programming: Strongly Polynomial?](https://topp.openproblem.net/p8); [A Strongly Polynomial Algorithm to Solve Combinatorial Linear Programs](https://doi.org/10.1287/opre.34.2.250); [A strongly polynomial algorithm for linear programs with at most two non-zero entries per row or column](https://homepages.cwi.nl/~dadush/papers/genflow.pdf); [No self-concordant barrier interior point method is strongly polynomial](https://arxiv.org/abs/2201.02186); [Trust Region Interior Point Methods: Optimal l2- and Faster Wide-Neighborhood Path Following](https://homepages.cwi.nl/~dadush/papers/trust-region.pdf); [A strongly polynomial-time algorithm for the general linear programming problem](https://arxiv.org/abs/2503.12041v10).

## 14. Shayan Oveis Gharan

[Research bibliography](https://dblp.org/pid/61/395.html).

### 1. Optimal polynomial-time approximation ratio for metric TSP

[TCS-7356](../../data/cards/TCS-7356.json) · added · status: `source_open` · evidence: `reviewed`.

The optimal algorithmic ratio extends his breakthrough below Christofides' factor.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [A (Slightly) Improved Approximation Algorithm for Metric TSP](https://arxiv.org/abs/2007.01409).

### 2. Fully polynomial randomized approximation of mixed discriminants

[TCS-7355](../../data/cards/TCS-7355.json) · added · status: `source_open` · evidence: `reviewed`.

Mixed discriminants connect his log-concavity and approximate-counting work.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [A polynomial time algorithm to approximate the mixed volume within a simply exponential factor](https://eccc.weizmann.ac.il/report/2007/037/revision/1/); [On the Complexity of Constrained Determinantal Point Processes](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2017.36).

## 15. Ilias Diakonikolas

[Research bibliography](https://dblp.org/pid/d/IliasDiakonikolas.html).

### 1. Polynomial-time learning of Gaussian mixtures

[TCS-5443](../../data/cards/TCS-5443.json) · reused · status: `uncertain` · evidence: `source`.

Efficient unrestricted Gaussian-mixture learning is directly within his distribution-learning program.

**Status scope:** Question recorded in a source from 2024; subsequent results and present open status have not been individually checked.

Sources: [Mixtures of Gaussians are Privately Learnable with a Polynomial Number of Samples](https://proceedings.mlr.press/v237/afzali24a.html).

### 2. Polynomial-time robust spectral estimation

[TCS-5087](../../data/cards/TCS-5087.json) · reused · status: `source_open` · evidence: `source`.

Robust spectral estimation is a substantial computational-statistical frontier in his robust learning research.

**Status scope:** Question recorded in a source from 2021; subsequent results and present open status have not been individually checked.

Sources: [Adversarially Robust Low Dimensional Representations](https://proceedings.mlr.press/v134/awasthi21a.html).

## 16. Daniel Kane

[Research bibliography](https://dblp.org/pid/52/6817.html).

### 1. Maximum influence of polynomial threshold functions

[TCS-6664](../../data/cards/TCS-6664.json) · reused · status: `source_open` · evidence: `reviewed`.

Influence of polynomial threshold functions relates directly to his Boolean-analysis work.

**Status scope:** Reviewed through 11 September 2026. The exact symmetric-maximizer conjecture is false, but the universal \(O(d\sqrt{n})\) influence bound remains open in the checked primary literature, including the April 2026 revisions on rational degree and Boolean surface area.

Sources: [The Gotsman–Linial Conjecture is False](https://arxiv.org/abs/2108.02288); [A Dual Perspective on Computational Complexity](https://dspace.mit.edu/server/api/core/bitstreams/7f2e32fd-d615-4dba-97be-f26cd30ca234/content); [The Correct Exponent for the Gotsman–Linial Conjecture](https://arxiv.org/abs/1210.1283); [On Graphs and the Gotsman–Linial Conjecture for \(d = 2\)](https://arxiv.org/abs/1709.06650); [The Boolean surface area of polynomial threshold functions](https://arxiv.org/abs/2604.08095); [Rational degree is polynomially related to degree](https://arxiv.org/abs/2601.08727).

### 2. Time complexity of Gaussian agnostic halfspace learning

[TCS-4592](../../data/cards/TCS-4592.json) · reused · status: `uncertain` · evidence: `index`.

Gaussian agnostic halfspace complexity connects his structural and algorithmic learning results.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Embedding Hard Learning Problems Into Gaussian Space](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2014.793).

## 17. David Woodruff

[Research bibliography](https://dblp.org/pid/w/DPWoodruff.html).

### 1. Input-sparsity relative spectral low-rank approximation

[TCS-7007](../../data/cards/TCS-7007.json) · reused · status: `source_open` · evidence: `source`.

Input-sparsity low-rank approximation extends his randomized numerical linear algebra.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2015 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357).

### 2. Optimal input-sparsity subspace embeddings

[TCS-7006](../../data/cards/TCS-7006.json) · reused · status: `source_open` · evidence: `source`.

Optimal input-sparsity subspace embeddings directly concern his sketching and numerical-linear-algebra work.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2015 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357).

## 18. Sanjeev Arora

[Research bibliography](https://dblp.org/pid/a/SArora.html).

### 1. Constant-factor approximation for Densest k-Subgraph

[TCS-6587](../../data/cards/TCS-6587.json) · reused · status: `source_open` · evidence: `reviewed`.

Densest k-subgraph is a major approximation barrier related to his approximation research.

**Status scope:** Checked through 10 September 2026. The constant-factor algorithm is already ruled out assuming ETH, which remains unproved. The May 2026 primary source explicitly notes the absence of NP-hardness of approximation even at factor 1.001. This card asks about a deterministic constant-factor algorithm on all unweighted graphs, and preserves the distinction between conditional evidence and an unconditional resolution.

Sources: [Detecting High Log-Densities — an \(O(n^{1}/4)\) Approximation for Densest k-Subgraph](https://arxiv.org/abs/1001.2891); [Polynomial integrality gaps for strong SDP relaxations of Densest k-subgraph](https://arxiv.org/abs/1110.1360); [Almost-Polynomial Ratio ETH-Hardness of Approximating Densest k-Subgraph](https://arxiv.org/abs/1611.05991); [A New Conjecture on Hardness of 2-CSP’s with Implications to Hardness of Densest k-Subgraph and Other Problems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2023.38); [A Scalable and Exact Relaxation for Densest k-Subgraph via Error Bounds](https://ojs.aaai.org/index.php/AAAI/article/view/38562); [A Note on Approximability of Densest At-Least-k-Subgraph](https://arxiv.org/abs/2605.25464).

### 2. Computational threshold for tensor PCA

[TCS-6657](../../data/cards/TCS-6657.json) · reused · status: `source_open` · evidence: `reviewed`.

Tensor PCA captures computational-statistical barriers relevant to his provable learning work.

**Status scope:** The May 2026 low-degree paper retains the conjectured gap for unrestricted algorithms and distinguishes spherical from independent-coordinate priors. The 2024 power-iteration and October 2025 stochastic-gradient improvements concern particular methods and do not provide a fixed-power improvement below \(n^{k/4}\). No full resolution found through 11 September 2026. The card explicitly fixes a finite-precision bit model; restricted lower bounds in the standard unrounded model are evidence, not a proof for all algorithms here.

Sources: [A statistical model for tensor PCA](https://arxiv.org/abs/1411.1076); [Sharp analysis of power iteration for tensor PCA](https://www.jmlr.org/papers/v25/24-0006.html); [Tensor cumulants for statistical inference on invariant distributions](https://arxiv.org/abs/2404.18735); [Near-Optimal Tensor PCA via Normalized Stochastic Gradient Ascent with Overparameterization](https://arxiv.org/abs/2510.14329); [Low-degree estimation thresholds in planted hypergraphs and tensor PCA](https://arxiv.org/abs/2605.30113).

## 19. Constantinos Daskalakis

[Research bibliography](https://dblp.org/pid/d/ConstantinosDaskalakis.html).

### 1. CLS versus FP

[TCS-7286](../../data/cards/TCS-7286.json) · reused · status: `source_open` · evidence: `reviewed`.

CLS versus FP connects continuous optimization, equilibrium computation and his total-search work.

**Status scope:** The source establishes the class equality but does not decide polynomial-time solvability. The individual discrete specification was rechecked on 13 September 2026 against the locally saved full paper. The prior 11 September status search and a small follow-up search supplied no verified resolution; the latter was inconclusive, so status remains source_open rather than a claim of exhaustive current verification.

Sources: [The Complexity of Gradient Descent: CLS = PPAD ∩ PLS](https://arxiv.org/abs/2011.01929).

### 2. Efficient learning of well-separated Gaussian mixtures

[TCS-3391](../../data/cards/TCS-3391.json) · reused · status: `uncertain` · evidence: `index`.

Efficient Gaussian-mixture learning relates to his algorithmic statistics program.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [The EM Algorithm gives Sample-Optimality for Learning Mixtures of Well-Separated Gaussians](https://proceedings.mlr.press/v125/kwon20a.html).

## 20. Prasad Raghavendra

[Research bibliography](https://dblp.org/pid/69/3746.html).

### 1. Small-Set Expansion Hypothesis

[TCS-7160](../../data/cards/TCS-7160.json) · reused · status: `open` · evidence: `reviewed`.

He co-introduced the Small-Set Expansion hypothesis.

**Status scope:** No proof or refutation located through 11 September 2026. The original exact-size regular-graph promise was checked separately from later weighted, volume and randomized variants. The August 2026 least-squares result is conditional on such a variant.

Sources: [Graph expansion and the unique games conjecture](https://doi.org/10.1145/1806689.1806792); [Wikipedia: Small set expansion hypothesis](https://en.wikipedia.org/wiki/Small_set_expansion_hypothesis); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1368726535); [Graph Expansion and the Unique Games Conjecture](https://www.dsteurer.org/paper/expansion.pdf); [Reductions Between Expansion Problems](https://arxiv.org/abs/1011.2586); [The Condition-Number Barrier in Sparse Least Squares](https://arxiv.org/abs/2608.02588).

### 2. Unconditional NP-hardness at the Goemans–Williamson Max-Cut threshold

[TCS-7281](../../data/cards/TCS-7281.json) · reused · status: `source_open` · evidence: `reviewed`.

Unconditional Max-Cut hardness probes the limits of his CSP and SDP approximation theory.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Optimal Inapproximability Results for MAX-CUT and Other 2-Variable CSPs](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/07/Optimal_Inapproximability_Results_for_MAX_CUT_and_Other_2_Variable_CSPs_1.pdf).

## 21. Oded Regev

[Research bibliography](https://dblp.org/pid/r/OdedRegev.html).

### 1. Dihedral hidden subgroup problem in BQP

[TCS-6521](../../data/cards/TCS-6521.json) · reused · status: `uncertain` · evidence: `reviewed`.

Dihedral HSP links his quantum algorithms to lattice and subset-sum problems.

**Status scope:** Reviewed through 11 September 2026. No verified polynomial-time solution is recorded. Simon’s August 2026 coset-algorithm claim is disputed: the September 1 Gupte–Ragavan–Zhandry response proves failure of the proposed template, and Guo–Yang identify an unsupported independence hypothesis. The review checked these primary statements without independently rerunning the Lean development. The 2022 Moore–Young claim was explicitly withdrawn.

Sources: [Another subexponential-time quantum algorithm for the dihedral hidden subgroup problem](https://arxiv.org/abs/1112.3333); [A Subexponential-Time Quantum Algorithm for the Dihedral Hidden Subgroup Problem](https://epubs.siam.org/doi/10.1137/S0097539703436345); [The dihedral hidden subgroup problem](https://arxiv.org/abs/2106.09907); [A Subexponential Time Algorithm for the Dihedral Hidden Subgroup Problem with Polynomial Space](https://arxiv.org/abs/quant-ph/0406151); [Quantum Computation and Lattice Problems](https://cims.nyu.edu/~regev/papers/quantum_average.pdf); [A Quantum Polynomial-Time Solution to The Dihedral Hidden Subgroup Problem](https://arxiv.org/abs/2202.09697); [A Polynomial-Time Quantum Algorithm for the Dihedral Coset Problem](https://eprint.iacr.org/2026/1591); [The ePrint:\(2026/1591\) Quantum Algorithm Does Not Solve DCP](https://eprint.iacr.org/2026/1693); [Rigorous Statements and Proofs of the Lemmas in Simon's Algorithm for the Dihedral Coset Problem and Their Underlying Hypothesis](https://arxiv.org/abs/2608.16598); [The Hidden Subgroup Problem in Semidirect Products and Quasi-Hamiltonian Groups](https://arxiv.org/abs/2608.05321).

### 2. Classical reductions matching quantum LWE hardness

[TCS-6861](../../data/cards/TCS-6861.json) · reused · status: `source_open` · evidence: `source`.

A classical worst-case reduction for LWE directly concerns the quantum reduction he introduced.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2016 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939).

## 22. Yael Tauman Kalai

[Research bibliography](https://dblp.org/pid/k/YaelTaumanKalai.html).

### 1. Noninteractive zero knowledge from one-way functions

[TCS-6552](../../data/cards/TCS-6552.json) · reused · status: `source_open` · evidence: `reviewed`.

Minimal assumptions for noninteractive zero knowledge connect her cryptographic proof systems.

**Status scope:** No construction of reusable adaptive NIZK arguments from ordinary OWFs alone, or refutation of that unrestricted implication, was found through 11 September 2026. The cited BARG, trapdoor-hash and derandomization constructions retain extra assumptions; recent OWF-only succinct proofs are interactive, and high-error characterizations run in the reverse direction.

Sources: [Commitment Schemes and Zero-Knowledge Protocols (2011)](https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf); [Noninteractive Zero Knowledge for NP from (Plain) Learning With Errors](https://web.eecs.umich.edu/~cpeikert/pubs/nizk-lwe.pdf); [Batch Arguments to NIZKs from One-Way Functions](https://eprint.iacr.org/2023/1938); [Black-Box Non-Interactive Zero Knowledge from Vector Trapdoor Hash](https://eprint.iacr.org/2024/1514); [Fiat-Shamir in the Plain Model from Derandomization (Or: Do Efficient Algorithms Believe that \(\mathrm{NP} = \mathrm{PSPACE}\)?)](https://eccc.weizmann.ac.il/report/2024/116/); [Non-Trivial Zero-Knowledge Implies One-Way Functions](https://arxiv.org/abs/2602.17651); [Succinct Zero-Knowledge Proofs from One-Way Functions: The Blackbox Way](https://doi.org/10.1007/978-3-032-35424-2_6).

### 2. Oblivious transfer from public-key encryption

[TCS-6549](../../data/cards/TCS-6549.json) · reused · status: `source_open` · evidence: `reviewed`.

Obtaining OT from general public-key encryption concerns the foundations of secure computation she studies.

**Status scope:** Checked through 10 September 2026. No unrestricted classical implication from arbitrary IND-CPA public-key encryption to OT was identified. Known oracle/black-box separations and positive results for rerandomizable or suitably samplable encryption do not settle this formulation. The card fixes semi-honest standalone security with classical communication and no setup.

Sources: [The Relationship between Public Key Encryption and Oblivious Transfer](https://vmahesh.cs.illinois.edu/papers/focs00.pdf); [Black-Box Constructions of Protocols for Secure Computation](https://iftachh.github.io/MyHomepage/papers/BlackBoxMPC/black-box-mpc.pdf); [Computational Hardness of Optimal FairComputation: Beyond Minicrypt](https://eprint.iacr.org/2021/882); [Oblivious Transfer from Rerandomizable PKE](https://eprint.iacr.org/2023/1002); [On the Implications from Updatable Encryption to Public-Key Cryptographic Primitives](https://doi.org/10.1587/transfun.2025CIP0019).

## 23. Shachar Lovett

[Research bibliography](https://dblp.org/pid/77/4422.html).

### 1. Log-rank conjecture

[TCS-6603](../../data/cards/TCS-6603.json) · reused · status: `source_open` · evidence: `reviewed`.

Log-rank is central to his communication-complexity work.

**Status scope:** Explicitly open in the August 2026 CCC version of Hambardzumyan–Lovett–Shirley. Checked through 10 September 2026. The established general upper bound is \(O(\sqrt{r})\); recent fixed-polynomial lower-bound refinements and signed-decomposition equivalences do not settle the conjecture.

Sources: [The Log-Rank Conjecture: New Equivalent Formulations](https://arxiv.org/abs/2510.02583v3); [Matrix discrepancy and the log-rank conjecture](https://doi.org/10.1007/s10107-024-02117-9); [Deterministic Communication vs. Partition Number](https://doi.org/10.1137/16M1059369); [Alphabet-Preserving Lifting for the Log-Rank Conjecture](https://arxiv.org/abs/2608.01812v1).

### 2. Two-source extraction at log n plus constant entropy

[TCS-7271](../../data/cards/TCS-7271.json) · reused · status: `source_open` · evidence: `reviewed`.

Optimal-entropy extraction relates to his pseudorandomness and additive-combinatorics work.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Two Source Extractors for Asymptotically Optimal Entropy, and (Many) More](https://arxiv.org/abs/2303.06802).

## 24. Dor Minzer

[Research bibliography](https://dblp.org/pid/161/4102.html).

### 1. Sliding-scale PCP conjecture

[TCS-7268](../../data/cards/TCS-7268.json) · reused · status: `source_open` · evidence: `reviewed`.

PCP parameter tradeoffs are directly related to his hardness-of-approximation results.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Polynomially Low Error PCPs with polyloglog n Queries via Modular Composition](https://arxiv.org/abs/1505.06362).

### 2. Unique Games Conjecture

[TCS-0006](../../data/cards/TCS-0006.json) · reused · status: `source_open` · evidence: `reviewed`.

Unique Games connects his Boolean-analysis, expansion and hardness work.

**Status scope:** The 2025 journal account distinguishes the proved 2-to-2 theorem from full UGC. No resolution of the quantified near-one-completeness statement was located in the primary-source search through 10 September 2026.

Sources: [On the Unique Games Conjecture](https://cs.nyu.edu/~khot/papers/UGCSurvey.pdf); [Optimal Algorithms and Inapproximability Results for Every CSP?](https://www.cs.cornell.edu/~abrahao/tdg/papers/p245.pdf); [Subexponential Algorithms for Unique Games and Related Problems](https://www.boazbarak.org/Papers/ssesubexp.pdf); [On the Proof of the 2-to-2 Games Conjecture](https://cs.nyu.edu/~khot/PCP-Spring-20/2-to-2-Exposition.pdf); [Towards a Proof of the 2-to-1 Games Conjecture](https://theoryofcomputing.org/articles/v021a011/).

## 25. Thatchaphol Saranurak

[Research bibliography](https://dblp.org/pid/123/4694.html).

### 1. Almost-linear directed vertex connectivity

[TCS-7345](../../data/cards/TCS-7345.json) · reused · status: `source_open` · evidence: `reviewed`.

Directed vertex connectivity continues his expander-decomposition and graph-algorithm program.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. Editorial exact endpoint with randomization allowed. The at-most-one-vertex convention completes the separator definition on complete bidirected graphs; it does not affect the unresolved general regime.

Sources: [Faster Algorithms for Global Minimum Vertex-Cut in Directed Graphs](https://arxiv.org/abs/2512.24355); [Approximating Directed Connectivity in Almost-Linear Time](https://arxiv.org/abs/2512.00176); [Krajinou grafových algoritmů](https://mj.ucw.cz/vyuka/ga/ga.pdf).

### 2. Strongly polynomial near-linear negative-weight shortest paths

[TCS-7341](../../data/cards/TCS-7341.json) · reused · status: `source_open` · evidence: `reviewed`.

Strongly polynomial fast negative-weight SSSP directly extends his shortest-path work.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. The approved real-weight formulation of the strong-polynomial endpoint fixes bounded error and worst-case operation cost. It is not the solved near-linear integer-weight question.

Sources: [Negative-Weight Single-Source Shortest Paths in Near-Linear Time: Now Faster!](https://arxiv.org/abs/2304.05279); [Negative-Weight Single-Source Shortest Paths in Near-linear Time](https://arxiv.org/abs/2203.03456); [Deterministic Negative-Weight Shortest Paths in Nearly Linear Time via Path Covers](https://arxiv.org/abs/2511.08551); [Bellman-Ford in Almost-Linear Time for Dense Graphs](https://arxiv.org/abs/2602.16153); [Krajinou grafových algoritmů](https://mj.ucw.cz/vyuka/ga/ga.pdf).

## 26. Lijie Chen

[Research bibliography](https://dblp.org/pid/116/0948-1.html).

### 1. NEXP versus nonuniform \(\mathrm{TC}^{0}\)

[TCS-7161](../../data/cards/TCS-7161.json) · reused · status: `open` · evidence: `reviewed`.

NEXP versus TC0 is a natural next frontier in his circuit-lower-bound research.

**Status scope:** No \(\mathrm{NEXP}\not\subset \mathrm{TC}^{0}\) resolution found through 11 September 2026. The checked March, July and September results retain different hard-language models or fixed depth and polynomial quantitative bounds. The September preprint has a source comment raising concerns and is recorded as an unverified claim.

Sources: [Non-Uniform ACC Circuit Lower Bounds](https://doi.org/10.1109/CCC.2011.36); [Wikipedia: Circuit complexity](https://en.wikipedia.org/wiki/Circuit_complexity); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1328197464); [Non-Uniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-ccc.pdf); [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/); [Almost-Everywhere Near-Cubic Wire Lower Bounds for SYM ∘ THR and \(\mathrm{THR} \circ  \mathrm{THR}\)](https://eccc.weizmann.ac.il/report/2026/167/); [Near-Maximum Circuit Lower Bounds for Exponential Time with Merlin-Arthur Queries](https://eccc.weizmann.ac.il/report/2026/118/).

### 2. Complexity of Minimum Circuit Size

[TCS-4786](../../data/cards/TCS-4786.json) · reused · status: `uncertain` · evidence: `source`.

MCSP is central to his work on meta-complexity and hardness magnification.

**Status scope:** Question recorded in a source from 2023; subsequent results and present open status have not been individually checked.

Sources: [Synergy Between Circuit Obfuscation and Circuit Minimization](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.31); [Simple Circuit Extensions for XOR in PTIME](https://doi.org/10.4230/LIPIcs.STACS.2026.23); [Sum-Of-Squares Lower Bounds for the Minimum Circuit Size Problem](https://doi.org/10.4230/LIPIcs.CCC.2023.31).

## 27. Moses Charikar

[Research bibliography](https://dblp.org/pid/c/MosesCharikar.html).

### 1. Optimal polynomial-time approximation ratio for Euclidean k-means

[TCS-7353](../../data/cards/TCS-7353.json) · added · status: `source_open` · evidence: `reviewed`.

Optimal Euclidean clustering approximation directly extends his k-means algorithms, including 2026 work.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654); [A (4 + epsilon)-Approximation for Euclidean k-Means via Non-Monotone Dual-Fitting](https://doi.org/10.1145/3798129.3800894).

### 2. Constant-factor approximation for Dasgupta’s hierarchical clustering objective

[TCS-7318](../../data/cards/TCS-7318.json) · reused · status: `source_open` · evidence: `reviewed`.

Hierarchical clustering approximability is directly connected to his clustering research.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. The question is the unrestricted graph objective. No data stability or external clustering oracle is assumed.

Sources: [A cost function for similarity-based hierarchical clustering](https://arxiv.org/abs/1510.05043); [Approximate Hierarchical Clustering via Sparsest Cut and Spreading Metrics](https://arxiv.org/abs/1609.09548).

## 28. László Babai

[Research bibliography](https://dblp.org/pid/b/LaszloBabai.html).

### 1. Graph isomorphism in polynomial time

[TCS-7222](../../data/cards/TCS-7222.json) · reused · status: `source_open` · evidence: `reviewed`.

Polynomial-time graph isomorphism is the main frontier after his quasipolynomial algorithm.

**Status scope:** Reviewed through 11 September 2026. Babai’s deterministic quasipolynomial algorithm remains the best general worst-case bound located; no polynomial-time algorithm or unconditional exclusion of one was found.

Sources: [Graph Isomorphism in Quasipolynomial Time](https://arxiv.org/abs/1512.03547); [Groups, Graphs, Algorithms: The Graph Isomorphism Problem](https://people.cs.uchicago.edu/~laci/papers/icm18-babai.pdf); [Parameterized complexity of graph isomorphism testing](https://www.sciencedirect.com/science/article/pii/S1574013726000274); [Fractional Homomorphism, Weisfeiler-Leman Invariance, and the Sherali-Adams Hierarchy for the Constraint Satisfaction Problem](https://doi.org/10.4230/LIPIcs.MFCS.2021.27); [On the Relative Power of Linear Algebraic Approximations of Graph Isomorphism](https://doi.org/10.4230/LIPIcs.MFCS.2021.37).

### 2. Graph canonization versus graph isomorphism

[TCS-7180](../../data/cards/TCS-7180.json) · reused · status: `source_open` · evidence: `reviewed`.

Canonization versus isomorphism directly concerns his group-theoretic graph algorithms.

**Status scope:** The reverse relation is open in the checked 2019 primary discussion. The reviewed ICALP 2026 result concerns random regular graphs and does not settle the general reduction. Searches through 11 September 2026 found no established resolution; this is not an independent audit of all later work.

Sources: [Canonical Form for Graphs in Quasipolynomial Time](https://par.nsf.gov/servlets/purl/10179675); [Wikipedia: Graph canonization](https://en.wikipedia.org/wiki/Graph_canonization); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1330143987); [Canonical Labelling of Random Regular Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.114).

## 29. Thomas Rothvoss

[Research bibliography](https://dblp.org/pid/10/1896.html).

### 1. Superpolynomial semidefinite extension complexity of perfect matching

[TCS-7283](../../data/cards/TCS-7283.json) · reused · status: `source_open` · evidence: `reviewed`.

SDP extension complexity continues his lower bounds for matching formulations.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Lower Bounds for Interactive Compression and Linear Programs](https://digital.lib.washington.edu/server/api/core/bitstreams/a7ac9607-c4f8-4d56-9b29-0f5ef033975d/content).

### 2. Beck–Fiala conjecture

[TCS-7315](../../data/cards/TCS-7315.json) · reused · status: `source_open` · evidence: `reviewed`.

Beck-Fiala connects his discrepancy and integer-optimization work.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. TCS-5224 concerned a particular route to a known range of Beck–Fiala, not the full conjecture admitted here.

Sources: [Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk](https://arxiv.org/abs/2508.03961); [Online Beck--Fiala Down to Logarithmic Sparsity](https://arxiv.org/abs/2607.14238).

## 30. Madhu Sudan

[Research bibliography](https://dblp.org/pid/s/MadhuSudan.html).

### 1. Polynomial-length constant-query locally decodable codes

[TCS-1020](../../data/cards/TCS-1020.json) · reused · status: `uncertain` · evidence: `index`.

Constant-query local decoding extends his foundational coding work.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

### 2. Full-length Reed–Solomon list decoding beyond Johnson

[TCS-1011](../../data/cards/TCS-1011.json) · reused · status: `uncertain` · evidence: `index`.

Reed-Solomon list decoding directly follows his algebraic list-decoding contributions.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 31. Nima Anari

[Research bibliography](https://dblp.org/pid/60/8821.html).

### 1. Fully polynomial randomized approximation of mixed discriminants

[TCS-7355](../../data/cards/TCS-7355.json) · added · status: `source_open` · evidence: `reviewed`.

Mixed-discriminant approximation extends his log-concavity and partition-constrained sampling work.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [A polynomial time algorithm to approximate the mixed volume within a simply exponential factor](https://eccc.weizmann.ac.il/report/2007/037/revision/1/); [On the Complexity of Constrained Determinantal Point Processes](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2017.36).

### 2. FPRAS for counting perfect matchings

[TCS-6628](../../data/cards/TCS-6628.json) · reused · status: `source_open` · evidence: `reviewed`.

General perfect-matching counting is a major next barrier for his sampling and counting methods.

**Status scope:** Checked through 10 September 2026. The general-graph question remains open in the checked primary literature. The August 2026 improvement is a permanent algorithm for bipartite graphs. Slow mixing of the particular general-graph Markov chains does not establish impossibility of all FPRAS approaches.

Sources: [Approximating the Permanent](https://doi.org/10.1137/0218077); [A Polynomial-Time Approximation Algorithm for the Permanent of a Matrix with Nonnegative Entries](https://faculty.cc.gatech.edu/~vigoda/Permanent.pdf); [On Counting Perfect Matchings in General Graphs](https://arxiv.org/abs/1712.07504); [Two-State Spin Systems with Negative Interactions](https://arxiv.org/abs/2309.04735); [Faster FPRAS for the Permanent via Restricted Poincaré Inequalities and Coupled Flows](https://arxiv.org/abs/2608.26599).

## 32. Julia Chuzhoy

[Research bibliography](https://dblp.org/pid/99/3386.html).

### 1. Optimal bounds in the Excluded Grid Theorem

[TCS-6683](../../data/cards/TCS-6683.json) · reused · status: `source_open` · evidence: `reviewed`.

Quantitative excluded-grid bounds are directly within her graph-minor research.

**Status scope:** The checked general bounds remain \(\Omega (r^{2} \log  r)\) and \(O(r^{9} \operatorname{polylog} r)\). The November 2025 product-structure result and SODA 2026 fixed-minor result refine different aspects and do not determine the all-graphs threshold. No matching asymptotic bounds found through 11 September 2026. The problem does not assume that either the near-quadratic or cubic conjecture is correct.

Sources: [Graph minors. V. Excluding a planar graph](https://doi.org/10.1016/0095-8956(86)90030-4); [Quickly Excluding a Planar Graph](https://www.sciencedirect.com/science/article/pii/S0095895684710732); [Polynomial Bounds for the Grid-Minor Theorem](https://arxiv.org/abs/1305.6577); [Towards \(Tight(er)\) Bounds for the Excluded Grid Theorem](https://arxiv.org/abs/1901.07944); [The Grid-Minor Theorem Revisited](https://link.springer.com/article/10.1007/s00493-025-00168-w); [Catching Rats in H-minor-free Graphs](https://arxiv.org/abs/2506.22857).

### 2. Polylogarithmic approximation for Directed Steiner Tree

[TCS-6588](../../data/cards/TCS-6588.json) · reused · status: `source_open` · evidence: `reviewed`.

Directed Steiner Tree concerns the routing and network-design barriers she studies.

**Status scope:** The July 2026 primary literature explicitly leaves this general-graph question open. The inherited 2024 claim was withdrawn, and its October 2025 replacement is restricted to a special supplied fractional solution; that claim is not counted as an established general result. Planar and quasipolynomial algorithms do not satisfy this card. Checked through 11 September 2026.

Sources: [Approximation Algorithms for Directed Steiner Problems](https://chekuri.web.engr.illinois.edu/pub.html); [\(O(\log ^{2} k/\log  \log  k)\)-Approximation Algorithm for Directed Steiner Tree: A Tight Quasi-Polynomial-Time Algorithm](https://people.idsia.ch/~grandoni/Pubblicazioni/GLL19stoc.pdf); [An \(O(\log  k)\)-Approximation for Directed Steiner Tree in Planar Graphs](https://arxiv.org/abs/2302.04747); [From Directed Steiner Tree to Directed Polymatroid Steiner Tree in Planar Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.42); [On the Integrality Gap of Directed Steiner Tree LPs with Relatively Integral Solutions](https://arxiv.org/abs/2412.10744); [Length-Constrained Network Design in Planar Digraphs](https://arxiv.org/abs/2607.25811).

## 33. Mohsen Ghaffari

[Research bibliography](https://dblp.org/pid/33/5673.html).

### 1. Sublogarithmic distributed MIS

[TCS-6499](../../data/cards/TCS-6499.json) · reused · status: `open` · evidence: `reviewed`.

Distributed MIS is a central target of his LOCAL-model work.

**Status scope:** Reviewed 10 September 2026. General-graph sublogarithmic elapsed-round complexity remains open in the checked literature; awake-time and high-girth results have different guarantees.

Sources: [Breaking Barriers for Distributed MIS by Faster Degree Reduction](https://arxiv.org/abs/2505.15652); [An Improved Distributed Algorithm for Maximal Independent Set](https://arxiv.org/abs/1506.05093); [Round Elimination via Self-Reduction: Closing Gaps for Distributed Maximal Matching](https://arxiv.org/abs/2505.15654).

### 2. Constant-round MIS in the congested clique

[TCS-6501](../../data/cards/TCS-6501.json) · reused · status: `open` · evidence: `reviewed`.

Constant-round congested-clique MIS extends his distributed graph algorithms.

**Status scope:** Reviewed 10 September 2026. Constant-round MIS on arbitrary input graphs remains open in the checked literature.

Sources: [When MIS and Maximal Matching are Easy in the Congested Clique](https://arxiv.org/abs/2502.21031); [Improved Massively Parallel Computation Algorithms for MIS, Matching, and Vertex Cover](https://arxiv.org/abs/1802.08237); [Time and Space Optimal Massively Parallel Algorithm for the 2-Ruling Set Problem](https://doi.org/10.4230/LIPIcs.DISC.2023.11).

## 34. Danupon Nanongkai

[Research bibliography](https://dblp.org/pid/61/2421.html).

### 1. Strongly polynomial near-linear negative-weight shortest paths

[TCS-7341](../../data/cards/TCS-7341.json) · reused · status: `source_open` · evidence: `reviewed`.

Strongly polynomial fast SSSP continues his shortest-path breakthroughs.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. The approved real-weight formulation of the strong-polynomial endpoint fixes bounded error and worst-case operation cost. It is not the solved near-linear integer-weight question.

Sources: [Negative-Weight Single-Source Shortest Paths in Near-Linear Time: Now Faster!](https://arxiv.org/abs/2304.05279); [Negative-Weight Single-Source Shortest Paths in Near-linear Time](https://arxiv.org/abs/2203.03456); [Deterministic Negative-Weight Shortest Paths in Nearly Linear Time via Path Covers](https://arxiv.org/abs/2511.08551); [Bellman-Ford in Almost-Linear Time for Dense Graphs](https://arxiv.org/abs/2602.16153); [Krajinou grafových algoritmů](https://mj.ucw.cz/vyuka/ga/ga.pdf).

### 2. Work-efficient parallel directed reachability

[TCS-6507](../../data/cards/TCS-6507.json) · reused · status: `open` · evidence: `reviewed`.

Work-efficient directed reachability concerns his parallel and distributed graph program.

**Status scope:** Reviewed 10 September 2026, including the August 2026 closure-sensitive algorithm. Near-linear input work with polylogarithmic depth remains the target.

Sources: [Parallel Reachability and Shortest Paths on Non-Sparse Digraphs: Near-Linear Work and Sub-Square-Root Depth](https://doi.org/10.4230/LIPIcs.ICALP.2026.15); [Parallel Reachability in Almost Linear Work and Square Root Depth](https://arxiv.org/abs/1905.08841); [Õ(1)-Depth Parallel Reachability Faster than Transitive Closure](https://arxiv.org/abs/2608.13231).

## 35. Richard Peng

[Research bibliography](https://dblp.org/pid/46/7997.html).

### 1. Exact directed maximum flow in \(O((m+n) \operatorname{polylog} n)\) time

[TCS-7228](../../data/cards/TCS-7228.json) · reused · status: `source_open` · evidence: `reviewed`.

Near-linear exact max flow extends his work on fast graph optimization.

**Status scope:** Primary-source check through 11 September 2026 found almost-linear bounds, not the fixed-polylogarithmic overhead required here. New preprint proofs were not independently verified.

Sources: [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://arxiv.org/abs/2203.00671); [Maximum Flow Without the Outer IPM](https://arxiv.org/abs/2608.17384).

### 2. Nearly linear-time solution of general sparse linear systems

[TCS-6585](../../data/cards/TCS-6585.json) · reused · status: `source_open` · evidence: `reviewed`.

General sparse systems broaden his Laplacian and numerical-linear-algebra methods.

**Status scope:** Checked through 10 September 2026. This is an editorial, fully specified near-linear target in the polynomial-conditioning and precision regime, not a named positive conjecture. The faster-than-matrix-multiplication problem has already been solved. The August 2026 report discusses broader scalable solvers but does not claim this universal guarantee; the simplicial-Laplacian reduction is not a general running-time lower bound.

Sources: [Solving Sparse Linear Systems Faster than Matrix Multiplication](https://arxiv.org/abs/2007.10254); [Nearly Linear Time Algorithms for Preconditioning and Solving Symmetric, Diagonally Dominant Linear Systems](https://epubs.siam.org/doi/10.1137/090771430); [Matrix anti-concentration inequalities with applications](https://arxiv.org/abs/2111.05553); [Hardness Results for Laplacians of Simplicial Complexes via Sparse-Linear Equation Complete Gadgets](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.53); [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394).

## 36. Thomas Vidick

[Research bibliography](https://dblp.org/pid/94/6173.html).

### 1. Quantum PCP conjecture

[TCS-6446](../../data/cards/TCS-6446.json) · reused · status: `source_open` · evidence: `reviewed`.

Quantum PCP is central to his quantum verification and Hamiltonian-complexity research.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495); [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/).

### 2. Asymptotically good quantum locally testable stabilizer codes

[TCS-6515](../../data/cards/TCS-6515.json) · reused · status: `source_open` · evidence: `reviewed`.

Good quantum locally testable codes connect his quantum coding and Hamiltonian-complexity research.

**Status scope:** Checked through 11 September 2026. No bounded-degree stabilizer family with constant rate, relative distance and normalized soundness was located. The corrected 2025 and July 2026 constructions retain inverse-polylogarithmic losses, while constant-soundness variants increase locality or sacrifice other parameters.

Sources: [Quantum Locally Testable Code with Constant Soundness](https://quantum-journal.org/papers/q-2024-10-18-1501/); [Asymptotically Good Quantum and Locally Testable Classical LDPC Codes](https://arxiv.org/abs/2111.03654); [Local testability of distance-balanced quantum codes](https://www.nature.com/articles/s41534-024-00908-8); [Expansion of higher-dimensional cubical complexes with application to quantum locally testable codes](https://arxiv.org/abs/2402.07476); [NLTS Hamiltonians from Good Quantum Codes](https://arxiv.org/abs/2206.13228); [Transversal non-Clifford gates on almost-good quantum LDPC and quantum locally testable codes](https://arxiv.org/abs/2604.01874); [Probabilistically Checking Quantum Proofs, with Interaction](https://arxiv.org/abs/2606.09588).

## 37. Amit Sahai

[Research bibliography](https://dblp.org/pid/s/AmitSahai.html).

### 1. Circuit obfuscation from polynomial-hard LWE

[TCS-6550](../../data/cards/TCS-6550.json) · reused · status: `source_open` · evidence: `reviewed`.

iO from LWE alone is central to his obfuscation research.

**Status scope:** Checked through 10 September 2026. No construction from the plain polynomial-hard decisional-LWE assumption fixed here was identified. Existing multi-assumption and circular-security constructions do not settle it. Polynomial hardness, polynomial modulus/noise ratio, classical adversaries, arbitrary circuits and no auxiliary leakage are explicit choices that make the broad LWE-alone question unambiguous.

Sources: [On the \((Im)\)possibility of Obfuscating Programs](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html); [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); [Indistinguishability Obfuscation from Well-Founded Assumptions](https://doi.org/10.1145/3785007); [Indistinguishability Obfuscation from LPN over \(F_{p}\), DLIN, and PRGs in \(\mathrm{NC}^{0}\)](https://eprint.iacr.org/2021/1334); [Factoring and Pairings Are Not Necessary for IO: Circular-Secure LWE Suffices](https://doi.org/10.4230/LIPIcs.ICALP.2022.28).

### 2. Identity-based encryption from arbitrary public-key encryption

[TCS-7278](../../data/cards/TCS-7278.json) · reused · status: `source_open` · evidence: `reviewed`.

Identity-based encryption from general PKE connects his functional-encryption and assumption-reduction work.

**Status scope:** The primary 2021 source supplies a generic-group barrier and does not refute the unrestricted implication. Formulation and barrier scope were checked on 13 September 2026; the bounded saved later-work review did not identify a general resolution. The foundational security definition uses the earlier recorded read.

Sources: [Generic-Group Identity-Based Encryption: A Tight Impossibility Result](https://eprint.iacr.org/2021/745.pdf); [Identity-Based Encryption from the Weil Pairing](https://crypto.stanford.edu/~dabo/pubs/papers/bfibe.pdf).

## 38. Tim Roughgarden

[Research bibliography](https://dblp.org/pid/r/TimRoughgarden.html).

### 1. Constant-factor universally truthful auctions for submodular bidders

[TCS-6632](../../data/cards/TCS-6632.json) · reused · status: `source_open` · evidence: `reviewed`.

Truthful welfare maximization concerns the algorithm-versus-incentives barriers he studies.

**Status scope:** The checked primary literature retains a gap between constant nontruthful welfare approximation and the general universally truthful guarantee. Theorem 2 of the SODA 2021 paper supplies \(O((\log  \log  m)^{2})\) for submodular bidders. The 2026 graph-auction results impose eligibility restrictions. No general constant-factor resolution found through 11 September 2026. The public per-value precision parameter makes the inherited polynomial-communication question explicit in bits.

Sources: [Improved Truthful Mechanisms for Combinatorial Auctions with Submodular Bidders](https://epubs.siam.org/doi/10.1137/20M1316068); [On the Power of Randomization in Algorithmic Mechanism Design](https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf); [An Impossibility Result for Truthful Combinatorial Auctions with Submodular Valuations](https://arxiv.org/abs/1011.1830); [Improved Truthful Mechanisms for Subadditive Combinatorial Auctions: Breaking the Logarithmic Barrier](https://arxiv.org/abs/2010.01420); [The Communication Complexity of Combinatorial Auctions in Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.27).

### 2. Randomized truthful unrelated-machine scheduling

[TCS-6674](../../data/cards/TCS-6674.json) · reused · status: `source_open` · evidence: `reviewed`.

Randomized truthful scheduling is a foundational approximation-mechanism target in his field.

**Status scope:** The Nisan–Ronen proof, now published in JACM in February 2026, resolves only deterministic truthful mechanisms. Its randomized discussion records \(2- 1/m\) and \((m+5)/2\) bounds. Searches through 11 September 2026 found no matching unrestricted randomized bounds; results for task-independent mechanisms, fractional objectives, Bayesian types or no-payment models do not resolve this formulation.

Sources: [A proof of the Nisan–Ronen conjecture](https://arxiv.org/abs/2301.11905); [A Proof of the Nisan–Ronen Conjecture](https://doi.org/10.1145/3785408); [Setting Lower Bounds on Truthfulness](https://arxiv.org/abs/1507.08708); [Randomized Truthful Mechanisms for Scheduling Unrelated Machines](https://link.springer.com/chapter/10.1007/978-3-540-92185-1_46); [An Improved Randomized Truthful Mechanism for Scheduling Unrelated Machines](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2008.1314); [New Bounds for Truthful Scheduling on Two Unrelated Selfish Machines](https://link.springer.com/article/10.1007/s00224-019-09927-x); [A proof of the Nisan–Ronen conjecture — Oxford repository copy](https://ora.ox.ac.uk/objects/uuid%3A814fc511-99e2-47cb-b06a-f472630996dc/files/r9593tw016).

## 39. Cynthia Dwork

[Research bibliography](https://dblp.org/pid/83/6616.html).

### 1. Polynomial-time private release of all marginals

[TCS-7236](../../data/cards/TCS-7236.json) · reused · status: `source_open` · evidence: `reviewed`.

Efficient private marginal release connects her foundational query-release work.

**Status scope:** No solution of the stated all-orders synopsis target was found through 11 September 2026. The explicit open-problem source is older; later-work searches are not an exhaustive review of every k-way, interactive or synthetic-data variant.

Sources: [The Complexity of Differential Privacy](https://projects.iq.harvard.edu/files/privacytools/files/complexityprivacy_1_01.pdf); [Faster Private Release of Marginals on Small Databases](https://arxiv.org/abs/1304.3754).

### 2. Computational versus statistical privacy in the curator model

[TCS-6825](../../data/cards/TCS-6825.json) · reused · status: `source_open` · evidence: `source`.

Statistical versus computational privacy is a foundational question linked to her cryptographic approach to privacy.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2014 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [The Algorithmic Foundations of Differential Privacy](https://www.cis.upenn.edu/~aaroth/privacybook.html).

## 40. Scott Aaronson

[Research bibliography](https://dblp.org/pid/56/1358.html).

### 1. Aaronson–Ambainis conjecture

[TCS-6605](../../data/cards/TCS-6605.json) · reused · status: `source_open` · evidence: `reviewed`.

He co-posed this conjecture on bounded low-degree polynomials and quantum query power.

**Status scope:** The 4 September 2026 primary paper explicitly leaves the unrestricted Aaronson–Ambainis conjecture open. Recent restricted-model and bounded-round results do not prove it; the 2019 general claim remains withdrawn. Checked through 11 September 2026.

Sources: [The Need for Structure in Quantum Speedups](https://arxiv.org/abs/0911.0996); [Quantum speedups need structure — withdrawn](https://arxiv.org/abs/1911.03748); [Influence in Completely Bounded Block-Multilinear Forms and Classical Simulation of Quantum Algorithms](https://ir.cwi.nl/pub/31883/31883.pdf); [Random Restrictions of Bounded Low Degree Polynomials Are Juntas](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.17); [Aaronson-Ambainis Conjecture Is True For Random Restrictions](https://eccc.weizmann.ac.il/report/2024/035/); [Quantum Speedups Require Structure or Depth](https://arxiv.org/abs/2608.19158); [Optimal inequalities for completely bounded polynomials and the limitations of quantum query algorithms](https://arxiv.org/abs/2609.05201).

### 2. Classical hardness of Boson Sampling

[TCS-6933](../../data/cards/TCS-6933.json) · reused · status: `source_open` · evidence: `source`.

Classical hardness of Boson Sampling directly extends his quantum-sampling program.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2016 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Quantum Algorithms: An Overview](https://arxiv.org/abs/1511.04206).

## 41. Bernhard Haeupler

[Research bibliography](https://dblp.org/pid/39/1043.html).

### 1. Efficient explicit constant-rate tree codes

[TCS-0013](../../data/cards/TCS-0013.json) · reused · status: `uncertain` · evidence: `index`.

Efficient tree codes are a foundational target for his interactive-coding research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf).

### 2. Optimal exact single-source shortest paths in CONGEST

[TCS-6555](../../data/cards/TCS-6555.json) · reused · status: `open` · evidence: `reviewed`.

Optimal distributed exact SSSP connects his low-congestion communication and shortest-path algorithms.

**Status scope:** Primary exact CONGEST bounds, randomized distance lower bounds, the approximation result and later-result searches were checked on 11 September 2026. No algorithm or impossibility theorem settling the full stated polylogarithmic-overhead target was found. The inherited 2026 paper is retained as related-work provenance, rather than used alone as evidence of the current best bound.

Sources: [Polylogarithmic time algorithms for shortest path forests in programmable matter](https://link.springer.com/article/10.1007/s00446-026-00505-2); [Single-source shortest paths in the CONGEST model with improved bounds](https://link.springer.com/article/10.1007/s00446-021-00412-8); [Parallel Exact Shortest Paths in Almost Linear Work and Square Root Depth](https://nairenc.github.io/nairenc_files/parallelexactsspsqrt.pdf); [Distributed Verification and Hardness of Distributed Approximation](https://arxiv.org/abs/1011.3049); [Undirected \((1+\varepsilon )\)-Shortest Paths via Minor-Aggregates: Near-Optimal Deterministic Parallel & Distributed Algorithms](https://arxiv.org/abs/2204.05874).

## 42. Aviad Rubinstein

[Research bibliography](https://dblp.org/pid/11/10308.html).

### 1. Constant-factor approximation for Densest k-Subgraph

[TCS-6587](../../data/cards/TCS-6587.json) · reused · status: `source_open` · evidence: `reviewed`.

Densest k-subgraph concerns the approximation barriers in his hardness research.

**Status scope:** Checked through 10 September 2026. The constant-factor algorithm is already ruled out assuming ETH, which remains unproved. The May 2026 primary source explicitly notes the absence of NP-hardness of approximation even at factor 1.001. This card asks about a deterministic constant-factor algorithm on all unweighted graphs, and preserves the distinction between conditional evidence and an unconditional resolution.

Sources: [Detecting High Log-Densities — an \(O(n^{1}/4)\) Approximation for Densest k-Subgraph](https://arxiv.org/abs/1001.2891); [Polynomial integrality gaps for strong SDP relaxations of Densest k-subgraph](https://arxiv.org/abs/1110.1360); [Almost-Polynomial Ratio ETH-Hardness of Approximating Densest k-Subgraph](https://arxiv.org/abs/1611.05991); [A New Conjecture on Hardness of 2-CSP’s with Implications to Hardness of Densest k-Subgraph and Other Problems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2023.38); [A Scalable and Exact Relaxation for Densest k-Subgraph via Error Bounds](https://ojs.aaai.org/index.php/AAAI/article/view/38562); [A Note on Approximability of Densest At-Least-k-Subgraph](https://arxiv.org/abs/2605.25464).

### 2. Truly subquadratic exact edit distance

[TCS-7179](../../data/cards/TCS-7179.json) · reused · status: `open` · evidence: `reviewed`.

Edit-distance complexity connects to his fine-grained hardness program.

**Status scope:** The checked primary literature gives conditional exact-distance lower bounds and a March 2026 approximation advance. Searches through 11 September 2026 found no established deterministic truly subquadratic exact algorithm or unconditional exclusion in this model.

Sources: [Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)](https://arxiv.org/abs/1412.0348); [Wikipedia: List of unsolved problems in computer science](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1345711618); [Quadratic Conditional Lower Bounds for String Problems and Dynamic Time Warping](https://arxiv.org/abs/1502.01063v2); [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702).

## 43. Mikkel Thorup

[Research bibliography](https://dblp.org/pid/t/MikkelThorup.html).

### 1. Expected linear-time integer sorting for every word length

[TCS-6537](../../data/cards/TCS-6537.json) · reused · status: `source_open` · evidence: `reviewed`.

Integer sorting is a direct target of his word-RAM algorithm research.

**Status scope:** The checked primary bounds and the CMU Spring 2025 source leave expected linear-time sorting across all word lengths open. Searches through 11 September 2026 found no result settling this full target. Recent parallel sorting results for keys in \([n]\) concern a restricted universe and a different performance model.

Sources: [Integer sorting in \(O(n\sqrt{\log  \log  n})\) expected time and linear space](https://doi.org/10.1109/SFCS.2002.1181890); [Deterministic sorting in \(O(n \log  \log  n)\) time and linear space](https://www.sciencedirect.com/science/article/pii/S019667740300155X); [Expected Linear Time Sorting for Word Size \(\Omega (\log ^{2} n \log  \log  n)\)](https://cs.au.dk/~gerth/papers/swat14sort.pdf); [Integer models of computation and integer sorting](https://www.cs.cmu.edu/~15451-s25/slides/lecture03.pdf).

### 2. Logarithmic Las Vegas dynamic connectivity

[TCS-7332](../../data/cards/TCS-7332.json) · reused · status: `source_open` · evidence: `reviewed`.

Dynamic connectivity continues his fundamental graph-data-structure work.

**Status scope:** Open in the cited dated sources. The bounded source and subsequent-result review on 13 September 2026 found no verified resolution of this target; this is not exhaustive certification of current openness.

Sources: [Fully Dynamic Connectivity in \(O(\log n(\log\log n)^2)\) Amortized Expected Time](https://theoretics.episciences.org/10791/pdf); [Dynamic Connectivity with Expected Polylogarithmic Worst-Case Update Time](https://arxiv.org/abs/2510.08297).

## 44. Rasmus Kyng

[Research bibliography](https://dblp.org/pid/140/7252.html).

### 1. Exact directed maximum flow in \(O((m+n) \operatorname{polylog} n)\) time

[TCS-7228](../../data/cards/TCS-7228.json) · reused · status: `source_open` · evidence: `reviewed`.

Exact near-linear flow extends his almost-linear flow and optimization algorithms.

**Status scope:** Primary-source check through 11 September 2026 found almost-linear bounds, not the fixed-polylogarithmic overhead required here. New preprint proofs were not independently verified.

Sources: [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://arxiv.org/abs/2203.00671); [Maximum Flow Without the Outer IPM](https://arxiv.org/abs/2608.17384).

### 2. Nearly linear-time solution of general sparse linear systems

[TCS-6585](../../data/cards/TCS-6585.json) · reused · status: `source_open` · evidence: `reviewed`.

General sparse linear systems concern the limits of his solver techniques.

**Status scope:** Checked through 10 September 2026. This is an editorial, fully specified near-linear target in the polynomial-conditioning and precision regime, not a named positive conjecture. The faster-than-matrix-multiplication problem has already been solved. The August 2026 report discusses broader scalable solvers but does not claim this universal guarantee; the simplicial-Laplacian reduction is not a general running-time lower bound.

Sources: [Solving Sparse Linear Systems Faster than Matrix Multiplication](https://arxiv.org/abs/2007.10254); [Nearly Linear Time Algorithms for Preconditioning and Solving Symmetric, Diagonally Dominant Linear Systems](https://epubs.siam.org/doi/10.1137/090771430); [Matrix anti-concentration inequalities with applications](https://arxiv.org/abs/2111.05553); [Hardness Results for Laplacians of Simplicial Complexes via Sparse-Linear Equation Complete Gadgets](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.53); [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394).

## 45. David Steurer

[Research bibliography](https://dblp.org/pid/59/254.html).

### 1. Computational threshold for tensor PCA

[TCS-6657](../../data/cards/TCS-6657.json) · reused · status: `source_open` · evidence: `reviewed`.

Tensor PCA is central to his sum-of-squares and inference work.

**Status scope:** The May 2026 low-degree paper retains the conjectured gap for unrestricted algorithms and distinguishes spherical from independent-coordinate priors. The 2024 power-iteration and October 2025 stochastic-gradient improvements concern particular methods and do not provide a fixed-power improvement below \(n^{k/4}\). No full resolution found through 11 September 2026. The card explicitly fixes a finite-precision bit model; restricted lower bounds in the standard unrounded model are evidence, not a proof for all algorithms here.

Sources: [A statistical model for tensor PCA](https://arxiv.org/abs/1411.1076); [Sharp analysis of power iteration for tensor PCA](https://www.jmlr.org/papers/v25/24-0006.html); [Tensor cumulants for statistical inference on invariant distributions](https://arxiv.org/abs/2404.18735); [Near-Optimal Tensor PCA via Normalized Stochastic Gradient Ascent with Overparameterization](https://arxiv.org/abs/2510.14329); [Low-degree estimation thresholds in planted hypergraphs and tensor PCA](https://arxiv.org/abs/2605.30113).

### 2. Small-Set Expansion Hypothesis

[TCS-7160](../../data/cards/TCS-7160.json) · reused · status: `open` · evidence: `reviewed`.

Small-set expansion connects his SDP, spectral and approximation research.

**Status scope:** No proof or refutation located through 11 September 2026. The original exact-size regular-graph promise was checked separately from later weighted, volume and randomized variants. The August 2026 least-squares result is conditional on such a variant.

Sources: [Graph expansion and the unique games conjecture](https://doi.org/10.1145/1806689.1806792); [Wikipedia: Small set expansion hypothesis](https://en.wikipedia.org/wiki/Small_set_expansion_hypothesis); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1368726535); [Graph Expansion and the Unique Games Conjecture](https://www.dsteurer.org/paper/expansion.pdf); [Reductions Between Expansion Problems](https://arxiv.org/abs/1011.2586); [The Condition-Number Barrier in Sparse Least Squares](https://arxiv.org/abs/2608.02588).

## 46. James R. Lee

[Research bibliography](https://dblp.org/pid/40/837.html).

### 1. Superpolynomial semidefinite extension complexity of perfect matching

[TCS-7283](../../data/cards/TCS-7283.json) · reused · status: `source_open` · evidence: `reviewed`.

Semidefinite extension complexity directly concerns his optimization lower bounds.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Lower Bounds for Interactive Compression and Linear Programs](https://digital.lib.washington.edu/server/api/core/bitstreams/a7ac9607-c4f8-4d56-9b29-0f5ef033975d/content).

### 2. Constant-factor approximation for uniform Sparsest Cut

[TCS-7266](../../data/cards/TCS-7266.json) · reused · status: `source_open` · evidence: `reviewed`.

Sparsest Cut connects his metric-embedding and SDP methods.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Lecture Notes on the ARV Algorithm for Sparsest Cut](https://arxiv.org/abs/1607.00854).

## 47. Ola Svensson

[Research bibliography](https://dblp.org/pid/11/6945.html).

### 1. Optimal polynomial-time approximation ratio for asymmetric TSP

[TCS-7357](../../data/cards/TCS-7357.json) · added · status: `source_open` · evidence: `reviewed`.

Optimal ATSP approximation continues his constant-factor ATSP breakthrough.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [Better approximation guarantee for Asymmetric TSP](https://arxiv.org/abs/2603.14334).

### 2. Optimal approximation ratio for precedence-constrained makespan

[TCS-6676](../../data/cards/TCS-6676.json) · reused · status: `source_open` · evidence: `reviewed`.

Precedence scheduling extends his approximation and inapproximability work.

**Status scope:** No polynomial-time fixed \((2- \varepsilon )\) improvement found through 11 September 2026. Svensson’s factor-two hardness requires the specified possibly stronger Unique Games variant. Recent fixed-machine approximation schemes and exact unit-job algorithms have narrower scope, while July 2026 UMPS hardness imposes machine eligibility restrictions absent here. The 12 September 2026 edit adopts absolute 0.01 benchmark acceptance; the saved open-status evidence concerns the underlying exact question and does not independently certify openness at that tolerance.

Sources: [Bounds for Certain Multiprocessing Anomalies](https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1966.tb01709.x); [Complexity of Scheduling under Precedence Constraints](https://pubsonline.informs.org/doi/abs/10.1287/opre.26.1.22); [Hardness of Precedence Constrained Scheduling on Identical Machines](https://theory.epfl.ch/osven/Ola%20Svensson_publications/SICOMP11b.pdf); [A Simpler QPTAS for Scheduling Jobs with Precedence Constraints](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2022.40); [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://arxiv.org/abs/2312.03495); [Inapproximability of Unique-Machine Precedence Scheduling for Unit-Length Jobs](https://arxiv.org/abs/2607.26590).

## 48. Alexandr Andoni

[Research bibliography](https://dblp.org/pid/66/6009.html).

### 1. Optimal \(\ell\)\(_{1}\) distortion of edit distance

[TCS-7297](../../data/cards/TCS-7297.json) · reused · status: `source_open` · evidence: `reviewed`.

Edit-distance embedding into L1 connects his high-dimensional distance and sketching research.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Low Distortion Embeddings for Edit Distance](https://doi.org/10.1145/1060590.1060623).

### 2. Optimal input-sparsity subspace embeddings

[TCS-7006](../../data/cards/TCS-7006.json) · reused · status: `source_open` · evidence: `source`.

Optimal subspace embeddings extend his dimensionality-reduction algorithms.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2015 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357).

## 49. Piotr Indyk

[Research bibliography](https://dblp.org/pid/i/PiotrIndyk.html).

### 1. Optimal deterministic restricted-isometry matrices

[TCS-6662](../../data/cards/TCS-6662.json) · reused · status: `source_open` · evidence: `reviewed`.

Deterministic RIP constructions concern explicit dimensionality reduction and compressed sensing.

**Status scope:** Reviewed through 11 September 2026. No polynomial-time deterministic construction with the required uniform optimal row bound was found in the checked sources. Optimal randomized row counts, restricted parameter regimes and coherence guarantees are recorded as partial progress.

Sources: [Doubly transitive equiangular tight frames that contain regular simplices](https://www.sciencedirect.com/science/article/pii/S0024379525003143); [The road to deterministic matrices with the restricted isometry property](https://www.math.ucdavis.edu/~strohmer/courses/270/road_to_rip.pdf); [Explicit constructions of RIP matrices and related problems](https://arxiv.org/abs/1008.4535); [Satisfying the restricted isometry property with the optimal number of rows and slightly less randomness](https://arxiv.org/abs/2311.07889).

### 2. Optimal \(\ell\)\(_{1}\) distortion of planar Earth Mover Distance

[TCS-6529](../../data/cards/TCS-6529.json) · reused · status: `source_open` · evidence: `source`.

Planar earthmover embedding connects his algorithms for similarity and geometric data.

**Status scope:** Retained in the source-based research proposal dated 10 September 2026. No full resolution was found in that search; this is not a completed independent open-status review.

Sources: [Research reference · www.weizmann.ac.il](https://www.weizmann.ac.il/math/gideon/sites/math.gideon/files/uploads/planar-earthmover.pdf).

## 50. Sanjam Garg

[Research bibliography](https://dblp.org/pid/33/5817.html).

### 1. Circuit obfuscation from polynomial-hard LWE

[TCS-6550](../../data/cards/TCS-6550.json) · reused · status: `source_open` · evidence: `reviewed`.

LWE-based iO continues his obfuscation constructions.

**Status scope:** Checked through 10 September 2026. No construction from the plain polynomial-hard decisional-LWE assumption fixed here was identified. Existing multi-assumption and circular-security constructions do not settle it. Polynomial hardness, polynomial modulus/noise ratio, classical adversaries, arbitrary circuits and no auxiliary leakage are explicit choices that make the broad LWE-alone question unambiguous.

Sources: [On the \((Im)\)possibility of Obfuscating Programs](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html); [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); [Indistinguishability Obfuscation from Well-Founded Assumptions](https://doi.org/10.1145/3785007); [Indistinguishability Obfuscation from LPN over \(F_{p}\), DLIN, and PRGs in \(\mathrm{NC}^{0}\)](https://eprint.iacr.org/2021/1334); [Factoring and Pairings Are Not Necessary for IO: Circular-Secure LWE Suffices](https://doi.org/10.4230/LIPIcs.ICALP.2022.28).

### 2. Oblivious transfer from public-key encryption

[TCS-6549](../../data/cards/TCS-6549.json) · reused · status: `source_open` · evidence: `reviewed`.

OT from PKE is a foundational secure-computation question connected to his cryptographic reductions.

**Status scope:** Checked through 10 September 2026. No unrestricted classical implication from arbitrary IND-CPA public-key encryption to OT was identified. Known oracle/black-box separations and positive results for rerandomizable or suitably samplable encryption do not settle this formulation. The card fixes semi-honest standalone security with classical communication and no setup.

Sources: [The Relationship between Public Key Encryption and Oblivious Transfer](https://vmahesh.cs.illinois.edu/papers/focs00.pdf); [Black-Box Constructions of Protocols for Secure Computation](https://iftachh.github.io/MyHomepage/papers/BlackBoxMPC/black-box-mpc.pdf); [Computational Hardness of Optimal FairComputation: Beyond Minicrypt](https://eprint.iacr.org/2021/882); [Oblivious Transfer from Rerandomizable PKE](https://eprint.iacr.org/2023/1002); [On the Implications from Updatable Encryption to Public-Key Cryptographic Primitives](https://doi.org/10.1587/transfun.2025CIP0019).

## 51. Pravesh Kothari

[Research bibliography](https://dblp.org/pid/47/7934.html).

### 1. Planted clique conjecture

[TCS-6656](../../data/cards/TCS-6656.json) · reused · status: `source_open` · evidence: `reviewed`.

Planted clique captures the statistical-computational barriers in his SOS work.

**Status scope:** Checked through 10 September 2026; no unrestricted polynomial-time solution below \(n^{1/2- \varepsilon}\) or unconditional hardness proof was identified. The exact formulation fixes constant-success detection and exactly k planted vertices. Low-degree and sum-of-squares bounds remain scoped to their models; the optimal-advantage result is conditional.

Sources: [Finding a Large Hidden Clique in a Random Graph](https://people.math.ethz.ch/~sudakovb/hidden-clique.pdf); [A Nearly Tight Sum-of-Squares Lower Bound for the Planted Clique Problem](https://doi.org/10.1137/17M1138236); [Finding planted cliques using gradient descent](https://arxiv.org/abs/2311.07540v2); [On optimal distinguishers for Planted Clique](https://arxiv.org/abs/2505.01990v2); [Robust Algorithms for Finding Cliques in Random Intersection Graphs via Sum-of-Squares](https://proceedings.mlr.press/v336/gobel26a.html).

### 2. Superpolynomial \(\mathrm{AC}^{0}[p]\)-Frege lower bounds

[TCS-6602](../../data/cards/TCS-6602.json) · reused · status: `source_open` · evidence: `reviewed`.

Modular bounded-depth Frege lower bounds connect his proof-complexity research.

**Status scope:** Checked through 10 September 2026. The 2026 primary sources retain modular Frege lower bounds as open. ITCS 2026.99 does not prove that its hard-to-prove candidates are tautologies. ECCC TR26-018 restricts derivation depth or proves a polynomial size bound; TR26-070 treats a restricted algebraic certificate representation. None establishes the fully specified tautology families and unrestricted derivation size lower bounds requested here.

Sources: [Extended Nullstellensatz proof systems](https://www.karlin.mff.cuni.cz/~krajicek/finitary.pdf); [Exponential Lower Bounds for the Pigeonhole Principle](https://www.cs.toronto.edu/~toni/Papers/exp-pigeon.pdf); [Amortized Closure and Its Applications in Lifting for Resolution over Parities](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.8); [\(\mathrm{AC}^{0}[p]\)-Frege Cannot Efficiently Prove That Constant-Depth Algebraic Circuit Lower Bounds Are Hard](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.99); [Resolution Width Lifts to Near-Quadratic-Depth \(Res(\oplus )\) Size](https://eccc.weizmann.ac.il/report/2026/018/); [Hard CNF Instances for Ideal Proof Systems](https://eccc.weizmann.ac.il/report/2026/070/).

## 52. Daniel Lokshtanov

[Research bibliography](https://dblp.org/pid/78/67.html).

### 1. FPT versus \(\mathrm{W}[1]\)

[TCS-6592](../../data/cards/TCS-6592.json) · reused · status: `source_open` · evidence: `reviewed`.

FPT versus W[1] is a foundational barrier for his parameterized algorithms.

**Status scope:** Explicitly presented as the central open conjecture in Bottesch’s primary paper and the parameterized-algorithms textbook. Research through 10 September 2026 located no proof of equality or separation. Conditional lower bounds and improved fixed-k algorithms are recorded with their distinct quantifiers.

Sources: [Parameterized Algorithms](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf); [On \(\mathrm{W}[1]\)-Hardness as Evidence for Intractability](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2018.73); [Constant Approximating k-Clique is \(\mathrm{W}[1]\)-hard](https://arxiv.org/abs/2102.04769); [Simple Combinatorial Construction of the \(k^{o(1)}\)-Lower Bound for Approximating the Parameterized k-Clique](https://arxiv.org/abs/2304.07516); [Faster Combinatorial k-Clique Algorithms](https://weizmann.elsevierpure.com/en/publications/faster-combinatorial-k-clique-algorithms-2/).

### 2. Polynomial kernels for Directed Feedback Vertex Set

[TCS-6379](../../data/cards/TCS-6379.json) · reused · status: `open` · evidence: `reviewed`.

Polynomial DFVS kernels directly concern his kernelization and graph-algorithm work.

**Status scope:** Checked the full 2016 source and WADS 2019 author manuscript, plus the 2025 journal abstract, institutional publication record and author publication listing. The publisher blocked access to its full journal text, so detailed theorem scope is attributed to the checked conference manuscript. Searches through 12 September 2026 found no resolution of the unrestricted solution-budget kernel. No independent proof verification.

Sources: [Polynomial Kernels for Deletion to Classes of Acyclic Digraphs](https://doi.org/10.4230/LIPIcs.STACS.2016.55); [Wannabe Bounded Treewidth Graphs Admit a Polynomial Kernel for Directed Feedback Vertex Set](https://doi.org/10.1145/3711669).

## 53. Ryan O'Donnell

[Research bibliography](https://dblp.org/pid/34/5965.html).

### 1. Fourier Entropy–Influence conjecture

[TCS-6604](../../data/cards/TCS-6604.json) · reused · status: `source_open` · evidence: `reviewed`.

Fourier entropy-influence is a central Boolean-analysis conjecture in his research area.

**Status scope:** Checked through 10 September 2026. The June 2026 primary paper explicitly retains classical FEI as open and proves only specified classes. The August 2026 disproof is of the quantum extension. No classical resolution was found in the checked sources; the formulation uses Shannon entropy, uniform measure and scalar Boolean functions throughout.

Sources: [The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions](https://www.cs.cmu.edu/~jswright/papers/fei.pdf); [A new bound for the Fourier-Entropy-Influence conjecture](https://arxiv.org/abs/2312.08271); [Further evidence towards the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/2606.00246); [Dense Hamiltonians at the Parseval Limit: The Noncommutative BH Constant is Exponential and the Quantum FEI Conjecture is False](https://arxiv.org/abs/2608.01424).

### 2. Mansour’s conjecture

[TCS-6581](../../data/cards/TCS-6581.json) · reused · status: `source_open` · evidence: `reviewed`.

Mansour's conjecture connects his Fourier analysis and computational learning work.

**Status scope:** Open in the strong logarithmic-accuracy form stated here, following the inspected primary sources and a later-result search through 11 September 2026. Fixed-error polynomial concentration, restricted DNF models, and generalized-basis learning results do not by themselves settle this formulation.

Sources: [The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions](https://www.ias.edu/sites/default/files/math/ODonnell_Fourier.pdf); [Mansour’s Conjecture is True for Random DNF Formulas](https://eccc.weizmann.ac.il/report/2010/023/revision/3/download/); [Sharper bounds on the Fourier concentration of DNFs](https://arxiv.org/abs/2109.04525v2); [A New Bound for the Fourier-Entropy-Influence Conjecture](https://link.springer.com/article/10.1007/s00493-024-00133-z); [Further evidence towards the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/2606.00246v2); [Learning DNF through Generalized Fourier Representations](https://arxiv.org/abs/2506.01075v2).

## 54. MohammadTaghi Hajiaghayi

[Research bibliography](https://dblp.org/pid/334/4488.html).

### 1. Polylogarithmic approximation for Directed Steiner Tree

[TCS-6588](../../data/cards/TCS-6588.json) · reused · status: `source_open` · evidence: `reviewed`.

Directed Steiner approximation connects his network-design research.

**Status scope:** The July 2026 primary literature explicitly leaves this general-graph question open. The inherited 2024 claim was withdrawn, and its October 2025 replacement is restricted to a special supplied fractional solution; that claim is not counted as an established general result. Planar and quasipolynomial algorithms do not satisfy this card. Checked through 11 September 2026.

Sources: [Approximation Algorithms for Directed Steiner Problems](https://chekuri.web.engr.illinois.edu/pub.html); [\(O(\log ^{2} k/\log  \log  k)\)-Approximation Algorithm for Directed Steiner Tree: A Tight Quasi-Polynomial-Time Algorithm](https://people.idsia.ch/~grandoni/Pubblicazioni/GLL19stoc.pdf); [An \(O(\log  k)\)-Approximation for Directed Steiner Tree in Planar Graphs](https://arxiv.org/abs/2302.04747); [From Directed Steiner Tree to Directed Polymatroid Steiner Tree in Planar Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.42); [On the Integrality Gap of Directed Steiner Tree LPs with Relatively Integral Solutions](https://arxiv.org/abs/2412.10744); [Length-Constrained Network Design in Planar Digraphs](https://arxiv.org/abs/2607.25811).

### 2. Single-exponential exact cut mimicking networks

[TCS-7348](../../data/cards/TCS-7348.json) · reused · status: `source_open` · evidence: `reviewed`.

Cut mimicking networks concern the compression and routing structures he studies.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. Editorial linear-exponent endpoint: the precise target is 2 to a constant times k, not an unspecified exponential in a polynomial of k. Arbitrary replacement graphs and exact set-cut preservation are essential.

Sources: [Cut-Preserving Vertex Sparsifiers for Planar and Quasi-Bipartite Graphs](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.53/LIPIcs.ICALP.2025.53.html); [On Mimicking Networks Representing Minimum Terminal Cuts](https://arxiv.org/abs/1207.6371); [Krajinou grafových algoritmů](https://mj.ucw.cz/vyuka/ga/ga.pdf).

## 55. Johan Håstad

[Research bibliography](https://dblp.org/pid/47/3155.html).

### 1. Majority outside constant-depth modular circuits

[TCS-1056](../../data/cards/TCS-1056.json) · reused · status: `source_open` · evidence: `reviewed`.

Modular-circuit lower bounds extend his Boolean circuit lower-bound program.

**Status scope:** The target is explicitly open in Jukna’s source. A 13 September 2026 small-text check of later modular-circuit work identified a symmetry-restricted AND result, not a solution for majority in unrestricted ACC⁰. No resolution was verified; status remains source_open.

Sources: [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html); [Optimal Lower Bounds for Symmetric Modular Circuits](https://arxiv.org/abs/2604.04760).

### 2. Unconditional NP-hardness at the Goemans–Williamson Max-Cut threshold

[TCS-7281](../../data/cards/TCS-7281.json) · reused · status: `source_open` · evidence: `reviewed`.

Unconditional sharp Max-Cut hardness continues his optimal-inapproximability work.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Optimal Inapproximability Results for MAX-CUT and Other 2-Variable CSPs](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/07/Optimal_Inapproximability_Results_for_MAX_CUT_and_Other_2_Variable_CSPs_1.pdf).

## 56. Ran Raz

[Research bibliography](https://dblp.org/pid/91/5912.html).

### 1. Superpolynomial arithmetic formula lower bounds

[TCS-6888](../../data/cards/TCS-6888.json) · reused · status: `source_open` · evidence: `source`.

Arithmetic formula lower bounds directly extend his algebraic-complexity results.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2010 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf).

### 2. Constant-factor randomized direct sums for total Boolean functions

[TCS-5892](../../data/cards/TCS-5892.json) · reused · status: `source_open` · evidence: `reviewed`.

Randomized direct sums for total functions concern his communication and information-complexity research.

**Status scope:** A user-authorized precise total-Boolean-function variant. The August 2026 primary preprint explicitly distinguishes relations from the remaining total-function question. Rechecked on 13 September 2026; its new theorem is a reported preprint claim, not an independently verified result or a refutation of this target.

Sources: [Lifting Theorems for Equality](https://doi.org/10.4230/LIPIcs.STACS.2019.50); [Efficient Communication Using Partial Information](https://eccc.weizmann.ac.il/report/2010/083/); [Zero-error information equals amortized communication complexity](https://arxiv.org/abs/2608.04141).

## 57. Daniel Dadush

[Research bibliography](https://dblp.org/pid/07/3765.html).

### 1. Single-exponential dependence on dimension for integer programming

[TCS-7264](../../data/cards/TCS-7264.json) · reused · status: `source_open` · evidence: `reviewed`.

Single-exponential integer programming is central to his geometry-of-numbers algorithms.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [A Brief History of Parameterized Algorithms for Block-Structured Integer Programs](https://drops.dagstuhl.de/storage/00lipics/lipics-vol358-ipec2025/html/LIPIcs.IPEC.2025.1/LIPIcs.IPEC.2025.1.html).

### 2. Komlós conjecture

[TCS-7314](../../data/cards/TCS-7314.json) · reused · status: `source_open` · evidence: `reviewed`.

Komlos directly connects his discrepancy and convex-geometric work.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. The companion Beck–Fiala target is a documented consequence, not a duplicate. No algorithmic construction requirement is added.

Sources: [Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk](https://arxiv.org/abs/2508.03961).

## 58. Huijia Lin

[Research bibliography](https://dblp.org/pid/37/778.html).

### 1. Circuit obfuscation from polynomial-hard LWE

[TCS-6550](../../data/cards/TCS-6550.json) · reused · status: `source_open` · evidence: `reviewed`.

LWE-based iO is a central next target after her obfuscation constructions.

**Status scope:** Checked through 10 September 2026. No construction from the plain polynomial-hard decisional-LWE assumption fixed here was identified. Existing multi-assumption and circular-security constructions do not settle it. Polynomial hardness, polynomial modulus/noise ratio, classical adversaries, arbitrary circuits and no auxiliary leakage are explicit choices that make the broad LWE-alone question unambiguous.

Sources: [On the \((Im)\)possibility of Obfuscating Programs](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html); [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); [Indistinguishability Obfuscation from Well-Founded Assumptions](https://doi.org/10.1145/3785007); [Indistinguishability Obfuscation from LPN over \(F_{p}\), DLIN, and PRGs in \(\mathrm{NC}^{0}\)](https://eprint.iacr.org/2021/1334); [Factoring and Pairings Are Not Necessary for IO: Circular-Secure LWE Suffices](https://doi.org/10.4230/LIPIcs.ICALP.2022.28).

### 2. Identity-based encryption from arbitrary public-key encryption

[TCS-7278](../../data/cards/TCS-7278.json) · reused · status: `source_open` · evidence: `reviewed`.

IBE from generic PKE concerns reducing assumptions for advanced encryption.

**Status scope:** The primary 2021 source supplies a generic-group barrier and does not refute the unrestricted implication. Formulation and barrier scope were checked on 13 September 2026; the bounded saved later-work review did not identify a general resolution. The foundational security definition uses the earlier recorded read.

Sources: [Generic-Group Identity-Based Encryption: A Tight Impossibility Result](https://eprint.iacr.org/2021/745.pdf); [Identity-Based Encryption from the Weil Pairing](https://crypto.stanford.edu/~dabo/pubs/papers/bfibe.pdf).

## 59. Zvika Brakerski

[Research bibliography](https://dblp.org/pid/53/1085.html).

### 1. Unleveled fully homomorphic encryption from LWE alone

[TCS-6551](../../data/cards/TCS-6551.json) · reused · status: `source_open` · evidence: `reviewed`.

FHE without circular-security assumptions continues his foundational FHE research.

**Status scope:** No classical unleveled compact FHE construction from the specified ordinary LWE assumption alone was found through 11 September 2026. Functional-encryption constructions use additional assumptions. The inspected February and April 2026 no-circularity proposals retain explicit level bounds; the latter also uses quantum evaluation. This card fixes polynomial-modulus LWE, nonuniform classical security and fresh-input FHE correctness.

Sources: [Efficient Fully Homomorphic Encryption from (Standard) LWE](https://epubs.siam.org/doi/10.1137/120868669); [Quantum FHE (Almost) As Secure As Classical](https://www.iacr.org/archive/crypto2018/10993383/10993383.pdf); [Fully Homomorphic Encryption: definitional issues and open problems](https://cseweb.ucsd.edu/classes/wi23/cse208-a/FHEorg.pdf); [Bootstrapping Homomorphic Encryption via Functional Encryption](https://eprint.iacr.org/2023/1376.pdf); [Bootstrapping Homomorphic Encryption via Functional Encryption — conference version](https://drops.dagstuhl.de/storage/00lipics/lipics-vol251-itcs2023/LIPIcs.ITCS.2023.17/LIPIcs.ITCS.2023.17.pdf); [Dynamic multi-key FHE without CRS from LWE](https://link.springer.com/article/10.1186/s42400-025-00431-z); [Efficient Quantum Fully Homomorphic Encryption](https://arxiv.org/abs/2604.23490).

### 2. Public-key quantum money from LWE alone

[TCS-7359](../../data/cards/TCS-7359.json) · added · status: `source_open` · evidence: `reviewed`.

Public verification from LWE alone concerns his lattice and quantum-cryptography program.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [Anonymous Public-Key Quantum Money and Quantum Voting](https://arxiv.org/abs/2411.04482); [On Quantum Money and Evasive Obfuscation](https://eprint.iacr.org/2025/325); [A General Quantum Duality for Representations of Groups with Applications to Quantum Money, Lightning, and Fire](https://mzhandry.github.io/pubs.quantum.html).

## 60. Daniel Wichs

[Research bibliography](https://dblp.org/pid/24/2359.html).

### 1. Sublinear-communication secure computation with polynomial setup

[TCS-5013](../../data/cards/TCS-5013.json) · reused · status: `uncertain` · evidence: `source`.

Communication-efficient MPC extends his succinct cryptographic protocols.

**Status scope:** Question recorded in a source from 2023; subsequent results and present open status have not been individually checked.

Sources: [Exponential Correlated Randomness Is Necessary in Communication-Optimal Perfectly Secure Two-Party Computation](https://doi.org/10.4230/LIPIcs.ITC.2023.18).

### 2. Noninteractive zero knowledge from one-way functions

[TCS-6552](../../data/cards/TCS-6552.json) · reused · status: `source_open` · evidence: `reviewed`.

Minimal assumptions for NIZK connect his cryptographic proof and delegation research.

**Status scope:** No construction of reusable adaptive NIZK arguments from ordinary OWFs alone, or refutation of that unrestricted implication, was found through 11 September 2026. The cited BARG, trapdoor-hash and derandomization constructions retain extra assumptions; recent OWF-only succinct proofs are interactive, and high-error characterizations run in the reverse direction.

Sources: [Commitment Schemes and Zero-Knowledge Protocols (2011)](https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf); [Noninteractive Zero Knowledge for NP from (Plain) Learning With Errors](https://web.eecs.umich.edu/~cpeikert/pubs/nizk-lwe.pdf); [Batch Arguments to NIZKs from One-Way Functions](https://eprint.iacr.org/2023/1938); [Black-Box Non-Interactive Zero Knowledge from Vector Trapdoor Hash](https://eprint.iacr.org/2024/1514); [Fiat-Shamir in the Plain Model from Derandomization (Or: Do Efficient Algorithms Believe that \(\mathrm{NP} = \mathrm{PSPACE}\)?)](https://eccc.weizmann.ac.il/report/2024/116/); [Non-Trivial Zero-Knowledge Implies One-Way Functions](https://arxiv.org/abs/2602.17651); [Succinct Zero-Knowledge Proofs from One-Way Functions: The Blackbox Way](https://doi.org/10.1007/978-3-032-35424-2_6).

## 61. Avishay Tal

[Research bibliography](https://dblp.org/pid/93/8727.html).

### 1. Exponential lower bounds for unrestricted threshold-of-threshold circuits

[TCS-1054](../../data/cards/TCS-1054.json) · reused · status: `source_open` · evidence: `reviewed`.

Threshold-of-threshold lower bounds connect his circuit-complexity work.

**Status scope:** The source states this challenge as open. The source-wide explicitness convention and circuit model were rechecked on 13 September 2026, together with the abstract of Chen’s subsequent work and a limited later-work search. No unconditional resolution was verified; this is not an exhaustive status review, and status remains source_open.

Sources: [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html); [Toward Super-Polynomial Size Lower Bounds for Depth-Two Threshold Circuits](https://arxiv.org/abs/1805.10698).

### 2. Sub-log-squared seeds for polynomial-size CNFs and DNFs

[TCS-1133](../../data/cards/TCS-1133.json) · reused · status: `uncertain` · evidence: `index`.

Short-seed generators for CNF/DNF extend his pseudorandomness research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/).

## 62. Kasper Green Larsen

[Research bibliography](https://dblp.org/pid/07/6242.html).

### 1. Superlogarithmic static cell-probe lower bounds

[TCS-6540](../../data/cards/TCS-6540.json) · reused · status: `source_open` · evidence: `reviewed`.

Superlogarithmic static cell-probe bounds are a core barrier in his data-structure lower bounds.

**Status scope:** Primary sources and later-result searches checked on 11 September 2026 did not supply a resolution of the stated static specialization. The STOC 2026 paper retains the broader static barrier as Open Problem 1.1. The fixed near-linear space, short-query Boolean output and uniform polynomial-time family are an expressly recorded specialization; conditional proof barriers and bounds for dynamic memory or superpolynomial query sets do not resolve it.

Sources: [The Natural Proofs Barrier against Data-Structure Lower-Bounds](https://doi.org/10.1145/3798129.3800843); [Stronger Cell Probe Lower Bounds via Local PRGs](https://eccc.weizmann.ac.il/report/2025/030/); [Lower Bounds for Linear Operators](https://eccc.weizmann.ac.il/report/2025/155/); [Crossing the Logarithmic Barrier for Dynamic Boolean Data Structure Lower Bounds](https://epubs.siam.org/doi/10.1137/18M1198429); [An \(\Omega ((\log  n/\log  \log  n)^{2})\) Cell-Probe Lower Bound for Dynamic Boolean Data Structures](https://eccc.weizmann.ac.il/report/2026/047/).

### 2. Multiphase conjecture

[TCS-7338](../../data/cards/TCS-7338.json) · reused · status: `source_open` · evidence: `reviewed`.

The multiphase problem directly concerns dynamic data-structure lower bounds.

**Status scope:** Open in the cited dated sources. The bounded source and subsequent-result review on 13 September 2026 found no verified resolution of this target; this is not exhaustive certification of current openness.

Sources: [Towards Polynomial Lower Bounds for Dynamic Problems](https://www.ccs.neu.edu/~viola/classes/papers/PatrascuTowards.pdf); [An Adaptive Step Toward the Multiphase Conjecture](https://arxiv.org/abs/1910.13543).

## 63. Huacheng Yu

[Research bibliography](https://dblp.org/pid/84/9059.html).

### 1. Superlogarithmic static cell-probe lower bounds

[TCS-6540](../../data/cards/TCS-6540.json) · reused · status: `source_open` · evidence: `reviewed`.

Strong static cell-probe lower bounds connect his data-structure complexity work.

**Status scope:** Primary sources and later-result searches checked on 11 September 2026 did not supply a resolution of the stated static specialization. The STOC 2026 paper retains the broader static barrier as Open Problem 1.1. The fixed near-linear space, short-query Boolean output and uniform polynomial-time family are an expressly recorded specialization; conditional proof barriers and bounds for dynamic memory or superpolynomial query sets do not resolve it.

Sources: [The Natural Proofs Barrier against Data-Structure Lower-Bounds](https://doi.org/10.1145/3798129.3800843); [Stronger Cell Probe Lower Bounds via Local PRGs](https://eccc.weizmann.ac.il/report/2025/030/); [Lower Bounds for Linear Operators](https://eccc.weizmann.ac.il/report/2025/155/); [Crossing the Logarithmic Barrier for Dynamic Boolean Data Structure Lower Bounds](https://epubs.siam.org/doi/10.1137/18M1198429); [An \(\Omega ((\log  n/\log  \log  n)^{2})\) Cell-Probe Lower Bound for Dynamic Boolean Data Structures](https://eccc.weizmann.ac.il/report/2026/047/).

### 2. Dynamic optimality conjecture

[TCS-6498](../../data/cards/TCS-6498.json) · reused · status: `source_open` · evidence: `reviewed`.

Dynamic optimality concerns the limits of the adaptive data structures he studies.

**Status scope:** The July 2026 primary preprint gives a growing competitive factor and still distinguishes its theorem from constant dynamic optimality. The primary text and subsequent-result searches were checked on 11 September 2026; no complete resolution was found in that check. This review does not independently verify the new proof.

Sources: [Splay trees are almost dynamically optimal](https://arxiv.org/abs/2607.18498); [Binary Search Trees and Dynamic Optimality, Lecture 23](https://www.cs.cmu.edu/~yangp/15-451/lecture23.pdf); [Dynamic Optimality—Almost](https://doi.org/10.1137/S0097539705447347); [What Does Dynamic Optimality Mean in External Memory?](https://doi.org/10.4230/LIPIcs.ITCS.2022.18).

## 64. Karl Bringmann

[Research bibliography](https://dblp.org/pid/96/2643.html).

### 1. Min-Plus Convolution Hypothesis

[TCS-6598](../../data/cards/TCS-6598.json) · reused · status: `source_open` · evidence: `reviewed`.

Min-plus convolution is central to his fine-grained algorithm program.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. Completes the existing TCS-6598 integer-word target, including output indexing, magnitude quantifiers, bounded error and worst-case cost. The established hypothesis title is retained; the yes/no statement asks whether its algorithmic negation holds.

Sources: [Deterministic Monotone Min-Plus Product and Convolution](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.119); [Necklaces, Convolutions, and \(X+Y\)](https://tmc.web.engr.illinois.edu/convol.pdf).

### 2. Near-linear output-sensitive Subset Sum

[TCS-7350](../../data/cards/TCS-7350.json) · reused · status: `source_open` · evidence: `reviewed`.

Output-sensitive Subset Sum directly extends his pseudopolynomial algorithms.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. The explicit input-reading term, multiplicities, truncation and word length are fixed. Algorithms is the editorial home because the target is a basic pseudopolynomial computation measured by its support size, closely tied to convolution; it is not counting the number of solutions.

Sources: [Top-k-Convolution and the Quest for Near-Linear Output-Sensitive Subset Sum](https://arxiv.org/abs/2107.13206); [Derandomizing Pseudopolynomial Algorithms for Subset Sum](https://arxiv.org/abs/2601.01390).

## 65. Amir Abboud

[Research bibliography](https://dblp.org/pid/129/1654.html).

### 1. Truly subcubic APSP

[TCS-6510](../../data/cards/TCS-6510.json) · reused · status: `open` · evidence: `reviewed`.

Truly subcubic APSP is a foundational target of his fine-grained complexity work.

**Status scope:** Reviewed 10 September 2026. The target is a fixed exponent saving for arbitrary real edge weights; the 2026 node-weighted triangle result does not supply it.

Sources: [Subcubic Equivalences between Path, Matrix and Triangle Problems](https://doi.org/10.1109/FOCS.2010.67); [Faster all-pairs shortest paths via circuit complexity](https://arxiv.org/abs/1312.6680); [Node-Weighted Triangles: Faster and Simpler](https://arxiv.org/abs/2605.08588).

### 2. Truly subquadratic algorithms for 3SUM

[TCS-0557](../../data/cards/TCS-0557.json) · reused · status: `uncertain` · evidence: `index`.

The 3SUM barrier concerns his fine-grained reductions and algorithmic lower bounds.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [The Open Problems Project](https://topp.openproblem.net/p11).

## 66. Eshan Chattopadhyay

[Research bibliography](https://dblp.org/pid/117/3135.html).

### 1. Two-source extraction at log n plus constant entropy

[TCS-7271](../../data/cards/TCS-7271.json) · reused · status: `source_open` · evidence: `reviewed`.

Entropy-threshold extraction directly extends his two-source extractor breakthrough.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Two Source Extractors for Asymptotically Optimal Entropy, and (Many) More](https://arxiv.org/abs/2303.06802).

### 2. Seeded extraction with constant total entropy loss

[TCS-1015](../../data/cards/TCS-1015.json) · reused · status: `uncertain` · evidence: `index`.

Optimal seeded extraction is central to his randomness-extraction research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 67. David Zuckerman

[Research bibliography](https://dblp.org/pid/z/DZuckerman.html).

### 1. Two-source extraction at log n plus constant entropy

[TCS-7271](../../data/cards/TCS-7271.json) · reused · status: `source_open` · evidence: `reviewed`.

Near-threshold two-source extraction continues his explicit-extractor work.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Two Source Extractors for Asymptotically Optimal Entropy, and (Many) More](https://arxiv.org/abs/2303.06802).

### 2. Optimal-size highly unbalanced lossless expanders

[TCS-1013](../../data/cards/TCS-1013.json) · reused · status: `uncertain` · evidence: `index`.

Unbalanced lossless expansion connects his extractor and pseudorandom construction program.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 68. Rocco Servedio

[Research bibliography](https://dblp.org/pid/s/RAServedio.html).

### 1. Mansour’s conjecture

[TCS-6581](../../data/cards/TCS-6581.json) · reused · status: `source_open` · evidence: `reviewed`.

Mansour's conjecture connects his Fourier-analytic learning research.

**Status scope:** Open in the strong logarithmic-accuracy form stated here, following the inspected primary sources and a later-result search through 11 September 2026. Fixed-error polynomial concentration, restricted DNF models, and generalized-basis learning results do not by themselves settle this formulation.

Sources: [The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions](https://www.ias.edu/sites/default/files/math/ODonnell_Fourier.pdf); [Mansour’s Conjecture is True for Random DNF Formulas](https://eccc.weizmann.ac.il/report/2010/023/revision/3/download/); [Sharper bounds on the Fourier concentration of DNFs](https://arxiv.org/abs/2109.04525v2); [A New Bound for the Fourier-Entropy-Influence Conjecture](https://link.springer.com/article/10.1007/s00493-024-00133-z); [Further evidence towards the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/2606.00246v2); [Learning DNF through Generalized Fourier Representations](https://arxiv.org/abs/2506.01075v2).

### 2. Learning Boolean juntas from uniform random examples

[TCS-6543](../../data/cards/TCS-6543.json) · reused · status: `source_open` · evidence: `reviewed`.

Uniform-distribution junta learning is a core problem in his learning work.

**Status scope:** No general learner with the stated polynomial dependence, or impossibility theorem for unrestricted learners, was found through 11 September 2026. Current sources retain the uniform-example barrier. Efficient membership-query, monotone-junta and correlated-random-walk results do not meet this exact model.

Sources: [Learning functions of k relevant variables; author manuscript titled Learning juntas](https://www.cs.cmu.edu/~odonnell/papers/juntas.pdf); [Finding Correlations in Subquadratic Time, with Applications to Learning Parities and the Closest Pair Problem](https://theory.stanford.edu/~valiant/papers/corrFull.pdf); [The Probably Approximately Correct Learning Model in Computational Learning Theory](https://arxiv.org/abs/2511.08791); [New Statistical and Computational Results for Learning Junta Distributions](https://arxiv.org/abs/2505.05819); [The Benefits of Temporal Correlations: SGD Learns k-Juntas from Random Walks Efficiently](https://arxiv.org/abs/2605.10237); [Inherited OpenReview research pointer; bibliographic identity not verified](https://openreview.net/pdf?id=wszZlP1K14); [Mathematics and Computation (March 27, 2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf).

## 69. Xi Chen

[Research bibliography](https://dblp.org/pid/16/3283-1.html).

### 1. Learning decision trees from uniform random examples in polynomial time

[TCS-7294](../../data/cards/TCS-7294.json) · reused · status: `source_open` · evidence: `reviewed`.

Efficient uniform decision-tree learning connects his learning-complexity research.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Decision trees are PAC-learnable from most product distributions: a smoothed analysis](https://arxiv.org/abs/0812.0933); [Backdoor Defense, Learnability and Obfuscation](https://doi.org/10.4230/LIPIcs.ITCS.2025.38).

### 2. Effective classification of polynomially testable hereditary graph properties

[TCS-6630](../../data/cards/TCS-6630.json) · reused · status: `source_open` · evidence: `reviewed`.

Efficient testability of hereditary graph properties concerns his property-testing work.

**Status scope:** Reviewed through 11 September 2026. The source’s finite-family structural classification remains incomplete in the checked literature. This card explicitly asks its effective decidability version. The August 2026 container theorem does not provide the required terminating classifier.

Sources: [Polynomial Property Testing](https://arxiv.org/html/2508.16878v1); [A Characterization of the (Natural) Graph Properties Testable with One-Sided Error](https://epubs.siam.org/doi/10.1137/06064888X); [Removal Lemmas with Polynomial Bounds](https://arxiv.org/abs/1611.10315); [Easily Testable Graph Properties](https://www.cambridge.org/core/product/identifier/S0963548314000765/type/journal_article); [Efficient Removal without Efficient Regularity](https://arxiv.org/abs/1709.08159); [A Quantitative Container Characterization of One-Sided Testability](https://eccc.weizmann.ac.il/report/2026/144/).

## 70. Vincent Cohen-Addad

[Research bibliography](https://dblp.org/pid/136/5814.html).

### 1. Optimal polynomial-time approximation ratio for Euclidean k-means

[TCS-7353](../../data/cards/TCS-7353.json) · added · status: `source_open` · evidence: `reviewed`.

Optimal high-dimensional k-means approximation directly extends his clustering results.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654); [A (4 + epsilon)-Approximation for Euclidean k-Means via Non-Monotone Dual-Fitting](https://doi.org/10.1145/3798129.3800894).

### 2. Constant-factor approximation for Dasgupta’s hierarchical clustering objective

[TCS-7318](../../data/cards/TCS-7318.json) · reused · status: `source_open` · evidence: `reviewed`.

Hierarchical clustering approximation is a direct research theme.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. The question is the unrestricted graph objective. No data stability or external clustering oracle is assumed.

Sources: [A cost function for similarity-based hierarchical clustering](https://arxiv.org/abs/1510.05043); [Approximate Hierarchical Clustering via Sparsest Cut and Spreading Metrics](https://arxiv.org/abs/1609.09548).

## 71. Sepehr Assadi

[Research bibliography](https://dblp.org/pid/125/2903.html).

### 1. Fully dynamic near-optimal matching with polylogarithmic updates

[TCS-6627](../../data/cards/TCS-6627.json) · reused · status: `source_open` · evidence: `reviewed`.

Near-optimal dynamic matching connects his matching and graph-algorithm research.

**Status scope:** Reviewed through 11 September 2026. No polylogarithmic-update algorithm meeting the fixed-accuracy, explicit-matching target was found. Matching-size estimators, ordered-RS-dependent bounds and the 2026 maximal-matching improvement do not resolve it.

Sources: [Sixteenth Biennial Scientific Report: March 2021–March 2023](https://pure.mpg.de/pubman/item/item_3527212_4/component/file_3527885/biennial-report-2023.pdf); [Fully Dynamic Matching: \((2- \sqrt{2})\)-Approximation in Polylog Update Time](https://epubs.siam.org/doi/10.1137/1.9781611977912.109); [Improved Bounds for Fully Dynamic Matching via Ordered Ruzsa-Szemeredi Graphs](https://arxiv.org/abs/2406.13573); [A note on Ordered Ruzsa-Szemerédi graphs](https://arxiv.org/abs/2502.02455); [On Approximate Fully-Dynamic Matching and Online Matrix-Vector Multiplication](https://arxiv.org/abs/2403.02582); [A Faster Deterministic Algorithm for Fully Dynamic Maximal Matching](https://arxiv.org/abs/2605.00797).

### 2. Directed reachability with nearly linear memory and polylogarithmic passes

[TCS-6556](../../data/cards/TCS-6556.json) · reused · status: `source_open` · evidence: `reviewed`.

Directed reachability in small memory connects his streaming-complexity work.

**Status scope:** The primary survey, cited multipass bounds and the revision of 9 September 2026 were checked on 11 September 2026. The recent paper explicitly retains the \(n^{1/2+o(1)}\)-pass upper benchmark. No polylogarithmic-pass algorithm or lower bound ruling out every polylogarithmic pass bound in the stated memory model was found. This check covers decision with adversarial fixed order, rather than a changed stream or a path-output requirement.

Sources: [Recent Advances in Multi-Pass Graph Streaming Lower Bounds](https://par.nsf.gov/servlets/purl/10488812); [Superlinear lower bounds for multipass graph processing](https://eccc.weizmann.ac.il/report/2013/002/revision/3/download/); [Parallel Reachability in Almost Linear Work and Square Root Depth](https://arxiv.org/abs/1905.08841); [Semi-Streaming Bipartite Matching in Fewer Passes and Optimal Space](https://arxiv.org/abs/2011.03495); [Almost Optimal Super-Constant-Pass Streaming Lower Bounds for Reachability](https://par.nsf.gov/servlets/purl/10315017); [Streaming Algorithms for Monotonicity Testing](https://arxiv.org/abs/2608.07073v2).

## 72. Monika Henzinger

[Research bibliography](https://dblp.org/pid/h/MonikaRauchHenzinger.html).

### 1. Deterministic fully dynamic connectivity with polylogarithmic worst-case updates

[TCS-6625](../../data/cards/TCS-6625.json) · reused · status: `source_open` · evidence: `reviewed`.

Deterministic dynamic connectivity is central to her dynamic graph program.

**Status scope:** Checked through 10 September 2026. The SODA 2026 connectivity paper explicitly retains deterministic polylogarithmic worst-case updates as open. Its unconditional new bound is randomized and expected; its deterministic polylogarithmic conclusion depends on the stated static low-congestion sparsifier construction. Deterministic subpolynomial worst-case bounds and polylogarithmic amortized bounds are already known.

Sources: [Poly-Logarithmic Deterministic Fully-Dynamic Algorithms for Connectivity, Minimum Spanning Tree, 2-Edge, and Biconnectivity](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf); [Dynamic graph connectivity in polylogarithmic worst case time](https://doi.org/10.1137/1.9781611973105.81); [A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond](https://arxiv.org/abs/1910.08025); [Dynamic Connectivity with Expected Polylogarithmic Worst-Case Update Time](https://arxiv.org/abs/2510.08297); [Expander Pruning with Polylogarithmic Worst-Case Recourse and Update Time](https://doi.org/10.1137/1.9781611978971.103); [Logarithmic Lower Bounds in the Cell-Probe Model](https://erikdemaine.org/papers/DynamicConnectivity_SICOMP/).

### 2. Optimal error for pure-DP continual counting

[TCS-6673](../../data/cards/TCS-6673.json) · reused · status: `open` · evidence: `reviewed`.

Optimal private continual counting connects her privacy-preserving dynamic algorithms.

**Status scope:** Checked through 11 September 2026. No matching order for the stated unrestricted causal pure-DP expected-maximum error was located. The July source records \(\Omega (\log ^{3/2}T)\) versus \(O(\log ^{2}T)\); later factorization results use restricted mechanisms and different error criteria. New preprint proofs were not independently audited.

Sources: [The Binary Tree Mechanism is Optimal for Approximate Differentially Private Continual Counting](https://arxiv.org/abs/2607.00876v2); [The Price of Differential Privacy under Continual Observation](https://proceedings.mlr.press/v202/jain23b.html); [Improved Error Bounds for Pure Differentially Private Continual Counting via Matrix Factorization](https://arxiv.org/abs/2607.08963); [Costs of Arbitrary Real Matrix Factorizations for Pure-DP Continual Counting](https://arxiv.org/abs/2607.28703v2); [A Near-Optimal Lower Bound for Prefix-Matrix Factorizations](https://arxiv.org/abs/2608.08238).

## 73. Shiri Chechik

[Research bibliography](https://dblp.org/pid/38/2434.html).

### 1. Optimal additive error of linear-size spanners

[TCS-6785](../../data/cards/TCS-6785.json) · reused · status: `source_open` · evidence: `reviewed`.

Linear-size additive spanners concern her graph-distance structures.

**Status scope:** The survey leaves the linear-size error tradeoff open. The later lower-bound and nearly linear upper-bound abstracts were checked on 13 September 2026 and do not give matching bounds for every fixed linear coefficient. No full determination was verified; status remains source_open.

Sources: [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152); [New Additive Spanner Lower Bounds by an Unlayered Obstacle Product](https://arxiv.org/abs/2207.11832); [Almost-Optimal Sublinear Additive Spanners](https://arxiv.org/abs/2303.12768).

### 2. Subquadratic exact fully dynamic weighted single-source distances

[TCS-5209](../../data/cards/TCS-5209.json) · reused · status: `source_open` · evidence: `reviewed`.

Fully dynamic exact SSSP is a major frontier for her dynamic graph algorithms.

**Status scope:** The 2017 blanket rebuilding remark is obsolete for several variants. This user-authorized exact weighted variant was specified on 13 September 2026; the checked later sources separate it from approximate and unweighted results. Their conditional barriers are not an unconditional resolution, and no exact new theorem for the selected model was identified in the bounded search.

Sources: [Deterministic Partially Dynamic Single Source Shortest Paths in Weighted Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2017.44); [Deterministic Partially Dynamic Single Source Shortest Paths in Weighted Graphs — full version](https://arxiv.org/abs/1705.10097); [Dynamic Approximate Shortest Paths and Beyond: Subquadratic and Worst-Case Update Time](https://arxiv.org/abs/1909.10850); [Deterministic Fully Dynamic SSSP and More](https://doi.org/10.1109/FOCS57990.2023.00142).

## 74. Anupam Gupta

[Research bibliography](https://dblp.org/pid/27/2931.html).

### 1. Optimal competitive ratio for convex body chasing

[TCS-6576](../../data/cards/TCS-6576.json) · reused · status: `source_open` · evidence: `source`.

Convex body chasing connects his online geometric algorithms.

**Status scope:** Retained in the source-based research proposal dated 10 September 2026. No full resolution was found in that search; this is not a completed independent open-status review.

Sources: [Research reference · theory.epfl.ch](https://theory.epfl.ch/WinterSchool2025/slides/2025/Gupta_lec4-chasing.pdf).

### 2. Constant-distortion Steiner point removal

[TCS-6527](../../data/cards/TCS-6527.json) · reused · status: `source_open` · evidence: `source`.

Steiner point removal concerns his metric approximation and graph-compression research.

**Status scope:** Retained in the source-based research proposal dated 10 September 2026. No full resolution was found in that search; this is not a completed independent open-status review.

Sources: [Research reference · epubs.siam.org](https://epubs.siam.org/doi/10.1137/1.9781611977912.191).

## 75. Debmalya Panigrahi

[Research bibliography](https://dblp.org/pid/81/6547.html).

### 1. Strongly polynomial maximum flow below the \(mn\) barrier

[TCS-7346](../../data/cards/TCS-7346.json) · reused · status: `source_open` · evidence: `reviewed`.

Strongly polynomial faster max flow extends his flow and cut work.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. The explicitly sourced exponent-saving question is made precise for finite rational capacities, with bounded-error randomization and worst-case operation cost. The rational encoding condition is separate from the arithmetic count.

Sources: [From Incremental Transitive Cover to Strongly Polynomial Maximum Flow](https://arxiv.org/abs/2510.20368); [Krajinou grafových algoritmů](https://mj.ucw.cz/vyuka/ga/ga.pdf).

### 2. Polylogarithmic maintenance of the exact global minimum cut

[TCS-6670](../../data/cards/TCS-6670.json) · reused · status: `source_open` · evidence: `reviewed`.

Fast dynamic exact min cut connects his graph optimization research.

**Status scope:** Reviewed through 11 September 2026. No exact fully dynamic algorithm meeting the polylogarithmic bounds at unrestricted connectivity was found in the checked primary sources. The 2026 exact \(n^{o(1)}\) result has a cut-size restriction, and the unrestricted 2026 tree-packing bound remains polynomial rather than polylogarithmic.

Sources: [Deterministic and Exact Fully-dynamic Minimum Cut of Superpolylogarithmic Size in Subpolynomial Time](https://arxiv.org/abs/2512.13105); [Unifying and Strengthening Hardness for Dynamic Problems via the Online Matrix-Vector Multiplication Conjecture](https://people.csail.mit.edu/virgi/6.s078/papers/omv.pdf); [Incremental Exact Min-Cut in Polylogarithmic Amortized Update Time](https://arxiv.org/abs/1611.06500); [Fully Dynamic Exact Edge Connectivity in Sublinear Time](https://arxiv.org/abs/2302.05951); [Tree-Packing Revisited: Faster Fully Dynamic Min-Cut and Arboricity](https://link.springer.com/article/10.1007/s00453-026-01394-4); [Fully Dynamic Approximate Minimum Cut in Subpolynomial Time per Operation](https://arxiv.org/abs/2412.15069).

## 76. Noga Alon

[Research bibliography](https://dblp.org/pid/a/NAlon.html).

### 1. Erdős girth conjecture

[TCS-6500](../../data/cards/TCS-6500.json) · reused · status: `open` · evidence: `reviewed`.

The girth conjecture connects his extremal graph theory to spanner lower bounds.

**Status scope:** Reviewed 10 September 2026. The general conjecture remains unresolved; several individual values of k are settled.

Sources: [Unconditional Lower Bounds for Degree Fault Tolerant Spanners](https://doi.org/10.4230/LIPIcs.ESA.2026.31); [On Sparse Spanners of Weighted Graphs](https://doi.org/10.1007/BF02189308).

### 2. Optimal asymptotic binary rate–distance tradeoff

[TCS-1010](../../data/cards/TCS-1010.json) · reused · status: `source_open` · evidence: `reviewed`.

The binary rate-distance tradeoff is a central extremal-coding question related to his combinatorial work.

**Status scope:** Checked through 10 September 2026. The August and September primary sources report genuine asymptotic upper-bound improvements beyond MRRW, but retain a gap above the binary GV lower curve. The exact function remains undetermined; polynomial multiplicative size improvements and results for other alphabets or coding models do not settle it. The 12 September 2026 edit adopts absolute 0.01 benchmark acceptance; the saved open-status evidence concerns the underlying exact question and does not independently certify openness at that tolerance.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/); [New upper bounds on the rate of a code via the Delsarte–MacWilliams inequalities](https://doi.org/10.1109/TIT.1977.1055688); [Asymptotic Improvement of the Gilbert–Varshamov Bound on the Size of Binary Codes](https://arxiv.org/abs/math/0404325); [Improvement of the Gilbert-Varshamov Bound for Linear Codes and Quantum Codes](https://arxiv.org/abs/2601.18590); [Binary code rate bounds via classical–quantum channels](https://arxiv.org/abs/2608.09347); [Comments on the recent improvements of the MRRW bounds](https://arxiv.org/abs/2609.01860).

## 77. Elchanan Mossel

[Research bibliography](https://dblp.org/pid/m/EMossel.html).

### 1. Computational Kesten–Stigum threshold

[TCS-6684](../../data/cards/TCS-6684.json) · reused · status: `source_open` · evidence: `reviewed`.

The computational Kesten-Stigum threshold connects his reconstruction and stochastic-block-model work.

**Status scope:** Efficient recovery above the threshold and information-theoretic recovery below it in suitable fixed-q assortative regimes are proved. The checked fixed-community computational lower bound remains conditional on an unproved low-degree conjecture. Growing-community algorithms in the August 2026 revision concern a different quantifier regime. No unconditional settlement of this precise fixed-q question found through 11 September 2026.

Sources: [Detection in the stochastic block model with multiple clusters: proof of the achievability conjectures, acyclic BP, and the information-computation gap](https://arxiv.org/abs/1512.09080); [Information-theoretic thresholds for community detection in sparse networks](https://proceedings.mlr.press/v49/banks16.html); [Low degree conjecture implies sharp computational thresholds in stochastic block model](https://arxiv.org/abs/2502.15024); [Stochastic block models with many communities and the Kesten–Stigum bound](https://arxiv.org/abs/2503.03047).

### 2. Fourier Entropy–Influence conjecture

[TCS-6604](../../data/cards/TCS-6604.json) · reused · status: `source_open` · evidence: `reviewed`.

Fourier entropy-influence is directly in the Boolean-analysis area he helped develop.

**Status scope:** Checked through 10 September 2026. The June 2026 primary paper explicitly retains classical FEI as open and proves only specified classes. The August 2026 disproof is of the quantum extension. No classical resolution was found in the checked sources; the formulation uses Shannon entropy, uniform measure and scalar Boolean functions throughout.

Sources: [The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions](https://www.cs.cmu.edu/~jswright/papers/fei.pdf); [A new bound for the Fourier-Entropy-Influence conjecture](https://arxiv.org/abs/2312.08271); [Further evidence towards the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/2606.00246); [Dense Hamiltonians at the Parseval Limit: The Noncommutative BH Constant is Exponential and the Quantum FEI Conjecture is False](https://arxiv.org/abs/2608.01424).

## 78. Allan Sly

[Research bibliography](https://dblp.org/pid/36/3231.html).

### 1. Algorithmic threshold for random k-SAT

[TCS-4876](../../data/cards/TCS-4876.json) · reused · status: `open` · evidence: `reviewed`.

Algorithmic random-SAT thresholds directly concern his random-CSP work.

**Status scope:** Read the conference source and full July 2025 version, the Fix publisher abstract and author introduction, and the full low-degree definitions and principal theorem statements. Searches through 12 September 2026 found no resolution for arbitrary polynomial-time assignment finding. The supremum definition spells out the source’s asymptotic algorithmic-threshold question. The source’s damaged saved density and its separate incidental logarithm typo are not used as mathematical definitions.

Sources: [Sharp Thresholds for the Overlap Gap Property: Ising p-Spin Glass and Random k-SAT](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2025.48); [Sharp Thresholds for the Overlap Gap Property: Ising p-Spin Glass and Random k-SAT — full version](https://arxiv.org/abs/2309.09913); [A Better Algorithm for Random k-SAT](https://doi.org/10.1137/09076516X); [The Algorithmic Phase Transition of Random k-SAT for Low Degree Polynomials](https://arxiv.org/abs/2106.02129).

### 2. Polynomial mixing of critical three-dimensional Ising dynamics

[TCS-6668](../../data/cards/TCS-6668.json) · reused · status: `source_open` · evidence: `source`.

Critical 3D Ising mixing connects his computational statistical-physics research.

**Status scope:** Retained in the source-based research proposal dated 10 September 2026. High-dimensional lattice results and the 2024 result at the tree uniqueness threshold do not resolve the three-dimensional lattice critical point. Status is assessed from these primary results and later-result searches.

Sources: [Log-Sobolev inequality for near critical Ising models](https://arxiv.org/abs/2202.02301); [Polynomial Mixing of the critical Glauber Dynamics for the Ising Model](https://arxiv.org/abs/2411.10318).

## 79. Shafi Goldwasser

[Research bibliography](https://dblp.org/pid/g/ShafiGoldwasser.html).

### 1. One-way functions from \(\mathrm{P} \ne  \mathrm{NP}\)

[TCS-0022](../../data/cards/TCS-0022.json) · reused · status: `source_open` · evidence: `reviewed`.

OWFs from worst-case complexity concerns the foundations of cryptography she co-established.

**Status scope:** Explicitly open in the original source. Primary literature was checked through 10 September 2026; no derivation of eventually secure classical one-way functions from \(\mathrm{P}\ne \mathrm{NP}\) alone was located. The security quantifiers are stronger than an infinitely-often one-wayness target.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3); [A Pseudorandom Generator from any One-way Function](https://johanhastad.se/prgfromowf.pdf); [On Worst-Case to Average-Case Reductions for NP Problems](https://lucatrevisan.github.io/pubs/BT03.pdf); [One-Way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://doi.org/10.4230/LIPIcs.ITCS.2026.97).

### 2. Public-key encryption from one-way functions

[TCS-6545](../../data/cards/TCS-6545.json) · reused · status: `source_open` · evidence: `reviewed`.

PKE from OWFs is a fundamental assumption gap in her field.

**Status scope:** Explicitly open in the supplied MIT lecture. Research through 10 September 2026 found no standard-model implication from arbitrary OWFs alone or refutation of that general implication. The formulation fixes uniform classical adversaries and allows non-black-box constructions; oracle barriers and stronger concrete assumptions are kept separate.

Sources: [Foundations of Cryptography, Lecture 10](https://mit6875.github.io/FA23SLIDES/lec10.pdf); [The Complexity of Public-Key Cryptography](https://eprint.iacr.org/2017/365); [Limits on the provable consequences of one-way permutations](https://doi.org/10.1145/73007.73012); [A Pseudorandom Generator from any One-way Function](https://johanhastad.se/prgfromowf.pdf); [Merkle Puzzles are Optimal — an \(O(n^{2})\)-query attack on any key exchange from a random oracle](https://www.boazbarak.org/Papers/merkle.pdf); [Public-Key Encryption from the MinRank Problem](https://arxiv.org/abs/2510.03752).

## 80. Chandra Chekuri

[Research bibliography](https://dblp.org/pid/82/3212.html).

### 1. Polylogarithmic approximation for Directed Steiner Tree

[TCS-6588](../../data/cards/TCS-6588.json) · reused · status: `source_open` · evidence: `reviewed`.

Directed Steiner approximation connects his network-design work.

**Status scope:** The July 2026 primary literature explicitly leaves this general-graph question open. The inherited 2024 claim was withdrawn, and its October 2025 replacement is restricted to a special supplied fractional solution; that claim is not counted as an established general result. Planar and quasipolynomial algorithms do not satisfy this card. Checked through 11 September 2026.

Sources: [Approximation Algorithms for Directed Steiner Problems](https://chekuri.web.engr.illinois.edu/pub.html); [\(O(\log ^{2} k/\log  \log  k)\)-Approximation Algorithm for Directed Steiner Tree: A Tight Quasi-Polynomial-Time Algorithm](https://people.idsia.ch/~grandoni/Pubblicazioni/GLL19stoc.pdf); [An \(O(\log  k)\)-Approximation for Directed Steiner Tree in Planar Graphs](https://arxiv.org/abs/2302.04747); [From Directed Steiner Tree to Directed Polymatroid Steiner Tree in Planar Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.42); [On the Integrality Gap of Directed Steiner Tree LPs with Relatively Integral Solutions](https://arxiv.org/abs/2412.10744); [Length-Constrained Network Design in Planar Digraphs](https://arxiv.org/abs/2607.25811).

### 2. Optimal approximation for submodular maximization over a matroid

[TCS-5407](../../data/cards/TCS-5407.json) · reused · status: `uncertain` · evidence: `source`.

Optimal matroid-constrained submodular approximation is directly in his submodular-optimization program.

**Status scope:** Question recorded in a source from 2022; subsequent results and present open status have not been individually checked.

Sources: [On Maximizing Sums of Non-Monotone Submodular and Linear Functions](https://doi.org/10.4230/LIPIcs.ISAAC.2022.41).

## 81. Ken-ichi Kawarabayashi

[Research bibliography](https://dblp.org/pid/45/6846.html).

### 1. Optimal bounds in the Excluded Grid Theorem

[TCS-6683](../../data/cards/TCS-6683.json) · reused · status: `source_open` · evidence: `reviewed`.

Excluded-grid bounds concern his structural graph theory and algorithms.

**Status scope:** The checked general bounds remain \(\Omega (r^{2} \log  r)\) and \(O(r^{9} \operatorname{polylog} r)\). The November 2025 product-structure result and SODA 2026 fixed-minor result refine different aspects and do not determine the all-graphs threshold. No matching asymptotic bounds found through 11 September 2026. The problem does not assume that either the near-quadratic or cubic conjecture is correct.

Sources: [Graph minors. V. Excluding a planar graph](https://doi.org/10.1016/0095-8956(86)90030-4); [Quickly Excluding a Planar Graph](https://www.sciencedirect.com/science/article/pii/S0095895684710732); [Polynomial Bounds for the Grid-Minor Theorem](https://arxiv.org/abs/1305.6577); [Towards \(Tight(er)\) Bounds for the Excluded Grid Theorem](https://arxiv.org/abs/1901.07944); [The Grid-Minor Theorem Revisited](https://link.springer.com/article/10.1007/s00493-025-00168-w); [Catching Rats in H-minor-free Graphs](https://arxiv.org/abs/2506.22857).

### 2. Hadwiger’s conjecture

[TCS-6651](../../data/cards/TCS-6651.json) · reused · status: `source_open` · evidence: `reviewed`.

Hadwiger's conjecture is a central graph-minor and coloring target related to his work.

**Status scope:** Ordinary Hadwiger remains explicitly open in the 9 September 2026 preprint; checked through 10 September 2026. The new triple-logarithmic upper bound is a preprint claim. The December 2025 disproof concerns the stronger odd-minor conjecture.

Sources: [Beyond Halfway to Hadwiger’s Conjecture](https://arxiv.org/abs/2609.06867v2); [Reducing Linear Hadwiger’s Conjecture to Coloring Small Graphs](https://arxiv.org/abs/2108.01633v5); [Hadwiger’s conjecture for K6-free graphs](https://doi.org/10.1007/BF01202354); [Disproof of the Odd Hadwiger Conjecture](https://arxiv.org/abs/2512.20392).

## 82. Dániel Marx

[Research bibliography](https://dblp.org/pid/95/1832.html).

### 1. FPT versus \(\mathrm{W}[1]\)

[TCS-6592](../../data/cards/TCS-6592.json) · reused · status: `source_open` · evidence: `reviewed`.

FPT versus W[1] underlies his parameterized complexity research.

**Status scope:** Explicitly presented as the central open conjecture in Bottesch’s primary paper and the parameterized-algorithms textbook. Research through 10 September 2026 located no proof of equality or separation. Conditional lower bounds and improved fixed-k algorithms are recorded with their distinct quantifiers.

Sources: [Parameterized Algorithms](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf); [On \(\mathrm{W}[1]\)-Hardness as Evidence for Intractability](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2018.73); [Constant Approximating k-Clique is \(\mathrm{W}[1]\)-hard](https://arxiv.org/abs/2102.04769); [Simple Combinatorial Construction of the \(k^{o(1)}\)-Lower Bound for Approximating the Parameterized k-Clique](https://arxiv.org/abs/2304.07516); [Faster Combinatorial k-Clique Algorithms](https://weizmann.elsevierpure.com/en/publications/faster-combinatorial-k-clique-algorithms-2/).

### 2. Set Cover Conjecture

[TCS-6594](../../data/cards/TCS-6594.json) · reused · status: `source_open` · evidence: `source`.

Set Cover exponents connect his fine-grained and parameterized lower-bound program.

**Status scope:** Retained in the source-based research proposal dated 10 September 2026. No full resolution was found in that search; this is not a completed independent open-status review.

Sources: [Research reference · drops.dagstuhl.de](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.34).

## 83. László Végh

[Research bibliography](https://dblp.org/pid/12/2680.html).

### 1. Strongly polynomial linear programming

[TCS-0008](../../data/cards/TCS-0008.json) · reused · status: `uncertain` · evidence: `reviewed`.

Strongly polynomial LP is a direct focus of his optimization work.

**Status scope:** The standard problem remains listed as open, but a direct claimed solution exists in Awoniyi’s July 2026 revision. This card records it without treating it as established: correctness, the iteration bound, and the full strongly polynomial guarantee have not been independently validated in this review. Checked through 10 September 2026.

Sources: [Problem 8: Linear Programming: Strongly Polynomial?](https://topp.openproblem.net/p8); [A Strongly Polynomial Algorithm to Solve Combinatorial Linear Programs](https://doi.org/10.1287/opre.34.2.250); [A strongly polynomial algorithm for linear programs with at most two non-zero entries per row or column](https://homepages.cwi.nl/~dadush/papers/genflow.pdf); [No self-concordant barrier interior point method is strongly polynomial](https://arxiv.org/abs/2201.02186); [Trust Region Interior Point Methods: Optimal l2- and Faster Wide-Neighborhood Path Following](https://homepages.cwi.nl/~dadush/papers/trust-region.pdf); [A strongly polynomial-time algorithm for the general linear programming problem](https://arxiv.org/abs/2503.12041v10).

### 2. Polynomial-time simplex pivot rule

[TCS-6572](../../data/cards/TCS-6572.json) · reused · status: `source_open` · evidence: `reviewed`.

Strongly polynomial simplex pivots concern his combinatorial approach to linear programming.

**Status scope:** Checked through 10 September 2026. The STACS 2026 and March 2026 primary publications retain the general polynomial simplex question as open. This card fixes deterministic total bit complexity for legal improving primal-simplex pivots from any supplied feasible basis on a finite-optimum rational LP. Strongly polynomial algorithms, nonlinear active-set bounds and distributional performance are distinct formulations.

Sources: [Smoothed Analysis of Algorithms: Why the Simplex Algorithm Usually Takes Polynomial Time](https://www.cs.yale.edu/homes/spielman/simplex/); [An unconditional lower bound for the active-set method on the hypercube](https://arxiv.org/abs/2502.18019); [An Unconditional Lower Bound for the Active-Set Method in Convex Quadratic Maximization](https://epubs.siam.org/doi/10.1137/1.9781611978971.14); [Lower Bounds for Ranking-Based Pivot Rules](https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.31/LIPIcs.STACS.2026.31.html); [On the number of degenerate simplex pivots](https://link.springer.com/article/10.1007/s10107-026-02349-x).

## 84. Santosh Vempala

[Research bibliography](https://dblp.org/pid/v/SantoshVempala.html).

### 1. Kannan–Lovász–Simonovits conjecture

[TCS-6523](../../data/cards/TCS-6523.json) · reused · status: `source_open` · evidence: `reviewed`.

KLS is central to his convex-body sampling and volume algorithms.

**Status scope:** The full KLS conjecture is explicitly open in the primary sources, including Letwin’s July 2026 preprint. Research through 10 September 2026 found no dimension-free general-function resolution. The recent quadratic-form and thin-shell results are not treated as proofs of the full conjecture; the July bound is labeled as a preprint result.

Sources: [The KLS Conjecture (problem 30)](https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/); [The Kannan–Lovász–Simonovits Conjecture](https://faculty.cc.gatech.edu/~vempala/papers/kls_survey.pdf); [Bourgain’s slicing problem and KLS isoperimetry up to polylog](https://arxiv.org/abs/2203.15551); [Logarithmic bounds for isoperimetry and slices of convex sets](https://www.weizmann.ac.il/math/klartag/sites/math.klartag/files/uploads/root_log.pdf); [Thin-shell bounds via parallel coupling](https://arxiv.org/abs/2507.15495v2); [The KLS constant is \(O(\log ^{1/4} n)\)](https://arxiv.org/abs/2607.24164v1).

### 2. Exact semidefinite feasibility in polynomial time

[TCS-6574](../../data/cards/TCS-6574.json) · reused · status: `source_open` · evidence: `reviewed`.

Exact SDP feasibility concerns the complexity foundations of convex optimization he studies.

**Status scope:** Checked through 10 September 2026. The primary literature retains general exact SDP feasibility as an open polynomial-time problem. Ramana’s dual does not establish \(\mathrm{NP}\cap \mathrm{coNP}\) membership in the Turing model, and recent convex-polynomial optimization results address a different constraint family. This card permits real witnesses, singular feasible points, weak infeasibility and unbounded feasible regions.

Sources: [An exact duality theory for semidefinite programming and its complexity implications](https://link.springer.com/article/10.1007/BF02614433); [On the Turing Model Complexity of Interior Point Methods for Semidefinite Programming](https://epubs.siam.org/doi/10.1137/15M103114X); [Exact algorithms for semidefinite programs with degenerate feasible set](https://www.sciencedirect.com/science/article/pii/S0747717120301176); [How Do Exponential Size Solutions Arise in Semidefinite Programming?](https://epubs.siam.org/doi/10.1137/21M1434945); [A combinatorial approach to Ramana’s exact dual for semidefinite programming](https://arxiv.org/abs/2510.07271); [Hesse’s Redemption: Efficient Convex Polynomial Programming](https://arxiv.org/abs/2511.03440).

## 85. Nikhil Srivastava

[Research bibliography](https://dblp.org/pid/30/2541.html).

### 1. Strongly explicit Ramanujan families for every degree

[TCS-7285](../../data/cards/TCS-7285.json) · reused · status: `source_open` · evidence: `reviewed`.

Explicit Ramanujan construction extends his interlacing-polynomial work.

**Status scope:** The primary source distinguishes available exact special-degree families from arbitrary-degree constructions with slack. The statement and a bounded later-work search were reviewed on 13 September 2026 without finding a general exact strongly explicit construction. This is not a claim of an exhaustive status audit.

Sources: [Explicit expanders of every degree and size](https://arxiv.org/abs/2003.11673).

### 2. Near-lossless undirected constant-degree vertex expanders

[TCS-1009](../../data/cards/TCS-1009.json) · reused · status: `uncertain` · evidence: `index`.

Lossless undirected expansion concerns explicit spectral and combinatorial expander construction.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 86. Seth Pettie

[Research bibliography](https://dblp.org/pid/77/888.html).

### 1. Deterministic linear-time minimum spanning tree

[TCS-6536](../../data/cards/TCS-6536.json) · reused · status: `source_open` · evidence: `reviewed`.

Deterministic linear MST is a foundational problem in his graph-algorithm work.

**Status scope:** The deterministic linear-time comparison problem remains open in the primary-author material checked through 11 September 2026. Integer-word algorithms, high-girth results and the optimal-decision-tree theorem do not settle this formulation.

Sources: [A Randomized Linear-Time Algorithm to Find Minimum Spanning Trees](https://people.csail.mit.edu/karger/Papers/mst.pdf); [A Minimum Spanning Tree Algorithm with Inverse-Ackermann Type Complexity](https://www.cs.princeton.edu/~chazelle/pubs/mst.pdf); [An Optimal Minimum Spanning Tree Algorithm](https://www.cs.princeton.edu/courses/archive/fall05/cos528/handouts/An%20Optimal%20Minimum.pdf); [Trans-dichotomous algorithms for minimum spanning trees and shortest paths](https://www.sciencedirect.com/science/article/pii/S0022000005800649); [Minimum Spanning Tree in Deterministic Linear Time For Graphs of High Girth](https://people.csail.mit.edu/dmoshkov/papers/mst/high-girth.pdf); [Randomized minimum spanning tree algorithms using exponentially fewer random bits](https://web.eecs.umich.edu/~pettie/papers/random-mst.pdf).

### 2. Deque conjecture

[TCS-6508](../../data/cards/TCS-6508.json) · reused · status: `source_open` · evidence: `reviewed`.

The deque conjecture directly concerns his adaptive-search-tree analysis.

**Status scope:** Reviewed 10 September 2026, including the July 2026 splay result. The conjecture asks for linear total cost under insertions and deletions at either end.

Sources: [Splay Trees, Davenport-Schinzel Sequences, and the Deque Conjecture](https://arxiv.org/abs/0707.2160); [A New Path from Splay to Dynamic Optimality](https://doi.org/10.1137/1.9781611975482.80); [Splay trees are almost dynamically optimal](https://arxiv.org/abs/2607.18498).

## 87. Timothy Chan

[Research bibliography](https://dblp.org/pid/60/3556.html).

### 1. Planar k-set extremal function

[TCS-0318](../../data/cards/TCS-0318.json) · reused · status: `source_open` · evidence: `reviewed`.

Planar k-sets is a central open barrier in his computational geometry area.

**Status scope:** The June 2025 problem entry retains the gap. The 2024 halving-line improvement changes lower-order terms rather than the exponent. No matching asymptotic bound was located in the status search through 10 September 2026.

Sources: [The Open Problems Project: Problem 7, k-sets](https://topp.openproblem.net/p7); [Improved Bounds for Planar k-Sets and Related Problems](https://courses.cs.duke.edu/cps234/fall08/handouts/dey.pdf); [Point Sets with Many k-Sets](https://link.springer.com/article/10.1007/s004540010022); [An Improved, Simple Construction of Many Halving Edges](https://rangevoting.org/many_halving_edges.pdf); [An Improvement of the Upper Bound for the Number of Halving Lines of Planar Sets](https://oa.upm.es/89576/1/10302927.pdf).

### 2. Linear-time exact inversion counting

[TCS-7351](../../data/cards/TCS-7351.json) · reused · status: `uncertain` · evidence: `reviewed`.

Linear-time inversion counting extends his fast counting and geometric algorithms.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. The precise target fixes deterministic worst-case time on logarithmic words. The linear endpoint is editorial rather than an attributed conjecture; present-status review remains limited by older direct evidence.

Sources: [Counting Inversions, Offline Orthogonal Range Counting, and Related Problems](https://tmc.web.engr.illinois.edu/inv_7_7_09.pdf); [Counting inversions adaptively](https://arxiv.org/abs/1503.01192).

## 88. Boaz Barak

[Research bibliography](https://dblp.org/pid/b/BBarak.html).

### 1. Planted clique conjecture

[TCS-6656](../../data/cards/TCS-6656.json) · reused · status: `source_open` · evidence: `reviewed`.

Planted clique is central to his work on computational barriers in inference.

**Status scope:** Checked through 10 September 2026; no unrestricted polynomial-time solution below \(n^{1/2- \varepsilon}\) or unconditional hardness proof was identified. The exact formulation fixes constant-success detection and exactly k planted vertices. Low-degree and sum-of-squares bounds remain scoped to their models; the optimal-advantage result is conditional.

Sources: [Finding a Large Hidden Clique in a Random Graph](https://people.math.ethz.ch/~sudakovb/hidden-clique.pdf); [A Nearly Tight Sum-of-Squares Lower Bound for the Planted Clique Problem](https://doi.org/10.1137/17M1138236); [Finding planted cliques using gradient descent](https://arxiv.org/abs/2311.07540v2); [On optimal distinguishers for Planted Clique](https://arxiv.org/abs/2505.01990v2); [Robust Algorithms for Finding Cliques in Random Intersection Graphs via Sum-of-Squares](https://proceedings.mlr.press/v336/gobel26a.html).

### 2. Average-case NP hardness from \(\mathrm{P} \ne  \mathrm{NP}\)

[TCS-0012](../../data/cards/TCS-0012.json) · reused · status: `source_open` · evidence: `reviewed`.

Average-case hardness from worst-case NP hardness connects his complexity and cryptography work.

**Status scope:** The original question is explicitly open in Wigderson’s book and the revised average-case survey. Current primary literature was checked through 10 September 2026; no resolution from \(\mathrm{P}\ne \mathrm{NP}\) alone was located. The card fixes deterministic exact AvgP and strict polynomial-time sampling, rather than conflating them with randomized heuristic hardness.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3); [On Worst-Case to Average-Case Reductions for NP Problems](https://lucatrevisan.github.io/pubs/BT03.pdf); [One-Way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://doi.org/10.4230/LIPIcs.ITCS.2026.97).

## 89. Toniann Pitassi

[Research bibliography](https://dblp.org/pid/p/TPitassi.html).

### 1. Superpolynomial lower bounds for unrestricted Frege proofs

[TCS-0025](../../data/cards/TCS-0025.json) · reused · status: `source_open` · evidence: `reviewed`.

Frege lower bounds are a central target of her proof-complexity program.

**Status scope:** Reviewed through 11 September 2026. No unconditional superpolynomial lower bound for unrestricted Frege proof size was found in the checked primary sources. The April 2026 tree-like result has a line-size cap, the formalization result concerns bounded-depth proofs, and the June 2026 algebraic result does not translate into the required propositional lower bound.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf); [The Relative Efficiency of Propositional Proof Systems](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf); [Polynomial Size Proofs of the Propositional Pigeonhole Principle](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/php_PolyFrege/FregePHP.pdf); [Superpolynomial Length Lower Bounds for Tree-Like Semantic Proof Systems with Bounded Line Size](https://arxiv.org/abs/2604.28172); [\(Res(\log )\) Proves Bounded-Depth Frege Lower Bounds](https://eccc.weizmann.ac.il/report/2026/055/); [A Lower Bound for Polynomial Calculus with Extension Rule](https://mirror.theoryofcomputing.org/articles/v022a004/).

### 2. Log-rank conjecture

[TCS-6603](../../data/cards/TCS-6603.json) · reused · status: `source_open` · evidence: `reviewed`.

Log-rank connects her communication lower bounds and lifting work.

**Status scope:** Explicitly open in the August 2026 CCC version of Hambardzumyan–Lovett–Shirley. Checked through 10 September 2026. The established general upper bound is \(O(\sqrt{r})\); recent fixed-polynomial lower-bound refinements and signed-decomposition equivalences do not settle the conjecture.

Sources: [The Log-Rank Conjecture: New Equivalent Formulations](https://arxiv.org/abs/2510.02583v3); [Matrix discrepancy and the log-rank conjecture](https://doi.org/10.1007/s10107-024-02117-9); [Deterministic Communication vs. Partition Number](https://doi.org/10.1137/16M1059369); [Alphabet-Preserving Lifting for the Log-Rank Conjecture](https://arxiv.org/abs/2608.01812v1).

## 90. Alexander Razborov

[Research bibliography](https://dblp.org/pid/r/AARazborov.html).

### 1. Superpolynomial \(\mathrm{AC}^{0}[p]\)-Frege lower bounds

[TCS-6602](../../data/cards/TCS-6602.json) · reused · status: `source_open` · evidence: `reviewed`.

Modular Frege lower bounds concern his foundational proof-complexity research.

**Status scope:** Checked through 10 September 2026. The 2026 primary sources retain modular Frege lower bounds as open. ITCS 2026.99 does not prove that its hard-to-prove candidates are tautologies. ECCC TR26-018 restricts derivation depth or proves a polynomial size bound; TR26-070 treats a restricted algebraic certificate representation. None establishes the fully specified tautology families and unrestricted derivation size lower bounds requested here.

Sources: [Extended Nullstellensatz proof systems](https://www.karlin.mff.cuni.cz/~krajicek/finitary.pdf); [Exponential Lower Bounds for the Pigeonhole Principle](https://www.cs.toronto.edu/~toni/Papers/exp-pigeon.pdf); [Amortized Closure and Its Applications in Lifting for Resolution over Parities](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.8); [\(\mathrm{AC}^{0}[p]\)-Frege Cannot Efficiently Prove That Constant-Depth Algebraic Circuit Lower Bounds Are Hard](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.99); [Resolution Width Lifts to Near-Quadratic-Depth \(Res(\oplus )\) Size](https://eccc.weizmann.ac.il/report/2026/018/); [Hard CNF Instances for Ideal Proof Systems](https://eccc.weizmann.ac.il/report/2026/070/).

### 2. Majority outside constant-depth modular circuits

[TCS-1056](../../data/cards/TCS-1056.json) · reused · status: `source_open` · evidence: `reviewed`.

Modular Boolean circuit lower bounds extend his circuit-lower-bound program.

**Status scope:** The target is explicitly open in Jukna’s source. A 13 September 2026 small-text check of later modular-circuit work identified a symmetry-restricted AND result, not a solution for majority in unrestricted ACC⁰. No resolution was verified; status remains source_open.

Sources: [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html); [Optimal Lower Bounds for Symmetric Modular Circuits](https://arxiv.org/abs/2604.04760).

## 91. Shuichi Hirahara

[Research bibliography](https://dblp.org/pid/150/4919.html).

### 1. Complexity of Minimum Circuit Size

[TCS-4786](../../data/cards/TCS-4786.json) · reused · status: `uncertain` · evidence: `source`.

MCSP is central to his meta-complexity research.

**Status scope:** Question recorded in a source from 2023; subsequent results and present open status have not been individually checked.

Sources: [Synergy Between Circuit Obfuscation and Circuit Minimization](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.31); [Simple Circuit Extensions for XOR in PTIME](https://doi.org/10.4230/LIPIcs.STACS.2026.23); [Sum-Of-Squares Lower Bounds for the Minimum Circuit Size Problem](https://doi.org/10.4230/LIPIcs.CCC.2023.31).

### 2. Average-case NP hardness from \(\mathrm{P} \ne  \mathrm{NP}\)

[TCS-0012](../../data/cards/TCS-0012.json) · reused · status: `source_open` · evidence: `reviewed`.

Worst-case to average-case hardness connects his recent complexity-to-cryptography results.

**Status scope:** The original question is explicitly open in Wigderson’s book and the revised average-case survey. Current primary literature was checked through 10 September 2026; no resolution from \(\mathrm{P}\ne \mathrm{NP}\) alone was located. The card fixes deterministic exact AvgP and strict polynomial-time sampling, rather than conflating them with randomized heuristic hardness.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3); [On Worst-Case to Average-Case Reductions for NP Problems](https://lucatrevisan.github.io/pubs/BT03.pdf); [One-Way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://doi.org/10.4230/LIPIcs.ITCS.2026.97).

## 92. Raghu Meka

[Research bibliography](https://dblp.org/pid/76/1906.html).

### 1. Sub-log-squared seeds for polynomial-size CNFs and DNFs

[TCS-1133](../../data/cards/TCS-1133.json) · reused · status: `uncertain` · evidence: `index`.

Short-seed CNF/DNF generators connect his pseudorandomness research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/).

### 2. Komlós conjecture

[TCS-7314](../../data/cards/TCS-7314.json) · reused · status: `source_open` · evidence: `reviewed`.

Komlos is central to his discrepancy and rounding work.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. The companion Beck–Fiala target is a documented consequence, not a duplicate. No algorithmic construction requirement is added.

Sources: [Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk](https://arxiv.org/abs/2508.03961).

## 93. Sam Hopkins

[Research bibliography](https://dblp.org/pid/130/9053-1.html).

### 1. Computational threshold for tensor PCA

[TCS-6657](../../data/cards/TCS-6657.json) · reused · status: `source_open` · evidence: `reviewed`.

Tensor PCA directly concerns his SOS and high-dimensional inference program.

**Status scope:** The May 2026 low-degree paper retains the conjectured gap for unrestricted algorithms and distinguishes spherical from independent-coordinate priors. The 2024 power-iteration and October 2025 stochastic-gradient improvements concern particular methods and do not provide a fixed-power improvement below \(n^{k/4}\). No full resolution found through 11 September 2026. The card explicitly fixes a finite-precision bit model; restricted lower bounds in the standard unrounded model are evidence, not a proof for all algorithms here.

Sources: [A statistical model for tensor PCA](https://arxiv.org/abs/1411.1076); [Sharp analysis of power iteration for tensor PCA](https://www.jmlr.org/papers/v25/24-0006.html); [Tensor cumulants for statistical inference on invariant distributions](https://arxiv.org/abs/2404.18735); [Near-Optimal Tensor PCA via Normalized Stochastic Gradient Ascent with Overparameterization](https://arxiv.org/abs/2510.14329); [Low-degree estimation thresholds in planted hypergraphs and tensor PCA](https://arxiv.org/abs/2605.30113).

### 2. Polynomial-time robust spectral estimation

[TCS-5087](../../data/cards/TCS-5087.json) · reused · status: `source_open` · evidence: `source`.

Robust spectral estimation connects his algorithmic robust-statistics research.

**Status scope:** Question recorded in a source from 2021; subsequent results and present open status have not been individually checked.

Sources: [Adversarially Robust Low Dimensional Representations](https://proceedings.mlr.press/v134/awasthi21a.html).

## 94. Urmila Mahadev

[Research bibliography](https://dblp.org/pid/140/7339.html).

### 1. Information-theoretic classical verification of quantum computation

[TCS-6580](../../data/cards/TCS-6580.json) · reused · status: `source_open` · evidence: `reviewed`.

Assumption-free classical verification is a main frontier after her computational verification breakthrough.

**Status scope:** Checked through 10 September 2026. The April 2026 primary paper explicitly leaves this single-prover, information-theoretic question open. The May 2026 trusted-gate result changes verifier resources, and the February 2026 witness-preserving protocol retains LWE. Neither meets this card’s classical-verifier and unbounded-cheater requirements.

Sources: [Verification of quantum computation: An overview of existing approaches](https://arxiv.org/abs/1709.06984); [\(\mathrm{IP} = \mathrm{PSPACE}\)](https://doi.org/10.1145/146585.146609); [Interactive Proofs for Quantum Computations](https://arxiv.org/abs/1704.04487); [A classical leash for a quantum system: Command of quantum systems via rigidity of CHSH games](https://arxiv.org/abs/1209.0448); [Classical Verification of Quantum Computations](https://arxiv.org/abs/1804.01082); [How to Classically Verify a Quantum Cat without Killing It](https://arxiv.org/abs/2602.09282); [Verification of Quantum Computations Without Trusted Preparations or Measurements](https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202501018); [A Relativizing MIP for BQP](https://arxiv.org/abs/2604.11952).

### 2. Remote state preparation from quantum-secure one-way functions

[TCS-2408](../../data/cards/TCS-2408.json) · reused · status: `uncertain` · evidence: `index`.

Remote state preparation from minimal assumptions connects her quantum-cryptography work.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Quantum Cryptography with Classical Communication: Parallel Remote State Preparation for Copy-Protection, Verification, and More](https://doi.org/10.4230/LIPIcs.ICALP.2023.67).

## 95. Anand Natarajan

[Research bibliography](https://dblp.org/pid/27/4274-1.html).

### 1. Quantum PCP conjecture

[TCS-6446](../../data/cards/TCS-6446.json) · reused · status: `source_open` · evidence: `reviewed`.

Quantum PCP connects his Hamiltonian complexity and nonlocal-proof work.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495); [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/).

### 2. QMA versus QCMA

[TCS-6448](../../data/cards/TCS-6448.json) · reused · status: `source_open` · evidence: `reviewed`.

Classical versus quantum witnesses concern the power of quantum proof systems he studies.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [Separating Quantum and Classical Advice with Good Codes](https://eccc.weizmann.ac.il/report/2026/020/).

## 96. Henry Yuen

[Research bibliography](https://dblp.org/pid/17/8909.html).

### 1. Quantum PCP conjecture

[TCS-6446](../../data/cards/TCS-6446.json) · reused · status: `source_open` · evidence: `reviewed`.

Quantum PCP is a central problem related to his quantum-complexity program.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495); [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/).

### 2. QMA versus \(\mathrm{QMA}(2)\)

[TCS-2229](../../data/cards/TCS-2229.json) · reused · status: `uncertain` · evidence: `index`.

The power of two unentangled proofs concerns his quantum proof-system research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Quantum Merlin-Arthur and Proofs Without Relative Phase](https://doi.org/10.4230/LIPIcs.ITCS.2024.9).

## 97. Jason Li

[Research bibliography](https://dblp.org/pid/12/975-6.html).

### 1. Almost-linear exact directed global minimum cut

[TCS-7344](../../data/cards/TCS-7344.json) · reused · status: `source_open` · evidence: `reviewed`.

Fast exact directed min cut continues his min-cut algorithm work.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. Editorial exact almost-linear endpoint. The statement fixes positive polynomial integer weights, bounded error and global outgoing-cut semantics; approximation results do not settle it.

Sources: [Approximating Directed Connectivity in Almost-Linear Time](https://arxiv.org/abs/2512.00176); [Almost-Optimal Approximation Algorithms for Global Minimum Cut in Directed Graphs](https://arxiv.org/abs/2512.09080); [Krajinou grafových algoritmů](https://mj.ucw.cz/vyuka/ga/ga.pdf).

### 2. Strongly polynomial near-linear negative-weight shortest paths

[TCS-7341](../../data/cards/TCS-7341.json) · reused · status: `source_open` · evidence: `reviewed`.

Strongly polynomial fast SSSP directly extends his shortest-path research.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. The approved real-weight formulation of the strong-polynomial endpoint fixes bounded error and worst-case operation cost. It is not the solved near-linear integer-weight question.

Sources: [Negative-Weight Single-Source Shortest Paths in Near-Linear Time: Now Faster!](https://arxiv.org/abs/2304.05279); [Negative-Weight Single-Source Shortest Paths in Near-linear Time](https://arxiv.org/abs/2203.03456); [Deterministic Negative-Weight Shortest Paths in Nearly Linear Time via Path Covers](https://arxiv.org/abs/2511.08551); [Bellman-Ford in Almost-Linear Time for Dense Graphs](https://arxiv.org/abs/2602.16153); [Krajinou grafových algoritmů](https://mj.ucw.cz/vyuka/ga/ga.pdf).

## 98. Yang P. Liu

[Research bibliography](https://dblp.org/pid/217/1820.html).

### 1. Exact directed maximum flow in \(O((m+n) \operatorname{polylog} n)\) time

[TCS-7228](../../data/cards/TCS-7228.json) · reused · status: `source_open` · evidence: `reviewed`.

Near-linear exact directed max flow extends his almost-linear optimization algorithms.

**Status scope:** Primary-source check through 11 September 2026 found almost-linear bounds, not the fixed-polylogarithmic overhead required here. New preprint proofs were not independently verified.

Sources: [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://arxiv.org/abs/2203.00671); [Maximum Flow Without the Outer IPM](https://arxiv.org/abs/2608.17384).

### 2. Almost-linear-work parallel exact maximum flow

[TCS-7349](../../data/cards/TCS-7349.json) · reused · status: `source_open` · evidence: `reviewed`.

Work-efficient parallel flow concerns parallelizing the graph-optimization breakthroughs he coauthored.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. The sourced work/depth endpoint is fixed to a uniform priority CRCW word PRAM, bounded error and worst-case resources. Subpolynomial depth is retained; polylogarithmic depth is not added as a stronger requirement.

Sources: [DAG Projections: Reducing Distance and Flow Problems to DAGs](https://arxiv.org/abs/2604.04752).

## 99. Mark Zhandry

[Research bibliography](https://dblp.org/pid/39/10308.html).

### 1. Public-key quantum money from LWE alone

[TCS-7359](../../data/cards/TCS-7359.json) · added · status: `source_open` · evidence: `reviewed`.

LWE-only public quantum money extends his quantum-money and lightning work.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [Anonymous Public-Key Quantum Money and Quantum Voting](https://arxiv.org/abs/2411.04482); [On Quantum Money and Evasive Obfuscation](https://eprint.iacr.org/2025/325); [A General Quantum Duality for Representations of Groups with Applications to Quantum Money, Lightning, and Fire](https://mzhandry.github.io/pubs.quantum.html).

### 2. One-way state generators versus EFI pairs

[TCS-1961](../../data/cards/TCS-1961.json) · reused · status: `uncertain` · evidence: `index`.

Minimal quantum cryptographic assumptions connect his quantum-cryptography program.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [One-Wayness in Quantum Cryptography](https://doi.org/10.4230/LIPIcs.TQC.2024.4).

## 100. Jan Vondrák

[Research bibliography](https://dblp.org/pid/29/5942.html).

### 1. Optimal approximation for submodular maximization over a matroid

[TCS-5407](../../data/cards/TCS-5407.json) · reused · status: `uncertain` · evidence: `source`.

Optimal matroid-constrained submodular maximization directly concerns his approximation research.

**Status scope:** Question recorded in a source from 2022; subsequent results and present open status have not been individually checked.

Sources: [On Maximizing Sums of Non-Monotone Submodular and Linear Functions](https://doi.org/10.4230/LIPIcs.ISAAC.2022.41).

### 2. Matroid secretary conjecture

[TCS-7316](../../data/cards/TCS-7316.json) · reused · status: `source_open` · evidence: `reviewed`.

Matroid secretary connects his work on matroids and stochastic optimization.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. No polynomial-time restriction has been silently appended. Earlier exclusions TCS-2570 and TCS-5552 address narrower algorithm/model questions.

Sources: [Constant-Competitiveness for Random Assignment Matroid Secretary Without Knowing the Matroid](https://arxiv.org/abs/2305.05353).

## 101. Saket Saurabh

[Research bibliography](https://dblp.org/pid/11/5491.html).

### 1. Polynomial kernels for Directed Feedback Vertex Set

[TCS-6379](../../data/cards/TCS-6379.json) · reused · status: `open` · evidence: `reviewed`.

Polynomial DFVS kernels connect his kernelization and directed-graph research.

**Status scope:** Checked the full 2016 source and WADS 2019 author manuscript, plus the 2025 journal abstract, institutional publication record and author publication listing. The publisher blocked access to its full journal text, so detailed theorem scope is attributed to the checked conference manuscript. Searches through 12 September 2026 found no resolution of the unrestricted solution-budget kernel. No independent proof verification.

Sources: [Polynomial Kernels for Deletion to Classes of Acyclic Digraphs](https://doi.org/10.4230/LIPIcs.STACS.2016.55); [Wannabe Bounded Treewidth Graphs Admit a Polynomial Kernel for Directed Feedback Vertex Set](https://doi.org/10.1145/3711669).

### 2. Polynomial kernels for Planar Deletion

[TCS-7022](../../data/cards/TCS-7022.json) · reused · status: `source_open` · evidence: `source`.

Planar-deletion kernels concern his parameterized structural graph work.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2020 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867).

## 102. Fedor Fomin

[Research bibliography](https://dblp.org/pid/f/FedorVFomin.html).

### 1. Polynomial kernels for H-minor-free Deletion

[TCS-7023](../../data/cards/TCS-7023.json) · reused · status: `source_open` · evidence: `source`.

Minor-free-deletion kernels extend his parameterized graph algorithms.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2020 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867).

### 2. Chromatic number in \(2^{n}\) time and polynomial space

[TCS-6728](../../data/cards/TCS-6728.json) · reused · status: `source_open` · evidence: `source`.

Polynomial-space chromatic-number algorithms concern his exact-exponential algorithm research.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2016 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Parameterized Algorithms](https://parameterized-algorithms.mimuw.edu.pl/).

## 103. Michal Pilipczuk

[Research bibliography](https://dblp.org/pid/61/8036.html).

### 1. Fixed-parameter tractability of graph isomorphism by rank-width

[TCS-7312](../../data/cards/TCS-7312.json) · reused · status: `source_open` · evidence: `reviewed`.

Rank-width parameterized isomorphism connects his structural graph and logic work.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Parameterized complexity of graph isomorphism testing](https://epub.uni-regensburg.de/78630/1/1-s2.0-S1574013726000274-main.pdf).

### 2. FPT approximation of twin-width

[TCS-7241](../../data/cards/TCS-7241.json) · reused · status: `source_open` · evidence: `reviewed`.

FPT twin-width approximation concerns the graph decompositions he studies.

**Status scope:** Reviewed through 11 September 2026. Bonnet lists the FPT approximation question, and the 2025 recognition paper explicitly leaves even general XP approximation open. No general resolution was found in the same-day review.

Sources: [Open problems in twin-width](https://perso.ens-lyon.fr/edouard.bonnet/openQuestions.html); [Twin-width one](https://arxiv.org/abs/2501.00991).

## 104. Marcin Pilipczuk

[Research bibliography](https://dblp.org/pid/09/4636.html).

### 1. Single-exponential FPT for directed feedback sets

[TCS-7035](../../data/cards/TCS-7035.json) · reused · status: `source_open` · evidence: `source`.

Single-exponential directed feedback algorithms connect his parameterized algorithms.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2020 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867).

### 2. Parameterized complexity of three-pair Directed Edge Multicut

[TCS-7036](../../data/cards/TCS-7036.json) · reused · status: `source_open` · evidence: `source`.

Directed edge multicut with three pairs concerns his directed cut-complexity work.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2020 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867).

## 105. Robert Krauthgamer

[Research bibliography](https://dblp.org/pid/k/RobertKrauthgamer.html).

### 1. Gupta–Newman–Rabinovich–Sinclair conjecture

[TCS-6525](../../data/cards/TCS-6525.json) · reused · status: `source_open` · evidence: `reviewed`.

GNRS is central to his metric-embedding and graph-approximation work.

**Status scope:** The planar constant-distortion case remains explicitly open in the checked May 2026 notes. Restricted-family and face-cover results, including February 2026 exact values for \(K_{2},_{n}\), do not settle arbitrary fixed-minor-free metrics. The inherited fixed-treewidth approximation theorem uses a stronger relaxation and expressly does not prove a flow–cut-gap bound. No general settlement found through 11 September 2026.

Sources: [Cuts, Trees and \(\ell\)\(_{1}\)-Embeddings of Graphs](https://people.eecs.berkeley.edu/~sinclair/cuts.pdf); [Pathwidth, trees, and random embeddings](https://arxiv.org/abs/0910.1409); [Approximating Sparsest Cut in Graphs of Bounded Treewidth](https://www.wisdom.weizmann.ac.il/~robi/papers/CKR-TreewidthSparsestCut-APPROX10.pdf); [A face cover perspective to \(\ell\)\(_{1}\) embeddings of planar graphs](https://arxiv.org/abs/1903.02758); [The exact value of \(c_{1}(K_{2},_{n})\)](https://arxiv.org/abs/2602.23745); [CS 583: Approximation Algorithms](https://courses.grainger.illinois.edu/CS583/sp2026/approx-algorithms-lecture-notes.pdf).

### 2. Optimal \(\ell\)\(_{1}\) distortion of edit distance

[TCS-7297](../../data/cards/TCS-7297.json) · reused · status: `source_open` · evidence: `reviewed`.

L1 embedding of edit distance connects his sketching and metric-complexity research.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Low Distortion Embeddings for Edit Distance](https://doi.org/10.1145/1060590.1060623).

## 106. Sanjeev Khanna

[Research bibliography](https://dblp.org/pid/k/SanjeevKhanna.html).

### 1. Constant-factor approximation for Densest k-Subgraph

[TCS-6587](../../data/cards/TCS-6587.json) · reused · status: `source_open` · evidence: `reviewed`.

Densest k-subgraph concerns his approximation-algorithm research.

**Status scope:** Checked through 10 September 2026. The constant-factor algorithm is already ruled out assuming ETH, which remains unproved. The May 2026 primary source explicitly notes the absence of NP-hardness of approximation even at factor 1.001. This card asks about a deterministic constant-factor algorithm on all unweighted graphs, and preserves the distinction between conditional evidence and an unconditional resolution.

Sources: [Detecting High Log-Densities — an \(O(n^{1}/4)\) Approximation for Densest k-Subgraph](https://arxiv.org/abs/1001.2891); [Polynomial integrality gaps for strong SDP relaxations of Densest k-subgraph](https://arxiv.org/abs/1110.1360); [Almost-Polynomial Ratio ETH-Hardness of Approximating Densest k-Subgraph](https://arxiv.org/abs/1611.05991); [A New Conjecture on Hardness of 2-CSP’s with Implications to Hardness of Densest k-Subgraph and Other Problems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2023.38); [A Scalable and Exact Relaxation for Densest k-Subgraph via Error Bounds](https://ojs.aaai.org/index.php/AAAI/article/view/38562); [A Note on Approximability of Densest At-Least-k-Subgraph](https://arxiv.org/abs/2605.25464).

### 2. Directed reachability with nearly linear memory and polylogarithmic passes

[TCS-6556](../../data/cards/TCS-6556.json) · reused · status: `source_open` · evidence: `reviewed`.

Space-efficient directed reachability connects his graph-streaming work.

**Status scope:** The primary survey, cited multipass bounds and the revision of 9 September 2026 were checked on 11 September 2026. The recent paper explicitly retains the \(n^{1/2+o(1)}\)-pass upper benchmark. No polylogarithmic-pass algorithm or lower bound ruling out every polylogarithmic pass bound in the stated memory model was found. This check covers decision with adversarial fixed order, rather than a changed stream or a path-output requirement.

Sources: [Recent Advances in Multi-Pass Graph Streaming Lower Bounds](https://par.nsf.gov/servlets/purl/10488812); [Superlinear lower bounds for multipass graph processing](https://eccc.weizmann.ac.il/report/2013/002/revision/3/download/); [Parallel Reachability in Almost Linear Work and Square Root Depth](https://arxiv.org/abs/1905.08841); [Semi-Streaming Bipartite Matching in Fewer Passes and Optimal Space](https://arxiv.org/abs/2011.03495); [Almost Optimal Super-Constant-Pass Streaming Lower Bounds for Reachability](https://par.nsf.gov/servlets/purl/10315017); [Streaming Algorithms for Monotonicity Testing](https://arxiv.org/abs/2608.07073v2).

## 107. Mika Göös

[Research bibliography](https://dblp.org/pid/25/7589.html).

### 1. Log-rank conjecture

[TCS-6603](../../data/cards/TCS-6603.json) · reused · status: `source_open` · evidence: `reviewed`.

Log-rank is a central communication-complexity barrier related to his lifting research.

**Status scope:** Explicitly open in the August 2026 CCC version of Hambardzumyan–Lovett–Shirley. Checked through 10 September 2026. The established general upper bound is \(O(\sqrt{r})\); recent fixed-polynomial lower-bound refinements and signed-decomposition equivalences do not settle the conjecture.

Sources: [The Log-Rank Conjecture: New Equivalent Formulations](https://arxiv.org/abs/2510.02583v3); [Matrix discrepancy and the log-rank conjecture](https://doi.org/10.1007/s10107-024-02117-9); [Deterministic Communication vs. Partition Number](https://doi.org/10.1137/16M1059369); [Alphabet-Preserving Lifting for the Log-Rank Conjecture](https://arxiv.org/abs/2608.01812v1).

### 2. Number-on-forehead Disjointness complexity

[TCS-6710](../../data/cards/TCS-6710.json) · reused · status: `source_open` · evidence: `source`.

Multiparty disjointness concerns his communication lower-bound program.

**Status scope:** Recorded as a question, conjecture or research direction in the cited None source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf); [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html).

## 108. Rahul Santhanam

[Research bibliography](https://dblp.org/pid/84/1179.html).

### 1. NEXP versus nonuniform \(\mathrm{TC}^{0}\)

[TCS-7161](../../data/cards/TCS-7161.json) · reused · status: `open` · evidence: `reviewed`.

NEXP versus TC0 continues his circuit-lower-bound work.

**Status scope:** No \(\mathrm{NEXP}\not\subset \mathrm{TC}^{0}\) resolution found through 11 September 2026. The checked March, July and September results retain different hard-language models or fixed depth and polynomial quantitative bounds. The September preprint has a source comment raising concerns and is recorded as an unverified claim.

Sources: [Non-Uniform ACC Circuit Lower Bounds](https://doi.org/10.1109/CCC.2011.36); [Wikipedia: Circuit complexity](https://en.wikipedia.org/wiki/Circuit_complexity); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1328197464); [Non-Uniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-ccc.pdf); [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/); [Almost-Everywhere Near-Cubic Wire Lower Bounds for SYM ∘ THR and \(\mathrm{THR} \circ  \mathrm{THR}\)](https://eccc.weizmann.ac.il/report/2026/167/); [Near-Maximum Circuit Lower Bounds for Exponential Time with Merlin-Arthur Queries](https://eccc.weizmann.ac.il/report/2026/118/).

### 2. Complexity of Minimum Circuit Size

[TCS-4786](../../data/cards/TCS-4786.json) · reused · status: `uncertain` · evidence: `source`.

MCSP concerns his meta-complexity and hardness-magnification research.

**Status scope:** Question recorded in a source from 2023; subsequent results and present open status have not been individually checked.

Sources: [Synergy Between Circuit Obfuscation and Circuit Minimization](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.31); [Simple Circuit Extensions for XOR in PTIME](https://doi.org/10.4230/LIPIcs.STACS.2026.23); [Sum-Of-Squares Lower Bounds for the Minimum Circuit Size Problem](https://doi.org/10.4230/LIPIcs.CCC.2023.31).

## 109. Shubhangi Saraf

[Research bibliography](https://dblp.org/pid/75/7249.html).

### 1. Superpolynomial arithmetic formula lower bounds

[TCS-6888](../../data/cards/TCS-6888.json) · reused · status: `source_open` · evidence: `source`.

General arithmetic formula lower bounds extend her algebraic-complexity work.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2010 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf).

### 2. Full-length Reed–Solomon list decoding beyond Johnson

[TCS-1011](../../data/cards/TCS-1011.json) · reused · status: `uncertain` · evidence: `index`.

Reed-Solomon decoding concerns her algorithmic coding research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 110. Amir Shpilka

[Research bibliography](https://dblp.org/pid/11/3816.html).

### 1. VP versus VNP

[TCS-0005](../../data/cards/TCS-0005.json) · reused · status: `source_open` · evidence: `reviewed`.

VP versus VNP is a foundational target of his arithmetic-circuit work.

**Status scope:** The August 2026 primary paper still identifies the unrestricted VP-versus-VNP separation as open and explicitly limits its new constructions. No general resolution was located in the status search through 10 September 2026.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [Completeness Classes in Algebra](https://doi.org/10.1145/800135.804419); [Superpolynomial Lower Bounds Against Low-Depth Algebraic Circuits](https://eccc.weizmann.ac.il/report/2021/081/); [Arithmetic circuit lower bounds from sumset expansion](https://eccc.weizmann.ac.il/report/2026/138/).

### 2. Derandomizing polynomial identity testing

[TCS-7113](../../data/cards/TCS-7113.json) · reused · status: `source_open` · evidence: `source`.

PIT derandomization is directly in his algebraic-algorithm program.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2021 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042).

## 111. Swastik Kopparty

[Research bibliography](https://dblp.org/pid/80/4866.html).

### 1. Polynomial-length constant-query locally decodable codes

[TCS-1020](../../data/cards/TCS-1020.json) · reused · status: `uncertain` · evidence: `index`.

Constant-query local decoding continues his algebraic coding work.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

### 2. Deterministic polynomial-time factorization over finite fields

[TCS-6614](../../data/cards/TCS-6614.json) · reused · status: `source_open` · evidence: `reviewed`.

Deterministic finite-field factorization connects his algebraic algorithms and pseudorandomness research.

**Status scope:** Open unconditionally for all explicitly represented finite fields and dense univariate inputs, based on sources checked through 11 September 2026. GRH alone is not known to give the requested general polynomial bound. Amortization over primes, fixed characteristic, special Galois groups and multivariate bounds retaining a univariate oracle do not resolve this exact question.

Sources: [Deterministic polynomial factorisation modulo many primes](https://arxiv.org/abs/2509.12705); [Factoring Polynomials Over Finite Fields: A Survey](https://people.csail.mit.edu/dmoshkov/courses/codes/poly-factorization.pdf); [Deterministic polynomial factoring over finite fields: a uniform approach via P-schemes](https://zeyuguo.bitbucket.io/papers/pscheme.pdf); [A number-theoretic conjecture implying faster algorithms for polynomial factorization and integer factorization](https://arxiv.org/abs/2511.10851); [On Factorization of Sparse Polynomials of Bounded Individual Degree](https://eccc.weizmann.ac.il/report/2026/036/).

## 112. Pavel Panteleev

[Research bibliography](https://dblp.org/pid/156/0010.html).

### 1. Asymptotically good quantum locally testable stabilizer codes

[TCS-6515](../../data/cards/TCS-6515.json) · reused · status: `source_open` · evidence: `reviewed`.

Good quantum locally testable codes are a main frontier after his good quantum LDPC breakthrough.

**Status scope:** Checked through 11 September 2026. No bounded-degree stabilizer family with constant rate, relative distance and normalized soundness was located. The corrected 2025 and July 2026 constructions retain inverse-polylogarithmic losses, while constant-soundness variants increase locality or sacrifice other parameters.

Sources: [Quantum Locally Testable Code with Constant Soundness](https://quantum-journal.org/papers/q-2024-10-18-1501/); [Asymptotically Good Quantum and Locally Testable Classical LDPC Codes](https://arxiv.org/abs/2111.03654); [Local testability of distance-balanced quantum codes](https://www.nature.com/articles/s41534-024-00908-8); [Expansion of higher-dimensional cubical complexes with application to quantum locally testable codes](https://arxiv.org/abs/2402.07476); [NLTS Hamiltonians from Good Quantum Codes](https://arxiv.org/abs/2206.13228); [Transversal non-Clifford gates on almost-good quantum LDPC and quantum locally testable codes](https://arxiv.org/abs/2604.01874); [Probabilistically Checking Quantum Proofs, with Interaction](https://arxiv.org/abs/2606.09588).

### 2. Quantum PCP conjecture

[TCS-6446](../../data/cards/TCS-6446.json) · reused · status: `source_open` · evidence: `reviewed`.

Quantum PCP is the central quantum-verification question linked to these local-code constructions.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495); [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/).

## 113. Gleb Kalachev

[Research bibliography](https://dblp.org/pid/239/5980.html).

### 1. Asymptotically good quantum locally testable stabilizer codes

[TCS-6515](../../data/cards/TCS-6515.json) · reused · status: `source_open` · evidence: `reviewed`.

Good quantum local testability extends his quantum LDPC construction work.

**Status scope:** Checked through 11 September 2026. No bounded-degree stabilizer family with constant rate, relative distance and normalized soundness was located. The corrected 2025 and July 2026 constructions retain inverse-polylogarithmic losses, while constant-soundness variants increase locality or sacrifice other parameters.

Sources: [Quantum Locally Testable Code with Constant Soundness](https://quantum-journal.org/papers/q-2024-10-18-1501/); [Asymptotically Good Quantum and Locally Testable Classical LDPC Codes](https://arxiv.org/abs/2111.03654); [Local testability of distance-balanced quantum codes](https://www.nature.com/articles/s41534-024-00908-8); [Expansion of higher-dimensional cubical complexes with application to quantum locally testable codes](https://arxiv.org/abs/2402.07476); [NLTS Hamiltonians from Good Quantum Codes](https://arxiv.org/abs/2206.13228); [Transversal non-Clifford gates on almost-good quantum LDPC and quantum locally testable codes](https://arxiv.org/abs/2604.01874); [Probabilistically Checking Quantum Proofs, with Interaction](https://arxiv.org/abs/2606.09588).

### 2. Quantum PCP conjecture

[TCS-6446](../../data/cards/TCS-6446.json) · reused · status: `source_open` · evidence: `reviewed`.

Quantum PCP connects the local constraints and expansion in his quantum codes to Hamiltonian complexity.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495); [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/).

## 114. Li-Yang Tan

[Research bibliography](https://dblp.org/pid/87/5034.html).

### 1. Optimal explicit pseudorandom generators for read-once branching programs

[TCS-6600](../../data/cards/TCS-6600.json) · reused · status: `source_open` · evidence: `reviewed`.

Optimal branching-program generators are central to his derandomization research.

**Status scope:** Checked through 10 September 2026. ECCC TR26-064 revision 3 explicitly retains the optimal general PRG target and the log-squared barrier. Its new generator is weighted; the July TR26-123 result is restricted to permutation programs. This card requires one ordinary, program-independent distribution family and optimal seed length as well as optimal work space.

Sources: [Pseudorandom generators for space-bounded computation](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf); [Better Pseudodistributions and Derandomization for Space-Bounded Computation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2021.28); [Hitting Sets Give Two-Sided Derandomization of Small Space](https://theoryofcomputing.org/articles/v018a021/); [Weighted Pseudorandom Generators for Read-Once Branching Programs via Weighted Pseudorandom Reductions](https://epubs.siam.org/doi/10.1137/1.9781611978971.124); [Improved Error Reduction for Weighted PRGs](https://eccc.weizmann.ac.il/report/2026/064/); [A Forward-Backward Weight Analysis of INW for Permutation Branching Programs](https://eccc.weizmann.ac.il/report/2026/123/).

### 2. Learning decision trees from uniform random examples in polynomial time

[TCS-7294](../../data/cards/TCS-7294.json) · reused · status: `source_open` · evidence: `reviewed`.

Uniform decision-tree learning connects his learning and Boolean-analysis work.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Decision trees are PAC-learnable from most product distributions: a smoothed analysis](https://arxiv.org/abs/0812.0933); [Backdoor Defense, Learnability and Obfuscation](https://doi.org/10.4230/LIPIcs.ITCS.2025.38).

## 115. Srikanth Srinivasan

[Research bibliography](https://dblp.org/pid/05/6302.html).

### 1. Superpolynomial arithmetic formula lower bounds

[TCS-6888](../../data/cards/TCS-6888.json) · reused · status: `source_open` · evidence: `source`.

General arithmetic formula lower bounds extend his restricted-model breakthroughs.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2010 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf).

### 2. Majority outside constant-depth modular circuits

[TCS-1056](../../data/cards/TCS-1056.json) · reused · status: `source_open` · evidence: `reviewed`.

Modular Boolean-circuit lower bounds concern his circuit-complexity program.

**Status scope:** The target is explicitly open in Jukna’s source. A 13 September 2026 small-text check of later modular-circuit work identified a symmetry-restricted AND result, not a solution for majority in unrestricted ACC⁰. No resolution was verified; status remains source_open.

Sources: [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html); [Optimal Lower Bounds for Symmetric Modular Circuits](https://arxiv.org/abs/2604.04760).

## 116. Euiwoong Lee

[Research bibliography](https://dblp.org/pid/129/5624.html).

### 1. Optimal polynomial-time approximation ratio for metric k-means

[TCS-7354](../../data/cards/TCS-7354.json) · added · status: `source_open` · evidence: `reviewed`.

Optimal metric k-means approximation directly extends his 2026 clustering work.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654).

### 2. Constant-colour polynomial-time colouring of 3-colourable graphs

[TCS-6637](../../data/cards/TCS-6637.json) · reused · status: `source_open` · evidence: `reviewed`.

Constant-color approximation of 3-colorable graphs concerns his hardness research.

**Status scope:** No constant-colour algorithm or unrestricted all-constant hardness resolution found through 11 September 2026. The February 2026 primary paper retains the gap between five-colour NP-hardness and a growing \(O(n^{0.19539})\) algorithmic bound. The March logic result is restricted to fixed-point logic with counting. This card explicitly allows bounded-error randomized algorithms.

Sources: [Better coloring of 3-colorable graphs](https://arxiv.org/abs/2406.00357); [Algebraic Approach to Promise Constraint Satisfaction](https://arxiv.org/abs/1811.00970); [d-To-1 Hardness of Coloring 3-Colorable Graphs with \(O(1)\) Colors](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.62); [Improved SDP-Based Algorithm for Coloring 3-Colorable Graphs](https://arxiv.org/abs/2602.05904); [Undefinability of Approximation of 2-to-2 Games](https://arxiv.org/abs/2504.03523).

## 117. Ce Jin

[Research bibliography](https://dblp.org/pid/224/0281.html).

### 1. Near-linear output-sensitive Subset Sum

[TCS-7350](../../data/cards/TCS-7350.json) · reused · status: `source_open` · evidence: `reviewed`.

Output-sensitive Subset Sum directly continues his subset-sum algorithm work.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. The explicit input-reading term, multiplicities, truncation and word length are fixed. Algorithms is the editorial home because the target is a basic pseudopolynomial computation measured by its support size, closely tied to convolution; it is not counting the number of solutions.

Sources: [Top-k-Convolution and the Quest for Near-Linear Output-Sensitive Subset Sum](https://arxiv.org/abs/2107.13206); [Derandomizing Pseudopolynomial Algorithms for Subset Sum](https://arxiv.org/abs/2601.01390).

### 2. Min-Plus Convolution Hypothesis

[TCS-6598](../../data/cards/TCS-6598.json) · reused · status: `source_open` · evidence: `reviewed`.

Min-plus convolution is a central fine-grained primitive in his research.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. Completes the existing TCS-6598 integer-word target, including output indexing, magnitude quantifiers, bounded error and worst-case cost. The established hypothesis title is retained; the yes/no statement asks whether its algorithmic negation holds.

Sources: [Deterministic Monotone Min-Plus Product and Convolution](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.119); [Necklaces, Convolutions, and \(X+Y\)](https://tmc.web.engr.illinois.edu/convol.pdf).

## 118. Josh Alman

[Research bibliography](https://dblp.org/pid/166/1624.html).

### 1. Matrix multiplication exponent

[TCS-0007](../../data/cards/TCS-0007.json) · reused · status: `source_open` · evidence: `reviewed`.

Matrix multiplication is a direct research focus.

**Status scope:** The latest primary upper bound located through 10 September 2026 is the reported omega<2.371177 from August 2026. It leaves the omega=2 question open. The model is exact arithmetic over C; the catalogue has not independently reproduced the numerical certificate. The 12 September 2026 edit adopts absolute 0.01 benchmark acceptance; the saved open-status evidence concerns the underlying exact question and does not independently certify openness at that tolerance.

Sources: [Gaussian elimination is not optimal](https://doi.org/10.1007/BF02165411); [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [Limits on the Universal Method for Matrix Multiplication](https://arxiv.org/abs/1812.08731); [More Asymmetry Yields Faster Matrix Multiplication](https://doi.org/10.1137/1.9781611978322.63); [Improving the matrix multiplication exponent with modern optimization and AlphaEvolve](https://arxiv.org/abs/2608.16884v1); [More Asymmetry Yields Faster Matrix Multiplication — August 2026 revision](https://arxiv.org/abs/2404.16349v3).

### 2. Explicit three-dimensional tensors of superlinear rank

[TCS-6895](../../data/cards/TCS-6895.json) · reused · status: `source_open` · evidence: `source`.

Explicit tensor rank lower bounds connect the algebraic structures in his algorithmic work.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2010 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf).

## 119. William Kuszmaul

[Research bibliography](https://dblp.org/pid/140/1108.html).

### 1. Constant-time deterministic dynamic dictionaries

[TCS-7331](../../data/cards/TCS-7331.json) · reused · status: `source_open` · evidence: `reviewed`.

Constant-time deterministic dynamic dictionaries concern his hashing and dictionary work.

**Status scope:** Open in the cited dated sources. The bounded source and subsequent-result review on 13 September 2026 found no verified resolution of this target; this is not exhaustive certification of current openness.

Sources: [Research Statement](https://people.csail.mit.edu/mip/docs/job-application07/statements.pdf).

### 2. Optimal randomized memory-reallocation overhead

[TCS-7340](../../data/cards/TCS-7340.json) · reused · status: `source_open` · evidence: `reviewed`.

Optimal memory reallocation directly connects his data-structure research.

**Status scope:** Open in the cited dated sources. The bounded source and subsequent-result review on 13 September 2026 found no verified resolution of this target; this is not exhaustive certification of current openness.

Sources: [A Nearly Quadratic Improvement for Memory Reallocation](https://arxiv.org/abs/2405.12152); [Memory Reallocation with Polylogarithmic Overhead](https://arxiv.org/abs/2602.15417v1).

## 120. Tomasz Kociumaka

[Research bibliography](https://dblp.org/pid/38/9892.html).

### 1. Linear-space LZ77 random access

[TCS-0467](../../data/cards/TCS-0467.json) · reused · status: `source_open` · evidence: `reviewed`.

LZ77-space random access connects his compressed string data structures.

**Status scope:** Reviewed 10 September 2026, including the July LZ-End result. The stated parse convention, space parameter, and deterministic query guarantee are explicit.

Sources: [Adaptive and Scalable Data Structures — Two problems on Lempel-Ziv compression](https://doi.org/10.4230/DagRep.15.5.1); [Balancing Straight-Line Programs](https://arxiv.org/abs/1902.03568); [Random Access to LZ-End: Faster and Deterministic](https://arxiv.org/abs/2607.14923).

### 2. Truly subquadratic exact edit distance

[TCS-7179](../../data/cards/TCS-7179.json) · reused · status: `open` · evidence: `reviewed`.

Exact edit-distance complexity concerns his fine-grained string algorithms.

**Status scope:** The checked primary literature gives conditional exact-distance lower bounds and a March 2026 approximation advance. Searches through 11 September 2026 found no established deterministic truly subquadratic exact algorithm or unconditional exclusion in this model.

Sources: [Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)](https://arxiv.org/abs/1412.0348); [Wikipedia: List of unsolved problems in computer science](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1345711618); [Quadratic Conditional Lower Bounds for String Problems and Dynamic Time Warping](https://arxiv.org/abs/1502.01063v2); [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702).

## 121. Gillat Kol

[Research bibliography](https://dblp.org/pid/39/4172.html).

### 1. Constant-factor randomized direct sums for total Boolean functions

[TCS-5892](../../data/cards/TCS-5892.json) · reused · status: `source_open` · evidence: `reviewed`.

Direct sums for total functions connect her communication and information-complexity research.

**Status scope:** A user-authorized precise total-Boolean-function variant. The August 2026 primary preprint explicitly distinguishes relations from the remaining total-function question. Rechecked on 13 September 2026; its new theorem is a reported preprint claim, not an independently verified result or a refutation of this target.

Sources: [Lifting Theorems for Equality](https://doi.org/10.4230/LIPIcs.STACS.2019.50); [Efficient Communication Using Partial Information](https://eccc.weizmann.ac.il/report/2010/083/); [Zero-error information equals amortized communication complexity](https://arxiv.org/abs/2608.04141).

### 2. Noise tolerance of binary interactive codes

[TCS-4802](../../data/cards/TCS-4802.json) · reused · status: `uncertain` · evidence: `source`.

Optimal binary interactive noise tolerance connects her interactive-coding research.

**Status scope:** Question recorded in a source from 2022; subsequent results and present open status have not been individually checked.

Sources: [Binary Codes with Resilience Beyond \(1/4\) via Interaction](https://doi.org/10.1109/FOCS54457.2022.00008).

## 122. Soheil Behnezhad

[Research bibliography](https://dblp.org/pid/192/1220.html).

### 1. One-cycle versus two-cycles conjecture

[TCS-6505](../../data/cards/TCS-6505.json) · reused · status: `open` · evidence: `reviewed`.

One-cycle versus two-cycles is a central low-memory MPC barrier in his parallel graph work.

**Status scope:** Reviewed 10 September 2026. The lower bound is conjectural. Constant-round results for geometric graphs or larger local memory do not establish this variant.

Sources: [\(O(1)\)-Round MPC Algorithms for Multi-Dimensional Grid Graph Connectivity, Euclidean MST and DBSCAN](https://doi.org/10.4230/LIPIcs.ICDT.2025.7); [Equivalence classes and conditional hardness in massively parallel computations](https://doi.org/10.1007/s00446-021-00418-2).

### 2. Sublogarithmic distributed MIS

[TCS-6499](../../data/cards/TCS-6499.json) · reused · status: `open` · evidence: `reviewed`.

Distributed MIS connects his sublinear and parallel graph algorithms.

**Status scope:** Reviewed 10 September 2026. General-graph sublogarithmic elapsed-round complexity remains open in the checked literature; awake-time and high-girth results have different guarantees.

Sources: [Breaking Barriers for Distributed MIS by Faster Degree Reduction](https://arxiv.org/abs/2505.15652); [An Improved Distributed Algorithm for Maximal Independent Set](https://arxiv.org/abs/1506.05093); [Round Elimination via Self-Reduction: Closing Gaps for Distributed Maximal Matching](https://arxiv.org/abs/2505.15654).

## 123. Maximilian Probst Gutenberg

[Research bibliography](https://dblp.org/pid/223/4496.html).

### 1. Subquadratic exact fully dynamic weighted single-source distances

[TCS-5209](../../data/cards/TCS-5209.json) · reused · status: `source_open` · evidence: `reviewed`.

Dynamic exact SSSP directly concerns his dynamic distance algorithms.

**Status scope:** The 2017 blanket rebuilding remark is obsolete for several variants. This user-authorized exact weighted variant was specified on 13 September 2026; the checked later sources separate it from approximate and unweighted results. Their conditional barriers are not an unconditional resolution, and no exact new theorem for the selected model was identified in the bounded search.

Sources: [Deterministic Partially Dynamic Single Source Shortest Paths in Weighted Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2017.44); [Deterministic Partially Dynamic Single Source Shortest Paths in Weighted Graphs — full version](https://arxiv.org/abs/1705.10097); [Dynamic Approximate Shortest Paths and Beyond: Subquadratic and Worst-Case Update Time](https://arxiv.org/abs/1909.10850); [Deterministic Fully Dynamic SSSP and More](https://doi.org/10.1109/FOCS57990.2023.00142).

### 2. Almost-linear exact directed global minimum cut

[TCS-7344](../../data/cards/TCS-7344.json) · reused · status: `source_open` · evidence: `reviewed`.

Fast directed min cut extends his flow and connectivity research.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. Editorial exact almost-linear endpoint. The statement fixes positive polynomial integer weights, bounded error and global outgoing-cut semantics; approximation results do not settle it.

Sources: [Approximating Directed Connectivity in Almost-Linear Time](https://arxiv.org/abs/2512.00176); [Almost-Optimal Approximation Algorithms for Global Minimum Cut in Directed Graphs](https://arxiv.org/abs/2512.09080); [Krajinou grafových algoritmů](https://mj.ucw.cz/vyuka/ga/ga.pdf).

## 124. Aaron Bernstein

[Research bibliography](https://dblp.org/pid/02/4059.html).

### 1. Subquadratic exact fully dynamic weighted single-source distances

[TCS-5209](../../data/cards/TCS-5209.json) · reused · status: `source_open` · evidence: `reviewed`.

Fully dynamic weighted exact SSSP is a central frontier in his dynamic shortest-path work.

**Status scope:** The 2017 blanket rebuilding remark is obsolete for several variants. This user-authorized exact weighted variant was specified on 13 September 2026; the checked later sources separate it from approximate and unweighted results. Their conditional barriers are not an unconditional resolution, and no exact new theorem for the selected model was identified in the bounded search.

Sources: [Deterministic Partially Dynamic Single Source Shortest Paths in Weighted Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2017.44); [Deterministic Partially Dynamic Single Source Shortest Paths in Weighted Graphs — full version](https://arxiv.org/abs/1705.10097); [Dynamic Approximate Shortest Paths and Beyond: Subquadratic and Worst-Case Update Time](https://arxiv.org/abs/1909.10850); [Deterministic Fully Dynamic SSSP and More](https://doi.org/10.1109/FOCS57990.2023.00142).

### 2. Deterministic subquadratic dynamic s–t reachability

[TCS-6477](../../data/cards/TCS-6477.json) · reused · status: `source_open` · evidence: `source`.

Deterministic dynamic reachability concerns his dynamic graph-algorithm program.

**Status scope:** Question recorded in a source from 2023; subsequent results and present open status have not been individually checked.

Sources: [Deterministic Fully Dynamic SSSP and More](https://doi.org/10.1109/FOCS57990.2023.00142).

## 125. Michael Kapralov

[Research bibliography](https://dblp.org/pid/76/6407.html).

### 1. Hypergraph cut sparsifiers with \(O(n/\varepsilon ^{2})\) hyperedges

[TCS-0946](../../data/cards/TCS-0946.json) · reused · status: `uncertain` · evidence: `reviewed`.

Optimal hypergraph sparsifiers extend his graph sketching and sparsification research.

**Status scope:** Checked through 11 September 2026. No \(Cn/\varepsilon ^{2}\) existence theorem or matching refutation was located. The old quadratic upper bound has been superseded by \(O(n \log  n/\varepsilon ^{2})\). The original source permits an arbitrary weighted hypergraph on the same vertices; this card preserves that scope. Later near-optimal storage statements do not remove the logarithmic edge-count gap.

Sources: [Problem 91: Cut-Sparsification of Hypergraphs](https://sublinear.info/index.php?title=Open_Problems:91); [Near-linear Size Hypergraph Cut Sparsifiers](https://arxiv.org/abs/2009.04992); [Twice-Ramanujan Sparsifiers](https://arxiv.org/abs/0808.0163); [Near-optimal Size Linear Sketches for Hypergraph Cut Sparsifiers](https://arxiv.org/abs/2407.03934); [Nearly Space-Optimal Graph and Hypergraph Sparsification in Insertion-Only Data Streams](https://arxiv.org/abs/2510.18180).

### 2. Directed reachability with nearly linear memory and polylogarithmic passes

[TCS-6556](../../data/cards/TCS-6556.json) · reused · status: `source_open` · evidence: `reviewed`.

Small-memory directed reachability concerns his graph-streaming and communication-lower-bound research.

**Status scope:** The primary survey, cited multipass bounds and the revision of 9 September 2026 were checked on 11 September 2026. The recent paper explicitly retains the \(n^{1/2+o(1)}\)-pass upper benchmark. No polylogarithmic-pass algorithm or lower bound ruling out every polylogarithmic pass bound in the stated memory model was found. This check covers decision with adversarial fixed order, rather than a changed stream or a path-output requirement.

Sources: [Recent Advances in Multi-Pass Graph Streaming Lower Bounds](https://par.nsf.gov/servlets/purl/10488812); [Superlinear lower bounds for multipass graph processing](https://eccc.weizmann.ac.il/report/2013/002/revision/3/download/); [Parallel Reachability in Almost Linear Work and Square Root Depth](https://arxiv.org/abs/1905.08841); [Semi-Streaming Bipartite Matching in Fewer Passes and Optimal Space](https://arxiv.org/abs/2011.03495); [Almost Optimal Super-Constant-Pass Streaming Lower Bounds for Reachability](https://par.nsf.gov/servlets/purl/10315017); [Streaming Algorithms for Monotonicity Testing](https://arxiv.org/abs/2608.07073v2).

## 126. Shay Solomon

[Research bibliography](https://dblp.org/pid/s/ShaySolomon.html).

### 1. Fully dynamic near-optimal matching with polylogarithmic updates

[TCS-6627](../../data/cards/TCS-6627.json) · reused · status: `source_open` · evidence: `reviewed`.

Near-optimal dynamic matching connects his dynamic matching research.

**Status scope:** Reviewed through 11 September 2026. No polylogarithmic-update algorithm meeting the fixed-accuracy, explicit-matching target was found. Matching-size estimators, ordered-RS-dependent bounds and the 2026 maximal-matching improvement do not resolve it.

Sources: [Sixteenth Biennial Scientific Report: March 2021–March 2023](https://pure.mpg.de/pubman/item/item_3527212_4/component/file_3527885/biennial-report-2023.pdf); [Fully Dynamic Matching: \((2- \sqrt{2})\)-Approximation in Polylog Update Time](https://epubs.siam.org/doi/10.1137/1.9781611977912.109); [Improved Bounds for Fully Dynamic Matching via Ordered Ruzsa-Szemeredi Graphs](https://arxiv.org/abs/2406.13573); [A note on Ordered Ruzsa-Szemerédi graphs](https://arxiv.org/abs/2502.02455); [On Approximate Fully-Dynamic Matching and Online Matrix-Vector Multiplication](https://arxiv.org/abs/2403.02582); [A Faster Deterministic Algorithm for Fully Dynamic Maximal Matching](https://arxiv.org/abs/2605.00797).

### 2. Deterministic fully dynamic connectivity with polylogarithmic worst-case updates

[TCS-6625](../../data/cards/TCS-6625.json) · reused · status: `source_open` · evidence: `reviewed`.

Deterministic dynamic connectivity concerns the worst-case guarantees of the graph data structures he studies.

**Status scope:** Checked through 10 September 2026. The SODA 2026 connectivity paper explicitly retains deterministic polylogarithmic worst-case updates as open. Its unconditional new bound is randomized and expected; its deterministic polylogarithmic conclusion depends on the stated static low-congestion sparsifier construction. Deterministic subpolynomial worst-case bounds and polylogarithmic amortized bounds are already known.

Sources: [Poly-Logarithmic Deterministic Fully-Dynamic Algorithms for Connectivity, Minimum Spanning Tree, 2-Edge, and Biconnectivity](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf); [Dynamic graph connectivity in polylogarithmic worst case time](https://doi.org/10.1137/1.9781611973105.81); [A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond](https://arxiv.org/abs/1910.08025); [Dynamic Connectivity with Expected Polylogarithmic Worst-Case Update Time](https://arxiv.org/abs/2510.08297); [Expander Pruning with Polylogarithmic Worst-Case Recourse and Update Time](https://doi.org/10.1137/1.9781611978971.103); [Logarithmic Lower Bounds in the Cell-Probe Model](https://erikdemaine.org/papers/DynamicConnectivity_SICOMP/).

## 127. Sayan Bhattacharya

[Research bibliography](https://dblp.org/pid/57/3907.html).

### 1. Fully dynamic near-optimal matching with polylogarithmic updates

[TCS-6627](../../data/cards/TCS-6627.json) · reused · status: `source_open` · evidence: `reviewed`.

Near-optimal fully dynamic matching is a central problem in his work.

**Status scope:** Reviewed through 11 September 2026. No polylogarithmic-update algorithm meeting the fixed-accuracy, explicit-matching target was found. Matching-size estimators, ordered-RS-dependent bounds and the 2026 maximal-matching improvement do not resolve it.

Sources: [Sixteenth Biennial Scientific Report: March 2021–March 2023](https://pure.mpg.de/pubman/item/item_3527212_4/component/file_3527885/biennial-report-2023.pdf); [Fully Dynamic Matching: \((2- \sqrt{2})\)-Approximation in Polylog Update Time](https://epubs.siam.org/doi/10.1137/1.9781611977912.109); [Improved Bounds for Fully Dynamic Matching via Ordered Ruzsa-Szemeredi Graphs](https://arxiv.org/abs/2406.13573); [A note on Ordered Ruzsa-Szemerédi graphs](https://arxiv.org/abs/2502.02455); [On Approximate Fully-Dynamic Matching and Online Matrix-Vector Multiplication](https://arxiv.org/abs/2403.02582); [A Faster Deterministic Algorithm for Fully Dynamic Maximal Matching](https://arxiv.org/abs/2605.00797).

### 2. Polylogarithmic worst-case updates for exact dynamic minimum spanning forests

[TCS-6626](../../data/cards/TCS-6626.json) · reused · status: `source_open` · evidence: `reviewed`.

Worst-case dynamic minimum spanning forests connect his dynamic graph-data-structure research.

**Status scope:** Current sources distinguish exact subpolynomial worst-case MSF maintenance from polylogarithmic amortized maintenance and the 2026 approximate weighted extension of connectivity algorithms. The inherited ICALP 2021 link was a mismatched matching citation and is identified as such. Checked through 11 September 2026.

Sources: [Poly-Logarithmic Deterministic Fully-Dynamic Algorithms for Connectivity, Minimum Spanning Tree, 2-Edge, and Biconnectivity](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf); [Faster Fully-Dynamic Minimum Spanning Forest](https://arxiv.org/abs/1407.6832); [Dynamic Minimum Spanning Forest with Subpolynomial Worst-case Update Time](https://arxiv.org/abs/1708.03962); [A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond](https://arxiv.org/abs/1910.08025); [Dynamic Connectivity with Expected Polylogarithmic Worst-Case Update Time](https://arxiv.org/abs/2510.08297); [Deterministic Rounding of Dynamic Fractional Matchings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2021.27).

## 128. Hung Le

[Research bibliography](https://dblp.org/pid/45/466-1.html).

### 1. Optimal additive error of linear-size spanners

[TCS-6785](../../data/cards/TCS-6785.json) · reused · status: `source_open` · evidence: `reviewed`.

Linear-size additive spanners directly concern his distance-preserving graph structures.

**Status scope:** The survey leaves the linear-size error tradeoff open. The later lower-bound and nearly linear upper-bound abstracts were checked on 13 September 2026 and do not give matching bounds for every fixed linear coefficient. No full determination was verified; status remains source_open.

Sources: [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152); [New Additive Spanner Lower Bounds by an Unlayered Obstacle Product](https://arxiv.org/abs/2207.11832); [Almost-Optimal Sublinear Additive Spanners](https://arxiv.org/abs/2303.12768).

### 2. Optimal size of four-additive graph spanners

[TCS-6783](../../data/cards/TCS-6783.json) · reused · status: `source_open` · evidence: `reviewed`.

Four-additive spanner size is a major canonical spanner tradeoff in his research.

**Status scope:** The +4 sparsity gap remains in the 2025 primary source. The broader variable-error linear-size question is retained separately as TCS-6785.

Sources: [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152); [Finding 4-Additive Spanners: Faster, Stronger, and Simpler](https://arxiv.org/abs/2510.17262); [The \(4/3\) Additive Spanner Exponent is Tight](https://arxiv.org/abs/1511.00700).

## 129. Merav Parter

[Research bibliography](https://dblp.org/pid/16/9365.html).

### 1. Spanners matching Thorup–Zwick emulator tradeoffs

[TCS-6784](../../data/cards/TCS-6784.json) · reused · status: `open` · evidence: `reviewed`.

Spanner-emulator tradeoffs connect her distributed distance-preserving structures.

**Status scope:** Checked the tutorial’s quantitative Section 8.2, the original emulator Theorem 4.1, the full 2018 hierarchy paper, and Tan–Zhang’s full October 2024 revision, Theorem 1.1 and Section 4. Confirmed the journal date with publisher metadata and searched subsequent work through 12 September 2026. The almost-optimal result does not attain zero exponent slack with fixed stretch constants. No proof was independently reconstructed.

Sources: [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152); [Spanners and emulators with sublinear distance errors](https://researchprofiles.ku.dk/en/publications/spanners-and-emulators-with-sublinear-distance-errors/); [A Hierarchy of Lower Bounds for Sublinear Additive Spanners](https://doi.org/10.1137/16M1105815); [Almost-Optimal Sublinear Additive Spanners](https://doi.org/10.1137/23M1581078).

### 2. Optimal exact single-source shortest paths in CONGEST

[TCS-6555](../../data/cards/TCS-6555.json) · reused · status: `open` · evidence: `reviewed`.

Optimal CONGEST SSSP concerns her distributed shortest-path algorithms.

**Status scope:** Primary exact CONGEST bounds, randomized distance lower bounds, the approximation result and later-result searches were checked on 11 September 2026. No algorithm or impossibility theorem settling the full stated polylogarithmic-overhead target was found. The inherited 2026 paper is retained as related-work provenance, rather than used alone as evidence of the current best bound.

Sources: [Polylogarithmic time algorithms for shortest path forests in programmable matter](https://link.springer.com/article/10.1007/s00446-026-00505-2); [Single-source shortest paths in the CONGEST model with improved bounds](https://link.springer.com/article/10.1007/s00446-021-00412-8); [Parallel Exact Shortest Paths in Almost Linear Work and Square Root Depth](https://nairenc.github.io/nairenc_files/parallelexactsspsqrt.pdf); [Distributed Verification and Hardness of Distributed Approximation](https://arxiv.org/abs/1011.3049); [Undirected \((1+\varepsilon )\)-Shortest Paths via Minor-Aggregates: Near-Optimal Deterministic Parallel & Distributed Algorithms](https://arxiv.org/abs/2204.05874).

## 130. Barna Saha

[Research bibliography](https://dblp.org/pid/66/3027.html).

### 1. Constant-factor edit-distance approximation in \(O(n \operatorname{polylog} n)\) time

[TCS-6624](../../data/cards/TCS-6624.json) · reused · status: `source_open` · evidence: `reviewed`.

Almost-linear constant-factor edit approximation directly continues her approximate string algorithms.

**Status scope:** Reviewed through 11 September 2026. No \(O(n \operatorname{polylog} n)\)-time, fixed-constant approximation for all input pairs was found in the checked primary sources. The August 2026 journal publication gives \(n^{1+\varepsilon}\) time, and the STOC 2026 approximation scheme targets a different runtime–accuracy regime.

Sources: [Edit Distance in Near-Linear Time: It’s a Constant Factor](https://epubs.siam.org/doi/10.1137/21M1392322); [Edit Distance in Near-Linear Time: it’s a Constant Factor — full manuscript](https://arxiv.org/abs/2005.07678); [Approximating Edit Distance in Near-Linear Time](https://arxiv.org/abs/1109.5635); [Constant factor approximations to edit distance on far input pairs in nearly linear time](https://arxiv.org/abs/1904.05459); [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702); [Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)](https://arxiv.org/abs/1412.0348).

### 2. Min-Plus Convolution Hypothesis

[TCS-6598](../../data/cards/TCS-6598.json) · reused · status: `source_open` · evidence: `reviewed`.

Min-plus convolution connects her fine-grained approximate computation research.

**Status scope:** Sources and subsequent-result searches checked on 13 September 2026. The cited results leave this target unanswered; this is a bounded literature review, not an exhaustive certification of current openness. Completes the existing TCS-6598 integer-word target, including output indexing, magnitude quantifiers, bounded error and worst-case cost. The established hypothesis title is retained; the yes/no statement asks whether its algorithmic negation holds.

Sources: [Deterministic Monotone Min-Plus Product and Convolution](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.119); [Necklaces, Convolutions, and \(X+Y\)](https://tmc.web.engr.illinois.edu/convol.pdf).

## 131. Rico Zenklusen

[Research bibliography](https://dblp.org/pid/48/4189.html).

### 1. Matroid secretary conjecture

[TCS-7316](../../data/cards/TCS-7316.json) · reused · status: `source_open` · evidence: `reviewed`.

Matroid secretary is central to his matroid and stochastic optimization work.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. No polynomial-time restriction has been silently appended. Earlier exclusions TCS-2570 and TCS-5552 address narrower algorithm/model questions.

Sources: [Constant-Competitiveness for Random Assignment Matroid Secretary Without Knowing the Matroid](https://arxiv.org/abs/2305.05353).

### 2. Optimal polynomial-time approximation ratio for Steiner Tree

[TCS-7358](../../data/cards/TCS-7358.json) · added · status: `source_open` · evidence: `reviewed`.

Optimal Steiner-tree approximation extends his network-design and approximation research.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [Steiner Tree Approximation via Iterative Randomized Rounding](https://doi.org/10.1145/2432622.2432628); [Better-Than-2 Approximations for Weighted Tree Augmentation and Applications to Steiner Tree](https://doi.org/10.1145/3722101).

## 132. Anindya De

[Research bibliography](https://dblp.org/pid/49/2398.html).

### 1. Learning Boolean juntas from uniform random examples

[TCS-6543](../../data/cards/TCS-6543.json) · reused · status: `source_open` · evidence: `reviewed`.

Uniform junta learning is directly in his learning-theory research.

**Status scope:** No general learner with the stated polynomial dependence, or impossibility theorem for unrestricted learners, was found through 11 September 2026. Current sources retain the uniform-example barrier. Efficient membership-query, monotone-junta and correlated-random-walk results do not meet this exact model.

Sources: [Learning functions of k relevant variables; author manuscript titled Learning juntas](https://www.cs.cmu.edu/~odonnell/papers/juntas.pdf); [Finding Correlations in Subquadratic Time, with Applications to Learning Parities and the Closest Pair Problem](https://theory.stanford.edu/~valiant/papers/corrFull.pdf); [The Probably Approximately Correct Learning Model in Computational Learning Theory](https://arxiv.org/abs/2511.08791); [New Statistical and Computational Results for Learning Junta Distributions](https://arxiv.org/abs/2505.05819); [The Benefits of Temporal Correlations: SGD Learns k-Juntas from Random Walks Efficiently](https://arxiv.org/abs/2605.10237); [Inherited OpenReview research pointer; bibliographic identity not verified](https://openreview.net/pdf?id=wszZlP1K14); [Mathematics and Computation (March 27, 2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf).

### 2. Mansour’s conjecture

[TCS-6581](../../data/cards/TCS-6581.json) · reused · status: `source_open` · evidence: `reviewed`.

Mansour connects his Fourier analysis and efficient learning work.

**Status scope:** Open in the strong logarithmic-accuracy form stated here, following the inspected primary sources and a later-result search through 11 September 2026. Fixed-error polynomial concentration, restricted DNF models, and generalized-basis learning results do not by themselves settle this formulation.

Sources: [The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions](https://www.ias.edu/sites/default/files/math/ODonnell_Fourier.pdf); [Mansour’s Conjecture is True for Random DNF Formulas](https://eccc.weizmann.ac.il/report/2010/023/revision/3/download/); [Sharper bounds on the Fourier concentration of DNFs](https://arxiv.org/abs/2109.04525v2); [A New Bound for the Fourier-Entropy-Influence Conjecture](https://link.springer.com/article/10.1007/s00493-024-00133-z); [Further evidence towards the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/2606.00246v2); [Learning DNF through Generalized Fourier Representations](https://arxiv.org/abs/2506.01075v2).

## 133. Xin Li

[Research bibliography](https://dblp.org/pid/09/1365-6.html).

### 1. Two-source extraction at log n plus constant entropy

[TCS-7271](../../data/cards/TCS-7271.json) · reused · status: `source_open` · evidence: `reviewed`.

Entropy-threshold two-source extraction directly extends his extractor constructions.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Two Source Extractors for Asymptotically Optimal Entropy, and (Many) More](https://arxiv.org/abs/2303.06802).

### 2. Seeded extraction with constant total entropy loss

[TCS-1015](../../data/cards/TCS-1015.json) · reused · status: `uncertain` · evidence: `index`.

Optimal seeded extraction concerns the randomness primitives he studies.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 134. Amnon Ta-Shma

[Research bibliography](https://dblp.org/pid/t/AmnonTaShma.html).

### 1. Explicit efficiently decoded binary codes beyond Gilbert–Varshamov

[TCS-1012](../../data/cards/TCS-1012.json) · reused · status: `uncertain` · evidence: `index`.

Efficient binary codes beyond Gilbert-Varshamov extend his explicit-code research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

### 2. Optimal explicit pseudorandom generators for read-once branching programs

[TCS-6600](../../data/cards/TCS-6600.json) · reused · status: `source_open` · evidence: `reviewed`.

Optimal small-space PRGs connect his derandomization and extractor work.

**Status scope:** Checked through 10 September 2026. ECCC TR26-064 revision 3 explicitly retains the optimal general PRG target and the log-squared barrier. Its new generator is weighted; the July TR26-123 result is restricted to permutation programs. This card requires one ordinary, program-independent distribution family and optimal seed length as well as optimal work space.

Sources: [Pseudorandom generators for space-bounded computation](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf); [Better Pseudodistributions and Derandomization for Space-Bounded Computation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2021.28); [Hitting Sets Give Two-Sided Derandomization of Small Space](https://theoryofcomputing.org/articles/v018a021/); [Weighted Pseudorandom Generators for Read-Once Branching Programs via Weighted Pseudorandom Reductions](https://epubs.siam.org/doi/10.1137/1.9781611978971.124); [Improved Error Reduction for Weighted PRGs](https://eccc.weizmann.ac.il/report/2026/064/); [A Forward-Backward Weight Analysis of INW for Permutation Branching Programs](https://eccc.weizmann.ac.il/report/2026/123/).

## 135. Gil Cohen

[Research bibliography](https://dblp.org/pid/25/8727.html).

### 1. Two-source extraction at log n plus constant entropy

[TCS-7271](../../data/cards/TCS-7271.json) · reused · status: `source_open` · evidence: `reviewed`.

Two-source extraction at the existential threshold concerns his extractor research.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Two Source Extractors for Asymptotically Optimal Entropy, and (Many) More](https://arxiv.org/abs/2303.06802).

### 2. Optimal explicit pseudorandom generators for read-once branching programs

[TCS-6600](../../data/cards/TCS-6600.json) · reused · status: `source_open` · evidence: `reviewed`.

Optimal branching-program PRGs connect his pseudorandom generator constructions.

**Status scope:** Checked through 10 September 2026. ECCC TR26-064 revision 3 explicitly retains the optimal general PRG target and the log-squared barrier. Its new generator is weighted; the July TR26-123 result is restricted to permutation programs. This card requires one ordinary, program-independent distribution family and optimal seed length as well as optimal work space.

Sources: [Pseudorandom generators for space-bounded computation](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf); [Better Pseudodistributions and Derandomization for Space-Bounded Computation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2021.28); [Hitting Sets Give Two-Sided Derandomization of Small Space](https://theoryofcomputing.org/articles/v018a021/); [Weighted Pseudorandom Generators for Read-Once Branching Programs via Weighted Pseudorandom Reductions](https://epubs.siam.org/doi/10.1137/1.9781611978971.124); [Improved Error Reduction for Weighted PRGs](https://eccc.weizmann.ac.il/report/2026/064/); [A Forward-Backward Weight Analysis of INW for Permutation Branching Programs](https://eccc.weizmann.ac.il/report/2026/123/).

## 136. Tali Kaufman

[Research bibliography](https://dblp.org/pid/42/209.html).

### 1. Linear-length locally testable codes and proofs

[TCS-6738](../../data/cards/TCS-6738.json) · reused · status: `source_open` · evidence: `source`.

Linear-length local testability is central to her codes and high-dimensional expansion work.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2017 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html).

### 2. Asymptotically good quantum locally testable stabilizer codes

[TCS-6515](../../data/cards/TCS-6515.json) · reused · status: `source_open` · evidence: `reviewed`.

Good quantum local testability concerns the quantum extensions of this expansion program.

**Status scope:** Checked through 11 September 2026. No bounded-degree stabilizer family with constant rate, relative distance and normalized soundness was located. The corrected 2025 and July 2026 constructions retain inverse-polylogarithmic losses, while constant-soundness variants increase locality or sacrifice other parameters.

Sources: [Quantum Locally Testable Code with Constant Soundness](https://quantum-journal.org/papers/q-2024-10-18-1501/); [Asymptotically Good Quantum and Locally Testable Classical LDPC Codes](https://arxiv.org/abs/2111.03654); [Local testability of distance-balanced quantum codes](https://www.nature.com/articles/s41534-024-00908-8); [Expansion of higher-dimensional cubical complexes with application to quantum locally testable codes](https://arxiv.org/abs/2402.07476); [NLTS Hamiltonians from Good Quantum Codes](https://arxiv.org/abs/2206.13228); [Transversal non-Clifford gates on almost-good quantum LDPC and quantum locally testable codes](https://arxiv.org/abs/2604.01874); [Probabilistically Checking Quantum Proofs, with Interaction](https://arxiv.org/abs/2606.09588).

## 137. Mary Wootters

[Research bibliography](https://dblp.org/pid/79/7019.html).

### 1. Full-length Reed–Solomon list decoding beyond Johnson

[TCS-1011](../../data/cards/TCS-1011.json) · reused · status: `uncertain` · evidence: `index`.

Full-length Reed-Solomon list decoding directly concerns her coding research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/).

### 2. Constant-rate binary locally decodable codes with logarithmic query complexity

[TCS-6609](../../data/cards/TCS-6609.json) · reused · status: `open` · evidence: `reviewed`.

Constant-rate binary local decoding is a major frontier related to her local-code work.

**Status scope:** The 2 April 2026 source explicitly identifies this binary problem as open. The January 2026 HDX result has different decoding guarantees. A search through 11 September 2026 found no resolution of the stated ordinary binary query model; this is a bounded literature check, not an independent proof audit.

Sources: [Asymptotically good large-alphabet LDCs with polylogarithmic query complexity](https://eccc.weizmann.ac.il/report/2025/168/revision/1/download/); [High Rate Efficient Local List Decoding from HDX](https://arxiv.org/abs/2601.22535v1).

## 138. Andrei Bulatov

[Research bibliography](https://dblp.org/pid/b/AndreiABulatov.html).

### 1. Finite-domain promise CSP dichotomy

[TCS-6635](../../data/cards/TCS-6635.json) · reused · status: `source_open` · evidence: `reviewed`.

Promise-CSP dichotomy is a main frontier after the finite-domain CSP dichotomy he proved.

**Status scope:** Open classification question in the cited survey, with relevant partial results checked through 10 September 2026. The card asks for an unconditional decision dichotomy over all fixed finite template pairs; it does not assume decision/search equivalence or a complete algebraic classification.

Sources: [An invitation to the promise constraint satisfaction problem](https://arxiv.org/abs/2208.13538); [A dichotomy theorem for nonuniform CSPs](https://arxiv.org/abs/1703.03021); [A Proof of the CSP Dichotomy Conjecture](https://arxiv.org/abs/1704.01914); [Promise Constraint Satisfaction: Algebraic Structure and a Symmetric Boolean Dichotomy](https://arxiv.org/abs/1704.01937); [Promises Make Finite (Constraint Satisfaction) Problems Infinitary](https://www.karlin.mff.cuni.cz/~barto/Articles/DoNotPromise.pdf); [Towards infinite PCSP: a dichotomy for monochromatic cliques](https://arxiv.org/abs/2605.09815).

### 2. Bodirsky–Pinsker conjecture

[TCS-6636](../../data/cards/TCS-6636.json) · reused · status: `source_open` · evidence: `reviewed`.

Infinite-domain CSP dichotomy extends his algebraic classification program.

**Status scope:** Checked through 10 September 2026. The latest checked primary papers explicitly retain the general dichotomy as open. The July \(FO/\mathrm{L}\)-hard classification has both a different complexity boundary and an expansion hypothesis; the August interpretability result does not settle tractability.

Sources: [A Proof of the CSP Dichotomy Conjecture](https://arxiv.org/abs/1704.01914); [Complexity of Infinite-Domain Constraint Satisfaction](https://wwwpub.zih.tu-dresden.de/~bodirsky/Book.pdf); [Topology Is Irrelevant (In a Dichotomy Conjecture for Infinite Domain Constraint Satisfaction Problems)](https://doi.org/10.1137/18M1216213); [Three Fundamental Questions in Modern Infinite-Domain Constraint Satisfaction](https://arxiv.org/abs/2502.06621); [Constraint Satisfaction Problems over Finitely Bounded Homogeneous Structures: a Dichotomy between FO and L-hard](https://arxiv.org/abs/2601.22691); [Decidability of Interpretability](https://arxiv.org/abs/2602.02302).

## 139. Dmitriy Zhuk

[Research bibliography](https://dblp.org/pid/05/11522.html).

### 1. Finite-domain promise CSP dichotomy

[TCS-6635](../../data/cards/TCS-6635.json) · reused · status: `source_open` · evidence: `reviewed`.

Promise-CSP dichotomy continues the algebraic complexity classification he helped establish.

**Status scope:** Open classification question in the cited survey, with relevant partial results checked through 10 September 2026. The card asks for an unconditional decision dichotomy over all fixed finite template pairs; it does not assume decision/search equivalence or a complete algebraic classification.

Sources: [An invitation to the promise constraint satisfaction problem](https://arxiv.org/abs/2208.13538); [A dichotomy theorem for nonuniform CSPs](https://arxiv.org/abs/1703.03021); [A Proof of the CSP Dichotomy Conjecture](https://arxiv.org/abs/1704.01914); [Promise Constraint Satisfaction: Algebraic Structure and a Symmetric Boolean Dichotomy](https://arxiv.org/abs/1704.01937); [Promises Make Finite (Constraint Satisfaction) Problems Infinitary](https://www.karlin.mff.cuni.cz/~barto/Articles/DoNotPromise.pdf); [Towards infinite PCSP: a dichotomy for monochromatic cliques](https://arxiv.org/abs/2605.09815).

### 2. Search-to-decision equivalence for finite promise CSPs

[TCS-6675](../../data/cards/TCS-6675.json) · reused · status: `source_open` · evidence: `reviewed`.

Search versus decision for promise CSPs concerns the limits of the algebraic approach.

**Status scope:** Explicitly open in §10 of Larrauri’s revised full paper, dated 25 May 2026. Its rounding hardness uses a weaker input promise than \(X\to A\), and its meta-problem undecidability varies the template. The revision corrects earlier overbroad interpretations. No full resolution found through 11 September 2026; this card asks the per-template tractability implication, not a stronger uniform black-box reduction theorem.

Sources: [An invitation to the promise constraint satisfaction problem](https://arxiv.org/abs/2208.13538); [Algebraic approach to promise constraint satisfaction](https://arxiv.org/abs/1811.00970); [Ineffectiveness for Search and Undecidability of PCSP Meta-Problems](https://arxiv.org/abs/2504.04639); [New Algorithms and Hardness Results for Robust Satisfiability of (Promise) CSPs](https://arxiv.org/abs/2602.10368); [Publications — FOCS 2025 research summary](https://albertolarrauri.github.io/publications/).

## 140. Jin-Yi Cai

[Research bibliography](https://dblp.org/pid/c/JinyiCai.html).

### 1. #BIS-easiness of Boolean log-supermodular counting CSPs

[TCS-7320](../../data/cards/TCS-7320.json) · reused · status: `source_open` · evidence: `reviewed`.

Boolean log-supermodular approximate counting concerns his counting-CSP and Holant classifications.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. The finite rational-weight formulation follows the conservative counting-CSP literature. No recent source settling this full reduction was identified; current-status confidence is bounded by the dated sources.

Sources: [Counting Constraint Satisfaction Problems](https://drops.dagstuhl.de/storage/02dagstuhl-follow-ups/dfu-vol007/DFU.Vol7.15301.205/DFU.Vol7.15301.205.pdf); [The complexity of approximating conservative counting CSPs](https://arxiv.org/abs/1208.1783).

### 2. FPRAS for #BIS

[TCS-7221](../../data/cards/TCS-7221.json) · reused · status: `source_open` · evidence: `reviewed`.

The complexity of #BIS is a central unresolved point in approximate-counting dichotomies.

**Status scope:** Checked through 11 September 2026. No FPRAS for #BIS on arbitrary bipartite graphs, and no unconditional impossibility theorem, was found in the cited literature; the positive results listed here impose structural restrictions.

Sources: [A Fixed-Parameter Perspective on #BIS](https://link.springer.com/article/10.1007/s00453-019-00606-4); [Counting Independent Sets and Colorings on Random Regular Bipartite Graphs](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2019.34); [A Spectral Approach to Approximately Counting Independent Sets in Dense Bipartite Graphs](https://arxiv.org/abs/2307.09533).

## 141. Pinyan Lu

[Research bibliography](https://dblp.org/pid/03/4112.html).

### 1. #BIS-easiness of Boolean log-supermodular counting CSPs

[TCS-7320](../../data/cards/TCS-7320.json) · reused · status: `source_open` · evidence: `reviewed`.

The #BIS-easiness conjecture concerns his approximate-counting classification work.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. The finite rational-weight formulation follows the conservative counting-CSP literature. No recent source settling this full reduction was identified; current-status confidence is bounded by the dated sources.

Sources: [Counting Constraint Satisfaction Problems](https://drops.dagstuhl.de/storage/02dagstuhl-follow-ups/dfu-vol007/DFU.Vol7.15301.205/DFU.Vol7.15301.205.pdf); [The complexity of approximating conservative counting CSPs](https://arxiv.org/abs/1208.1783).

### 2. Randomized truthful unrelated-machine scheduling

[TCS-6674](../../data/cards/TCS-6674.json) · reused · status: `source_open` · evidence: `reviewed`.

Randomized truthful scheduling connects his mechanism-design research.

**Status scope:** The Nisan–Ronen proof, now published in JACM in February 2026, resolves only deterministic truthful mechanisms. Its randomized discussion records \(2- 1/m\) and \((m+5)/2\) bounds. Searches through 11 September 2026 found no matching unrestricted randomized bounds; results for task-independent mechanisms, fractional objectives, Bayesian types or no-payment models do not resolve this formulation.

Sources: [A proof of the Nisan–Ronen conjecture](https://arxiv.org/abs/2301.11905); [A Proof of the Nisan–Ronen Conjecture](https://doi.org/10.1145/3785408); [Setting Lower Bounds on Truthfulness](https://arxiv.org/abs/1507.08708); [Randomized Truthful Mechanisms for Scheduling Unrelated Machines](https://link.springer.com/chapter/10.1007/978-3-540-92185-1_46); [An Improved Randomized Truthful Mechanism for Scheduling Unrelated Machines](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2008.1314); [New Bounds for Truthful Scheduling on Two Unrelated Selfish Machines](https://link.springer.com/article/10.1007/s00224-019-09927-x); [A proof of the Nisan–Ronen conjecture — Oxford repository copy](https://ora.ox.ac.uk/objects/uuid%3A814fc511-99e2-47cb-b06a-f472630996dc/files/r9593tw016).

## 142. Martin Grohe

[Research bibliography](https://dblp.org/pid/g/MGrohe.html).

### 1. Graph canonization versus graph isomorphism

[TCS-7180](../../data/cards/TCS-7180.json) · reused · status: `source_open` · evidence: `reviewed`.

Canonization versus isomorphism is central to his graph-isomorphism and logic work.

**Status scope:** The reverse relation is open in the checked 2019 primary discussion. The reviewed ICALP 2026 result concerns random regular graphs and does not settle the general reduction. Searches through 11 September 2026 found no established resolution; this is not an independent audit of all later work.

Sources: [Canonical Form for Graphs in Quasipolynomial Time](https://par.nsf.gov/servlets/purl/10179675); [Wikipedia: Graph canonization](https://en.wikipedia.org/wiki/Graph_canonization); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1330143987); [Canonical Labelling of Random Regular Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.114).

### 2. Seese’s conjecture

[TCS-6654](../../data/cards/TCS-6654.json) · reused · status: `source_open` · evidence: `reviewed`.

Seese's conjecture connects logical tractability to graph structure.

**Status scope:** Reviewed through 11 September 2026. Seese’s MSO\(_{1}\) decidability implication remains unresolved in the checked primary literature. The parity extension, the shrub-depth expressiveness characterization and the July 2026 2-WQO result have distinct hypotheses or conclusions.

Sources: [Forbidden Induced Subgraphs for Bounded Shrub-Depth and the Expressive Power of MSO](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.167); [The structure of the models of decidable monadic theories of graphs](https://doi.org/10.1016/0168-0072(91)90054-P); [Vertex-minors, monadic second-order logic, and a conjecture by Seese](https://www.labri.fr/perso/courcell/Textes1/BC-Oum%282007%29.pdf); [MSO undecidability for hereditary classes of unbounded clique-width](https://doi.org/10.1016/j.ejc.2023.103700); [Hereditary 2-WQO Graph Classes Have Bounded Clique-Width](https://arxiv.org/abs/2607.10939).

## 143. Eric Vigoda

[Research bibliography](https://dblp.org/pid/03/4633.html).

### 1. Rapid mixing of Glauber dynamics with \(\Delta +2\) colours

[TCS-6621](../../data/cards/TCS-6621.json) · reused · status: `source_open` · evidence: `reviewed`.

Mixing for Delta-plus-two colorings is central to his coloring-sampling work.

**Status scope:** Reviewed through 11 September 2026. The general-graph \(\Delta +2\) conjecture remains open in the checked sources. August 2026 results improve restricted-girth regimes with fixed relative slack; they do not establish the universal additive-two bound.

Sources: [Glauber dynamics for colourings of chordal graphs and graphs of bounded treewidth](https://arxiv.org/abs/2010.16158); [Sampling Colorings with Fixed Color Class Sizes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.134); [Flip Dynamics for Sampling Colorings: Improving \((11/6- \varepsilon )\) Using a Simple Metric](https://arxiv.org/abs/2407.04870); [Sampling Colorings Close to the Maximum Degree: Non-Markovian Coupling and Local Uniformity](https://arxiv.org/abs/2604.11938); [A Spectral Local-to-Global Principle for Spin Systems on Graphs with Girth At Least Five](https://arxiv.org/abs/2608.25491).

### 2. FPRAS for counting perfect matchings

[TCS-6628](../../data/cards/TCS-6628.json) · reused · status: `source_open` · evidence: `reviewed`.

FPRAS for general perfect matching extends his celebrated bipartite counting result.

**Status scope:** Checked through 10 September 2026. The general-graph question remains open in the checked primary literature. The August 2026 improvement is a permanent algorithm for bipartite graphs. Slow mixing of the particular general-graph Markov chains does not establish impossibility of all FPRAS approaches.

Sources: [Approximating the Permanent](https://doi.org/10.1137/0218077); [A Polynomial-Time Approximation Algorithm for the Permanent of a Matrix with Nonnegative Entries](https://faculty.cc.gatech.edu/~vigoda/Permanent.pdf); [On Counting Perfect Matchings in General Graphs](https://arxiv.org/abs/1712.07504); [Two-State Spin Systems with Negative Interactions](https://arxiv.org/abs/2309.04735); [Faster FPRAS for the Permanent via Restricted Poincaré Inequalities and Coupled Flows](https://arxiv.org/abs/2608.26599).

## 144. Yitong Yin

[Research bibliography](https://dblp.org/pid/30/328.html).

### 1. Rapid mixing of Glauber dynamics with \(\Delta +2\) colours

[TCS-6621](../../data/cards/TCS-6621.json) · reused · status: `source_open` · evidence: `reviewed`.

Coloring Glauber dynamics connects his sampling and correlation-decay research.

**Status scope:** Reviewed through 11 September 2026. The general-graph \(\Delta +2\) conjecture remains open in the checked sources. August 2026 results improve restricted-girth regimes with fixed relative slack; they do not establish the universal additive-two bound.

Sources: [Glauber dynamics for colourings of chordal graphs and graphs of bounded treewidth](https://arxiv.org/abs/2010.16158); [Sampling Colorings with Fixed Color Class Sizes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.134); [Flip Dynamics for Sampling Colorings: Improving \((11/6- \varepsilon )\) Using a Simple Metric](https://arxiv.org/abs/2407.04870); [Sampling Colorings Close to the Maximum Degree: Non-Markovian Coupling and Local Uniformity](https://arxiv.org/abs/2604.11938); [A Spectral Local-to-Global Principle for Spin Systems on Graphs with Girth At Least Five](https://arxiv.org/abs/2608.25491).

### 2. Polynomial mixing of critical three-dimensional Ising dynamics

[TCS-6668](../../data/cards/TCS-6668.json) · reused · status: `source_open` · evidence: `source`.

Critical Ising mixing concerns his spin-system sampling work.

**Status scope:** Retained in the source-based research proposal dated 10 September 2026. High-dimensional lattice results and the 2024 result at the tree uniqueness threshold do not resolve the three-dimensional lattice critical point. Status is assessed from these primary results and later-result searches.

Sources: [Log-Sobolev inequality for near critical Ising models](https://arxiv.org/abs/2202.02301); [Polynomial Mixing of the critical Glauber Dynamics for the Ising Model](https://arxiv.org/abs/2411.10318).

## 145. Alistair Sinclair

[Research bibliography](https://dblp.org/pid/s/AlistairSinclair.html).

### 1. FPRAS for counting perfect matchings

[TCS-6628](../../data/cards/TCS-6628.json) · reused · status: `source_open` · evidence: `reviewed`.

General perfect-matching counting extends his approximation-scheme work.

**Status scope:** Checked through 10 September 2026. The general-graph question remains open in the checked primary literature. The August 2026 improvement is a permanent algorithm for bipartite graphs. Slow mixing of the particular general-graph Markov chains does not establish impossibility of all FPRAS approaches.

Sources: [Approximating the Permanent](https://doi.org/10.1137/0218077); [A Polynomial-Time Approximation Algorithm for the Permanent of a Matrix with Nonnegative Entries](https://faculty.cc.gatech.edu/~vigoda/Permanent.pdf); [On Counting Perfect Matchings in General Graphs](https://arxiv.org/abs/1712.07504); [Two-State Spin Systems with Negative Interactions](https://arxiv.org/abs/2309.04735); [Faster FPRAS for the Permanent via Restricted Poincaré Inequalities and Coupled Flows](https://arxiv.org/abs/2608.26599).

### 2. FPRAS for #BIS

[TCS-7221](../../data/cards/TCS-7221.json) · reused · status: `source_open` · evidence: `reviewed`.

#BIS is a central counting-complexity barrier in his MCMC field.

**Status scope:** Checked through 11 September 2026. No FPRAS for #BIS on arbitrary bipartite graphs, and no unconditional impossibility theorem, was found in the cited literature; the positive results listed here impose structural restrictions.

Sources: [A Fixed-Parameter Perspective on #BIS](https://link.springer.com/article/10.1007/s00453-019-00606-4); [Counting Independent Sets and Colorings on Random Regular Bipartite Graphs](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2019.34); [A Spectral Approach to Approximately Counting Independent Sets in Dense Bipartite Graphs](https://arxiv.org/abs/2307.09533).

## 146. Umesh Vazirani

[Research bibliography](https://dblp.org/pid/v/UVVazirani.html).

### 1. Quantum PCP conjecture

[TCS-6446](../../data/cards/TCS-6446.json) · reused · status: `source_open` · evidence: `reviewed`.

Quantum PCP directly concerns his quantum verification and Hamiltonian-complexity research.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495); [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/).

### 2. NP outside BQP

[TCS-0037](../../data/cards/TCS-0037.json) · reused · status: `source_open` · evidence: `reviewed`.

The power of quantum computation on NP connects his foundational quantum-complexity work.

**Status scope:** No unconditional separation or general quantum polynomial-time SAT algorithm found through 11 September 2026. Black-box lower bounds do not establish the ordinary language-class separation. June 2026 work continues to use \(\mathrm{NP}\nsubseteq \mathrm{BQP}\) explicitly as an unproved hardness hypothesis.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027); [A fast quantum mechanical algorithm for database search](https://arxiv.org/abs/quant-ph/9605043); [Strengths and Weaknesses of Quantum Computing](https://arxiv.org/abs/quant-ph/9701001); [Complexity of detecting large coefficients in the Pauli basis](https://arxiv.org/abs/2606.19545).

## 147. Ronald de Wolf

[Research bibliography](https://dblp.org/pid/w/RonalddeWolf.html).

### 1. Quantum query complexity versus bounded approximate degree

[TCS-0033](../../data/cards/TCS-0033.json) · reused · status: `uncertain` · evidence: `index`.

Query complexity versus approximate degree is a central quantum lower-bound question in his research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf).

### 2. Superpolynomial semidefinite extension complexity of perfect matching

[TCS-7283](../../data/cards/TCS-7283.json) · reused · status: `source_open` · evidence: `reviewed`.

SDP extension lower bounds connect his work on quantum communication and optimization.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Lower Bounds for Interactive Compression and Linear Programs](https://digital.lib.washington.edu/server/api/core/bitstreams/a7ac9607-c4f8-4d56-9b29-0f5ef033975d/content).

## 148. Andris Ambainis

[Research bibliography](https://dblp.org/pid/70/5481.html).

### 1. Aaronson–Ambainis conjecture

[TCS-6605](../../data/cards/TCS-6605.json) · reused · status: `source_open` · evidence: `reviewed`.

He co-posed the conjecture linking bounded polynomials to quantum query limitations.

**Status scope:** The 4 September 2026 primary paper explicitly leaves the unrestricted Aaronson–Ambainis conjecture open. Recent restricted-model and bounded-round results do not prove it; the 2019 general claim remains withdrawn. Checked through 11 September 2026.

Sources: [The Need for Structure in Quantum Speedups](https://arxiv.org/abs/0911.0996); [Quantum speedups need structure — withdrawn](https://arxiv.org/abs/1911.03748); [Influence in Completely Bounded Block-Multilinear Forms and Classical Simulation of Quantum Algorithms](https://ir.cwi.nl/pub/31883/31883.pdf); [Random Restrictions of Bounded Low Degree Polynomials Are Juntas](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.17); [Aaronson-Ambainis Conjecture Is True For Random Restrictions](https://eccc.weizmann.ac.il/report/2024/035/); [Quantum Speedups Require Structure or Depth](https://arxiv.org/abs/2608.19158); [Optimal inequalities for completely bounded polynomials and the limitations of quantum query algorithms](https://arxiv.org/abs/2609.05201).

### 2. Maximum randomized-versus-quantum gap for total functions

[TCS-0029](../../data/cards/TCS-0029.json) · reused · status: `uncertain` · evidence: `index`.

The largest quantum speedup for total functions is a direct quantum-query research target.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf).

## 149. Aram Harrow

[Research bibliography](https://dblp.org/pid/03/2246.html).

### 1. QMA versus \(\mathrm{QMA}(2)\)

[TCS-2229](../../data/cards/TCS-2229.json) · reused · status: `uncertain` · evidence: `index`.

QMA versus two unentangled proofs connects his quantum proof-system and product-state work.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Quantum Merlin-Arthur and Proofs Without Relative Phase](https://doi.org/10.4230/LIPIcs.ITCS.2024.9).

### 2. Area law for gapped two-dimensional Hamiltonians

[TCS-6516](../../data/cards/TCS-6516.json) · reused · status: `source_open` · evidence: `reviewed`.

Two-dimensional area laws connect his quantum many-body and tensor-network research.

**Status scope:** Checked through 10 September 2026. The February and April 2026 results retain extra hypotheses; the general globally gapped 2D entropy area law remains unresolved. The formulation explicitly requires a size-independent constant and fixes the geometric boundary, interaction norms, local dimension, uniqueness, and global gap.

Sources: [An Area Law for One Dimensional Quantum Systems](https://arxiv.org/abs/0705.2024v4); [An area law for 2D frustration-free spin systems](https://arxiv.org/abs/2103.02492v3); [Entanglement spread area law in gapped ground states](https://doi.org/10.1038/s41567-022-01740-7); [Area Laws and Tensor Networks for Maximally Mixed Ground States](https://doi.org/10.1007/s00220-026-05554-z); [Quantum matter is weakly entangled at low energies](https://arxiv.org/abs/2604.14143v1); [Two-dimensional local Hamiltonian problem with area laws is QMA-complete](https://doi.org/10.1016/j.jcp.2021.110534).

## 150. András Gilyén

[Research bibliography](https://dblp.org/pid/198/5085.html).

### 1. Quantum query complexity versus bounded approximate degree

[TCS-0033](../../data/cards/TCS-0033.json) · reused · status: `uncertain` · evidence: `index`.

Polynomial approximation versus quantum queries connects the foundations of singular-value transformation.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf).

### 2. Dihedral hidden subgroup problem in BQP

[TCS-6521](../../data/cards/TCS-6521.json) · reused · status: `uncertain` · evidence: `reviewed`.

Efficient dihedral HSP is a central quantum-algorithm barrier relevant to his algorithmic program.

**Status scope:** Reviewed through 11 September 2026. No verified polynomial-time solution is recorded. Simon’s August 2026 coset-algorithm claim is disputed: the September 1 Gupte–Ragavan–Zhandry response proves failure of the proposed template, and Guo–Yang identify an unsupported independence hypothesis. The review checked these primary statements without independently rerunning the Lean development. The 2022 Moore–Young claim was explicitly withdrawn.

Sources: [Another subexponential-time quantum algorithm for the dihedral hidden subgroup problem](https://arxiv.org/abs/1112.3333); [A Subexponential-Time Quantum Algorithm for the Dihedral Hidden Subgroup Problem](https://epubs.siam.org/doi/10.1137/S0097539703436345); [The dihedral hidden subgroup problem](https://arxiv.org/abs/2106.09907); [A Subexponential Time Algorithm for the Dihedral Hidden Subgroup Problem with Polynomial Space](https://arxiv.org/abs/quant-ph/0406151); [Quantum Computation and Lattice Problems](https://cims.nyu.edu/~regev/papers/quantum_average.pdf); [A Quantum Polynomial-Time Solution to The Dihedral Hidden Subgroup Problem](https://arxiv.org/abs/2202.09697); [A Polynomial-Time Quantum Algorithm for the Dihedral Coset Problem](https://eprint.iacr.org/2026/1591); [The ePrint:\(2026/1591\) Quantum Algorithm Does Not Solve DCP](https://eprint.iacr.org/2026/1693); [Rigorous Statements and Proofs of the Lemmas in Simon's Algorithm for the Dihedral Coset Problem and Their Underlying Hypothesis](https://arxiv.org/abs/2608.16598); [The Hidden Subgroup Problem in Semidirect Products and Quasi-Hamiltonian Groups](https://arxiv.org/abs/2608.05321).

## 151. Alexander Sherstov

[Research bibliography](https://dblp.org/pid/93/259.html).

### 1. Log-rank conjecture

[TCS-6603](../../data/cards/TCS-6603.json) · reused · status: `source_open` · evidence: `reviewed`.

Log-rank is a central communication-complexity target related to his lower-bound research.

**Status scope:** Explicitly open in the August 2026 CCC version of Hambardzumyan–Lovett–Shirley. Checked through 10 September 2026. The established general upper bound is \(O(\sqrt{r})\); recent fixed-polynomial lower-bound refinements and signed-decomposition equivalences do not settle the conjecture.

Sources: [The Log-Rank Conjecture: New Equivalent Formulations](https://arxiv.org/abs/2510.02583v3); [Matrix discrepancy and the log-rank conjecture](https://doi.org/10.1007/s10107-024-02117-9); [Deterministic Communication vs. Partition Number](https://doi.org/10.1137/16M1059369); [Alphabet-Preserving Lifting for the Log-Rank Conjecture](https://arxiv.org/abs/2608.01812v1).

### 2. Exponential lower bounds for unrestricted threshold-of-threshold circuits

[TCS-1054](../../data/cards/TCS-1054.json) · reused · status: `source_open` · evidence: `reviewed`.

Threshold-of-threshold lower bounds connect his sign-rank and approximation methods.

**Status scope:** The source states this challenge as open. The source-wide explicitness convention and circuit model were rechecked on 13 September 2026, together with the abstract of Chen’s subsequent work and a limited later-work search. No unconditional resolution was verified; this is not an exhaustive status review, and status remains source_open.

Sources: [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html); [Toward Super-Polynomial Size Lower Bounds for Depth-Two Threshold Circuits](https://arxiv.org/abs/1805.10698).

## 152. Omri Weinstein

[Research bibliography](https://dblp.org/pid/85/9060.html).

### 1. Constant-factor randomized direct sums for total Boolean functions

[TCS-5892](../../data/cards/TCS-5892.json) · reused · status: `source_open` · evidence: `reviewed`.

Direct sums for total functions concern his amortization and information-complexity research.

**Status scope:** A user-authorized precise total-Boolean-function variant. The August 2026 primary preprint explicitly distinguishes relations from the remaining total-function question. Rechecked on 13 September 2026; its new theorem is a reported preprint claim, not an independently verified result or a refutation of this target.

Sources: [Lifting Theorems for Equality](https://doi.org/10.4230/LIPIcs.STACS.2019.50); [Efficient Communication Using Partial Information](https://eccc.weizmann.ac.il/report/2010/083/); [Zero-error information equals amortized communication complexity](https://arxiv.org/abs/2608.04141).

### 2. Superlogarithmic static cell-probe lower bounds

[TCS-6540](../../data/cards/TCS-6540.json) · reused · status: `source_open` · evidence: `reviewed`.

Strong static cell-probe lower bounds extend his data-structure complexity research.

**Status scope:** Primary sources and later-result searches checked on 11 September 2026 did not supply a resolution of the stated static specialization. The STOC 2026 paper retains the broader static barrier as Open Problem 1.1. The fixed near-linear space, short-query Boolean output and uniform polynomial-time family are an expressly recorded specialization; conditional proof barriers and bounds for dynamic memory or superpolynomial query sets do not resolve it.

Sources: [The Natural Proofs Barrier against Data-Structure Lower-Bounds](https://doi.org/10.1145/3798129.3800843); [Stronger Cell Probe Lower Bounds via Local PRGs](https://eccc.weizmann.ac.il/report/2025/030/); [Lower Bounds for Linear Operators](https://eccc.weizmann.ac.il/report/2025/155/); [Crossing the Logarithmic Barrier for Dynamic Boolean Data Structure Lower Bounds](https://epubs.siam.org/doi/10.1137/18M1198429); [An \(\Omega ((\log  n/\log  \log  n)^{2})\) Cell-Probe Lower Bound for Dynamic Boolean Data Structures](https://eccc.weizmann.ac.il/report/2026/047/).

## 153. Erik Waingarten

[Research bibliography](https://dblp.org/pid/146/0153.html).

### 1. Optimal \(\ell\)\(_{1}\) distortion of edit distance

[TCS-7297](../../data/cards/TCS-7297.json) · reused · status: `source_open` · evidence: `reviewed`.

L1 embeddings of edit distance connect his distance estimation and sketching research.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Low Distortion Embeddings for Edit Distance](https://doi.org/10.1145/1060590.1060623).

### 2. Optimal input-sparsity subspace embeddings

[TCS-7006](../../data/cards/TCS-7006.json) · reused · status: `source_open` · evidence: `source`.

Optimal subspace embeddings concern his high-dimensional algorithmic work.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2015 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357).

## 154. Jelani Nelson

[Research bibliography](https://dblp.org/pid/68/3296.html).

### 1. Optimal deterministic restricted-isometry matrices

[TCS-6662](../../data/cards/TCS-6662.json) · reused · status: `source_open` · evidence: `reviewed`.

Deterministic RIP concerns the limits of dimensionality reduction and compressed sensing.

**Status scope:** Reviewed through 11 September 2026. No polynomial-time deterministic construction with the required uniform optimal row bound was found in the checked sources. Optimal randomized row counts, restricted parameter regimes and coherence guarantees are recorded as partial progress.

Sources: [Doubly transitive equiangular tight frames that contain regular simplices](https://www.sciencedirect.com/science/article/pii/S0024379525003143); [The road to deterministic matrices with the restricted isometry property](https://www.math.ucdavis.edu/~strohmer/courses/270/road_to_rip.pdf); [Explicit constructions of RIP matrices and related problems](https://arxiv.org/abs/1008.4535); [Satisfying the restricted isometry property with the optimal number of rows and slightly less randomness](https://arxiv.org/abs/2311.07889).

### 2. Optimal input-sparsity subspace embeddings

[TCS-7006](../../data/cards/TCS-7006.json) · reused · status: `source_open` · evidence: `source`.

Optimal sparse embeddings directly connect his sketching research.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2015 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357).

## 155. Kunal Talwar

[Research bibliography](https://dblp.org/pid/06/3696.html).

### 1. Polynomial-time private release of all marginals

[TCS-7236](../../data/cards/TCS-7236.json) · reused · status: `source_open` · evidence: `reviewed`.

Efficient private marginals connect his differential-privacy algorithms.

**Status scope:** No solution of the stated all-orders synopsis target was found through 11 September 2026. The explicit open-problem source is older; later-work searches are not an exhaustive review of every k-way, interactive or synthetic-data variant.

Sources: [The Complexity of Differential Privacy](https://projects.iq.harvard.edu/files/privacytools/files/complexityprivacy_1_01.pdf); [Faster Private Release of Marginals on Small Databases](https://arxiv.org/abs/1304.3754).

### 2. Optimal competitive ratio for convex body chasing

[TCS-6576](../../data/cards/TCS-6576.json) · reused · status: `source_open` · evidence: `source`.

Convex body chasing connects his online and metric-approximation work.

**Status scope:** Retained in the source-based research proposal dated 10 September 2026. No full resolution was found in that search; this is not a completed independent open-status review.

Sources: [Research reference · theory.epfl.ch](https://theory.epfl.ch/WinterSchool2025/slides/2025/Gupta_lec4-chasing.pdf).

## 156. Adam Smith

[Research bibliography](https://dblp.org/pid/04/5072.html).

### 1. Private PAC sample complexity from VC and Littlestone dimensions

[TCS-0506](../../data/cards/TCS-0506.json) · reused · status: `source_open` · evidence: `reviewed`.

Private PAC sample complexity concerns his statistical foundations of privacy.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?](https://proceedings.mlr.press/v336/nissim26a.html).

### 2. Computational versus statistical privacy in the curator model

[TCS-6825](../../data/cards/TCS-6825.json) · reused · status: `source_open` · evidence: `source`.

Computational versus statistical privacy is a foundational question related to his cryptographic privacy work.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2014 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [The Algorithmic Foundations of Differential Privacy](https://www.cis.upenn.edu/~aaroth/privacybook.html).

## 157. Kobbi Nissim

[Research bibliography](https://dblp.org/pid/65/801.html).

### 1. Polynomial-time private convex-hull point selection

[TCS-3312](../../data/cards/TCS-3312.json) · reused · status: `uncertain` · evidence: `index`.

Efficient private convex-hull selection connects his private geometric algorithms.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [How to Find a Point in the Convex Hull Privately](https://doi.org/10.4230/LIPIcs.SoCG.2020.52).

### 2. Private PAC sample complexity from VC and Littlestone dimensions

[TCS-0506](../../data/cards/TCS-0506.json) · reused · status: `source_open` · evidence: `reviewed`.

Dimension-based private sample complexity concerns the foundations of private learnability he studies.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?](https://proceedings.mlr.press/v336/nissim26a.html).

## 158. Salil Vadhan

[Research bibliography](https://dblp.org/pid/v/SPVadhan.html).

### 1. L versus BPL

[TCS-0026](../../data/cards/TCS-0026.json) · reused · status: `source_open` · evidence: `reviewed`.

Space-bounded derandomization is a central target in his pseudorandomness work.

**Status scope:** Checked through 11 September 2026, including the latest displayed ECCC revision of the 2026 weighted-PRG paper. No deterministic logarithmic-space simulation of all BPL languages was found.

Sources: [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf); [Better Pseudodistributions and Derandomization for Space-Bounded Computation](https://drops.dagstuhl.de/storage/00lipics/lipics-vol207-approx-random2021/LIPIcs.APPROX-RANDOM.2021.28/LIPIcs.APPROX-RANDOM.2021.28.pdf); [Improved Error Reduction for Weighted PRGs](https://eccc.weizmann.ac.il/report/2026/064/).

### 2. Private PAC sample complexity from VC and Littlestone dimensions

[TCS-0506](../../data/cards/TCS-0506.json) · reused · status: `source_open` · evidence: `reviewed`.

Private PAC complexity connects his learning and privacy research.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?](https://proceedings.mlr.press/v336/nissim26a.html).

## 159. Omer Reingold

[Research bibliography](https://dblp.org/pid/r/OmerReingold.html).

### 1. L versus BPL

[TCS-0026](../../data/cards/TCS-0026.json) · reused · status: `source_open` · evidence: `reviewed`.

BPL versus L is a main derandomization frontier beyond undirected connectivity.

**Status scope:** Checked through 11 September 2026, including the latest displayed ECCC revision of the 2026 weighted-PRG paper. No deterministic logarithmic-space simulation of all BPL languages was found.

Sources: [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf); [Better Pseudodistributions and Derandomization for Space-Bounded Computation](https://drops.dagstuhl.de/storage/00lipics/lipics-vol207-approx-random2021/LIPIcs.APPROX-RANDOM.2021.28/LIPIcs.APPROX-RANDOM.2021.28.pdf); [Improved Error Reduction for Weighted PRGs](https://eccc.weizmann.ac.il/report/2026/064/).

### 2. Optimal explicit pseudorandom generators for read-once branching programs

[TCS-6600](../../data/cards/TCS-6600.json) · reused · status: `source_open` · evidence: `reviewed`.

Optimal space-bounded generators connect his pseudorandomness program.

**Status scope:** Checked through 10 September 2026. ECCC TR26-064 revision 3 explicitly retains the optimal general PRG target and the log-squared barrier. Its new generator is weighted; the July TR26-123 result is restricted to permutation programs. This card requires one ordinary, program-independent distribution family and optimal seed length as well as optimal work space.

Sources: [Pseudorandom generators for space-bounded computation](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf); [Better Pseudodistributions and Derandomization for Space-Bounded Computation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2021.28); [Hitting Sets Give Two-Sided Derandomization of Small Space](https://theoryofcomputing.org/articles/v018a021/); [Weighted Pseudorandom Generators for Read-Once Branching Programs via Weighted Pseudorandom Reductions](https://epubs.siam.org/doi/10.1137/1.9781611978971.124); [Improved Error Reduction for Weighted PRGs](https://eccc.weizmann.ac.il/report/2026/064/); [A Forward-Backward Weight Analysis of INW for Permutation Branching Programs](https://eccc.weizmann.ac.il/report/2026/123/).

## 160. Assaf Naor

[Research bibliography](https://dblp.org/pid/n/AssafNaor.html).

### 1. Real Grothendieck constant

[TCS-7352](../../data/cards/TCS-7352.json) · added · status: `source_open` · evidence: `reviewed`.

He coauthored the breakthrough on Krivine's bound and studies its metric and algorithmic consequences.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [The Grothendieck constant is strictly smaller than Krivine’s bound](https://arxiv.org/abs/1103.6161); [New Lower and Upper Bounds for the Grothendieck Constant](https://arxiv.org/abs/2608.11158).

### 2. Gupta–Newman–Rabinovich–Sinclair conjecture

[TCS-6525](../../data/cards/TCS-6525.json) · reused · status: `source_open` · evidence: `reviewed`.

GNRS is a central target in his metric-embedding research.

**Status scope:** The planar constant-distortion case remains explicitly open in the checked May 2026 notes. Restricted-family and face-cover results, including February 2026 exact values for \(K_{2},_{n}\), do not settle arbitrary fixed-minor-free metrics. The inherited fixed-treewidth approximation theorem uses a stronger relaxation and expressly does not prove a flow–cut-gap bound. No general settlement found through 11 September 2026.

Sources: [Cuts, Trees and \(\ell\)\(_{1}\)-Embeddings of Graphs](https://people.eecs.berkeley.edu/~sinclair/cuts.pdf); [Pathwidth, trees, and random embeddings](https://arxiv.org/abs/0910.1409); [Approximating Sparsest Cut in Graphs of Bounded Treewidth](https://www.wisdom.weizmann.ac.il/~robi/papers/CKR-TreewidthSparsestCut-APPROX10.pdf); [A face cover perspective to \(\ell\)\(_{1}\) embeddings of planar graphs](https://arxiv.org/abs/1903.02758); [The exact value of \(c_{1}(K_{2},_{n})\)](https://arxiv.org/abs/2602.23745); [CS 583: Approximation Algorithms](https://courses.grainger.illinois.edu/CS583/sp2026/approx-algorithms-lecture-notes.pdf).

## 161. Éva Tardos

[Research bibliography](https://dblp.org/pid/t/EvaTardos.html).

### 1. Constant-factor universally truthful auctions for submodular bidders

[TCS-6632](../../data/cards/TCS-6632.json) · reused · status: `source_open` · evidence: `reviewed`.

Truthful welfare approximation connects her algorithmic mechanism-design work.

**Status scope:** The checked primary literature retains a gap between constant nontruthful welfare approximation and the general universally truthful guarantee. Theorem 2 of the SODA 2021 paper supplies \(O((\log  \log  m)^{2})\) for submodular bidders. The 2026 graph-auction results impose eligibility restrictions. No general constant-factor resolution found through 11 September 2026. The public per-value precision parameter makes the inherited polynomial-communication question explicit in bits.

Sources: [Improved Truthful Mechanisms for Combinatorial Auctions with Submodular Bidders](https://epubs.siam.org/doi/10.1137/20M1316068); [On the Power of Randomization in Algorithmic Mechanism Design](https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf); [An Impossibility Result for Truthful Combinatorial Auctions with Submodular Valuations](https://arxiv.org/abs/1011.1830); [Improved Truthful Mechanisms for Subadditive Combinatorial Auctions: Breaking the Logarithmic Barrier](https://arxiv.org/abs/2010.01420); [The Communication Complexity of Combinatorial Auctions in Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.27).

### 2. Minimax rate of sequential binary calibration

[TCS-7319](../../data/cards/TCS-7319.json) · reused · status: `source_open` · evidence: `reviewed`.

Sequential calibration concerns learning and forecasting in repeated games, a major theme in her field.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. Ordinary calibration is distinct from multicalibration and from simultaneous regret bounds for all proper scoring rules. The source’s finite forecast-set convention is preserved.

Sources: [Breaking the \(T^{2/3}\) Barrier for Sequential Calibration](https://arxiv.org/abs/2406.13668).

## 162. Robert Kleinberg

[Research bibliography](https://dblp.org/pid/k/RDKleinberg.html).

### 1. Matroid secretary conjecture

[TCS-7316](../../data/cards/TCS-7316.json) · reused · status: `source_open` · evidence: `reviewed`.

Matroid secretary directly connects his online selection and mechanism-design work.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. No polynomial-time restriction has been silently appended. Earlier exclusions TCS-2570 and TCS-5552 address narrower algorithm/model questions.

Sources: [Constant-Competitiveness for Random Assignment Matroid Secretary Without Knowing the Matroid](https://arxiv.org/abs/2305.05353).

### 2. Instance-optimal finite-time best-arm identification

[TCS-6838](../../data/cards/TCS-6838.json) · reused · status: `source_open` · evidence: `source`.

Instance-optimal best-arm identification concerns his bandit and sequential-decision research.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2020 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Bandit Algorithms](https://banditalgs.com/).

## 163. S. Matthew Weinberg

[Research bibliography](https://dblp.org/pid/52/2474.html).

### 1. Constant-factor universally truthful auctions for submodular bidders

[TCS-6632](../../data/cards/TCS-6632.json) · reused · status: `source_open` · evidence: `reviewed`.

Truthful welfare approximation relates directly to his auction-design program.

**Status scope:** The checked primary literature retains a gap between constant nontruthful welfare approximation and the general universally truthful guarantee. Theorem 2 of the SODA 2021 paper supplies \(O((\log  \log  m)^{2})\) for submodular bidders. The 2026 graph-auction results impose eligibility restrictions. No general constant-factor resolution found through 11 September 2026. The public per-value precision parameter makes the inherited polynomial-communication question explicit in bits.

Sources: [Improved Truthful Mechanisms for Combinatorial Auctions with Submodular Bidders](https://epubs.siam.org/doi/10.1137/20M1316068); [On the Power of Randomization in Algorithmic Mechanism Design](https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf); [An Impossibility Result for Truthful Combinatorial Auctions with Submodular Valuations](https://arxiv.org/abs/1011.1830); [Improved Truthful Mechanisms for Subadditive Combinatorial Auctions: Breaking the Logarithmic Barrier](https://arxiv.org/abs/2010.01420); [The Communication Complexity of Combinatorial Auctions in Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.27).

### 2. Algorithmic versus dominant-strategy implementation

[TCS-6958](../../data/cards/TCS-6958.json) · reused · status: `source_open` · evidence: `source`.

Algorithmic versus incentive-compatible implementation concerns his reductions in mechanism design.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2007 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Algorithmic Game Theory](https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf).

## 164. Yang Cai

[Research bibliography](https://dblp.org/pid/14/5359-1.html).

### 1. Constant-factor universally truthful auctions for submodular bidders

[TCS-6632](../../data/cards/TCS-6632.json) · reused · status: `source_open` · evidence: `reviewed`.

Truthful submodular auctions concern the computational mechanism-design barriers he studies.

**Status scope:** The checked primary literature retains a gap between constant nontruthful welfare approximation and the general universally truthful guarantee. Theorem 2 of the SODA 2021 paper supplies \(O((\log  \log  m)^{2})\) for submodular bidders. The 2026 graph-auction results impose eligibility restrictions. No general constant-factor resolution found through 11 September 2026. The public per-value precision parameter makes the inherited polynomial-communication question explicit in bits.

Sources: [Improved Truthful Mechanisms for Combinatorial Auctions with Submodular Bidders](https://epubs.siam.org/doi/10.1137/20M1316068); [On the Power of Randomization in Algorithmic Mechanism Design](https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf); [An Impossibility Result for Truthful Combinatorial Auctions with Submodular Valuations](https://arxiv.org/abs/1011.1830); [Improved Truthful Mechanisms for Subadditive Combinatorial Auctions: Breaking the Logarithmic Barrier](https://arxiv.org/abs/2010.01420); [The Communication Complexity of Combinatorial Auctions in Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.27).

### 2. Algorithmic versus dominant-strategy implementation

[TCS-6958](../../data/cards/TCS-6958.json) · reused · status: `source_open` · evidence: `source`.

Implementing algorithms truthfully connects his mechanism-reduction research.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2007 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Algorithmic Game Theory](https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf).

## 165. Michal Feldman

[Research bibliography](https://dblp.org/pid/43/1464.html).

### 1. Existence of complete EFX allocations for additive valuations

[TCS-0011](../../data/cards/TCS-0011.json) · reused · status: `open` · evidence: `reviewed`.

Complete EFX connects her fair-division and algorithmic economics work.

**Status scope:** Checked through 11 September 2026. No proof or counterexample for unrestricted nonnegative additive valuations was located. The August 2026 four-agent, at-most-nine-goods preprint is a restricted positive result; the 2026 submodular counterexamples fall outside the additive model. The computational certificate corpus for the small-instance theorem was not rerun.

Sources: [Problem 3: Does EFX always exist?](https://tcsopenproblems.com/problem/3); [Fair Division of Indivisible Goods: A Survey](https://arxiv.org/abs/2202.07551); [EFX Exists for Three Agents](https://arxiv.org/abs/2002.05119); [Almost Full EFX Exists for Four Agents](https://ojs.aaai.org/index.php/AAAI/article/view/20410); [Complete EFX Allocations Exist for Four Additive Agents and Up to Nine Goods](https://arxiv.org/abs/2608.08590v1); [Counterexamples to EFX for Submodular and Subadditive Valuations](https://arxiv.org/abs/2605.06451).

### 2. Constant-factor universally truthful auctions for submodular bidders

[TCS-6632](../../data/cards/TCS-6632.json) · reused · status: `source_open` · evidence: `reviewed`.

Truthful welfare approximation concerns her auction research.

**Status scope:** The checked primary literature retains a gap between constant nontruthful welfare approximation and the general universally truthful guarantee. Theorem 2 of the SODA 2021 paper supplies \(O((\log  \log  m)^{2})\) for submodular bidders. The 2026 graph-auction results impose eligibility restrictions. No general constant-factor resolution found through 11 September 2026. The public per-value precision parameter makes the inherited polynomial-communication question explicit in bits.

Sources: [Improved Truthful Mechanisms for Combinatorial Auctions with Submodular Bidders](https://epubs.siam.org/doi/10.1137/20M1316068); [On the Power of Randomization in Algorithmic Mechanism Design](https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf); [An Impossibility Result for Truthful Combinatorial Auctions with Submodular Valuations](https://arxiv.org/abs/1011.1830); [Improved Truthful Mechanisms for Subadditive Combinatorial Auctions: Breaking the Logarithmic Barrier](https://arxiv.org/abs/2010.01420); [The Communication Complexity of Combinatorial Auctions in Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.27).

## 166. Shuchi Chawla

[Research bibliography](https://dblp.org/pid/c/ShuchiChawla.html).

### 1. Constant-factor universally truthful auctions for submodular bidders

[TCS-6632](../../data/cards/TCS-6632.json) · reused · status: `source_open` · evidence: `reviewed`.

Truthful submodular welfare approximation connects her auction and mechanism-design work.

**Status scope:** The checked primary literature retains a gap between constant nontruthful welfare approximation and the general universally truthful guarantee. Theorem 2 of the SODA 2021 paper supplies \(O((\log  \log  m)^{2})\) for submodular bidders. The 2026 graph-auction results impose eligibility restrictions. No general constant-factor resolution found through 11 September 2026. The public per-value precision parameter makes the inherited polynomial-communication question explicit in bits.

Sources: [Improved Truthful Mechanisms for Combinatorial Auctions with Submodular Bidders](https://epubs.siam.org/doi/10.1137/20M1316068); [On the Power of Randomization in Algorithmic Mechanism Design](https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf); [An Impossibility Result for Truthful Combinatorial Auctions with Submodular Valuations](https://arxiv.org/abs/1011.1830); [Improved Truthful Mechanisms for Subadditive Combinatorial Auctions: Breaking the Logarithmic Barrier](https://arxiv.org/abs/2010.01420); [The Communication Complexity of Combinatorial Auctions in Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.27).

### 2. Randomized truthful unrelated-machine scheduling

[TCS-6674](../../data/cards/TCS-6674.json) · reused · status: `source_open` · evidence: `reviewed`.

Randomized truthful scheduling is a central approximation-mechanism frontier in her area.

**Status scope:** The Nisan–Ronen proof, now published in JACM in February 2026, resolves only deterministic truthful mechanisms. Its randomized discussion records \(2- 1/m\) and \((m+5)/2\) bounds. Searches through 11 September 2026 found no matching unrestricted randomized bounds; results for task-independent mechanisms, fractional objectives, Bayesian types or no-payment models do not resolve this formulation.

Sources: [A proof of the Nisan–Ronen conjecture](https://arxiv.org/abs/2301.11905); [A Proof of the Nisan–Ronen Conjecture](https://doi.org/10.1145/3785408); [Setting Lower Bounds on Truthfulness](https://arxiv.org/abs/1507.08708); [Randomized Truthful Mechanisms for Scheduling Unrelated Machines](https://link.springer.com/chapter/10.1007/978-3-540-92185-1_46); [An Improved Randomized Truthful Mechanism for Scheduling Unrelated Machines](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2008.1314); [New Bounds for Truthful Scheduling on Two Unrelated Selfish Machines](https://link.springer.com/article/10.1007/s00224-019-09927-x); [A proof of the Nisan–Ronen conjecture — Oxford repository copy](https://ora.ox.ac.uk/objects/uuid%3A814fc511-99e2-47cb-b06a-f472630996dc/files/r9593tw016).

## 167. Shahar Dobzinski

[Research bibliography](https://dblp.org/pid/34/917.html).

### 1. Constant-factor universally truthful auctions for submodular bidders

[TCS-6632](../../data/cards/TCS-6632.json) · reused · status: `source_open` · evidence: `reviewed`.

Universally truthful submodular auctions directly concern his mechanism lower bounds.

**Status scope:** The checked primary literature retains a gap between constant nontruthful welfare approximation and the general universally truthful guarantee. Theorem 2 of the SODA 2021 paper supplies \(O((\log  \log  m)^{2})\) for submodular bidders. The 2026 graph-auction results impose eligibility restrictions. No general constant-factor resolution found through 11 September 2026. The public per-value precision parameter makes the inherited polynomial-communication question explicit in bits.

Sources: [Improved Truthful Mechanisms for Combinatorial Auctions with Submodular Bidders](https://epubs.siam.org/doi/10.1137/20M1316068); [On the Power of Randomization in Algorithmic Mechanism Design](https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf); [An Impossibility Result for Truthful Combinatorial Auctions with Submodular Valuations](https://arxiv.org/abs/1011.1830); [Improved Truthful Mechanisms for Subadditive Combinatorial Auctions: Breaking the Logarithmic Barrier](https://arxiv.org/abs/2010.01420); [The Communication Complexity of Combinatorial Auctions in Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.27).

### 2. Characterizing domains restricted to affine maximizers

[TCS-6957](../../data/cards/TCS-6957.json) · reused · status: `source_open` · evidence: `source`.

Affine-maximizer domain characterization connects his structural mechanism-design work.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2007 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Algorithmic Game Theory](https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf).

## 168. Vitaly Feldman

[Research bibliography](https://dblp.org/pid/67/1162.html).

### 1. Private PAC sample complexity from VC and Littlestone dimensions

[TCS-0506](../../data/cards/TCS-0506.json) · reused · status: `source_open` · evidence: `reviewed`.

Private learning sample complexity connects his statistical-query and privacy work.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?](https://proceedings.mlr.press/v336/nissim26a.html).

### 2. Learning decision trees from uniform random examples in polynomial time

[TCS-7294](../../data/cards/TCS-7294.json) · reused · status: `source_open` · evidence: `reviewed`.

Uniform decision-tree learning concerns his computational learning-theory program.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists.

Sources: [Decision trees are PAC-learnable from most product distributions: a smoothed analysis](https://arxiv.org/abs/0812.0933); [Backdoor Defense, Learnability and Obfuscation](https://doi.org/10.4230/LIPIcs.ITCS.2025.38).

## 169. Shay Moran

[Research bibliography](https://dblp.org/pid/119/5111.html).

### 1. Linear-size sample compression

[TCS-6541](../../data/cards/TCS-6541.json) · reused · status: `source_open` · evidence: `reviewed`.

Linear sample compression is central to his combinatorial learning theory.

**Status scope:** Checked through 10 September 2026. The general linear bound remains open in the primary sources checked. The 2026 graph-ball theorems concern structured classes. The claimed breakthrough at arXiv:2603.23561 is withdrawn and is included only to document its status. This card fixes labeled, possibly improper, unordered-subset compression with all side bits counted.

Sources: [Sample compression schemes for VC classes](https://arxiv.org/abs/1503.06960v2); [Dual VC Dimension Obstructs Sample Compression by Embeddings](https://proceedings.mlr.press/v247/chase24a.html); [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html); [Sample compression schemes for balls in structurally sparse graphs](https://arxiv.org/abs/2604.02949v1); [The No-Clash Teaching Dimension is Bounded by VC Dimension [withdrawn]](https://arxiv.org/abs/2603.23561v4).

### 2. Multiclass sample compression from binary compression

[TCS-4792](../../data/cards/TCS-4792.json) · reused · status: `source_open` · evidence: `source`.

Multiclass compression connects his work on multiclass learnability and its dimensions.

**Status scope:** Question recorded in a source from 2025; subsequent results and present open status have not been individually checked.

Sources: [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html).

## 170. Gregory Valiant

[Research bibliography](https://dblp.org/pid/80/6006.html).

### 1. Polynomial-time learning of Gaussian mixtures

[TCS-5443](../../data/cards/TCS-5443.json) · reused · status: `uncertain` · evidence: `source`.

Gaussian-mixture learning concerns his algorithmic distribution-learning work.

**Status scope:** Question recorded in a source from 2024; subsequent results and present open status have not been individually checked.

Sources: [Mixtures of Gaussians are Privately Learnable with a Polynomial Number of Samples](https://proceedings.mlr.press/v237/afzali24a.html).

### 2. Tight Characterization of Instance-Optimal Identity Testing

[TCS-0672](../../data/cards/TCS-0672.json) · reused · status: `uncertain` · evidence: `index`.

Instance-optimal identity testing connects his sample-efficient statistical testing program.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [COLT / PMLR](https://proceedings.mlr.press/v247/canonne24a.html).

## 171. Gautam Kamath

[Research bibliography](https://dblp.org/pid/73/11140.html).

### 1. Private PAC sample complexity from VC and Littlestone dimensions

[TCS-0506](../../data/cards/TCS-0506.json) · reused · status: `source_open` · evidence: `reviewed`.

Optimal private learning complexity concerns his privacy and statistical-learning research.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?](https://proceedings.mlr.press/v336/nissim26a.html).

### 2. Polynomial-time learning of Gaussian mixtures

[TCS-5443](../../data/cards/TCS-5443.json) · reused · status: `uncertain` · evidence: `source`.

Efficient Gaussian-mixture learning connects his distribution-learning program.

**Status scope:** Question recorded in a source from 2024; subsequent results and present open status have not been individually checked.

Sources: [Mixtures of Gaussians are Privately Learnable with a Polynomial Number of Samples](https://proceedings.mlr.press/v237/afzali24a.html).

## 172. Jerry Li

[Research bibliography](https://dblp.org/pid/162/8838.html).

### 1. Polynomial-time robust spectral estimation

[TCS-5087](../../data/cards/TCS-5087.json) · reused · status: `source_open` · evidence: `source`.

Robust spectral estimation directly concerns his robust high-dimensional inference work.

**Status scope:** Question recorded in a source from 2021; subsequent results and present open status have not been individually checked.

Sources: [Adversarially Robust Low Dimensional Representations](https://proceedings.mlr.press/v134/awasthi21a.html).

### 2. Computational threshold for tensor PCA

[TCS-6657](../../data/cards/TCS-6657.json) · reused · status: `source_open` · evidence: `reviewed`.

Tensor PCA captures computational-statistical barriers in his provable inference research.

**Status scope:** The May 2026 low-degree paper retains the conjectured gap for unrestricted algorithms and distinguishes spherical from independent-coordinate priors. The 2024 power-iteration and October 2025 stochastic-gradient improvements concern particular methods and do not provide a fixed-power improvement below \(n^{k/4}\). No full resolution found through 11 September 2026. The card explicitly fixes a finite-precision bit model; restricted lower bounds in the standard unrounded model are evidence, not a proof for all algorithms here.

Sources: [A statistical model for tensor PCA](https://arxiv.org/abs/1411.1076); [Sharp analysis of power iteration for tensor PCA](https://www.jmlr.org/papers/v25/24-0006.html); [Tensor cumulants for statistical inference on invariant distributions](https://arxiv.org/abs/2404.18735); [Near-Optimal Tensor PCA via Normalized Stochastic Gradient Ascent with Overparameterization](https://arxiv.org/abs/2510.14329); [Low-degree estimation thresholds in planted hypergraphs and tensor PCA](https://arxiv.org/abs/2605.30113).

## 173. Clément Canonne

[Research bibliography](https://dblp.org/pid/28/9840L.html).

### 1. Tight Characterization of Instance-Optimal Identity Testing

[TCS-0672](../../data/cards/TCS-0672.json) · reused · status: `uncertain` · evidence: `index`.

Instance-optimal identity testing directly concerns his distribution-testing research.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [COLT / PMLR](https://proceedings.mlr.press/v247/canonne24a.html).

### 2. Equivalence Testing with Conditional Samples

[TCS-0841](../../data/cards/TCS-0841.json) · reused · status: `uncertain` · evidence: `index`.

Conditional-sampling equivalence testing connects his work on stronger testing access models.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:87).

## 174. Ronitt Rubinfeld

[Research bibliography](https://dblp.org/pid/r/RonittRubinfeld.html).

### 1. Effective classification of polynomially testable hereditary graph properties

[TCS-6630](../../data/cards/TCS-6630.json) · reused · status: `source_open` · evidence: `reviewed`.

Efficient testing of hereditary graph properties concerns her foundational property-testing work.

**Status scope:** Reviewed through 11 September 2026. The source’s finite-family structural classification remains incomplete in the checked literature. This card explicitly asks its effective decidability version. The August 2026 container theorem does not provide the required terminating classifier.

Sources: [Polynomial Property Testing](https://arxiv.org/html/2508.16878v1); [A Characterization of the (Natural) Graph Properties Testable with One-Sided Error](https://epubs.siam.org/doi/10.1137/06064888X); [Removal Lemmas with Polynomial Bounds](https://arxiv.org/abs/1611.10315); [Easily Testable Graph Properties](https://www.cambridge.org/core/product/identifier/S0963548314000765/type/journal_article); [Efficient Removal without Efficient Regularity](https://arxiv.org/abs/1709.08159); [A Quantitative Container Characterization of One-Sided Testability](https://eccc.weizmann.ac.il/report/2026/144/).

### 2. Sublinear testing of bounded-degree graph isomorphism

[TCS-6672](../../data/cards/TCS-6672.json) · reused · status: `source_open` · evidence: `source`.

Bounded-degree isomorphism testing connects her sublinear graph-algorithm research.

**Status scope:** Retained in the source-based research proposal dated 10 September 2026. The source asks for the full query complexity and gives an \(n^{2/3}\) lower bound up to logarithmic factors for two unknown graphs. The first decisive target here is any truly sublinear tester.

Sources: [Open Problems in Testing Graph Properties — Oded Goldreich](https://eccc.weizmann.ac.il/report/2021/088/).

## 175. Dana Ron

[Research bibliography](https://dblp.org/pid/85/4800.html).

### 1. Effective classification of polynomially testable hereditary graph properties

[TCS-6630](../../data/cards/TCS-6630.json) · reused · status: `source_open` · evidence: `reviewed`.

Hereditary graph testability is a central structural question in her testing area.

**Status scope:** Reviewed through 11 September 2026. The source’s finite-family structural classification remains incomplete in the checked literature. This card explicitly asks its effective decidability version. The August 2026 container theorem does not provide the required terminating classifier.

Sources: [Polynomial Property Testing](https://arxiv.org/html/2508.16878v1); [A Characterization of the (Natural) Graph Properties Testable with One-Sided Error](https://epubs.siam.org/doi/10.1137/06064888X); [Removal Lemmas with Polynomial Bounds](https://arxiv.org/abs/1611.10315); [Easily Testable Graph Properties](https://www.cambridge.org/core/product/identifier/S0963548314000765/type/journal_article); [Efficient Removal without Efficient Regularity](https://arxiv.org/abs/1709.08159); [A Quantitative Container Characterization of One-Sided Testability](https://eccc.weizmann.ac.il/report/2026/144/).

### 2. Optimal query cost of reducing testing adaptivity

[TCS-4259](../../data/cards/TCS-4259.json) · reused · status: `source_open` · evidence: `reviewed`.

Adaptivity reduction concerns the power of different property-testing models she studies.

**Status scope:** The source’s general round-reduction question is unresolved in the checked text; its known one-round bound does not determine the newly explicit full extremal tradeoff. This user-authorized editorial development was reviewed on 13 September 2026. The saved later-source check is bounded and does not certify exhaustive current status.

Sources: [An Adaptivity Hierarchy Theorem for Property Testing](https://doi.org/10.4230/LIPIcs.CCC.2017.27); [An adaptivity hierarchy theorem for property testing — journal publication](https://doi.org/10.1007/s00037-018-0168-4); [An adaptivity hierarchy theorem for property testing — institutional attachment](https://www.repository.cam.ac.uk/items/73b70279-d662-43f0-b591-98afd3ce529c).

## 176. Maria-Florina Balcan

[Research bibliography](https://dblp.org/pid/b/MariaFlorinaBalcan.html).

### 1. Characterizing adversarially robust PAC learnability

[TCS-5153](../../data/cards/TCS-5153.json) · reused · status: `source_open` · evidence: `source`.

Robust PAC characterization connects her learning-theory and adversarial robustness work.

**Status scope:** Question recorded in a source from 2019; subsequent results and present open status have not been individually checked.

Sources: [VC Classes are Adversarially Robustly Learnable, but Only Improperly](https://proceedings.mlr.press/v99/montasser19a.html).

### 2. Constant-factor approximation for Dasgupta’s hierarchical clustering objective

[TCS-7318](../../data/cards/TCS-7318.json) · reused · status: `source_open` · evidence: `reviewed`.

Hierarchical-clustering approximation concerns her algorithmic clustering research.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. The question is the unrestricted graph objective. No data stability or external clustering oracle is assumed.

Sources: [A cost function for similarity-based hierarchical clustering](https://arxiv.org/abs/1510.05043); [Approximate Hierarchical Clustering via Sparsest Cut and Spreading Metrics](https://arxiv.org/abs/1609.09548).

## 177. Nika Haghtalab

[Research bibliography](https://dblp.org/pid/149/1265.html).

### 1. Minimax rate of sequential binary calibration

[TCS-7319](../../data/cards/TCS-7319.json) · reused · status: `source_open` · evidence: `reviewed`.

Calibration connects her online-learning and algorithmic decision-making work.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. Ordinary calibration is distinct from multicalibration and from simultaneous regret bounds for all proper scoring rules. The source’s finite forecast-set convention is preserved.

Sources: [Breaking the \(T^{2/3}\) Barrier for Sequential Calibration](https://arxiv.org/abs/2406.13668).

### 2. Characterizing adversarially robust PAC learnability

[TCS-5153](../../data/cards/TCS-5153.json) · reused · status: `source_open` · evidence: `source`.

Robust learnability concerns her research on learning under adversarial behavior.

**Status scope:** Question recorded in a source from 2019; subsequent results and present open status have not been individually checked.

Sources: [VC Classes are Adversarially Robustly Learnable, but Only Improperly](https://proceedings.mlr.press/v99/montasser19a.html).

## 178. Elad Hazan

[Research bibliography](https://dblp.org/pid/72/739.html).

### 1. Minimax dimension dependence in bandit convex optimization

[TCS-6577](../../data/cards/TCS-6577.json) · reused · status: `open` · evidence: `reviewed`.

Bandit convex dimension dependence is central to his online convex optimization research.

**Status scope:** The March 2026 primary book explicitly lists the minimax dimension dependence as open. Searches through 11 September 2026 found no established matching rate for the specified unrestricted one-point model. Recent smooth-loss and two-point results do not settle it.

Sources: [Bandit Convex Optimisation](https://tor-lattimore.com/downloads/cvx-book/cvx.pdf); [Bandit Convex Optimisation, Chapter 14: Outlook](https://www.cambridge.org/core/books/abs/bandit-convex-optimisation/outlook/FAEE9479EE720E949F7CECDADCE307D5); [Improved Regret for Zeroth-Order Adversarial Bandit Convex Optimisation](https://arxiv.org/abs/2006.00475v3); [Logarithmic High-Probability Regret for Online Convex Optimization with Two-Point Bandit Feedback](https://arxiv.org/abs/2603.25029v4); [Adversarial Bandit Optimization with Globally Bounded Perturbations to Convex Losses](https://arxiv.org/abs/2606.19891v2).

### 2. Optimal competitive ratio for convex body chasing

[TCS-6576](../../data/cards/TCS-6576.json) · reused · status: `source_open` · evidence: `source`.

Convex body chasing connects his online convex and geometric optimization work.

**Status scope:** Retained in the source-based research proposal dated 10 September 2026. No full resolution was found in that search; this is not a completed independent open-status review.

Sources: [Research reference · theory.epfl.ch](https://theory.epfl.ch/WinterSchool2025/slides/2025/Gupta_lec4-chasing.pdf).

## 179. Rong Ge

[Research bibliography](https://dblp.org/pid/89/6869-1.html).

### 1. Computational threshold for tensor PCA

[TCS-6657](../../data/cards/TCS-6657.json) · reused · status: `source_open` · evidence: `reviewed`.

Tensor PCA is a canonical computational barrier in his nonconvex inference research.

**Status scope:** The May 2026 low-degree paper retains the conjectured gap for unrestricted algorithms and distinguishes spherical from independent-coordinate priors. The 2024 power-iteration and October 2025 stochastic-gradient improvements concern particular methods and do not provide a fixed-power improvement below \(n^{k/4}\). No full resolution found through 11 September 2026. The card explicitly fixes a finite-precision bit model; restricted lower bounds in the standard unrounded model are evidence, not a proof for all algorithms here.

Sources: [A statistical model for tensor PCA](https://arxiv.org/abs/1411.1076); [Sharp analysis of power iteration for tensor PCA](https://www.jmlr.org/papers/v25/24-0006.html); [Tensor cumulants for statistical inference on invariant distributions](https://arxiv.org/abs/2404.18735); [Near-Optimal Tensor PCA via Normalized Stochastic Gradient Ascent with Overparameterization](https://arxiv.org/abs/2510.14329); [Low-degree estimation thresholds in planted hypergraphs and tensor PCA](https://arxiv.org/abs/2605.30113).

### 2. Efficient learning of well-separated Gaussian mixtures

[TCS-3391](../../data/cards/TCS-3391.json) · reused · status: `uncertain` · evidence: `index`.

Gaussian-mixture learning connects his provable nonconvex and latent-variable algorithms.

**Status scope:** Imported from the previous catalogue. Current open status has not been established by a new review.

Sources: [The EM Algorithm gives Sample-Optimality for Learning Mixtures of Well-Separated Gaussians](https://proceedings.mlr.press/v125/kwon20a.html).

## 180. Tengyu Ma

[Research bibliography](https://dblp.org/pid/54/9061.html).

### 1. Computational threshold for tensor PCA

[TCS-6657](../../data/cards/TCS-6657.json) · reused · status: `source_open` · evidence: `reviewed`.

Tensor PCA relates to his provable nonconvex inference and learning research.

**Status scope:** The May 2026 low-degree paper retains the conjectured gap for unrestricted algorithms and distinguishes spherical from independent-coordinate priors. The 2024 power-iteration and October 2025 stochastic-gradient improvements concern particular methods and do not provide a fixed-power improvement below \(n^{k/4}\). No full resolution found through 11 September 2026. The card explicitly fixes a finite-precision bit model; restricted lower bounds in the standard unrounded model are evidence, not a proof for all algorithms here.

Sources: [A statistical model for tensor PCA](https://arxiv.org/abs/1411.1076); [Sharp analysis of power iteration for tensor PCA](https://www.jmlr.org/papers/v25/24-0006.html); [Tensor cumulants for statistical inference on invariant distributions](https://arxiv.org/abs/2404.18735); [Near-Optimal Tensor PCA via Normalized Stochastic Gradient Ascent with Overparameterization](https://arxiv.org/abs/2510.14329); [Low-degree estimation thresholds in planted hypergraphs and tensor PCA](https://arxiv.org/abs/2605.30113).

### 2. Distribution-free improper learning of two unrestricted halfspaces

[TCS-7293](../../data/cards/TCS-7293.json) · reused · status: `source_open` · evidence: `reviewed`.

Learning two halfspaces is a canonical small-network learning problem related to his neural-network theory.

**Status scope:** The 2026 TheoretiCS source explicitly retains the fixed-two-halfspace polynomial-time question. A July 2026 subexponential-time preprint does not establish the requested polynomial bound. Checked through 13 September 2026 within a bounded literature review.

Sources: [The Intersection of Two Halfspaces Has High Threshold Degree](https://web.cs.ucla.edu/~sherstov/pdf/hshs.pdf); [Improved Hardness Results for Learning Intersections of Halfspaces](https://theoretics.episciences.org/18105); [Learning Functions of Halfspaces](https://arxiv.org/abs/2603.08700v2).

## 181. Zeyuan Allen-Zhu

[Research bibliography](https://dblp.org/pid/10/7536.html).

### 1. Exact semidefinite feasibility in polynomial time

[TCS-6574](../../data/cards/TCS-6574.json) · reused · status: `source_open` · evidence: `reviewed`.

Exact SDP feasibility concerns the computational foundations of his optimization work.

**Status scope:** Checked through 10 September 2026. The primary literature retains general exact SDP feasibility as an open polynomial-time problem. Ramana’s dual does not establish \(\mathrm{NP}\cap \mathrm{coNP}\) membership in the Turing model, and recent convex-polynomial optimization results address a different constraint family. This card permits real witnesses, singular feasible points, weak infeasibility and unbounded feasible regions.

Sources: [An exact duality theory for semidefinite programming and its complexity implications](https://link.springer.com/article/10.1007/BF02614433); [On the Turing Model Complexity of Interior Point Methods for Semidefinite Programming](https://epubs.siam.org/doi/10.1137/15M103114X); [Exact algorithms for semidefinite programs with degenerate feasible set](https://www.sciencedirect.com/science/article/pii/S0747717120301176); [How Do Exponential Size Solutions Arise in Semidefinite Programming?](https://epubs.siam.org/doi/10.1137/21M1434945); [A combinatorial approach to Ramana’s exact dual for semidefinite programming](https://arxiv.org/abs/2510.07271); [Hesse’s Redemption: Efficient Convex Polynomial Programming](https://arxiv.org/abs/2511.03440).

### 2. Computational threshold for tensor PCA

[TCS-6657](../../data/cards/TCS-6657.json) · reused · status: `source_open` · evidence: `reviewed`.

Tensor PCA connects his nonconvex optimization and provable-learning research.

**Status scope:** The May 2026 low-degree paper retains the conjectured gap for unrestricted algorithms and distinguishes spherical from independent-coordinate priors. The 2024 power-iteration and October 2025 stochastic-gradient improvements concern particular methods and do not provide a fixed-power improvement below \(n^{k/4}\). No full resolution found through 11 September 2026. The card explicitly fixes a finite-precision bit model; restricted lower bounds in the standard unrounded model are evidence, not a proof for all algorithms here.

Sources: [A statistical model for tensor PCA](https://arxiv.org/abs/1411.1076); [Sharp analysis of power iteration for tensor PCA](https://www.jmlr.org/papers/v25/24-0006.html); [Tensor cumulants for statistical inference on invariant distributions](https://arxiv.org/abs/2404.18735); [Near-Optimal Tensor PCA via Normalized Stochastic Gradient Ascent with Overparameterization](https://arxiv.org/abs/2510.14329); [Low-degree estimation thresholds in planted hypergraphs and tensor PCA](https://arxiv.org/abs/2605.30113).

## 182. Aleksander Mądry

[Research bibliography](https://dblp.org/pid/67/2454.html).

### 1. Exact directed maximum flow in \(O((m+n) \operatorname{polylog} n)\) time

[TCS-7228](../../data/cards/TCS-7228.json) · reused · status: `source_open` · evidence: `reviewed`.

Near-linear exact max flow is a direct frontier of his flow-algorithm program.

**Status scope:** Primary-source check through 11 September 2026 found almost-linear bounds, not the fixed-polylogarithmic overhead required here. New preprint proofs were not independently verified.

Sources: [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://arxiv.org/abs/2203.00671); [Maximum Flow Without the Outer IPM](https://arxiv.org/abs/2608.17384).

### 2. Characterizing adversarially robust PAC learnability

[TCS-5153](../../data/cards/TCS-5153.json) · reused · status: `source_open` · evidence: `source`.

Robust PAC learnability connects the foundations of his adversarial-robustness work.

**Status scope:** Question recorded in a source from 2019; subsequent results and present open status have not been individually checked.

Sources: [VC Classes are Adversarially Robustly Learnable, but Only Improperly](https://proceedings.mlr.press/v99/montasser19a.html).

## 183. Eli Ben-Sasson

[Research bibliography](https://dblp.org/pid/02/476.html).

### 1. Linear-length locally testable codes and proofs

[TCS-6738](../../data/cards/TCS-6738.json) · reused · status: `source_open` · evidence: `source`.

Linear-length locally testable proofs connect his PCP, IOP and algebraic-proof work.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2017 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html).

### 2. Weak automatability of Resolution

[TCS-5332](../../data/cards/TCS-5332.json) · reused · status: `open` · evidence: `reviewed`.

Resolution automatability concerns his proof-complexity and automated-reasoning research.

**Status scope:** Read the complete original abstract, the full regular-Resolution definitions and weak-automatability corollary, the Atserias–Müller author-version main theorems, and the May 2026 full-paper weak-automatability discussion and definitions. Searches through 12 September 2026 found no resolution. The unary-budget promise formulation makes the original distinction precise; no strong-automatability hardness claim has been transferred to it.

Sources: [Proof Complexity and Its Relations to SAT Solving (Invited Talk)](https://doi.org/10.4230/LIPIcs.STACS.2025.1); [Regular resolution effectively simulates resolution](https://doi.org/10.1016/j.ipl.2024.106489); [Automating Resolution is NP-Hard](https://arxiv.org/abs/1904.02991); [The Proof Analysis Problem](https://arxiv.org/abs/2506.16956).

## 184. Yuval Ishai

[Research bibliography](https://dblp.org/pid/05/667.html).

### 1. One-way functions in \(\mathrm{NC}^{0}\) from one-way functions

[TCS-7274](../../data/cards/TCS-7274.json) · reused · status: `source_open` · evidence: `reviewed`.

NC0 one-way functions from arbitrary OWFs connect his local computation and randomized-encoding research.

**Status scope:** Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists. The original personal-list citation studied attacks on Goldreich’s candidate; the foundational locality-construction reference is used here instead.

Sources: [Cryptography in \(\mathrm{NC}^{0}\)](https://doi.org/10.1137/S0097539705446950).

### 2. Sublinear-communication secure computation with polynomial setup

[TCS-5013](../../data/cards/TCS-5013.json) · reused · status: `uncertain` · evidence: `source`.

Sublinear-communication MPC directly extends his communication-efficient cryptographic protocols.

**Status scope:** Question recorded in a source from 2023; subsequent results and present open status have not been individually checked.

Sources: [Exponential Correlated Randomness Is Necessary in Communication-Optimal Perfectly Secure Two-Party Computation](https://doi.org/10.4230/LIPIcs.ITC.2023.18).

## 185. Brent Waters

[Research bibliography](https://dblp.org/pid/w/BrentWaters.html).

### 1. Circuit obfuscation from polynomial-hard LWE

[TCS-6550](../../data/cards/TCS-6550.json) · reused · status: `source_open` · evidence: `reviewed`.

LWE-based iO continues his obfuscation constructions.

**Status scope:** Checked through 10 September 2026. No construction from the plain polynomial-hard decisional-LWE assumption fixed here was identified. Existing multi-assumption and circular-security constructions do not settle it. Polynomial hardness, polynomial modulus/noise ratio, classical adversaries, arbitrary circuits and no auxiliary leakage are explicit choices that make the broad LWE-alone question unambiguous.

Sources: [On the \((Im)\)possibility of Obfuscating Programs](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html); [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); [Indistinguishability Obfuscation from Well-Founded Assumptions](https://doi.org/10.1145/3785007); [Indistinguishability Obfuscation from LPN over \(F_{p}\), DLIN, and PRGs in \(\mathrm{NC}^{0}\)](https://eprint.iacr.org/2021/1334); [Factoring and Pairings Are Not Necessary for IO: Circular-Secure LWE Suffices](https://doi.org/10.4230/LIPIcs.ICALP.2022.28).

### 2. Identity-based encryption from arbitrary public-key encryption

[TCS-7278](../../data/cards/TCS-7278.json) · reused · status: `source_open` · evidence: `reviewed`.

IBE from generic PKE directly concerns the encryption primitive he helped develop.

**Status scope:** The primary 2021 source supplies a generic-group barrier and does not refute the unrestricted implication. Formulation and barrier scope were checked on 13 September 2026; the bounded saved later-work review did not identify a general resolution. The foundational security definition uses the earlier recorded read.

Sources: [Generic-Group Identity-Based Encryption: A Tight Impossibility Result](https://eprint.iacr.org/2021/745.pdf); [Identity-Based Encryption from the Weil Pairing](https://crypto.stanford.edu/~dabo/pubs/papers/bfibe.pdf).

## 186. Craig Gentry

[Research bibliography](https://dblp.org/pid/28/2376.html).

### 1. Unleveled fully homomorphic encryption from LWE alone

[TCS-6551](../../data/cards/TCS-6551.json) · reused · status: `source_open` · evidence: `reviewed`.

Unbounded-depth FHE from LWE alone is a central frontier after his FHE breakthrough.

**Status scope:** No classical unleveled compact FHE construction from the specified ordinary LWE assumption alone was found through 11 September 2026. Functional-encryption constructions use additional assumptions. The inspected February and April 2026 no-circularity proposals retain explicit level bounds; the latter also uses quantum evaluation. This card fixes polynomial-modulus LWE, nonuniform classical security and fresh-input FHE correctness.

Sources: [Efficient Fully Homomorphic Encryption from (Standard) LWE](https://epubs.siam.org/doi/10.1137/120868669); [Quantum FHE (Almost) As Secure As Classical](https://www.iacr.org/archive/crypto2018/10993383/10993383.pdf); [Fully Homomorphic Encryption: definitional issues and open problems](https://cseweb.ucsd.edu/classes/wi23/cse208-a/FHEorg.pdf); [Bootstrapping Homomorphic Encryption via Functional Encryption](https://eprint.iacr.org/2023/1376.pdf); [Bootstrapping Homomorphic Encryption via Functional Encryption — conference version](https://drops.dagstuhl.de/storage/00lipics/lipics-vol251-itcs2023/LIPIcs.ITCS.2023.17/LIPIcs.ITCS.2023.17.pdf); [Dynamic multi-key FHE without CRS from LWE](https://link.springer.com/article/10.1186/s42400-025-00431-z); [Efficient Quantum Fully Homomorphic Encryption](https://arxiv.org/abs/2604.23490).

### 2. Fully homomorphic encryption from public-key encryption

[TCS-7277](../../data/cards/TCS-7277.json) · reused · status: `source_open` · evidence: `reviewed`.

FHE from generic PKE concerns the minimal assumptions needed for his encryption paradigm.

**Status scope:** The primary source proves a restricted black-box separation, not impossibility of arbitrary constructions. The later functional-encryption implication requires an additional premise. These scopes were checked on 13 September 2026; the bounded status review found no resolution of the stated general implication.

Sources: [On the Power of Hierarchical Identity-Based Encryption](https://eprint.iacr.org/2015/815.pdf); [Lecture 15: Fully Homomorphic Encryption](https://mit6875.github.io/LECNOTES/lec15.pdf); [Bootstrapping Homomorphic Encryption via Functional Encryption](https://doi.org/10.4230/LIPIcs.ITCS.2023.17).

## 187. Moni Naor

[Research bibliography](https://dblp.org/pid/n/MoniNaor.html).

### 1. Collision-resistant hashing from one-way functions

[TCS-6547](../../data/cards/TCS-6547.json) · reused · status: `source_open` · evidence: `reviewed`.

Collision resistance from OWFs concerns his foundational cryptographic reductions.

**Status scope:** No unrestricted implication or refutation was found in the primary literature checked through 11 September 2026. Existing black-box separations do not settle this ordinary-model existence statement. The definitions explicitly use uniform honest algorithms, nonuniform classical adversaries, public fresh keys and factor-two compression.

Sources: [One-Way Functions are Necessary and Sufficient for Secure Signatures](https://www.cs.princeton.edu/courses/archive/spr08/cos598D/Rompel.pdf); [Finding collisions on a one-way street: Can secure hash functions be based on general assumptions?](https://link.springer.com/chapter/10.1007/BFb0054137); [Cryptographic Hashing From Strong One-Way Functions: Or: One-Way Product Functions and their Applications](https://ieee-focs.org/FOCS-2018-Papers/pdfs/59f850.pdf); [One-Way Functions vs. TFNP: Simpler and Improved](https://eprint.iacr.org/2023/945); [Doubly-Efficient Interactive Arguments for Bounded-Space from One-Way Functions](https://eccc.weizmann.ac.il/report/2026/111/).

### 2. One-way permutations from one-way functions

[TCS-6546](../../data/cards/TCS-6546.json) · reused · status: `source_open` · evidence: `reviewed`.

One-way permutations from arbitrary OWFs concern the foundational primitive reductions he studies.

**Status scope:** No derivation from ordinary one-way functions alone, or refutation of the unrestricted existence implication, was found through 11 September 2026. The 2025 full-domain trapdoor construction requires subexponential iO and OWF assumptions. Existing oracle and black-box barriers do not settle the unrestricted question. This card explicitly fixes the full-domain keyed convention.

Sources: [Limits on the Provable Consequences of One-way Functions](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1988/6060.html); [A Pseudorandom Generator from any One-way Function](https://epubs.siam.org/doi/10.1137/S0097539793244708); [On Black-Box Separations among Injective One-Way Functions](https://link.springer.com/chapter/10.1007/978-3-642-19571-6_36); [On Constructing One-Way Permutations from Indistinguishability Obfuscation](https://eprint.iacr.org/2015/752.pdf); [On One-Shot Signatures, Quantum vs Classical Binding, and Obfuscating Permutations](https://arxiv.org/abs/2507.12456).

## 188. Ran Canetti

[Research bibliography](https://dblp.org/pid/c/RanCanetti.html).

### 1. Chosen-ciphertext security from ordinary public-key encryption

[TCS-6548](../../data/cards/TCS-6548.json) · reused · status: `source_open` · evidence: `reviewed`.

CCA encryption from arbitrary PKE concerns his cryptographic security and composition work.

**Status scope:** No construction from ordinary CPA-secure public-key encryption alone in the plain model, or refutation of that unrestricted implication, was found through 11 September 2026. Bounded-CCA results and constructions with injective trapdoor functions, hinting PRGs, batch arguments or random oracles leave this target open.

Sources: [CS 276 — Projects](https://theory.stanford.edu/~trevisan/cs276/projects.html); [Towards a Separation of Semantic and CCA Security for Public Key Encryption](https://www.iacr.org/archive/tcc2007/43920433/43920433.pdf); [Black-Box Construction of a Non-malleable Encryption Scheme from Any Semantically Secure One](https://www.cs.columbia.edu/~dglasner/MyPapers/non-mal.pdf); [Realizing Chosen Ciphertext Security Generically in Attribute-Based Encryption and Predicate Encryption](https://www.iacr.org/archive/crypto2019/116940363/116940363.pdf); [Chosen Ciphertext Security from Injective Trapdoor Functions](https://par.nsf.gov/servlets/purl/10295635); [Chosen Ciphertext Security via BARGs](https://eprint.iacr.org/2023/1957); [Threshold Public-Key Encryption: Definitions, Relations, and CPA-to-CCA Transforms](https://eprint.iacr.org/2025/1665).

### 2. Oblivious transfer from public-key encryption

[TCS-6549](../../data/cards/TCS-6549.json) · reused · status: `source_open` · evidence: `reviewed`.

OT from PKE is a central foundation-of-secure-computation question in his research area.

**Status scope:** Checked through 10 September 2026. No unrestricted classical implication from arbitrary IND-CPA public-key encryption to OT was identified. Known oracle/black-box separations and positive results for rerandomizable or suitably samplable encryption do not settle this formulation. The card fixes semi-honest standalone security with classical communication and no setup.

Sources: [The Relationship between Public Key Encryption and Oblivious Transfer](https://vmahesh.cs.illinois.edu/papers/focs00.pdf); [Black-Box Constructions of Protocols for Secure Computation](https://iftachh.github.io/MyHomepage/papers/BlackBoxMPC/black-box-mpc.pdf); [Computational Hardness of Optimal FairComputation: Beyond Minicrypt](https://eprint.iacr.org/2021/882); [Oblivious Transfer from Rerandomizable PKE](https://eprint.iacr.org/2023/1002); [On the Implications from Updatable Encryption to Public-Key Cryptographic Primitives](https://doi.org/10.1587/transfun.2025CIP0019).

## 189. Rafael Pass

[Research bibliography](https://dblp.org/pid/p/RPass.html).

### 1. One-way functions from \(\mathrm{P} \ne  \mathrm{NP}\)

[TCS-0022](../../data/cards/TCS-0022.json) · reused · status: `source_open` · evidence: `reviewed`.

OWFs from worst-case NP hardness connects his work on the foundations of cryptography.

**Status scope:** Explicitly open in the original source. Primary literature was checked through 10 September 2026; no derivation of eventually secure classical one-way functions from \(\mathrm{P}\ne \mathrm{NP}\) alone was located. The security quantifiers are stronger than an infinitely-often one-wayness target.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3); [A Pseudorandom Generator from any One-way Function](https://johanhastad.se/prgfromowf.pdf); [On Worst-Case to Average-Case Reductions for NP Problems](https://lucatrevisan.github.io/pubs/BT03.pdf); [One-Way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://doi.org/10.4230/LIPIcs.ITCS.2026.97).

### 2. Average-case NP hardness from \(\mathrm{P} \ne  \mathrm{NP}\)

[TCS-0012](../../data/cards/TCS-0012.json) · reused · status: `source_open` · evidence: `reviewed`.

Worst-case to average-case NP hardness concerns his meta-complexity-to-cryptography program.

**Status scope:** The original question is explicitly open in Wigderson’s book and the revised average-case survey. Current primary literature was checked through 10 September 2026; no resolution from \(\mathrm{P}\ne \mathrm{NP}\) alone was located. The card fixes deterministic exact AvgP and strict polynomial-time sampling, rather than conflating them with randomized heuristic hardness.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3); [On Worst-Case to Average-Case Reductions for NP Problems](https://lucatrevisan.github.io/pubs/BT03.pdf); [One-Way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://doi.org/10.4230/LIPIcs.ITCS.2026.97).

## 190. Aayush Jain

[Research bibliography](https://dblp.org/pid/126/6084.html).

### 1. Circuit obfuscation from polynomial-hard LWE

[TCS-6550](../../data/cards/TCS-6550.json) · reused · status: `source_open` · evidence: `reviewed`.

Basing iO on polynomial-hardness LWE continues his obfuscation breakthroughs.

**Status scope:** Checked through 10 September 2026. No construction from the plain polynomial-hard decisional-LWE assumption fixed here was identified. Existing multi-assumption and circular-security constructions do not settle it. Polynomial hardness, polynomial modulus/noise ratio, classical adversaries, arbitrary circuits and no auxiliary leakage are explicit choices that make the broad LWE-alone question unambiguous.

Sources: [On the \((Im)\)possibility of Obfuscating Programs](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html); [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf); [Indistinguishability Obfuscation from Well-Founded Assumptions](https://doi.org/10.1145/3785007); [Indistinguishability Obfuscation from LPN over \(F_{p}\), DLIN, and PRGs in \(\mathrm{NC}^{0}\)](https://eprint.iacr.org/2021/1334); [Factoring and Pairings Are Not Necessary for IO: Circular-Secure LWE Suffices](https://doi.org/10.4230/LIPIcs.ICALP.2022.28).

### 2. Identity-based encryption from arbitrary public-key encryption

[TCS-7278](../../data/cards/TCS-7278.json) · reused · status: `source_open` · evidence: `reviewed`.

IBE from generic PKE concerns reducing assumptions for the encryption tools in his field.

**Status scope:** The primary 2021 source supplies a generic-group barrier and does not refute the unrestricted implication. Formulation and barrier scope were checked on 13 September 2026; the bounded saved later-work review did not identify a general resolution. The foundational security definition uses the earlier recorded read.

Sources: [Generic-Group Identity-Based Encryption: A Tight Impossibility Result](https://eprint.iacr.org/2021/745.pdf); [Identity-Based Encryption from the Weil Pairing](https://crypto.stanford.edu/~dabo/pubs/papers/bfibe.pdf).

## 191. Guy Rothblum

[Research bibliography](https://dblp.org/pid/00/6232.html).

### 1. Noninteractive zero knowledge from one-way functions

[TCS-6552](../../data/cards/TCS-6552.json) · reused · status: `source_open` · evidence: `reviewed`.

NIZK from minimal assumptions concerns his verification and cryptographic-proof work.

**Status scope:** No construction of reusable adaptive NIZK arguments from ordinary OWFs alone, or refutation of that unrestricted implication, was found through 11 September 2026. The cited BARG, trapdoor-hash and derandomization constructions retain extra assumptions; recent OWF-only succinct proofs are interactive, and high-error characterizations run in the reverse direction.

Sources: [Commitment Schemes and Zero-Knowledge Protocols (2011)](https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf); [Noninteractive Zero Knowledge for NP from (Plain) Learning With Errors](https://web.eecs.umich.edu/~cpeikert/pubs/nizk-lwe.pdf); [Batch Arguments to NIZKs from One-Way Functions](https://eprint.iacr.org/2023/1938); [Black-Box Non-Interactive Zero Knowledge from Vector Trapdoor Hash](https://eprint.iacr.org/2024/1514); [Fiat-Shamir in the Plain Model from Derandomization (Or: Do Efficient Algorithms Believe that \(\mathrm{NP} = \mathrm{PSPACE}\)?)](https://eccc.weizmann.ac.il/report/2024/116/); [Non-Trivial Zero-Knowledge Implies One-Way Functions](https://arxiv.org/abs/2602.17651); [Succinct Zero-Knowledge Proofs from One-Way Functions: The Blackbox Way](https://doi.org/10.1007/978-3-032-35424-2_6).

### 2. Polynomial-time private release of all marginals

[TCS-7236](../../data/cards/TCS-7236.json) · reused · status: `source_open` · evidence: `reviewed`.

Efficient private query release connects his private-learning and data-analysis research.

**Status scope:** No solution of the stated all-orders synopsis target was found through 11 September 2026. The explicit open-problem source is older; later-work searches are not an exhaustive review of every k-way, interactive or synthetic-data variant.

Sources: [The Complexity of Differential Privacy](https://projects.iq.harvard.edu/files/privacytools/files/complexityprivacy_1_01.pdf); [Faster Private Release of Marginals on Small Databases](https://arxiv.org/abs/1304.3754).

## 192. John Wright

[Research bibliography](https://dblp.org/pid/10/3047-4.html).

### 1. Quantum PCP conjecture

[TCS-6446](../../data/cards/TCS-6446.json) · reused · status: `source_open` · evidence: `reviewed`.

Quantum PCP connects his quantum-complexity and multiprover-proof work.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495); [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/).

### 2. QMA versus QCMA

[TCS-6448](../../data/cards/TCS-6448.json) · reused · status: `source_open` · evidence: `reviewed`.

The relative power of classical and quantum witnesses concerns his quantum-complexity research.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [Separating Quantum and Classical Advice with Good Codes](https://eccc.weizmann.ac.il/report/2026/020/).

## 193. Zhengfeng Ji

[Research bibliography](https://dblp.org/pid/30/2575.html).

### 1. Quantum PCP conjecture

[TCS-6446](../../data/cards/TCS-6446.json) · reused · status: `source_open` · evidence: `reviewed`.

Quantum PCP is a central Hamiltonian-complexity target related to his work.

**Status scope:** Literature checked on 10 September 2026; dates and review scope are recorded below.

Sources: [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495); [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/).

### 2. QMA versus \(\mathrm{QMA}_{1}\)

[TCS-4737](../../data/cards/TCS-4737.json) · reused · status: `uncertain` · evidence: `source`.

Perfect completeness in QMA connects his quantum verification and proof-complexity work.

**Status scope:** Question recorded in a source from 2026; subsequent results and present open status have not been individually checked.

Sources: [Towards a Universal Gateset for QMA1](https://doi.org/10.4230/LIPIcs.MFCS.2026.98).

## 194. Shi Li

[Research bibliography](https://dblp.org/pid/31/4501-1.html).

### 1. Optimal polynomial-time approximation ratio for metric k-means

[TCS-7354](../../data/cards/TCS-7354.json) · added · status: `source_open` · evidence: `reviewed`.

Optimal metric clustering approximation directly extends his clustering research.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654).

### 2. Optimal polynomial-time approximation ratio for metric k-Median

[TCS-6659](../../data/cards/TCS-6659.json) · reused · status: `source_open` · evidence: `reviewed`.

The metric k-median ratio is a central frontier after his approximation improvements.

**Status scope:** Reviewed through 11 September 2026. The checked general-metric result remains \(2+\varepsilon\) with a strict budget, while the classical hardness threshold is \(1+2/e\). The FPT algorithm, Euclidean schemes and 2026 k-Means results do not settle the polynomial-time target here. The 12 September 2026 edit adopts absolute 0.01 benchmark acceptance; the saved open-status evidence concerns the underlying exact question and does not independently certify openness at that tolerance.

Sources: [A \((2+\varepsilon )\)-Approximation Algorithm for Metric k-Median](https://people.idsia.ch/~grandoni/Pubblicazioni/CGLSS25stoc.pdf); [A threshold of ln n for approximating set cover](https://disco.ethz.ch/alumni/pascalv/refs/ds_1998_feige.pdf); [A new greedy approach for facility location problems](https://cgi.di.uoa.gr/~vassilis/co/co-papers/jain02.pdf); [Tight FPT Approximations for k-Median and k-Means](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.42); [Almost-Optimal Upper and Lower Bounds for Clustering in Low Dimensional Euclidean Spaces](https://arxiv.org/abs/2603.09846); [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654).

## 195. Nitin Saxena

[Research bibliography](https://dblp.org/pid/86/6915.html).

### 1. Derandomizing polynomial identity testing

[TCS-7113](../../data/cards/TCS-7113.json) · reused · status: `source_open` · evidence: `source`.

Deterministic PIT is a direct focus of his algebraic-complexity research.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2021 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042).

### 2. Superpolynomial arithmetic formula lower bounds

[TCS-6888](../../data/cards/TCS-6888.json) · reused · status: `source_open` · evidence: `source`.

General arithmetic formula lower bounds connect his arithmetic-circuit program.

**Status scope:** Recorded as a question, conjecture or research direction in the cited 2010 source version. Present open status has not been checked; the import date is not an open-status review.

Sources: [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf).

## 196. Nisheeth Vishnoi

[Research bibliography](https://dblp.org/pid/02/2229.html).

### 1. Fully polynomial randomized approximation of mixed discriminants

[TCS-7355](../../data/cards/TCS-7355.json) · added · status: `source_open` · evidence: `reviewed`.

Mixed-discriminant approximation directly concerns his work on constrained determinantal sampling.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [A polynomial time algorithm to approximate the mixed volume within a simply exponential factor](https://eccc.weizmann.ac.il/report/2007/037/revision/1/); [On the Complexity of Constrained Determinantal Point Processes](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2017.36).

### 2. Kannan–Lovász–Simonovits conjecture

[TCS-6523](../../data/cards/TCS-6523.json) · reused · status: `source_open` · evidence: `reviewed`.

KLS connects his convex-geometric sampling and optimization research.

**Status scope:** The full KLS conjecture is explicitly open in the primary sources, including Letwin’s July 2026 preprint. Research through 10 September 2026 found no dimension-free general-function resolution. The recent quadratic-form and thin-shell results are not treated as proofs of the full conjecture; the July bound is labeled as a preprint result.

Sources: [The KLS Conjecture (problem 30)](https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/); [The Kannan–Lovász–Simonovits Conjecture](https://faculty.cc.gatech.edu/~vempala/papers/kls_survey.pdf); [Bourgain’s slicing problem and KLS isoperimetry up to polylog](https://arxiv.org/abs/2203.15551); [Logarithmic bounds for isoperimetry and slices of convex sets](https://www.weizmann.ac.il/math/klartag/sites/math.klartag/files/uploads/root_log.pdf); [Thin-shell bounds via parallel coupling](https://arxiv.org/abs/2507.15495v2); [The KLS constant is \(O(\log ^{1/4} n)\)](https://arxiv.org/abs/2607.24164v1).

## 197. Niv Buchbinder

[Research bibliography](https://dblp.org/pid/48/4123.html).

### 1. Optimal approximation for submodular maximization over a matroid

[TCS-5407](../../data/cards/TCS-5407.json) · reused · status: `uncertain` · evidence: `source`.

Optimal submodular maximization is central to his approximation research.

**Status scope:** Question recorded in a source from 2022; subsequent results and present open status have not been individually checked.

Sources: [On Maximizing Sums of Non-Monotone Submodular and Linear Functions](https://doi.org/10.4230/LIPIcs.ISAAC.2022.41).

### 2. Matroid secretary conjecture

[TCS-7316](../../data/cards/TCS-7316.json) · reused · status: `source_open` · evidence: `reviewed`.

Matroid secretary connects his online and stochastic submodular optimization work.

**Status scope:** Open target supported by the dated sources. Literature was checked on 11 September 2026, with the limits recorded here; this is not an exhaustive certification of current openness. No polynomial-time restriction has been silently appended. Earlier exclusions TCS-2570 and TCS-5552 address narrower algorithm/model questions.

Sources: [Constant-Competitiveness for Random Assignment Matroid Secretary Without Knowing the Matroid](https://arxiv.org/abs/2305.05353).

## 198. Václav Rozhoň

[Research bibliography](https://dblp.org/pid/204/8692.html).

### 1. Deterministic LOCAL MIS in \(O(\log  n)\) rounds

[TCS-6506](../../data/cards/TCS-6506.json) · reused · status: `open` · evidence: `reviewed`.

Deterministic logarithmic-round MIS continues his distributed derandomization work.

**Status scope:** Reviewed 10 September 2026. Polylogarithmic deterministic MIS is solved; the \(O(\log  n)\) target remains open in the checked literature.

Sources: [Near-Optimal Deterministic Network Decomposition and Ruling Set, and Improved MIS](https://arxiv.org/abs/2410.19516); [Lower Bounds for Maximal Matchings and Maximal Independent Sets](https://arxiv.org/abs/1901.02441); [Polylogarithmic-Time Deterministic Network Decomposition and Distributed Derandomization](https://arxiv.org/abs/1907.10937); [Faster Distributed \(\Delta\)-Coloring via a Reduction to MIS](https://doi.org/10.1137/1.9781611978971.162).

### 2. Distributed Lovász Local Lemma in \(O(\log  \log  n)\) rounds

[TCS-6554](../../data/cards/TCS-6554.json) · reused · status: `open` · evidence: `reviewed`.

Optimal distributed LLL connects his network-decomposition and derandomization program.

**Status scope:** The original conjecture, primary distributed bounds, the 2025 locality result and the August 2026 resilient-LLL paper were checked on 11 September 2026. No result settling the exact bounded-degree \(O(\log  \log  n)\) worst-case target was found. The fixed factor \(1/2\) and order of slack/degree quantifiers preserve the saved precise interpretation. Node averages and results for stronger communication models are not substituted for this guarantee.

Sources: [Sublogarithmic Distributed Algorithms for Lovász Local Lemma, and the Complexity Hierarchy](https://arxiv.org/abs/1705.04840); [On the Locality of the Lovász Local Lemma](https://arxiv.org/abs/2502.11690); [Improved Distributed Algorithms for the Lovász Local Lemma and Edge Coloring](https://arxiv.org/abs/2208.08701); [A Lower Bound for the Distributed Lovász Local Lemma](https://jukkasuomela.fi/lll-lb/); [Triangle-Free Coloring in LOCAL via Resilient Lovász Local Lemma](https://arxiv.org/abs/2608.13357).

## 199. Roei Tell

[Research bibliography](https://dblp.org/pid/143/2243.html).

### 1. P versus BPP

[TCS-0003](../../data/cards/TCS-0003.json) · reused · status: `uncertain` · evidence: `reviewed`.

Full polynomial-time derandomization is a central target of his research.

**Status scope:** \(\mathrm{P}=\mathrm{BPP}\) remains the target of mainstream derandomization work cited in May 2026. A July 2026 revision of a preprint claims separation; this review has not established its correctness or independent validation. The card is not marked resolved. Status search performed through 10 September 2026.

Sources: [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf); [\(\mathrm{P}=\mathrm{BPP}\) unless E has sub-exponential circuits: Derandomizing the XOR Lemma](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/IW97/proc.pdf); [Pseudorandomness Beating the Hybrid Argument for Insensitive Algorithms](https://eccc.weizmann.ac.il/report/2026/082/); [Probabilistic Computers (and Hence Quantum Computers) Are Rigorously More Powerful Than Classical Deterministic Computers, and Derandomization](https://arxiv.org/abs/2308.09549v9).

### 2. NEXP versus nonuniform \(\mathrm{TC}^{0}\)

[TCS-7161](../../data/cards/TCS-7161.json) · reused · status: `open` · evidence: `reviewed`.

NEXP versus TC0 connects his circuit lower bounds and derandomization work.

**Status scope:** No \(\mathrm{NEXP}\not\subset \mathrm{TC}^{0}\) resolution found through 11 September 2026. The checked March, July and September results retain different hard-language models or fixed depth and polynomial quantitative bounds. The September preprint has a source comment raising concerns and is recorded as an unverified claim.

Sources: [Non-Uniform ACC Circuit Lower Bounds](https://doi.org/10.1109/CCC.2011.36); [Wikipedia: Circuit complexity](https://en.wikipedia.org/wiki/Circuit_complexity); [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1328197464); [Non-Uniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-ccc.pdf); [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/); [Almost-Everywhere Near-Cubic Wire Lower Bounds for SYM ∘ THR and \(\mathrm{THR} \circ  \mathrm{THR}\)](https://eccc.weizmann.ac.il/report/2026/167/); [Near-Maximum Circuit Lower Bounds for Exponential Time with Merlin-Arthur Queries](https://eccc.weizmann.ac.il/report/2026/118/).

## 200. Vera Traub

[Research bibliography](https://dblp.org/pid/170/0126.html).

### 1. Optimal polynomial-time approximation ratio for asymmetric TSP

[TCS-7357](../../data/cards/TCS-7357.json) · added · status: `source_open` · evidence: `reviewed`.

Optimal ATSP approximation directly extends her improved ATSP algorithms.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [Better approximation guarantee for Asymmetric TSP](https://arxiv.org/abs/2603.14334).

### 2. Optimal polynomial-time approximation ratio for metric TSP

[TCS-7356](../../data/cards/TCS-7356.json) · added · status: `source_open` · evidence: `reviewed`.

Optimal metric TSP approximation continues her TSP and combinatorial optimization research.

**Status scope:** The cited primary sources and a targeted later-work search were checked on 13 September 2026. No resolution of this precise target was located. This is a bounded literature review, not an exhaustive certification of openness or an independent verification of the cited proofs.

Sources: [A (Slightly) Improved Approximation Algorithm for Metric TSP](https://arxiv.org/abs/2007.01409).
