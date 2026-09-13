# Author-based open-problem card proposals

Research date: 13 September 2026. Scope: 22 researchers, two recommendations each except three for Tomasz Kociumaka, giving 45 author–problem assignments and 32 distinct topics.

This is a research proposal, not an import into the published catalogue. The researcher associations below are editorial recommendations informed by publications; they do not imply that each researcher originated or endorsed the stated question. Existing cards should be enriched or reviewed instead of duplicated. An existing record is not itself evidence that a problem remains open.

The selection contains 14 topics represented in active Atlas records, 17 new candidate topics, and one replacement direction for an outdated tree-edit-distance record. “New” means no matching active topic was found in this repository, not newly posed in the literature. Targets explicitly identified as editorial strengthenings still need the normal model and formulation review before becoming benchmark cards. Recent preprint claims have not been independently proof-checked.

## Assignments

| Researcher | First recommendation | Second recommendation | Third recommendation |
| --- | --- | --- | --- |
| J. Ian Munro | P01: compact suffix-array access | P02: optimal packed-text index construction | |
| Gonzalo Navarro | P04: compact top-k document retrieval | P03: linear-space LZ77 random access | |
| Yakov Nekrich | P04: compact top-k document retrieval | P05: fully dynamic planar nearest neighbors | |
| Jean Cardinal | P06: NP versus the existential theory of the reals | P07: the 1/3–2/3 conjecture | |
| Moshe Lewenstein | P08: binary jumbled-index construction | P09: Strong SetDisjointness | |
| Ely Porat | P10: optimal 3SUM-indexing tradeoffs | P11: Hamming-distance oracles over general alphabets | |
| Micha Sharir | P12: planar k-sets | P13: Voronoi diagrams of lines in three dimensions | |
| Erik Demaine | P14: dynamic optimality | P15: Dürer’s conjecture | |
| Stefan Felsner | P07: the 1/3–2/3 conjecture | P16: universal point sets for planar graphs | |
| Tomasz Kociumaka | P17: almost-linear edit-distance approximation schemes | P18: optimal k-mismatch text indexing | P19: exact text-to-pattern Hamming distances |
| Jakub Radoszewski | P18: optimal k-mismatch text indexing | P20: elastic-degenerate string intersection | |
| Solon P. Pissis | P21: optimal gapped string indexing | P20: elastic-degenerate string intersection | |
| Shay Golan | P22: optimal minimizer density | P23: almost-linear constant-factor LCS approximation | |
| Paweł Gawrychowski | P24: exact distance labels for planar graphs | P25: linear-time LZ77 pattern matching | |
| Gad Landau | P26: linear-time unit-Monge multiplication | P17: almost-linear edit-distance approximation schemes | |
| Amihood Amir | P19: exact text-to-pattern Hamming distances | P08: binary jumbled-index construction | |
| Masayuki Takeda | P25: linear-time LZ77 pattern matching | P27: constant-factor smallest-grammar approximation | |
| Maxime Crochemore | P27: constant-factor smallest-grammar approximation | P28: a general 2-approximation for shortest common superstring | |
| Inge Li Gørtz | P21: optimal gapped string indexing | P29: the dense NFA Acceptance Hypothesis | |
| Philip Bille | P03: linear-space LZ77 random access | P30: near-quadratic unweighted tree edit distance | |
| Travis Gagie | P31: fully functional suffix trees in BWT-run-linear space | P27: constant-factor smallest-grammar approximation | |
| Esko Ukkonen | P28: a general 2-approximation for shortest common superstring | P32: breaking two for sum-of-pairs multiple sequence alignment | |

## Distinct candidate topics

### P01. Compact suffix-array access

**Suggested question.** Can a binary text of length n be represented in O(n) bits while supporting SA[i] queries in (log log n)^{O(1)} worst-case time on a deterministic word RAM with Θ(log n)-bit words? The text and every auxiliary structure count toward the space bound.

This asks how much navigation a representation of essentially text size can support. Munro’s connection is direct through compact text indexing, including [Munro–Navarro–Nekrich, CPM 2020](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2020.24).

