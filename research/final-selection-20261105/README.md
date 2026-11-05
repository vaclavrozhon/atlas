# Final-selection review — 5 November 2026

The initial proposal assigns every active card a color: **500 green and 646 red**.
There are **10 large and 25 small categories**. Every category initially meets
its 25/10 green target; manual review may change those counts. This is a proposal
for the user to review, not a declaration that human finalization is complete.

## Editorial changes

- Split Structural graph theory from Graph algorithms; merge privacy into Cryptography.
- Merge Automated reasoning into Logic, verification and automated reasoning.
  Retain large Automata and formal languages and small Database theory.
- Split Algebraic algorithms from Algebraic complexity.
- Rename the former beyond-worst-case category Average-case analysis, retaining
  random, planted and smoothed models and moving other models elsewhere.
- Restore 14 candidates whose recorded first public solution was in 2026; nine
  are green. Preserve the scientific status and proof-review caveats.
- Develop archived TCS-0495 (linear rules with transitivity), add TCS-7512
  (primary-key consistent query answering) and TCS-7513 (bag-query resilience),
  and move TCS-6380 (parallel joins) into Database theory. See database-research.json
  for the CONCUR, KDD and database-venue search and deduplication decisions.
- Add nine diverse Miscellaneous candidates: union-closed sets, Hadamard matrices,
  cap sets, lonely runners, Nivat, distinct subset sums, Rota’s basis conjecture,
  Feige’s small-deviation conjecture and Langton’s ant. Move C7 Shannon capacity
  here; retain the existing sunflower and 1/3–2/3 partial-order candidates.
  Claimed solutions to two new candidates are explicitly qualified on their cards.
- TCS-7376 already represents the proposed streaming Euclidean MST problem and
  is green; no duplicate was added.

Fifteen modest balancing moves were applied; before-images are in
selection-moves-before.json. Current category remains the default. The interface
offers exactly one large/small pair on 220 cards and preserves color when moving.
Diversity informed editorial choices; no square-root quota was imposed. The
general Exact Matching problem TCS-6511 is green, its bipartite case TCS-0611 red.

## Exception with positive votes

All 86 other upvoted catalogue cards are green. **TCS-6168 is red** despite its
two positive votes: TCS-4786 retains the central Minimum Circuit Size Problem,
and TCS-0020 retains the direct circuit lower-bound question for EXP. TCS-6168
asks for a conditional implication between these themes; its place goes to the
PCP representative TCS-7268. This is a diversity choice, not an implication claim.
The explanation is displayed beside the red card. Votes were rechecked immediately
before publication (votes-prepublication.json).

## Shared review

Use Edit selection and the team editor key. The private local key is outside Git
at ~/.config/atlas-notes/selection-editor-token (mode 0600). Public visitors see
the selection; editors can toggle colors and use the offered up/down moves.
The sidebar counts all greens against the target, independently of search/color
filters. All/Green/Red filters support reviewing the proposed dataset.

Initial defaults live in data/final_selection.json. The existing Sites service
stores manual overrides separately with revision checks and idempotent retries.
Publication never resets those overrides. No edit-history, undo or versioned
export feature was added. The older Top 100/500/1000 ranking views remain in About
and do not determine green membership.

Community feedback remains in research/community-feedback-20261105/ and the
existing service. The reader does not fetch or display it, and generated card
exports omit community_reviews. Canonical cards and original contributions remain
intact. The GitHub new-problem form still preserves unsent local drafts.

## Validation and deployment

- Isolated data/publication checks passed, including cutoff eligibility.
- The service passed 12 real-SQLite tests covering notes, proposals, votes and selection.
- Browser checks cover shared editors, read-only visitors, counts above/below quota,
  conflicts, lost replies, reloads, publication, map synchronization and mobile widths.
- All 1,146 cards render in both layouts: 85,955 formula renderings without errors.
  A pre-existing word-boundary truncation bug was fixed without changing statements.
- Service version 4 deployed successfully from commit
  c8c607e74b1c16ef14a79437f9a1f81cebd9708e, preserving the existing site and D1 database.
- The reader is published at https://vaclavrozhon.github.io/atlas/ (Pages commit
  e703509240f008c13de48153a5ebf0c1585286a4). See deployment.json and ui/live.json.
- A real editor color change was observed by an independent visitor, restored to
  its original value and confirmed after reload. The live total remains 500 green.
- All 19 original public notes, the proposal list and 97 aggregate vote records
  are unchanged after deploying the service.

## Deferred work

**Do not begin phase 4 until the user finalizes the green cards.** Then remind
them to run the whole-catalogue web search for solvedness and the numeric-answer
precision audit, including exponents at additive accuracy 0.01. TCS-0154’s earlier
correction remains. Targeted research for new/restored candidates was in scope;
it does not certify the rest of the catalogue’s current status.

## Initial category counts

| Category | Green / target | Candidates |
| --- | ---: | ---: |
| Computational complexity | 25 / 25 | 65 |
| Algorithms | 25 / 25 | 34 |
| Automata and formal languages | 25 / 25 | 40 |
| Logic, verification and automated reasoning | 25 / 25 | 80 |
| Distributed, parallel and sublinear algorithms | 25 / 25 | 55 |
| Optimization and numerical computation | 25 / 25 | 38 |
| Geometry, topology and metric spaces | 25 / 25 | 46 |
| Learning theory | 25 / 25 | 42 |
| Cryptography and differential privacy | 25 / 25 | 46 |
| Quantum computation and information | 25 / 25 | 52 |
| Computability and algorithmic information theory | 10 / 10 | 32 |
| Proof complexity | 10 / 10 | 26 |
| Communication complexity and Boolean function analysis | 10 / 10 | 29 |
| Fine-grained complexity | 10 / 10 | 27 |
| Pseudorandomness and derandomization | 10 / 10 | 39 |
| Parameterized complexity and algorithms | 10 / 10 | 37 |
| Approximation algorithms and inapproximability | 10 / 10 | 27 |
| Online algorithms, scheduling and packing | 10 / 10 | 29 |
| Average-case analysis | 10 / 10 | 16 |
| Sampling, Markov chains and mixing times | 10 / 10 | 17 |
| Counting and enumeration | 10 / 10 | 24 |
| Structural graph theory | 10 / 10 | 32 |
| Graph algorithms | 10 / 10 | 22 |
| Data structures | 10 / 10 | 28 |
| Dynamic algorithms | 10 / 10 | 29 |
| String algorithms and computational biology | 10 / 10 | 25 |
| Game theory, social choice and fair division | 10 / 10 | 28 |
| Algebraic algorithms | 10 / 10 | 27 |
| Algebraic complexity | 10 / 10 | 36 |
| Lattices and computational number theory | 10 / 10 | 28 |
| Coding and information theory | 10 / 10 | 25 |
| Property testing and distribution learning | 10 / 10 | 19 |
| Constraint satisfaction | 10 / 10 | 18 |
| Database theory | 10 / 10 | 16 |
| Miscellaneous | 10 / 10 | 12 |
