# Atlas rules

Confirmed editorial and repository decisions, updated on 13 September 2026.
This is the authoritative policy document. Current category names, quotas and
focus choices live in the linked data registries. Dated research observations
live in [research/review-notes.md](../research/review-notes.md) and individual
research reports; they do not override later card reviews or user decisions.
All project-authored content, including cards, documentation and UI, is English.

## Purpose and selection

The atlas benchmarks AI research capabilities through important open problems in
theoretical computer science. Each problem must explain what is being asked,
why it matters, and what would count as solving it. Prefer major, long-standing
challenges; strongly motivated newer questions remain eligible.

Our primary goal is a benchmark of **500 problems**. The **Top 100** is a
priority subset of those same 500, with secondary editorial attention. Organize
categories and rank their problems once for these nested selections. A
1,000-problem benchmark is no longer an active goal.

Assess scientific importance, intellectual interest, foundations and community
relevance together. A question should expose a substantial barrier, general
principle or consequential phenomenon. Explain what a resolution would enable.
An open-question paragraph in a paper, a prestigious venue, age, popularity or a
numerical score alone does not establish suitability.

Use substantive motivation, surveys, monographs, established problem lists,
independent research and connections to central questions as complementary
evidence. No particular source type is mandatory. Informed editorial taste is
welcome: give a specific rationale and distinguish judgment from sourced facts.

Prefer consequential questions over narrow follow-ups, parameter tuning and
changes to a single construction. A small canonical question or an improvement
in a practical model can qualify through substantial wider consequences.
Incomplete formulation alone is not grounds to discard an important question;
record what remains to be specified and review it further.

Consolidate duplicate formulations. Related variants deserve separate cards
when they capture substantially different targets. Individually significant,
logically dependent problems may coexist, although this should be uncommon;
P versus NP is the main anticipated cluster. Document implication directions,
assumptions and equivalences. Logical dependence alone does not justify removal.

Related-problem links form a symmetric, non-transitive editorial relation among
active cards. Include substantive implications (even if only one answer settles
the other target), generalizations, special cases and close structural variants.
Sharing a category, author or keyword alone is insufficient. Aim for roughly
two to three neighbors on average, allowing both isolated cards and large hubs;
do not fill a quota or discard a useful relation to cap a card's degree. Store
stable IDs in `related_problem_ids`; show titles and links without explanations.
Publication derives the reverse links and suppresses inactive targets. Existing
directional `problem_relations` metadata retains its precise mathematical meaning.

Formalization effort must not affect selection. Background theory and statements
may be formalized after selection. Completed cards still require precise targets.

## Benchmark success

Accepted answers require a complete, mathematically correct proof checked in
Lean. Its theorem must match the card's assumptions, model, quantifiers and
answer criterion. Questions may ask for a proposition, a number, or a function
or curve; there is no preference for a binary answer.

By default, for a numerical target, including an integer, the Lean benchmark
requires absolute error at most 0.01, represented exactly as 1/100. Explicitly
user-approved exact targets follow their recorded answer criterion instead.
For a function or curve
f on a stated domain D, including an integer-valued function,
it requires a supplied function g and a proof that |g(x)-f(x)| ≤ 1/100 for every
x in D. State units, normalization and the full domain; an uncertified plot,
sampled agreement or a one-sided estimate is insufficient. A certified interval
of width at most 1/50 qualifies via its midpoint. Exact determination is welcome
but is not required for these numerical targets. This tolerance is benchmark
acceptance, not a claim to have resolved a related exact conjecture.

The supplied approximation need not be integer-valued even when the target is.
For an integer target N, prove |a-(N : ℝ)| ≤ 1/100 with a real approximation a;
apply the same convention pointwise to integer-valued functions. A certified
interval or an unambiguous mathematical expression can specify the answer
without a decimal expansion or a simple exact definition of N. Do not infer
an extra exact-equality or integer-output requirement from integrality alone.
This records the user's
correction to the earlier integer exception.

The user subsequently selected an exact witness-based answer for BB(6): supply
one complete six-state transition table, prove in Lean that it halts on the
specified blank tape, and prove that every halting machine in the same class
runs for no more steps. The witness's runtime then specifies BB(6) exactly;
no simple closed form, decimal expansion or full simulation is required as part
of the submitted answer. The halting and universal maximality proofs are both
mandatory. This BB(6) decision does not change other cards' acceptance precision.

