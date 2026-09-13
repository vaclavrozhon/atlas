# Three additions and three completed records

The user approved these six changes on 11 September 2026 after the previous
five-GPT/five-Claude batch. Three new cards were authored and three existing
records were completed under their original identifiers. All six have explicit
statements, definitions, answer criteria, primary references, dated progress and
individual importance assessments. Their short summaries were updated where an
existing summary would otherwise describe an obsolete draft.

| Action | ID | Target | Bucket | Position |
|---|---|---|---|---:|
| Add | TCS-7240 | Output-polynomial vertex enumeration of bounded rational polytopes | Counting and enumeration | 4 |
| Add | TCS-7238 | Sound polynomial-time refutation of random 3-SAT at constant density | Beyond worst-case and average-case analysis | 5 |
| Add | TCS-7239 | Greedy CDCL without restarts p-simulating resolution | Automated reasoning and unification | 4 |
| Complete | TCS-5773 | Decidability of the general integer Skolem problem | Semantics, logic and verification | 7 |
| Complete | TCS-4245 | Parity games in deterministic polynomial time | Semantics, logic and verification | 6 |
| Complete | TCS-0026 | L = BPL | Pseudorandomness and derandomization | 3 |

Positions are from catalogue version `9abfd29259986cb02ca4`. The existing Top 100
focus prefixes are preserved. Parity games move from position 129 to 6 after an
individual score of 99 replaces the provisional unassessed score of 50. Skolem
moves from 10 to 7, with score 98; BPL moves from 5 to 3, with score 97. These are
editorial assessments of scientific importance, independent of proof verification
or current-status certification.

The same positions were verified after the concurrent repository reorganization
in version `61c93a48ce5deedba424`. Canonical cards now live in `data/cards/`
under their `TCS-....json` identifiers; the local reader export lives in `web/`.

## Exact formulations and source checks

- **Vertex enumeration:** boundedness, variable dimension, degeneracy, empty
  instances, binary rational input/output and total output size are explicit.
  [Reimers–Stougie](https://arxiv.org/abs/1404.5584v2) distinguish the bounded
  question from the unbounded case. The more recent
  [hyperplane-arrangement algorithm](https://arxiv.org/abs/2401.16675) measures
  a different output; it is not treated as a solution for one inequality-defined
  polytope. No claim of polynomial delay is added.
- **Random 3-SAT:** the card asks the user's exact-satisfiability variant, allowing
  classical randomization but never an incorrect UNSAT answer. Clauses are sampled
  independently with replacement; the constant density is chosen before the
  input size. [Allen–O'Donnell–Witmer](https://www.cs.cmu.edu/~odonnell/papers/random-csp-refutation.pdf)
  define sound refutation and distinguish stronger gap certification. The
  [Feige-hypothesis formulation discussed by Barak](https://eccc.weizmann.ac.il/report/2012/120/revision/1/download/)
  also requires soundness on nearly satisfiable formulas. These are not silently
  identified, and consequences of the gap hypothesis are not assigned to the new
  card. The [2026 CSP result](https://arxiv.org/abs/2604.27336) generalizes
  density/degree/strength tradeoffs without settling this constant-density target.
- **CDCL:** the operational rules are based on Paper D, Section D.2, of
  [Vinyals' thesis](https://jakobnordstrom.se/docs/publications/MV_PhDthesis.pdf).
  The card fixes greedy propagation and conflict processing, arbitrary trivial
  asserting analysis, conflict-driven assertion-level backjumping, optional legal
  learned-clause deletion, and no restarts or preprocessing. It explicitly asks
  for a polynomial-time translation of a supplied resolution proof. This is not
  a claim about autonomous proof search, every fixed learning heuristic, or the
  equivalence of this trace model with pool resolution.
  [Vinyals' 2022 exposition](https://simons.berkeley.edu/sites/default/files/docs/21462/satreunionslides-marcvinyals.pdf)
  distinguishes non-greedy and preprocessing simulations, and
  [Buss–Thapen's 2026 paper](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/heightTradeoff/)
  explicitly leaves its proposed related separation unproved.
- **Skolem:** preserves the general discrete integer recurrence, with arbitrary
  order and no supplied index bound. The
  [corrected July 2026 low-order revision](https://arxiv.org/abs/2507.11234v3)
  and [July 2026 conditional result](https://arxiv.org/abs/2607.15510) are recorded
  with their respective restrictions. The original 2022 source and quotation
  remain attached to TCS-5773.
- **BPL:** fixes uniform machines, polynomial worst-case time, logarithmic counted
  work space and fresh independent coins. The target is equality of language
  classes, not a uniform compiler or one particular generator construction.
  [Hoza's simulation](https://drops.dagstuhl.de/storage/00lipics/lipics-vol207-approx-random2021/LIPIcs.APPROX-RANDOM.2021.28/LIPIcs.APPROX-RANDOM.2021.28.pdf)
  and the latest displayed revision of
  [the 2026 weighted-PRG paper](https://eccc.weizmann.ac.il/report/2026/064/)
  do not establish logarithmic-space derandomization.

## Parity-games status caveat

The statement and review of TCS-4245 are complete, but its current status is
explicitly **unverified**, not certified open.

[Van der Heijden's November 2025 preprint](https://arxiv.org/abs/2511.03752v1)
claims a polynomial-time solution to the full problem. The arXiv record inspected
here displayed that claim without a withdrawal notice. This review inspected the
paper but did not independently verify its proof, produce a counterexample or
locate an authoritative adjudication of correctness.

[Suilen–Pérez, April 2026](https://arxiv.org/abs/2604.26748) still describe
polynomial-time parity-game solving as open. That is evidence of later usage,
not a refutation of the earlier claim. Both records appear in the card's sources,
context, progress and status note. The reader displays `Current status unverified`.
The importance change does not certify or reject the claimed solution.

## Verification

[changes.json](changes.json) records identifiers and actions.
verify.py checks that exactly three IDs were added and that only the
three approved existing records changed their saved research fields. It also
checks canonical/export agreement, primary-source provenance, complete-card
fields, preserved focus selection and the explicit parity-games status caveat.
Results are saved in verification.json.

The strict first-publication check is preserved in
initial-publication-verification.json:
at that point every other record's checked research fields were unchanged.
While the standard checks ran, ten other cards acquired independent
`quality_review` updates. Their observed hashes and changed fields are recorded
in concurrent-changes.json. The final validation keeps
those edits and checks the six cards in this batch against their canonical files;
it does not attribute those ten changes to this task.
The public catalogue subsequently switched to an active-record-only export in
another concurrent change. Final validation accepts that representation only
when it contains exactly the original 2,756 active identifiers and these three
additions. The complete initial publication contained 7,231 records; the active
export contains 2,759. This task does not restore archived records into that export.

The baseline in before.json keeps content hashes for all previous
records and full snapshots for the three reviewed records. The original source
references and historical identifiers remain in the completed cards.

Standard publication checks run through `make check`; their output is in
make-check.log. That suite passed before the concurrent
directory reorganization; canonical/export agreement and the six-card browser
check were rerun successfully against the new paths afterward. The six-card
browser check checks models and references, the visible
parity-games caveat and mobile overflow for the long CDCL definition. Completion
results are recorded in checks.json and
browser-check.json.

Source searches are not a proof that no later result exists. No cited proof was
formally verified in this editorial task, and no proposed solutions or suggested
intermediate goals were inserted into the problem statements.
