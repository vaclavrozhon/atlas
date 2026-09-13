# Textbook and survey question import, 10 September 2026

The user authorized importing problems while retaining the independent library,
and explicitly prohibited access to that library from the atlas UI. This import
therefore freezes question paraphrases and external bibliographic references in
`../../imports/textbook-surveys-20260910.json`. Normal publication reads that file;
it does not read or serve the independent library, its manifests, or its PDFs.

All 555 source annotations are accounted for: 424 questions, 58 conjectures and
73 research directions, drawn from 47 of the 50 publications. The other three
publications contained no retained explicit unresolved entries in the read versions.

- 472 annotations seed 472 new short drafts.
- 82 annotations supplement 75 existing cards, including four grouped entries
  that each refer to two existing targets and the grouped ETH/SETH entry.
- One further annotation repeats a target among the new drafts.
- The resulting 547 cards carry 560 source-note attachments. Grouped annotations
  can occur on two existing cards; they do not merge those existing identities.

`screen.py` and `screening.json` retrieve possible duplicates using text similarity.
`decisions.py` contains manually chosen matches after inspecting question text,
locators, models, and available saved formulations. Similarity scores never
automatically merge cards. Edition differences, general versus restricted models,
deterministic versus randomized hypotheses, recovery versus detection, and weak
versus strong quantitative targets were reasons to retain separate drafts.
Collection-wide semantic deduplication remains incomplete.

`prepare.py` materializes the approved input. The input snapshot, its fingerprint,
and a compressed baseline catalogue are private audit records in this directory;
they are never copied into the HTTP document root. Stable IDs are assigned by the
publisher using `source-import:` registry keys. `site/textbook-additions.json`
and `.csv` map each source annotation to its atlas ID(s), with external references.

Source notes are an overlay after canonical card reviews and corrections. Existing
formal statements, statuses, review tiers and IDs are preserved. A later full review
of a new draft also takes priority over the original seed, while its bibliographic
annotations survive republication. Imported drafts have provisional importance 50,
not a fabricated individual assessment. Source summaries are explicitly paraphrases,
not direct quotations or newly verified self-contained formal statements.

The dated-source limitations remain material, including the inconsistent printed
rate inequality in Vadhan, the historical finite-CSP dichotomy, research directions
about alternative proofs of known results, partial source drafts, and internally
resolved items already excluded from the library inventory. This import performs
no fresh claim about the present open status of those source questions.

Validation: `qa/test_source_imports.py`, `qa/textbook-questions.cjs`, the existing
quick-card browser regression, and taxonomy checks. These cover completeness,
external references, retained caveats, stable IDs, repeat import, later reviews,
matching CSV/JSON exports, filters, search, personal notes, offline operation,
mobile layout and HTTP 404 responses for former library paths.