On 16 September 2026, the user explicitly retained TCS-6607, binary deletion
channel capacity, with absolute 1/100 accuracy as a formalization task. A known
uniform finite-block estimate already gives unrestricted approximation at that
accuracy. Keep this card active and distinguish its known approximation
guarantee from the separate open exact-capacity problem. This decision does not
require a new scientific result, an efficient evaluation algorithm or exact
determination of the curve.

Asymptotic-complexity questions retain their stated precision, such
as constant-factor matching bounds; 0.01 is not an additive error on big-O
notation. Infinite values, where allowed, require proof of infinitude. Partial
advances and special cases count only if they meet the entire answer criterion.

Sources, tools and human involvement in solution attempts are unrestricted.
There is no predetermined time or compute limit.

The catalogue is a working candidate pool with different review levels.
Inclusion, selection, a working summary or a formulation edit does not certify
that a question is correctly formulated or remains open today.

## Problem statements

Write mathematical expressions in explicit LaTeX math delimiters: `\(...\)`
for inline notation and `\[...\]` for displayed equations. Use braces for
complete exponents, indices and root arguments. Keep prose outside math mode,
preserve all operands, quantifiers and inequalities when changing typography,
and validate expressions with the reader's bundled KaTeX. Source excerpts and
reference titles may contain math and must render it too. Compact previews and
paragraph breaks must not cut through a formula. Formatting alone must not
change a card's mathematical target, review status or evidence level.

Use the established name as the entire title of a named problem: for example,
`Kannan–Lovász–Simonovits conjecture`, without an introductory article, explanatory
subtitle, acronym in parentheses or restatement of the question. Retain a qualifier
only when it distinguishes the actual target from another version, such as the
asymptotic Gotsman–Linial conjecture. For unnamed problems, use a short descriptive
noun phrase that identifies the task and its essential model or bound. Recover
draft titles from their saved question and context; article titles, page locators
and extracted prose belong in provenance, not in the problem title. Do not infer
a named conjecture merely because the source mentions it as an assumption or a
related problem, and do not invent missing mathematical content to shorten a title.

Every active problem, including inherited drafts and previously reviewed cards,
needs individual formulation review. Prioritize developing the Top 500, with
the Top 100 as its priority subset: the first five/two selected problems in each
large/small category. Record individual
outcomes and unresolved choices; do not automatically promote a batch of drafts.

Give each card one main mathematical target with explicit quantifiers. Prefer
“determine this number/function” when the scientific target is an optimal
exponent, ratio, extremal function or tradeoff curve. Keep genuine existence,
decidability and class-comparison questions binary when that is their natural
target. The supported `question_type` values are:

- `yes_no`: specify inputs, promises, model, guarantees and parameter dependence.
  State what proof or refutation establishes. A universal asymptotic claim's
  negation need not have a finite counterexample.
- `asymptotic_complexity`: specify the task or fixed algorithm, cost measure,
  worst-case/expected/amortized convention, randomness, error, parameters and
  requested precision, such as matching bounds up to constant factors.
- `numerical_value`: define a numerical constant, whether integer or real, and
  require its determination with the absolute 1/100 Lean acceptance tolerance.
- `function`: define a numerical function, whether integer- or real-valued,
  including its parameters, domain and units, and require the same tolerance
  throughout that domain.
- `exact_value`: an explicitly selected exact target, including BB(6), or a
  historical exact-value record. Define the quantity and accepted representation
  and require a proof of equality. A concrete extremal witness with proved
  attainment and a matching universal bound may specify the value without a
  closed form or a decimal expansion. Record the user-approved exact criterion
  instead of inferring it solely from an integer-valued target.

An infimum or supremum need not be attained. State the appropriate approaching
upper/lower bounds instead of silently demanding an optimum-achieving object.
A well-defined quantity or curve does not need a predetermined grammar for its
answer. A formula, certified evaluation rule or another unambiguous mathematical
description can qualify if it establishes the requested values and precision;
merely renaming the defining optimization or limit does not. Lack of an
anticipated closed form is not grounds for deletion.

The `formal` statement and `definitions` must be self-contained. Define objects,
domains, hypotheses, encodings, computational model, uniformity, parameter
dependencies, probability spaces, error, costs and limiting conventions that
affect the answer. State quantifier order. Translation into a proof assistant
should require no additional mathematical choices; this does not claim that a
formalization already exists. Citations to definitions do not replace those
conditions in the card itself.

