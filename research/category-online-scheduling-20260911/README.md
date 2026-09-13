# Merge online algorithms with scheduling and packing

Approved by the user on 11 September 2026. The combined small category uses the
`online` ID and `Online algorithms` stable key; its current display label comes
from `categories.json`. It occupies the former online position after approximation.

All 25 active scheduling/packing records join the 80 online records. The merged
pool contains 105 candidates. No record is removed or restored, and statements,
working summaries, sources, statuses and importance scores are preserved.
Historical scheduling keys remain valid for imports, overrides and archive
manifests, without recreating a separate active category.

The two focus places pair the deterministic k-server conjecture (TCS-6575) with
unrelated-machine makespan (TCS-6638). Bandit convex optimization (TCS-6577),
precedence-constrained makespan (TCS-6676) and bin packing (TCS-6640) remain active
below the two-place prefix, in their existing score order.

There are now 10 large and 24 small categories. The combined bucket retains the
usual quota of 2/20 for Top 100/1000. One small-category slot is reserved for a
future decision, accounting for 2/20 unassigned benchmark places. Against the
saved baseline, the selections contain 98 and 964 records; the latter also has
the existing one-place cryptography and fifteen-place miscellaneous shortfalls.

## Evidence and checks

- `before.json.gz`: complete catalogue before the merger.
- `before-categories.json`, `before-benchmark_selection.json`: previous registry
  and focus review.
- `dry-run.json`: exact migration check on the frozen baseline, including all
  4,472 archived records and every non-routing card field.
- `verification.json`: published catalogue and export checks.
- `checks.log`, `checks.json`: `make check` passed (exit 0), covering ranking,
  taxonomy, all 555 source entries and repeated isolated publication.
- `browser-validation.json`: browser checks for the merged category and benchmark
  exports; desktop and mobile screenshots accompany the report.

The previously delivered PDF and its frozen source snapshot remain dated artifacts.
Current JSON, CSV, offline-reader and summary exports follow the combined category.

Validation completed successfully: all data checks, both browser suites and visual
inspection of the combined category on desktop and mobile passed.
