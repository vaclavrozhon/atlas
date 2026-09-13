# External open-problem collections — 11 September 2026

**Subsequent action:** the user approved all fourteen additions. They are now
canonical cards TCS-7241–TCS-7254; see [the import record](imported.md).
The review and its original comparison counts below describe the pre-import state.

**Recommendation: discuss fourteen additions, with the first seven preferred
for additional coverage.** The remaining seven are major graph conjectures to
compare with the existing category selection. This review changes no cards,
ranks, benchmark selections or publication files.

Start with [the justified recommendations](recommendations.md): precise targets,
significance, literature evidence, nearby Atlas records and suggested categories.
[The exclusion and follow-up notes](notes.md) explain resolved traps, existing
coverage and alternatives. The [source-by-source ledger](screening.csv) records
all **1,783 source entries**, compared against **7,231 current/historical Atlas
identities**, with eight additional removed direction IDs kept reserved.

## Recommended set

| Priority | Candidate | Contribution to coverage |
| --- | --- | --- |
| R1 — preferred | FPT approximation of twin-width | Finding a decomposition without one supplied. |
| R2 — preferred | PL four-sphere recognition | A fundamental computability boundary in topology. |
| R3 — preferred | Linear-size stable ternary compaction circuits | A concrete Boolean circuit-size target. |
| R4 — preferred | Boolean dimension of planar cover graphs | Sparse order structure and reachability representation. |
| R5 — preferred | Constant-factor subcubic treewidth sparsifiers | Preserving graph structure after sparsification. |
| R6 — preferred | Polynomial-time minimum-color cycle | An explicit optimization target beyond the present quasipolynomial bound. |
| R7 — preferred | Automatization of MWIS dynamic programming | Uniform algorithms competitive with the best tropical circuit. |
| R8 — graph comparison | Tutte's 5-flow conjecture | Integral-flow existence. |
| R9 — graph comparison | Berge–Fulkerson conjecture | Perfect-matching covers. |
| R10 — graph comparison | Barnette's conjecture | A canonical planar Hamiltonicity boundary. |
| R11 — graph comparison | Caccetta–Häggkvist conjecture | Directed degree versus short cycles. |
| R12 — graph comparison | Tuza's conjecture | Triangle packing versus covering. |
| R13 — graph comparison | Seymour's second-neighborhood conjecture | Directed local expansion; proof-claim conflict recorded. |
| R14 — graph comparison | Neumann–Lara's planar two-color conjecture | Partition into acyclic directed subgraphs. |

This order is editorial judgment under [the Atlas rules](../../docs/RULES.md).
Several preferred candidates also belong to graph theory; compare them jointly
with R8–R14 and existing graph records. The 100/500 and possible 1,000-problem
selections and quotas remain unchanged. Formalization effort did not affect
selection. These are discussion candidates, not fourteen approved imports.

## Coverage

The seven requested collections contributed **1,354 entries**:

