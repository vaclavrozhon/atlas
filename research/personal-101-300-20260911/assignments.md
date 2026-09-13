# Researcher problem suggestions 101–300

Review date: 2026-09-11. 400 assignments, 295 distinct problems: 283 existing cards and 12 additions.

Each researcher receives two substantial questions. Affinity is an editorial inference from the supplied research profile and the mathematical content; it is not an assertion that the researcher personally endorsed these priorities. The list gives short formulations, not full technical specifications. The linked canonical cards carry models and references.

Of the 12 new cards, nine have individually reviewed formulations and three remain explicitly marked source drafts. Across the full selection, 104 distinct cards have incomplete formulation metadata. Reusing an existing card does not newly certify its current openness or its formal completeness. Recent claims and rejected candidates are documented in [the admission audit](admission-audit.md).

Repeated questions point to the same ID. Related but distinct targets retain their existing IDs; for example, exact versus approximate edit distance, or information-theoretic code existence versus efficient construction. The rejected constant-time LCL decidability problem TCS-0513 is absent.

## 101. Michael Fredman

Dynamic optimality and fundamental limits of data structures.

- **[TCS-6498](../../data/cards/TCS-6498.json)** (formulated card): Are splay trees constant-competitive with the best offline binary search tree for every access sequence, allowing an additive initialization cost? [Source](https://arxiv.org/abs/2607.18498).
- **[TCS-6540](../../data/cards/TCS-6540.json)** (formulated card): Is there an explicit static data-structure problem with logarithmic-size queries requiring ω(log n) probes with near-linear storage? [Source](https://doi.org/10.1145/3798129.3800843).

## 102. Harold Gabow

Exact matching and combinatorial graph algorithms.

- **[TCS-6538](../../data/cards/TCS-6538.json)** (formulated card): Can an exact maximum-cardinality matching in a general graph be computed in randomized (m+n)^{1+o(1)} time? [Source](https://pubsonline.informs.org/doi/abs/10.1287/moor.2020.0388).
- **[TCS-6511](../../data/cards/TCS-6511.json)** (formulated card): Can a perfect matching with exactly k red edges be found, or ruled out, deterministically in polynomial time in a red/blue general graph? [Source](https://doi.org/10.4230/LIPIcs.STACS.2023.29).

## 103. Zvi Galil

String algorithms and matching-based optimization.

- **[TCS-7322](../../data/cards/TCS-7322.json)** (new; formulated card): Can shortest common superstring be approximated within factor two in polynomial time by some algorithm, without restricting it to maximum-overlap greedy? [Source](https://eccc.weizmann.ac.il/report/2026/157/).
- **[TCS-7179](../../data/cards/TCS-7179.json)** (formulated card): Can exact edit distance of length-n strings be computed in O(n^{2−ε}) time for some fixed ε>0? [Source](https://arxiv.org/abs/1412.0348).

## 104. Robert Sedgewick

Sorting and its analysis connect the general integer-sorting barrier with the long-standing average-case complexity of Shellsort.

- **[TCS-6537](../../data/cards/TCS-6537.json)** (formulated card): Can n word-sized integers be sorted in expected O(n) time on a uniform word RAM for every word length w≥log n? [Source](https://doi.org/10.1109/SFCS.2002.1181890).
- **[TCS-7173](../../data/cards/TCS-7173.json)** (source draft): What is the optimal expected number of operations of Shellsort on a uniformly random permutation, optimized over increment sequences as a function of input size? [Source](https://arxiv.org/abs/cs/9906008).

## 105. David Eppstein

Geometric spanning trees and dynamic graph optimization.

- **[TCS-0403](../../data/cards/TCS-0403.json)** (source draft; status unverified): For every fixed dimension d, can the exact Euclidean minimum spanning tree of n points be computed in O(n polylog n) time? This is the near-linear interpretation of the source’s geometric MST question. [Source](https://topp.openproblem.net/p5).
- **[TCS-6626](../../data/cards/TCS-6626.json)** (formulated card): Can an exact minimum spanning forest be maintained with polylogarithmic worst-case time per edge insertion, deletion or weight change? [Source](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf).

## 106. Seth Pettie

Optimal comparison algorithms and minimum spanning trees.

- **[TCS-6536](../../data/cards/TCS-6536.json)** (formulated card): Can a minimum spanning tree of an arbitrary real-weighted graph be computed deterministically in O(m+n) comparison-RAM time? [Source](https://people.csail.mit.edu/karger/Papers/mst.pdf).
- **[TCS-0388](../../data/cards/TCS-0388.json)** (formulated card): Can all n² pairwise sums x_i+y_j of two real n-element lists be sorted in O(n²) time on a uniform real RAM? [Source](https://topp.openproblem.net/p41).

## 107. Timothy Chan

Output-sensitive geometry and the arithmetic complexity of geometric problems.

- **[TCS-0410](../../data/cards/TCS-0410.json)** (source draft; status unverified): Can the convex hull of n points in every fixed dimension be computed in O(n log(f+2)+f) time, where f is the number of output facets? [Source](https://topp.openproblem.net/p15).
- **[TCS-0557](../../data/cards/TCS-0557.json)** (source draft; status unverified): Does 3SUM on n real numbers have an O(n^{2−ε}) algorithm for some constant ε>0 in the real-RAM model? [Source](https://topp.openproblem.net/p11).

## 108. Gary Miller

Work-efficient parallel graph algorithms.

- **[TCS-6507](../../data/cards/TCS-6507.json)** (formulated card): Can parallel directed reachability use near-linear total work and polylogarithmic depth on arbitrary sparse graphs? [Source](https://doi.org/10.4230/LIPIcs.ICALP.2026.15).
- **[TCS-6504](../../data/cards/TCS-6504.json)** (formulated card): Can perfect matching in general graphs be constructed by logspace-uniform polynomial-size circuits of polylogarithmic depth, without randomness? [Source](https://doi.org/10.1109/FOCS.2017.70).

## 109. Moses Charikar

Approximation barriers in clustering-like graph problems and compression.

- **[TCS-6587](../../data/cards/TCS-6587.json)** (formulated card): Does Densest k-Subgraph admit a polynomial-time constant-factor approximation? [Source](https://arxiv.org/abs/1001.2891).
- **[TCS-6513](../../data/cards/TCS-6513.json)** (formulated card): Does the smallest grammar generating a given explicit string admit a polynomial-time constant-factor approximation? [Source](https://doi.org/10.1109/TIT.2005.850116).

## 110. David Shmoys

Facility location and scheduling approximation.

- **[TCS-6659](../../data/cards/TCS-6659.json)** (formulated card): Does metric k-Median admit polynomial-time approximation ratio 1+2/e+ε for every constant ε>0? [Source](https://people.idsia.ch/~grandoni/Pubblicazioni/CGLSS25stoc.pdf).
- **[TCS-6638](../../data/cards/TCS-6638.json)** (formulated card): Can unrelated-machine makespan be approximated in polynomial time within 2−ε for some universal ε>0? [Source](https://ir.cwi.nl/pub/18055).

## 111. David Williamson

Semidefinite approximation and covering/deletion problems.

- **[TCS-7281](../../data/cards/TCS-7281.json)** (formulated card): Is beating the Goemans–Williamson Max-Cut approximation constant by any fixed amount NP-hard without assuming Unique Games? [Source](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/07/Optimal_Inapproximability_Results_for_MAX_CUT_and_Other_2_Variable_CSPs_1.pdf).
- **[TCS-6591](../../data/cards/TCS-6591.json)** (source draft): Does Directed Feedback Vertex Set admit a polynomial-time constant-factor approximation? [Source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2016.55).

## 112. Sanjeev Khanna

Precedence scheduling and min-plus convolution connect approximation limits with resource-sensitive combinatorial algorithms.

- **[TCS-6676](../../data/cards/TCS-6676.json)** (formulated card): Can precedence-constrained scheduling on identical machines beat approximation factor two by an absolute constant when the number of machines is part of the input? [Source](https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1966.tb01709.x).
- **[TCS-6598](../../data/cards/TCS-6598.json)** (source draft): Does min-plus convolution of two length-n integer arrays require n^{2−o(1)} time in the word-RAM model? [Source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.119).

## 113. Chandra Chekuri

Network design and the discrepancy barriers underlying rounding.

- **[TCS-6588](../../data/cards/TCS-6588.json)** (formulated card): Does Directed Steiner Tree admit a polynomial-time polylogarithmic approximation in the number of terminals? [Source](https://chekuri.web.engr.illinois.edu/pub.html).
- **[TCS-7314](../../data/cards/TCS-7314.json)** (new; formulated card): Does every real matrix whose columns have Euclidean norm at most one admit a ±1 column signing with every row sum bounded by a universal constant? [Source](https://arxiv.org/abs/2508.03961).

## 114. Aravind Srinivasan

Probabilistic rounding and online selection under combinatorial constraints.

- **[TCS-7315](../../data/cards/TCS-7315.json)** (new; formulated card): Does every set system in which each element belongs to at most t sets have discrepancy O(√t), independently of the numbers of sets and elements? [Source](https://arxiv.org/abs/2508.03961).
- **[TCS-7316](../../data/cards/TCS-7316.json)** (new; formulated card): Does the general matroid secretary problem admit a constant-competitive randomized strategy for adversarial weights arriving in uniformly random order? [Source](https://arxiv.org/abs/2305.05353).

## 115. Anna Karlin

Metric TSP and randomized online decision making.

- **[TCS-6589](../../data/cards/TCS-6589.json)** (formulated card): Is the integrality gap of the subtour LP for symmetric metric TSP at most 4/3? [Source](https://arxiv.org/abs/2607.01536v2).
- **[TCS-6575](../../data/cards/TCS-6575.json)** (formulated card): Is there a deterministic k-competitive online strategy for k-server on every metric space? [Source](https://www.cs.cmu.edu/~sleator/papers/server-problems.pdf).

## 116. Susanne Albers

Scheduling complexity and online service problems.

- **[TCS-0935](../../data/cards/TCS-0935.json)** (source draft; status unverified): For each fixed number m≥3 of identical machines, can precedence-constrained unit-job makespan be optimized in polynomial time? [Source](https://a3nm.net/work/research/questions/#complexity-of-makespan-scheduling-of-unit-jobs-with-precedence-constraints).
- **[TCS-6676](../../data/cards/TCS-6676.json)** (formulated card): Can precedence-constrained scheduling on identical machines beat approximation factor two by an absolute constant when the number of machines is part of the input? [Source](https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1966.tb01709.x).

## 117. Claire Mathieu

Approximation schemes for packing and geometric optimization.

- **[TCS-6640](../../data/cards/TCS-6640.json)** (formulated card): Is there a polynomial-time bin-packing algorithm whose number of bins exceeds optimum by at most an absolute constant? [Source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2014.1).
- **[TCS-0408](../../data/cards/TCS-0408.json)** (source draft; status unverified): What is the optimal exact running time for minimum-total-length perfect matching of 2n points in the Euclidean plane? Approximate matching does not settle this target. [Source](https://topp.openproblem.net/p6).

## 118. Amos Fiat

Randomized online algorithms and secretary-type selection.

- **[TCS-7317](../../data/cards/TCS-7317.json)** (new; formulated card): Does randomized k-server on every finite metric admit a polylog(k)-competitive strategy against an oblivious adversary, with no dependence on the number of metric points? [Source](https://arxiv.org/abs/2605.01497).
- **[TCS-7316](../../data/cards/TCS-7316.json)** (new; formulated card): Does the general matroid secretary problem admit a constant-competitive randomized strategy for adversarial weights arriving in uniformly random order? [Source](https://arxiv.org/abs/2305.05353).

## 119. Yossi Azar

Randomized service and unrelated-machine scheduling connect online load management with the algorithmic difficulty of allocating work.

- **[TCS-7317](../../data/cards/TCS-7317.json)** (new; formulated card): Does randomized k-server on every finite metric admit a polylog(k)-competitive strategy against an oblivious adversary, with no dependence on the number of metric points? [Source](https://arxiv.org/abs/2605.01497).
- **[TCS-6638](../../data/cards/TCS-6638.json)** (formulated card): Can unrelated-machine makespan be approximated in polynomial time within 2−ε for some universal ε>0? [Source](https://ir.cwi.nl/pub/18055).

## 120. Nikhil Bansal

The two central vector-balancing conjectures behind algorithmic discrepancy.

- **[TCS-7314](../../data/cards/TCS-7314.json)** (new; formulated card): Does every real matrix whose columns have Euclidean norm at most one admit a ±1 column signing with every row sum bounded by a universal constant? [Source](https://arxiv.org/abs/2508.03961).
- **[TCS-7315](../../data/cards/TCS-7315.json)** (new; formulated card): Does every set system in which each element belongs to at most t sets have discrepancy O(√t), independently of the numbers of sets and elements? [Source](https://arxiv.org/abs/2508.03961).

## 121. Niv Buchbinder

Influence-maximization adaptivity and matroid secretary selection concern the value of information in sequential combinatorial optimization.

- **[TCS-7288](../../data/cards/TCS-7288.json)** (source draft): Is the adaptivity gap for influence maximization under full-adoption feedback bounded by an absolute constant on every graph? [Source](https://iris.gssi.it/handle/20.500.12571/26964).
- **[TCS-7316](../../data/cards/TCS-7316.json)** (new; formulated card): Does the general matroid secretary problem admit a constant-competitive randomized strategy for adversarial weights arriving in uniformly random order? [Source](https://arxiv.org/abs/2305.05353).

## 122. Anupam Gupta

Metric representations and terminal-preserving graph compression.

- **[TCS-6525](../../data/cards/TCS-6525.json)** (formulated card): For every fixed excluded minor H, do all shortest-path metrics of H-minor-free graphs embed into ℓ₁ with distortion bounded only by H? [Source](https://people.eecs.berkeley.edu/~sinclair/cuts.pdf).
- **[TCS-6527](../../data/cards/TCS-6527.json)** (source draft): Can every weighted graph with designated terminals be reduced to a minor on exactly those terminals while preserving all terminal distances within a universal constant factor? [Source](https://epubs.siam.org/doi/10.1137/1.9781611977912.191).

## 123. Thomas Rothvoss

Dimension dependence in integer programming and semidefinite extension complexity both ask how efficiently discrete feasible sets can be represented or optimized.

- **[TCS-7264](../../data/cards/TCS-7264.json)** (formulated card): Can integer programming with n variables be solved in 2^{O(n)} times a polynomial in the input bit length? [Source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol358-ipec2025/html/LIPIcs.IPEC.2025.1/LIPIcs.IPEC.2025.1.html).
- **[TCS-7283](../../data/cards/TCS-7283.json)** (formulated card): Does the perfect matching polytope require semidefinite extended formulations of superpolynomial size? [Source](https://digital.lib.washington.edu/server/api/core/bitstreams/a7ac9607-c4f8-4d56-9b29-0f5ef033975d/content).

## 124. Shayan Oveis Gharan

The integrality gaps at the center of symmetric and asymmetric TSP.

- **[TCS-6589](../../data/cards/TCS-6589.json)** (formulated card): Is the integrality gap of the subtour LP for symmetric metric TSP at most 4/3? [Source](https://arxiv.org/abs/2607.01536v2).
- **[TCS-6590](../../data/cards/TCS-6590.json)** (formulated card): Is the integrality gap of the subtour LP for asymmetric metric TSP at most two? [Source](https://epubs.siam.org/doi/10.1137/20M1339313).

## 125. Aleksander Mądry

Exact network flow and the arithmetic complexity of linear programming.

- **[TCS-7228](../../data/cards/TCS-7228.json)** (formulated card): Can exact directed maximum flow with polynomially bounded integer capacities be computed in O((m+n) polylog n) time? [Source](https://arxiv.org/abs/2203.00671).
- **[TCS-0008](../../data/cards/TCS-0008.json)** (formulated card; status unverified): Does rational linear programming have a strongly polynomial algorithm, with polynomial intermediate bit lengths? [Source](https://topp.openproblem.net/p8).

## 126. Yin Tat Lee

Convex geometry and the foundations of fast optimization.

- **[TCS-6574](../../data/cards/TCS-6574.json)** (formulated card): Is exact feasibility of rational semidefinite programs decidable in polynomial bit complexity, including degenerate instances without an interior-point promise? [Source](https://link.springer.com/article/10.1007/BF02614433).
- **[TCS-6572](../../data/cards/TCS-6572.json)** (formulated card): Does some simplex pivot rule solve every rational linear program in polynomial bit complexity? [Source](https://www.cs.yale.edu/homes/spielman/simplex/).

## 127. Aaron Sidford

Integer shortest paths and sparse linear systems are two basic targets for the fast graph and continuous optimization methods in this profile.

- **[TCS-7263](../../data/cards/TCS-7263.json)** (formulated card): Can directed SSSP with positive integer weights be solved in deterministic O(m+n) word-RAM time? [Source](https://arxiv.org/abs/2504.17033).
- **[TCS-6585](../../data/cards/TCS-6585.json)** (formulated card): Can arbitrary sparse rational linear systems be solved in nearly linear time, with the precision and conditioning dependence specified in the atlas? [Source](https://arxiv.org/abs/2007.10254).

## 128. Richard Peng

Parallel reachability and min-plus distance circuits ask, in different models, which graph computations can be made fundamentally faster.

- **[TCS-6507](../../data/cards/TCS-6507.json)** (formulated card): Can parallel directed reachability use near-linear total work and polylogarithmic depth on arbitrary sparse graphs? [Source](https://doi.org/10.4230/LIPIcs.ICALP.2026.15).
- **[TCS-0481](../../data/cards/TCS-0481.json)** (formulated card): Must every min-plus circuit computing one exact pair distance in an n-vertex complete undirected weighted graph have Ω(n³) gates? [Source](https://doi.org/10.1007/s00224-014-9574-4).

## 129. Yurii Nesterov

Oracle and arithmetic complexity in convex optimization.

- **[TCS-0008](../../data/cards/TCS-0008.json)** (formulated card; status unverified): Does rational linear programming have a strongly polynomial algorithm, with polynomial intermediate bit lengths? [Source](https://topp.openproblem.net/p8).
- **[TCS-6574](../../data/cards/TCS-6574.json)** (formulated card): Is exact feasibility of rational semidefinite programs decidable in polynomial bit complexity, including degenerate instances without an interior-point promise? [Source](https://link.springer.com/article/10.1007/BF02614433).

## 130. Arkadi Nemirovski

P-matrix complementarity and Smale’s energy problem expose foundational complexity questions in continuous optimization.

- **[TCS-7231](../../data/cards/TCS-7231.json)** (formulated card): Can every rational P-matrix linear complementarity problem be solved in polynomial time? [Source](https://deepblue.lib.umich.edu/items/a1c9654c-7237-481d-b85a-799c7fae07a5).
- **[TCS-6578](../../data/cards/TCS-6578.json)** (source draft): Can a BSS real-arithmetic algorithm construct n points on the sphere in polynomial time whose logarithmic energy is within O(log n) of minimum? [Source](https://www.lebesgue.fr/sites/default/files/inline-files/Yakir.pdf).

## 131. Aaron Bernstein

Dynamic shortest paths and matching.

- **[TCS-0478](../../data/cards/TCS-0478.json)** (formulated card): Can exact fully dynamic directed all-pairs shortest paths have Õ(m) amortized update time and polylogarithmic query time for positive polynomially bounded integer weights? [Source](https://doi.org/10.4230/DagRep.11.1.1).
- **[TCS-6627](../../data/cards/TCS-6627.json)** (formulated card): Can a (1+ε)-approximate maximum matching be maintained fully dynamically with polylogarithmic update time for each fixed ε>0? [Source](https://pure.mpg.de/pubman/item/item_3527212_4/component/file_3527885/biennial-report-2023.pdf).

## 132. Danupon Nanongkai

Distributed shortest paths and dynamic connectivity measures.

- **[TCS-6555](../../data/cards/TCS-6555.json)** (formulated card): Can exact weighted SSSP in CONGEST be solved in Õ(√n+D) rounds on every undirected network of hop diameter D? [Source](https://link.springer.com/article/10.1007/s00446-026-00505-2).
- **[TCS-6670](../../data/cards/TCS-6670.json)** (formulated card): Can the exact global minimum cut of an undirected graph be maintained fully dynamically with polylogarithmic update time? [Source](https://arxiv.org/abs/2512.13105).

## 133. Thatchaphol Saranurak

Dynamic graph decomposition and spanning-forest maintenance.

- **[TCS-6625](../../data/cards/TCS-6625.json)** (formulated card): Can fully dynamic graph connectivity be maintained deterministically with polylogarithmic worst-case update and query times? [Source](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf).
- **[TCS-6626](../../data/cards/TCS-6626.json)** (formulated card): Can an exact minimum spanning forest be maintained with polylogarithmic worst-case time per edge insertion, deletion or weight change? [Source](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf).

## 134. Shiri Chechik

Distance representations, routing and graph sparsification.

- **[TCS-7305](../../data/cards/TCS-7305.json)** (source draft): For every k≥2, can universal compact routing attain stretch 2k−1 and Õ(n^{1/k}) words per vertex without a preliminary handshake? [Source](https://theory.stanford.edu/~virgi/cs267/papers/chechik-compactroute.pdf).
- **[TCS-6500](../../data/cards/TCS-6500.json)** (formulated card): For every integer k≥2, are there arbitrarily large n-vertex graphs of girth greater than 2k with Ω_k(n^{1+1/k}) edges? [Source](https://doi.org/10.4230/LIPIcs.ESA.2026.31).

## 135. Karl Bringmann

Fine-grained barriers for exact and approximate string distance.

- **[TCS-7179](../../data/cards/TCS-7179.json)** (formulated card): Can exact edit distance of length-n strings be computed in O(n^{2−ε}) time for some fixed ε>0? [Source](https://arxiv.org/abs/1412.0348).
- **[TCS-7220](../../data/cards/TCS-7220.json)** (formulated card): For every ε>0, does edit distance admit a (1+ε)-approximation in truly subquadratic time? [Source](https://theorydish.blog/2018/07/20/approximating-edit-distance/).

## 136. Kasper Green Larsen

Unconditional cell-probe lower bounds.

- **[TCS-0949](../../data/cards/TCS-0949.json)** (source draft; status unverified): Does Boolean matrix–vector multiplication require ω(n) cell probes per query when an n×n Boolean matrix is stored succinctly with only o(n²) redundancy? [Source](https://sublinear.info/index.php?title=Open_Problems:75).
- **[TCS-6540](../../data/cards/TCS-6540.json)** (formulated card): Is there an explicit static data-structure problem with logarithmic-size queries requiring ω(log n) probes with near-linear storage? [Source](https://doi.org/10.1145/3798129.3800843).

## 137. Rasmus Kyng

Exact maximum flow and general sparse linear systems capture the reach of nearly linear numerical and graph algorithms.

- **[TCS-7228](../../data/cards/TCS-7228.json)** (formulated card): Can exact directed maximum flow with polynomially bounded integer capacities be computed in O((m+n) polylog n) time? [Source](https://arxiv.org/abs/2203.00671).
- **[TCS-6585](../../data/cards/TCS-6585.json)** (formulated card): Can arbitrary sparse rational linear systems be solved in nearly linear time, with the precision and conditioning dependence specified in the atlas? [Source](https://arxiv.org/abs/2007.10254).

## 138. Bernard Chazelle

Discrepancy and the geometry of range spaces.

- **[TCS-7314](../../data/cards/TCS-7314.json)** (new; formulated card): Does every real matrix whose columns have Euclidean norm at most one admit a ±1 column signing with every row sum bounded by a universal constant? [Source](https://arxiv.org/abs/2508.03961).
- **[TCS-6526](../../data/cards/TCS-6526.json)** (source draft): What is the optimal dependence on ε of the size of weak ε-nets for convex ranges in each fixed Euclidean dimension? [Source](https://arxiv.org/abs/1808.02686).

## 139. Pankaj Agarwal

Combinatorial geometry and high-dimensional geometric measure.

- **[TCS-0318](../../data/cards/TCS-0318.json)** (source draft): What is the asymptotic maximum number of k-element subsets strictly separable by a line from the remaining points of an n-point planar set in general position? [Source](https://topp.openproblem.net/p7).
- **[TCS-7184](../../data/cards/TCS-7184.json)** (source draft): What is the optimal exact running time for computing the volume of the union of n axis-parallel boxes in each fixed dimension d≥3? [Source](https://doi.org/10.1109/FOCS.2013.51).

## 140. Joseph Mitchell

Exact planar matching and the planar Steiner ratio connect geometric distances to optimal network structure.

- **[TCS-0408](../../data/cards/TCS-0408.json)** (source draft; status unverified): What is the optimal exact running time for minimum-total-length perfect matching of 2n points in the Euclidean plane? Approximate matching does not settle this target. [Source](https://topp.openproblem.net/p6).
- **[TCS-7185](../../data/cards/TCS-7185.json)** (source draft): Is the Euclidean Steiner-tree/MST length ratio of every finite planar point set at least √3/2? [Source](https://doi.org/10.1007/s00453-011-9508-3).

## 141. Emo Welzl

Randomized linear programming and geometric search.

- **[TCS-6573](../../data/cards/TCS-6573.json)** (formulated card): Is the edge-graph diameter of every d-dimensional polyhedron with n facets bounded by a polynomial in n and d? [Source](https://ti.inf.ethz.ch/ew/courses/Geo25/lecture/gca25-10.pdf).
- **[TCS-0411](../../data/cards/TCS-0411.json)** (source draft; status unverified): Can point location in a three-dimensional polyhedral subdivision with n faces use O(n) space and O(log n) query time? [Source](https://topp.openproblem.net/p13).

## 142. Kenneth Clarkson

Polyhedral diameter and Tarski fixed-point queries concern the complexity of navigating geometric and ordered feasible sets.

- **[TCS-6573](../../data/cards/TCS-6573.json)** (formulated card): Is the edge-graph diameter of every d-dimensional polyhedron with n facets bounded by a polynomial in n and d? [Source](https://ti.inf.ethz.ch/ew/courses/Geo25/lecture/gca25-10.pdf).
- **[TCS-0491](../../data/cards/TCS-0491.json)** (formulated card): For every fixed k, can a fixed point of an oracle-given monotone map [n]^k→[n]^k be found using O_k(log² n) deterministic queries? [Source](https://doi.org/10.4230/DagRep.12.1.101).

## 143. Sariel Har-Peled

Entrywise low-rank approximation and weak convex ε-nets link geometric approximation with compact representations of data.

- **[TCS-7298](../../data/cards/TCS-7298.json)** (source draft): Does entrywise ℓ₁ rank-k approximation admit a polynomial-time approximation factor independent of k when k is part of the input? [Source](https://epubs.siam.org/doi/10.1137/1.9781611975482.47).
- **[TCS-6526](../../data/cards/TCS-6526.json)** (source draft): What is the optimal dependence on ε of the size of weak ε-nets for convex ranges in each fixed Euclidean dimension? [Source](https://arxiv.org/abs/1808.02686).

## 144. Assaf Naor

Metric embedding and dimension reduction.

- **[TCS-6524](../../data/cards/TCS-6524.json)** (source draft): Does every doubling subset of Hilbert space embed bi-Lipschitz into a finite-dimensional Euclidean space with dimension and distortion depending only on its doubling constant? [Source](https://web.math.princeton.edu/~naor/homepage%20files/assouad-N%28K%29.pdf).
- **[TCS-6529](../../data/cards/TCS-6529.json)** (source draft): What is the optimal ℓ₁ embedding distortion of planar Earth Mover Distance on an n×n grid? [Source](https://www.weizmann.ac.il/math/gideon/sites/math.gideon/files/uploads/planar-earthmover.pdf).

## 145. Neil Robertson

Graph minors and the structure of cubic graphs.

- **[TCS-6651](../../data/cards/TCS-6651.json)** (formulated card): Does every graph of chromatic number at least t contain a K_t minor? [Source](https://arxiv.org/abs/2609.06867v2).
- **[TCS-7249](../../data/cards/TCS-7249.json)** (formulated card): Does every bridgeless cubic graph have six perfect matchings, allowing repetition, such that every edge belongs to exactly two? [Source](https://www.openproblemgarden.org/op/the_berge_fulkerson_conjecture).

## 146. Maria Chudnovsky

Induced subgraphs and chromatic structure.

- **[TCS-6652](../../data/cards/TCS-6652.json)** (formulated card): For every fixed forbidden induced graph H, does every H-free n-vertex graph contain a clique or independent set of size n^{ε_H} for some ε_H>0? [Source](https://mathweb.ucsd.edu/~asuk/erdos_hajnal.pdf).
- **[TCS-6653](../../data/cards/TCS-6653.json)** (formulated card): For every tree T and clique bound k, is chromatic number bounded in all T-induced-free graphs with clique number at most k? [Source](https://arxiv.org/abs/2302.08922).

## 147. Jaroslav Nešetřil

Sparse graph classes, logic and structural tractability.

- **[TCS-6678](../../data/cards/TCS-6678.json)** (formulated card): Is first-order model checking fixed-parameter tractable on every hereditary monadically dependent graph class? [Source](https://arxiv.org/abs/2501.04166).
- **[TCS-7241](../../data/cards/TCS-7241.json)** (formulated card): Can twin-width be approximated in fixed-parameter time with the approximation guarantee depending only on the true twin-width? [Source](https://perso.ens-lyon.fr/edouard.bonnet/openQuestions.html).

## 148. Nathan Linial

Metric geometry and Boolean-function analysis.

- **[TCS-6525](../../data/cards/TCS-6525.json)** (formulated card): For every fixed excluded minor H, do all shortest-path metrics of H-minor-free graphs embed into ℓ₁ with distortion bounded only by H? [Source](https://people.eecs.berkeley.edu/~sinclair/cuts.pdf).
- **[TCS-6604](../../data/cards/TCS-6604.json)** (formulated card): Is the Fourier entropy of every Boolean function bounded by a universal constant times its total influence? [Source](https://www.cs.cmu.edu/~jswright/papers/fei.pdf).

## 149. Tomasz Kociumaka

String distance and the limits of grammar compression.

- **[TCS-7235](../../data/cards/TCS-7235.json)** (formulated card): For every fixed ε>0, can edit distance be (1+ε)-approximated in n^{1+o(1)} time? [Source](https://arxiv.org/abs/2005.07678).
- **[TCS-0468](../../data/cards/TCS-0468.json)** (formulated card): Can occurrence of an explicit m-symbol pattern in an LZ77-compressed text with z phrases be decided in O(z+m) time, including preprocessing? [Source](https://doi.org/10.4230/DagRep.15.5.1).

## 150. Paolo Ferragina

The pair concerns the space needed to support random access in two central compressed-text representations.

- **[TCS-0467](../../data/cards/TCS-0467.json)** (formulated card): Can random access in an LZ77-compressed string of length N use O(z) words and O(log N) worst-case query time, where z is its parse size? [Source](https://doi.org/10.4230/DagRep.15.5.1).
- **[TCS-0470](../../data/cards/TCS-0470.json)** (formulated card): Can a string generated by a grammar of g rules support O(log N)-time random access using only O(g log g) bits in total? [Source](https://doi.org/10.4230/DagRep.15.5.1).

## 151. Gonzalo Navarro

The pair connects the approximation of grammar size with searching directly in compressed input.

- **[TCS-6513](../../data/cards/TCS-6513.json)** (formulated card): Does the smallest grammar generating a given explicit string admit a polynomial-time constant-factor approximation? [Source](https://doi.org/10.1109/TIT.2005.850116).
- **[TCS-0468](../../data/cards/TCS-0468.json)** (formulated card): Can occurrence of an explicit m-symbol pattern in an LZ77-compressed text with z phrases be decided in O(z+m) time, including preprocessing? [Source](https://doi.org/10.4230/DagRep.15.5.1).

## 152. Pavel Pevzner

Sequence assembly and reconstruction from noisy sequence observations.

- **[TCS-7322](../../data/cards/TCS-7322.json)** (new; formulated card): Can shortest common superstring be approximated within factor two in polynomial time by some algorithm, without restricting it to maximum-overlap greedy? [Source](https://eccc.weizmann.ac.il/report/2026/157/).
- **[TCS-6623](../../data/cards/TCS-6623.json)** (formulated card): Can every n-bit string be reconstructed from polynomially many independent deletion-channel traces at any fixed deletion rate below one? [Source](https://www.math.kent.edu/~zchase/tr_lower.pdf).

## 153. Bonnie Berger

Multiple-sequence alignment and approximate edit distance are central algorithmic primitives for comparing biological sequences.

- **[TCS-6669](../../data/cards/TCS-6669.json)** (source draft): Can sum-of-pairs multiple sequence alignment be approximated in polynomial time within 2−ε for some constant ε>0? [Source](https://i.cs.hku.hk/~chin/paper/encycl_msa-1.pdf).
- **[TCS-7220](../../data/cards/TCS-7220.json)** (formulated card): For every ε>0, does edit distance admit a (1+ε)-approximation in truly subquadratic time? [Source](https://theorydish.blog/2018/07/20/approximating-edit-distance/).

## 154. Richard Lipton

Circuit complexity and exact algebraic counting.

- **[TCS-0020](../../data/cards/TCS-0020.json)** (source draft; status unverified): Does EXP contain a language with no polynomial-size Boolean circuits? [Source](https://www.math.ias.edu/files/mathandcomp.pdf).
- **[TCS-6616](../../data/cards/TCS-6616.json)** (source draft): Can the exact permanent of an n×n integer matrix be computed in O*((2−ε)^n) time for some fixed ε>0? [Source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.36).

## 155. Eric Allender

Circuit minimization and unambiguous logarithmic space connect metacomplexity with the structural space-complexity side of this profile.

- **[TCS-5501](../../data/cards/TCS-5501.json)** (source draft; status unverified): Is the Minimum Circuit Size Problem NP-hard under deterministic polynomial-time many-one reductions, when a function is given by its full truth table? [Source](https://doi.org/10.4230/LIPIcs.CCC.2023.31).
- **[TCS-6533](../../data/cards/TCS-6533.json)** (formulated card): Is NL=UL: can every nondeterministic logarithmic-space decision problem be solved with at most one accepting computation per input? [Source](https://people.cs.rutgers.edu/~allender/papers/nlul.pdf).

## 156. Paul Beame

Proof lower bounds and time-space tradeoffs for graph computation.

- **[TCS-6602](../../data/cards/TCS-6602.json)** (formulated card): Can superpolynomial proof-size lower bounds be proved for constant-depth Frege systems with modular counting connectives? [Source](https://www.karlin.mff.cuni.cz/~krajicek/finitary.pdf).
- **[TCS-6556](../../data/cards/TCS-6556.json)** (formulated card): Can directed reachability be decided with near-linear streaming memory and polylogarithmically many passes over an adversarially ordered edge stream? [Source](https://par.nsf.gov/servlets/purl/10488812).

## 157. Lance Fortnow

The structure of counting, alternation and space complexity.

- **[TCS-6532](../../data/cards/TCS-6532.json)** (formulated card): Is the polynomial hierarchy strict at every finite level? [Source](https://www.math.ias.edu/files/Book-online-Aug0619.pdf).
- **[TCS-6455](../../data/cards/TCS-6455.json)** (formulated card): Does every polynomial-space computation taking time T have an interactive proof with a polynomial-input-time verifier and an honest prover running in poly(T) time? [Source](https://eccc.weizmann.ac.il/report/2026/102/).

## 158. Michael Sipser

Randomness and small circuit classes.

- **[TCS-0003](../../data/cards/TCS-0003.json)** (formulated card; status unverified): Does P=BPP: can every polynomial-time bounded-error randomized decision algorithm be replaced by a deterministic polynomial-time algorithm? [Source](https://www.math.ias.edu/files/mathandcomp.pdf).
- **[TCS-6535](../../data/cards/TCS-6535.json)** (formulated card): Is nonuniform TC⁰ strictly weaker than NC¹? [Source](https://eccc.weizmann.ac.il/report/2018/199/).

## 159. Shmuel Safra

Small-soundness PCPs and the hardness of approximate graph colouring are two substantive manifestations of the PCP and inapproximability program.

- **[TCS-7268](../../data/cards/TCS-7268.json)** (formulated card): Does the sliding-scale PCP conjecture hold with inverse-polynomial soundness, the constant query bound and alphabet dependence specified in the atlas? [Source](https://arxiv.org/abs/1505.06362).
- **[TCS-7237](../../data/cards/TCS-7237.json)** (formulated card): Is it NP-hard to distinguish 3-colourable graphs from graphs requiring more than six colours? [Source](https://arxiv.org/abs/1811.00970).

## 160. Seinosuke Toda

The relation between counting and decision complexity.

- **[TCS-6532](../../data/cards/TCS-6532.json)** (formulated card): Is the polynomial hierarchy strict at every finite level? [Source](https://www.math.ias.edu/files/Book-online-Aug0619.pdf).
- **[TCS-1004](../../data/cards/TCS-1004.json)** (source draft; status unverified): Does counting the satisfying assignments of a DNF admit a deterministic fully polynomial relative-approximation scheme? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 161. Jin-Yi Cai

The complexity landscape of exact and approximate counting CSPs.

- **[TCS-7320](../../data/cards/TCS-7320.json)** (new; formulated card): Is approximate counting for every fixed finite family of nonnegative rational Boolean log-supermodular constraints approximation-preserving reducible to #BIS? [Source](https://drops.dagstuhl.de/storage/02dagstuhl-follow-ups/dfu-vol007/DFU.Vol7.15301.205/DFU.Vol7.15301.205.pdf).
- **[TCS-7221](../../data/cards/TCS-7221.json)** (formulated card): Does counting independent sets in bipartite graphs admit an FPRAS? [Source](https://link.springer.com/article/10.1007/s00453-019-00606-4).

## 162. Xi Chen

Log-supermodular approximate counting and exact assignment-market equilibrium connect this profile’s counting and equilibrium-complexity work.

- **[TCS-7320](../../data/cards/TCS-7320.json)** (new; formulated card): Is approximate counting for every fixed finite family of nonnegative rational Boolean log-supermodular constraints approximation-preserving reducible to #BIS? [Source](https://drops.dagstuhl.de/storage/02dagstuhl-follow-ups/dfu-vol007/DFU.Vol7.15301.205/DFU.Vol7.15301.205.pdf).
- **[TCS-7284](../../data/cards/TCS-7284.json)** (source draft): Is computing an exact Hylland–Zeckhauser market equilibrium FIXP-hard? [Source](https://epubs.siam.org/doi/10.1137/23M157586X).

## 163. Boaz Barak

Average-case computational barriers and metacomplexity.

- **[TCS-6656](../../data/cards/TCS-6656.json)** (formulated card): Can a polynomial-time randomized algorithm distinguish G(n,1/2) from the same graph with a planted clique of size n^{1/2−ε}, for some fixed ε>0? [Source](https://people.math.ethz.ch/~sudakovb/hidden-clique.pdf).
- **[TCS-5501](../../data/cards/TCS-5501.json)** (source draft; status unverified): Is the Minimum Circuit Size Problem NP-hard under deterministic polynomial-time many-one reductions, when a function is given by its full truth table? [Source](https://doi.org/10.4230/LIPIcs.CCC.2023.31).

## 164. David Steurer

The computational-statistical gaps behind sum-of-squares algorithms.

- **[TCS-6657](../../data/cards/TCS-6657.json)** (formulated card): What is the polynomial-time detection threshold for dense tensor PCA in the Gaussian spiked model? [Source](https://arxiv.org/abs/1411.1076).
- **[TCS-7238](../../data/cards/TCS-7238.json)** (formulated card): Can random 3-SAT at a sufficiently large constant clause density be refuted in polynomial time with high probability? [Source](https://www.cs.cmu.edu/~odonnell/papers/random-csp-refutation.pdf).

## 165. Prasad Raghavendra

The conjectures governing the limits of semidefinite approximation.

- **[TCS-0006](../../data/cards/TCS-0006.json)** (formulated card): For every constant completeness and soundness gap, is the corresponding large-alphabet Unique Games promise problem NP-hard? [Source](https://cs.nyu.edu/~khot/papers/UGCSurvey.pdf).
- **[TCS-7160](../../data/cards/TCS-7160.json)** (formulated card): For every fixed ε>0, is distinguishing small sets with expansion at most ε from all comparably small sets having expansion at least 1−ε NP-hard, for a suitable fixed set-size fraction? [Source](https://doi.org/10.1145/1806689.1806792).

## 166. Nisheeth Vishnoi

Polynomial simplex rules and deterministic approximate counting connect continuous optimization to derandomized combinatorial computation.

- **[TCS-6572](../../data/cards/TCS-6572.json)** (formulated card): Does some simplex pivot rule solve every rational linear program in polynomial bit complexity? [Source](https://www.cs.yale.edu/homes/spielman/simplex/).
- **[TCS-6629](../../data/cards/TCS-6629.json)** (formulated card): Does the permanent of a nonnegative rational matrix admit a deterministic FPTAS? [Source](https://doi.org/10.1145/1008731.1008738).

## 167. Amir Yehudayoff

Log-rank and arithmetic branching-program simulation connect communication lower bounds with algebraic computation.

- **[TCS-6603](../../data/cards/TCS-6603.json)** (formulated card): Is deterministic communication complexity of every Boolean matrix polynomially bounded by the logarithm of its real rank? [Source](https://arxiv.org/abs/2510.02583v3).
- **[TCS-6612](../../data/cards/TCS-6612.json)** (formulated card): Is VP_ℂ=VBP_ℂ: can polynomial-size arithmetic circuits of polynomial degree always be replaced by polynomial-size algebraic branching programs? [Source](https://eccc.weizmann.ac.il/report/2025/083/revision/1/download/).

## 168. Ben Rossman

Small-depth circuits and formula composition.

- **[TCS-1053](../../data/cards/TCS-1053.json)** (source draft; status unverified): Is there an explicit Boolean function family requiring depth-three AND/OR circuits of size 2^{ω(√n)}? [Source](https://web.vu.lt/mif/s.jukna/boolean/index.html).
- **[TCS-0017](../../data/cards/TCS-0017.json)** (source draft; status unverified): Is L(g∘f)≥cL(g)L(f) for a universal c>0, where L is Boolean formula size and composition uses disjoint input blocks? [Source](https://www.math.ias.edu/files/mathandcomp.pdf).

## 169. Alexander Sherstov

The pair concerns polynomial representations of computation and the possibility of exponential quantum savings in communication.

- **[TCS-0033](../../data/cards/TCS-0033.json)** (source draft; status unverified): What is the largest separation between quantum query complexity and bounded approximate degree for partial Boolean functions? The polynomial must stay in [0,1] on every Boolean input, including inputs outside the promise. [Source](https://www.scottaaronson.com/papers/open.pdf).
- **[TCS-6450](../../data/cards/TCS-6450.json)** (formulated card): For every total two-party Boolean function, is bounded-error randomized communication polynomially bounded by quantum communication with unlimited shared entanglement? [Source](https://eccc.weizmann.ac.il/report/2026/013/).

## 170. Jan Krajíček

Bounded arithmetic and the structure of propositional proof systems.

- **[TCS-1099](../../data/cards/TCS-1099.json)** (source draft; status unverified): Do there exist integers i>j≥1 for which Buss’s theories T₂^i and T₂^j prove different sentences? [Source](https://arxiv.org/abs/2504.04416).
- **[TCS-7273](../../data/cards/TCS-7273.json)** (formulated card): Is there a disjoint NP pair complete under polynomial-time many-one reductions between disjoint pairs? [Source](https://arxiv.org/abs/1601.01487).

## 171. Toniann Pitassi

Lower bounds for the strongest standard propositional proof systems.

- **[TCS-6601](../../data/cards/TCS-6601.json)** (formulated card): Are some tautologies provable only with superpolynomial-size Extended Frege proofs? [Source](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf).
- **[TCS-0025](../../data/cards/TCS-0025.json)** (formulated card): Are shortest proofs of propositional tautologies in unrestricted Frege systems sometimes superpolynomial in the formula length? [Source](https://www.math.ias.edu/files/Book-online-Aug0619.pdf).

## 172. Samuel Buss

Bounded arithmetic and arithmetic-strength proof systems.

- **[TCS-1098](../../data/cards/TCS-1098.json)** (source draft; status unverified): Can one prove that PV₁ proves no sentence asserting correctness of a polynomial-time SAT decision algorithm? [Source](https://arxiv.org/abs/2504.04416).
- **[TCS-1099](../../data/cards/TCS-1099.json)** (source draft; status unverified): Do there exist integers i>j≥1 for which Buss’s theories T₂^i and T₂^j prove different sentences? [Source](https://arxiv.org/abs/2504.04416).

## 173. Jakob Nordström

Restart-free CDCL and Frege versus Extended Frege ask how practical proof mechanisms and stronger proof systems compare.

- **[TCS-7239](../../data/cards/TCS-7239.json)** (formulated card): Does greedy CDCL without restarts polynomially simulate resolution? [Source](https://jakobnordstrom.se/docs/publications/MV_PhDthesis.pdf).
- **[TCS-6663](../../data/cards/TCS-6663.json)** (formulated card): Does Frege polynomially simulate Extended Frege in proof size? [Source](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf).

## 174. Rahul Santhanam

Circuit lower bounds and algorithms that estimate circuit complexity.

- **[TCS-7161](../../data/cards/TCS-7161.json)** (formulated card): Does NEXP require superpolynomial-size constant-depth threshold circuits? [Source](https://doi.org/10.1109/CCC.2011.36).
- **[TCS-5501](../../data/cards/TCS-5501.json)** (source draft; status unverified): Is the Minimum Circuit Size Problem NP-hard under deterministic polynomial-time many-one reductions, when a function is given by its full truth table? [Source](https://doi.org/10.4230/LIPIcs.CCC.2023.31).

## 175. Manindra Agrawal

Derandomization in computational number theory.

- **[TCS-6614](../../data/cards/TCS-6614.json)** (formulated card): Can univariate polynomials over explicitly represented finite fields be factored deterministically in time polynomial in degree and field-description length? [Source](https://arxiv.org/abs/2509.12705).
- **[TCS-7265](../../data/cards/TCS-7265.json)** (formulated card): Can an n-bit prime be constructed deterministically in polynomial time for every n? [Source](https://eccc.weizmann.ac.il/report/2022/081/).

## 176. Neeraj Kayal

Arithmetic circuit lower bounds and the power of branching programs.

- **[TCS-0010](../../data/cards/TCS-0010.json)** (source draft; status unverified): Is there an explicit family of constant-degree n-variable polynomials requiring ω(n) arithmetic circuit size? The source draft still needs a precise field and explicitness convention. [Source](https://www.math.ias.edu/files/mathandcomp.pdf).
- **[TCS-6612](../../data/cards/TCS-6612.json)** (formulated card): Is VP_ℂ=VBP_ℂ: can polynomial-size arithmetic circuits of polynomial degree always be replaced by polynomial-size algebraic branching programs? [Source](https://eccc.weizmann.ac.il/report/2025/083/revision/1/download/).

## 177. Nitin Saxena

Identity testing and deterministic polynomial factorization.

- **[TCS-7113](../../data/cards/TCS-7113.json)** (source draft): Can identity testing for explicitly given arithmetic circuits be derandomized in polynomial time? The existing source draft still needs its field and degree conventions fixed. [Source](https://arxiv.org/abs/2309.17042).
- **[TCS-6614](../../data/cards/TCS-6614.json)** (formulated card): Can univariate polynomials over explicitly represented finite fields be factored deterministically in time polynomial in degree and field-description length? [Source](https://arxiv.org/abs/2509.12705).

## 178. Amir Shpilka

Derandomization and the formula complexity of algebraic computation.

- **[TCS-7113](../../data/cards/TCS-7113.json)** (source draft): Can identity testing for explicitly given arithmetic circuits be derandomized in polynomial time? The existing source draft still needs its field and degree conventions fixed. [Source](https://arxiv.org/abs/2309.17042).
- **[TCS-6613](../../data/cards/TCS-6613.json)** (formulated card): Does the determinant have polynomial-size arithmetic formulas over ℂ? [Source](https://www.sciencedirect.com/science/article/pii/0020019084900188).

## 179. Shubhangi Saraf

Algebraic lower bounds and local decoding.

- **[TCS-7269](../../data/cards/TCS-7269.json)** (formulated card): Does the permanent require multilinear arithmetic formulas of size 2^{Ω(n)}? [Source](https://eccc.weizmann.ac.il/report/2017/004/).
- **[TCS-1020](../../data/cards/TCS-1020.json)** (source draft; status unverified): Do binary constant-query locally decodable codes exist with polynomial blocklength and a positive constant noise tolerance? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 180. Valentine Kabanets

The pair links derandomization assumptions to the strength of the circuit lower bounds they imply.

- **[TCS-1022](../../data/cards/TCS-1022.json)** (source draft; status unverified): Does deterministic polynomial-time derandomization of promise-BPP imply a language in NEXP requiring circuits of size 2^{n^{Ω(1)}}? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).
- **[TCS-0021](../../data/cards/TCS-0021.json)** (formulated card): Does NP contain a language with no polynomial-size Boolean circuits? [Source](https://www.math.ias.edu/files/mathandcomp.pdf).

## 181. Christopher Umans

Algebraic multiplication algorithms and explicit pseudorandom objects.

- **[TCS-0007](../../data/cards/TCS-0007.json)** (formulated card): Is the exponent of exact matrix multiplication over ℂ equal to two? [Source](https://doi.org/10.1007/BF02165411).
- **[TCS-1013](../../data/cards/TCS-1013.json)** (source draft; status unverified): Can lossless bipartite expanders simultaneously have polylogarithmic left degree D and only O(KD) right vertices for expansion of K-element sets? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 182. Peter Bürgisser

Tensor asymptotics and algebraic lower bounds.

- **[TCS-7262](../../data/cards/TCS-7262.json)** (formulated card): Does every concise tensor in ℂ^n⊗ℂ^n⊗ℂ^n have asymptotic rank n? [Source](https://arxiv.org/abs/2411.15789).
- **[TCS-6666](../../data/cards/TCS-6666.json)** (formulated card): Is the number of integer roots of a univariate integer polynomial polynomially bounded by its constant-free arithmetic straight-line-program length? [Source](https://doi.org/10.1215/S0012-7094-95-08105-8).

## 183. Ketan Mulmuley

Orbit geometry and the central separations of algebraic complexity.

- **[TCS-6611](../../data/cards/TCS-6611.json)** (formulated card): Must any determinant representation of the permanent by affine linear matrix entries have superpolynomial dimension? [Source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2021.4).
- **[TCS-0005](../../data/cards/TCS-0005.json)** (formulated card): Does the permanent have polynomial-size arithmetic circuits over ℂ, equivalently VP_ℂ=VNP_ℂ? [Source](https://www.math.ias.edu/files/mathandcomp.pdf).

## 184. Hendrik Lenstra

Integer programming and deterministic computational number theory.

- **[TCS-7264](../../data/cards/TCS-7264.json)** (formulated card): Can integer programming with n variables be solved in 2^{O(n)} times a polynomial in the input bit length? [Source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol358-ipec2025/html/LIPIcs.IPEC.2025.1/LIPIcs.IPEC.2025.1.html).
- **[TCS-6620](../../data/cards/TCS-6620.json)** (source draft): For every ε>0, is the least quadratic nonresidue modulo a sufficiently large prime p at most p^ε? [Source](https://arxiv.org/abs/1410.7073).

## 185. Arjen Lenstra

Classical factoring and the Boolean circuit cost of multiplication concern the basic arithmetic underlying computational number theory.

- **[TCS-6617](../../data/cards/TCS-6617.json)** (formulated card): Can every integer be factored by a classical randomized polynomial-time algorithm? [Source](https://www.csa.iisc.ac.in/~chandan/research/survey_CNT.pdf).
- **[TCS-7223](../../data/cards/TCS-7223.json)** (formulated card): Can multiplication of two n-bit integers be computed by Boolean circuits with O(n) gates? [Source](https://www.wisdom.weizmann.ac.il/~oded/cc-book.html).

## 186. Eshan Chattopadhyay

Optimal explicit randomness extraction.

- **[TCS-7271](../../data/cards/TCS-7271.json)** (formulated card): Can a deterministic polynomial-time two-source extractor output one constant-error bit from independent n-bit sources each having min-entropy log₂n+O(1)? [Source](https://arxiv.org/abs/2303.06802).
- **[TCS-1016](../../data/cards/TCS-1016.json)** (source draft; status unverified): Can constant-error seeded extractors have seed length log₂n+O(1) while outputting Ω(k) bits from min-entropy k? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 187. Xin Li

Multi-source and seeded extraction near their information-theoretic limits.

- **[TCS-7271](../../data/cards/TCS-7271.json)** (formulated card): Can a deterministic polynomial-time two-source extractor output one constant-error bit from independent n-bit sources each having min-entropy log₂n+O(1)? [Source](https://arxiv.org/abs/2303.06802).
- **[TCS-1015](../../data/cards/TCS-1015.json)** (source draft; status unverified): Can seeded extractors have logarithmic seed length and constant total entropy loss, at constant statistical error? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 188. Ronen Shaltiel

Hardness-based pseudorandomness and structured weak random sources.

- **[TCS-1018](../../data/cards/TCS-1018.json)** (source draft; status unverified): Can hardness-to-randomness generators preserve seed length within a constant factor of the hard function’s input length at optimal polynomial stretch? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).
- **[TCS-1005](../../data/cards/TCS-1005.json)** (source draft; status unverified): Can BPP be simulated deterministically in subexponential time without an unproved hardness assumption? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 189. Anup Rao

Communication rank and tree codes connect the complexity of interaction with its reliable transmission.

- **[TCS-6603](../../data/cards/TCS-6603.json)** (formulated card): Is deterministic communication complexity of every Boolean matrix polynomially bounded by the logarithm of its real rank? [Source](https://arxiv.org/abs/2510.02583v3).
- **[TCS-0013](../../data/cards/TCS-0013.json)** (source draft; status unverified): Do constant-alphabet tree codes with positive constant relative distance admit polynomial-time encoding and decoding? Distance is measured on suffixes after two input histories diverge; the decoding noise convention remains in the source draft. [Source](https://www.math.ias.edu/files/mathandcomp.pdf).

## 190. Gábor Tardos

Beck–Fiala discrepancy and the log-rank conjecture connect combinatorial structure with the complexity of rounding and communication.

- **[TCS-7315](../../data/cards/TCS-7315.json)** (new; formulated card): Does every set system in which each element belongs to at most t sets have discrepancy O(√t), independently of the numbers of sets and elements? [Source](https://arxiv.org/abs/2508.03961).
- **[TCS-6603](../../data/cards/TCS-6603.json)** (formulated card): Is deterministic communication complexity of every Boolean matrix polynomially bounded by the logarithm of its real rank? [Source](https://arxiv.org/abs/2510.02583v3).

## 191. Ryan O’Donnell

Fourier analysis and the geometry of Boolean threshold functions.

- **[TCS-6604](../../data/cards/TCS-6604.json)** (formulated card): Is the Fourier entropy of every Boolean function bounded by a universal constant times its total influence? [Source](https://www.cs.cmu.edu/~jswright/papers/fei.pdf).
- **[TCS-6664](../../data/cards/TCS-6664.json)** (formulated card): For each fixed degree d, is the maximum average sensitivity of an n-variable polynomial threshold function asymptotically at most the symmetric Gotsman–Linial benchmark? [Source](https://arxiv.org/abs/2108.02288).

## 192. Shachar Lovett

Communication rank and the Fourier structure of DNF.

- **[TCS-6603](../../data/cards/TCS-6603.json)** (formulated card): Is deterministic communication complexity of every Boolean matrix polynomially bounded by the logarithm of its real rank? [Source](https://arxiv.org/abs/2510.02583v3).
- **[TCS-6581](../../data/cards/TCS-6581.json)** (formulated card): Does every s-term DNF have a Fourier approximation supported on at most (s/ε)^{O(log(1/ε))} coefficients with squared error at most ε? [Source](https://www.ias.edu/sites/default/files/math/ODonnell_Fourier.pdf).

## 193. Swastik Kopparty

Local decoding and Reed–Solomon list decoding.

- **[TCS-1020](../../data/cards/TCS-1020.json)** (source draft; status unverified): Do binary constant-query locally decodable codes exist with polynomial blocklength and a positive constant noise tolerance? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).
- **[TCS-1011](../../data/cards/TCS-1011.json)** (source draft; status unverified): Can full-length Reed–Solomon codes have polynomial-size lists beyond the Johnson radius at some fixed positive rate? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 194. Atri Rudra

Adversarial Reed–Solomon list decoding and explicit Gilbert–Varshamov codes separate efficient decoding from explicit code construction.

- **[TCS-1337](../../data/cards/TCS-1337.json)** (source draft; status unverified): Does some family of Reed–Solomon evaluation sets admit polynomial-time list decoding beyond the Johnson radius against worst-case adversarial errors? [Source](https://doi.org/10.4230/LIPIcs.ICALP.2026.43).
- **[TCS-6859](../../data/cards/TCS-6859.json)** (source draft): Can binary linear codes meeting the Gilbert–Varshamov bound be constructed deterministically in time polynomial in their own blocklength, without exhaustive search? [Source](https://cse.buffalo.edu/faculty/atri/courses/coding-theory/book/).

## 195. Mary Wootters

Local access to encoded data and the binary rate-distance frontier.

- **[TCS-6609](../../data/cards/TCS-6609.json)** (formulated card): Do constant-rate binary locally decodable codes exist with O(log n) queries and positive constant error tolerance? [Source](https://eccc.weizmann.ac.il/report/2025/168/revision/1/download/).
- **[TCS-7267](../../data/cards/TCS-7267.json)** (formulated card): Do binary codes asymptotically beat the Gilbert–Varshamov rate at some fixed relative distance? [Source](https://cse.buffalo.edu/faculty/atri/courses/coding-theory/book/web-coding-book.pdf).

## 196. Leonard Adleman

The arithmetic assumptions behind RSA and deterministic prime generation.

- **[TCS-7276](../../data/cards/TCS-7276.json)** (source draft): Does polynomial-time average-case RSA inversion with exponent 65537 imply polynomial-time average-case factoring in the atlas’s RSA-modulus distribution? [Source](https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf).
- **[TCS-7265](../../data/cards/TCS-7265.json)** (formulated card): Can an n-bit prime be constructed deterministically in polynomial time for every n? [Source](https://eccc.weizmann.ac.il/report/2022/081/).

## 197. Whitfield Diffie

The weakest basis for key exchange and discrete-logarithm security.

- **[TCS-7229](../../data/cards/TCS-7229.json)** (formulated card): Does existence of classical one-way functions imply classical key agreement in the plain model? [Source](https://eprint.iacr.org/2021/016).
- **[TCS-6618](../../data/cards/TCS-6618.json)** (formulated card): Can discrete logarithms in prime fields be computed by a classical randomized polynomial-time algorithm? [Source](https://www.csa.iisc.ac.in/~chandan/research/survey_CNT.pdf).

## 198. Martin Hellman

Cryptographic inversion and the relationship between RSA and factoring.

- **[TCS-6546](../../data/cards/TCS-6546.json)** (formulated card): Does existence of one-way functions imply existence of full-domain one-way permutations? [Source](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1988/6060.html).
- **[TCS-7276](../../data/cards/TCS-7276.json)** (source draft): Does polynomial-time average-case RSA inversion with exponent 65537 imply polynomial-time average-case factoring in the atlas’s RSA-modulus distribution? [Source](https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf).

## 199. Moni Naor

Minimal assumptions and the information complexity of secret sharing.

- **[TCS-6547](../../data/cards/TCS-6547.json)** (formulated card): Do arbitrary one-way functions imply collision-resistant hash functions in the standard model? [Source](https://www.cs.princeton.edu/courses/archive/spr08/cos598D/Rompel.pdf).
- **[TCS-7275](../../data/cards/TCS-7275.json)** (source draft): Do some n-participant access structures require perfect secret-sharing schemes of size 2^{Ω(n)}, allowing unrestricted nonlinear schemes? [Source](https://eprint.iacr.org/2019/174.pdf).

## 200. Ran Canetti

Security under active attack and composable noninteractive proof primitives.

- **[TCS-6548](../../data/cards/TCS-6548.json)** (formulated card): Does IND-CPA public-key encryption imply IND-CCA2 public-key encryption without extra assumptions or setup? [Source](https://theory.stanford.edu/~trevisan/cs276/projects.html).
- **[TCS-6552](../../data/cards/TCS-6552.json)** (formulated card): Do one-way functions imply reusable adaptive noninteractive zero-knowledge arguments for NP in the common-reference-string model? [Source](https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf).

## 201. Mihir Bellare

The foundations of chosen-ciphertext security and collision resistance.

- **[TCS-6548](../../data/cards/TCS-6548.json)** (formulated card): Does IND-CPA public-key encryption imply IND-CCA2 public-key encryption without extra assumptions or setup? [Source](https://theory.stanford.edu/~trevisan/cs276/projects.html).
- **[TCS-6547](../../data/cards/TCS-6547.json)** (formulated card): Do arbitrary one-way functions imply collision-resistant hash functions in the standard model? [Source](https://www.cs.princeton.edu/courses/archive/spr08/cos598D/Rompel.pdf).

## 202. Phillip Rogaway

The existence of one-way functions and their relation to permutations ask what mathematical foundations symmetric cryptography actually requires.

- **[TCS-7167](../../data/cards/TCS-7167.json)** (formulated card): Do classical one-way functions exist? [Source](https://doi.org/10.1023/A:1023634616182).
- **[TCS-6546](../../data/cards/TCS-6546.json)** (formulated card): Does existence of one-way functions imply existence of full-domain one-way permutations? [Source](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1988/6060.html).

## 203. Victor Shoup

Generic-group and arithmetic assumptions in public-key cryptography.

- **[TCS-6618](../../data/cards/TCS-6618.json)** (formulated card): Can discrete logarithms in prime fields be computed by a classical randomized polynomial-time algorithm? [Source](https://www.csa.iisc.ac.in/~chandan/research/survey_CNT.pdf).
- **[TCS-7276](../../data/cards/TCS-7276.json)** (source draft): Does polynomial-time average-case RSA inversion with exponent 65537 imply polynomial-time average-case factoring in the atlas’s RSA-modulus distribution? [Source](https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf).

## 204. Yuval Ishai

Information complexity of secret sharing and distributed function evaluation.

- **[TCS-7275](../../data/cards/TCS-7275.json)** (source draft): Do some n-participant access structures require perfect secret-sharing schemes of size 2^{Ω(n)}, allowing unrestricted nonlinear schemes? [Source](https://eprint.iacr.org/2019/174.pdf).
- **[TCS-2732](../../data/cards/TCS-2732.json)** (source draft; status unverified): Is there a perfectly secure three-server distributed point function on an N-point domain with N^{o(1)} bits per server key? [Source](https://doi.org/10.4230/LIPIcs.ITC.2022.17).

## 205. Sanjam Garg

The weakest foundations of obfuscation and succinct arguments.

- **[TCS-6550](../../data/cards/TCS-6550.json)** (formulated card): Does ordinary polynomial-hard LWE alone imply indistinguishability obfuscation for all polynomial-size Boolean circuits? [Source](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html).
- **[TCS-7279](../../data/cards/TCS-7279.json)** (source draft): Does LWE alone imply succinct noninteractive arguments for every NP relation? [Source](https://eccc.weizmann.ac.il/report/2026/098/).

## 206. Zvika Brakerski

Homomorphic encryption and lattice-based one-way structure.

- **[TCS-6551](../../data/cards/TCS-6551.json)** (formulated card): Does ordinary LWE alone imply compact, unleveled fully homomorphic encryption without a circular-security assumption? [Source](https://epubs.siam.org/doi/10.1137/120868669).
- **[TCS-7280](../../data/cards/TCS-7280.json)** (source draft): Does ordinary LWE imply one-way permutations? [Source](https://simons.berkeley.edu/open-problems-cryptography-summer-2015).

## 207. Eli Ben-Sasson

PCP parameters and succinct verification of general computations.

- **[TCS-7268](../../data/cards/TCS-7268.json)** (formulated card): Does the sliding-scale PCP conjecture hold with inverse-polynomial soundness, the constant query bound and alphabet dependence specified in the atlas? [Source](https://arxiv.org/abs/1505.06362).
- **[TCS-7279](../../data/cards/TCS-7279.json)** (source draft): Does LWE alone imply succinct noninteractive arguments for every NP relation? [Source](https://eccc.weizmann.ac.il/report/2026/098/).

## 208. Tal Rabin

Threshold information sharing and complete secure-computation primitives.

- **[TCS-7275](../../data/cards/TCS-7275.json)** (source draft): Do some n-participant access structures require perfect secret-sharing schemes of size 2^{Ω(n)}, allowing unrestricted nonlinear schemes? [Source](https://eprint.iacr.org/2019/174.pdf).
- **[TCS-6549](../../data/cards/TCS-6549.json)** (formulated card): Does public-key encryption imply oblivious transfer secure against a semi-honest corruption of either participant? [Source](https://vmahesh.cs.illinois.edu/papers/focs00.pdf).

## 209. Tal Malkin

The assumption hierarchy for secure computation and key agreement.

- **[TCS-6549](../../data/cards/TCS-6549.json)** (formulated card): Does public-key encryption imply oblivious transfer secure against a semi-honest corruption of either participant? [Source](https://vmahesh.cs.illinois.edu/papers/focs00.pdf).
- **[TCS-7274](../../data/cards/TCS-7274.json)** (formulated card): Does existence of arbitrary one-way functions imply existence of one-way functions computable in NC⁰? [Source](https://doi.org/10.1137/S0097539705446950).

## 210. Xiaoyun Wang

Collision-resistant hashing and a worst-case foundation for noisy parity both concern the strength and justification of cryptographic hardness.

- **[TCS-6547](../../data/cards/TCS-6547.json)** (formulated card): Do arbitrary one-way functions imply collision-resistant hash functions in the standard model? [Source](https://www.cs.princeton.edu/courses/archive/spr08/cos598D/Rompel.pdf).
- **[TCS-6454](../../data/cards/TCS-6454.json)** (formulated card): Does worst-case hardness of binary Nearest Codeword imply average-case hardness of low-noise LPN at the atlas’s specified polynomial sample and noise parameters? [Source](https://eccc.weizmann.ac.il/report/2026/095/).

## 211. Yevgeniy Dodis

Extracting usable randomness from imperfect sources.

- **[TCS-1015](../../data/cards/TCS-1015.json)** (source draft; status unverified): Can seeded extractors have logarithmic seed length and constant total entropy loss, at constant statistical error? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).
- **[TCS-1024](../../data/cards/TCS-1024.json)** (source draft; status unverified): Can deterministic extraction handle circuit-samplable sources below half entropy under a precisely stated hardness assumption? The current source draft does not yet fix that assumption. [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 212. Rafail Ostrovsky

Private access to outsourced data and the inherent overhead of oblivious memory.

- **[TCS-7323](../../data/cards/TCS-7323.json)** (new; source draft): Do arbitrary one-way functions suffice for sublinear-communication single-server private information retrieval without a database-dependent client hint? The joint security and communication parameters remain to be specified. [Source](https://www.iacr.org/archive/eurocrypt2000/1807/18070122-new.pdf).
- **[TCS-7324](../../data/cards/TCS-7324.json)** (new; source draft): Is logarithmic bandwidth overhead unavoidable for offline ORAM with unrestricted data encoding and constant client storage? The exact word-size, memory and security parameters remain to be specified. [Source](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/oram_lower.pdf).

## 213. Amit Sahai

Obfuscation and noninteractive zero knowledge from weak assumptions.

- **[TCS-6550](../../data/cards/TCS-6550.json)** (formulated card): Does ordinary polynomial-hard LWE alone imply indistinguishability obfuscation for all polynomial-size Boolean circuits? [Source](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html).
- **[TCS-6552](../../data/cards/TCS-6552.json)** (formulated card): Do one-way functions imply reusable adaptive noninteractive zero-knowledge arguments for NP in the common-reference-string model? [Source](https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf).

## 214. Brent Waters

The assumption hierarchy for advanced public-key encryption.

- **[TCS-7278](../../data/cards/TCS-7278.json)** (source draft): Does arbitrary public-key encryption imply identity-based encryption? [Source](https://eprint.iacr.org/2021/745.pdf).
- **[TCS-7277](../../data/cards/TCS-7277.json)** (source draft): Does arbitrary public-key encryption imply compact fully homomorphic encryption? [Source](https://eprint.iacr.org/2015/815.pdf).

## 215. Chris Peikert

Unleveled FHE and one-way permutations from LWE ask which cryptographic capabilities follow from the lattice assumption alone.

- **[TCS-6551](../../data/cards/TCS-6551.json)** (formulated card): Does ordinary LWE alone imply compact, unleveled fully homomorphic encryption without a circular-security assumption? [Source](https://epubs.siam.org/doi/10.1137/120868669).
- **[TCS-7280](../../data/cards/TCS-7280.json)** (source draft): Does ordinary LWE imply one-way permutations? [Source](https://simons.berkeley.edu/open-problems-cryptography-summer-2015).

## 216. Daniele Micciancio

Exact SVP with limited space and polynomial-factor approximation are two central algorithmic barriers for Euclidean lattices.

- **[TCS-6619](../../data/cards/TCS-6619.json)** (formulated card): Can exact Euclidean shortest vectors be found in 2^{O(n)} time using only polynomial space? [Source](https://eccc.weizmann.ac.il/report/2010/014/).
- **[TCS-6667](../../data/cards/TCS-6667.json)** (formulated card): Can Euclidean SVP be approximated within a polynomial factor in the lattice dimension in classical polynomial time? [Source](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Lovasz/LovaszLenstraLenstrafactor.pdf).

## 217. Elette Boyle

Distributed point functions and general secret-sharing complexity.

- **[TCS-2732](../../data/cards/TCS-2732.json)** (source draft; status unverified): Is there a perfectly secure three-server distributed point function on an N-point domain with N^{o(1)} bits per server key? [Source](https://doi.org/10.4230/LIPIcs.ITC.2022.17).
- **[TCS-7275](../../data/cards/TCS-7275.json)** (source draft): Do some n-participant access structures require perfect secret-sharing schemes of size 2^{Ω(n)}, allowing unrestricted nonlinear schemes? [Source](https://eprint.iacr.org/2019/174.pdf).

## 218. Michael Kearns

Noise-tolerant learning and the limits of efficient PAC learning.

- **[TCS-6542](../../data/cards/TCS-6542.json)** (formulated card): Can an arbitrary parity on n bits be learned in polynomial time from uniform examples corrupted by any fixed noise rate below one half? [Source](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/2003-Noise-Tolerant_Learning.pdf).
- **[TCS-5358](../../data/cards/TCS-5358.json)** (formulated card): Can polynomial-size DNF formulas be PAC learned in polynomial time from random labeled examples under every input distribution? [Source](https://proceedings.mlr.press/v23/feldman12b.html).

## 219. Yoav Freund

Fourier concentration of DNF and uniform-distribution decision-tree learning connect structural approximation with efficient learning.

- **[TCS-6581](../../data/cards/TCS-6581.json)** (formulated card): Does every s-term DNF have a Fourier approximation supported on at most (s/ε)^{O(log(1/ε))} coefficients with squared error at most ε? [Source](https://www.ias.edu/sites/default/files/math/ODonnell_Fourier.pdf).
- **[TCS-7294](../../data/cards/TCS-7294.json)** (formulated card): Can size-s decision trees be learned from uniform random examples in poly(n,s,1/ε) time? [Source](https://arxiv.org/abs/0812.0933).

## 220. Shai Ben-David

Sample compression and teaching dimension ask whether fundamental learning complexity has equally economical combinatorial explanations.

- **[TCS-6541](../../data/cards/TCS-6541.json)** (formulated card): Does every Boolean class of VC dimension d have a labeled sample compression scheme using O(d) examples and side-information bits? [Source](https://arxiv.org/abs/1503.06960v2).
- **[TCS-0691](../../data/cards/TCS-0691.json)** (source draft; status unverified): Is recursive teaching dimension at most C times VC dimension for every finite concept class, for a universal constant C? [Source](https://proceedings.mlr.press/v40/Simon15b.html).

## 221. Sanjoy Dasgupta

Hierarchical clustering and metric k-Median are two central, explicitly defined clustering objectives with unresolved approximation thresholds.

- **[TCS-7318](../../data/cards/TCS-7318.json)** (new; formulated card): Does Dasgupta’s graph-based hierarchical clustering cost admit a deterministic polynomial-time constant-factor approximation on arbitrary nonnegatively weighted graphs? [Source](https://arxiv.org/abs/1510.05043).
- **[TCS-6659](../../data/cards/TCS-6659.json)** (formulated card): Does metric k-Median admit polynomial-time approximation ratio 1+2/e+ε for every constant ε>0? [Source](https://people.idsia.ch/~grandoni/Pubblicazioni/CGLSS25stoc.pdf).

## 222. Nati Srebro

Entrywise low-rank approximation and information-efficient proper learning connect representation constraints with statistical guarantees.

- **[TCS-7298](../../data/cards/TCS-7298.json)** (source draft): Does entrywise ℓ₁ rank-k approximation admit a polynomial-time approximation factor independent of k when k is part of the input? [Source](https://epubs.siam.org/doi/10.1137/1.9781611975482.47).
- **[TCS-0679](../../data/cards/TCS-0679.json)** (source draft; status unverified): Does every VC-dimension-d binary class admit a proper agnostic learner with O(d) conditional mutual information and O(√(d/n)) expected empirical excess loss? [Source](https://proceedings.mlr.press/v125/steinke20b.html).

## 223. Sham Kakade

Efficient reinforcement learning with function approximation.

- **[TCS-7325](../../data/cards/TCS-7325.json)** (new; source draft): Can stochastic-transition linear Bellman-complete MDPs be learned with polynomial sample and computational complexity in d, H, A and 1/ε, without an exploration oracle? Representation and arithmetic conventions remain to be specified. [Source](https://arxiv.org/abs/2603.23461).
- **[TCS-0708](../../data/cards/TCS-0708.json)** (source draft; status unverified): What is the minimax regret in horizon H and episode count T for kernel-based episodic MDPs satisfying the source’s RKHS transition assumption? [Source](https://proceedings.mlr.press/v247/vakili24a.html).

## 224. Elad Hazan

Simultaneous scoring-rule regret and calibration ask what one predictor can guarantee under multiple measures of sequential performance.

- **[TCS-1529](../../data/cards/TCS-1529.json)** (source draft; status unverified): Is there one online probabilistic forecaster with optimal regret simultaneously for every bounded proper scoring rule, up to a universal constant? [Source](https://proceedings.mlr.press/v336/frongillo26a.html).
- **[TCS-7319](../../data/cards/TCS-7319.json)** (new; formulated card): What is the minimax expected ℓ₁ calibration error after T sequential binary forecasts against an adaptive adversary that does not observe the current forecast? [Source](https://arxiv.org/abs/2406.13668).

## 225. Sébastien Bubeck

High-dimensional online geometry and randomized service problems.

- **[TCS-6576](../../data/cards/TCS-6576.json)** (source draft): What is the optimal dimension dependence of the competitive ratio for online convex body chasing? [Source](https://theory.epfl.ch/WinterSchool2025/slides/2025/Gupta_lec4-chasing.pdf).
- **[TCS-7317](../../data/cards/TCS-7317.json)** (new; formulated card): Does randomized k-server on every finite metric admit a polylog(k)-competitive strategy against an oblivious adversary, with no dependence on the number of metric points? [Source](https://arxiv.org/abs/2605.01497).

## 226. Nicolò Cesa-Bianchi

Sequential prediction and partial-information learning.

- **[TCS-0711](../../data/cards/TCS-0711.json)** (source draft; status unverified): Can contextual bandits simultaneously achieve regret O(√(KT(log|Π_m|+log m))) to every class in an arbitrary nested sequence Π₁⊂⋯⊂Π_M? [Source](https://proceedings.mlr.press/v125/foster20a.html).
- **[TCS-6577](../../data/cards/TCS-6577.json)** (formulated card): What is the minimax joint dependence on dimension d and horizon T of regret in adversarial bandit convex optimization? [Source](https://tor-lattimore.com/downloads/cvx-book/cvx.pdf).

## 227. Gábor Lugosi

Sparse robust estimation and the KLS conjecture connect high-dimensional statistics with concentration and functional inequalities.

- **[TCS-7296](../../data/cards/TCS-7296.json)** (source draft): Can sparse Gaussian means be estimated robustly in polynomial time at the information-theoretically optimal sample size? [Source](https://proceedings.mlr.press/v178/diakonikolas22e.html).
- **[TCS-6523](../../data/cards/TCS-6523.json)** (formulated card): Does every isotropic log-concave measure have a Poincaré constant bounded independently of dimension, as conjectured by Kannan, Lovász and Simonovits? [Source](https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/).

## 228. Maria-Florina Balcan

Hierarchical clustering and learning intersections of halfspaces connect data organization with computational learnability.

- **[TCS-7318](../../data/cards/TCS-7318.json)** (new; formulated card): Does Dasgupta’s graph-based hierarchical clustering cost admit a deterministic polynomial-time constant-factor approximation on arbitrary nonnegatively weighted graphs? [Source](https://arxiv.org/abs/1510.05043).
- **[TCS-7293](../../data/cards/TCS-7293.json)** (source draft): Can intersections of two arbitrary halfspaces be PAC learned, possibly improperly, in polynomial time under every input distribution? [Source](https://web.cs.ucla.edu/~sherstov/pdf/hshs.pdf).

## 229. Adam Klivans

Efficient learning of structured Boolean functions.

- **[TCS-6543](../../data/cards/TCS-6543.json)** (formulated card): Can every k-junta on n Boolean variables be learned from uniform examples in time polynomial in n, 2^k and 1/ε? [Source](https://www.cs.cmu.edu/~odonnell/papers/juntas.pdf).
- **[TCS-0677](../../data/cards/TCS-0677.json)** (source draft; status unverified): Can every size-s decision tree be properly PAC learned in poly(n,s,1/ε) time, with a polynomial-size decision tree as the output hypothesis? [Source](https://proceedings.mlr.press/v178/open-problem-blanc22a.html).

## 230. Vitaly Feldman

Private sample complexity and efficient marginal release concern the statistical and computational price of privacy.

- **[TCS-0506](../../data/cards/TCS-0506.json)** (formulated card): Can every finite Boolean class be privately PAC learned with sample complexity polynomial in its VC dimension and the iterated logarithm of its Littlestone dimension? [Source](https://proceedings.mlr.press/v336/nissim26a.html).
- **[TCS-7236](../../data/cards/TCS-7236.json)** (formulated card): Can all Boolean marginals be released privately in polynomial time from a database whose size is polynomial in the number of attributes and inverse accuracy? [Source](https://projects.iq.harvard.edu/files/privacytools/files/complexityprivacy_1_01.pdf).

## 231. Gautam Kamath

Robust high-dimensional estimation and private data analysis.

- **[TCS-7296](../../data/cards/TCS-7296.json)** (source draft): Can sparse Gaussian means be estimated robustly in polynomial time at the information-theoretically optimal sample size? [Source](https://proceedings.mlr.press/v178/diakonikolas22e.html).
- **[TCS-7236](../../data/cards/TCS-7236.json)** (formulated card): Can all Boolean marginals be released privately in polynomial time from a database whose size is polynomial in the number of attributes and inverse accuracy? [Source](https://projects.iq.harvard.edu/files/privacytools/files/complexityprivacy_1_01.pdf).

## 232. Jerry Li

Gaussian-mixture density estimation and tensor decomposition under Kruskal’s condition ask when statistical identifiability yields efficient algorithms.

- **[TCS-7295](../../data/cards/TCS-7295.json)** (source draft): Can arbitrary k-component Gaussian mixtures be density-estimated in total variation in time polynomial in dimension, k and inverse accuracy? [Source](https://people.csail.mit.edu/moitra/docs/mv.pdf).
- **[TCS-0054](../../data/cards/TCS-0054.json)** (source draft; status unverified): Can an order-three tensor be decomposed in polynomial time whenever its rank-R factor matrices have Kruskal ranks k_A+k_B+k_C≥2R+2? This is the full uniqueness promise, not an assumption of randomly chosen factors. [Source](https://proceedings.mlr.press/v35/bhaskara14b.html).

## 233. Kobbi Nissim

Private PAC sample complexity and continual counting ask how much accuracy must be lost when statistical outputs protect individuals.

- **[TCS-0506](../../data/cards/TCS-0506.json)** (formulated card): Can every finite Boolean class be privately PAC learned with sample complexity polynomial in its VC dimension and the iterated logarithm of its Littlestone dimension? [Source](https://proceedings.mlr.press/v336/nissim26a.html).
- **[TCS-6673](../../data/cards/TCS-6673.json)** (formulated card): What is the optimal worst-case error of pure-DP continual release of prefix counts as a function of stream length and privacy level? [Source](https://arxiv.org/abs/2607.00876v2).

## 234. Adam Smith

Private stochastic prediction and private marginal release connect sequential statistical estimation with simultaneous data analysis.

- **[TCS-0507](../../data/cards/TCS-0507.json)** (source draft; status unverified): What is the optimal gap-dependent expected pseudo-regret for pure-DP stochastic full-information prediction, as a joint function of action count K, horizon T, privacy ε and smallest positive mean-loss gap Δ? [Source](https://proceedings.mlr.press/v247/hu24a.html).
- **[TCS-7236](../../data/cards/TCS-7236.json)** (formulated card): Can all Boolean marginals be released privately in polynomial time from a database whose size is polynomial in the number of attributes and inverse accuracy? [Source](https://projects.iq.harvard.edu/files/privacytools/files/complexityprivacy_1_01.pdf).

## 235. Frank McSherry

Private continual counting and efficient marginal release address the accuracy and computational cost of processing large private datasets.

- **[TCS-6673](../../data/cards/TCS-6673.json)** (formulated card): What is the optimal worst-case error of pure-DP continual release of prefix counts as a function of stream length and privacy level? [Source](https://arxiv.org/abs/2607.00876v2).
- **[TCS-7236](../../data/cards/TCS-7236.json)** (formulated card): Can all Boolean marginals be released privately in polynomial time from a database whose size is polynomial in the number of attributes and inverse accuracy? [Source](https://projects.iq.harvard.edu/files/privacytools/files/complexityprivacy_1_01.pdf).

## 236. Santosh Vempala

Convex-body geometry and the complexity of polyhedral representations.

- **[TCS-6523](../../data/cards/TCS-6523.json)** (formulated card): Does every isotropic log-concave measure have a Poincaré constant bounded independently of dimension, as conjectured by Kannan, Lovász and Simonovits? [Source](https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/).
- **[TCS-7240](../../data/cards/TCS-7240.json)** (formulated card): Can all vertices of a rational polytope given by inequalities be enumerated in output-polynomial time? [Source](https://arxiv.org/abs/1404.5584v2).

## 237. Alistair Sinclair

Counting perfect matchings and sampling graph colourings are central barriers in approximate counting and Markov-chain computation.

- **[TCS-6628](../../data/cards/TCS-6628.json)** (formulated card): Does counting perfect matchings in general graphs admit an FPRAS? [Source](https://doi.org/10.1137/0218077).
- **[TCS-6621](../../data/cards/TCS-6621.json)** (formulated card): Does single-site Glauber dynamics for proper q-colourings mix in polynomial time for every graph whenever q≥Δ+2? [Source](https://arxiv.org/abs/2010.16158).

## 238. Martin Dyer

The log-supermodular counting boundary and deterministic DNF counting address classification and derandomization of approximate counting.

- **[TCS-7320](../../data/cards/TCS-7320.json)** (new; formulated card): Is approximate counting for every fixed finite family of nonnegative rational Boolean log-supermodular constraints approximation-preserving reducible to #BIS? [Source](https://drops.dagstuhl.de/storage/02dagstuhl-follow-ups/dfu-vol007/DFU.Vol7.15301.205/DFU.Vol7.15301.205.pdf).
- **[TCS-1004](../../data/cards/TCS-1004.json)** (source draft; status unverified): Does counting the satisfying assignments of a DNF admit a deterministic fully polynomial relative-approximation scheme? [Source](https://people.seas.harvard.edu/~salil/pseudorandomness/).

## 239. Leslie Ann Goldberg

Approximation-preserving complexity of counting graph structures.

- **[TCS-7221](../../data/cards/TCS-7221.json)** (formulated card): Does counting independent sets in bipartite graphs admit an FPRAS? [Source](https://link.springer.com/article/10.1007/s00453-019-00606-4).
- **[TCS-6671](../../data/cards/TCS-6671.json)** (source draft): Does counting Euler tours of undirected graphs admit an FPRAS? [Source](https://sites.cs.st-andrews.ac.uk/scm2024/abstracts.html).

## 240. Eric Vigoda

Sampling graph colorings and perfect matchings.

- **[TCS-6621](../../data/cards/TCS-6621.json)** (formulated card): Does single-site Glauber dynamics for proper q-colourings mix in polynomial time for every graph whenever q≥Δ+2? [Source](https://arxiv.org/abs/2010.16158).
- **[TCS-6628](../../data/cards/TCS-6628.json)** (formulated card): Does counting perfect matchings in general graphs admit an FPRAS? [Source](https://doi.org/10.1137/0218077).

## 241. Dana Randall

Critical Ising mixing and the KLS conjecture connect high-dimensional sampling with the geometry and phase transitions of probability measures.

- **[TCS-6668](../../data/cards/TCS-6668.json)** (source draft): Does Glauber dynamics for the zero-field three-dimensional Ising model at critical temperature mix in polynomial time in the side length? [Source](https://arxiv.org/abs/2202.02301).
- **[TCS-6523](../../data/cards/TCS-6523.json)** (formulated card): Does every isotropic log-concave measure have a Poincaré constant bounded independently of dimension, as conjectured by Kannan, Lovász and Simonovits? [Source](https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/).

## 242. Bernhard Haeupler

Network coding and reliable interactive communication.

- **[TCS-6584](../../data/cards/TCS-6584.json)** (formulated card): Can network coding ever increase achievable multiple-unicast rates over fractional routing in an undirected capacitated network? [Source](https://ics.uci.edu/~vazirani/isit.pdf).
- **[TCS-0013](../../data/cards/TCS-0013.json)** (source draft; status unverified): Do constant-alphabet tree codes with positive constant relative distance admit polynomial-time encoding and decoding? Distance is measured on suffixes after two input histories diverge; the decoding noise convention remains in the source draft. [Source](https://www.math.ias.edu/files/mathandcomp.pdf).

## 243. Fabian Kuhn

Distributed lower bounds and local randomized algorithms.

- **[TCS-6557](../../data/cards/TCS-6557.json)** (formulated card): Does an explicit polynomial-time graph predicate require ω(1) deterministic rounds in the unicast congested clique? [Source](https://people.csail.mit.edu/andyd/cong_clique_podc14.pdf).
- **[TCS-6554](../../data/cards/TCS-6554.json)** (formulated card): Can the distributed Lovász Local Lemma be solved in O(log log n) randomized LOCAL rounds under a fixed polynomial slack condition and bounded dependency degree? [Source](https://arxiv.org/abs/1705.04840).

## 244. Mohsen Ghaffari

The LOCAL and massively parallel complexity of symmetry breaking.

- **[TCS-6499](../../data/cards/TCS-6499.json)** (formulated card): Can randomized LOCAL algorithms find a maximal independent set on every n-vertex graph in o(log n) rounds with high probability? [Source](https://arxiv.org/abs/2505.15652).
- **[TCS-6505](../../data/cards/TCS-6505.json)** (formulated card): Must distinguishing one long cycle from two equal-length cycles take Ω(log n) rounds in low-memory MPC? [Source](https://doi.org/10.4230/LIPIcs.ICDT.2025.7).

## 245. Baruch Awerbuch

Deterministic symmetry breaking and CONGEST triangle detection measure the cost of network-wide coordination under different communication constraints.

- **[TCS-6506](../../data/cards/TCS-6506.json)** (formulated card): Can deterministic LOCAL algorithms find an MIS on every n-vertex graph in O(log n) rounds? [Source](https://arxiv.org/abs/2410.19516).
- **[TCS-2997](../../data/cards/TCS-2997.json)** (formulated card): What is the optimal randomized round complexity of triangle detection in CONGEST on arbitrary n-vertex networks? [Source](https://adga-workshop.org/2025/keren.pdf).

## 246. Hagit Attiya

The power of shared-memory primitives and consensus communication.

- **[TCS-7304](../../data/cards/TCS-7304.json)** (source draft): Can combining deterministic shared-object types increase their wait-free consensus power beyond the maximum power of the separate types? [Source](https://perso.telecom-paristech.fr/kuznetso/EFREI18-old/book.pdf).
- **[TCS-7303](../../data/cards/TCS-7303.json)** (source draft): Can asynchronous crash consensus tolerate every t<n/2 failures with O(n²) expected messages against a strong adaptive adversary? [Source](https://link.springer.com/article/10.1007/s00446-017-0315-1).

## 247. Faith Ellen

Consensus hierarchies and the computational strength of queues.

- **[TCS-3416](../../data/cards/TCS-3416.json)** (source draft; status unverified): Can a wait-free linearizable queue be implemented using only objects of consensus number two, for arbitrarily many processes? [Source](https://doi.org/10.4230/LIPIcs.OPODIS.2020.13).
- **[TCS-7304](../../data/cards/TCS-7304.json)** (source draft): Can combining deterministic shared-object types increase their wait-free consensus power beyond the maximum power of the separate types? [Source](https://perso.telecom-paristech.fr/kuznetso/EFREI18-old/book.pdf).

## 248. Nir Shavit

Wait-free queue implementation and robustness of consensus numbers concern the computational strength of shared objects, closely connected to topological solvability.

- **[TCS-3416](../../data/cards/TCS-3416.json)** (source draft; status unverified): Can a wait-free linearizable queue be implemented using only objects of consensus number two, for arbitrarily many processes? [Source](https://doi.org/10.4230/LIPIcs.OPODIS.2020.13).
- **[TCS-7304](../../data/cards/TCS-7304.json)** (source draft): Can combining deterministic shared-object types increase their wait-free consensus power beyond the maximum power of the separate types? [Source](https://perso.telecom-paristech.fr/kuznetso/EFREI18-old/book.pdf).

## 249. Valerie King

Byzantine agreement and dynamic graph connectivity.

- **[TCS-7302](../../data/cards/TCS-7302.json)** (source draft): Can perfectly secure asynchronous Byzantine agreement achieve Õ(n²) expected communicated bits while tolerating every t<n/3 Byzantine faults? [Source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.DISC.2025.1).
- **[TCS-6625](../../data/cards/TCS-6625.json)** (formulated card): Can fully dynamic graph connectivity be maintained deterministically with polylogarithmic worst-case update and query times? [Source](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf).

## 250. Jelani Nelson

Optimal deterministic restricted-isometry matrices and optimal sparse-recovery decoding distinguish measurement design from efficient reconstruction.

- **[TCS-6662](../../data/cards/TCS-6662.json)** (formulated card): Can restricted-isometry matrices with m=O(k log(n/k)) rows be constructed deterministically in polynomial time at constant distortion? [Source](https://www.sciencedirect.com/science/article/pii/S0024379525003143).
- **[TCS-0984](../../data/cards/TCS-0984.json)** (source draft; status unverified): Can deterministic ℓ₂/ℓ₁ sparse recovery achieve O(k log(n/k)) measurements and O(n polylog n) decoding time with a universal constant approximation guarantee? [Source](https://sublinear.info/index.php?title=Open_Problems:24).

## 251. Sofya Raskhodnikova

Sublinear testing of structural properties of functions.

- **[TCS-1033](../../data/cards/TCS-1033.json)** (formulated card): Does polynomial-query testability of a dense graph property imply polynomial-query additive estimation of its distance from that property? [Source](https://epubs.siam.org/doi/10.1137/060652324).
- **[TCS-0848](../../data/cards/TCS-0848.json)** (source draft; status unverified): Can submodularity of a real-valued function on {0,1}^n be tested with poly(n,1/ε) value queries, using distance defined by the fraction of function values that must change? [Source](https://sublinear.info/index.php?title=Open_Problems:37).

## 252. Edith Cohen

Hypergraph cut sparsifiers and Earth Mover Distance sketches ask how much information can be retained in small summaries.

- **[TCS-0946](../../data/cards/TCS-0946.json)** (source draft; status unverified): Does every weighted n-vertex hypergraph have a (1±ε) cut sparsifier with O(n/ε²) hyperedges, with no extra logarithmic factor? [Source](https://sublinear.info/index.php?title=Open_Problems:91).
- **[TCS-0973](../../data/cards/TCS-0973.json)** (source draft; status unverified): Can planar Earth Mover Distance between two equal-cardinality subsets of [n]² be approximated within a constant factor using polylog(n)-bit randomized sketches? [Source](https://sublinear.info/index.php?title=Open_Problems:49).

## 253. Sepehr Assadi

Streaming reachability and the MPC cycle distinction expose communication barriers behind graph processing with limited local memory.

- **[TCS-6556](../../data/cards/TCS-6556.json)** (formulated card): Can directed reachability be decided with near-linear streaming memory and polylogarithmically many passes over an adversarially ordered edge stream? [Source](https://par.nsf.gov/servlets/purl/10488812).
- **[TCS-6505](../../data/cards/TCS-6505.json)** (formulated card): Must distinguishing one long cycle from two equal-length cycles take Ω(log n) rounds in low-memory MPC? [Source](https://doi.org/10.4230/LIPIcs.ICDT.2025.7).

## 254. Lov Grover

The largest possible quantum query advantages and their space costs.

- **[TCS-0029](../../data/cards/TCS-0029.json)** (source draft; status unverified): What is the largest possible separation between bounded-error randomized and quantum query complexity for total Boolean functions? [Source](https://www.scottaaronson.com/papers/open.pdf).
- **[TCS-0034](../../data/cards/TCS-0034.json)** (source draft; status unverified): What is the optimal quantum query–space tradeoff for collision detection and element distinctness, accounting separately for quantum memory and classically stored data accessible in superposition? [Source](https://www.scottaaronson.com/papers/open.pdf).

## 255. Andris Ambainis

Quantum queries, approximation polynomials and classical simulation barriers.

- **[TCS-0033](../../data/cards/TCS-0033.json)** (source draft; status unverified): What is the largest separation between quantum query complexity and bounded approximate degree for partial Boolean functions? The polynomial must stay in [0,1] on every Boolean input, including inputs outside the promise. [Source](https://www.scottaaronson.com/papers/open.pdf).
- **[TCS-6605](../../data/cards/TCS-6605.json)** (formulated card): Must every bounded low-degree real polynomial on the Boolean cube with non-negligible variance have a variable of polynomially large influence? [Source](https://arxiv.org/abs/0911.0996).

## 256. John Watrous

Quantum proof systems and interactive game complexity.

- **[TCS-6448](../../data/cards/TCS-6448.json)** (formulated card): Is QMA=QCMA: can a classical witness replace a quantum witness for every polynomial-time quantum verification problem? [Source](https://eccc.weizmann.ac.il/report/2026/020/).
- **[TCS-0862](../../data/cards/TCS-0862.json)** (source draft; status unverified): Are constant-round quantum refereed games decidable in polynomial space? [Source](https://tcsopenproblems.com/problem/13).

## 257. Ronald de Wolf

Quantum communication and the value of quantum advice.

- **[TCS-6450](../../data/cards/TCS-6450.json)** (formulated card): For every total two-party Boolean function, is bounded-error randomized communication polynomially bounded by quantum communication with unlimited shared entanglement? [Source](https://eccc.weizmann.ac.il/report/2026/013/).
- **[TCS-6449](../../data/cards/TCS-6449.json)** (formulated card): Is BQP/qpoly=BQP/poly: can polynomial classical advice always replace polynomial quantum advice? [Source](https://eccc.weizmann.ac.il/report/2026/020/).

## 258. Richard Jozsa

The border between classically simulable and hard quantum processes.

- **[TCS-7299](../../data/cards/TCS-7299.json)** (source draft): Is multiplicatively approximating the squared permanent of a typical complex Gaussian matrix #P-hard in the average-case reduction sense required for boson sampling? [Source](https://arxiv.org/abs/1011.3245).
- **[TCS-7300](../../data/cards/TCS-7300.json)** (source draft): Can every polynomially gapped local stoquastic adiabatic computation be simulated by a classical randomized polynomial-time algorithm? [Source](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.125.170504).

## 259. David Deutsch

The fundamental computational power and limits of quantum computation.

- **[TCS-0036](../../data/cards/TCS-0036.json)** (formulated card): Is BQP strictly larger than BPP: is there a total decision problem with a quantum polynomial-time algorithm but no classical randomized polynomial-time algorithm? [Source](https://www.math.ias.edu/files/mathandcomp.pdf).
- **[TCS-0037](../../data/cards/TCS-0037.json)** (formulated card): Is NP outside BQP: does SAT have no bounded-error quantum polynomial-time algorithm? [Source](https://www.math.ias.edu/files/mathandcomp.pdf).

## 260. Aram Harrow

Entanglement, many-body structure and quantum proof complexity.

- **[TCS-6516](../../data/cards/TCS-6516.json)** (formulated card): Does every uniformly gapped local Hamiltonian with a unique ground state on a two-dimensional lattice obey an entanglement entropy area law? [Source](https://arxiv.org/abs/0705.2024v4).
- **[TCS-0861](../../data/cards/TCS-0861.json)** (source draft; status unverified): Is QMA(2), with two unentangled quantum witnesses, contained in bounded-error quantum exponential time? [Source](https://tcsopenproblems.com/problem/9).

## 261. Fernando Brandão

Quantum constraint satisfaction and the structure of entanglement.

- **[TCS-6446](../../data/cards/TCS-6446.json)** (formulated card): Is approximating the ground energy of bounded-locality Hamiltonians within a constant additive gap QMA-hard, when the Hamiltonian is normalized by its number of terms? [Source](https://arxiv.org/abs/1309.7495).
- **[TCS-6518](../../data/cards/TCS-6518.json)** (formulated card): Does a bipartite state with negative partial transpose exist from which no entanglement can be distilled, even using arbitrarily many copies? [Source](https://arxiv.org/abs/quant-ph/9801069).

## 262. Henry Yuen

Undecidability phenomena and efficient quantum verification.

- **[TCS-6520](../../data/cards/TCS-6520.json)** (formulated card): Is the unassisted quantum capacity of every effectively described finite-dimensional quantum channel computable to arbitrary additive accuracy? [Source](https://arxiv.org/abs/quant-ph/0304127).
- **[TCS-6447](../../data/cards/TCS-6447.json)** (formulated card): Does every QMA promise problem admit a constant-round strong quantum interactive oracle proof with polynomial communication and O(1) queries? [Source](https://arxiv.org/abs/2601.12874).

## 263. Jeffrey Ullman

The expressive and enumeration complexity of database queries.

- **[TCS-0492](../../data/cards/TCS-0492.json)** (formulated card): Is containment of conjunctive queries under bag semantics decidable over all finite bag databases? [Source](https://a3nm.net/work/research/questions/#decidability-of-conjunctive-query-containment-under-bag-semantics).
- **[TCS-6645](../../data/cards/TCS-6645.json)** (formulated card): Does the conjectured full structural classification of conjunctive queries permitting linear preprocessing and constant-delay enumeration hold? [Source](https://arxiv.org/abs/2206.04988).

## 264. Ronald Fagin

Logical characterizations of complexity classes.

- **[TCS-7232](../../data/cards/TCS-7232.json)** (formulated card): Are spectra of first-order sentences closed under complementation? [Source](https://arxiv.org/abs/0907.5495).
- **[TCS-7195](../../data/cards/TCS-7195.json)** (formulated card): Is there an effectively specified logic capturing exactly polynomial-time properties of finite unordered structures? [Source](https://doi.org/10.1109/LICS.2008.11).

## 265. Georg Gottlob

Existential-rule queries and expressive ontology reasoning.

- **[TCS-0494](../../data/cards/TCS-0494.json)** (source draft; status unverified): Does bounded derivation depth for existential database rules imply finite controllability: does every failed query entailment have a finite countermodel? [Source](https://a3nm.net/work/research/questions/#does-bounded-derivation-depth-imply-finite-controllability).
- **[TCS-6680](../../data/cards/TCS-6680.json)** (formulated card): Is conjunctive-query entailment for unrestricted SROIQ knowledge bases decidable? [Source](https://ceur-ws.org/Vol-2373/paper-25.pdf).

## 266. Leonid Libkin

Query determinacy and information-theoretic database bounds.

- **[TCS-0497](../../data/cards/TCS-0497.json)** (source draft; status unverified): Is it decidable whether a path query is determined by views that are unions of path queries, over finite databases? [Source](https://a3nm.net/work/research/questions/#determinacy-of-path-queries-by-unions-of-path-views).
- **[TCS-0488](../../data/cards/TCS-0488.json)** (source draft; status unverified): Are the entropic upper bounds on database-query output size computable to arbitrary accuracy from the query and its entropy constraints? [Source](https://doi.org/10.4230/DagRep.12.7.180).

## 267. Dexter Kozen

Fixpoint games and decision problems in modal logic.

- **[TCS-4245](../../data/cards/TCS-4245.json)** (formulated card; status unverified): Can the winner of every finite parity game be computed in deterministic polynomial time? [Source](https://doi.org/10.4230/LIPIcs.CSL.2017.27).
- **[TCS-6643](../../data/cards/TCS-6643.json)** (formulated card): Is unification in basic modal logic K decidable? [Source](https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=9592&wshow=paper).

## 268. Neil Immerman

Choiceless polynomial time and L versus NL connect descriptive complexity with the power of small-space computation.

- **[TCS-7311](../../data/cards/TCS-7311.json)** (source draft): Does choiceless polynomial time with counting express every isomorphism-invariant polynomial-time property of finite structures? [Source](https://arxiv.org/abs/math/9705225).
- **[TCS-0004](../../data/cards/TCS-0004.json)** (formulated card): Can directed s–t reachability be decided in deterministic O(log n) working space, equivalently L=NL? [Source](https://www.math.ias.edu/files/mathandcomp.pdf).

## 269. Bruno Courcelle

The boundary of graph-structural logical metatheorems.

- **[TCS-6654](../../data/cards/TCS-6654.json)** (formulated card): Must every graph class with decidable MSO₁ theory have bounded clique-width, in the precise theory convention of Seese’s conjecture? [Source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.167).
- **[TCS-6678](../../data/cards/TCS-6678.json)** (formulated card): Is first-order model checking fixed-parameter tractable on every hereditary monadically dependent graph class? [Source](https://arxiv.org/abs/2501.04166).

## 270. Wolfgang Thomas

Algebraic characterizations of definability by automata and logic.

- **[TCS-6561](../../data/cards/TCS-6561.json)** (formulated card): Is membership decidable in every fixed level of the dot-depth hierarchy of regular languages? [Source](https://arxiv.org/abs/2401.16195).
- **[TCS-6564](../../data/cards/TCS-6564.json)** (formulated card): Is it decidable whether a regular language of finite trees is first-order definable? [Source](https://lmcs.episciences.org/699).

## 271. Géraud Sénizergues

Equivalence of grammar and transducer models.

- **[TCS-0164](../../data/cards/TCS-0164.json)** (source draft; status unverified): Is equivalence decidable for two unambiguous context-free grammars? [Source](https://a3nm.net/work/research/questions/#equivalence-of-unambiguous-context-free-grammars).
- **[TCS-6563](../../data/cards/TCS-6563.json)** (formulated card): Is equivalence decidable for deterministic macro tree transducers? [Source](https://doi.org/10.1016/j.ipl.2022.106332).

## 272. Javier Esparza

Skolem decidability and deterministic equivalence of d-DNNFs concern exact symbolic questions underlying verification and model representation.

- **[TCS-5773](../../data/cards/TCS-5773.json)** (formulated card): Is it decidable whether an integer linear recurrence sequence ever has a zero term? [Source](https://doi.org/10.4230/LIPIcs.MFCS.2022.20).
- **[TCS-6650](../../data/cards/TCS-6650.json)** (source draft): Can equivalence of two deterministic decomposable negation-normal-form circuits be decided deterministically in polynomial time? [Source](https://arxiv.org/html/2605.12378v1).

## 273. Joël Ouaknine

The decidability of zero events in discrete and continuous linear dynamics.

- **[TCS-5773](../../data/cards/TCS-5773.json)** (formulated card): Is it decidable whether an integer linear recurrence sequence ever has a zero term? [Source](https://doi.org/10.4230/LIPIcs.MFCS.2022.20).
- **[TCS-6566](../../data/cards/TCS-6566.json)** (formulated card): Is the unbounded Continuous Skolem problem decidable: can one decide whether a specified coordinate of a rational linear differential system ever becomes zero? [Source](https://perso.uclouvain.be/vincent.blondel/publications/10BDJ.pdf).

## 274. Patricia Bouyer

Parametric timed systems and quantitative continuous-time verification.

- **[TCS-7309](../../data/cards/TCS-7309.json)** (formulated card): Is reachability decidable for discrete-time parametric timed automata with at most two parametric clocks and arbitrarily many nonnegative integer parameters? [Source](https://link.springer.com/article/10.1007/s00224-023-10121-3).
- **[TCS-7310](../../data/cards/TCS-7310.json)** (source draft): Is exact time-bounded reachability-threshold comparison decidable for rational continuous-time MDPs without an unproved transcendence conjecture? [Source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.133).

## 275. Kim Larsen

Simple stochastic games and mean-payoff games are central quantitative game-solving barriers relevant to timed and reactive verification.

- **[TCS-6567](../../data/cards/TCS-6567.json)** (formulated card): Can simple stochastic games be solved in polynomial time? [Source](https://www.sciencedirect.com/science/article/pii/089054019290048K).
- **[TCS-6568](../../data/cards/TCS-6568.json)** (formulated card): Can the threshold winner of an arbitrary finite mean-payoff game be computed in polynomial time? [Source](https://link.springer.com/chapter/10.1007/BFb0030814).

## 276. Orna Kupferman

Game-theoretic foundations of reactive synthesis.

- **[TCS-4245](../../data/cards/TCS-4245.json)** (formulated card; status unverified): Can the winner of every finite parity game be computed in deterministic polynomial time? [Source](https://doi.org/10.4230/LIPIcs.CSL.2017.27).
- **[TCS-6568](../../data/cards/TCS-6568.json)** (formulated card): Can the threshold winner of an arbitrary finite mean-payoff game be computed in polynomial time? [Source](https://link.springer.com/chapter/10.1007/BFb0030814).

## 277. Alexandra Silva

Generalized star height and synchronizing automata ask how algebraic descriptions constrain the expressive and operational behavior of finite automata.

- **[TCS-6559](../../data/cards/TCS-6559.json)** (formulated card): Is there a regular language whose generalized star height is greater than one, when complement does not count toward star height? [Source](https://www.irif.fr/~jep/Problemes/starheight.html).
- **[TCS-6558](../../data/cards/TCS-6558.json)** (formulated card): Does every synchronizing n-state deterministic finite automaton have a reset word of length at most (n−1)²? [Source](https://arxiv.org/abs/2608.24245).

## 278. Catuscia Palamidessi

Information-flow limits and the computability of information quantities.

- **[TCS-6608](../../data/cards/TCS-6608.json)** (formulated card): Is validity of unconditional Shannon information inequalities over arbitrary finite discrete random variables decidable? [Source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICDT.2024.19).
- **[TCS-7215](../../data/cards/TCS-7215.json)** (source draft): Is the Shannon capacity of an arbitrary finite graph computable to arbitrary additive accuracy? [Source](https://doi.org/10.1109/tit.2006.872856).

## 279. Thierry Coquand

Internal semisimplicial types and normalization in pure type systems concern the expressive foundations of dependent type theory.

- **[TCS-6569](../../data/cards/TCS-6569.json)** (formulated card): Can ordinary homotopy type theory internally define a uniform tower of semisimplicial types at all finite dimensions, without adding a second strict equality? [Source](https://nicolaikraus.github.io/docs/on_semisimplicial_types.pdf).
- **[TCS-6583](../../data/cards/TCS-6583.json)** (formulated card): In every pure type system, does weak normalization of a typable term imply its strong normalization? [Source](https://tlca.di.unito.it/opltlca/problem9.pdf).

## 280. Gérard Huet

Word-equation complexity and one-relation monoid equality connect unification to the basic decision theory of rewriting.

- **[TCS-0171](../../data/cards/TCS-0171.json)** (source draft; status unverified): Is satisfiability of word equations in NP? Variables range over finite strings and equality means equality after simultaneous substitution. [Source](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/92.html).
- **[TCS-6641](../../data/cards/TCS-6641.json)** (formulated card): Is the uniform word problem decidable for monoids presented by a single defining relation? [Source](https://link.springer.com/article/10.1007/s00233-021-10216-8).

## 281. Peter O’Hearn

Word equations with lengths and equivalence of decomposable circuits are two concrete decision barriers related to symbolic program analysis.

- **[TCS-6562](../../data/cards/TCS-6562.json)** (formulated card): Is satisfiability of word equations together with linear constraints on variable lengths decidable? [Source](https://arxiv.org/abs/2406.02160).
- **[TCS-6650](../../data/cards/TCS-6650.json)** (source draft): Can equivalence of two deterministic decomposable negation-normal-form circuits be decided deterministically in polynomial time? [Source](https://arxiv.org/html/2605.12378v1).

## 282. Andrew Pitts

Denotational models and their equational theories.

- **[TCS-6570](../../data/cards/TCS-6570.json)** (formulated card): Does a Scott-continuous model of the untyped lambda calculus have equational theory exactly beta-conversion? [Source](https://tlca.di.unito.it/opltlca/opltlcasu29.html).
- **[TCS-7306](../../data/cards/TCS-7306.json)** (source draft): Does an effective Scott-continuous lambda model have a recursively enumerable equational theory? [Source](https://arxiv.org/abs/0806.2264).

## 283. Luke Ong

Higher-order recursion and equivalence of tree-producing programs.

- **[TCS-6582](../../data/cards/TCS-6582.json)** (formulated card): Is equivalence of deterministic higher-order recursion schemes decidable? [Source](https://www.cs.rhul.ac.uk/home/uxac009/files/papers/tocl17.pdf).
- **[TCS-6563](../../data/cards/TCS-6563.json)** (formulated card): Is equivalence decidable for deterministic macro tree transducers? [Source](https://doi.org/10.1016/j.ipl.2022.106332).

## 284. Lars Birkedal

Semisimplicial types and equivalence of decomposable circuits connect expressive foundations with exact reasoning about symbolic program representations.

- **[TCS-6569](../../data/cards/TCS-6569.json)** (formulated card): Can ordinary homotopy type theory internally define a uniform tower of semisimplicial types at all finite dimensions, without adding a second strict equality? [Source](https://nicolaikraus.github.io/docs/on_semisimplicial_types.pdf).
- **[TCS-6650](../../data/cards/TCS-6650.json)** (source draft): Can equivalence of two deterministic decomposable negation-normal-form circuits be decided deterministically in polynomial time? [Source](https://arxiv.org/html/2605.12378v1).

## 285. Tobias Nipkow

One-rule termination and shortest word-equation solutions concern the decision procedures supporting symbolic automation.

- **[TCS-6644](../../data/cards/TCS-6644.json)** (source draft): Is termination decidable for string-rewriting systems consisting of one rule? [Source](https://epubs.siam.org/doi/10.1137/S009753979833297X).
- **[TCS-7194](../../data/cards/TCS-7194.json)** (source draft): Does every satisfiable word equation of length n have a solution in which each substituted word has length at most 2^{poly(n)}? [Source](https://ii.uni.wroc.pl/~aje/WordEq2015/papers/PlandowskiRytter.pdf).

## 286. Lawrence Paulson

Modal unification and the consistency of computational hardness with bounded arithmetic concern proof search and the mathematical foundations of automated reasoning.

- **[TCS-6643](../../data/cards/TCS-6643.json)** (formulated card): Is unification in basic modal logic K decidable? [Source](https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=9592&wshow=paper).
- **[TCS-1098](../../data/cards/TCS-1098.json)** (source draft; status unverified): Can one prove that PV₁ proves no sentence asserting correctness of a polynomial-time SAT decision algorithm? [Source](https://arxiv.org/abs/2504.04416).

## 287. Xavier Leroy

One-rule rewriting termination and normalization of pure type systems are foundational questions about semantics-preserving symbolic computation.

- **[TCS-6644](../../data/cards/TCS-6644.json)** (source draft): Is termination decidable for string-rewriting systems consisting of one rule? [Source](https://epubs.siam.org/doi/10.1137/S009753979833297X).
- **[TCS-6583](../../data/cards/TCS-6583.json)** (formulated card): In every pure type system, does weak normalization of a typable term imply its strong normalization? [Source](https://tlca.di.unito.it/opltlca/problem9.pdf).

## 288. Michael Fellows

The defining tractability barrier and preprocessing limits of parameterized complexity.

- **[TCS-6592](../../data/cards/TCS-6592.json)** (formulated card): Can k-Clique be solved in f(k)n^{O(1)} time, equivalently FPT=W[1]? [Source](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf).
- **[TCS-6660](../../data/cards/TCS-6660.json)** (source draft): Does Edge Multiway Cut parameterized by the deletion budget have a polynomial kernel? [Source](https://arxiv.org/abs/2002.08825).

## 289. Fedor Fomin

Exact clique-width recognition and minimal dominating-set enumeration concern graph structure and output-sensitive algorithms.

- **[TCS-7181](../../data/cards/TCS-7181.json)** (source draft): For every fixed k, is it polynomial-time decidable whether an input graph has clique-width at most k? [Source](https://doi.org/10.1137/070687256).
- **[TCS-0553](../../data/cards/TCS-0553.json)** (source draft; status unverified): Can all inclusion-minimal dominating sets of an arbitrary graph be enumerated in time polynomial in the input plus total output size? [Source](https://doi.org/10.4230/DagRep.8.10.63).

## 290. Daniel Lokshtanov

Parameterized complexity and exact exponential-time algorithms.

- **[TCS-6595](../../data/cards/TCS-6595.json)** (formulated card): For every ε>0, does some k-CNF satisfiability problem require more than O*((2−ε)^n) deterministic time? [Source](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturi_2001_jcss.pdf).
- **[TCS-7313](../../data/cards/TCS-7313.json)** (formulated card): Does deterministic ETH imply deterministic Gap-ETH for sparse 3-CNF formulas? [Source](https://eccc.weizmann.ac.il/report/2024/114/).

## 291. Marek Cygan

The exact exponential-time barriers for TSP and Set Cover fit the algebraic and combinatorial algorithmic side of this profile.

- **[TCS-7233](../../data/cards/TCS-7233.json)** (formulated card): Can general weighted TSP on n vertices be solved in O*((2−ε)^n) time for some fixed ε>0? [Source](https://arxiv.org/abs/2405.03018v2).
- **[TCS-6594](../../data/cards/TCS-6594.json)** (source draft): For every ε>0, is some bounded-set-size version of Set Cover impossible in O*((2−ε)^n) time, where n is the universe size? [Source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.34).

## 292. Andrei Bulatov

Algebraic classifications of constraint satisfaction and counting.

- **[TCS-6636](../../data/cards/TCS-6636.json)** (formulated card): Does the Bodirsky–Pinsker tractability dichotomy hold for CSPs of reducts of finitely bounded homogeneous structures? [Source](https://arxiv.org/abs/1704.01914).
- **[TCS-7320](../../data/cards/TCS-7320.json)** (new; formulated card): Is approximate counting for every fixed finite family of nonnegative rational Boolean log-supermodular constraints approximation-preserving reducible to #BIS? [Source](https://drops.dagstuhl.de/storage/02dagstuhl-follow-ups/dfu-vol007/DFU.Vol7.15301.205/DFU.Vol7.15301.205.pdf).

## 293. Dmitriy Zhuk

Promise constraint satisfaction beyond the resolved finite CSP dichotomy.

- **[TCS-6635](../../data/cards/TCS-6635.json)** (formulated card): Does every finite-template decision promise CSP belong to P or become NP-hard? [Source](https://arxiv.org/abs/2208.13538).
- **[TCS-6637](../../data/cards/TCS-6637.json)** (formulated card): Can every 3-colourable graph be coloured in polynomial time with a universal constant number of colours? [Source](https://arxiv.org/abs/2406.00357).

## 294. Constantinos Daskalakis

Continuous Local Search and sequential calibration connect equilibrium computation with learning dynamics and forecasting.

- **[TCS-7286](../../data/cards/TCS-7286.json)** (source draft): Does every problem in Continuous Local Search have a polynomial-time algorithm? [Source](https://arxiv.org/abs/2011.01929).
- **[TCS-7319](../../data/cards/TCS-7319.json)** (new; formulated card): What is the minimax expected ℓ₁ calibration error after T sequential binary forecasts against an adaptive adversary that does not observe the current forecast? [Source](https://arxiv.org/abs/2406.13668).

## 295. Ariel Procaccia

The existence and computation of fair allocations.

- **[TCS-0011](../../data/cards/TCS-0011.json)** (source draft): Does every instance of indivisible goods with additive nonnegative valuations admit a complete EFX allocation, including arbitrarily many agents? [Source](https://tcsopenproblems.com/problem/3).
- **[TCS-6633](../../data/cards/TCS-6633.json)** (formulated card): Does exact envy-free cake cutting for arbitrarily many agents admit a protocol with polynomially many Robertson–Webb queries? [Source](https://link.springer.com/article/10.1007/s00355-025-01633-7).

## 296. Vincent Conitzer

Metric voting distortion and existence of competitive equilibrium connect social-choice information limits with allocation.

- **[TCS-6634](../../data/cards/TCS-6634.json)** (formulated card): What is the optimal worst-case expected distortion achievable by randomized voting rules when only rankings from an unknown metric are given? [Source](https://arxiv.org/abs/2505.13630).
- **[TCS-7207](../../data/cards/TCS-7207.json)** (source draft): For two agents with additive preferences over indivisible goods, does competitive equilibrium exist for almost every budget pair in the source’s normalization? [Source](https://doi.org/10.1287/moor.2020.1062).

## 297. Shahar Dobzinski

The approximation limits imposed by truthful mechanisms.

- **[TCS-6632](../../data/cards/TCS-6632.json)** (formulated card): Does a polynomial-time universally truthful combinatorial auction achieve constant-factor welfare approximation for submodular bidders? [Source](https://epubs.siam.org/doi/10.1137/20M1316068).
- **[TCS-6674](../../data/cards/TCS-6674.json)** (formulated card): Can randomized truthful mechanisms beat the known linear deterministic approximation barrier for unrelated-machine makespan? [Source](https://arxiv.org/abs/2301.11905).

## 298. Lenore Blum

Complexity and decidability over the real numbers.

- **[TCS-7321](../../data/cards/TCS-7321.json)** (new; formulated card): Is P_ℝ=NP_ℝ in the exact unit-cost Blum–Shub–Smale model over the ordered real field, allowing finitely many arbitrary real machine constants? [Source](https://www.emis.de/journals/BBMS/Bulletin/bul971/meer.pdf).
- **[TCS-7230](../../data/cards/TCS-7230.json)** (formulated card): Is the first-order theory of the real field with exponentiation decidable, without an unproved number-theoretic assumption? [Source](https://arxiv.org/abs/2603.08365v2).

## 299. André Nies

Definability, computability and algorithmic randomness.

- **[TCS-6646](../../data/cards/TCS-6646.json)** (formulated card): Does Martin’s conjecture fully classify Turing-invariant degree-increasing functions under determinacy? [Source](https://doi.org/10.1017/bsl.2025.10137).
- **[TCS-6648](../../data/cards/TCS-6648.json)** (formulated card): Does Kolmogorov–Loveland randomness coincide with Martin-Löf randomness? [Source](https://arxiv.org/abs/2403.19817).

## 300. Ming Li

Minimum circuit size and adaptive algorithmic randomness connect description complexity with the foundations of information.

- **[TCS-5501](../../data/cards/TCS-5501.json)** (source draft; status unverified): Is the Minimum Circuit Size Problem NP-hard under deterministic polynomial-time many-one reductions, when a function is given by its full truth table? [Source](https://doi.org/10.4230/LIPIcs.CCC.2023.31).
- **[TCS-6648](../../data/cards/TCS-6648.json)** (formulated card): Does Kolmogorov–Loveland randomness coincide with Martin-Löf randomness? [Source](https://arxiv.org/abs/2403.19817).

