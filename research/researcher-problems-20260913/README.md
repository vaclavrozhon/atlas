# Researcher-linked problem additions — 13 September 2026

Applied the user’s request to add the 24 problems from the preceding discussion and choose the right category for each. The list covers 12 researchers with two connections each; the ambiguous name “ars large” was explicitly skipped. Research connections are not assertions of exclusive authorship or of a researcher’s personal ranking.

Disposition: 15 new identities, three restorations under their original identities, one completed existing index card, and five matches to existing substantive cards. No duplicate cards were created for the latter six. Canonical English content and references live only in `data/cards/`.

## Individual decisions

| Researcher | Card | Problem | Category key | Action |
| --- | --- | --- | --- | --- |
| Allan Borodin | [TCS-6575](../../data/cards/TCS-6575.json) | Deterministic competitiveness of k-server | Online algorithms | matched existing |
| Allan Borodin | [TCS-7335](../../data/cards/TCS-7335.json) | Randomized competitive ratio of list update | Online algorithms | new |
| Faith Ellen | [TCS-7336](../../data/cards/TCS-7336.json) | Common2 membership of FIFO queues | Distributed, parallel and sublinear algorithms | new |
| Faith Ellen | [TCS-7337](../../data/cards/TCS-7337.json) | Register space of obstruction-free set agreement | Distributed, parallel and sublinear algorithms | new |
| Gerth Brodal | [TCS-7326](../../data/cards/TCS-7326.json) | Worst-case logarithmic dynamic planar convex hulls | Dynamic graph algorithms | new |
| Gerth Brodal | [TCS-7327](../../data/cards/TCS-7327.json) | Buffered fully persistent search trees | Data structures | new |
| John Iacono | [TCS-0474](../../data/cards/TCS-0474.json) | Constant-update working-set heaps on pointer machines | Data structures | restore |
| John Iacono | [TCS-5706](../../data/cards/TCS-5706.json) | Unified bound for binary search trees | Data structures | restore |
| Martín Farach-Colton | [TCS-0466](../../data/cards/TCS-0466.json) | Certifying Karp–Rabin fingerprints | String algorithms and bioinformatics | restore |
| Martín Farach-Colton | [TCS-7340](../../data/cards/TCS-7340.json) | Optimal randomized memory-reallocation overhead | Data structures | new |
| Michael Bender | [TCS-0300](../../data/cards/TCS-0300.json) | Randomized complexity of online labeling | Data structures | complete existing |
| Michael Bender | [TCS-7339](../../data/cards/TCS-7339.json) | Near-linear incremental topological ordering | Dynamic graph algorithms | new |
| Mihai Pătrașcu | [TCS-6540](../../data/cards/TCS-6540.json) | Superlogarithmic static cell-probe lower bounds | Data structures | matched existing |
| Mihai Pătrașcu | [TCS-7338](../../data/cards/TCS-7338.json) | Multiphase conjecture | Data structures | new |
| Mikkel Thorup | [TCS-6537](../../data/cards/TCS-6537.json) | Expected linear-time integer sorting for every word length | Algorithms & data structures | matched existing |
| Mikkel Thorup | [TCS-7331](../../data/cards/TCS-7331.json) | Constant-time deterministic dynamic dictionaries | Data structures | new |
| Robert Tarjan | [TCS-6498](../../data/cards/TCS-6498.json) | Dynamic optimality conjecture | Data structures | matched existing |
| Robert Tarjan | [TCS-7328](../../data/cards/TCS-7328.json) | Amortized decrease-key complexity of standard pairing heaps | Data structures | new |
| Seth Pettie | [TCS-6508](../../data/cards/TCS-6508.json) | Deque conjecture | Data structures | matched existing |
| Seth Pettie | [TCS-7332](../../data/cards/TCS-7332.json) | Logarithmic Las Vegas dynamic connectivity | Dynamic graph algorithms | new |
| Stefan Langerman | [TCS-7329](../../data/cards/TCS-7329.json) | Logarithmic fully retroactive priority queues | Data structures | new |
| Stefan Langerman | [TCS-7330](../../data/cards/TCS-7330.json) | Simultaneous local and global bounds for confluently persistent tries | Data structures | new |
| Tsvi Kopelowitz | [TCS-7333](../../data/cards/TCS-7333.json) | Subquadratic-space 3SUM indexing with polylogarithmic queries | Data structures | new |
| Tsvi Kopelowitz | [TCS-7334](../../data/cards/TCS-7334.json) | Strong SetDisjointness conjecture | Data structures | new |

## Category decisions