| Collection | Entries | Coverage |
| --- | ---: | --- |
| [OpenTCS](https://opentcs.cc/problems/) | 296 | All problem tiles; original linked sources used for interpretation. |
| [Marwaha](https://tcsopenproblems.com/) | 13 | All questions and discussions; main targets have current or historical Atlas counterparts. |
| [Sublinear.info](https://sublinear.info/) | 102 | Entire numbered index, statements and posted progress updates. |
| [TOPP](https://topp.openproblem.net/) | 78 | Entire numbered index, including solved and partly solved pages. |
| [Open Problem Garden](https://www.openproblemgarden.org/) | 707 | Union of paginated subject indices, including 273 spam/test/nonproblem entries; mathematical entries screened for accepted scope and relevant formulations inspected. |
| [Amarilli](https://a3nm.net/work/research/questions/) | 74 | 55 listed open, 13 solved and 6 retired; linked-collection hub also followed. |
| [cstheory open-problem tag](https://cstheory.stackexchange.com/questions/tagged/open-problem?sort=votes) | 84 | All questions returned by the tag API; 222 returned answers consulted as discovery/status context. |

Expansion contributed **429 additional entries**:

| Linked collection | Entries | Coverage |
| --- | ---: | --- |
| [Automata Exchange](https://automata.exchange/) | 102 | Full paginated index. |
| [RTA](https://www.cs.tau.ac.il/~nachum/rtaloop/) | 107 | All numbered pages, including source-marked solutions. |
| [TLCA](https://tlca.di.unito.it/opltlca/) | 26 | All numbered problems, including five source-marked solved entries. |
| [West](https://dwest.web.illinois.edu/openp/) | 76 | Full index and relevant linked formulations; editorial list positions identify entries. |
| [Trotter](https://people.math.gatech.edu/~trotter/rprob.html) | 17 | All headings; one is an introduction. |
| [Bonnet](https://perso.ens-lyon.fr/edouard.bonnet/openQuestions.html) | 6 | All twin-width questions. |
| [Korhonen](https://tuukkakorhonen.com/problems.html) | 8 | All questions; three now marked solved by the author. |
| [Separability workshop](https://gitlab.com/gze/open-problems-separability/-/wikis/home) | 13 | All numbered questions and recorded updates. |
| Three cstheory collection threads | 74 | Answers to questions 174, 38560 and 22493 separately inventoried; overlap the answer context above. |

These are **source occurrences, not 1,783 distinct currently open problems**.
Twenty occurrences lead to fourteen recommendations. Secondary copies, solved
entries, introductions and repeated discussions remain in the audit.

Expansion is finite, not a traversal of every recursively linked website.
[The hub inventory](linked-collections.json) records Amarilli's collection links.
Wikipedia's CS list was compared with the repository's
[same-day existing audit](../wikipedia-20260911/README.md), not counted as a fresh
traversal. The broad Erdős database and MathOverflow general-math thread were
inspected as scope/discovery hubs; their entire contents were not enumerated.
The unfiltered cstheory unanswered feed was outside the inventory. PolyTCS, the
Garden-derived graph mirror and Monniaux's polyhedral representation discussion
served as contextual leads, not independent status authorities or additional
complete inventories.

## What the ledger certifies

Each row identifies the source, disposition, reason and evidence. `atlas_ids`
records substantive comparison or source provenance; `retrieval_leads` contains
only similarity candidates, never duplicate decisions. Numbered source URLs
were normalized; shared collection roots were excluded from exact matching.

| Disposition | Meaning |
| --- | --- |
| `recommend` | R1–R14, with comparison and current literature check. |
| `represented_target` | A main target compared with the named Atlas record. |
| `source_already_indexed` | Source provenance overlap; not equivalence of every subquestion on a composite page. |
| `related_existing`, `repair_existing_first` | A relation or repair opportunity, short of equivalence. |
| `resolved_literature` | Later work answers the specified target; preprint and verification limits remain in the notes. |
| `source_reports_solved`, `source_reports_retired` | Collection-reported disposition, not an independent proof audit. |
| `partial_resolution` | Only a stated portion/model/range is settled. |
| `defer`, `needs_formulation` | No recommendation yet; formulation or status issues remain explicit. |
| `scope_or_priority` | No sufficiently strong admission case under current scope/priorities; not blanket rejection of graph theory. |
| `resource_or_discussion`, `spam_or_nonproblem` | Not an independent mathematical problem to import. |

This is systematic screening, **not a complete literature review for every
entry**. Current literature checks concentrate on recommendations, plausible
near misses and apparent resolutions. Residual `defer` rows remain visible
instead of being labeled duplicates, solved or unimportant without evidence.
No mathematical proof was independently verified, formally or otherwise.

## Comparison evidence

The project was reorganized and other cards reviewed concurrently. Initial
comparison used 2,759 catalogue records; final state labels were refreshed from
`data/cards/`. All final active IDs were already in the 7,231-identity corpus.
The eight reserved direction IDs lack recovered full cards and were checked
through saved removal reasons.

[review-metadata.json](review-metadata.json) records counts, observed Git HEAD
and hashes; [baseline.json](baseline.json) identifies the initial catalogue.
Historical records were read from snapshots and Git history, including fifteen
otherwise missing identities from the old large-bucket snapshot.
[comparison-register.json.gz](comparison-register.json.gz) retains only IDs,
state labels and deletion reasons. It is not a restoration archive.

Downloaded pages, full temporary catalogue copies, extraction helpers and raw
similarity results remain in ignored local `cache/`, outside the versioned
report. The report is auditable through source URLs, locators, Atlas IDs and
Git history. Re-fetching websites later need not reproduce the same counts or
status labels.
