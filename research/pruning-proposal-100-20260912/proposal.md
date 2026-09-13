# 100 candidates for removal — 12 September 2026

**Screened all 1,066 active cards; selected exactly 100 candidates.** The 36 already inactive cards are outside the proposal. This is a review proposal; no catalogue data was changed.

[Searchable table](proposal.html) · [Spreadsheet TSV](proposal.tsv) · [Detailed JSON](decisions.json) · [All-card screen](all-card-review.tsv) · [Source checks](source-checks.json)

The list contains **4 historical targets answered by later work, 3 duplicate targets, 6 conditional consolidations, 2 problematic extractions, and 85 editorial cuts**. The latter divide into 57 specialized models/subcases, 17 secondary quantitative frontiers and 11 specific methods/constructions.

**13 high-confidence recommendations, 69 medium, 18 borderline.** Confidence describes the strength of the removal recommendation. The borderline cards have substantial scientific content and are the first recommendations I would reconsider if the proposed loss of coverage is too large. The order groups reasons and confidence; it is not a measured scientific ranking from 1 to 100.

Selection follows the goal of a 500-problem benchmark. I compared scientific significance and the independent contribution of each target; score, ranking, focus membership, category sizes and formalization effort did not determine selection. A small canonical problem can be important, and being a draft or asking for a number/function is not a removal reason. None of the twenty cards retained in the preceding 480-removal review is proposed here.

Every active card was screened using its current title and saved target summary. 150 cards then received a further target/motivation assessment, including all 100 selected cards and relevant alternatives. The exact displayed fields and current hashes are in [the read ledger](read-ledger.json). This is not a new full mathematical or open-status certification of all 1,066 problems. Targeted primary-source checks support the later-result cases; other priority judgments use the saved card and source material.

The six conditional consolidations need scope alignment before deletion. In particular, the girth cards use different quantifiers, the APSP cards use different computational models, and the cryptography entry bundles different implications. Their shared subject is not a proof of equivalence. The proposed retained IDs remain active and are outside this list.

Accepting every recommendation would leave **966 active cards**. No category quota or benchmark selection has been changed.