Replace subjective mathematical predicates with precise requirements. In
particular, define the class meant by “natural”; for “explicit”, specify the
representation or construction algorithm, input, output, uniformity and resource
bound. Apply the same principle to “efficient”, “optimal”, “simple”, “canonical”
and “sufficiently large” whenever they affect truth or acceptable answers.

Preserve the source question. Do not silently strengthen, weaken or specialize
it to obtain a cleaner or binary statement. Document editorial interpretations
and specializations against their sources. The user-authorized review of
12 September 2026 permits broadening a binary threshold conjecture to determine
its underlying quantity or function. Record that change explicitly and retain
the original conjecture as sourced context, without presenting the new target
as equivalent to it. If the intended target cannot be
recovered, mark `statement_review.status` as `needs_specification` and identify
its `remaining_issue`. Do not certify an invented replacement.

Problem content must contain no suggested solutions, proposed approaches,
hints, recommended techniques or intermediate milestones. Keep factual
motivation, definitions, dated known results and provenance separately identified.
The `answer_criterion` defines success without coaching the solver.

## Sources, review and summaries

Completed cards contain substantial, problem-specific context, significance,
references, dated progress, a supported question type and an answer criterion.
Use primary sources and check subsequent results. Cite model definitions as
well as theorems; record editions, revisions, dates and precise locators when
relevant. A publisher's structural validation is not mathematical verification.

Keep formulation review separate from current-status review and evidence level.
Distinguish a problem open in a dated source, a checked current open question,
an uncertain claimed solution and a verified resolution. Do not present an
unverified preprint as an accepted theorem or treat an old source as a fresh
status check. Record verification limits and preserve source provenance.

Drafts may show saved excerpts or topic labels while awaiting individual review.
A working summary explains the task, question, context and significance in five
English sentences, using saved source material. Save it in `working_summary`
with its date and source references. Preserve missing assumptions explicitly;
summaries neither certify current openness nor promote evidence levels.

An individually justified disposition can set `review_outcome.complete` without
inventing a theorem for an invalid extraction, subjective request or duplicate.
Do not use this for a genuine problem that is merely difficult to formulate.
Resolved and excluded records belong in the inactive archive. Deactivation
preserves the complete card using the activity workflow below.

## Categories

[data/categories.json](../data/categories.json) is the single editable registry
of stable IDs, keys, display names, order and quotas. Rename labels and reorder
entries there without changing stable identities. Historical source subjects
remain provenance. Category assignments are explicit editorial decisions,
not keyword guesses. Quotas are selection targets, not candidate-pool limits.

The current plan has ten large and twenty-five small categories. They contribute
25/10 problems each to the primary Top 500 and 5/2 to its Top 100 subset.
The registry's fifty/twenty quotas and the existing Top 1000 export remain a
legacy larger view, not an active selection goal. The Data structures addition
fills the slot released by the online/scheduling merger. Generate counts and
category reports from data instead of copying mutable inventories into instructions.

Apply these accepted boundaries using the registry's current display labels:

- **Algorithms and Data structures:** Algorithms retains the historical `ads`
  ID and `Algorithms & data structures` key. The separate small Data structures
  category covers search trees, dictionaries, heaps, priority queues, cell-probe
  and word-RAM operation bounds, ordered collections, external-memory structures,
  history-independent representations and static query oracles. General online
  labeling, ordered-list, rank/selection and prefix-product primitives belong
  here even when they support updates. An offline heap batch requesting only
  final survivors remains Algorithms. A cut sparsifier alone is not a query
  interface. Geometric, compressed-text and graph-class query problems can retain
  specialist homes; unresolved algebraic boundary cases require individual review.
- **Dynamic algorithms:** retain the historical dynamic-graph key. Maintain
  graph, geometry, string, language, database, matroid or optimization solutions
  after insertions, deletions and other input changes. This includes incremental,
  decremental and fully dynamic models. General data-structure primitives use
  the separate category above. Dynamic programming, dynamical systems and static
  edit distance do not qualify merely through their names. Locality, streaming,
  privacy and competitive-analysis targets retain their specialist homes.
- **Online algorithms, scheduling and packing:** one small category with the
  stable online ID/key covers competitive analysis, sequential selection,
  prophet/secretary problems, online optimization, bandit regret, and offline
  scheduling and packing. Scheduling is no longer separate; online questions
  no longer default to Optimization. Merely mentioning online algorithms does
  not override specialist learning, privacy, quantum or distributed targets.