**Status and route.** New candidate; high priority. The polyloglog target is an editorial threshold. [Thankachan, revised September 2026](https://arxiv.org/abs/2607.17287) explains why even log^{o(1)} n time at this space bound would be a substantial breakthrough. [Kempa–Kociumaka, August 2026](https://arxiv.org/abs/2608.19123) claim constant-time **inverse** suffix-array access and a nonconstant lower bound for SA access. These are different operations; do not nominate constant-time ISA as open.

### P02. Optimal construction of compact indexes from packed text

**Suggested question.** Given a packed binary text of length n, can an O(n)-bit index supporting constant-time inverse suffix-array queries be constructed deterministically in O(n/log n) time, including preprocessing, on a Θ(log n)-bit word RAM?

The target matches the number of input words. It separates the cost of constructing an index from the cost of querying one. Munro’s sublinear-construction work makes this a natural association.

**Status and route.** New candidate; an editorial strengthening requiring a final construction-model review. [Kempa–Kociumaka, August 2026](https://arxiv.org/abs/2608.19123) give O(n/√log n) construction for binary texts and connect improvements in relevant regimes to Dictionary Matching. Their result therefore does not attain the proposed input-size target. Use that specific target rather than an unquantified “faster compressed-index construction” program. The earlier [CPM 2020 paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2020.24) supplies Munro’s direct research connection.

### P03. Linear-space LZ77 random access

**Question.** Given an LZ77 parse with z phrases of a text of length N, can O(z) total words support deterministic character access in O(log N) worst-case time? Include the parse and all navigation information; permit overlapping copies, and do not keep the expanded text.

This is a basic test of whether a highly compressed representation remains usable without a logarithmic storage increase. Navarro’s [survey of repetitive-string algorithms](https://arxiv.org/abs/2004.02781) and Bille’s work on compressed-string access give strong topic associations; this is not an attribution of the conjecture to them.

**Status and route.** Already [TCS-0467](../../data/cards/TCS-0467.json). Gawrychowski explicitly poses the question in [Dagstuhl 25191, §5.4, May 2025](https://doi.org/10.4230/DagRep.15.5.1). [Boneh–Gawrychowski, July 2026](https://arxiv.org/abs/2607.14923) address LZ-End, whose phrase count differs from ordinary LZ77. Enrich the existing card, not a second copy.

### P04. Compact top-k document retrieval

**Suggested question.** For documents of total length n over alphabet size σ, can an O(n log σ)-bit index report the k documents with highest occurrence counts for a packed query pattern P, in O(1 + |P|/log_σ n + k) time? Document boundaries, identifiers and ranking ties must be encoded consistently in the final model.

This connects text indexing to ranked retrieval over document or genome collections. Both Navarro and Nekrich are direct coauthors.

**Status and route.** New candidate; high priority. Their [SODA 2025 paper and author abstract](https://users.dcc.uchile.cl/~gnavarro/abstracts/soda25.html) explicitly identify optimal retrieval near text-size space as open. The result uses a CSA plus O(n log log n) bits and largely matches the CSA’s own access costs. The constant-alphabet case makes the remaining space gap particularly meaningful. Keep compact bits distinct from O(n) words.

### P05. Fully dynamic planar nearest neighbors

**Question.** Can an exact Euclidean nearest-neighbor structure in the plane support insertions, deletions and queries in O(log n) time per operation? A useful first formulation permits expected amortized updates and worst-case queries with near-linear space.

This is the two-dimensional analogue of a basic search-tree interface. Nekrich’s connection is direct through dynamic geometric data structures.

**Status and route.** Review and develop [TCS-0387](../../data/cards/TCS-0387.json), whose current statement is only a topic label. The [original TOPP question](https://topp.openproblem.net/p63) records the logarithmic target. [Iacono–Nekrich, 2025](https://arxiv.org/abs/2504.07366) obtain optimal queries with near-logarithmic insertions in the incremental setting. Deletions and the complete logarithmic target remain essential distinctions. Do not quote the old TOPP partial-results list as the latest upper bounds.

### P06. NP versus the existential theory of the reals

**Question.** Is ∃R = NP, equivalently is feasibility of existential real polynomial systems in NP under the usual finite binary encoding?

This asks whether geometric existence problems always have efficiently checkable discrete certificates. It organizes the complexity of geometric representations, recognition and realization problems, making it a stronger general-algorithms choice for Cardinal than another narrowly specialized ∃R-completeness classification.

**Status and route.** New candidate; high priority outside string algorithms. Cardinal coauthors [The Existential Theory of the Reals as a Complexity Class: A Compendium](https://arxiv.org/abs/2407.18006). The known containment NP ⊆ ∃R ⊆ PSPACE does not establish either equality or strictness. [Meer–Wurm, 2025](https://arxiv.org/abs/2502.00680) study structural and relativized questions; their oracle results do not settle the unrelativized equality.

### P07. The 1/3–2/3 conjecture

**Question.** Does every finite partial order that is not a total order contain two incomparable elements x,y such that between one third and two thirds of its linear extensions place x before y?

A balanced comparison would reduce uncertainty by a constant factor when sorting under partial information. Felsner has a direct connection through [Balancing pairs and the cross product conjecture](https://trotter.math.gatech.edu/papers/97.pdf). Cardinal’s association is editorial, supported by his [sorting-under-partial-information work](https://arxiv.org/abs/0911.0086); the question is not attributed to him.

**Status and route.** Already [TCS-7177](../../data/cards/TCS-7177.json), including recent literature checks. General partial orders remain the target. Special-family results and verification on small posets do not settle it. The known efficient sorting algorithm is not itself an open problem.

### P08. Optimal construction of binary jumbled indexes

**Suggested question.** What is the optimal preprocessing time for an O(n)-word index of a binary text that answers, in O(1) time, whether a substring has prescribed numbers of zeroes and ones? In particular, is n^{1+o(1)} preprocessing possible?

Equivalently, compute the minimum and maximum number of ones over substrings of every length. The question captures order-insensitive pattern search and a basic convolution barrier. [Amir–Chan–Lewenstein–Lewenstein](https://arxiv.org/abs/1405.0189) provide direct author connections and distinguish alphabet regimes.

**Status and route.** New candidate. The almost-linear target is editorial. Truly subquadratic preprocessing is already known and must not be proposed as open. [Jin–Park–Saha–Xu, ICALP 2026](https://arxiv.org/abs/2605.07150) obtain deterministic n^{1.5+o(1)} monotone convolution and the corresponding binary-jumbled application. Do not transfer large-alphabet hardness to the binary case without a reduction.

### P09. Strong SetDisjointness

**Question.** For a family of sets of total size N, must every static data structure answering whether two named sets intersect satisfy S·T² = Ω̃(N²), where S is its space and T its query time?

This would give a general polynomial space–query-time barrier behind text indexes, geometric searching and database queries. Fix polynomial preprocessing and the classical word-RAM model in the card; randomized guarantees should be stated explicitly rather than left implicit.

**Status and route.** New candidate; high priority. Lewenstein and Porat are direct coauthors of [Conditional Lower Bounds for Space/Time Tradeoffs](https://arxiv.org/abs/1706.05847). This is the conjecture itself, not an unconditional theorem obtained by assuming it. It must also be distinguished from stronger old 3SUM-indexing conjectures that have been refuted. No resolution of this set-disjointness tradeoff was located in the dated search.

### P10. Optimal space–time tradeoffs for 3SUM-indexing

**Suggested question.** Preprocess two sets A,B of n word-sized integers to answer whether a query integer c belongs to A+B. Determine the optimal tradeoff between stored space and query time, allowing polynomial preprocessing and bounded-error randomization.

The problem connects reusable search information to additive structure, with consequences for string indexing. Porat’s direct connection includes [the space/time-tradeoff framework](https://arxiv.org/abs/1706.05847).

**Status and route.** New candidate; high priority, but the tradeoff should be the card’s numerical target, not “any improvement.” [Dinur–Golovnev, ICALP 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.78) improve the tradeoff in an intermediate space regime and also improve related string-indexing bounds. Their result follows earlier function-inversion improvements. Do not resurrect the false assertion that every sublinear query requires quadratic space.

### P11. Hamming-distance oracles over general alphabets

**Suggested question.** After preprocessing two strings of lengths n,m, support exact Hamming-distance queries between equal-length substrings. Determine the optimal preprocessing/query tradeoff for a polynomial-size alphabet. Can the Õ(nm/x) preprocessing, O(x) query regime available for constant alphabets be attained for general alphabets?

This isolates a reusable similarity-query primitive rather than recomputing each comparison. Porat is a coauthor of the final publication.

**Status and route.** New candidate; high priority. [Boneh–Fried–Golan–Kraus–Porat, CPM 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.1) give Õ(nm/√x) preprocessing for general alphabets. Their matching lower bound in the constant-alphabet regime is conditional and restricted to combinatorial algorithms; it does not settle the general-alphabet tradeoff. Approximate oracles are a separate result. Use the five-author final paper rather than the older four-author preprint for attribution.

### P12. Planar k-sets

**Question.** Determine, up to constant factors, the maximum number K₂(n,k) of k-element subsets of n planar points in general position that can be strictly separated from the other points by a line, uniformly over k ≤ n/2.

This is a central extremal obstacle in arrangements, levels and geometric selection algorithms. Sharir’s work on arrangement complexity makes the association direct and substantial.

**Status and route.** Already [TCS-0318](../../data/cards/TCS-0318.json). Its recent source review should be reused. The [TOPP k-sets entry](https://topp.openproblem.net/p7) provides the classical question. Improving the constants in a special halving-line bound does not determine the full extremal function; retain the full uniform target.

### P13. Voronoi diagrams of lines in three dimensions

**Suggested question.** Is the combinatorial complexity of the Euclidean Voronoi diagram of n lines in three-dimensional space O(n^{2+ε}) for every fixed ε > 0? The precise treatment of degeneracies should be fixed in the card.

The question measures the complexity of a fundamental proximity structure. Sharir’s envelope and union-complexity results are central to the known bounds.

**Status and route.** Review and develop [TCS-0417](../../data/cards/TCS-0417.json), currently a topic label. The [TOPP entry](https://topp.openproblem.net/p3) records the near-quadratic conjecture against a quadratic lower bound and essentially cubic upper bound, with primary references to Sharir. The dated search found no general resolution. Bounds for polyhedral metrics or a fixed level set do not establish the Euclidean diagram bound.

### P14. Dynamic optimality

**Question.** Is there an online binary-search-tree algorithm whose cost is within a universal constant factor of the optimal offline BST on every access sequence? The stronger splay-tree version asks this for splaying itself.

This asks whether a simple adaptive structure can compete with complete knowledge of future accesses. Demaine is a direct coauthor of [Dynamic Optimality—Almost](https://doi.org/10.1137/S0097539705447347).

**Status and route.** Already [TCS-6498](../../data/cards/TCS-6498.json), which uses the splay-specific formulation. Reuse that target rather than silently replacing it with the weaker existence question. [Chmel et al., July 2026](https://arxiv.org/abs/2607.18498) claim an approximately log-logarithmic competitive ratio for splay trees. Their preprint does not claim a constant ratio.

### P15. Dürer’s conjecture

**Question.** Can every convex polyhedron be cut along edges and unfolded into one connected planar net without overlapping face interiors?

This is a fundamental geometric construction question, with a direct connection to Demaine’s folding and unfolding research.

**Status and route.** Already [TCS-0406](../../data/cards/TCS-0406.json); the short record deserves a full statement. The [TOPP entry](https://topp.openproblem.net/p9) gives the exact edge-unfolding question and references Demaine’s related work. General cuts through faces, nonconvex polyhedra and disconnected unfoldings change the problem. No general resolution was located in the dated search.

### P16. Universal point sets for planar graphs

**Suggested question.** What is the smallest function u(n) such that one set of u(n) planar points supports a crossing-free straight-line drawing of every n-vertex planar graph? In particular, can u(n) be O(n)?

The point set must be chosen before the graph, while the assignment of vertices to points may depend on the graph. The question asks how much geometric space is needed to represent arbitrary planar combinatorics.

**Status and route.** Already [TCS-0377](../../data/cards/TCS-0377.json). Felsner coauthors [Universal Point Sets for Subclasses of Planar Graphs](https://arxiv.org/abs/2303.00109). Linear-size results for subclasses do not settle general planar graphs, where the broad linear-versus-quadratic gap remains. The [TOPP entry](https://topp.openproblem.net/p45) supplies the classical formulation.

### P17. Almost-linear edit-distance approximation schemes

**Question.** For every fixed ε > 0, can the edit distance of two explicit strings of total length n be approximated within 1+ε in randomized worst-case time n^{1+o(1)} with success probability at least 2/3?

This would make accurate sequence comparison scale almost as well as reading the sequences. Kociumaka’s modern sequence-comparison work and Landau’s foundational edit-distance algorithms give strong, but not exclusive, associations.

**Status and route.** Already [TCS-7235](../../data/cards/TCS-7235.json). [Andoni–Nosatzki, 2020](https://arxiv.org/abs/2005.07678) address constant-factor approximation. [Approximation Schemes for Edit Distance and LCS, STOC 2026](https://arxiv.org/abs/2603.29702) give n²/2^{log^{Ω(1)} n} time, which is far from the requested almost-linear bound. Neither a fixed constant approximation nor time n^{1+δ} for a fixed δ attains this target.

### P18. Optimal k-mismatch text indexing

**Suggested question.** For every fixed k ≥ 2, can an O(n)-word index report all occurrences of a query pattern P within Hamming distance k in O(|P| + log^{O(k)} n + occ) time? More generally, determine the optimal space–query-time tradeoff, including its dependence on k.

This is a core approximate-search problem relevant to read mapping and similar sequence-search tasks. Kociumaka and Radoszewski are direct coauthors of the newest source.

**Status and route.** New candidate; high priority. [Space-Efficient k-Mismatch Text Indexes, SODA 2026](https://arxiv.org/abs/2510.26264), §9, explicitly asks for further space and query improvements after improving the general space bound to O(n log^{k−1} n). The linear-space target is an editorial strengthening. It must not be confused with k=1, constant-alphabet improvements, or indexing under insertions and deletions.

### P19. Exact text-to-pattern Hamming distances

**Suggested question.** For a text of length n and a pattern of length m over a polynomial-size alphabet, what is the optimal time to compute the exact Hamming distance at every alignment? A major threshold is O(n m^{1/2−ε}) for some fixed ε > 0.

This is the basic all-alignments approximate-matching primitive, not an indexed-query or approximate-distance version. Amir’s classic k-mismatch work and Kociumaka’s later bounded-mismatch algorithms provide direct research connections.

**Status and route.** New candidate; high priority. [Chan–Jin–Vassilevska Williams–Xu, FOCS 2023, revised 2024](https://arxiv.org/abs/2310.13174) give O(n√m) Las Vegas time and relate exact matching to a range-restricted **counting** version of 3SUM. Their equivalence is not an unconditional matching lower bound or an equivalence to ordinary decision 3SUM. The exponent threshold above is editorial; deterministic log-factor removal would be a smaller question.

### P20. Optimal elastic-degenerate string intersection

**Question.** An elastic-degenerate string is a sequence of sets of alternative strings and represents all concatenations choosing one alternative per position. How fast can we decide whether two such representations share a string? In particular, can the Õ(n₂N₁^{ω−1} + n₁N₂^{ω−1}) upper bound be improved by a fixed polynomial factor in the N parameters?

Here nᵢ counts positions and Nᵢ is the total explicit length of alternatives. This is a concrete comparison primitive for pangenome representations. Both Pissis and Radoszewski are direct coauthors.

**Status and route.** New candidate. [Elastic-Degenerate String Comparison](https://arxiv.org/abs/2411.07782), §9, explicitly asks this question. General near-linear time would contradict the stated SETH barrier in appropriate regimes; the unresolved issue is the parameter-sensitive algorithmic frontier. The input must remain the explicit alternatives, since further compression changes the complexity. The exact proposed exponent and representation conventions need a final card review.

### P21. Optimal gapped string indexing

**Suggested question.** Preprocess a text T to answer queries consisting of two patterns P₁,P₂ and an interval [a,b], reporting occurrence pairs whose starting-position difference lies in that interval. Determine the optimal space–query-time tradeoff, including output cost.

This captures paired motifs and sequence features separated by variable-length gaps. Fix the gap convention explicitly; it differs by |P₁| from counting intervening characters. Pissis and Gørtz are direct coauthors of the principal source.

**Status and route.** New candidate; high priority. [Bille et al., STACS 2024](https://arxiv.org/abs/2211.16860) obtain simultaneous subquadratic space and sublinear query overhead and connect the problem to shifted set intersection and 3SUM-indexing. [Dinur–Golovnev, ICALP 2026](https://arxiv.org/abs/2512.04258) further improve related tradeoffs. The full frontier remains the proposed target; the first such subquadratic/sublinear index is already known. Fixed preprocessing gaps and consecutive-occurrence queries are different variants.

### P22. Optimal minimizer density

**Suggested question.** Determine tight bounds and efficient constructions for d*(σ,k,w), the minimum expected sampling density over total orders on k-mers, for a uniformly random infinite σ-ary sequence and a fixed leftmost tie rule. The most relevant alphabet is DNA, σ=4.

A minimizer selects the smallest k-mer in each window containing w consecutive k-mers. Lower density reduces stored seeds while retaining a seed in every window. Golan coauthors [GreedyMini, Bioinformatics 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12261476/).

**Status and route.** New candidate; strong biological relevance, but scope it carefully. [Shur, 2025](https://arxiv.org/abs/2506.05277) already gives an exact exponential algorithm and solves several small-parameter families. [Generating minimum-density minimizers, January 2026](https://doi.org/10.64898/2026.01.25.701585) develops exact generation further. The open proposal is a sharp general constructive theory and its complexity, not mere computability or “the first optimal minimizer.” Expected density over input strings is different from averaging over random minimizer orders.

### P23. Almost-linear constant-factor LCS approximation

**Question.** For strings of total length n over a polynomial-size alphabet, is there a randomized n^{1+o(1)}-time algorithm returning a common subsequence of length at least LCS/C for some universal constant C?

This would make similarity under deletions computationally accessible without losing an input-dependent factor. The alphabet must grow: a constant-alphabet constant approximation is trivial.

**Status and route.** New candidate; high priority. Golan coauthors [Deterministic LCS Approximation in Near-Linear Time, 2025](https://arxiv.org/abs/2507.22486) and [Exploring the Gap Between LCS and LCStr, CPM 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.27). The latter discusses the unresolved general-alphabet approximation gap. Subpolynomial approximation factors and the quasi-strongly-subquadratic 2026 approximation scheme do not yield a constant factor in almost-linear time. Allowing randomization here avoids conflating the target with the stronger deterministic question.

### P24. Exact distance labels for planar graphs

**Question.** What is the smallest worst-case label length needed so that exact distances in any unweighted undirected planar graph can be recovered using only the labels of the two queried vertices?

This asks how compactly a graph metric can be distributed across its vertices. The broad gap is between Ω(n^{1/3}) and O(√n) bits, rather than a query-time shave. Gawrychowski is a direct coauthor of the improved upper bound.

**Status and route.** Already [TCS-0775](../../data/cards/TCS-0775.json); replace its topic label with a precise model. [Gawrychowski–Uznański, Algorithmica 2023](https://doi.org/10.1007/s00453-023-01133-z) identifies the major open gap. Do not substitute distance oracles that also consult a shared graph data structure, approximate labels, or weighted-graph bounds.

### P25. Linear-time LZ77 pattern matching

**Question.** Given an LZ77 representation with z phrases and an explicit pattern of length m, can occurrence existence be decided deterministically in O(z+m) time, charging all preprocessing and allowing self-referencing copies?

Gawrychowski explicitly poses the question in [Dagstuhl 25191, §5.4](https://doi.org/10.4230/DagRep.15.5.1). Takeda’s association is through compressed matching, including [A Unifying Framework for Compressed Pattern Matching](https://citeseerx.ist.psu.edu/document?doi=b773cb5a017d788887703b97a627806432bdd3f6&repid=rep1&type=pdf).

**Status and route.** Already [TCS-0468](../../data/cards/TCS-0468.json). The [2011 LZ77 algorithm](https://arxiv.org/abs/1104.4203) has an extra logarithmic factor in the compressed-text term. [Linear-time grammar-compressed pattern matching](https://arxiv.org/abs/2111.05016) does not remove it for LZ77 because conversion can enlarge the representation. Occurrence detection avoids conflating the question with the cost of listing a very large output.

### P26. Linear-time unit-Monge distance multiplication

**Question.** Can two simple unit-Monge matrices, each given by its O(n)-size implicit permutation representation, be multiplied in the min-plus semiring in O(n) time, with the product returned implicitly?

This is Landau’s explicit “Can DIST tables be merged in linear time?” question, and a shared primitive behind semi-local sequence comparison and compressed-string algorithms. Explicit n-by-n input and output would make the proposed bound meaningless.

**Status and route.** New candidate. [Tiskin, Fast Distance Multiplication of Unit-Monge Matrices](https://doi.org/10.1007/s00453-013-9830-z) gives O(n log n) and explicitly attributes the linear target to Landau. The later [Core-Sparse Monge Matrix Multiplication](https://pure.mpg.de/rest/items/item_3629474_1/component/file_3629475/content) broadens the structured-matrix framework; no general linear solution was located. Although only a logarithmic gap remains, its role as a reusable alignment primitive makes it more substantial than a single-interface optimization.

### P27. Constant-factor approximation of the smallest grammar

**Question.** Can a polynomial-time algorithm output an acyclic grammar generating exactly a given string whose total right-hand-side length is at most C times optimum, for a universal constant C?

This asks whether a near-best hierarchical explanation of repeated data can be found efficiently. Gagie has a direct grammar-approximation connection, for example [On Two LZ78-style Grammars](https://arxiv.org/abs/1705.09538). Takeda’s compression work and Crochemore’s broader text-algorithm and compression work motivate the other associations; neither is being credited with originating this general approximation question.

**Status and route.** Already [TCS-6513](../../data/cards/TCS-6513.json), reviewed in September 2026. [The Smallest Grammar Problem](https://doi.org/10.1109/TIT.2005.850116) is a primary source for the approximation gap. An O(log n) approximation, a result for a specific compressor, or a different grammar-size convention does not settle the constant-factor target.

### P28. A general 2-approximation for shortest common superstring

**Question.** Is there a polynomial-time algorithm that, for every explicit set of strings, outputs a common superstring of length at most twice the optimum?

This is a central string-assembly approximation barrier. The association with Ukkonen is particularly direct through his superstring work; Crochemore’s connection is through string assembly and approximation algorithms. [A recent survey](https://arxiv.org/abs/2407.20422) gives historical context.

**Status and route.** The broader optimal-ratio target is already [TCS-7322](../../data/cards/TCS-7322.json); treat factor two as a milestone within that card. [Chukhin et al., August 2026](https://eccc.weizmann.ac.il/report/2026/157/) claim a 7/3 approximation. [Shibata, 1 September 2026](https://arxiv.org/abs/2609.01365) claims a 9/4 lower bound for maximum-overlap greedy. The greedy claim has not been independently verified here and does not refute the existence of a different 2-approximation algorithm. TCS-0816 concerns a separate exact exponential-time question.

### P29. The dense NFA Acceptance Hypothesis

**Suggested question.** For a fixed alphabet, n-state NFAs with Θ(n²) transitions, and an input word of length Θ(n), is n^{3−o(1)} time necessary for acceptance, or can a classical algorithm achieve O(n^{3−ε}) for some fixed ε > 0?

This connects automata simulation to labeled-graph matching, language reachability and dynamic lower bounds. Gørtz’s association is adjacent rather than direct authorship: [Bille–Gørtz, Sparse Regular Expression Matching](https://arxiv.org/abs/1907.04752) studies the underlying simulation framework. The dense arbitrary-NFA question is different from their sparse regex target.

**Status and route.** New candidate; broad significance, but a weaker personal association than gapped indexing. [Bringmann–Grønlund–Künnemann–Larsen, TheoretiCS 2024](https://arxiv.org/abs/2311.10204) formulate the hypothesis for general, including non-combinatorial, algorithms. Sparse-NFA SETH lower bounds do not settle the dense case. A final card should copy the source’s precise randomization and parameter conventions rather than silently expanding them.

### P30. Near-quadratic unweighted tree edit distance

**Suggested question.** Can exact unit-cost edit distance between rooted ordered labeled trees of total size n be computed in n^{2+o(1)} time? Operations are node insertion, deletion and relabeling with the standard ordered-tree semantics.

This asks whether hierarchical sequence comparison can be almost as fast as ordinary string edit distance. Bille’s tree-edit-distance work makes the association direct.

**Status and route.** Replacement direction for [TCS-5851](../../data/cards/TCS-5851.json), whose “truly subcubic” target is outdated. The [ICALP 2026 monotone-product paper](https://arxiv.org/abs/2605.07150) records and derandomizes an upper bound n^{(3+ω)/2+o(1)}, already below cubic. [Hardness of Dynamic Tree Edit Distance and Friends, ITCS 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.78) explicitly distinguishes the unresolved static string-versus-tree difficulty. Its dynamic lower bounds and weighted APSP equivalence do not settle the proposed static unit-cost target. The near-quadratic threshold is editorial.

### P31. Fully functional suffix trees in BWT-run-linear space

**Suggested question.** Can a text with r runs in its Burrows–Wheeler transform have a fully functional suffix-tree representation in O(r) words with polylogarithmic time per standard navigation operation?

The card must enumerate the interface, including parent/child navigation, suffix links, string depth, LCA and leaf-to-text-position access. Merely counting or reporting pattern occurrences is insufficient. The question seeks an entire navigation structure at the scale of repetitive input, and Gagie is a direct coauthor of the foundational r-index work.

**Status and route.** New candidate, with medium editorial priority because of its proximity to existing compressed-navigation questions. [Gagie–Navarro–Prezza](https://arxiv.org/abs/1705.10382) give the foundational structures; [Non-overlapping Indexing in BWT-Runs Bounded Space](https://par.nsf.gov/servlets/purl/10539699) explicitly discusses the still-open O(r)-space suffix-tree representation. O(r)-space pattern search is already known. This is not the previously removed character-access-only card TCS-6920, although the importance review should acknowledge that relationship.

### P32. Breaking two for sum-of-pairs multiple sequence alignment

**Question.** For an arbitrary number k of input strings and metric substitution/gap costs, is there a polynomial-time (2−ε)-approximation to minimum sum-of-pairs multiple sequence alignment for a universal ε > 0 independent of k?

This is a fundamental obstacle in comparing many biological sequences. Ukkonen’s association is editorial through sequence alignment and approximate matching, not a claim that he originated the factor-two question.

**Status and route.** Already [TCS-6669](../../data/cards/TCS-6669.json). The [Multiple Sequence Alignment survey](https://i.cs.hku.hk/~chin/paper/encycl_msa-1.pdf) and [Some Open Problems in Computational Molecular Biology](https://profs.sci.univr.it/~rrizzi/classes/BioComp2003/homeworks/openProblems.pdf) document the barrier. Bounds of the form 2−c/k, for fixed c, do not provide the required uniform improvement. Sum-of-pairs, column scoring, fixed-k alignment and local alignment must remain separate.

## Editorial order for new work

Start with P01, P04, P09, P10, P11, P18, P19, P21 and P23: they combine broad primitive-level significance with specific current sources. P06 is an especially strong general complexity candidate. P20 and P22 provide the clearest additional pangenome and sequencing connections, but their parameterized targets deserve careful formulation. P02 and P26 concern optimal construction or reusable alignment primitives. P29 has broad significance but a less direct researcher association; P31 is less urgent given existing compressed-navigation coverage.

P30 should begin as a status correction and replacement proposal for the old tree-edit-distance question. The 14 already represented topics should produce better statements, source updates or researcher links, not duplicate cards. No active or deleted catalogue record was changed by this research.

## Candidates deliberately excluded or qualified

- **Rotation distance:** [Dorfer, February 2026](https://arxiv.org/abs/2602.22874) claims NP-completeness. Do not present the old complexity question as safely open without assessing that claim.
- **Greedy Superstring Conjecture:** the September 2026 counterexample claim makes it unsuitable for an unqualified open card. The general approximation barrier P28 survives that distinction.
- **The runs conjecture and the classical distinct-squares bound:** both have been solved. [Franek’s PSC 2025 overview](https://www.stringology.org/papers/PSC2025.pdf) distinguishes these theorems from remaining stronger questions. Those narrower refinements were not chosen merely to manufacture unique author assignments.
- **Truly subcubic unweighted tree edit distance:** already surpassed; use P30 as a replacement direction.
- **Constant-time compact ISA access:** claimed solved in August 2026; P01 concerns SA and P02 construction time.
- **First subquadratic binary jumbled-index construction, first subquadratic-space/sublinear-query gapped index, and first general k-errata-tree space improvement:** all are already achieved by the cited papers. The proposals concern the remaining optimal frontiers.
- **O(r)-space character access:** TCS-6920 was deliberately removed on editorial-importance grounds. It is not recommended for automatic restoration. The active LZ77 access question P03 is the preferred general navigation card.
- **Unquantified dynamic compressed-index improvements:** TCS-6930 was previously removed for lack of a concrete target. Do not reintroduce the same broad program under an author’s name.
- **Generic approximate edit-distance indexing:** Navarro’s older IWOCA question is relevant background, but the more current compact top-k question is used for his assignment. P18 supplies a separately defined Hamming-indexing target; no unsupported claim is made that older edit-indexing lower-bound questions remain unchanged.

## Coverage and limits

The count treats Solon P. Pissis as one person and includes Esko Ukkonen. “Demaine” is interpreted as Erik Demaine and “Ian Munroe” as J. Ian Munro. Most selected questions concern string algorithms or biological sequence analysis; the geometry, order-theory and complexity choices reflect the named researchers’ main areas.

The dated literature search checked primary papers, author publication pages and open-problem statements, followed by comparison with active cards and deletion records. It is a candidate-selection review, not an exhaustive proof audit or a certification of every proposed strengthened threshold. Personal associations explicitly marked as editorial should remain marked that way in any later import.
