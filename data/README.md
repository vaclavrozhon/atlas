# Canonical atlas data

`cards/TCS-XXXX.json` is the editable source for an **active** problem. Each file contains
its statement, definitions, answer criterion, background, source references,
review status, category, importance assessment and optional working summary.
Drafts remain drafts: moving them into this directory does not certify their
formulation or current open status. Follow [the atlas rules](../docs/RULES.md).

**Inactive** cards live separately in `archive/cards/TCS-XXXX.json`. Preserve
their complete contents, but exclude them from routine improvements, source
checks, validation, selection, rankings, publication and imports. Search
`cards/`, not all of `data/`, when doing editorial work. Archive contents are
read only for explicitly requested archival work or reactivation; they need
not meet today's active-card schema. Activity is determined by the folder and
is separate from the scientific `status` field.

- `categories.json`: category IDs, stable keys, labels, order and quotas.
- `benchmark_selection.json`: ordered focus choices and their editorial reasons.
- `criteria.json`: scientific selection criteria and labels.
- `metadata.json`: dataset background and methodology.
- `archive/index.json`: inactive IDs mapped to archival reasons, including legacy removals.
- `archive/cards/`: complete inactive cards, excluded from ordinary work and publication.
- `archive/activity.jsonl`: archival and explicit restoration decisions.
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
without rewriting source cards, and omits links to inactive problems.
IDs must exist in the active catalogue or archive index; self-links and duplicates fail
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

## Deactivate or reactivate cards

```sh
python3 scripts/archive_cards.py TCS-0123 --reason 'Specific editorial reason.'
make publish
```

Archival moves the exact card file into `archive/cards/`, keeps its ID reserved,
records the reason and removes it from focus selections. It does not choose
replacement problems. Multiple IDs may be supplied for the same reason.
Live snapshots and removal deltas also remove inactive cards from open readers.
Do not delete card files or use resolved/excluded cards as an active backlog.

Ordinary imports, even with `--replace`, reject inactive IDs and their historical
source keys. A stale card copied into `cards/` cannot override the archive.
Only a later explicit user request authorizes reactivation:

```sh
python3 scripts/archive_cards.py TCS-0123 --restore --reason 'Superseding editorial decision.'
make publish
```

Restoration validates the requested card against current active requirements,
preserves its complete file and identity, and records the decision. It does not
restore former focus membership automatically. If validation fails, only that
explicitly requested card may be prepared for reactivation.

The 13 September 2026 migration superseded `deleted_records.json` with the
archive index and recovered available historical card content from Git.
Recovery provenance and any unavailable legacy contents are recorded in
`archive/recovery.json`; missing historical content is not fabricated.

A card may also contain `community_reviews`: editorial responses to public notes
or proposals. Each entry records `source` (`direct` or `github`), the contribution
`id`, `original_problem_id`, verbatim `original_text`, `status` (`solved`, `reviewed`
or `added`), `response`, and `reviewed_on`. Keep the response on the active card
that incorporates the feedback, including when an older card was consolidated.
The original contribution stays in its service; publication adds a separate
response in the reader and does not rewrite or delete the author's text.
