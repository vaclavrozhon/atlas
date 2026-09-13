**Graph-algorithm candidates around Bernstein, Haeupler, Saranurak, Nanongkai, Henzinger, Chan, and Mareš**

Research date: 13 September 2026. The user confirmed that the first researcher is Aaron Bernstein. The initial proposal below was subsequently approved in full and applied: eleven new cards and four existing-card updates. See the [import review and category mapping](IMPORT.md). Category registries and focus selections were preserved.

The shortlist has ten graph-related targets and five additional general algorithmic targets connected to Chan. Eight of the first ten fit Graph theory and algorithms; G8 fits Fine-grained complexity and G10 fits Parallel and distributed algorithms under the existing category rules. G7 overlaps an existing integer-weight SSSP card and is better considered as a possible extension or companion model than counted as an independent missing topic. C3–C5 already have catalogue entries.

The evidence combines primary papers, authors' publication pages, subsequent results through 2026, and a search of current cards and deletion reasons. “Candidate” means that the cited results leave the stated target unanswered and this search found no resolution. It does not mean that every later preprint has been exhaustively audited. Some targets below are editorial selections of a major endpoint rather than conjectures attributed verbatim to the named researchers. Associations mean a documented connection to their research, not authorship of the open question.

Notation: \(n\) is the number of vertices and \(m\) the number of edges/arcs. Near-linear means \(\widetilde O(m+n)\), hiding polylogarithmic factors; almost-linear means \((m+n)^{1+o(1)}\). They are different targets. Randomized algorithmic proposals permit bounded error at most \(1/3\); deterministic proposals do not. Final card authoring must preserve the model distinctions below.

**Ten graph-related candidates**

