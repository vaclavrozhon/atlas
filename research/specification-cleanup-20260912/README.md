# Specification cleanup — 12 September 2026

Later the same day, the user authorized reconsideration under the numerical and
curve policy. The [quantitative review](../quantitative-questions-20260912/README.md)
restored TCS-0318, TCS-1010, TCS-6606, TCS-7210, TCS-7211 and TCS-7214.
It supersedes their deletion decisions below; the counts here describe the
earlier pass and are retained as dated history.

The user asked to review active cards marked as needing specification and either
complete them or remove them. The review covered the 103 initially flagged cards
and two newly flagged cards encountered during concurrent editorial work.
Ten specifications were completed and 95 cards removed. Immediately after the
changes, no active card retained `statement_review.status: needs_specification`.

Every disposition was considered individually from the saved statement, remaining
issue and source-recovery notes. Additional primary-source reading was used for
the ten completed specifications and selected difficult model comparisons.
This is not a fresh literature review of all 105 problems. Deletion means the
inherited benchmark was not retained under the user's specify-or-delete decision;
it does not claim that its underlying research topic is unimportant or resolved.
The removal decision overrides the earlier policy of keeping these incomplete
cards in the active pool. Other unfinished drafts without this flag were outside
the requested screen.

| Card | Completed specification |
| --- | --- |
| TCS-7272 | NISZK versus SZK, stated equivalently as a deterministic reduction between explicitly defined sampling-circuit promise problems. |
| TCS-7276 | RSA versus factoring for exponent 65537: exact balanced-prime ensemble, inverse-polynomial average success on both sides and unrestricted existence implication. |
| TCS-7277 | PKE implies unleveled FHE: IND-CPA experiment, circuit-family correctness and circuit-independent compactness. |
| TCS-7278 | PKE implies IBE: adaptive identity challenge, key-extraction access, correctness and polynomial parameter bounds. |
| TCS-7285 | Strongly explicit Ramanujan families: effective unbounded sizes, fixed-degree uniform rotation map, port and multigraph conventions. |
| TCS-7286 | CLS versus FP, stated equivalently through the discrete Either-Solution problem with complete input/output relations. |
| TCS-7288 | Influence adaptivity gap: all outgoing edge states of reached vertices, fixed live-edge randomness and per-realization seed budget. |
| TCS-7293 | Improper learning of two Boolean-cube halfspaces: supplied target-length bound, exact example interface, circuit hypotheses and polynomial bit costs. |
| TCS-7298 | Variable-rank entrywise ℓ₁ approximation: rational factors, real optimum, polynomial bit costs and exact handling of zero optimum. |
| TCS-7310 | CTMDP reachability: measurable timed positional policies, generator semantics and the source's strict vector threshold. |

The two discrete class formulations are source-equivalent replacements for missing
protocol or numerical definitions, supported by
[Goldreich–Sahai–Vadhan](https://eccc.weizmann.ac.il/report/1999/013/download) and
[Fearnley–Goldberg–Hollender–Savani](https://arxiv.org/abs/2011.01929).
The influence feedback correction follows
[Chen–Peng, Section 2](https://www.microsoft.com/en-us/research/uploads/prod/2019/09/isaac19_adaptivityGapFullAdoption.pdf).
The change from an imported non-strict comparison to a strict vector predicate
follows [Majumdar–Salamati–Soudjani, Problem 1](https://doi.org/10.4230/LIPIcs.ICALP.2020.133).
Other editorial numerical and family conventions are identified in each card's
`statement_review`; evidence levels and source-open status were preserved.

The removed set includes TCS-0318, TCS-1010 and TCS-6606 from the explicit focus
selection. Their underlying quantities were already defined, but their saved
reviews had no accepted answer representation that excluded an operational
restatement. This pass did not silently replace them with a selected conjectured
bound, a computability question or a new expression grammar. Their focus entries
were removed. Existing category quotas and the ranking rules remain the basis for
generated benchmark membership; no replacement focus choice was invented.

[ledger.json](ledger.json) gives all individual outcomes and reasons.
[summary.json](summary.json) records counts and the affected focus IDs.
The canonical deletion log reserves removed IDs and stores their specific reasons
and saved source links. No removed card snapshots were created. The active quality
queue was reconciled with these outcomes.

Publication and validation results are recorded in [validation.json](validation.json).
