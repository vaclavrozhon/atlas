# Approved additions — 11 September 2026

The user approved adding all fourteen recommendations after the source review.
All fourteen were imported as new canonical cards, with no skipped records.
The importer reserved stable IDs **TCS-7241–TCS-7254** and their source keys in
`data/id_registry.json`. Each card includes a self-contained statement and
model definitions, an answer criterion, source-linked context and progress,
an individual importance assessment, review dates and a five-sentence summary.

| Recommendation | Canonical card | Category key | Editorial importance |
| --- | --- | --- | ---: |
| R1 | [TCS-7241: FPT approximation of twin-width](../../data/cards/TCS-7241.json) | Parameterized and exact algorithms | 94 |
| R2 | [TCS-7242: PL four-sphere recognition](../../data/cards/TCS-7242.json) | Computational geometry and metric spaces | 94 |
| R3 | [TCS-7243: Stable ternary compaction circuits](../../data/cards/TCS-7243.json) | Computational complexity | 89 |
| R4 | [TCS-7244: Boolean dimension of planar cover graphs](../../data/cards/TCS-7244.json) | Structural graph theory | 88 |
| R5 | [TCS-7245: Subcubic treewidth sparsifiers](../../data/cards/TCS-7245.json) | Structural graph theory | 90 |
| R6 | [TCS-7246: Minimum-color cycle](../../data/cards/TCS-7246.json) | Structural graph theory | 85 |
| R7 | [TCS-7247: Automatizing MWIS](../../data/cards/TCS-7247.json) | Parameterized and exact algorithms | 88 |
| R8 | [TCS-7248: Tutte’s 5-flow conjecture](../../data/cards/TCS-7248.json) | Structural graph theory | 97 |
| R9 | [TCS-7249: Berge–Fulkerson](../../data/cards/TCS-7249.json) | Structural graph theory | 94 |
| R10 | [TCS-7250: Barnette](../../data/cards/TCS-7250.json) | Structural graph theory | 94 |
| R11 | [TCS-7251: Caccetta–Häggkvist](../../data/cards/TCS-7251.json) | Structural graph theory | 96 |
| R12 | [TCS-7252: Tuza](../../data/cards/TCS-7252.json) | Structural graph theory | 93 |
| R13 | [TCS-7253: Seymour’s second neighborhood](../../data/cards/TCS-7253.json) | Structural graph theory | 94 |
| R14 | [TCS-7254: Neumann–Lara](../../data/cards/TCS-7254.json) | Structural graph theory | 92 |

Importance scores are individual scientific judgments, not the ordering of the
source-review shortlist. That shortlist preferred broad additional coverage.
The importer did not change category quotas or explicit benchmark focus choices;
normal publication derives the remaining ranking from the saved scores.

## Formulation and status decisions

TCS-7246 fixes ETH as a standing hypothesis. The original author explicitly
allows an ETH-based obstruction, and the recommendation left this convention
to card authoring. An exact polynomial-time algorithm answers positively; a
proof that any such algorithm would contradict ETH answers negatively. A
stronger unlisted hardness assumption is insufficient. The hypothesis is
visible in the title, statement, definitions and acceptance criterion.

TCS-7247 uses binary maximum/addition gates, zero as the only constant, and
counts all gates including inputs. Its size parameter requires correctness for
all nonnegative real weights; its algorithm handles binary nonnegative integer
weights with bit cost. The cited all-real-weight circuit parameter is equivalent
up to linear overhead, preserving polynomial automatization. The target is
computing the optimum, not necessarily outputting a circuit.

TCS-7253 has `status: uncertain`: the May 2026 complete-proof claim conflicts
with a later specialist paper explicitly retaining the general conjecture.
Both sources and their dates are present. Formulation review is complete, but
neither correctness nor acceptance of the full-proof claim is certified.
The other thirteen cards use `source_open`, with dated review limitations.

The stable-compaction reference was checked against its bibliographic metadata:
its preprint revision is 26 October 2020 and the conference is SODA 2021.
It is not labeled as a 2022 preprint revision.

## Validation

The prepared batch passed the canonical record validator before import, including
categories, evidence/status fields, citation IDs and five-sentence summaries.
The import returned fourteen new IDs and no skipped records.

- `make publish` passed and rebuilt the local reader and exports.
- `make check` passed: category and ranking consistency, nested benchmark
  exports, clean rebuilds, canonical-input preservation, import/deletion guards,
  and deployment tests against a temporary local Git remote.
- A batch-specific check confirmed that all fourteen canonical records and
  registry mappings appear in the generated catalogue with their exact authored
  statements and summaries. None was added to the explicit focus prefix.
- Report links, reference IDs and new-file whitespace checks passed.

The generated status counts for this batch are thirteen `source_open` and one
`uncertain`. No production deployment or Git commit was made for this addition.

The source-review ledger and comparison metadata retain their historical
pre-import meaning. Canonical card files above are the current editable content;
the temporary authoring batch stays in ignored `cache/`.