- **Graph theory and algorithms:** the accepted structural scope includes minors,
  decompositions, width parameters, sparse classes, separators, logical
  characterizations, hereditary/forbidden-subgraph structure, coloring, and
  expansion/girth questions with computational consequences. It also includes
  static spanning trees, matching, subgraph detection, canonization, paths,
  graph-width algorithms and graph-specific labels. Dynamic, distributed,
  parameterized and fine-grained targets take specialist precedence.
- **General combinatorics:** largely excluded, with no dedicated category or
  quota to fill. Selected computationally motivated exceptions may use a
  suitable specialist category or Miscellaneous with a specific rationale.
  The accepted graph scope is not permission to restore all combinatorics;
  noisy combinatorial source labels are not grounds for blanket removal either.
- **Geometry, games and optimization:** computational topology belongs with
  geometry; voting and preference aggregation with game theory/social choice.
  Optimization includes numerics and information-based complexity. A central
  truthfulness requirement determines game-theory placement, even for scheduling
  or approximation applications; mentions of games, allocations or truthful
  data alone do not establish this condition.
- **Constraint satisfaction:** coloring under a colorability promise belongs
  here when that promise defines the main target. Growing-palette problems can
  belong to the family without being single fixed-template PCSPs. Structural
  coloring, partial-coloring objectives and proof-system bounds need their own
  category assessment.
- **Beyond worst-case and average-case analysis:** includes smoothed, planted,
  semi-random, average-case hardness, instance-optimal and prediction-based
  models. General statistical sample complexity, cryptographic assumptions and
  quantum questions keep their specialist homes.
- **Retired knowledge representation:** preserve topics according to their main
  target: representation size in complexity; equivalence, negation and symbolic
  operations in automated reasoning; ontology queries in databases; output
  enumeration in counting/enumeration.
- **Miscellaneous:** last in the registry, for worthwhile cross-disciplinary or
  unusual questions difficult to place elsewhere. It is neither a replacement
  for formulation review nor a route to restore general combinatorics.

The user retained TCS-6674 in game theory because of incentives and TCS-6637 in
constraint satisfaction because of its promise. TCS-6725 and TCS-3984 follow the
latter preference as editorial extensions. Suggested moves for trace
reconstruction TCS-6623 and LPN TCS-6542 were not accepted: “I do not know” left
existing assignments intact. Reconfiguration/computational games, molecular
computing/programmable matter and kernelization remain discussion candidates,
not approved new categories.

## Ranking and benchmark selection

In the live reader, order active problems within each category by decreasing
shared vote score (thumbs up minus thumbs down), breaking ties by the editorial
order below. This same order determines membership in Top 100, Top 500 and the
legacy Top 1000 view, using the existing quotas. Calculate selection before search
filters, preserve category order and subset nesting, and never promote retired
records. Keep one changeable vote per browser identity; clicking the selected
thumb cancels it. Repeated or retried submissions must not multiply votes.
Shared votes persist independently of catalogue publications. Canonical editorial
data and static exports retain the reproducible editorial ranking; the live
reader applies the current shared votes on top of it.

[data/benchmark_selection.json](../data/benchmark_selection.json) stores ordered
focus IDs, topics and reasons. Choose the first five/two jointly for importance
and topic diversity, then place them at the top of each large/small category.
For example, the complexity prefix should span distinct barriers rather than
consist entirely of P versus NP variants. Preserve scores when changing the
focus order. The remainder follows decreasing importance with stable-ID ties;
resolved records sort last without losing historical assessments.

Use one order of categories and one ranking of problems within each category
for the primary Top 500 and its Top 100 subset. Top 100 uses the first five/two,
Top 500 the first twenty-five/ten, and the legacy Top 1000 view the first
fifty/twenty per large/small category. Top 100 is contained in Top 500, which is
contained in the legacy Top 1000 view;
changing selection size must not reorder problems. Reader filters narrow membership without
replenishing quotas. Resolved, deleted and excluded cards are ineligible. Missing
or invalid focus choices require a new editorial decision, not resurrection of
a removed card. Generated reports state shortfalls explicitly. Redistribution
of unfilled category quotas remains undecided; do not change the 5/2, 25/10 or
50/20 quotas automatically or silently backfill a shortfall from another category.