1. **G1 — Strongly polynomial near-linear negative-weight shortest paths.** Given a directed graph with arbitrary real edge lengths and no negative cycle, compute all distances from one source in \(\widetilde O(m+n)\) operations on a comparison-addition real RAM. Unreachable distances are infinity. The operation bound must not depend on a numerical weight bound. This is a major remaining gap between integer scaling and arbitrary real inputs, with direct connections to **Aaron Bernstein and Danupon Nanongkai**.

   Bernstein–Nanongkai–Wulff-Nilsen obtained near-linear SSSP with integer weights and a \(\log W\) dependence. Bringmann–Cassis–Fischer explicitly ask whether this dependence can be removed in §1.4, question 3. Their question 4, derandomization for integer weights, has since been answered by Haeupler–Jiang–Saranurak and should not be proposed again. For real weights, the 2026 papers by Quanrud–Tajkhorshid and Li–Li–Rao–Zhang give substantial polynomial improvements. The subsequent Li–Li–Zhang preprint gives \(n^{2+o(1)}\) time: almost linear for dense graphs, but it does not settle near-linear time for all densities. [Original breakthrough](https://arxiv.org/abs/2203.03456), [explicit open question](https://arxiv.org/abs/2304.05279), [deterministic integer result](https://arxiv.org/abs/2511.08551), [2026 real-weight progress](https://arxiv.org/abs/2511.18253), [February 2026 dense-graph result](https://arxiv.org/abs/2602.16153).

   **Atlas:** no matching active target found. Related to TCS-7263 (positive integers in linear time) and TCS-6510 (all-pairs distances), but neither has this input/model/complexity target. **Priority: very high.**

2. **G2 — Steiner Shortcut Conjecture.** Can every directed graph be augmented with Steiner vertices and \(\widetilde O(m)\) new edges so that reachability between original vertices is preserved exactly and every reachable original pair has a path of polylogarithmic length? Take graphs without isolated vertices to avoid irrelevant input-size conventions. This asks about existence, without adding an efficient-construction requirement.

   This is Conjecture 2 in *Reviving Thorup's Shortcut Conjecture* (PDF page 4; printed page 2), coauthored by **Bernstein, Haeupler, and Saranurak**. The original version allowing only new edges on the old vertex set was refuted; the Steiner version is explicitly left open. Its attraction is a structural explanation of whether long directed computations can be compressed. Existence alone does not prove a work-efficient parallel construction. [Primary source, STOC 2026](https://arxiv.org/abs/2510.24954).

   **Atlas:** no Steiner-vertex version found. TCS-6507 asks for a parallel reachability algorithm. Deleted TCS-6492 concerned another edge-budget slice of ordinary shortcuts; G2 changes the allowed representation and escapes the known lower bounds. **Priority: very high.**

3. **G3 — Deterministic almost-linear undirected vertex connectivity.** For a simple undirected unweighted graph, deterministically compute its vertex connectivity and a corresponding minimum separator in \((m+n)^{1+o(1)}\) time. Use the standard convention that deletion may disconnect the graph or leave one vertex, so \(\kappa(K_n)=n-1\). This closes a substantial randomized/deterministic gap for a basic graph primitive.

   **Nanongkai and Saranurak** coauthored the randomized reduction to polylogarithmically many max-flows, yielding almost-linear time with modern flow algorithms. Jiang–Nalam–Saranurak–Yingchareonthawornchai give deterministic \(\widehat O(m\kappa)\) time in 2025; it still depends polynomially on connectivity. Their introduction traces the problem to **Henzinger–Rao–Gabow**. Fixed-connectivity results do not settle arbitrary \(\kappa\). [Randomized reduction](https://arxiv.org/abs/2104.00104), [deterministic progress, Theorem 1.2](https://arxiv.org/abs/2503.20985).

   **Atlas:** no duplicate found. TCS-7075 asks about augmentation, which changes the graph rather than measuring its current connectivity. **Priority: very high.**

4. **G4 — Almost-linear exact global minimum edge-cut in directed graphs.** Given a directed graph with positive polynomially bounded integer edge weights, minimize \(w(E(S,V\setminus S))\) over all nonempty proper vertex subsets in randomized \((m+n)^{1+o(1)}\) time, and output an attaining cut. This is a global cut with no prescribed terminals.

   Quanrud and, independently, Mosenzon give almost-linear \((1+\varepsilon)\)-approximation schemes with an inverse-\(\varepsilon\) dependence. Their results do not give an almost-linear exact algorithm when the optimum is large. Almost-linear exact single-pair max-flow does not automatically handle the unknown optimal terminal pair with the same total cost. These are substantial modern directions beyond the six requested researchers. [Quanrud](https://arxiv.org/abs/2512.00176), [Mosenzon, introduction and Theorem 1.1](https://arxiv.org/abs/2512.09080).

   **Atlas:** no duplicate found. TCS-7228 instead targets a *specified* s–t flow in \(\widetilde O(m+n)\) time. It differs both in quantification over terminals and in the desired overhead. **Priority: high.**

5. **G5 — Almost-linear exact directed vertex connectivity.** For a simple unweighted digraph, find a smallest set of vertices whose deletion destroys strong connectivity or leaves at most one vertex, in randomized \((m+n)^{1+o(1)}\) time. For a nontrivial separator, this means a partition \((L,S,R)\) with nonempty \(L,R\), no arc from \(L\) to \(R\), and minimum \(|S|\). Already disconnected instances have value zero.

   Chuzhoy–Mosenzon–Trabelsi (SODA 2026) give an unweighted bound \(\min\{m^{1+o(1)}\kappa,n^{2+o(1)}\}\). Their weighted algorithm also breaks the longstanding bound originating in **Henzinger–Rao–Gabow**. The approximation schemes cited for G4 apply to directed vertex cuts, but retain a precision cost for exactness. The proposed endpoint is an editorial choice, not a claim that this paper formally conjectures almost-linear time. [2026 primary paper](https://arxiv.org/abs/2512.24355), [approximation progress](https://arxiv.org/abs/2512.00176), [Henzinger's original research announcement](https://theory.stanford.edu/~aflb/1996-97.html).

   **Atlas:** no duplicate found. G3 requires determinism in undirected graphs; G5 permits randomness but must handle directed graphs. They capture different gaps and neither proposed statement directly subsumes the other. **Priority: high.**

6. **G6 — Strongly polynomial maximum flow below the \(mn\) barrier.** Is there a fixed \(\varepsilon>0\) and a strongly polynomial algorithm computing an exact s–t maximum flow in \(O((mn)^{1-\varepsilon})\) arithmetic operations for all directed networks with \(m\ge n-1\) and arbitrary nonnegative rational capacities? The operation count must be independent of capacity magnitudes and intermediate encodings must have polynomial bit length. Randomization may be allowed; a completed card must fix expected versus worst-case costs.

   This is the explicit longstanding question in the introduction of Dadush–Orlin–Sidford–Végh (SODA 2026; PDF page 3, printed page 1). Their improvements cover structured networks, while the general strongly polynomial bound remains \(O(mn)\). An almost-linear strongly polynomial algorithm would be a stronger endpoint, but the sourced polynomial improvement is already a major target. [Primary source](https://arxiv.org/abs/2510.20368).

   **Atlas:** distinct from TCS-7228, whose capacities are polynomially bounded and whose goal is polylogarithmic overhead, and from TCS-0809, which concerns planar minimum-cost flow. This adds a central problem associated with **Dadush, Orlin, Sidford, and Végh**. **Priority: very high.**

7. **G7 — Linear-time nonnegative real-weight directed SSSP.** Compute exact distances from one source in \(O(m+n)\) deterministic worst-case time in the comparison-addition model, for arbitrary nonnegative real edge lengths. This is the clean optimal endpoint after breaking the sorting barrier.

   Duan–Mao–Shu–Yin (ICALP 2026) obtain \(O(m\sqrt{\log n}+\sqrt{mn\log n\log\log n})\), improving the 2025 \(O(m\log^{2/3}n)\) breakthrough. The result is not linear. The question is also a natural contemporary continuation of Mareš's shortest-path chapter; it is not explicitly stated there in this modern form. [Current primary result](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.81).

   **Atlas:** closely overlaps TCS-7263, which fixes positive integer weights and the word RAM. Prefer reviewing a broader card or explicitly justified companion model over adding a second card merely for a different weight domain. **Priority: high scientifically; conditional editorial addition.**

8. **G8 — Directed unweighted APSP below \(n^{5/2}\).** Is there a fixed \(\varepsilon>0\) and a bounded-error word-RAM algorithm computing the exact distance matrix of every unweighted directed n-vertex graph in \(O(n^{5/2-\varepsilon})\) time? This is a concrete decision about the Directed Unweighted APSP Hypothesis, without assuming \(\omega=2\) in the algorithmic target.

   **Timothy Chan**, Vassilevska Williams, and Xu develop its equivalence class in their 2021 paper. Unlike undirected unweighted APSP, the standard directed bound does not fall to near-quadratic merely by setting \(\omega=2\). Fischer (STOC 2026) links the directed-unweighted, Strong APSP, and ordinary integer APSP hypotheses under \(\omega=2\) and an additional additive-combinatorics assumption. Thus an older proposal to establish that conditional relationship would be stale, but the algorithmic question remains. [Chan et al.](https://arxiv.org/abs/2102.06181), [2026 update](https://arxiv.org/abs/2603.27736).

   **Atlas:** related to TCS-6510 (real-weight APSP below cubic) and TCS-6937; not the same statement. **Category: Fine-grained complexity. Priority: high, subject to consolidating this APSP cluster.**

9. **G9 — Single-exponential exact cut mimicking networks.** Does every nonnegatively edge-weighted undirected graph with k specified terminals have a weighted graph on \(2^{O(k)}\) vertices containing the same terminals and preserving every minimum terminal bipartition cut exactly? The new graph may use arbitrary Steiner vertices and need not be a contraction/minor of the original.

   The general size gap is exponential lower bounds versus doubly exponential upper bounds. The 2025 Chen–Tan paper reviews that gap, proves improved results for planar and quasi-bipartite graphs, and emphasizes that contraction can be much weaker. Restricting G9 to contractions would run into known doubly exponential lower bounds. This is a major graph compression question associated with **Krauthgamer, Rika, Khan, Raghavendra, Chen, and Tan**. [Primary survey and new results, §1 and Table 1](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.53/LIPIcs.ICALP.2025.53.html), [general construction](https://arxiv.org/abs/1207.6371).

   **Atlas:** no matching target found. TCS-3480 preserves a different metric-labeling problem under a crossing-edge budget. A Gomory–Hu tree preserves pairwise minimum cuts; G9 preserves cuts separating arbitrary terminal subsets, so that theorem does not settle G9. **Priority: high.**

10. **G10 — Work-efficient parallel exact directed maximum flow.** For polynomially bounded nonnegative integer capacities, compute an exact s–t maximum flow using \((m+n)^{1+o(1)}\) total work and \((m+n)^{o(1)}\) depth, with bounded error in a standard shared-memory parallel RAM model. Asking for polylogarithmic depth would strengthen this target; the stated subpolynomial-depth version is already a major open question.

    **Haeupler–Jiang–Saranurak**, in *DAG Projections* (STOC 2026), explicitly identify this as a major open problem and relate it to approximate flow on DAGs. Their theorem is a reduction, not a solution to the parallel exact-flow question. Sequential almost-linear exact flow is known and does not suffice. [Primary source, abstract and §1.2](https://arxiv.org/abs/2604.04752).

    **Atlas:** TCS-6507 concerns reachability; TCS-4763 concerns approximate multi-commodity minimum-cost flow, as recorded in its saved context. Neither is this exact single-commodity target. **Category: Parallel and distributed algorithms. Priority: very high.**

**Two documented connections for every requested researcher**

| Researcher | First connection | Second connection |
| --- | --- | --- |
| Aaron Bernstein | G1: coauthor of the negative-weight integer SSSP breakthrough | G2: coauthor of the paper proposing the Steiner Shortcut Conjecture |
| Bernhard Haeupler | G2: Steiner shortcuts | G10: exact parallel flow and DAG projections |
| Thatchaphol Saranurak | G3: deterministic and randomized vertex connectivity | G2/G10: shortcuts and parallel flow |
| Danupon Nanongkai | G1: negative-weight SSSP | G3: coauthor of the randomized vertex-connectivity reduction whose deterministic analogue is sought |
| Monika Henzinger | G3: foundational undirected vertex-connectivity algorithms | G5: foundational directed/weighted vertex-connectivity algorithms, explicitly revisited by the 2026 work |
| Timothy M. Chan | G8: directed unweighted APSP | C1–C5 below: subset sum, inversion counting, convolution, and structured sorting |

Henzinger's links here are to foundational work, not a claim that she authored the newest papers. For a more representative dynamic-algorithms alternative, her exact dynamic global min-cut line is also highly relevant, but TCS-6670 already represents that direction. Similarly, deterministic fully dynamic connectivity (TCS-6625) and approximate dynamic matching (TCS-6627) are already present and should not be counted as discoveries.

**Five more general algorithmic problems connected to Chan**

- **C1 — Near-linear output-sensitive Subset Sum.** Given positive integers \(X=(x_1,\dots,x_n)\) and a threshold t, enumerate the distinct attainable sums \(S=\{\sum_{i\in I}x_i:I\subseteq[n]\}\cap[0,t]\) in \(\widetilde O(n+|S|)\) time, with polylogarithmic factors in n and t on an appropriately sized word RAM. This is a stronger output-sensitive endpoint than merely \(\widetilde O(n+t)\). Bringmann–Nakos explicitly pose the question; **Chan's SODA 2026 paper** derandomizes known \(\widetilde O(|S|^{4/3})\) and \(\widetilde O(|S|\sqrt n)\) algorithms. Include input-reading time for an explicit multiset. This target is distinct from the existing worst-case exponential Subset Sum card. **New candidate; Algorithms or Counting and enumeration after editorial review. Priority: very high.** [Explicit question](https://arxiv.org/abs/2107.13206), [Chan, §3](https://arxiv.org/abs/2601.01390).

- **C2 — Linear-time exact inversion counting.** Given a permutation \(\pi\) of \([n]\), compute \(|\{(i,j):i<j,\pi(i)>\pi(j)\}|\) exactly in \(O(n)\) time on a word RAM with \(\Theta(\log n)\)-bit words. Chan–Pătraşcu give \(O(n\sqrt{\log n})\); their linear-time approximation is not an exact solution. This is a particularly accessible question about the power of offline algorithms, separate from integer sorting because the input is already rank-compressed. The linear endpoint is our editorial formulation of the remaining complexity gap, not a quotation of a conjecture in their paper. No newer exact linear-time result was found, but its current-status evidence is weaker than C1's fresh 2026 reference. **New candidate; Algorithms. Priority: medium/high; further status confirmation desirable.** [Author-hosted primary paper, §§1.1–1.2](https://tmc.web.engr.illinois.edu/inv_7_7_09.pdf).

- **C3 — Truly subquadratic min-plus convolution.** For two arrays A,B of length n, compute all \(c_k=\min_{i+j=k}(a_i+b_j)\) in \(O(n^{2-\varepsilon})\) time for fixed \(\varepsilon>0\). Preserve the existing card's word-RAM and polynomially bounded integer assumptions. Chan coauthored early subquadratic-by-logarithmic-factors algorithms; that is different from a fixed exponent improvement. **Already TCS-6598; retain/enrich rather than add.** [Bremner–Chan et al., introduction and §3](https://arxiv.org/abs/1212.4771).

- **C4 — Sorting X+Y in quadratic time.** Given two real arrays of length n, sort their \(n^2\) pairwise sums in \(O(n^2)\) time. The distinction between a nonuniform decision tree using \(O(n^2)\) comparisons and a uniform real-RAM algorithm is essential. Chan's joint paper explains this classical question and its convolution connections. **Already TCS-0388; retain/enrich.** [Primary discussion, PDF page 4](https://tmc.web.engr.illinois.edu/convol.pdf).

- **C5 — A fixed exponential improvement over meet-in-the-middle for Subset Sum.** Is worst-case Subset Sum solvable in \(O(2^{(1/2-\varepsilon)n}\operatorname{poly}(L))\) time for some fixed \(\varepsilon>0\), where L is the binary input length, allowing bounded-error randomization? The fixed saving in the exponent distinguishes the target from polynomial-factor improvements. Chan's 2026 introduction recalls this unresolved exponential regime while solving a different pseudopolynomial derandomization problem. **Already represented by TCS-4790, whose saved formulation still needs completion; clarify that card rather than duplicate it.** [Chan, introduction](https://arxiv.org/abs/2601.01390).

Klee's measure (TCS-7184), ordinary 3SUM (TCS-0557), real APSP (TCS-6510), and integer sorting (TCS-6537) are additional obvious connections to Chan's research area or Mareš's material, but they do not fill new catalogue gaps. They were not counted as new proposals.

**What comes from Mareš**

I read the complete current [*Krajinou grafových algoritmů* PDF](https://mj.ucw.cz/vyuka/ga/ga.pdf), dated 25 February 2026 in its footer, and checked the [chapter/version index](https://mj.ucw.cz/vyuka/ga/). Chapter dates differ substantially; the footer is not evidence that every complexity bound has been freshly updated.

Two explicit major open questions are already represented: deterministic comparison-based linear MST (chapter 6, printed page 38; TCS-6536) and matrix multiplication exponent two (chapter 14, printed page 98; TCS-0007). Chapter 14 also discusses Chan's min-plus/APSP algorithms and motivates the existing APSP question and G8. Its historical numerical bounds must be updated from recent sources.

Chapters 1–4 provide the foundation for G3–G6 and the distinction between terminal-pair cuts and G9's terminal-set cuts; chapter 13 supplies the shortest-path background for G1/G7. These are modern continuations of the material, not claims that Mareš explicitly poses all those endpoints. Chapter 4's Gomory–Hu construction should not be turned into a new open almost-linear construction problem: that target has been resolved, including deterministically. TCS-5235 already records this resolution. [Deterministic 2025 result on a coauthor's page](https://rasmuskyng.com/research.html).

**Problems deliberately excluded after checking newer work**

| Tempting proposal | Reason to exclude that formulation |
| --- | --- |
| Near-linear negative-integer-weight SSSP | Bernstein–Nanongkai–Wulff-Nilsen, with later improvements, already achieve this. |
| Deterministic near-linear negative-integer-weight SSSP | Haeupler–Jiang–Saranurak, STOC 2026, achieve it with a scaling dependence. |
| Deterministic near-linear weighted undirected global min-cut | Henzinger–Li–Rao–Wang, SODA 2024, achieve it. [Primary paper](https://arxiv.org/abs/2401.05627). |
| Almost-linear exact max-flow/min-cost flow with polynomially bounded integer data | Known even deterministically. G6 changes numerical complexity, G10 changes parallel complexity, and TCS-7228 asks for a smaller overhead. [Primary deterministic result](https://arxiv.org/abs/2309.16629). |
| Randomized almost-linear unweighted undirected vertex connectivity | Follows from the existing randomized reduction and modern flow algorithms. G3 explicitly requires determinism. |
| Almost-linear constant-accuracy directed edge/vertex connectivity approximation | Achieved by the 2025/2026 works of Quanrud and Mosenzon. G4/G5 explicitly require exactness. |
| Almost-linear Gomory–Hu tree construction | Resolved, including deterministic construction in 2025. |
| Deterministic \(\widetilde O(n+t)\) Subset Sum | Chan, SODA 2026, resolves it; C1 is output-sensitive. |
| Original Thorup shortcut conjecture without Steiner vertices | Refuted; G2 is the revised conjecture. |

**Recommended editorial order**

Develop G1, G2, G3, G6, G9, and C1 first. G4/G5 form a second useful pair around exact directed cuts. G10 is an excellent parallel-algorithms addition. Review G8 against the APSP cluster and G7 against the existing positive-integer SSSP card before making a new card. Keep C2 as a promising additional basic problem with an explicitly weaker current-status review. Update C3–C5 in place if selected for further work.

This order is an editorial judgment about significance and coverage, rather than a claim that prestige, age, or an author's name establishes importance. The report selects targets and supplies evidence; full benchmark cards would still need their uniformity, randomness, operation model, and acceptance conventions completed individually.
