# Catalogue editorial standard

Persistent requirements from the user. Apply these to every completed card.

## Selection scope

Apply [SELECTION_POLICY.md](SELECTION_POLICY.md) when choosing problems for the
benchmark. The user explicitly excludes most general combinatorics, with
selected edge cases retained in a suitable category or Miscellaneous. Structural
graph theory is now an accepted small category of 20 problems within the scope
defined in the policy. Algorithmic graph problems remain in scope. The remaining
intentional exclusions are not gaps a coverage review should automatically fill.

## Current workflow: publish the whole quick pass first

On 10 September 2026, the user replaced the request to finish another 100
detailed cards before stopping. They now want ALL saved catalogue records in
the UI as very short cards immediately, using only material already saved, and
then a return to high-effort individual reviews. Do not cap the quick pass at
1,000. Keep incremental publication active and preserve existing IDs and notes.

Quick drafts may expose an existing question excerpt or topic label with its
source. Mark incomplete formulations and unreviewed status honestly. This is an
explicitly requested intermediate stage, not a claim that every inherited record
already meets the completed-card standard below. Never fill missing mathematical
conditions by guesswork or promote an automatic extraction to reviewed status.

## Completed-card requirements

- Write all card content and UI text in English.
- Publish each completed card immediately so it appears in the live reader.
- Keep the source-checking diligence and substantial explanatory context of the
  approved cards. Prioritize data structures, distributed algorithms, and graph
  algorithms, then continue through the entire catalogue.
- Every question must be well-defined and have an unambiguous mathematical
  resolution. This requirement was explicitly added on 10 September 2026.

## Accepted question forms

1. **Yes/no proposition.** State the quantified claim, inputs, promises, model,
   guarantees, and parameter dependencies. Explain what a proof and a refutation
   would establish. For universal claims, do not incorrectly require a finite
   counterexample when the negation is an asymptotic separation.
2. **Asymptotic complexity.** Define the task or fixed algorithm, the cost
   measure, worst-case/expected/amortized convention, randomness and error,
   parameters, and the requested precision (for example, matching bounds up to
   constant factors). Partial improvements are progress, not a full resolution.
3. **Exact value.** Define the finite mathematical quantity and all conventions
   affecting it. Require an explicit value with a proof of equality; for extrema,
   this includes attainment and a matching bound. A finite, unambiguous expression
   may specify an enormous integer without writing its decimal expansion. Added
   for the user's explicit request to determine BB(6) on 10 September 2026.

Avoid unqualified requests such as “find a better algorithm,” “understand X,”
“find a natural assumption,” “characterize X up to specified factors” when the
factors are unspecified, or “can this be generalized?” Give each card one main
target. Put weaker milestones and related questions in context or progress.

The `formal` statement and `definitions` must make the question self-contained.
A reference to a numbered definition is useful provenance, but is not a
substitute for explaining the relevant mathematical object or access model.
State computational-model restrictions that affect the answer. Record any
editorial specialization of a broader source question explicitly.

Each completed card records `question_type` (`yes_no`, `asymptotic_complexity`, or
`exact_value`) and an `answer_criterion`. These are an editorial
commitment, not an automated certificate of mathematical validity.

## Sources and status

Use primary sources, dated progress, and checks for later results. Preserve
identifiers when developing existing records. Cite model definitions as well as
theorems. Separate the reason for including a problem (editorial judgment) from
the mathematical claim (which must be precise).

A question already answered, or subject to a recent claimed solution, must not
silently remain a confirmed open problem. Retain its history and record the
status and verification limits. Untouched legacy entries and source notes are
unfinished material; do not present them as satisfying this standard.

## Importance ordering (user instruction, 10 September 2026)

Within every category, order cards by importance. Assess foundational significance,
breadth of consequences, and influence on other questions. Each completed card
must have an `importance` object with an integer `score` (0–100), `method` equal
to `editorial`, a specific `reason`, and an assessment date. These are editorial
judgments, not objective measurements. Use roughly 95–100 for defining landmarks,
80–94 for core questions with broad consequences, 65–79 for substantial structural
or algorithmic questions, and 50–64 for narrower fundamental model questions.
Importance does not increase merely because a card was added or reviewed recently.

Canonical assessments live in cards/*.json; importance_overrides.json records
individual assessments of still-unfinished drafts without promoting their evidence
level. Unassessed drafts share a provisional midpoint, explicitly labeled in the
UI; ID tie-breaking does not assert relative importance. Refine these as each
card is developed. publish.py assigns category positions consistently across
JSON, CSV, offline data, and live updates. The default UI sort is Importance.

The category-wide scope review is in `importance_category_review.json`, with the
initial grouping audit in `research/importance/category_review.tsv`. It
uses shared scores for questions of comparable scope. Specific follow-up
assessments in `importance_overrides.json` take precedence, followed by canonical
detailed-card assessments in `cards/*.json`. This review does not promote draft
evidence or validate current open status. Resolved records sort last; scores
remain intact. `importance-ranking.csv` exports every category in its importance
order, and `importance-overview.md` shows the first ten assessed candidates each.

## Individual dispositions

If a source contains only a subjective expository request, an invalid extraction,
or a duplicate, record an individually justified disposition with references in
record_corrections.json. Retain the ID and history. A review_outcome with
complete=true finishes that record’s review without inventing a mathematical
question or promoting its source evidence. Excluded records remain readable as
“Retired after review” and are omitted from the awaiting-review draft filter.
Do not use this mechanism for a merely difficult-to-formulate genuine problem.
