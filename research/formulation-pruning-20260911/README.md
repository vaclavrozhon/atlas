# Formulation and scope pruning — 11 September 2026

This is the continuation of the quick catalogue screen, following the user's
clarification to retain precise, consequential questions (including exact values
and optimal asymptotic complexity), and remove vague or narrow research directions.
The user then asked for a source-based specification attempt on TCS-5661,
TCS-2541 and TCS-2334, with deletion if a faithful specification was unclear.

The 380 flagged entries were skimmed individually for target and scope. The
flags were triage aids, not automatic deletion rules. Most flags were harmless:
for example, a simple graph is a defined object, and a general optimal-complexity
question need not have a binary answer. This was not a full mathematical or
current-status review. Retention does not certify completeness, importance or
current openness.

The resulting changes remove 21 entries and narrow TCS-3228 to the explicit
Sparse Complexity completeness question stated immediately after its original
broad question in the primary source. It remains a draft; the source's definitions
and reduction convention still require full formulation review.

For the three requested specification attempts, the primary passages were read:

- TCS-5661: [ESA 2019, page 3](https://doi.org/10.4230/LIPIcs.ESA.2019.2).
  The asymptotic sorting-network bounds already occur in the source's account
  of known constructions. No mathematical simplicity criterion is supplied.
- TCS-2541: [DISC 2023, introduction and conclusion](https://doi.org/10.4230/LIPIcs.DISC.2023.31).
  The paper identifies very high communication and decision costs but does not
  fix the cost and probability bounds that would constitute practicality.
- TCS-2334: [ITCS 2023, Open Question 4](https://doi.org/10.4230/LIPIcs.ITCS.2023.89).
  Complementation is mentioned, but the additional closure operations and exact
  comparison guarantee are not fixed.

All three were deleted: supplying these choices would invent a new target.
The precise individual reasons, including primary locators, are in
[removals.json](removals.json) and the canonical deletion log. Only IDs and
reasons are kept for deleted entries; there are no archived card snapshots.

[ledger.json](ledger.json) records each screened ID's disposition.
[retained-notes.json](retained-notes.json) records selected retention decisions
and short source-recovery notes for the separate full-review process.
[validation.json](validation.json) records publication and verification results.

No focus choice was among the removed entries. Historical IDs remain reserved.
The change concerns local canonical data and generated reader exports.

The catalogue decreased from 2,714 to 2,693 cards. `make check` and
`make check-web` passed. The removed IDs are absent from the canonical card
directory, JSON and CSV catalogues, offline JavaScript and all benchmark exports.
The deletion log reserves IDs even when no historical source-key mapping exists.