A completed card's `importance` contains an integer score from 0 to 100,
`method: editorial`, a specific reason and assessment date. Use approximately
95–100 for defining landmarks, 80–94 for core broad questions, 65–79 for substantial
structural or algorithmic questions, and 50–64 for narrower fundamental models.
These are editorial judgments. Unassessed drafts share a provisional midpoint
of 50; stable-ID ties do not assert relative importance. Age, recent publication,
a new review or more detailed prose must not raise importance automatically.
Draft importance assessments do not change evidence or verify openness.

Calibration decisions: the Path ORAM bucket-three/four-versus-five question
TCS-0458 was judged too incremental, without excluding ORAM as a subject.
TCS-0474 working-set heaps was explicitly removed on 11 September 2026 and
restored by the user’s later request to add the researcher-linked problem list on
13 September 2026; see [the restoration audit](../research/researcher-problems-20260913/README.md).
The request for more context
about distributed OR TCS-0464 did not approve its exclusion. Preserve these
distinctions when applying broad pruning criteria.

## Authoring and publication

For the ongoing individual completion pass, parallel processes in the same
checkout must reserve a pending active card before starting its review with
`python3 scripts/review_queue.py claim --worker PROCESS_NAME`. Use the returned
token when recording completion. The [shared review workflow](../research/card-completion-20260913/README.md#parallel-review-workflow)
defines reservations, release and the [unfinished-card inventory](../research/card-completion-20260913/unfinished.md).
A reservation does not certify completion and does not replace source review.

Cards have two editorial activity states, determined by directory placement:
**active** in `data/cards/` and **inactive** in `data/archive/cards/`. Activity is
separate from scientific `status`, evidence, importance and formulation review.
Every routine editorial task, source search, improvement pass, validation,
ranking, selection and publication operates on active cards only. Treat the
archive as absent from the working atlas. Do not recursively include it when
searching for cards, allocate review effort to it, repair old archive schemas,
or use it to fill category quotas. Consult or reactivate an inactive card only
when explicitly requested by the user.

Each active `data/cards/TCS-XXXX.json` is the complete editable source for its problem:
statement, definitions, sources, category, importance, history and summary stay
together. `context_blocks` owns paragraph text and citations when present;
publication derives searchable `context`. Without blocks, retain `context`.
Criterion labels, selection groups/targets, category ranks/counts and benchmark
focus are derived. Legacy `rank`, `classification_method` and top-level
`importance_method` are obsolete. The nested `importance.method` remains required.
Do not maintain override layers or edit generated catalogues to change content.

Keep stable IDs and historical source-key mappings in `data/id_registry.json`.
Inactive IDs and keys remain reserved. Use `scripts/archive_cards.py` with an ID
and specific reason to deactivate a card: it moves the complete file to
`data/archive/cards/`, records the reason in `data/archive/index.json`, and removes
any focus selection without choosing a replacement. Never discard card content
as part of pruning, deduplication or resolution. Ordinary imports, including
`--replace`, and stale files cannot reactivate an archived identity.
An explicit later user instruction may authorize reconsideration and restoration.
Use `--restore` after checking the requested card against current active-card
requirements; keep its identity and record the superseding decision. The activity
log preserves the previous archival and restoration decisions. Historical IDs
whose content predates recoverable repository history stay reserved in the index;
do not invent replacement content. This supersedes the former ID-only deletion
policy on 13 September 2026.
See [data/README.md](../data/README.md) for import and editing commands.

`web/` contains source assets. `make publish` validates data and builds the complete
reader, catalogue, rankings, benchmark exports and update delta in ignored
`build/`. `catalog.json` is also the full live-update snapshot; `data.js` supports
direct offline opening. Publication does not rewrite canonical inputs.
`make serve` and `make deploy` build automatically. Research and the independent
library remain outside the published site. Preserve reader state, open details,
scroll position and contribution drafts across incremental updates.

The candidate pool supports the primary **500-problem benchmark** and may
temporarily contain more records while selection and review continue. The
earlier 800-card pool target is superseded. Reduce the pool through staged,
individually justified removals. Judge the problem's
scientific interest and consequences independently of its current score, rank,
focus membership or the resulting category sizes. Early-ranked and previously
reviewed cards have no immunity. Do not fill category gaps merely to balance
the pool. Candidate-pool reduction is distinct from the nested benchmark quotas;
do not silently change or redistribute those quotas during pruning.
For editorial work, primarily develop Top 500 with importance and broad
coverage. Give secondary attention to its Top 100 priority subset. The retained
Top 1000 view does not create an additional research target. Publish each
completed card promptly. This records the content target and does
not initiate additional research during repository maintenance.
