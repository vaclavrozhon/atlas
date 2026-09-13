# Five-sentence working summaries for small categories

User request, 11 September 2026: write approximately five sentences about every
active problem in the small buckets, using subagents, before the final-card stage.

The frozen scope is the existing candidate pool: `selection_group == "small"`
and no `scope_exclusion`, totaling 1,104 saved IDs in 25 categories. This pool
includes TCS-0485, an already excluded duplicate whose disposition is preserved.
Counts describe saved records, not verified distinct open problems.

## Authorship and source basis

Three subagents individually wrote 364, 343 and 342 summaries. The root task
wrote another 55 in four categories while implementing and checking publication.
The final assignments and all original record hashes are in `manifest.json`;
`agent-*-input.json` and `root-input.json` preserve the supplied drafting material.
The two reassignments are explained in `COORDINATION.md`.

Canonical text lives in `../../draft_summaries/*.json`. Every summary contains
five sentences, an authoring date and references to the existing record's sources.
Most material comes from saved formulations, source notes, detailed cards and
extraction contexts. Selected original publications were consulted to clarify
otherwise incomplete passages; this was not an exhaustive later-result search.

The explanations retain missing conditions and damaged notation explicitly.
An inherited topic label, rhetorical question or already recorded duplicate is
not silently turned into a newly verified open problem. Existing formal text,
status, evidence, review dates, categories, ranking and identifiers stay intact.

Examples of clarified source passages include TCS-1158 (adaptive state
identification), TCS-1368 (cographic-matroid basis finding), TCS-1962 (fractional
clique growth), TCS-4636 (regular-language definability), and TCS-6192
(correlation-decay algorithms). TCS-4640 introduces an orbit problem in the
source rather than naming one of its subsequent open questions. TCS-6825 keeps
the historical 2014 question and cites a 2023 conditional separation in its
summary. These explanations do not count as completed research-card reviews.

## Reader and checks

Read the [collected text](../../build/small-bucket-summaries.md) or open
the [small-category reader](../../build/index.html).
Both reader layouts show the summaries, and search, copy, CSV, JSON, offline
data and live updates retain them. Existing excerpts remain available in details.
An already open reader needs one page reload to load the updated JavaScript.

`validation.json` records coverage, exact preservation of original research
content, citation validity, sentence counts, word counts, and export parity.
`browser-validation.json` covers visible text, search, notes, live updates,
escaping, both layouts, mobile width and offline loading. The matching screenshots
are `desktop.png` and `mobile.png`. Individual agents recorded source caveats in
`agent-*-notes.md`.

The general `make check` suite also exercises import preservation, ranking,
taxonomy, repeat publication, single-record updates and failure behavior.
The shared working-summary layer preserves the independently authored concurrent
large-category descriptions; small-category coverage checks do not remove them.