1. **[TCS-3114: Thus, the case that remains open concerns uncountable X and general (random) sequences X.](../../data/cards/TCS-3114.json)**

   Learning theory · Later result answers the historical target · **high**

   Blanchard's COLT 2022 result explicitly closes the COLT 2021 universal-online-learning questions, including weak and strong learning on general spaces. The card still extracts the earlier unresolved case.

   **Scope / condition:** The solved target uses deterministic target functions. Preserve the distinction from TCS-2654, which permits arbitrarily dependent responses.

   **Keep / consult:** [TCS-2654](../../data/cards/TCS-2654.json).

   **Evidence:** [Universal Online Learning: an Optimistically Universal Learning Rule](https://proceedings.mlr.press/v178/blanchard22b.html). Do not extend the conclusion to arbitrary dependent responses in TCS-2654.

2. **[TCS-3347: Complexity of conditional-independence implication](../../data/cards/TCS-3347.json)**

   Coding and information theory · Later result answers the historical target · **high**

   The 2020 source leaves conditional-independence implication undecided. Li's later undecidability theorem covers finite-support random variables with unrestricted alphabet sizes, so the standard historical question has an answer.

   **Scope / condition:** A separately specified fixed-alphabet or other restricted complexity problem would need its own assessment; the theorem is not about unconditional Shannon inequalities.

   **Evidence:** [Undecidability of Network Coding, Conditional Information Inequalities, and Conditional Independence Implication](https://arxiv.org/html/2205.11461v3). Fixed cardinalities have different decidability behavior. This does not resolve the separate unconditional Shannon-inequality card TCS-6608.

3. **[TCS-6418: Simultaneously time- and message-optimal distributed MST](../../data/cards/TCS-6418.json)**

   Distributed, parallel and sublinear algorithms · Later result answers the historical target · **high**

   The saved 2011 target asks for simultaneous near-optimal time and message complexity for distributed MST. Pandurangan, Robinson and Scquizzato give precisely these randomized bounds; this historical target should leave the open-problem pool.

   **Scope / condition:** The result permits Las Vegas randomization. Do not reinterpret the old card as a new deterministic target.

   **Evidence:** [A Time- and Message-Optimal Distributed Algorithm for Minimum Spanning Trees](https://arxiv.org/abs/1607.06883). This is the randomized target. No new deterministic target is inferred.

4. **[TCS-6737: Polynomial-query testing of minor-closed bounded-degree properties](../../data/cards/TCS-6737.json)**

   Property testing and distribution learning · Later result answers the historical target · **high**

   Kumar, Seshadhri and Stolman provide a tester with polynomial dependence on degree and inverse proximity for each fixed minor-closed property. This answers the historical polynomial-query target.

   **Scope / condition:** The theorem permits two-sided error and property-dependent constants. A one-sided tester is a different target, not an implicit replacement.

   **Evidence:** [Random walks and forbidden minors II: A polynomial-query tester for minor-closed properties of bounded-degree graphs](https://arxiv.org/abs/1904.01055). Constants depend on the fixed property. The result does not assert a one-sided tester with the same guarantee.

5. **[TCS-0054: Tensor decomposition at the uniqueness threshold](../../data/cards/TCS-0054.json)**

   Algebraic computation · Duplicate target · **high**

   This is another entry for the same Bhaskara–Charikar–Moitra–Vijayaraghavan tensor-decomposition open-problem paper and its uniqueness-threshold target. Keep the question once under the more specific Kruskal-threshold entry.

   **Scope / condition:** Transfer any unique provenance and preserve the precise robustness and computational-model requirements.

   **Keep / consult:** [TCS-4949](../../data/cards/TCS-4949.json).

6. **[TCS-0691: Recursive Teaching Dimension Versus VC Dimension](../../data/cards/TCS-0691.json)**

   Learning theory · Duplicate target · **high**

   Its saved question is exactly the universal linear bound of recursive teaching dimension by VC dimension for finite classes. TCS-2339 already states that same inequality explicitly.

   **Scope / condition:** Transfer the Simon–Zilles source; retain recursive teaching, rather than substituting non-clashing teaching or sample compression.

   **Keep / consult:** [TCS-2339](../../data/cards/TCS-2339.json).

7. **[TCS-6007: Explicit noncommutative circuit lower bounds](../../data/cards/TCS-6007.json)**

   Algebraic computation · Duplicate target · **high**

   The saved summary identifies general explicit noncommutative circuit lower bounds, already represented by TCS-6890. The paper's restricted ABP and formula results provide context rather than a different selected target.

   **Scope / condition:** Agree on the field and explicitness convention when developing the surviving general circuit question.

   **Keep / consult:** [TCS-6890](../../data/cards/TCS-6890.json).

8. **[TCS-3685: Average-case formula hardness of the majority Andreev function](../../data/cards/TCS-3685.json)**

   Computational complexity · Invalid or non-independent extraction · **high**

   The current reviewed card records a direct contradiction of its literal average-case target: a single input-table bit already gives inverse-polynomial advantage. This is stronger evidence for retirement than an ordinary unfinished statement.

   **Scope / condition:** A corrected distribution, encoding or advantage target would be a new source-supported formulation to assess; the paper's worst-case theorem is not being refuted.

   **Evidence:** [Existing card's raw-table consistency check](https://doi.org/10.4230/LIPIcs.ITCS.2019.35). The observation concerns the displayed raw-table model, not the source's separate worst-case theorem or a corrected intended average-case problem.

9. **[TCS-5777: Monotone versus general spanning-tree polynomial circuits](../../data/cards/TCS-5777.json)**

   Algebraic computation · Invalid or non-independent extraction · **high**

   The extracted sentence is the broad introductory question about monotone versus unrestricted computation. The same paper then proves concrete strong monotone separations for spanning-tree polynomials; the card identifies no additional independent residual conjecture.

   **Scope / condition:** Retire this extraction, not the general study of cancellation or every question in the paper. Its solved theorems can remain context elsewhere.

   **Evidence:** [Monotone Complexity of Spanning Tree Polynomial Re-Visited](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2022.39). The broader study of monotone versus unrestricted complexity is not declared solved; the problem is the absence of an independent residual target in this extraction.

10. **[TCS-0133: Stronger versions of inclusion of probabilistic automata](../../data/cards/TCS-0133.json)**

   Automata and formal languages · Consolidation requiring scope alignment · **medium**

   Both this seminar entry and TCS-3863 target unconditional containment for finitely ambiguous probabilistic automata. Their shared numerical-comparison obstacle is a better single benchmark entry than two loosely specified occurrences.

   **Scope / condition:** Compare pointwise probability containment, acceptance conventions and ambiguity bounds before merging; this is a proposed consolidation, not a certified equivalence.

   **Keep / consult:** [TCS-3863](../../data/cards/TCS-3863.json).

11. **[TCS-0171: Complexity of word unification](../../data/cards/TCS-0171.json)**

   Automated reasoning, rewriting and unification · Consolidation requiring scope alignment · **medium**

   Word unification and the word-equation satisfiability entry cover the same basic string-substitution complexity question in their ordinary unconstrained reading. The extra general label has little independent selection value.

   **Scope / condition:** First align constants, empty words and equation-system conventions. Do not merge additional regular or length constraints into the ordinary problem.

   **Keep / consult:** [TCS-0163](../../data/cards/TCS-0163.json).

12. **[TCS-2783: Erdős girth conjecture](../../data/cards/TCS-2783.json)**

   Structural graph theory and graph algorithms · Consolidation requiring scope alignment · **medium**

   This repeats the Erdős girth-conjecture theme in TCS-6500, with valuable routing provenance. One carefully reconciled girth entry would preserve the scientific challenge and avoid two slots for its near-identical extremal formulation.

   **Scope / condition:** The current cards differ: all sufficiently large n versus arbitrarily large n, and girth at least 2k+2 versus greater than 2k. Preserve or explicitly decide these quantifiers; no equivalence is asserted here.

   **Keep / consult:** [TCS-6500](../../data/cards/TCS-6500.json).

13. **[TCS-6937: Randomized APSP hypothesis](../../data/cards/TCS-6937.json)**

   Fine-grained complexity · Consolidation requiring scope alignment · **medium**

   The integer-weight randomized APSP hypothesis and the real-weight APSP card organize the same main exponent barrier. I would consider presenting their model variants together instead of keeping a separate textbook occurrence.

   **Scope / condition:** The integer word model and comparison-addition real RAM are different. Preserve both model-specific claims; a generic statement that these cards are duplicates would be incorrect.

   **Keep / consult:** [TCS-6510](../../data/cards/TCS-6510.json).

14. **[TCS-6953: Cryptographic primitives from worst-case or average-case hardness](../../data/cards/TCS-6953.json)**

   Cryptography · Consolidation requiring scope alignment · **medium**

   This broad source question bundles worst-case hardness, average-case hardness, one-way functions and trapdoors. Several sharper active cards already separate those foundational implications; retain its source and missing branches within that cluster.

   **Scope / condition:** Map every assumption and conclusion first. Infinitely-often one-wayness and public-key encryption are not automatically equivalent to all branches of the original trapdoor question.

   **Keep / consult:** [TCS-0022](../../data/cards/TCS-0022.json), [TCS-6453](../../data/cards/TCS-6453.json), [TCS-6545](../../data/cards/TCS-6545.json).

15. **[TCS-7033: Polynomial kernels for directed feedback sets](../../data/cards/TCS-7033.json)**

   Parameterized complexity and algorithms · Consolidation requiring scope alignment · **medium**

   The survey bundles directed feedback vertex and arc kernelization, while TCS-6379 already carries the central solution-size kernel question. A consolidated entry can avoid spending a separate slot on the survey occurrence.

   **Scope / condition:** Preserve the arc branch and explicitly verify the parameter-preserving reductions and deterministic kernel convention before removing the bundled entry.

   **Keep / consult:** [TCS-6379](../../data/cards/TCS-6379.json).

16. **[TCS-3314: Competitive chasing of three sets on the line](../../data/cards/TCS-3314.json)**

   Online algorithms, scheduling and packing · Specialized model or subcase · **high**

   Chasing exactly three arbitrary sets on the real line is a sharply restricted request-family question. It is an attractive small puzzle, but its saved motivation gives it less independent reach than the general k-server and convex-chasing frontiers.

   **Scope / condition:** The sets are not necessarily intervals or convex; one-dimensional convex chasing is not a resolution.

17. **[TCS-0073: Complexity of mixed equilibria in identical-payoff polymatrix games](../../data/cards/TCS-0073.json)**

   Game theory, social choice and fair division · Specialized model or subcase · **medium**

   Mixed-equilibrium complexity in identical-payoff polymatrix games isolates a specific network-coordination restriction. I would prioritize the broader equilibrium and incentive barriers over an additional card for this payoff-structure variant.

   **Scope / condition:** Shared payoff is not itself an efficient algorithm; the removal argument is editorial, not a resolution claim.

18. **[TCS-0173: Pattern unification modulo variable-preserving equations](../../data/cards/TCS-0173.json)**

   Automated reasoning, rewriting and unification · Specialized model or subcase · **medium**

   The target combines higher-order patterns with variable-preserving equational theories. It adds a specific closure question for symbolic unification beside the more central word, modal and rewriting decision barriers.

   **Scope / condition:** The presentation of the equation set must still be fixed; incompleteness of that detail is not the reason for the proposed cut.

19. **[TCS-0328: Sparse \((1 + \epsilon )\)-emulator for Euclidean Point Sets](../../data/cards/TCS-0328.json)**

   Geometry, topology and metric spaces · Specialized model or subcase · **medium**

   The target optimizes sparse near-isometric emulators for Euclidean points using abstract auxiliary vertices. It is a specific geometric representation variant beside broader metric-distortion and graph-spanner tradeoffs.

   **Scope / condition:** Abstract emulators and geometric Steiner spanners are not equivalent; the distinction is precisely the extra model choice being evaluated.

20. **[TCS-0363: Negative cycles on surface embedded graphs](../../data/cards/TCS-0363.json)**

   Geometry, topology and metric spaces · Specialized model or subcase · **medium**

   Negative-weight closed walks subject to contractibility combine path optimization with one topological constraint. I would place this particular surface-embedded task below the general shortest-path and topological-decision barriers.

   **Scope / condition:** Closed walks may repeat edges; neither ordinary negative-cycle detection nor simple-cycle algorithms settle the target.

21. **[TCS-0414: Surface Reconstruction](../../data/cards/TCS-0414.json)**

   Geometry, topology and metric spaces · Specialized model or subcase · **medium**

   This asks for topology recovery from samples of surfaces with singular features, extending a particular geometric reconstruction setting. Its benchmark contribution is focused on sampling guarantees for sharp edges and corners rather than a general topology or metric barrier.

   **Scope / condition:** A meaningful singular-surface theorem could be substantial. The missing density convention alone is not grounds for deletion.

22. **[TCS-0871: Universality and inclusion of AC-recognizable languages](../../data/cards/TCS-0871.json)**

   Automata and formal languages · Specialized model or subcase · **medium**

   Universality and inclusion are asked for the particular AC-recognizable tree-language model. I would favor the central unresolved language-equivalence and automaton-state-complexity questions over another equational recognition variant.

   **Scope / condition:** This is a scope judgment; decidability of restricted transition forms is not a solution of the full model.

23. **[TCS-0914: Deterministic min-cost matching with delays](../../data/cards/TCS-0914.json)**

   Optimization and numerical computation · Specialized model or subcase · **medium**

   Deterministic matching with waiting costs is a specific online objective combining metric movement and delay. I would prioritize the general matching and online metric-allocation questions over this additional cost-model variant.

   **Scope / condition:** This is not offline matching, and the missing competitive-ratio specification alone is not the basis for the proposal.

24. **[TCS-0957: Approximating Rank in the Bounded-Degree Model](../../data/cards/TCS-0957.json)**

   Distributed, parallel and sublinear algorithms · Specialized model or subcase · **medium**

   This isolates additive rank estimation for finite-field matrices with bounded row and column degree. The specific access model and matrix promise give it lower priority than general algebraic computation and sublinear-model characterizations.

   **Scope / condition:** Rank estimation on incidence matrices is only a special case and does not settle general sparse matrices.

25. **[TCS-0968: “For All” Guarantee for Computationally Bounded Adversaries](../../data/cards/TCS-0968.json)**

   Distributed, parallel and sublinear algorithms · Specialized model or subcase · **medium**

   This combines public compressed sensing, adaptive signal choice and computationally bounded adversaries. The benchmark would gain one cryptographic relaxation of a recovery guarantee, rather than a general sparse-recovery or cryptographic-foundations result.

   **Scope / condition:** The unrestricted-adversary impossibility does not settle the computationally bounded model.

26. **[TCS-1035: Cost of restricting linear circuits to depth two](../../data/cards/TCS-1035.json)**

   Computational complexity · Specialized model or subcase · **medium**

   The question measures the cost of forcing linear OR, SUM or XOR computations into exactly two layers. This adds a restricted depth comparison to a catalogue already rich in broader linear-circuit and circuit-versus-formula barriers.

   **Scope / condition:** The three operation systems must stay distinct; the rationale is marginal benchmark coverage rather than an alleged common answer.

27. **[TCS-1478: Adversarial sequential prediction with abstentions for VC classes](../../data/cards/TCS-1478.json)**

   Learning theory · Specialized model or subcase · **medium**

   This combines adaptive corruptions, abstention and unknown clean distributions for VC classes. The requested extension removes a reduction-dimension condition from that particular sequential prediction model, rather than changing the general PAC or online learnability boundary.

   **Scope / condition:** Finite VC dimension alone is not asserted to suffice; the model-specific extension is the target being deprioritized.

28. **[TCS-1539: VC-dimension bounds for adversarially robust compression](../../data/cards/TCS-1539.json)**

   Learning theory · Specialized model or subcase · **medium**

   Adversarially robust sample compression adds perturbation-set preservation and a stability-related premise to the central compression question. I would prioritize ordinary sample compression and broad robust learnability over this additional compression-model refinement.

   **Scope / condition:** The known negative statement for robust learnability alone does not settle the stronger premise here.

29. **[TCS-2111: Fully polynomial learning of positive ReLU networks under Gaussian inputs](../../data/cards/TCS-2111.json)**

   Learning theory · Specialized model or subcase · **medium**

   The chosen target is noiseless Gaussian learning of positive combinations of ReLUs with normalized weights. This restricted network/distribution/sign regime contributes less broad coverage than the general learning barriers, even though polynomial dependence on width remains meaningful.

   **Scope / condition:** Improper prediction, not parameter recovery, is required; the existing quasipolynomial width dependence is not a solution.

30. **[TCS-2243: \(\mathrm{TC}^{0}/\mathrm{NC}^{1}\) complexity dichotomy](../../data/cards/TCS-2243.json)**

   Automata and formal languages · Specialized model or subcase · **medium**

   The proposed TC0/NC1 dichotomy concerns visibly pushdown languages, adding a low-depth classification inside a structured language family. Its independent contribution is narrower than the general circuit-class and language-decidability barriers.

   **Scope / condition:** Do not confuse the classification target with separating TC0 from NC1 in general.

31. **[TCS-2680: Relativizing subexponential UP from heuristic average-case NP](../../data/cards/TCS-2680.json)**

   Beyond worst-case and average-case analysis · Specialized model or subcase · **medium**

   The exact conjecture requires a heuristic-average-case-to-UP implication relative to every oracle and at a specified subexponential scale. That relativizing, quantitative strengthening has less independent reach than the main worst-case versus average-case hardness questions.

   **Scope / condition:** The universal oracle quantifier is part of the target, not an optional proof technique.

32. **[TCS-2689: Deterministic safety and termination in hybrid synchrony](../../data/cards/TCS-2689.json)**

   Distributed, parallel and sublinear algorithms · Specialized model or subcase · **medium**

   The question removes randomized progress from one hybrid-synchrony permissionless-consensus model. Its safety/termination distinction is useful, but the specific participation model makes it a more specialized target than general agreement boundaries.

   **Scope / condition:** Do not apply an asynchronous impossibility theorem without matching the source's synchrony and participation assumptions.

33. **[TCS-3344: Decidability of rounded planar-rotation reachability](../../data/cards/TCS-3344.json)**

   Semantics, logic and verification · Specialized model or subcase · **medium**

   Reachability for rounded planar rotations isolates one numerical-dynamics model at two dimensions. It is a useful verification example, but more specialized than the general recurrence, linear-loop and reachability barriers.

   **Scope / condition:** Rounding can fundamentally change an orbit; ordinary rotation analysis does not decide this problem.

34. **[TCS-3414: Explicit permutation groups requiring superpolynomial graph embeddings](../../data/cards/TCS-3414.json)**

   Algebraic computation · Specialized model or subcase · **medium**

   This asks for large graph representations of explicit permutation actions with a distinguished invariant subset. It is an interesting representation lower bound, but the extra action-realization requirement makes its benchmark contribution more specialized than the main group-isomorphism and algebraic lower-bound questions.

   **Scope / condition:** The target is not ordinary realization of abstract groups as automorphism groups.

35. **[TCS-3557: Does extension preservation eliminate stratified intensional negation?](../../data/cards/TCS-3557.json)**

   Database theory and finite model theory · Specialized model or subcase · **medium**

   This is an exact preservation/expressiveness equivalence between stratified and semi-positive Datalog under induced database extensions. I would give that language-specific negation-elimination boundary lower priority than the broader logic-capturing and query-containment questions.

   **Scope / condition:** Induced-extension preservation differs from ordinary monotonicity; no general preservation theorem is being treated as a solution.

36. **[TCS-3655: Inductive-inductive types from inductive types without UIP](../../data/cards/TCS-3655.json)**

   Semantics, logic and verification · Specialized model or subcase · **medium**

   Eliminating finitary induction–induction without uniqueness of identity proofs concerns one primitive-reduction question in dependent type theory. I would prioritize the broader univalence, resizing and internal higher-structure foundations over this additional compilation boundary.

   **Scope / condition:** The equality restriction is substantive; an existing UIP-based reduction cannot simply be reused.

37. **[TCS-3676: Binary-horizon MDP reward-threshold complexity](../../data/cards/TCS-3676.json)**

   Optimization and numerical computation · Specialized model or subcase · **medium**

   The target classifies exact reward-threshold decisions for explicitly described MDPs with binary-encoded long horizons. It is a particular encoding-sensitive variant beside the broader stochastic-game and optimization-complexity questions.

   **Scope / condition:** The source's hardness of choosing a specified first action is not a theorem about this threshold problem.

38. **[TCS-3906: Sample complexity of symmetric Markov-chain identity testing](../../data/cards/TCS-3906.json)**

   Property testing and distribution learning · Specialized model or subcase · **medium**

   The target optimizes identity-testing samples for symmetric Markov chains observed along one trajectory. It adds a specific dependence and access model rather than a general distribution-testing or mixing barrier.

   **Scope / condition:** Starting distribution, chain distance and mixing promises are essential; independent sampling bounds are not a resolution.

39. **[TCS-4299: Collision detection in deterministic broadcast](../../data/cards/TCS-4299.json)**

   Distributed, parallel and sublinear algorithms · Specialized model or subcase · **medium**

   This asks whether collision feedback accelerates deterministic broadcast in the specified radio-network model. It compares one physical-layer capability for one communication task, with less independent coverage than broader distributed-computation questions.

   **Scope / condition:** Randomized benefits of collision detection do not establish a deterministic separation.

40. **[TCS-4463: Markov computability versus K-computability](../../data/cards/TCS-4463.json)**

   Computability and algorithmic information theory · Specialized model or subcase · **medium**

   This isolates a Markov-versus-K-computability separation for a particular represented codomain O(B). The representation-specific witness is less broad than the main randomness, degree-structure and computability barriers already represented.

   **Scope / condition:** The codomain representation is mathematically essential; the proposed cut does not generalize to all comparisons of represented-space computation.

41. **[TCS-4490: Complexity of positive matrix powers](../../data/cards/TCS-4490.json)**

   Algebraic computation · Specialized model or subcase · **medium**

   Higher-dimensional PosMatPow is a particular matrix-dynamics predicate within a catalogue already containing Skolem, Positivity and continuous-Skolem problems. Its present scientific motivation is chiefly the extension of one low-dimensional analysis.

   **Scope / condition:** Do not claim equivalence with recurrence positivity without recovering the PosMatPow predicate and power quantifier.

42. **[TCS-4495: Recovery hardness for sparse planted dense subgraphs](../../data/cards/TCS-4495.json)**

   Beyond worst-case and average-case analysis · Specialized model or subcase · **medium**

   This selects exact recovery in a particular sparse planted-subgraph exponent region under the planted-clique hypothesis. The detection/recovery distinction matters, but the restricted phase region makes it a more specialized benchmark than the central planted-model thresholds.

   **Scope / condition:** Dense, leakage-assisted and restricted-algorithm hardness results do not resolve the saved interior region.

43. **[TCS-4549: Polynomial-time colorful choice with polynomially many colors](../../data/cards/TCS-4549.json)**

   Geometry, topology and metric spaces · Specialized model or subcase · **medium**

   Allowing polynomially many colors is a particular redundancy tradeoff in colorful Carathéodory computation. I would prioritize general fixed-point and convex-optimization complexity over this relaxation of one geometric existence theorem.

   **Scope / condition:** The required output still uses at most one point from each color; extra colors do not make the task trivially solvable.

44. **[TCS-4677: Deciding first-order definability of orbit-finite automata](../../data/cards/TCS-4677.json)**

   Automata and formal languages · Specialized model or subcase · **medium**

   First-order definability for orbit-finite data automata extends a classical finite-alphabet correspondence into one infinite-data model. I would assign it lower priority than the broad regular-tree definability and equivalence barriers.

   **Scope / condition:** Aperiodicity alone is not a complete criterion in this setting.

45. **[TCS-4716: \(\mathrm{AC}^{0}\)-distinguishable locally indistinguishable \(\mathrm{NC}^{0}\) sources](../../data/cards/TCS-4716.json)**

   Pseudorandomness and derandomization · Specialized model or subcase · **medium**

   The construction simultaneously demands NC0 generation, large-coordinate indistinguishability and AC0 distinguishability. These combined circuit restrictions support a particular simple secret-sharing architecture rather than a general cryptographic existence barrier.

   **Scope / condition:** Local indistinguishability and global circuit indistinguishability are different requirements, both essential to the target.

46. **[TCS-4778: Derandomizing amplified relational computation](../../data/cards/TCS-4778.json)**

   Pseudorandomness and derandomization · Specialized model or subcase · **medium**

   This compares amplification and derandomization conventions for a particular relational-computation class. I would give these quantitative reliability variants lower priority than the primary search-versus-decision and P/BPP frontiers.

   **Scope / condition:** Multiple valid outputs do change amplification behavior; decision-problem error reduction is not an answer.

47. **[TCS-4869: Fine-grained reductions from 4-cycles to triangles](../../data/cards/TCS-4869.json)**

   Fine-grained complexity · Specialized model or subcase · **medium**

   The question seeks a particular fine-grained reduction from four-cycles to triangles in a source centered on listing. I would prioritize the main APSP, 3SUM and clique relationships over another task-specific reduction edge.

   **Scope / condition:** Decision and enumeration, including output size and instance blowup, must be aligned; no equivalence is assumed.

48. **[TCS-4894: Parity versus \(\mathrm{AC}^{0}\) with shallow quantum preprocessing](../../data/cards/TCS-4894.json)**

   Quantum computation and information · Specialized model or subcase · **medium**

   The target tests parity against a specific shallow-quantum-preprocessing/classical-AC0 pipeline. It is a restricted hybrid architecture comparison beside the broader quantum-classical computational and query separations.

   **Scope / condition:** Quantum gate fan-in, classical postprocessing and approximation probability all matter; classical parity lower bounds do not suffice.

49. **[TCS-4960: Polynomial depth lower bounds for Transformers](../../data/cards/TCS-4960.json)**

   Computational complexity · Specialized model or subcase · **medium**

   Polynomial depth lower bounds for a specified decoder-only Transformer model target one architecture and its resource conventions. I would prefer more broadly transferable circuit, formula and communication barriers in the main benchmark.

   **Scope / condition:** This is not a dismissal of learning theory or attention models; stronger evidence of consequences outside the chosen architecture would improve its case.

50. **[TCS-4977: Classical-witness versus quantum-witness hierarchies](../../data/cards/TCS-4977.json)**

   Quantum computation and information · Specialized model or subcase · **medium**

   Containment between particular classical-witness and quantum-witness polynomial hierarchies adds another alternation convention beyond the central QMA/QCMA and QMA(2) questions. I would give this hierarchy-level variant lower independent priority.

   **Scope / condition:** Measuring a quantum witness does not automatically preserve alternating quantifiers, so the containment is not claimed trivial.

51. **[TCS-5004: Polynomial-time robust online decision making](../../data/cards/TCS-5004.json)**

   Online algorithms, scheduling and packing · Specialized model or subcase · **medium**

   The question makes one robust-MDP regret guarantee computationally efficient with polynomial horizon, state and action dependence. It sits inside a specified uncertainty model, so I would prioritize more general online decision and bandit complexity barriers.

   **Scope / condition:** Information-theoretic regret guarantees do not imply a polynomial-time implementation.

52. **[TCS-5087: Polynomial-time robust spectral estimation](../../data/cards/TCS-5087.json)**

   Learning theory · Specialized model or subcase · **medium**

   The target combines adversarial poisoning, low-rank representation and spectral-norm recovery of an unobserved clean matrix. It is a particular robust estimation model beside the broader learning, low-rank approximation and computational-statistical questions.

   **Scope / condition:** Frobenius guarantees and detecting poisoning do not supply the requested spectral estimator.

53. **[TCS-5210: Polylogarithmic-query pattern-freeness testing](../../data/cards/TCS-5210.json)**

   Property testing and distribution learning · Specialized model or subcase · **medium**

   Polylogarithmic testing of constant-size forbidden sequence patterns is a focused ordered-pattern family. I would prioritize the broader structural classifications of testable properties over another pattern-specific query frontier.

   **Scope / condition:** The fixed-pattern, proximity and domain conventions remain necessary; constant pattern size does not automatically give constant queries.

54. **[TCS-5334: Sample-efficient latent-tree Ising learning](../../data/cards/TCS-5334.json)**

   Property testing and distribution learning · Specialized model or subcase · **medium**

   The intended target is sample-optimal proper learning in the latent-tree Ising family. It is a specific hidden-variable statistical-computational gap; the broader learning questions have greater independent coverage in the benchmark.

   **Scope / condition:** The current card additionally records a missing-logarithm conflict in the source. That defect needs correction, but is not by itself the reason to discard the genuine learning question.

55. **[TCS-5349: Dimension-free regret for bounded-max-norm experts](../../data/cards/TCS-5349.json)**

   Online algorithms, scheduling and packing · Specialized model or subcase · **medium**

   Dimension-free regret is sought under the particular bounded factorization-max-norm promise with the factorization hidden. This special structural promise adds less general coverage than unrestricted expert, bandit and convex-optimization regret questions.

   **Scope / condition:** Low rank, bounded max norm and a known factorization are different assumptions.

56. **[TCS-5434: Nontrivial agnostic membership-query learning of \(\mathrm{ACC}^{0}\)](../../data/cards/TCS-5434.json)**

   Learning theory · Specialized model or subcase · **medium**

   Agnostic membership-query learning of ACC0 with a nontrivial time saving combines a specific circuit class, query access and noise guarantee. I would prioritize the general circuit-learning/hardness connections over this additional restricted learning target.

   **Scope / condition:** Realizable learning and circuit satisfiability algorithms do not automatically yield the required agnostic guarantee.

57. **[TCS-5863: Decidability of stochastic resolvability for \(\omega\)-automata](../../data/cards/TCS-5863.json)**

   Automata and formal languages · Specialized model or subcase · **medium**

   Stochastic resolvability concerns one way to execute Büchi and coBüchi nondeterminism online with almost-sure success. This is a specialized resolver-existence boundary rather than a general automata equivalence or universality problem.

   **Scope / condition:** Checking a supplied resolver and deciding whether some resolver exists are different problems.

58. **[TCS-6814: Efficient PTAS for fixed-machine job-shop makespan](../../data/cards/TCS-6814.json)**

   Parameterized complexity and algorithms · Specialized model or subcase · **medium**

   An efficient approximation scheme with fixed-machine dependence is a specialized parameter regime of job-shop makespan. I would prioritize the broader scheduling approximation barriers and general parameterized complexity questions.

   **Scope / condition:** An ordinary PTAS with parameter-dependent polynomial exponent does not satisfy the EPTAS target.

59. **[TCS-7086: Incremental polynomial-time binary-matroid circuit enumeration](../../data/cards/TCS-7086.json)**

   Counting and enumeration · Specialized model or subcase · **medium**

   The target imposes incremental polynomial time and polynomial space specifically on binary-matroid circuit enumeration. It is a focused combination of object family and output-resource guarantees beside the general enumeration-class barriers.

   **Scope / condition:** Minimality, duplicate avoidance and the binary-matroid input representation matter; arbitrary dependent-set listing does not suffice.

60. **[TCS-7288: Adaptivity gap of influence maximization with full feedback](../../data/cards/TCS-7288.json)**

   Beyond worst-case and average-case analysis · Specialized model or subcase · **medium**

   The full adaptivity-gap function measures the value of observations for independent-cascade influence maximization with full-adoption feedback. Its dependence on a particular diffusion and feedback model gives it lower priority than more general online-selection and inference barriers.

   **Scope / condition:** Keep the whole n,k function in view; this proposal is not based on disallowing quantitative or functional answers.

61. **[TCS-0310: Polynomial-time weighted falsifiability of unambiguous DNFs](../../data/cards/TCS-0310.json)**

   Computational complexity · Specialized model or subcase · **borderline**

   Weighted falsifiability of an unambiguous DNF combines a narrow representation promise with optimization over its complement. I would prioritize general d-DNNF negation and equivalence, while acknowledging this is a concrete test of their underlying obstruction.

   **Scope / condition:** Easy unweighted counting does not solve binary-weight optimization, and no equivalence to the general representation problems is claimed.

62. **[TCS-1125: Sub-log-squared seeds for width-four ordered branching programs](../../data/cards/TCS-1125.json)**

   Pseudorandomness and derandomization · Specialized model or subcase · **borderline**

   This selects the first particularly small-width seed-length frontier for ordered branching programs, while TCS-6600 retains the general optimal-generator target. I would consider keeping the width-four challenge as context rather than an additional slot.

   **Scope / condition:** A constant-width case can expose a genuine general barrier. Error dependence must match the source, and the general and width-four targets are not equivalent.

63. **[TCS-1595: Decidability of fifth-order \(\beta\)-matching](../../data/cards/TCS-1595.json)**

   Automated reasoning, rewriting and unification · Specialized model or subcase · **borderline**

   Fifth-order beta-matching fills one remaining order threshold in a restricted matching hierarchy. I would treat that narrow boundary as secondary in a 500-problem benchmark, while recognizing its clear computability content.

   **Scope / condition:** Beta-only matching must not be replaced by beta-eta matching; known general matching results may use different equality rules.

64. **[TCS-1978: Search tractability of BLP-solvable promise CSPs](../../data/cards/TCS-1978.json)**

   Constraint satisfaction · Specialized model or subcase · **borderline**

   This restricts promise-CSP search-versus-decision to the BLP-solvable class, while TCS-6675 preserves the general construction barrier. Its role is an important tractable-decision subcase rather than an independently broad target.

   **Scope / condition:** A solution of this BLP case would not resolve the general promise-CSP search question; this is an editorial comparison, not a duplicate claim.

65. **[TCS-3331: DynFO maintenance of red-predecessor parity](../../data/cards/TCS-3331.json)**

   Dynamic algorithms · Specialized model or subcase · **borderline**

   The target is one parity-of-existential-coverage query in order-free, initially empty DynFO. It is a useful diagnostic example, but the specific logical maintenance convention gives it lower benchmark priority than general dynamic graph and logical expressiveness barriers.

   **Scope / condition:** This is not direct-set parity, and quantifier-free lower bounds do not resolve DynFO.

66. **[TCS-3391: Efficient learning of well-separated Gaussian mixtures](../../data/cards/TCS-3391.json)**

   Learning theory · Specialized model or subcase · **borderline**

   The remaining question is efficient global recovery of well-separated Gaussian mixtures after local EM convergence and sample guarantees are understood. I would put this favorable-distribution recovery regime below the main general learning and statistical-computational thresholds.

   **Scope / condition:** A good local initialization is not automatically available; this is a substantive rather than cosmetic algorithmic gap.

67. **[TCS-3792: Deterministic linearizable objects for set agreement](../../data/cards/TCS-3792.json)**

   Distributed, parallel and sublinear algorithms · Specialized model or subcase · **borderline**

   The target extends a task/object separation to higher set-agreement parameters while simultaneously requiring determinism, linearizability and reusable ports. That exact combination is less broadly representative than the main coordination and distributed-complexity barriers.

   **Scope / condition:** The source's k=2 separation does not prove the universal higher-k statement; the model distinction remains substantive.

68. **[TCS-4350: Uniform compressed word problem for graph groups](../../data/cards/TCS-4350.json)**

   Algebraic computation · Specialized model or subcase · **borderline**

   The remaining obstacle combines arbitrary straight-line-program compression with an input-specified graph group. I would give this particular uniform compressed-word model lower priority than the broader word, conjugacy and group-isomorphism decision barriers.

   **Scope / condition:** The uniformity obstacle is real; fixed-group algorithms and power-word algorithms do not solve it.

69. **[TCS-4454: Half-snowflake embeddings into Wasserstein p-space](../../data/cards/TCS-4454.json)**

   Geometry, topology and metric spaces · Specialized model or subcase · **borderline**

   The half-snowflake target improves universality inside the specific three-dimensional Wasserstein-p host for p greater than two. It has genuine metric content, but this host/exponent combination adds less broad coverage than the central embedding conjectures.

   **Scope / condition:** This is not the stronger near-isometry question, and planar transport results do not solve it.

70. **[TCS-4659: Determinacy of Wadge games for Muller tree languages](../../data/cards/TCS-4659.json)**

   Automata and formal languages · Specialized model or subcase · **borderline**

   This asks for ZFC provability of Wadge-game determinacy for Muller tree languages. It is substantial descriptive set theory, but its specific axiomatic-strength comparison has less direct computational payoff for this benchmark than the main automata decision problems.

   **Scope / condition:** Borel determinacy does not settle non-Borel regular tree languages; this is not a claim that the theorem is routine.

71. **[TCS-5779: Constant-factor online contention resolution for matroids](../../data/cards/TCS-5779.json)**

   Online algorithms, scheduling and packing · Specialized model or subcase · **borderline**

   This studies online contention resolution for correlated matroid activations relative to offline balance. Its close connection to the secretary programme is valuable, but I would prioritize that central programme over a separate correlated-activation comparison.

   **Scope / condition:** Do not assume independent activations or treat a conditional secretary-based result as an unconditional answer.

72. **[TCS-7196: Polynomial-time EFX for three additive agents](../../data/cards/TCS-7196.json)**

   Game theory, social choice and fair division · Specialized model or subcase · **borderline**

   The three-agent case asks for computational efficiency after EFX existence is known. It is a meaningful next threshold, but adds a more restricted target beside general EFX existence and efficient EFX approximation.

   **Scope / condition:** This is a computational question and is not equivalent to TCS-0011. Its importance as the smallest unresolved algorithmic case makes this a borderline cut.

73. **[TCS-3056: Deterministic convolution with negative entries](../../data/cards/TCS-3056.json)**

   Algebraic computation · Specific method or construction · **high**

   The target extends one fast n-fold Boolean-convolution result to signed entries. Its main contribution would be removing the no-cancellation restriction of that algorithmic setting, with less independent reach than the general convolution and algebraic-computation barriers.

   **Scope / condition:** Do not infer that all signed convolution questions are minor; this judgment concerns the selected extension and its saved efficiency target.

74. **[TCS-4293: PLS-completeness of k-means local minima](../../data/cards/TCS-4293.json)**

   Optimization and numerical computation · Specific method or construction · **high**

   PLS-completeness of finding a local optimum for the k-means method studies the inherent limitations of a particular heuristic's neighborhood. I would give the unrestricted clustering approximation and general total-search barriers higher priority.

   **Scope / condition:** A long convergence example does not by itself prove PLS-completeness.

75. **[TCS-6466: Polynomial tour complexity of BKZ](../../data/cards/TCS-6466.json)**

   Lattices and computational number theory · Specific method or construction · **high**

   The open target bounds the number of tours of the particular BKZ basis-reduction algorithm. It would strengthen analysis of an important practical method, but has less independent foundational scope than the best possible lattice-algorithm and hardness questions.

   **Scope / condition:** The count of tours is not the total cost of exact block solving; practical early stopping is not a worst-case proof.

76. **[TCS-3845: Efficient distributed multicommodity routing](../../data/cards/TCS-3845.json)**

   Distributed, parallel and sublinear algorithms · Specific method or construction · **medium**

   The selected task finds multicommodity routes inside the low-width random-network setting used to simulate parallel algorithms. I would treat this as a focused supporting construction rather than another general routing or parallel-computation benchmark.

   **Scope / condition:** Its potential improvement to parallel-to-distributed simulation is real; this is a comparative priority judgment, not merely a criticism of missing bounds.

77. **[TCS-3940: Note however that we do not know whether these lower bounds imply general algorithmic hardness.](../../data/cards/TCS-3940.json)**

   Fine-grained complexity · Specific method or construction · **medium**

   The saved direction asks to convert graph-pattern polynomial lower bounds into general algorithmic hardness. Its selected contribution remains tied to the interpretation of one algebraic lower-bound framework; broader subgraph complexity questions already express the scientific objective more directly.

   **Scope / condition:** The awkward extracted title is not the reason for removal, and method-specific hardness is not itself a general algorithmic lower bound.

78. **[TCS-4301: Two-sided hardness amplification by ODD-MAX-BIT](../../data/cards/TCS-4301.json)**

   Communication complexity and Boolean function analysis · Specific method or construction · **medium**

   The target upgrades a specific ODD-MAX-BIT amplification mechanism from one-sided hardness to ordinary two-sided approximate degree. Its wider uses are real, but the proposed theorem remains tied to this composition rather than the full hardness-amplification frontier.

   **Scope / condition:** The universal inner function and pointwise approximation convention must be preserved; known one-sided amplification does not settle it.

79. **[TCS-5288: Entropy-optimal grammar compression](../../data/cards/TCS-5288.json)**

   String algorithms and computational biology · Specific method or construction · **medium**

   The target asks whether grammar-based compression can achieve a specific entropy-optimality benchmark, already at zero order. It compares one representation family with statistical coding rather than the broad optimal grammar-size and string-algorithm frontiers.

   **Scope / condition:** Counterexamples to named compressors do not rule out all grammars, and entropy optimality is not the same as constant-factor smallest-grammar approximation.

80. **[TCS-6198: Majority hardness of balanced functions](../../data/cards/TCS-6198.json)**

   Communication complexity and Boolean function analysis · Specific method or construction · **medium**

   The question tests the source's majority-hardness notion by seeking a balanced counterexample. Its immediate payoff is a limit on that specific amplification principle, making it a lower-priority standalone target than general information compression and direct sums.

   **Scope / condition:** Majority-hardness is a source-defined predicate, not ordinary difficulty of evaluating majority.

81. **[TCS-6433: Polynomial-time Győri–Lovász partitions](../../data/cards/TCS-6433.json)**

   Algorithms · Specific method or construction · **medium**

   The target algorithmizes the exact rooted, prescribed-size Győri–Lovász partition guarantee, already at five parts. I would give this construction problem lower independent priority than general connectivity, flow and disjoint-path barriers.

   **Scope / condition:** Stronger-connectivity constructions do not resolve the original theorem's algorithmic case.

82. **[TCS-6859: Polynomial-time Gilbert–Varshamov inner-code construction](../../data/cards/TCS-6859.json)**

   Coding and information theory · Specific method or construction · **medium**

   This removes exhaustive search from the inner-code step of a Gilbert–Varshamov construction on the component's own dimension scale. Its natural role is a focused explicit-construction challenge rather than a separate general code-rate frontier.

   **Scope / condition:** It does not ask merely for a faster implementation, and should not be misrepresented as the general question of beating Gilbert–Varshamov.

83. **[TCS-3513: Explicit positive-rate codes below the Plotkin point](../../data/cards/TCS-3513.json)**

   Coding and information theory · Specific method or construction · **borderline**

   The target turns the generalized-channel CP-distribution feasibility criterion into explicit positive-rate codes. I would prioritize the central rate–distance and decoding frontiers over this construction within a more specialized channel framework.

   **Scope / condition:** This covers more than an ordinary binary Hamming channel, so the judgment is borderline and not based on the word Plotkin alone.

84. **[TCS-0344: Additivity of extension complexity under Cartesian products](../../data/cards/TCS-0344.json)**

   Optimization and numerical computation · Secondary quantitative frontier · **medium**

   The conjecture asks whether extension complexity is exactly additive under Cartesian product. It refines how two existing descriptions combine, with less direct algorithmic scope than general LP, SDP and extension-complexity barriers.

   **Scope / condition:** The possibility of sharing inequalities is a real structural question; additivity for pyramids is only a special case.

85. **[TCS-0943: Polynomial-pass barriers to near-exact streaming Max-Cut](../../data/cards/TCS-0943.json)**

   Distributed, parallel and sublinear algorithms · Secondary quantitative frontier · **medium**

   The target couples a near-exact Max-Cut accuracy depending on C with a polynomial-pass exponent barrier. It refines one problem's memory–accuracy–pass landscape beyond the broader streaming and sketching model questions.

   **Scope / condition:** The accuracy may depend on the desired pass exponent; do not strengthen this to one fixed accuracy for every exponent.

86. **[TCS-2529: Polynomial-time ultrametric embedding](../../data/cards/TCS-2529.json)**

   Geometry, topology and metric spaces · Secondary quantitative frontier · **medium**

   Exact optimization or a PTAS for the instance-optimal ultrametric embedding improves the quality of one hierarchical representation. I would give it lower priority than the main universal metric embedding and distortion questions.

   **Scope / condition:** Computing a distribution over embeddings and evaluating worst-pair expected distortion must remain separate from deterministic embeddings.

87. **[TCS-3580: Class-dependent parameter exponents for minor-closed vertex deletion](../../data/cards/TCS-3580.json)**

   Parameterized complexity and algorithms · Secondary quantitative frontier · **medium**

   This asks whether the polynomial degree in an FPT exponent must depend on the excluded-minor class. It refines dependence inside an existing tractability theorem, with less independent impact than the general kernelization and tractability barriers.

   **Scope / condition:** A limitation of irrelevant-vertex techniques is not a lower bound against every algorithm; the hypothesized complexity assumption remains to be fixed.

88. **[TCS-3690: Untuned switching regret for oblivious adversarial bandits](../../data/cards/TCS-3690.json)**

   Online algorithms, scheduling and packing · Secondary quantitative frontier · **medium**

   The target removes prior tuning of the switch budget while matching known regret rates for every comparator against an oblivious adversary. That adaptive-parameter guarantee is a narrower increment than establishing a new broad online-learning rate or learnability boundary.

   **Scope / condition:** Adaptive-adversary impossibility and algorithms told the switch budget do not resolve this untuned target.

89. **[TCS-4419: Structural randomized query lower bounds for subgraph containment](../../data/cards/TCS-4419.json)**

   Communication complexity and Boolean function analysis · Secondary quantitative frontier · **medium**

   This refines randomized subgraph-query lower bounds through parameters of the fixed pattern, including independence number. I would prioritize the general evasiveness and query-complexity barriers over additional pattern-sensitive inequalities.

   **Scope / condition:** The rationale is the extra granularity of the proposed structural bounds, not a claim that all subgraph queries behave alike.

90. **[TCS-5215: Accuracy threshold for agnostic ReLU learning](../../data/cards/TCS-5215.json)**

   Learning theory · Secondary quantitative frontier · **medium**

   This locates the accuracy threshold between known efficient and conditionally hard regimes for agnostic learning of one ReLU. It is a detailed error-versus-time frontier within a restricted predictor class rather than a general learnability classification.

   **Scope / condition:** The distribution-free and sphere-normalization conventions matter; no threshold value is asserted here.

91. **[TCS-5221: Sublinear-in-q prophet inequalities for q-matroid intersection](../../data/cards/TCS-5221.json)**

   Online algorithms, scheduling and packing · Secondary quantitative frontier · **medium**

   The selected goal improves linear dependence on the number of matroids in a prophet inequality. This is a quantitative intersection-parameter frontier, secondary to the broader secretary and online selection principles in the pool.

   **Scope / condition:** The proposal concerns the full q dependence, not merely a constant adjustment, and restricted partition-matroid examples do not settle every case.

92. **[TCS-5275: Supercritical proof size–depth tradeoffs](../../data/cards/TCS-5275.json)**

   Proof complexity · Secondary quantitative frontier · **medium**

   The target constructs a supercritical size–depth tradeoff within particular proof systems. I would rank this refined two-resource separation below the central proof-system simulations and unrestricted lower bounds.

   **Scope / condition:** The exact meaning of supercritical must come from the source; an ordinary tradeoff is not the requested result.

93. **[TCS-5330: Near-linear-query approximation schemes for matroid intersection](../../data/cards/TCS-5330.json)**

   Optimization and numerical computation · Secondary quantitative frontier · **medium**

   The remaining goal matches a randomized near-linear-query matroid-intersection approximation scheme deterministically. It sharpens the query cost and randomness of this oracle primitive rather than changing its basic solvability.

   **Scope / condition:** The target is still substantial derandomization; the existing deterministic two-thirds approximation does not settle it.

94. **[TCS-5442: Steiner Tree bidirected-cut integrality gap below two](../../data/cards/TCS-5442.json)**

   Approximation algorithms and inapproximability · Secondary quantitative frontier · **medium**

   The goal improves the integrality gap of one specific bidirected Steiner Tree relaxation below two. It evaluates the strength of that formulation more directly than the best attainable approximation for the optimization problem itself.

   **Scope / condition:** The bidirected, undirected-cut and hypergraphic relaxations are distinct; stronger-relaxation results do not settle this gap.

95. **[TCS-6768: Simultaneous polynomial-length constant-space refutations](../../data/cards/TCS-6768.json)**

   Proof complexity · Secondary quantitative frontier · **medium**

   This asks whether constant-space proofs can simultaneously have polynomial length. It is the extreme low-memory regime of a broader size–space programme already represented by more general proof-space comparisons.

   **Scope / condition:** The applicable proof system and space measure must be retained; no configuration-counting shortcut is asserted to solve it.

96. **[TCS-1133: Sub-log-squared seeds for polynomial-size CNFs and DNFs](../../data/cards/TCS-1133.json)**

   Pseudorandomness and derandomization · Secondary quantitative frontier · **borderline**

   The selected endpoint is a sub-log-squared seed for polynomial-size CNFs and DNFs. It adds a quantitative frontier for a specific circuit family to an already substantial derandomization collection.

   **Scope / condition:** Constant-error and inverse-polynomial-error results must not be conflated; this report does not claim that a later PRG solves the saved target.

97. **[TCS-4259: Query cost of reducing testing adaptivity](../../data/cards/TCS-4259.json)**

   Property testing and distribution learning · Secondary quantitative frontier · **borderline**

   The question improves universal simulation costs when reducing the number of testing batches. I would prioritize the main adaptive-query separations over a further quantitative sharpening of this simulation bound.

   **Scope / condition:** Its universal scope makes this borderline. The unspecified amount of improvement is a formulation issue, not the primary removal reason.

98. **[TCS-5031: Littlestone-dimension regret bounds for unrestricted classes](../../data/cards/TCS-5031.json)**

   Learning theory · Secondary quantitative frontier · **borderline**

   This removes a regularity restriction from the Littlestone-dimension regret characterization. With TCS-2336 already preserving the general multiclass minimax frontier, I would give a separate entry for the minimax-regularity exception lower priority.

   **Scope / condition:** Measurability and minimax conventions may distinguish the statements. Do not mark it as an exact duplicate or silently discard the unrestricted-class issue.

99. **[TCS-6721: Additive-one approximation for bin packing](../../data/cards/TCS-6721.json)**

   Online algorithms, scheduling and packing · Secondary quantitative frontier · **borderline**

   The additive-one target sharpens the already retained constant-additive bin-packing challenge TCS-6640. I would consider giving this stronger endpoint context within the same topic rather than a second independent benchmark slot.

   **Scope / condition:** One extra bin is a longstanding meaningful optimum, not a routine constant improvement. Removing this card would drop a strictly sharper target unless it is explicitly preserved.

100. **[TCS-6784: Spanners matching Thorup–Zwick emulator tradeoffs](../../data/cards/TCS-6784.json)**

   Algorithms · Secondary quantitative frontier · **borderline**

   The surviving gap is attaining the exact Thorup–Zwick emulator edge exponent with an actual spanner, rather than arbitrarily close exponents with slack-dependent constants. This is a sharper refinement than the larger additive-spanner frontiers retained elsewhere.

   **Scope / condition:** The full hierarchy and fixed constants matter; do not call the almost-matching result a resolution or conflate this with the retained four-additive problem TCS-6783.