The assigned keys reuse the existing taxonomy. `Dynamic graph algorithms` is displayed as Dynamic algorithms and includes the planar convex hull, graph connectivity and incremental topological ordering. Integer sorting stays in `Algorithms & data structures` (displayed as Algorithms). List update and k-server stay in Online algorithms. Concurrent queues and register-space set agreement belong to Distributed, parallel and sublinear algorithms. Fingerprint certification belongs to String algorithms and bioinformatics. The remaining questions concern basic representations, priority queues, search trees, allocators or space-query bounds and belong to Data structures. Each card records its own rationale.

## Duplicate and model distinctions

- TCS-6498 already supplies the splay-tree dynamic-optimality conjecture; do not add a second generic dynamic-optimality entry.
- TCS-6508 already supplies Tarjan’s deque conjecture, here linked to Pettie’s research direction.
- TCS-6537 already asks for expected linear-time integer sorting for every word length; only mathematical typesetting was repaired.
- TCS-6540 is retained as the existing explicit, near-linear-space static cell-probe barrier. Its saved space budget is n times squared log n. The broader discussion also mentioned polynomial superlinear space; this audit does not assert that the two regimes are equivalent or strengthen the existing benchmark without notice.
- TCS-6575 retains the established function target for the deterministic k-server ratio, with the repository’s pointwise 1/100 tolerance. The k-server conjecture would determine this function; no second yes/no card is added.
- TCS-0300 was an unfinished index entry. It now has a complete constant-slack randomized list-labeling formulation, references to Saks and the See-Saw work, and upper/lower-bound context.
- Standard two-pass pairing heaps are distinct from the removed pure-pairing-heap card TCS-6514. The July 2026 standard-heap improvement is an announcement in the cited pure-heap preprint; the card does not represent it as an independently checked companion proof.
- The logarithmic Las Vegas connectivity target is distinct from TCS-6625’s deterministic worst-case polylogarithmic target. The dynamic dictionary target is distinct from TCS-6586’s static construction problem.
- The weak polylogarithmic-query 3SUM-indexing target is retained; the already-refuted stronger tradeoff conjecture is not added.
- The near-linear topological-ordering target asks for maintained order comparisons. Almost-linear cycle detection alone does not solve it, and the seminar’s more specific combinatorial improvement is not asserted equivalent.
- Multiphase uses charged word-RAM preprocessing; unrestricted-preprocessing cell-probe variants and semi-adaptive lower bounds are not silently identified with it.
- The allocator target is worst-case expected movement overhead for general allocators. The February 2026 lower bound applies to general allocators, and resizability and history-independence are not imposed.
- Numerical and function targets retain explicit Lean absolute-error tolerance 1/100, including register counts. Asymptotic-complexity targets require matching constant-factor bounds.

## Authorized restorations

The latest request to add the discussed problems supersedes earlier selection removals for TCS-0466 (fingerprint certification), TCS-0474 (pointer-machine working-set heaps), and TCS-5706 (the unified BST bound). Those three entries were removed from the active deletion guard and restored under their existing IDs. No other deletion disposition was changed. `decisions.json` records the superseded reasons, without storing duplicate card content.

## Source and formulation limits

Source checks were bounded and performed on 13 September 2026. Cited 2026 preprints were not independently proof-verified. Cards use `source_open` where a source states an open target, rather than claiming exhaustive present-day certification. Older-source confidence is explicitly qualified for deterministic dictionaries, confluent tries, and Common2 queues.

The confluent-trie minimum-bound question is deliberately marked `needs_specification`: the navigation records retained by later updates and the depth/size convention for copies between versions still need exact combined accounting. The source’s minimum expression is preserved without pretending the entire benchmark has been settled editorially. All other newly authored or completed cards have explicit model, quantifiers, cost and acceptance criteria.

For buffered full persistence, the source’s qualitative efficient-cloning question is sharpened editorially to simultaneous buffered bounds, constant-I/O cloning and linear history space; this is clearly distinguished from a literal conjecture in the source. Other explicit benchmark choices, including the polynomial 3SUM universe and constant slack for list labeling, are recorded on their cards.

## Validation

- `make publish` passed after the final card edits and refreshed the local reader and exports.
- `make check` passed: schema and taxonomy validation, related-problem consistency, export parity, repeatable publication, stable-ID/deletion protections, and deployment tests against a temporary local repository.
- `node tests/math.cjs` passed for all active-card formulas. The check initially found an unsupported LaTeX command in the new pairing-heap card; that presentation issue was corrected before the successful run.
- `git diff --check` passed.
- A targeted manifest check confirmed that all 24 intended IDs are active, their saved categories match the decisions, and the 12 researchers each have exactly two entries. Category totals are 15 Data structures, three Dynamic algorithms, two Online algorithms, two Distributed/parallel/sublinear, one Algorithms and one String algorithms/bioinformatics.

The workspace also contains independent ongoing catalog edits. These totals describe this request’s 24 decisions; global catalog totals are not attributed solely to this batch.
