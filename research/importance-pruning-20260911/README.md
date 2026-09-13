# Individual importance review — 11 September 2026

All **2,695 active candidates across 35 categories** received an individual
assessment against the importance, interest, foundations and community-relevance
criteria in [atlas rules](../../docs/RULES.md). The final pass
archives **10 records**, leaving **2,685 active candidates**: six narrow research
follow-ups and four source-extraction errors. No score threshold or category
removal quota was used.

The complete review is in all-reviewed.csv, with one row per
originally active ID, an individual rationale, the available community evidence,
source references and the final removal decision. Review categories are frozen;
publication categories preserve the independent concurrent category review.

| Reviewer | Individually assessed records |
| --- | ---: |
| Algorithms agent | 813 |
| Geometry agent | 662 |
| Logic agent | 604 |
| Root | 616 |
| Total | 2,695 |

The numbered removal reasons
include source locations and the limits of each judgment. The
archive README explains
restoration. All 7,156 stable IDs remain available, including earlier archives.

The first assessment used each saved question, working summary and source
metadata. Ambiguous targets and proposed removals received additional source
context checks. These assessments are editorial judgments from saved evidence,
not a fresh literature search or citation census for every record. Retention
does not certify that a problem is currently open, distinct, precisely formulated
or ready for the final benchmark.

[CALIBRATION.md](CALIBRATION.md) records the user's rejection of the Path ORAM
bucket refinement, the request for more context about information leakage in OR,
and the reason for retaining the initially suspect ABR hashing question.
The OR record remains active. Other rescues after fuller source reading are
recorded in the agents' context notes.

Three preliminary removal candidates were not selected: TCS-5384 needs a clearer
assessment of what an alternative private-optimization mechanism would enable;
TCS-2671 is a duplicate-formulation issue involving a fundamental target already
represented by TCS-0027; and TCS-3808 remains flagged as a technical question
answered within its source. These last two findings belong in the recorded
deduplication and source-status follow-up, alongside other historical questions
identified in the agents' notes. This pass does not silently convert an
importance verdict into a current-status claim.

Source reading also exposed **11 incorrect working summaries**. Their original
and corrected five sentences, source locations and reasons are preserved in
[summary-corrections.json](summary-corrections.json). Only the summary overlays
were corrected; those edits do not promote the records' evidence or research
status. The immediate pre-archive snapshot includes these corrections.

Validation commands, run from the repository root:

```sh
make check
python3 tcs-open-problems/atlas/qa/importance_review.py
node tcs-open-problems/atlas/qa/selection-pruning.cjs
```

The batch audit checks complete review coverage, original archive snapshots,
stable IDs and research fields, preservation of prior manifests and concurrent
category edits, summary corrections and export agreement. It is a historical
batch audit; later intentional content changes can invalidate its snapshot
comparisons. The publication regression separately tests restoration after newer
summary edits. Browser validation checks archived records, reasons, sources,
corrected summaries, persistent notes and mobile width against the running UI.

Results are saved in validation.json and
browser-validation.json. All checks passed, including
the restoration dry run; [test-results.json](test-results.json) links the reports
and the complete publication regression output.
