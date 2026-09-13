# Second 300-card fundamentality screen — 11 September 2026

The user accepted the previous removals, requested a brief pass through every
remaining card, and authorized another 300 deletions. The starting pool contained
1,977 canonical cards. This run removed exactly 300, leaving 1,677. All 300 had
active statuses (`open`, `source_open`, or `uncertain`); no resolved or excluded
record was used to reach the count. No focus choice needed removal.

## Scope and method

Every starting card received a brief editorial screen of its title and saved
question. Source-question excerpts and summary context were used when the formal
field was boilerplate. Every removal candidate additionally received a reading
of its full saved working summary and substantive importance rationale. Records
edited concurrently were read again before application; a hash check covered
the complete current pool immediately before deletion.

This was a selection screen, not a full formulation or literature review. It
does not certify that retained questions remain open, or that removed questions
are resolved. Decisions concern the breadth and consequences of the problem,
not its category population, score, rank, publication venue or ease of
formalization. Precise general complexity questions and consequential small
canonical problems remain eligible, including nonbinary targets.

## Removal types

Each removal has one primary editorial classification; the types overlap in
ordinary language.

| Type | Cards | Selection rationale |
| --- | ---: | --- |
| Specialized model or variant | 141 | A particular graph class, automaton extension, oracle, geometric representation, game convention or combination of restrictions, without sufficient broader consequences for this pool. |
| Quantitative refinement | 80 | A sharper exponent, logarithmic factor, parameter range, query tradeoff or protocol overhead within an established problem. |
| Particular method or construction | 53 | An auxiliary lemma, translation, reduction, algorithm family or construction route rather than an independently central target. |
| Vague or bundled direction | 26 | Unselected guarantees, subjective requirements or several source-specific follow-ups combined into one direction. |

## Concrete examples

| ID | Removed target | Why it was below the cutoff |
| --- | --- | --- |
| TCS-0346 | Negative contractible marked walks on a genus-two surface | A narrowly constrained topological routing variant. |
| TCS-1468 | Four-sided skyline reporting at ordinary range-reporting cost | A specialized geometric query tradeoff. |
| TCS-1792 | Improve the 1.7088 exponential base for Equal Subset Sum | A numerical exact-algorithm refinement. |
| TCS-3268 | Remove a log-log factor from a permutation-program PRG seed | A quantitative construction improvement. |
| TCS-3722 | RLBWT-to-LZ77 conversion in linear time and run-linear space | A resource tradeoff between two text representations. |
| TCS-4713 | Symmetric two-sided lossless expanders for quasi-cyclic quantum codes | An auxiliary construction tailored to one code framework. |
| TCS-4878 | Adversarial soundness of binned Boson Sampling validation | Assessment of one proposed diagnostic method. |
| TCS-4916 | Beat exponent 2+1/22.5 for low-accuracy infinity regression | A fine runtime improvement under a matrix-multiplication assumption. |
| TCS-5197 | Find one satisfactory definition of reconstruction-attack success | A conceptual definition agenda without a fixed acceptance criterion. |
| TCS-6290 | Randomized bottom-up BST rebalancing under local restrictions | A particular implementation family rather than general search-tree optimality. |

## Records and publication

- `baseline.json`: starting IDs and hashes, with no archived card bodies.
- `read-ledger.json`: fields inspected and last-read hashes for all 1,977 cards.
- `decisions.tsv`: exactly 300 individually written reasons and primary types.
- `applied.json`: the 300 applied ID/reason tombstones, including saved source locators.
- `run.json`: counts and initial publication version.
- `read.py`: a display and reading-ledger helper; it does not choose or delete cards.

Canonical removals are recorded in `data/deleted_records.json`; their card files
were removed. Stable IDs and source-key reservations remain in the registry.
The publisher regenerated the reader, rankings, benchmark exports and update
snapshot from the remaining canonical records.

## Validation

- `make check` passed the isolated data, ranking, category, relation, export,
  deletion, import-protection and deployment checks.
- `make check-web` passed reader navigation, benchmark/export parity, mobile
  layout, deletion updates, missed snapshots and account-free notes tests.
- All 300 tombstones match the applied reasons. The remaining ID set equals the
  1,977 starting IDs minus exactly those 300 IDs. None appears in the published
  catalogue or any of the three benchmark exports.
- Top 100 contains 100 cards, Top 500 contains 494, and the possible Top 1000
  export contains 937. Category shortfalls were left explicit.

The browser check had assumed the editorial catalogue must contain a related
pair. It now supplies and restores a browser-only fixture. This also exposed a
navigation bug: clicking a related link to the current hash did not reveal the
target after search had hidden it. The reader now handles that same-hash click
explicitly; both layouts pass the regression check. No artificial relationships
were added to canonical cards.

## Deployment

The updated reader was pushed to `gh-pages` at commit
`7a36efb54560268db9dcf4fbeadc55c337c1cfd2`; GitHub's Pages build and deployment
completed successfully. Its catalogue version is `7b702c0c6f0f7d4ec056`.
The final build also picked up concurrent edits to retained cards, including
related-problem links; these are not counted as removals in this run.
`deployment.json` records the deployed snapshot and checks, and
`live-verification.json` records the public catalogue check.
