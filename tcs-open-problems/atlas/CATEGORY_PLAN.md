# Agreed category plan and proposed alternatives

Updated 2026-09-10. The applied plan contains 10 large groups of 50 and 25 small
groups of 20: all 1,000 planned places now have a named category. Beyond worst-case
and average-case analysis fills the last small slot. Current counts are in
[the category report](site/category-sizes.md).
New alternatives below are suggestions, not accepted replacements.
Apply [SELECTION_POLICY.md](SELECTION_POLICY.md), including the intentional
exclusion of most general combinatorics and the accepted structural graph scope.

## Agreed large categories — 50 each

1. Quantum computation
2. Computational geometry and metric spaces
3. Computational complexity
4. Algorithms & data structures
5. Learning theory
6. Cryptography
7. Distributed, parallel and sublinear algorithms
8. Automata and formal languages
9. Semantics, logic and verification
10. Optimization and numerics

## Agreed small categories — 20 each

1. Approximation algorithms and hardness of approximation
2. Parameterized and exact algorithms
3. Fine-grained complexity
4. Pseudorandomness and derandomization
5. Proof complexity
6. Communication complexity and Boolean function analysis
7. Coding and information theory
8. Algebraic computation
9. Lattices and computational number theory
10. Randomized algorithms and sampling
11. String algorithms and bioinformatics
12. Dynamic graph algorithms
13. Counting and enumeration
14. Property testing and distribution learning
15. Differential privacy
16. Algorithmic game theory, mechanism design and fair division
17. Constraint satisfaction
18. Scheduling and packing
19. Automated reasoning and unification
20. Database theory and finite model theory
21. Computability and algorithmic information
22. Knowledge representation and reasoning
23. Structural graph theory
24. Beyond worst-case and average-case analysis
25. Miscellaneous

## Accepted scope merges — 2026-09-10

- Former small category 18, Computational social choice, is absorbed into
  small category 16, Algorithmic game theory, mechanism design and fair division.
  Its scope includes voting and preference aggregation; its name and target of
  20 remain unchanged.
- Former small category 20, Computational topology, is absorbed into large
  category 2, Computational geometry and metric spaces. Its scope now explicitly
  includes computational topology; its name and target of 50 remain unchanged.
- The two former standalone small categories are removed from the agreed plan.
  Remaining small categories are numbered consecutively above. These are scope
  merges, not exclusions of their problems. Structural graph theory now fills
  one freed slot; the remaining slot was subsequently filled by Beyond worst-case and average-case analysis.

## Accepted addition — Structural graph theory, 20 problems

The user accepted **Structural graph theory** as a small category on 2026-09-10.
Its TCS-oriented scope is graph minors and
decompositions; treewidth, clique-width, twin-width and related parameters;
sparse graph classes, separators and logical characterizations; hereditary
classes, forbidden induced subgraphs and coloring structure; and selected
expansion/girth questions with computational consequences. Structural bounds
and characterizations would belong here, while running-time questions for
particular algorithms would normally remain in ADS or Parameterized and exact
algorithms. This supersedes the earlier default exclusion of structural graph
theory within this agreed scope. The broad general-combinatorics exclusion
remains in force.

Examples already represented in the catalogue include TCS-5475 (graph-minor
structure bounds), TCS-0342 (twin-width of string graphs), TCS-6178 (shrub-depth
obstructions and MSO), TCS-1206 (sparse graph classes and logical stability),
TCS-2371 (spectral expanding expanders), and TCS-6500 (girth and spanners).
These are candidate topic examples, not a new verification of their open status.

## Discussion candidates — not accepted changes

Possible categories to merge into other groups or replace:

- Small 10, Randomized algorithms and sampling: prefer narrowing this broad
  label to Sampling, Markov chains and mixing times. General randomized
  algorithms already occur throughout ADS, complexity and other groups.
  Sampling remains distinct from derandomization and should not be lost.
- Small 18, Scheduling and packing: a weaker candidate if another slot is
  needed. Its topics can be retained in Optimization and numerics and in
  Approximation. Its original pool of 76 records also supports keeping it.

Potential additions:

- Reconfiguration and computational games: algorithms and complexity of moving
  between feasible solutions, token swapping, recoloring, and games/puzzles.
  Focus on computational questions rather than restoring pure combinatorics.
  The coverage audit identified 31 game/puzzle records with 21 distinct saved
  source titles; that is not a deduplicated open-problem count.
- Molecular computing and programmable matter: chemical reaction networks,
  tile assembly, and computational models of programmable matter. The audit
  identified 14 records with 11 distinct saved source titles; a target of 20
  would require further collection and review.

Another possible rename, without adding a category: expand small 12 to
Dynamic and temporal graph algorithms. The original groups contain 42 dynamic
and 36 temporal records; they are distinct models that can share a selection
bucket.

The user accepted the social-choice and topology merges and the addition of
Structural graph theory. Beyond worst-case and average-case analysis now fills the remaining slot. Other
suggestions in this discussion section remain unapproved.

Counts and source records: [coverage audit](research/taxonomy-coverage-20260910.md).

## Accepted addition — Beyond worst-case and average-case analysis

Small category 24, target 20, added on 2026-09-10. Miscellaneous remains last,
now small 25. Includes beyond-worst-case input models, average-case complexity
and hardness, smoothed and semi-random analysis, planted problems, instance-optimal
algorithms and algorithms with predictions. General statistical sample complexity,
cryptographic assumptions and quantum topics keep their specialist homes.
The combined name is the working interpretation of the user's suggestion to
include average-case analysis. Kernelization was discussed but not added.
