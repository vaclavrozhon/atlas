# Canonical atlas data

`cards/TCS-XXXX.json` is the only editable source for a problem. Each file contains
its statement, definitions, answer criterion, background, source references,
review status, category, importance assessment and optional working summary.
Drafts remain drafts: moving them into this directory does not certify their
formulation or current open status. Follow [the atlas rules](../docs/RULES.md).

- `categories.json`: category IDs, stable keys, labels, order and quotas.
- `benchmark_selection.json`: ordered focus choices and their editorial reasons.
- `criteria.json`: scientific selection criteria and labels.
- `metadata.json`: dataset background and methodology.
- `deleted_records.json`: deleted IDs mapped to removal reasons; no archived cards.
- `id_registry.json`: historical source-key-to-ID mappings. IDs remain reserved.

The primary benchmark goal is 500 problems, with Top 100 as its priority subset
and secondary editorial focus. They use the same category order and ranked
prefixes: 25/10 and 5/2 problems per large/small category respectively. The
registry's 50/20 `target` values support the legacy Top 1000 view; a 1,000-problem
benchmark is no longer an active goal.

Run `make publish` after edits. It computes category totals, benchmark membership,
rankings, JSON/CSV exports and live updates without rewriting these source files.
`build/catalog.json` is generated; a clean rebuild works without any prior catalogue.
Working summaries are stored in each card's `working_summary` field.
Question types include `yes_no`, `numerical_value`, `function`, `exact_value`
and `asymptotic_complexity`. Numerical and curve cards state the default absolute
1/100 Lean acceptance tolerance, units and domain in `answer_criterion`, including
when the target is integer-valued. Approximations need not be integers or simple
exact expressions. `exact_value` also supports explicitly approved exact targets:
BB(6) accepts a concrete machine with halting and universal maximality proofs,
whose runtime specifies the value. Asymptotic
targets retain their specified matching-bound precision. See the
[manifest](../docs/MANIFEST.md) and [rules](../docs/RULES.md).
Related active problems are stored as stable IDs in `related_problem_ids`.
The relation is symmetric: publication adds the reverse link automatically,
without rewriting source cards, and omits links to deleted or retired problems.
IDs must exist in the catalogue or deletion log; self-links and duplicates fail
validation. The reader shows linked problem titles without explanations. The
separate `related` field is reserved for bibliographic objects, not card IDs.
When `context_blocks` exists, it owns the paragraph text and citations; searchable
`context` is derived. Otherwise keep `context`. Criterion labels, ranks, counts
and benchmark focus are derived too. Legacy `rank`, `classification_method` and
top-level `importance_method` are omitted; the nested `importance.method` remains.

## Add or update cards

Use `python3 scripts/import_cards.py /path/to/cards.json` from the repository root.
The input may be one complete card, a list of cards, or an object containing a
`cards` list. The importer validates each record and allocates an unused stable ID
when `id` is omitted. A stable `key` reconnects later imports to their original ID.
Existing cards are skipped; `--replace` explicitly enables replacement.
Then run `make publish`.

For a direct edit, change the existing JSON file. Keep its filename and ID stable,
and choose an existing category key from `categories.json`. Record review dates
when the corresponding review is actually performed. Counts, category ranks,
selection-group fields and `benchmark_focus` are generated, not authored fields.

## Remove cards

Add the ID and a specific reason to `deleted_records.json`, remove its card file,
and run `make publish`. Update a selected problem's entry in
`benchmark_selection.json` when necessary; missing focus choices are reported.
Deleted IDs and their historical import keys cannot be reimported. Even a stale
card file copied back into `cards/` is ignored by publication. The IDs are never
reallocated, including IDs absent from the historical registry. Live snapshots
and deletion deltas remove the records from already open readers.

An explicitly user-authorized later restoration is a new editorial decision:
record why the deletion is superseded, retain the original ID/key, remove that
ID's deletion entry and validate its completed canonical card. Ordinary imports
and stale files still cannot restore deleted IDs automatically.

The September 2026 cleanup removed 4,472 archived records. The deletion log also
includes eight research directions deleted before that cleanup. Git history is
unchanged; the working tree contains no restoration archive.
