# Related problems: first catalogue-wide pass

The reader now shows **Related problems** in both Compact and Full views. Each
entry is a linked card title and stable ID, with no explanation beside the link.
The first five entries are visible; longer lists can be expanded. Links work
across category, search and benchmark filters and beyond the loaded page.

The pass began with 1,973 active cards. A concurrent editorial cleanup removed
300 cards; application used the remaining 1,673 active cards and did not recreate
removed records. The final graph contains **1,664 undirected edges** connecting
1,342 cards. There are 331 isolated cards, an average degree of 1.989, and 383
edges crossing category boundaries. The largest neighborhood is P versus NP
with 30 related problems. The average was an editorial guide, not a per-card
quota or a reason to add weak relationships.

## Editorial method

All 35 categories were screened using card titles and available question text,
with working summaries, definitions and sources inspected for candidate
relationships and unclear targets. This is a first relatedness pass, not an
exhaustive all-pairs implication map or an independent open-status audit.

`groups.tsv` records explicit editorial decisions: `C` selects each pair within
a tightly related group and `S` selects the first ID against the remaining IDs.
Groups cover concrete implications, restrictions and generalizations, close
representations of the same problem, and substantive structural variants.
Being related does not assert equivalence, the same computational model, or
that both answers transfer. In particular, uniform/nonuniform computation,
randomized/deterministic algorithms, and existence/construction are distinguished.
There is no transitive closure of similarity.

`candidates.py` supplies lexical retrieval suggestions only. It does not write
cards, and its scores do not select links. Suggestions based on incidental words,
shared author names, generic source titles or unclear excerpts were discarded.
`rejected_pairs.json` records two broad derandomization connections rejected at
final review. Selected source checks are recorded in `source-checks.md`.

Existing card links were reviewed as well. String IDs in the bibliography field
`related` and the two `related_catalogue_ids` lists were migrated into
`related_problem_ids` when retained. Links to inactive targets were removed from
active cards. Existing directional `problem_relations` records were preserved.
The audit distinguishes retained, inactive and declined legacy links; for
example, sharing the name Hartmanis did not justify connecting real-time digit
computation with the Berman–Hartmanis isomorphism conjecture.

## Storage and maintenance

Canonical links live in each `data/cards/TCS-XXXX.json` file as
`related_problem_ids`. The authored graph is symmetric. Publication also derives
reverse links automatically, drops retired/deleted endpoints, and rejects
unknown IDs, duplicate targets and self-links. The JSON, offline JavaScript and
CSV exports include the resulting adjacency lists. Subbenchmark links can point
to active cards in the wider catalogue.

`apply_review.py` reads current cards immediately before modifying only link
fields and `updated_at`, verifies preservation of other content, and refuses to
recreate a concurrently removed card. Existing independently authored links in
the canonical field are preserved. The script is a historical application aid;
the canonical card files remain the editable source of truth.

`audit.json` contains screened active IDs, group decisions, degree counts,
legacy-link dispositions, skipped group members removed during concurrent work,
and hashes of unchanged non-link content. `validation.json` records final
structural and browser checks.

## Validation

- `make check`: passed; isolated clean publication, rankings, taxonomy, relation
  validation, imports, deletions, export parity and deployment regression tests.
- `node tests/pages.cjs`: passed; related navigation in both layouts, across
  filters and pagination, project-prefix loading and mobile layout.
- `node tests/deletions.cjs`: passed; offline loading, live target renames, escaped
  titles, incoming-link removal and restoration, and preservation of expanded
  related lists.
- Desktop and mobile rendering inspected in Chrome; no horizontal overflow.
