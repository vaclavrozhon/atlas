# Parallel card review — 15 September 2026

This checkpoint contains four individual card reviews against the content standard of `TCS-0001` (P versus NP). Worker `card-review-third-862815` used the existing shared reservation infrastructure while two other review processes were active. All four reservations were completed and released.

## Completed cards

| Card | Result |
| --- | --- |
| [TCS-0841](../../data/cards/TCS-0841.json) | Specify adaptive conditional access to two unknown distributions, including zero-mass queries, total variation, error and worst-case query cost. Request constant-factor dependence on domain size at each fixed distance. Record that the checked 2024 result resolves the main historical gap up to suppressed logarithmic factors; mark the remaining exact target **uncertain**. |
| [TCS-0848](../../data/cards/TCS-0848.json) | Retain the source's polynomial-query question for arbitrary real-valued set functions. Specify one-sided error, normalized Hamming distance, exact value access, uniform computation and the universal polynomial bound. Separate bounded-range Lp results from this target, including the September 2026 paper. |
| [TCS-1029](../../data/cards/TCS-1029.json) | Define ordinary fixed-pattern copy counts, matrix-normalized edit distance, strict farness and the feasible parameter domain. Ask for matching bounds in both proximity and graph order, with constants depending only on the pattern. Record the counting and precision conventions as editorial specifications. |
| [TCS-1030](../../data/cards/TCS-1030.json) | Replace the broad classification programme with the concrete conjecture of polynomial one-sided testing for induced four-cycle freeness, following explicit user authorization. Specify uniform induced-subgraph sampling, allowed edge edits, distance normalization and rejection probability. |

Every card now includes definitions, quantifiers, a Lean proof acceptance criterion, source-linked context and progress, a five-sentence working summary, and a dated formulation/status review. Existing importance scores are preserved. The rationale for TCS-1030 was reassessed for its selected target, with the previous assessment retained in its provenance.

## Authorized target revision: TCS-1030

The user explicitly chose: “Vybrat konkrétní užší tvrzení a výslovně zaznamenat změnu cíle” (choose a concrete narrower claim and explicitly record the target change).

The inherited question was Goldreich's Open Problem 8.26, a characterization of all dense graph properties testable with polynomial reciprocal-distance query complexity, allowing two-sided error. The selected target is Conjecture 3.6 of Gishboliner–Shapira's 2025 survey: polynomial testing of induced four-cycle freeness. The canonical test samples at most a fixed polynomial in reciprocal distance many vertices, queries all their pairs, and rejects exactly upon seeing an induced four-cycle.

These questions are not equivalent. The card's `target_revision` preserves the old title, target, references and importance assessment; its earlier textbook notes and index provenance remain. The revised context and summary also explain the change. The selected target did not duplicate an active card or the recorded reason for the previously retired general proximity-oblivious characterization card.

## Source handling

Primary problem statements, source definitions and relevant theorem statements were inspected individually. References in the cards identify the exact versions and locators. [source-cache.json](source-cache.json) records hashes and locations of inspected local PDF/text copies; downloaded copies are kept in the ignored source cache. The original submodularity problem page was recovered from its previously saved full text when live access failed.

The status review is bounded and dated 15 September 2026. It does not independently verify complete source proofs, certify exhaustive literature coverage, or provide Lean formalizations. In particular, TCS-0841 does not present the historical gap as wholly unresolved after the SODA 2024 result.

## Coordination and validation

- Claimed inputs were checked by token and SHA-256 before each completion. Canonical writes, queue updates and ledger appends used `.publish.lock` and `complete_review.complete`.
- An initial export failure exposed that `source_formulation` must be an object. The two affected records were corrected under the shared lock, and their updated hashes and amendments were recorded before publication succeeded.
- Browser inspection then caught the default “Original source wording” caption on editorial paraphrases. All four cards now explicitly label these as editorial paraphrases and cite the source. This correction is also recorded in the ledger.
- `make publish` rebuilt local reader exports after completed edits. No remote deployment is part of this checkpoint.
- `make check` passed on an isolated snapshot, including schema/export consistency, ranking, taxonomy, related links, publication, deployment tests against a temporary local Git remote, and reservation infrastructure tests.
- `node tests/math.cjs` passed for 1,049 active cards and 19,047 expressions: parsing, balanced delimiters, preserved formulas and escaped HTML.
- A focused browser audit checked these four cards in compact and full layouts at widths 1,440 and 390 pixels. Published content matched canonical fields, expanded details and mathematics rendered, and there were no KaTeX errors, browser errors, failed HTTP responses or page-wide horizontal overflow. Desktop and mobile screenshots of TCS-1030 were also visually inspected. The audit was repeated after the caption correction.
- Final queue records were checked against canonical output hashes, and this worker held no remaining reservations. Other processes' cards and claims were left to their owners.

See [verification.json](verification.json) for the final card hashes and check results, and [browser-audit.json](browser-audit.json) for the 16 layout/card cases. This is a four-card checkpoint, not completion of the entire review queue.
