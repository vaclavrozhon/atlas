# Category boundaries from user feedback — 11 September 2026

The user asked to classify a few ambiguous cards together and apply the resulting
preferences to related cards. This round concerns four examples. The saved card
statements and summaries provide the topic evidence; no new mathematical or
current-open-status review was performed.

## Direct feedback

| Card | User response | Action |
| --- | --- | --- |
| TCS-6623: worst-case trace reconstruction | Undecided | Retain String algorithms and computational biology. The assistant recommended information theory, but the user did not adopt that recommendation. |
| TCS-6542: learning parity with noise | Undecided | Retain Learning theory. The assistant recommended keeping this category; no general LPN routing rule was approved. |
| TCS-6674: truthful unrelated-machine scheduling | Game theory, social choice and fair division; the incentive not to lie is decisive | Retain the category and record the explicit rationale on the card. |
| TCS-6637: constant-colour colouring of three-colourable graphs | Constraint satisfaction; constraint satisfaction under a promise | Retain the category and record the explicit rationale on the card. |

## Applied to neighbouring cards

Both moves below are editorial applications of the user's preference for
TCS-6637, not additional individually approved answers. Each input has a strong
colourability promise, and every local colouring constraint must still be
satisfied with the relaxed output palette. A palette growing with input size
does not define a single fixed-template PCSP; the grouping is thematic.

| Card | Previous category | New category | Reason |
| --- | --- | --- | --- |
| TCS-6725: colour a promised three-colourable graph with O(log n) colours | Approximation algorithms and inapproximability | Constraint satisfaction | The same input promise and proper-colouring task as TCS-6637, with a logarithmic output palette. |
| TCS-3984: colouring hardness for two-colourable 3-uniform hypergraphs | Approximation algorithms and inapproximability | Constraint satisfaction | The promise is a two-colouring satisfying all triples; the target concerns satisfying the same constraints with more colours. |

## Boundary checks

The active cards were screened for promise colouring and for truthfulness,
incentive compatibility, strategic reports and mechanism design. Candidate
matches were checked against their saved targets and summaries.

| Cards | Decision and reason |
| --- | --- |
| TCS-3231, TCS-5941, TCS-6632, TCS-6957, TCS-6958 | The neighbouring incentive and mechanism questions already belong to game theory. No category move is needed. |
| TCS-5017 | Retain learning: "truthful" refers to correctly labelled added examples, not an incentive constraint. |
| TCS-6638, TCS-6676 | Retain scheduling: the target contains no strategic misreporting requirement. |
| TCS-5425 | Retain distributed/parallel: the saved question asks for NC construction of an allocation, not a truthfulness guarantee. |
| TCS-1168 | Retain approximation pending recovery of the directed-colouring convention; the saved summary explicitly identifies this missing definition. Do not infer a local constraint model from the title. |
| TCS-2625 | Retain approximation: the promise permits deletion of vertices and the target is an almost-colouring/independent-set hardness gap, rather than satisfying all colouring constraints. |
| TCS-0594, TCS-6651 | Retain structural graph theory: diameter-restricted recognition and the relation between chromatic number and clique minors are different targets. |
| TCS-0548 | Retain counting/enumeration: the target is enumeration of induced subgraphs. |
| TCS-4187 | Retain proof complexity: the target is the size of polynomial-calculus proofs. |
| TCS-7237 | Retain constraint satisfaction: its three-versus-six colouring hardness target already follows the user's preference. |

Only `area` and `category_assignment` change in the canonical cards. The two
directly confirmed cards only receive a more specific assignment rationale.
Stable IDs, statements, source provenance, status, importance scores, category
registry, deleted-record policy and explicit focus selections are preserved.
`decisions.json` stores the prior assignment fields for all four edited cards;
`validation.json` records publication and preservation checks. Generated category
counts and ranks follow the two moves.

Other work concurrently updated source-file paths and consolidated unrelated
records. The validation report records those external differences from the
initial snapshot. They were retained; preservation checks for this batch compare
the four edited cards directly with their originals and verify the two undecided
cards separately. No claim of an unchanged entire working tree is intended.
