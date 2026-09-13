# Category names and order — 11 September 2026

The user approved the discussed order of 10 large and 25 small categories and
12 display-name changes. The parameterized category is displayed as
“Parameterized complexity and algorithms”, with “exact” removed.

`../../categories.json` is the single editable source for category IDs, stable
keys, current display labels, group targets and order. `../../categories.py`
validates and loads that registry. Taxonomy constants resolve stable IDs rather
than relying on their position in a list. Published `areas` metadata carries the
same labels and order into the browser and generated exports.

Historical category keys remain compatible with existing cards, imports,
editorial decisions, benchmark selections and archival manifests. All individual
records, category membership, scores and positions within each category are
preserved by the naming change. The browser uses current labels in active and
archived cards, filter chips, search, copied text and downloads. Label-only live
updates rebuild search terms and preserve active filters and focused notes.

Markdown reports follow the approved category order. CSV exports add explicit
label columns beside stable keys; JSON exports include the category metadata.
The editable category plan links to the registry and generated table instead of
maintaining another independent list of current names.

## Evidence and checks

- `before.json.gz` preserves the initial catalogue snapshot.
- `verify.py` and `validation.json` compare all records, category membership,
  counts, labels, order and exports. Two edits from the separate learning/edit-
  distance session arrived after the initial snapshot; they are checked against
  their exact authored files and listed explicitly in the validation report.
- `browser-label-validation.json` checks displayed labels, live renaming and
  reordering, preserved filters/notes, search, HTML escaping, downloads, mobile
  layout and offline rendering. `mobile.png` captures the category list.
- The existing taxonomy and Top 100/1000 browser suites check all 35 filters,
  registry order and unchanged benchmark membership.
- `make check` checks ranking, taxonomy, imports and repeated publication in an
  isolated copy, including the new registry files.

Historical review reports retain the names used when those reviews were made.

`verification.json` records the completed checks and their exact scope. The long
full-suite publication process was interrupted; `publication-validation.json`
records the successful focused check of two isolated publications. Preservation
reports refer to their recorded versions; subsequent independent authoring may
add or update records while retaining these category labels and order.
