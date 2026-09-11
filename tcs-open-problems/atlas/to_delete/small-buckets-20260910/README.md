# Preliminary pruning of the 25 small categories — 10 September 2026

**2,939 candidates → 1,104 retained; 1,835 provisionally quarantined.**

The first snapshot contained 2,572 small-category candidates. A concurrent textbook/survey import added 367; those questions were also screened. The final count refers to the candidate pool of all 25 small categories, not to the whole atlas. This pass does not change the decisions of the separate large-category batch.

The review prioritizes central computational barriers, general decision problems, major conjectures and broad algorithmic primitives. Lower-priority variants, paper-specific follow-ups, requests for alternative methods, vague directions and extraction fragments were provisionally removed. Saved questions/source topics were read category by category, followed by an excerpt audit of ambiguous retained records and a rescue pass for landmark topics. Existing individually reviewed cards and approved fundamental proposals were preserved. There was no score cutoff, age cutoff or requirement to keep the same fraction of every category.

These are editorial importance decisions, not completed open-status reviews or a guarantee that every survivor belongs in the final top 1,000. Quotas of 20 per small category have not been applied. A short card or an incomplete formulation alone was not a reason to discard a major problem. Semantic deduplication and exact comparisons between overlapping formulations remain incomplete.

| Category | Before | Quarantined | Retained |
|---|---:|---:|---:|
| Approximation algorithms and hardness of approximation | 277 | 206 | 71 |
| Parameterized and exact algorithms | 502 | 365 | 137 |
| Fine-grained complexity | 76 | 33 | 43 |
| Pseudorandomness and derandomization | 133 | 66 | 67 |
| Proof complexity | 148 | 95 | 53 |
| Communication complexity and Boolean function analysis | 126 | 66 | 60 |
| Coding and information theory | 113 | 65 | 48 |
| Algebraic computation | 163 | 86 | 77 |
| Lattices and computational number theory | 55 | 26 | 29 |
| Randomized algorithms and sampling | 55 | 36 | 19 |
| String algorithms and bioinformatics | 138 | 97 | 41 |
| Dynamic graph algorithms | 54 | 30 | 24 |
| Counting and enumeration | 122 | 77 | 45 |
| Property testing and distribution learning | 88 | 45 | 43 |
| Differential privacy | 29 | 8 | 21 |
| Algorithmic game theory, mechanism design and fair division | 119 | 78 | 41 |
| Constraint satisfaction | 96 | 53 | 43 |
| Scheduling and packing | 101 | 67 | 34 |
| Automated reasoning and unification | 102 | 70 | 32 |
| Database theory and finite model theory | 117 | 75 | 42 |
| Computability and algorithmic information | 129 | 80 | 49 |
| Knowledge representation and reasoning | 17 | 6 | 11 |
| Structural graph theory | 81 | 41 | 40 |
| Beyond worst-case and average-case analysis | 76 | 46 | 30 |
| Miscellaneous | 22 | 18 | 4 |
| **Total** | **2939** | **1835** | **1104** |

## Files and reversibility

- `records.json`: full pre-removal records, including statements, references, source notes, stable IDs and original subjects.
- `manifest.json`: live quarantine decisions with individual reasons and previous selection categories. Only `state: "quarantined"` excludes an entry.
- `decisions.csv`: searchable removal ledger, including the saved target and source locator.
- `all-reviewed.csv`: all retained and quarantined decisions, including the later source imports.
- `catalog-before.json.gz`: complete catalogue immediately before this batch was applied.
- `review-input.json`, `late-additions.json`, `editorial-decisions.json`, `late-decisions.json`, `adjustments.json` and audit text files: the frozen review inputs and reasoning.

The default UI omits quarantined records. The Selection scope filter and direct stable-ID links still expose them with the removal reason. Full exports retain them, and browser notes/bookmarks remain attached to the same IDs. No source, canonical card, reference or mathematical status field was deleted or overwritten by the pruning mechanism.

To restore one or more records without overwriting any later editorial improvements:

```bash
python3 atlas/to_delete/small-buckets-20260910/restore.py TCS-1165 --dry-run
python3 atlas/to_delete/small-buckets-20260910/restore.py TCS-1165
python3 atlas/to_delete/small-buckets-20260910/restore.py --all
```

Run from the repository root. The script updates this manifest and republishes under the shared publication lock; it does not copy stale text back from the snapshot. The table above records the original decision, while later restorations are recorded in the manifest.

## Two individually checked historical targets

TCS-6720 asks for a constant-factor approximation for asymmetric metric TSP; [Svensson, Tarnawski and Végh](https://arxiv.org/abs/1708.04215) supplied one. TCS-7115 states the finite-template CSP dichotomy; [Bulatov](https://arxiv.org/abs/1703.03021) proved it (independently also Zhuk). These dated source records were archived with explicit resolution references in the decision ledger; their original status fields remain preserved. This spot check is not an exhaustive audit of the present status of the other questions.

## Verification

Checks passed for exact full-record snapshots and SHA-256, all 7,156 stable IDs, source-annotation preservation, unchanged large-category membership, all 25 candidate counts, repeat-publication idempotence and full-batch restoration using an isolated manifest. JSON, CSV, live-update data and the offline reader agree.

Browser checks covered the actual 2,939 → 1,104 update while editing a subsequently archived record: note text and focus survived, only 17 cards were rendered, and there were no browser errors. Archive reasons, prior categories, direct links, reload-persistent notes, BB(6), mobile width and offline small-category filtering passed. The portable ZIP was refreshed from the reader files and passed CRC/export consistency checks. The measured browser test duration is recorded as an end-to-end value, not a main-thread blocking measurement.

Results: [data/restoration validation](validation.json), [browser validation](browser-validation.json), [offline ZIP validation](offline-validation.json). The existing 35-category UI regression and 555-entry source-import preservation checks also passed.
