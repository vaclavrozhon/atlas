# LaTeX formatting audit — 12 September 2026

The reader already bundled KaTeX, but most mathematical expressions had no math
delimiters. Its rendering options also excluded source excerpts and reference
titles. Compact previews could cut through a formula, and blank lines could split
one formula into separate HTML paragraphs.

The card pass adds explicit inline LaTeX to existing mathematical notation:
indices, exponents, roots, probability bounds, sums, integrals, sets, complexity
classes and asymptotic expressions. Existing valid LaTeX is retained. Ambiguous
nested indices, root scope, textual probability subscripts and several named
parameters were checked individually. Formatting does not change quantifiers,
mathematical targets, evidence, status, sources or editorial importance. Concurrent
scientific reviews and removals were preserved.

The reader now shares formula boundaries in `web/math.js`, uses them for compact
previews and paragraph breaks, and renders source excerpts and reference titles.
Long inline formulas scroll within a narrow card. Search strips the formatting
while preserving mathematical operators and names. HTML remains escaped and KaTeX
runs with `trust: false`; public reader notes keep their plain-text contract.

`changes.json` records the applied card/field counts. `edits.tsv` lists each field
and hashes of its before/after text, without copying obsolete card content into a
second catalogue. Publication continues to derive all reader outputs from canonical
cards. No deleted cards were restored.

## Verification

- `tests/math.cjs` checks every LaTeX expression on every active card with the
  locally bundled KaTeX, balanced delimiters, safe HTML, paragraph boundaries,
  search text and formula-safe excerpt boundaries.
- `tests/math-browser.cjs` renders all active cards in both Compact and Full,
  checks KaTeX errors and leftover delimiters, and checks source excerpts,
  reference titles, long-preview boundaries and mobile width with local fixtures.
- Full data/publication regressions and existing notes/votes browser tests run
  alongside the formatting checks.
- Desktop/mobile screenshots and the all-card browser audit are saved here.

The completed catalogue pass covers **1,073 active cards** and changed formatting
on **620 cards**. The final canonical validation parsed **9,618 expressions** with
no errors. A scan of every visible text field found no remaining un-delimited
powers, indices, LaTeX commands or the mathematical Unicode operators targeted by
the audit. The all-card browser pass rendered 1,073 cards in each layout and
20,187 formula instances without parse errors or leftover delimiters. Subsequent
scientific reviews of TCS-4274 and TCS-4301 were retained and their new notation
was formatted and revalidated separately.

`make check` passed. The aggregate browser command was terminated with status 143
after the all-card math pass; the reader-pages check passed when rerun separately.
The remaining browser checks were run separately as well.

## Deployment

Published reader commit: `f8c07e87fa2896f617317afb54b9cae74c92a054`.
Final catalogue version: `189d4ac740f51d814b2c`. The live browser verification
checks a formerly plain SAT exponent, the KLS statement, mobile width and shared
vote loading, without writing notes or votes. Its screenshots and results are
stored in `live-desktop.png`, `live-mobile.png` and `live.json`.
All individual browser checks and the notes/votes Worker test suite passed.
