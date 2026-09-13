# Individual category review, 11 September 2026

User request: reconsider whether any problems belong in a different category.
The review covers the entire active cohort at the start of the task: 2,695 saved
records across all 35 agreed categories, including the retained duplicate pointer
TCS-0485. Existing archive decisions are preserved.

Three subagents read 863, 697 and 704 records, respectively; the root read 431.
`manifest.json` records disjoint assignments, and `baseline.json` preserves the
starting catalogue. Every reviewed ID occurs in exactly one `*-review-*.json`
batch. A missing move means the existing category was retained. Explicit
`borderline` notes explain cases where another home was plausible but did not
justify a move. Decisions are individual judgments from the saved question,
fuller source context and explanations, not output from a keyword classifier.

## Applied decisions

The review moved 668 records and retained 2,027. Of the moves, 374 cross the
large/small boundary. Current totals are 1,355 large-category and 1,340
small-category candidates. Miscellaneous is empty after its four records move
to specialist categories; Top 100 consequently contains 98 available records.

`decisions.json` gives the outcome for every reviewed ID. `report.json` records
counts; the [readable review](../../web/category-review-20260911.md) gives the
category census and every move with a reason and source link. The active routing
input is `../../category_overrides.json`; its previous contents are preserved in
`category-overrides-before.json`. `finalize.py` validates complete review coverage
before integrating the decisions. No category names or future quotas change.

The main boundary conventions are:

- Use the actual problem and computational model, rather than the paper's topic
  or an incidental word such as signature, locality, polymorphism or allocation.
- Keep explicit FPT, kernel and exponential-parameter targets with parameterized
  and exact algorithms; distinguish fine-grained reduction and exponent barriers.
- Keep communication rounds, streaming storage and local oracle models distinct
  from ordinary graph algorithms and geometric data structures.
- Route group computation, arithmetic circuits and matrix rigidity to algebra;
  solving equations in unknown terms and formal proof procedures belong with
  automated reasoning or proof complexity as appropriate.
- Distinguish statistical learning and distribution testing from generic online
  optimization, bandits and numerical convergence. A paper's learning application
  does not automatically determine the category of an analytic conjecture.
- Preserve a defensible specialist home for an interdisciplinary question;
  unexplained source fragments do not justify invented models.

The root reconciled the proposed moves across agents. Additional independent
checks compared root and agent proposals with their actual source records;
agent audit notes preserve concrete corrections to rationale wording. The
reviewed duplicate TCS-0485 follows the category of its canonical TCS-0310.

## Source corrections

Three working summaries had confused a paper's topic with the selected question.
`summary-corrections.json` records their exact before/after text and evidence:
TCS-2219 concerns k-Disjoint Paths certificates, TCS-5112 concerns 3SUM, and
TCS-5341 concerns converting hitting-set generators into pseudorandom generators.
All three keep five sentences and their existing sources, IDs and research status.
All other summaries remain unchanged. Selected primary-source checks are listed
in `source-checks.md`.

## Verification and later work

`python3 ../../qa/category_review.py` checks full coverage, applied destinations,
all unchanged research fields, exact archive preservation, both authorship
collections and matching exports. `validation.json` records the result; `verification.json` records the passing
command suite and publication version.
`make check` checks ranking, taxonomy, frozen imports and publication behavior.
Browser checks cover category filters, current small/large totals, Top 100 quota
caps, source summaries, notes and live/offline data.

The earlier small/large summary inventories remain frozen authorship cohorts.
Their historical validation files are not rewritten to match later categories;
summary collection exports instead follow current category placement. Likewise,
the concurrent importance-selection review keeps its independent frozen cohort
and may later archive records without undoing these topic decisions.
