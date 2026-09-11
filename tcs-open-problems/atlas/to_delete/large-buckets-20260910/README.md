# Preliminary pruning of the ten large categories

Editorial selection recorded on 10 September 2026. This is a reversible candidate-pool reduction, not final selection of 50 problems per category.

Reviewed **4,203** large-category records; provisionally archived **2,069**; retained **2,134**. The initial pool was 4,098; 105 concurrently imported large-category records were included in the same review. The 25 small categories were outside this pruning pass.

| Category | Before | Moved here | Retained |
| --- | ---: | ---: | ---: |
| Quantum computation | 411 | 226 | 185 |
| Computational geometry and metric spaces | 583 | 271 | 312 |
| Computational complexity | 338 | 155 | 183 |
| Algorithms & data structures | 788 | 437 | 351 |
| Learning theory | 384 | 209 | 175 |
| Cryptography | 172 | 84 | 88 |
| Distributed, parallel and sublinear algorithms | 398 | 175 | 223 |
| Automata and formal languages | 339 | 144 | 195 |
| Semantics, logic and verification | 445 | 216 | 229 |
| Optimization and numerics | 345 | 152 | 193 |

## What was moved

| Reason | Records |
| --- | ---: |
| Unusable fragments, local proof/algorithm commentary and background passages | 668 |
| Paper-specific extensions and refinements | 1013 |
| Narrow variants or residual special cases | 354 |
| Restatements with a retained candidate identified | 16 |
| Research directions, model proposals or engineering tasks without one specified question | 14 |
| Already resolved according to the existing individual review | 4 |

## Review method and limits

All records in the ten current large buckets were screened from their saved titles and formulations, using the recorded source context and existing editorial judgments. The explicit per-ID decisions are saved in the research directory. No score threshold, publication-year cutoff or per-category removal quota was used. In a second look, 524 initially flagged borderline records were retained; well-defined specialist questions and potentially important barriers receive the benefit of doubt. Retention is not certification that an entry is open or belongs in the final 1,000.

The review does not freshly establish current open status. Four records were already marked resolved by their existing individual reviews. A malformed excerpt is removed as an atlas entry, without a claim that every question in its source is unimportant. The `fragment` label includes incomplete or anaphoric statements and should not be read as claiming every such passage is a literal extraction false positive. Concrete false positives have more specific reasons.

## Files

- [records.json](records.json): complete frozen copies of all provisionally removed cards, including IDs, formulations, references, status, importance and source provenance.
- [manifest.json](manifest.json): persistent decisions and explanations. Publication reads `records[ID].state`; `quarantined` excludes a record and `retained` restores it.
- [decisions.csv](decisions.csv): readable decision table with individual anchors and retained IDs for restatements.
- [all-reviewed.csv](all-reviewed.csv): decisions for all 4,203 screened large-category records.
- [catalog-before.json.gz](catalog-before.json.gz): full pre-pruning publication, including all categories.
- [restore.py](restore.py): reinstate current versions without overwriting newer editorial work.

The snapshot and the counts above describe this review at publication time. A later restoration does not rewrite the historical snapshots or original decision CSV; current state is in `manifest.json` and the regenerated atlas. The frozen archive SHA-256 is recorded in the manifest.

## Where the records appear

The default atlas and its large-category counts show retained candidates. Use **More filters → Selection scope → Archive** to inspect preliminary removals. Their badges distinguish them from subject-scope exclusions. Direct links, references and browser notes keep the same stable IDs. Full exports continue to include archived records. The independent source library remains outside the atlas UI.

## Restoration

From the atlas root, first inspect a proposed restoration:

```sh
python3 to_delete/large-buckets-20260910/restore.py --dry-run TCS-6462
```

Reinstate that record and republish:

```sh
python3 to_delete/large-buckets-20260910/restore.py TCS-6462
```

To reverse this entire provisional batch:

```sh
python3 to_delete/large-buckets-20260910/restore.py --all
```

Restoration lifts only this batch’s quarantine. Other explicit subject-scope decisions still apply. The tool retains current card content; it does not reload stale text from the snapshot. Repackage the portable ZIP after a later restoration if using that separate copy.
