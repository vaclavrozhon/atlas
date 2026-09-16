# Individual completion review — 13 September 2026

In progress. The user requested a thorough completion pass over every unfinished
active card. During the mobile-data phase the user prohibited pushes and large
network transfers; source checks used the local library and small textual requests.
Later on 13 September the user reported being on Wi-Fi and explicitly authorized
pushing the current workspace. This publication permission does not mark the
completion pass finished.

The baseline contains 1,049 canonical cards, of which 1,013 are active. Of these,
606 have unfinished evidence: 583 lack definitions and answer criteria, and 23
have developed statements, including eight explicit specification gaps. The
review starts with the one unfinished Top 100 card, then the other 174 unfinished
Top 500 cards, then the remaining 431 cards.

- [queue.json](queue.json) records individual progress and input/output hashes.
- [unfinished.md](unfinished.md) lists all unfinished active cards for review.
- [input-hashes.json](input-hashes.json) records the baseline of all canonical cards.
- [reviews.jsonl](reviews.jsonl) records substantive editorial decisions, source
  passages checked and the limits of each status check. It contains no full-card
  backups; completed active content lives in `data/cards/`, with subsequently
  deactivated records preserved in `data/archive/cards/`.

## Parallel review workflow

All processes sharing **this checkout** use the same active-only queue. From the
repository root, inspect the current state and atomically take one card:

```sh
python3 scripts/review_queue.py status
python3 scripts/review_queue.py list --available
python3 scripts/review_queue.py claim --worker review-2
```

`claim` returns JSON containing the card ID, path, current input hash and a unique
`token`. Save that token. Optional `--id TCS-6663`, `--area "Proof complexity"`
or `--priority top500` narrow the selection. Automatic selection preserves the
existing queue order. `list --json` provides machine-readable rows and reservation
owners. [unfinished.md](unfinished.md) is the readable inventory of all pending
active reviews, including reserved ones; the CLI shows live availability.

Reserve **before editing**. Perform the individual review described below, then
call `complete_review.complete(...)` with `claim_token` set to the returned token.
The helper requires the matching token for reserved cards, verifies the input
hash, validates the revised card, records its review and removes the reservation.
It also refreshes `unfinished.md`. Existing unreserved reviews can still finish
through the helper, but new workers should always reserve first. If the input
differs from the saved baseline, `baseline_changed` is true; inspect and reconcile
the current card, then supply its checked hash as `expected_sha256` as before.
Taking a card never changes its review state or counts it as complete.

If stopping before completion, release the reservation with its token:

```sh
python3 scripts/review_queue.py release --id TCS-6663 --token TOKEN_FROM_CLAIM
```

Reservations persist until explicit release or successful completion; they do
not expire during a long source review. A crashed worker leaves a visible
reservation. After establishing that it has stopped, its saved token can release
that reservation; an old token cannot release a subsequent worker's reservation.
The local runtime file `.review-claims.json` is ignored by Git. Its reservation
operations and completion use the same `.publish.lock`, so competing processes
cannot take the same card through this workflow. Separate clones/worktrees do
not share this lock: parallel reviewers must use the same checkout. Direct file
edits cannot be prevented by this cooperative reservation mechanism.

The canonical progress record remains `queue.json`; claims do not add a new
review state. `python3 scripts/review_queue.py export` rebuilds `unfinished.md`
after any older tool updates the queue. No command opens archived card bodies or
promotes a card merely because it was reserved or its fields were populated.

## Review standard and history

Completion means a source-grounded, self-contained mathematical statement,
definitions, an answer criterion requiring a Lean proof, substantive context and
dated progress. It does not assert that the problem has been solved, that source
proofs have been independently verified, or that a bounded literature search
establishes current openness conclusively. Evidence, formulation and current
status remain separate. Cards are never promoted solely because fields were
filled, and a genuinely unrecovered source target must retain its specific gap.

Existing individually assessed scores, categories, exclusions and prior
consolidation decisions are preserved. Previously unassessed cards require an
individual importance assessment under the completed-card rules; their new
scores have problem-specific reasons and may change membership of the ranked
exports. The queue priorities remain the baseline priorities, so this does not
silently shrink the review scope. The first Wi-Fi publication checkpoint completed
51 of the 606 baseline cards. The renewed request explicitly requires continuing
until every unfinished active card meets the P versus NP reference standard.
Independent concurrent card edits are not automatically credited as this pass’s
completed reviews.

The renewed active census started with 1,064 cards. It added eight developed cards
with outstanding model flags to the queue: TCS-0011, TCS-0465, TCS-0946, TCS-1714,
TCS-6578, TCS-6622, TCS-7177 and TCS-7330. All eight have now received individual
reviews. TCS-5851 had already been deactivated by another workspace change and
is recorded as out of the active scope; its inactive body was not reviewed as
part of this census. An additional individual audit of the developed active companion TCS-7260
extended the queue to 615 entries. A fresh active-only census subsequently added
299 already developed cards that still needed an individual quality and source
audit, increasing the queue to 914 entries. At the latest checkpoint, 232 are
completed, 681 pending and one outside active scope. The live counts
in `queue.json` are authoritative after this checkpoint. This remains incomplete.

`complete_review.py` records individually authored revisions after checking the
input hash under the publication lock. A concurrent change requires explicit
reconciliation; it is not overwritten using the old baseline. The ledger keeps
both substantive reviews and subsequent amendments, so its line count is not a
completion count. Selected primary source PDFs and extracted text are retained
locally in the ignored `sources/` cache to make the reviewed definitions and
theorem scopes inspectable. Source links and precise locators are versioned in
the cards and ledger; downloaded third-party texts are not redistributed.

On 13 September the user explicitly chose concrete editorial variants for the
eight previously documented specification gaps. Those cards now identify the
selected variant and preserve the broader source direction in context:

- TCS-3986: a fixed heuristic premise and the Boolean-or-permanent hardness disjunction.
- TCS-4259: the extremal round-reduction query function, up to universal constants.
- TCS-4457: algebraic interactions, total-variation sampling and bounded-probability postselection.
- TCS-4982: uniform randomized membership-query learning implying deterministic P equals NP.
- TCS-5209: exact weighted distances with deterministic subquadratic worst-case updates.
- TCS-5892: public-coin global-error direct sums for total Boolean functions.
- TCS-6756: the optimal approximation scale under UGC and NP not contained in BPP.
- TCS-6934: exclusion of linear-time CNF-SAT on deterministic multitape machines.

These choices do not retroactively attribute the precise variants to the source
authors. Their justification and status limits are recorded individually in the
review ledger. TCS-5158 was matched to a published negative resolution and retained
as a resolved canonical record, subsequently moved to `data/archive/cards/`
by the independent activity migration. Completed queue entries record their
current output path; archived content remains a completed review.

This checkpoint also completes and archives TCS-5494 (published matching bounds for
stochastic stationarity) and TCS-7008 (the explicitly selected fully polynomial
entrywise low-rank target under P different from NP). There are now 1,055 active
cards. Their model choices, resolution scope and full content are preserved. The
completion helper requires an explicit archival reason for an inactive outcome,
validates its content and immediately invokes the activity workflow.

TCS-6529 was also completed and archived after matching the planar Earth Mover
distortion target to the published STOC 2026 resolution. At this checkpoint
there are 636 detailed active cards and 419 pending active reviews in the queue.

The review continued on 14 September. The user reiterated that only active cards
are in scope; no pre-existing archived card bodies are being reviewed. The helper
now records the actual Prague calendar date rather than a fixed first-day date.
The current checkpoint includes exact matching, MST and convex-hull complexity,
three-dimensional point location, polygon visibility recognition, three separate
homeomorphism questions, EMD sketching, proper decision-tree learning and the
recursive teaching dimension conjecture. The queue remains incomplete.

Further individual checks completed TCS-0664 and TCS-1539 and matched three
previously active questions to published resolutions: TCS-0684 (horizon-free
reinforcement learning), TCS-3113 (improper agnostic CPAC impossibility), and
TCS-2654 (the general bounded-metric arbitrary-response online question). Their
full reviewed records were preserved through the archive workflow; pre-existing
archived bodies were not reviewed.

TCS-0671 now specifies the agnostic rate-comparison question and records a
matching August 2026 claimed refutation as uncertain. TCS-0683 specifies the
source-grounded reconstruction target with explicitly documented bounded-data
and computational-model choices, rather than conflating it with density learning.


The next checkpoint completes TCS-1573, TCS-2732, TCS-3025, TCS-0029,
TCS-0033, TCS-0027, TCS-0034, TCS-0861 and TCS-0862. In particular,
TCS-0033 records the published exponential separation while retaining the
broader extremal query-bound target. The quantum query/space card records the
September 2026 label-symmetry restriction, and the unitary-synthesis card
distinguishes restricted-query bounds from general polynomial-time synthesis.
All nine remain active. At that checkpoint 81 individual reviews had been
completed since the renewed request, in addition to the original 51.

The following checkpoint completes TCS-1138, TCS-5013, TCS-1043, TCS-1005,
TCS-0557, TCS-6599, TCS-6594 and TCS-0024. TCS-1043 was matched directly
to Göös’s published 2015 theorem and archived after its full review. No
pre-existing archived body was inspected. The remaining cards distinguish
conditional counting verification, layered versus general secure computation,
exact subexponential class quantifiers, randomized algorithm conventions and
the direction of circuit/proof-complexity implications. At this checkpoint
there are 1,057 active cards, 584 detailed active cards and 473 pending queue
entries; 89 reviews have been completed since the renewed request.


The current checkpoint additionally completes TCS-3031, TCS-0136, TCS-1015,
TCS-1016, TCS-1006, TCS-1018 and TCS-1014. The logic cards distinguish the full
Coq calculus from a proved consistent restricted fragment, and integer-order
register automata from dense-order models. The randomness cards recover exact
seed, entropy, circuit and uniformity parameters. TCS-1006 retains the universal
scalar-table question while recording the distinct July 2026 NC matching claim;
TCS-1014 checks the September 2026 published two-sided-expander result against
the constant-output-gap target. At this checkpoint 147 entries are completed,
466 remain pending and one is outside the active scope: 96 reviews since the
renewed request. There are 1,057 active cards and 591 detailed active cards.


The next three completed reviews are TCS-6660, TCS-6576 and TCS-1004.
They specify randomized same-problem kernelization with full encoding bounds,
the all-horizon asymptotic Euclidean chasing ratio, and deterministic relative
DNF counting with fully polynomial reciprocal-accuracy dependence. The running
checkpoint is now 150 completed entries, 463 pending and one out of active
scope, with 1,057 active cards and 594 detailed active cards. Of these reviews,
99 were completed after the renewed request.


Six further individual reviews complete TCS-6668, TCS-6839, TCS-6840,
TCS-6843, TCS-6857 and TCS-6851. They distinguish the cubic-lattice critical
temperature from the tree threshold, worst-state plus-boundary mixing from
2026 phase-ordering results, and interaction-wise monotonicity from
order-preserving dynamics. The expander and pivot cards now specify exact
walks and convergence targets. TCS-6851 corrects an imported exact-output
misreading by restoring Aldous–Fill’s supplied-start, fixed-relative-error
approximation question. The checkpoint has 156 completed entries, 457 pending
and one outside active scope, with 1,057 active cards and 600 detailed active
cards. There have been 105 individual completions since the renewed request.
The completed active-card hash audit passed; inactive bodies were skipped.


The following reviews complete TCS-6671, TCS-6620 and TCS-6672, preserving
their assessed scores. Euler-tour counting now has a labelled-edge normalization
and fully polynomial relative-accuracy guarantee. Vinogradov’s conjecture
specifies the unconditional all-primes target and its quantifier-negation. The
bounded-degree isomorphism tester uses two unknown input graphs, an explicit
edge-edit distance and worst-case sublinear query accounting. The running
checkpoint is 159 completed, 454 pending and one outside active scope, with
1,057 active cards and 603 detailed active cards; 108 completions occurred
after the renewed request.

The next checkpoint completes TCS-3037 (parity subgraph dichotomy) with explicit
deterministic FPT Turing reductions and the full 2024 hereditary/tree classification.
TCS-0543 now targets the source’s explicit polylogarithmic dynamic maximal matching
question, since its older sublinear threshold was solved in 2025 and improved in
2026. TCS-0536 distinguishes total edge-coloring update work from recourse, fixes
all-degree additive slack, and checks the May 2026 recourse results. TCS-0541
defines expected average stretch for actual spanning forests and separates these
from metric-tree embeddings. All three dynamic cards preserve their individual
scores. This checkpoint has 163 completed, 450 pending and one outside active
scope, with 1,057 active and 607 detailed active cards; 112 completions occurred
after the renewed request. The archive’s existing card bodies were not read.

The next checkpoint completes TCS-0545 with a specified deterministic black-box
weighted-matching conversion for every approximation ratio, distinguishing the
near-optimal SODA 2026 result. TCS-1116 now defines the universal additive EFX
constant with absolute 1/100 benchmark precision, positive-good comparisons and
complete allocations; it incorporates the July 2026 frontier revision and the
separate May 2026 EFkX results. TCS-0658 selects the quantum-ETH implication as
an explicit assumption variant of Bennett’s cryptographic-factor GapSVP question,
with exact promise, encoding and quantum-computation conventions. All three
scores were preserved. Counts are 166 completed, 447 pending and one outside
active scope, with 1,057 active cards and 610 detailed active cards; 115 reviews
were completed after the renewed request. The pass remains in progress.

Seven additional reviews complete TCS-0672, TCS-1052, TCS-1053, TCS-1034,
TCS-1035, TCS-1036 and TCS-1040. Identity testing now states the finite rational
efficient-functional branch explicitly and requires the same distance in both
bounds. The depth-three cards recover the original exponents, NP explicitness
and gate-count convention; restricted 2026 results are separated from those
targets. The four linear-circuit cards instead count wires, define each operation
and depth convention, and preserve the quantitative gap questions. In particular,
the 2017 polynomial XOR depth penalty resolves a narrower follow-up, not the
maximal-order question. The nonlinear card retains arbitrary-fan-in Boolean
gates and full-input correctness. All seven assessed scores were preserved.
Counts are 173 completed, 440 pending and one outside active scope, with 1,057
active and 617 detailed active cards; 122 completions followed the renewed
request. Existing archived card bodies remain outside the review.


Five further reviews complete TCS-0019, TCS-0017, TCS-0924, TCS-1099 and
TCS-1096. The formula cards distinguish failure of a polynomial upper bound
from eventual domination, and the constant-loss KRW formula-size variant from
depth and weaker-loss versions. TCS-0924 retains the original factor-four
improvement request and was matched to Shi Li’s published general-processing-time
result before being archived. The two bounded-arithmetic cards now supply the
complete BASIC axioms, full formula hierarchy and relevant induction schemes;
the circuit-unprovability card also defines the representation and arithmetic
upper-bound sentence. The February and April 2026 results are recorded with
their different theory and complexity-class scopes. All five scores were preserved.
The checkpoint is 178 completed, 435 pending and one outside active scope, with
1,056 active cards and 621 detailed active cards; 127 reviews followed the renewed
request. The 176-entry hash audit checked 167 then-active outputs with no hash
mismatches and skipped all nine inactive bodies. Forty-three original completed
records predate the separate quality_review metadata field; that absence was
recorded as a metadata difference, not silently filled or treated as a new review.


Eight further individual reviews complete TCS-0287, TCS-5011, TCS-5825,
TCS-2861, TCS-0306, TCS-7260, TCS-6650 and TCS-7194. The sequence extractor
specifies conditional effective dimensions and global oracle independence. The
perceptron card recovers the source's polylogarithmic slack and distinguishes
the Gaussian conjecture from the Rademacher lower-bound theorem. Prefix-U-one
retains worst-case operation cost. Matroid WNR sampling uses the base polytope,
exact marginals and an explicit expected-time oracle model, with the 2026 proof-gap
discussion recorded. The three d-DNNF cards distinguish polynomial-time
complementation, polynomial-size existence and deterministic equivalence;
the structured-output lower bound is not applied to unrestricted circuits.
TCS-7260 was an already developed active companion without an individual
completion review and was added to the queue for this audit, increasing its
scope from 614 to 615 entries. TCS-7194 distinguishes expanded shortest-solution
length from compressed size and fixes the universal polynomial exponent.

The checkpoint is 186 completed, 428 pending and one outside active scope, with
1,056 active cards and 628 detailed active cards; 135 reviews followed the renewed
request. The active-output hash audit checked 177 completed active records with
no mismatches and skipped all nine inactive bodies. The queue is not a certificate
that every older developed active card has already passed individual quality
audit; that remaining census is still part of the requested work. No pre-existing
archived card body was reviewed. This pass remains incomplete.


Nine further individual reviews complete TCS-6285, TCS-2029, TCS-4746,
TCS-3886, TCS-4988, TCS-5593, TCS-6139, TCS-6091 and TCS-6712. The
randomized-class questions now distinguish accepting computation paths, error
parameter quantifiers, globally gapped witness predicates and effective
representative enumerations without an extra computable-clock requirement.
TFNP uses all-input totality and the source's many-one search reductions. The
Black-Box Hypothesis includes unary size bounds and full computational cost.
The random-tape card restores arbitrary two-way access and records its explicit
sublinear-exponent convention; the depth-three card fixes the E evaluator and
infinitely-often class noncontainment convention. Restricted and conditional
results are distinguished from general resolutions.

TCS-6712 was an active duplicate of TCS-0019: formula balancing and polynomial
padding make its nonuniform class equality the negation of the retained
linear-circuit separation. After an individual source and quantifier review,
its content was preserved through the archive workflow, and the retained card
now includes the equivalence and all source provenance. No pre-existing
archived card body was reviewed.

This checkpoint is 195 completed, 419 pending and one outside active scope,
with 1,055 active cards and 636 detailed active cards; 144 reviews followed the
renewed request. The active-output hash audit checked 185 completed active
records with no mismatches and skipped all ten inactive bodies. Individual
audits of the older developed cards outside this queue also remain in scope.
The completion pass is still in progress.


The next seven reviews complete TCS-6714, TCS-6817, TCS-6978, TCS-1602,
TCS-7222, TCS-6747 and TCS-6743. The matching card specifies nonuniform
logarithmic-depth circuits and explains the source’s equivalent threshold-matching
variant. Directed reachability uses a single uniform machine meeting both time
and space bounds. The explicitly selected quasilinear multitape-time versus
linear-space variant is covered by Williams’s published 2025 theorem; its complete
card was preserved through the archive workflow rather than advertised as open.

Tournament king search now has a full deterministic decision-tree target with
constant-factor asymptotic precision. The expected randomized improvement,
partial reachability and resolved strong-king problem remain distinct. The two
graph-isomorphism cards specify deterministic and bounded-error randomized
computation separately, handle malformed encodings, incorporate the author’s
2017 correction and distinguish parameterized progress from a general algorithm.
Randomized evasiveness explicitly selects the two-sided-error question and checks
original query-model definitions before describing zero-error lower bounds.

The fresh census corrects the earlier informal tracking of older developed
cards: 299 active records without an individual quality audit were added to the
queue, without editing or promoting their bodies. Existing wording reviews or
filled definitions alone were not credited as this audit. One of these, TCS-7222,
has now received its individual review. The 153 already individually reviewed
active cards outside the queue remain separately accounted for.

At this checkpoint there are 1,055 active cards: 344 have an individually
recorded completion/quality review, and 711 still require work. A total of 643
have definitions and an answer criterion; this structural count is not a
completion certificate. The queue has 914 records: 202 completed (191 still
active and 11 subsequently archived), 711 pending and one previously removed
from active scope. There have been 151 completions since the renewed request.
No pre-existing archived card body was reviewed. The overall pass remains
incomplete. Concurrent community-feedback edits are retained separately and
are not automatically counted as new individual completions.

Validation for this checkpoint: `make check` passed in the shared workspace;
publication and the complete active-card KaTeX check passed in an isolated
checkout containing the individually reviewed changes (15,941 expressions).
The isolated publication contains 1,054 active cards; the additional new card
in the shared workspace belongs to concurrent feedback work and remains
pending in this pass. The active completion-output hash audit has 191 matches
and skips all 11 subsequently archived bodies. Previously completed TCS-0019
and TCS-0020 received separately checked contextual feedback additions without
changing their completed targets; the ledger records the updated hashes.


The final deployment of checkpoint 202 used the combined shared workspace,
including the concurrent community-feedback changes and the new active card.
It superseded the temporary isolated build described above: all 1,055 active
cards and 15,974 mathematical expressions passed publication validation, and
live version `f4ccfe1b302db8a9096a` was verified after deployment
`7e9beab74cbb8d856608d7190af10c1ffe86d403`.

Six further individual reviews complete TCS-6593, TCS-6595, TCS-6592,
TCS-6532, TCS-6617 and TCS-6601. ETH and SETH now define attainable
exponential rates, distinguish infima from attained bounds, and state the
precise order of their algorithm and width quantifiers. The FPT card fixes
uniformity, complete input length and parameterized many-one reductions.
The polynomial-hierarchy card repairs incorrect Sigma notation and specifies
the all-level assertion and its finite-collapse negation. Factoring fixes the
full output, bit model, success probability and worst-case random clock.
Extended Frege specifies its proof encoding and extension freshness, and
checks Cook's correction and the scope of recent conditional, algebraic and
intuitionistic results. All six retain their assessed importance and categories.

Checkpoint 208 has 1,055 active cards: 350 individually completed/reviewed and
705 pending. The queue has 208 completed records, comprising 197 active cards
and 11 subsequently archived cards, plus 705 pending and one outside active
scope. The 153 independently reviewed active cards outside this queue remain
separately counted. There have been 157 completions since the renewed request.
No pre-existing archived card body was inspected. Filled fields alone are not
credited as a completed quality audit, and the overall pass remains incomplete.

Validation for checkpoint 208: `make check` passed, combined shared-workspace
publication passed, and `node tests/math.cjs` checked all 1,055 active cards
and 16,016 mathematical expressions. `git diff --check` passed. The completion
hash audit matched all 197 completed active outputs and skipped all 11 inactive
bodies. The published version is `7a41d3e7a6247773f215`. Concurrent community
changes are retained in the combined publication without being automatically
credited as this pass's individual completions.


Four further individual reviews complete TCS-0007, TCS-6603, TCS-4245 and
TCS-6571. The matrix-multiplication exponent retains the approved absolute
1/100 numerical target while making arithmetic circuits and infimum bounds
precise. Log-rank fixes the protocol and real-rank models and distinguishes
one-sided rectangle partitions from full deterministic protocols. Parity games
now specify arbitrary vertex ownership, binary priorities and a uniform bit
model; the November 2025 claimed solution remains explicitly unverified,
with the June 2026 CONCUR revision recorded separately. Hilbert's tenth
problem over Q now specifies full total computability and Lean acceptance,
with source-checked distinctions from integer rings, universal quantifiers
and extra height predicates. Existing scores and categories are retained.

Checkpoint 212 has 1,055 active cards: 354 individually completed/reviewed and
701 pending. Its queue contains 212 completed records (201 active and 11
subsequently archived), 701 pending and one outside active scope. The other
153 reviewed active cards are accounted for separately. There have been 161
completions since the renewed request. The completed active-output hash
audit matches all 201 records; inactive bodies were skipped. The overall
pass remains incomplete.

Validation for checkpoint 212: `make check` passed. Combined workspace
publication and `node tests/math.cjs` passed for all 1,055 active cards and
16,077 mathematical expressions; version `c296ba06b37299573e06`. The
publication retains the concurrent community-feedback changes.


Four further individual audits complete TCS-6656, TCS-6666, TCS-0021 and
TCS-6651. Planted clique now fixes the exact-size planted distribution,
balanced testing success and eventual-success quantifiers, distinguishing
stronger advantage hypotheses, restricted refutation lower bounds and new
conditional applications. The tau conjecture specifies charged construction
of integer constants, distinct integer roots and its full exponent negation;
the source review separates finite circuit censuses from asymptotic evidence.
The NP circuit card fixes nonuniform size bounds and their infinitely-often
negation, including the scopes of natural proofs, ACC and depth-two threshold
results. Hadwiger now has full Lean acceptance, precise ordinary branch sets,
correct small-case indexing, and a source-checked distinction from odd minors.
The recent triple-logarithmic coloring theorem remains a preprint claim.
All four retain their assessed importance and categories.

Checkpoint 216 has 1,055 active cards: 358 individually completed/reviewed and
697 pending. The queue has 216 completed entries (205 active and 11 subsequently
archived), 697 pending and one outside active scope. The other 153 individually
reviewed active cards remain separately accounted for. There have been 165
completions since the renewed request. The completed active-output hash audit
matches all 205 records and skips all 11 inactive bodies. The overall pass
remains incomplete; concurrent feedback work is preserved separately.

Validation for checkpoint 216: `make check` passed, followed by combined
workspace publication and `node tests/math.cjs` for all 1,055 active cards and
16,233 mathematical expressions. Version `765f3cb7d9b99f5b53fc` retains the
concurrent community-feedback changes. Source hashes match all 205 completed
active outputs; no inactive card body was read.

Four further individual audits complete TCS-6618, TCS-6611, TCS-7314 and
TCS-7248. Prime-field discrete logarithms now specify a complete uniform
classical bit model, per-instance success, full input and output encodings,
and the scope of generic, small-characteristic and quantum results. Permanent
versus determinant fixes unrestricted complex affine representations,
nonuniform matrix size and the quantifiers of superpolynomial growth, and
separates ordinary representations from border, symmetry and additive
Boolean-sum restrictions. Komlós fixes full real-matrix signing and its
unbounded-discrepancy negation. Its status review was amended before
publication after a further search located the 10 September Guo–Fang–Lu
preprint claiming the full constant bound: the target matches, but the new
proof has not been independently verified, so the card remains active with
uncertain status. The earlier same-day negative search conclusion is
explicitly superseded in the ledger. Tutte 5-flow fixes integer conservation,
parallel edges, components and Lean acceptance, with primary-source context
and a distinction between existence and the recently refuted reconfiguration
property. Existing importance assessments and categories are retained.

Checkpoint 220 has 1,055 active cards: 362 individually completed/reviewed and
693 pending. Its queue contains 220 completed records (209 active and 11
subsequently archived), 693 pending and one outside active scope. The other
153 reviewed active cards are counted separately. There have been 169
completions since the renewed request. The active-output hash audit matches
all 209 completed records and skips all 11 inactive bodies. The overall pass
remains incomplete; an uncertain scientific status does not prevent completion
of an accurately qualified editorial review.

Validation for checkpoint 220: `make check` passed before the final Komlós
status amendment; that amendment passed canonical validation, followed by
combined-workspace publication and `node tests/math.cjs` for all 1,055 cards
and 16,381 mathematical expressions. Published version:
`8e9f60788f9b38e408f9`. Concurrent community-feedback work is preserved in the
combined publication and is not automatically credited as individual review.

Four further individual audits complete TCS-7315, TCS-6523, TCS-5773 and
TCS-6682. Beck–Fiala now specifies full binary-matrix signing, universal
constants, its unbounded-discrepancy negation and the ranges of recent
partial results; the 10 September full-target proof claim is marked uncertain
pending independent verification. KLS fixes the isotropic log-concave measure,
function class, variance and gradient conventions, and distinguishes Cheeger
and Poincaré normalizations and recent thin-shell and quadratic-function
results from the full conjecture. Skolem specifies a uniform total decider,
exact finite input syntax, zero-index and degenerate recurrence conventions,
and the scopes of corrected low-order, density-one and conditional results.
Reed now has full Lean acceptance, precise finite graph parameters and the
exact ceiling, with corrected clique-blowup and strict recolouring-threshold
context. All four preserve assessed importance and categories.

Checkpoint 224 has 1,055 active cards: 366 individually completed/reviewed and
689 pending. The queue contains 224 completed records (213 active and 11
subsequently archived), 689 pending and one outside active scope. The other
153 reviewed active cards are counted separately. There have been 173
completions since the renewed request. The active-output hash audit matches
all 213 completed records and skips all 11 inactive bodies. The overall pass
remains incomplete. Concurrent feedback work remains separate and is retained
in combined-workspace publication.

Validation for checkpoint 224: `make check` passed, followed by combined
workspace publication and `node tests/math.cjs` for all 1,055 active cards and
16,551 mathematical expressions. Published version: `393f22252d7b8e34a040`.
The snapshot retains the concurrent community-feedback changes; subsequent
independent card edits are not credited as this pass’s completed reviews.

Deployment note for checkpoint 224: concurrent publication advanced the shared
build before the Pages snapshot. The deployed combined version was
`e18fb388ad4dac4a8223`, commit `8a8c218920472530e89ddd5f3118298fdf8b993f`,
and its live version was subsequently verified. It includes the four audited
cards and the concurrent updates. A later combined build also passed all
mathematical rendering checks for 16,582 expressions. The source commit for
the four owned reviews is `28001fb9`; concurrent canonical work was preserved.

Two further individual audits complete TCS-7230 and TCS-7221. Tarski’s
exponential-function problem now has a fixed finite sentence grammar, uniform
total bit-machine semantics and exact Lean acceptance, with the real Schanuel
assumption and the weaker effective separation condition correctly separated.
Its June2026 source gives unrestricted decidability only conditionally; the
unconditional restricted model-completeness result does not settle the target.
The #BIS audit corrects the 2019 author list and reconciles the differently
titled 2023 preprint and ICALP2024 article. It specifies explicit graph and
accuracy encodings, relative error, every-random-tape runtime and the full
impossibility negation, and distinguishes fixed-density, random-regular and
balanced-count results from the total count on all bipartite graphs.

The combined checkpoint 232 census is 1,055 active cards: 374 individually
completed/reviewed and 681 pending. Six other individually completed records
were added to the shared ledger by the concurrent random-card review:
TCS-7365, TCS-7227, TCS-1021, TCS-6112, TCS-0073 and TCS-0985. These are
separately authored reviews, rather than automatic credit for field edits.
The queue has 232 completed records (221 active and 11 subsequently archived),
681 pending and one outside active scope; the other 153 reviewed active cards
remain separately accounted for. The overall active-card pass is incomplete.

Validation for the combined checkpoint 232: `make check` passed. Publication
and `node tests/math.cjs` passed for all 1,055 cards and 16,743 mathematical
expressions, version `b031d8f5e440b0e4a108`. All 221 completed active output
hashes match; the 11 inactive card bodies were skipped. The two owned source
reviews are committed with their own queue and ledger snapshot; the six
concurrent completions remain preserved for their separate source commit.

Deployment note for checkpoint 232: concurrent publication advanced the shared
build before the Pages snapshot. The actual deployed and live-verified version
was `463b6bec23bf6ba5a023`, Pages commit
`f561c2282224ce1a64cf8f52264509336763f8a3`. It retained the combined updates.

Two further owned audits complete TCS-7229 and TCS-6545. Both now specify
uniform classical bit-machine conventions, independent probability spaces,
eventual negligible security, full Lean acceptance and the actual negation of
the one-way-function existence implication. Key agreement keeps arbitrary
polynomial interaction and full-key indistinguishability; public-key encryption
keeps the approved bit-message chosen-plaintext model and average correctness.
The audits distinguish oracle-query bounds, restricted reductions and extra
bounded-storage assumptions from the unrestricted targets.

The follow-up PKE search found Li–Ni–Zan ePrint 2023/1260, which explicitly
claims the full positive implication. Neither its proof nor a conclusive later
assessment was verified. Both cards therefore have uncertain scientific
status and remain active. A logged amendment corrects the initial key-agreement
no-claim-found note. The PKE review also checks the corrected April 2009
Barak–Mahmoody theorem and the May 2026 publication of the specific MinRank
construction.

The combined checkpoint 238 has 1,055 active cards: 380 individually completed
or reviewed and 675 pending. The queue contains 238 completions (227 active,
11 subsequently archived), 675 pending and one outside active scope. Ten
concurrent random-card reviews are included in this combined accounting,
separately from the owned source changes; the four added since checkpoint 232
are TCS-6450, TCS-0811, TCS-4715 and TCS-4238. The other 153 reviewed active
cards remain separately accounted for. The whole pass is still incomplete.

Validation: `make check` passed for the two owned edits. Combined publication
was repeated after the concurrent author repaired a formula delimiter in
TCS-4238; the subsequent `node tests/math.cjs` passed all 1,055 active cards
and 16,901 expressions. The published build is `81289a35b2eea279ca5b`.
All 227 completed active output hashes match; the 11 inactive bodies were
skipped. Concurrent source work is preserved for its separate commit.


Two further owned reviews complete TCS-6646 and TCS-6635. Martin’s conjecture
now has explicit cone and ordinal-rank quantifiers, both conjecture parts,
full determinacy/dependent-choice assumptions and faithful internal set-theoretic
Lean acceptance. The audit reads the corrected order-preserving result, the
survey erratum at limit ordinals, and the differently scoped 2026 Day–Marks
paper. Choice-based counterexamples do not refute its determinacy target.

The promise-CSP card preserves its unconditional fixed-template decision target,
with precise explicit encodings, uniform algorithms, promise reductions and the
full negation. It removes the old algorithm instructions, adds the 2019 symmetric
Boolean classification without negations and the July 2026 three-element target
classification, and checks the conditional scope of the LICS 2026 result.

Checkpoint 240 has 1,055 active cards: 382 individually completed/reviewed and
673 pending. The queue contains 240 completions (229 active and 11 later
archived), 673 pending and one outside active scope; 153 reviewed active cards
are separately accounted for. Ten completed concurrent random-card reviews
remain preserved separately from the owned source commit. The full pass is
still incomplete.

Validation: make check and publication passed. The combined build version is
40298fc778ed5961c111, and node tests/math.cjs passed all 1,055 active cards and
16,997 expressions. All 229 completed active output hashes match; the 11
inactive card bodies were skipped.


Four further owned reviews complete TCS-6446, TCS-7235, TCS-7220 and TCS-6624.
The quantum-PCP card preserves the saved classical-reduction variant and names
that qualifier explicitly: the original 2013 source instead permits quantum
reductions, so their equivalence is not asserted. Its audit checks normalized
energy, exact local-matrix encodings, QMA promises, complete Lean acceptance,
the corrected status of the games formulation, NLTS and the restricted scope
of 2025–2026 amplification and interactive results.

The three edit-distance reviews define their respective quantifier orders and
bit costs: near-exact almost-linear approximation, near-exact truly subquadratic
approximation and constant-factor approximation with a fixed polylogarithmic
overhead. The first two keep unit-cost substitutions distinct from the
insertion/deletion convention in a cited intermediate manuscript. The audit
checks the July 2022 constant-factor theorem and its August 2026 journal
publication, the March 2026 approximation scheme and its June STOC provenance,
the additive term in the far-pair result, and the conditional scope of exact
edit-distance hardness. Neither n to a fixed exponent above one nor the
subpolynomial saving in the 2026 scheme is substituted for a stronger target.

Checkpoint 245 had 1,055 active cards: 387 individually completed/reviewed and
668 pending. Its queue contained 245 completions (234 active, 11 subsequently
archived), 668 pending and one outside active scope. Eleven concurrent random
reviews were included, with TCS-1019 newly completed since checkpoint 240.
The other 153 reviewed active cards are separately accounted for. All 234
active output hashes matched, and the 11 inactive bodies were skipped.

Validation for checkpoint 245: make check and publication passed. The combined
publication version was 1941c00367b60eb9c4c9; node tests/math.cjs passed all
1,055 active cards and 17,133 expressions. Two further concurrent reviews,
TCS-7113 and TCS-0247, subsequently advanced the combined count to 389 reviewed
active cards and 666 pending (247 queue completions, including 11 inactive).
All 236 completed active output hashes match. These thirteen concurrent source
reviews remain preserved for their separate source commit. The full pass is
still incomplete.


Two further owned reviews complete TCS-7234 and TCS-6667. They retain the same
unrestricted rational-basis short-vector target with distinct uniform quantum
and classical randomized bit models, fixed rank-only approximation exponents,
nonzero output on every run and complete Lean acceptance. The quantum review
records the disputed August 2026 DCP claim and the September response, including
failed ePrint PDF retrieval and the unverified scope of the linked Lean code;
it no longer says that no claim was found. Decision, uniqueness promises and
arbitrary-basis search remain explicitly distinct.

The classical audit visually checks the scanned LLL short-vector and bit-cost
propositions, checks the exact certificate and conditional-hardness scopes,
and reads the PotBKZ theorem including coefficient, enumeration and node costs.
The 2024 Shenoy factor depends on the actual basis and does not establish a
uniform polynomial in rank. Wan’s 8 September major revision expressly drops
its first version’s dimension-dependent claims; the retained constant-factor
claims are identified as unverified. April deterministic-subexponential
reductions, the September RANDOM publication and generic-metric oracle bounds
are scoped separately from the full target.

Checkpoint 251 has 1,055 active cards: 393 individually completed/reviewed and
662 pending. The queue contains 251 completions (240 active and 11 later
archived), 662 pending and one outside active scope; 153 reviewed active cards
remain separately accounted for. All 240 completed active hashes match, and
inactive card bodies were skipped. Fifteen concurrent random-card reviews are
included, with TCS-7113, TCS-0247, TCS-5085 and TCS-7257 added since checkpoint
245; their source changes remain preserved for separate commits.

Validation: make check passed; publication produced 0e44573e820d0fecaac8;
node tests/math.cjs passed 1,055 active cards and 17,377 expressions. A subsequent
sixteenth concurrent completion, TCS-7373, advances the combined queue to 252
completed and 661 pending, or 394 reviewed active cards. The overall pass is
still incomplete.

Deployment note for checkpoint 247: the combined root build was deployed and
live-verified as a6e9bc6def6bbba3d8ac, Pages commit
c6288951c454d4c7c542d9b653ae9d325a4512fe. Concurrent publication had advanced
the shared build; the combined state was retained.

Checkpoint 257 completes TCS-6665, the rational finite-alphabet private-message
broadcast capacity function. It now has complete deterministic code maps, a
joint average-error criterion, explicit base-two units, the entire channel-table
domain and corrected 1/100 Lean acceptance. The review checked Marton’s original
model, the finite auxiliary-cardinality theorem, product-channel sum-rate
regularization, the conditional convergence hypotheses in the 2024 full-text XML,
and the actual scope of the 2026 outer-bound and Marton-suboptimality manuscripts.
The latter’s unconstrained example has an enlarged rational alphabet; its proof
and numerical certificates were not independently verified.

The combined census is 1,052 active cards: 396 individually completed/reviewed
and 656 pending. The queue has 257 completions, including 14 now-inactive records
whose bodies were skipped; all 243 completed active queue output hashes match.
Twenty concurrent individual reviews are included, with TCS-3631, TCS-5127,
TCS-4099 and TCS-0818 added since checkpoint 252. The last three of those were
individually retired as resolved in that concurrent review. They are separate
from the owned broadcast-card change.

Validation for checkpoint 257: make check and make publish passed; the combined
publication is de64c6070abf16f85a8d. The math check passed 1,052 active cards and
17,427 expressions. The earlier checkpoint 252 deployment produced Pages commit
5eea803f86ddddc21dc65f65980207d531389392 (version 0c9fc96da100fd698dc2); the
subsequent concurrent publication was live-verified as a38f481993089503a57f
with publication timestamp 2026-09-14T19:55:27+00:00.

Checkpoint 261 completes TCS-6606 and TCS-6628. The Gaussian-interference
review repairs the channel and acceptance formulas, preserves the full real
domain and average-message power model, distinguishes complex-channel constant
gaps from the requested real-unit tolerance, and qualifies all current claims.
The 2026 outer-bound manuscript’s body only gives the recorded very-weak and
one-sided specializations; Khandani v12 remains unverified. The 2013 survey’s
pagination was corrected against the publisher’s summary.

The general perfect-matching FPRAS card now specifies its full bit encoding,
finite probabilistic machine, every-tape polynomial clock, relative error and
Lean acceptance. The chain lower bound was corrected to its actual disjunction:
exponentially small perfect-matching stationary mass or exponential mixing.
The review distinguishes unweighted all-matchings counting from the unary-weight
monomer–dimer result, and records the 2026 bipartite and fixed-density advances
without expanding their scope.

The combined census is 1,052 active cards: 400 individually completed/reviewed
and 652 pending. The queue has 261 completions, including 14 inactive records.
Twenty-two concurrent individual reviews are included, with TCS-1007 and
TCS-0652 added since checkpoint 257. make check, publication and the active
formula check passed for this checkpoint. Checkpoint 257 was deployed and
live-verified at a34d3b2c663110bfe8a5, published 2026-09-14T20:07:34+00:00,
Pages commit 5e94e207f87329af478f26a5cd0dd1b80ac826e2.

Checkpoint 265 completes TCS-6629, the deterministic nonnegative permanent
FPTAS question. The target now specifies a single finite deterministic machine,
full rational encodings, a universal polynomial bit clock, exact zero behavior,
relative error and complete Lean acceptance. The review checked the 2019 Bethe
comparison, the precise current versions of the August/September 2026 factor
improvements, and the fixed density/weight assumptions in the new dense-matrix
FPTAS. Recent proofs and any linked formalization were not independently
verified. The former block-replication instructions and methodological hints
were removed. No new partial guarantee was treated as the full FPTAS.

The checkpoint 265 census was 1,052 active cards: 404 individually completed/
reviewed and 648 pending. The queue included 265 completions and 14 inactive
records; all completed active output hashes matched. Twenty-five concurrent
individual reviews were included, with TCS-0469, TCS-0056 and TCS-6944 newly
completed. The subsequent concurrent TCS-0761 review raises the total to 266
completions, 405 completed/reviewed active cards and 647 pending, with 26
concurrent individual reviews credited. Publication and the formula check passed
for checkpoint 265: 1,052 cards and 17,671 expressions. The preceding full
make check passed at checkpoint 261. That checkpoint was deployed and
live-verified as a8e21ac4f81da82327b2, published 2026-09-14T20:19:35+00:00,
Pages commit e06420b08cfe17610b850a54cd41f71b4132ac2a.

Checkpoint 267 completes TCS-6616. The exact permanent question now has an
explicit portable rational-coefficient uniform-circuit formulation, separately
identified as an editorial model choice. It specifies full generator and circuit
encodings, construction time, arithmetic size and a universal characteristic-zero
identity. The review distinguishes finite-ring, integer bit-complexity, restricted
formula and conditional tensor-rank results from this target. The current
versions and theorem scopes of the ICALP 2019/2026 papers, Li's revised paper
and the July 2026 Fourier preprint were checked without independently verifying
their complete proofs. Its publication and active formula checks passed; the
latter covered 1,052 cards and 17,927 expressions. The preceding checkpoint 266
was live-verified at 0c402cc5daac7bdd8f75, published 2026-09-14T20:26:19+00:00,
Pages commit c973b17936a6c87abb4d9d9a363afb64588cc813.

The combined working census subsequently reached 271 queue completions after
the concurrent individual reviews of TCS-0538, TCS-0787, TCS-6125 and TCS-7023.
There are 1,052 active cards: 410 completed/reviewed and 642 pending. Fourteen
completed queue records are inactive; 153 previously individually reviewed active
cards are outside the queue. On 15 September the user requested a shared list for
parallel processes. The reservation CLI and automatically refreshed unfinished
inventory above implement that handoff without changing review states or counts.

Checkpoint 277 completes TCS-6663 and TCS-6602. The Frege/EF comparison
now fixes its full syntax, acyclic definitions and proof-bit accounting while
retaining size-only simulation. Its context corrects the fixed-parameter scope
of the Kneser–Lovász result and distinguishes the June rewriting theorem's
short chains from an efficient chain constructor. The modular Frege card fixes
a complete finite basis, source modular axioms, flattened line depth and full
proof and construction encodings. It retains one uniform DNF family per prime
across every fixed depth and makes both Lean answer directions explicit.
The no-short-proof DNFs of ITCS 2026 still have unproved tautologicity in the
checked version; parity-resolution depth bounds and restricted algebraic
certificates were not promoted to unrestricted modular Frege results.

The combined checkpoint includes the concurrent completed reviews TCS-6708,
TCS-6036, TCS-6724 and TCS-6836, bringing the working count to 416 reviewed
active cards and 636 pending out of 1,052 active cards. Publication and the
formula check passed for this checkpoint, covering 18,155 expressions. The
shared-queue implementation also passed five tests, including a six-process
reservation race, stale-token rejection, active-only listing and the complete
review's ownership/hash/release path; the full make check passed. The preceding
combined deployment was live-verified as 48b5ed741f8159a84dec, published
2026-09-15T07:37:26+00:00, Pages commit
4bed98731b284db33b0d44080b1647425c23756a.

Checkpoint 283 completes TCS-0025 and TCS-6652. Unrestricted Frege now
has complete proof-bit accounting and both Lean answer directions, with no
extra uniform hard-family or line-size requirement. Its review distinguishes
the April tree-like and bounded-depth results, the June algebraic lower bound
and the September restricted-IPS upper bound. The Erdős–Hajnal review fixes
finite graph domains and the all-exponents negation, removes methodological
instructions, checks the recent special cases and marks the unverified revised
full-solution claim as uncertain. The withdrawn older proof was not treated as
a refutation of the revision.

The combined working census is 1,052 active cards: 422 individually completed/
reviewed and 630 pending, including the concurrent completions TCS-0594,
TCS-3059, TCS-6898 and TCS-1011. There are 283 completed queue records,
14 of them inactive; all 269 completed active output hashes match. Publication
and the active formula check passed, covering 18,379 expressions. The preceding
deployment was live-verified as 6110b063f40c559c1561, published
2026-09-15T09:33:09+00:00, Pages commit
1f9bbcdb61192cfcfa9790776f55fa77788891d0.

Checkpoint 285 completes TCS-6604, the classical Fourier Entropy–Influence
conjecture. It now has exact spectrum and bit-flip conventions and full Lean
acceptance in both directions. The review removes proof instructions, checks
the accuracy dependence of the DNF consequence, restores the 2011 provenance
of the coordinate-entropy bound, distinguishes online journal and revision dates,
and verifies that both August counterexample papers concern different scalar or
operator domains. The June separation results retain their model assumptions.
No new preprint proof was independently certified.

The working census, including concurrent TCS-6768, is 424 individually completed/
reviewed active cards and 628 pending out of 1,052. The queue has 285 completed
records, including 14 inactive records. Publication and the active formula check
passed, and completed active output hashes match. Checkpoint 283 was deployed
and live-verified as 0d45cbd9d21acc4a1312, published
2026-09-15T09:52:46+00:00, Pages commit
f01edee623edfb7eda967271dc1922dae0043fc0.

Checkpoint 289 completes TCS-6612, VP versus VBP over the complex numbers.
The card fixes nonuniform polynomial families, semantic degree, circuit and
branching-program encodings, coefficient accounting and both Lean answer
directions. It distinguishes exact computation from border approximation,
restricted multilinear lower bounds and the different symmetry/orbit-size
classes of the 2026 separation. The current ECCC primer, original factor-closure
paper, depth survey and recent primary sources were checked at their stated
locators; the min-plus comparison used the current abstract only. No new proof
was independently formalized or certified.

At that checkpoint the census was 1,052 active cards: 428 individually completed/
reviewed and 624 pending, including concurrent completions TCS-0494, TCS-1061
and TCS-5520. Publication and the active formula check passed, covering 18,564
expressions. The later combined census reached 295 completed queue records,
16 inactive, with all 279 completed active output hashes matching. Its 1,050
active cards comprise 432 completed/reviewed and 618 pending after concurrent
reviews TCS-6477, TCS-6723, TCS-0491, TCS-7361, TCS-1135 and TCS-7351; the
first two were individually resolved and archived by the parallel reviewer.
The previous combined deployment was live-verified as 0e0ff836ab08b03d1381,
published 2026-09-15T15:16:44+00:00, Pages commit
82bf0b9e9a18e74a624c6d8df44e5e01517a3690.

Checkpoint 298 completes TCS-6647, rigidity of the full Turing-degree order.
The review fixes full oracle/quotient conventions and both Lean answer directions,
removes construction suggestions, distinguishes global restrictions from local
structures, and checks the precise cone, jump and representation results. It
adds the 2018 local structural theorem and 2021 conditional genericity result
without dropping its continuum-hypothesis assumption. Cooper's author-uploaded
Theorem 1.1 was matched to the full negative answer, with the later primary
survey's unverified-construction assessment preserved. Status is now uncertain;
no proof or refutation of that construction was certified.

Including concurrent TCS-6953 and the individually resolved/archived TCS-1009,
the combined census is 1,049 active cards: 434 individually completed/reviewed
and 615 pending. The 298 completed queue records include 17 inactive records;
all 281 completed active output hashes match. Publication and the active formula
check passed, covering 18,719 expressions. The preceding combined deployment
was live-verified as e7fc652b18d7cf23e197, published
2026-09-15T17:12:50+00:00, Pages commit
2b8cb4617923505c0d4debc6c862c91b6caabac4.

Checkpoint 301 completes TCS-6638, the optimal approximation ratio for unrelated
machine makespan. It retains the user-authorized numerical target and adds full
binary encodings, deterministic bit complexity, zero-optimum handling and
infimum quantifiers without attainment. The original journal's model and main
bounds were visually checked, with rational/zero/forbidden-entry compatibility
recorded separately in the audit. The card removes rounding walkthroughs, fixes
the two-value exponent, keeps hardness assumptions explicit and distinguishes
prediction budgets and the fair-mechanism result's optimal initial allocation.
The latter was checked in its June 2026 revision; the full 2005 rounding proof
was not retrieved and is not represented as reviewed.

With concurrent TCS-1029 and TCS-0848, the census is 1,049 active cards: 437
individually completed/reviewed and 612 pending. The 301 completed queue records
include 17 inactive records; all 284 completed active output hashes match.
Publication and the active formula check passed, covering 18,868 expressions.
An earlier deployment attempt encountered bare-string source_formulation fields
in the two concurrently completed cards; their owner corrected the metadata
shape and ledger hashes without changing mathematical content. The retry
succeeded and was live-verified as 86b3654cee038a0fb50c, published
2026-09-15T17:23:02+00:00, Pages commit
62982f7295786d0fb363901c8e8effbcae53ef7a.

Checkpoint 308 completes TCS-6625, exact deterministic fully dynamic
connectivity. The card now fixes finite uniform word-RAM semantics, initialization,
all sequence lengths, persistent storage and both complete Lean answer directions.
It removes algorithm and potential-derandomization instructions. Primary bounds
were checked with their amortization, randomness and cell-width restrictions.
A newer FOCS 2026 accepted-paper title was found and corroborated on an author
page, but the inspected entries supplied neither a theorem nor manuscript link.
The card remains active with uncertain current status; no deterministic theorem
was inferred from the title. The balanced-cut application locator was corrected
to Section 6.2, with an explicit ledger amendment.

The combined census is 1,049 active cards: 444 individually completed/reviewed
and 605 pending. The 308 completed queue records include 17 inactive records;
all 291 active completed output hashes match. Publication and active formula
validation passed, covering 19,071 expressions. The preceding deployment was
live-verified as d356a5212abf2a26bb07, published 2026-09-15T17:45:37+00:00,
Pages commit 5385824f26eb549fdea09022796220319d3c59a7.

Checkpoint 312 completes TCS-6575, the universal deterministic k-server ratio.
The numerical function target and absolute 1/100 precision are preserved, with
all metric/strategy/additive-constant quantifiers, legal move recursion, finite
offline minimization, units and infimum nonattainment now explicit. The review
removes algorithm-selection and potential-proof instructions. Primary classical
models and bounds were checked, including visual inspection of the garbled-font
1995 manuscript. It distinguishes the 2025 maximum-movement time objective and
the 2026 randomized/advice-assisted computational results from the retained
sum-of-distances deterministic model. The restricted tree theorem is supported
by its primary abstract; its complete proof was not retrieved.

Including concurrent completion and archival of TCS-6016, the combined census
is 1,048 active cards: 447 individually completed/reviewed and 601 pending.
The 312 completed queue records include 18 inactive records; all 294 active
completed hashes match. Publication and active formula checks passed, covering
19,151 expressions. The preceding connectivity deployment was live-verified as
fb0a860b471119912bd2, published 2026-09-15T18:03:51+00:00, Pages commit
386ae6ab6784af601de81bab2333116c10973784.

Checkpoint 314 completes TCS-6568, the exact mean-payoff winner language.
It retains the zero-threshold liminf target and adds full binary encoding,
invalid-input behavior, history-dependent strategies, finite real liminf,
and both complete Lean decision-complexity directions. The individual review
checks positional certificates and primary pseudopolynomial bounds, preserves
published ergodic smoothed-analysis hypotheses and universal-graph restrictions,
and records the 2025 simplex correspondence's potentially exponential encoding
size. The new March 2026 recursive algorithm explicitly leaves its improved
runtime analysis open; it is now included with that limitation. The July 2026
source's reduction uses its stated succinct graph-class representation.

The combined census is 1,048 active cards: 449 individually completed/reviewed
and 599 pending. The 314 completed queue records include 18 inactive records;
all 296 active completed hashes match. Publication and active formula validation
passed, covering 19,245 expressions. A concurrent Pages push rejected one local
deployment attempt because another process advanced the branch; its resulting
same-version publication was live-verified as a12fecc42ce2986c04c3, published
2026-09-15T18:10:38+00:00. The rejected push did not alter or force the branch.

Checkpoint 331 includes the individual completion of TCS-0003, P versus BPP.
Its total-language target now has exact finite fair-coin semantics, a worst-case
polynomial clock on all random tapes, explicit uniform machine quantifiers,
and both complete Lean answer directions. The inspected 2019 book numbering
replaces the earlier edition reference. The May 2026 insensitivity theorem
retains its hardness and structural assumptions. Lin's current July revision
is recorded as a direct unverified separation claim, preserving uncertain
status. Oracle/promise results are distinguished from the retained target;
no construction walkthrough or weaker intermediate task is supplied.

The concurrent census is 1,044 active cards: 462 completed/reviewed and 582
pending. The queue has 331 completed records, 309 still active and 22 inactive;
all active completed hashes match. Publication and active formula validation
passed with 19,646 expressions. The preceding mean-payoff deployment was
live-verified as f2fd10d437d5a2c8a7f5, published 2026-09-15T18:17:33+00:00,
Pages commit bcd9c2ed28a23f1c5b396ced017685fccf8798ed.

Checkpoint 335 includes TCS-6510, truly subcubic APSP, completed on
16 September using primary-source checks conducted on 15 September. The review
retains arbitrary real edge weights and the randomized uniform real-RAM target,
fixes exact primitive operations and joint output probability, and distinguishes
worst-case time from expected time. It specifies graph corner cases, finite
shortest-distance semantics and both complete Lean answer directions. Source
scope now separates integer-range reductions from strongly polynomial ones,
node/few-weight algorithms, supplied prediction certificates and the August
barrier for reductions uniform over arbitrary triangle relations.

The concurrent census is 1,044 active cards: 466 completed/reviewed and
578 pending. The queue has 335 completed records, 313 still active and
22 inactive; all active completed hashes match. Publication and active
formula validation passed, covering 19,867 expressions. The preceding BPP
publication was live-verified as 92a5b7fbb208a199edc6, published
2026-09-15T18:28:51+00:00, Pages commit ff245fa7b4f3c51a20ae724a50912271efcd1e3b.

Checkpoint 347 includes individual completions of TCS-0036 and TCS-0037.
Both quantum comparisons now specify finite H/T/CNOT gate matrices, exact
measurement probabilities, uniform classical circuit generation, polynomial
register/gate bounds and the full Lean answer directions. The NP card additionally
has a classical certificate model and an explicit total 3-SAT encoding. Their
source reviews distinguish noncontainment from mere inequality, total languages
from promises, and unrestricted computation from oracle and sampling models.
The September 2026 promise/oracle result is included in BPP versus BQP; the NP
card checks the June Pauli-coefficient reduction and the separate nonlinear
coprocessor proposal. Old solver walkthroughs are removed. Both book conjecture
numbers now match the inspected August 2019 edition.

The concurrent census is 1,044 active cards: 478 completed/reviewed and
566 pending. The queue has 347 completed records, 325 still active and
22 inactive; all active completed hashes match. Publication and formula
validation passed, covering 20,304 expressions. The prior APSP publication was
live-verified as a071023def5d48a2da62, published 2026-09-16T01:36:55+00:00,
Pages commit cee6cabfb9167624717d374aac628ebfad9d58d0.

Checkpoint 356 includes TCS-0008, strongly polynomial linear programming.
The review fixes the retained rational arithmetic model, numerical-size convention,
universal complexity constants and exact three-way output semantics. It separates
special matrix classes and path-following bounds from unrestricted LP, and records
the scope of the STOC 2026 trust-region results. Awoniyi's same-author Validation
paper is distinguished from independent confirmation; Truffet's August revision
and its correction notice are added as an unverified general solution claim.
The card remains uncertain; no full claimed proof was certified.

The concurrent census is 1,043 active cards: 485 completed/reviewed and 558
pending. The queue has 915 records, 356 completed, with 333 completed still active
and 23 inactive; 152 active cards are outside the queue. All active completed
hashes match. Publication and formula validation passed for 20,570 expressions.
The preceding quantum publication was live-verified as 6b4bb67fa78fe57bf728,
published 2026-09-16T01:49:11+00:00, Pages commit
328bc269eff7f39adbb7b9d062b0399a917b67dc.

Checkpoint 364 includes TCS-6572, the polynomial-time simplex pivot question.
The review retains supplied-basis deterministic total bit time, defines legal
positive-reduced-cost ratio-test pivots including degeneracy, and makes terminal
basis certification and all charged helper/history computation explicit. It adds
the full Lean criterion, the current August ranking version and the distinction
between memory states, matrix-entry counts and binary input length. The April
shortest-monotone-path hardness result is scoped to shortest paths; neither it,
local antistalling, smoothed guarantees nor nonlinear active-set lower bounds
settles the retained unrestricted question.

The concurrent census is 1,042 active cards: 492 completed/reviewed and 550
pending. The queue has 364 completed records, 340 active and 24 inactive,
plus 152 active cards outside the queue; all active completed hashes match.
Publication passed at 1,043 active cards before another process retired a card;
the subsequent formula check passed on all 1,042 active cards and 20,838 formulas.
The preceding LP deployment was live-verified as e05b5289554899663ac6,
published 2026-09-16T02:00:12+00:00, Pages commit
701e93140ce3b0c64e8e40e910d46766ee45eb65.

Checkpoint 376 includes TCS-0673, previously a title-only first-order minimax
question. Its explicitly identified editorial variant now defines the original
asymmetric-neighborhood optimality notion, a uniform exact first-order oracle
program, common-null-set correctness of finite limits and mandatory local
attraction at strict local minimax points. The latter prevents a vacuous
never-convergent method. Sources distinguish true local optimality from necessary
derivative conditions, Hessian-assisted methods and restricted 2024/2026 results.
An inaccessible OpenReview submission is recorded only as a status-review limit;
its indexed claim is not treated as a verified theorem. The card remains uncertain.

The concurrent census is 1,040 active cards: 502 completed/reviewed and 538
pending. The queue has 376 completed records, 350 active and 26 inactive;
152 active cards are outside the queue. All active completed hashes match.
Publication and mathematical rendering checks passed, covering 21,189 formulas.
The preceding simplex publication was live-verified as 516e0db87c7ebe31aa41,
published 2026-09-16T02:04:57+00:00, Pages commit
5497f2232c95f272a797e9791188ec9f24da83b4.

Checkpoint 387 includes TCS-0026, L versus BPL. The review fixes the total-language
model, counts all visited work cells and auxiliary storage, and gives a finite
coin-count definition with an all-random-path polynomial clock. Complete Lean
acceptance now covers the class inclusion or its full separation negation.
The source audit corrects the book edition/conjecture locator, distinguishes
Hoza's space bound from polynomial time, and separates weighted generators and
short regular-program simulations from unrestricted derandomization. The May
ECCC revision is read from its revision-specific PDF; its root download still
serves the superseded April version. The July Cheng–Wu revision is included.

The concurrent census is 1,038 active cards: 511 completed/reviewed and 527
pending. The queue has 387 completed records, 359 active and 28 inactive, with
152 active cards outside it; all active completed hashes match. Publication and
formula checks passed on the preceding 1,039-card snapshot, covering 21,391
formulas. The preceding minimax deployment was live-verified as
602351f3bd82715f4013, published 2026-09-16T02:12:39+00:00, Pages commit
c008c9e8146ae86fef8498f8e02047ce406a646b.

Checkpoint 395 includes TCS-6600, optimal ordinary generators for ordered
read-once branching programs. The review specifies one uniform program,
seed-length and bit-output modes, binary parameter encodings, charged work
tapes and worst-case time, followed by a full Lean existence/negation criterion.
The current audit includes the September RANDOM proceedings and the newly
published width-three hitting-set preprint. Weighted outputs, hitting guarantees,
permutation transitions and time-only explicitness remain separate from the
retained target. Construction and seed-enumeration walkthroughs were removed.

The concurrent census is 1,038 active cards: 519 completed/reviewed and 519
pending. The queue has 395 completed records, 367 active and 28 inactive, plus
152 active cards outside it; all active completed hashes match. Publication and
formula checks passed on 1,038 cards, covering 21,736 formulas. The preceding
L-versus-BPL snapshot was pushed to Pages as a1d74ac606733a9830a1, commit
a84e51134f7ead084e032335de45843269ca416a; the deployment command succeeded.

Checkpoint 401 includes TCS-0012 and TCS-0022, the P-versus-NP implications to
average-case NP hardness and one-way functions. Both retain their distinct
uniform models and receive full Lean implication/negation criteria. The first
specifies strict exact sampling, off-support correctness and a single decider’s
positive-moment bound. The second fixes public forward evaluation, all-path
inverter time, same-length preimages and the arbitrarily-large-length quantifier
in failure of eventual security. The book references now match the inspected
2019 edition. Source checks distinguish the January randomized-description
characterizations, their specific premises and source-specific AvgP notation,
and the April conditional-generator results. Old solver walkthroughs are removed.

The concurrent census is 1,037 active cards: 524 completed/reviewed and 513
pending. The queue has 401 completed records, 372 active and 29 inactive, with
152 active cards outside it; all active completed hashes match. Publication and
formula checks passed on 1,037 active cards, covering 22,013 formulas. The prior
ordinary-PRG snapshot was live-verified as b8d03e8a8af45e6bbc20, published
2026-09-16T02:28:21+00:00, Pages commit
7b083ccda5c699d30ff767272ee31e926b8a4843.

Checkpoint 410 includes TCS-5358, distribution-free PAC learning of DNF.
The review fixes one uniform polynomial clock, integer accuracy/confidence
inputs, charged independent-example access, arbitrary distributions and fully
written Boolean-circuit hypotheses. The former generic explicitness sentence
contradicted circuit output and is removed. Complete Lean acceptance now covers
improper learning and its full negation. Source checks retain the assumptions
of the 2016/2021 improper lower bounds and distinguish the current exact-query,
relative-error testing and uniform-training PQ results. The 2026 query-learning
talk is matched to its 2025 paper rather than recorded as a new theorem.

The concurrent census is 1,036 active cards: 532 completed/reviewed and 504
pending. The queue has 410 completed records, 380 active and 30 inactive, plus
152 active cards outside it; all active completed hashes match. Publication and
formula checks passed on 1,036 active cards, covering 22,335 formulas. The prior
average-case/OWF deployment was live-verified as c2665f8788b3706648c1, published
2026-09-16T02:37:24+00:00, Pages commit
317209ab28143dcb9ee06040fb15601b4168152f.

Checkpoint 416 includes TCS-6574, exact semidefinite feasibility. The review
specifies the dense rational encoding, total decision language, real variable
domain, zero-variable endpoint and universal deterministic bit-time bound.
Complete Lean acceptance remains decision-only and covers singular feasible
matrices, irrational-only parameters, weak infeasibility and unbounded regions.
The source audit preserves the distinction between exact dual systems and short
binary certificates, the geometric assumptions of approximation algorithms and
the arithmetic/genericity qualifications of symbolic algorithms. The September
Newton-method preprint explicitly retains the open exact-SDP question and its
separate derivative-oracle/real-number model. Solver walkthroughs were removed.

Publication and formula checks passed on 1,036 active cards, covering 22,571
formulas. The completion checkpoint has 416 finished queue records, including
386 still-active cards, plus 152 active cards outside the queue: 538 reviewed
and 498 pending at that completion. The prior DNF snapshot was live-verified as
119e25635e8119e36b9c, published 2026-09-16T02:42:21+00:00, Pages commit
b07615d7bdf8bb0386e45832d87d7d1564ece453.

Checkpoint 447 completes TCS-6585 (general sparse linear systems),
TCS-7316 (matroid secretary) and TCS-5779 (correlated contention resolution).
The sparse-system card fixes every word-RAM, input, precision, clock and output
convention and the full Lean quantifiers. The two online-selection cards now
have complete models, expected/per-element guarantees and known-prior scope.

The user-requested recent-arXiv intake additionally refreshes TCS-6575
(deterministic k-server), TCS-4737 (Clifford+T QMA perfect completeness) and
TCS-6450 (classical/quantum communication). Matching new proof claims change
these and the two secretary-related cards to uncertain, with theorem/model
matches and explicit independent-verification limits. The new communication
source corrects an earlier bounded search that missed the August exponential
claim. See recent-arxiv-20260916.md for coverage, dated sources and boundaries.
No existing archived bodies were reviewed.

The concurrent census is 1,035 active cards: 568 reviewed and
467 pending. The queue has 447 completed records,
416 active and 31 inactive, plus 152 active cards outside
it; all active completed hashes match. Publication and formula checks passed
on 1,035 active cards, covering 23,676 formulas. The previous SDP deployment
succeeded as de24eb0164ebb15ca134, Pages commit
6b64228839bcf02a45fe76aa3aa836cd784c6559.

Checkpoint 465 completes TCS-4952 (total-function quantum/classical communication gaps) and TCS-7317 (randomized k-server asymptotics). The former now specifies a total Boolean family, all communication conventions and a polylogarithmic-versus-polynomial separation; the matching August/September claims are recorded as uncertain. The latter retains its explicit constant-factor target, all finite metrics and an oblivious adversary; the deterministic factor-k claim does not close its asymptotic gap. TCS-1649 additionally records the extended September BVASS paper, whose conclusion retains the general reachability question and whose structural VASS representation is not a uniform effective reduction.

The concurrent census is 1,032 active cards: 583 reviewed and 449 pending. The queue has 465 completed records, 431 active and 34 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,032 active cards, covering 24,271 formulas. An earlier unlocked formula run encountered a concurrent retirement; the locked run removes that race. The first recent-arXiv batch was live-verified as 2039431149cf24f51e2b, Pages commit 517d2147ad8c178d64822f4235484193505f6191.

Checkpoint 474. Completed TCS-6863 with a fully specified classical polynomial-time polynomial-factor search-SVP target for power-of-two cyclotomic ideals, explicitly authorized as a specialization of the historical broad direction. The card fixes dense signed-integer encodings, all-path bit-time, per-input probability, universal exponents, full vector output and norm conventions. Checked conditional quantum results, restricted easy ideal classes, the January 2026 refinement, and the two September hardness claims in different rings. These distinctions preserve source_open for the selected target. The preceding deployment was live-verified as f5c83c2281471154d12d, Pages commit d3fe8fc741e4587be87b436b55fe9d38fe17f75f.

The concurrent census is 1,032 active cards: 592 reviewed and 440 pending. The queue has 474 completed records, 440 active and 34 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,032 active cards, covering 24,510 formulas.

Checkpoint 478. Completed TCS-0661 with explicit fixed-rank cyclotomic modules, canonical Euclidean norm, dense generator encoding, integer squared thresholds and deterministic many-one hardness. The September 1 rank-two claim matches the existential-rank target and is recorded as uncertain pending independent proof verification. Related unique-SVP and conditional average-SIVP results retain their promises and limitations.

The concurrent census is 1,032 active cards: 596 reviewed and 436 pending. The queue has 478 completed records, 444 active and 34 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,032 active cards, covering 24,707 formulas.

Checkpoint 484. Completed the deterministic constant-factor Densest k-Subgraph formulation, exact output and bit model, with dated approximation and hardness boundaries.

The concurrent census is 1,032 active cards: 602 reviewed and 430 pending. The queue has 484 completed records, 450 active and 34 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,032 active cards, covering 24,982 formulas.

Checkpoint 486. Completed the single-prover classical verification question with uniform resource bounds, unbounded-strategy soundness and 2026 model distinctions.

The concurrent census is 1,032 active cards: 604 reviewed and 428 pending. The queue has 486 completed records, 452 active and 34 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,032 active cards, covering 25,051 formulas.

Checkpoint 490. Completed the fixed polynomial-hard LWE-to-iO implication, precise security quantifiers, and strengthened-assumption versus heuristic boundaries through September 2026.

The concurrent census is 1,032 active cards: 608 reviewed and 424 pending. The queue has 490 completed records, 456 active and 34 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,032 active cards, covering 25,153 formulas.

Checkpoint 496. Completed arbitrary IND-CPA encryption to semi-honest OT with explicit simulation quantifiers, uniformity qualifications and 2026 source boundaries.

The concurrent census is 1,032 active cards: 614 reviewed and 418 pending. The queue has 496 completed records, 462 active and 34 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,032 active cards, covering 25,467 formulas.

Checkpoint 503. Completed individual binary Gilbert–Varshamov rate review and checked recent coding results.

The concurrent census is 1,031 active cards: 620 reviewed and 411 pending. The queue has 503 completed records, 468 active and 35 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,031 active cards, covering 25,686 formulas.

Checkpoint 507. Completed exact Caccetta–Häggkvist formulation and primary-source status review.

The concurrent census is 1,031 active cards: 624 reviewed and 407 pending. The queue has 507 completed records, 472 active and 35 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,031 active cards, covering 25,791 formulas.

Checkpoint 512. Completed exact weighted TSP model and 2026 algorithm-status review.

The concurrent census is 1,031 active cards: 629 reviewed and 402 pending. The queue has 512 completed records, 477 active and 35 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,031 active cards, covering 25,960 formulas.

Checkpoint 513. Completed Asser spectrum-complement review with exact fragment and complexity boundaries.

The concurrent census is 1,031 active cards: 630 reviewed and 401 pending. The queue has 513 completed records, 478 active and 35 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,031 active cards, covering 25,980 formulas.

Checkpoint 519. Individually completed TCS-6685: exact user-approved BB(6) witness, full transition semantics, verified final-step convention, 2026 BB5 proof scope and dated September holdouts.

The concurrent census is 1,031 active cards: 636 reviewed and 395 pending. The queue has 519 completed records, 484 active and 35 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,031 active cards, covering 26,161 formulas.

Checkpoint 523. Individually completed TCS-6683: optimal excluded-grid asymptotics, exact threshold convention, full Lean acceptance and scope checks of 2026 structural advances.

The concurrent census is 1,031 active cards: 640 reviewed and 391 pending. The queue has 523 completed records, 488 active and 35 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,031 active cards, covering 26,296 formulas.

Checkpoint 528. Individually completed TCS-6678: effective monadic dependence, fully encoded deterministic model checking, class-wise quantifiers and July 2026 theorem scopes.

The concurrent census is 1,031 active cards: 645 reviewed and 386 pending. The queue has 528 completed records, 493 active and 35 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,031 active cards, covering 26,485 formulas.

Checkpoint 530. Individually completed TCS-6676: infimum approximation ratio, binary scheduling model, unattained optima and unconditional 1/100 acceptance versus conditional hardness.

The concurrent census is 1,031 active cards: 647 reviewed and 384 pending. The queue has 530 completed records, 495 active and 35 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,031 active cards, covering 26,583 formulas.

Checkpoint 536. Completed unrestricted truthful-in-expectation scheduling review and checked September universal-truthfulness preprint.

The concurrent census is 1,029 active cards: 651 reviewed and 378 pending. The queue has 536 completed records, 499 active and 37 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,029 active cards, covering 26,742 formulas.

Checkpoint 539. Completed Gyárfás–Sumner formulation and current primary-source pass.

The concurrent census is 1,029 active cards: 654 reviewed and 375 pending. The queue has 539 completed records, 502 active and 37 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,029 active cards, covering 26,874 formulas.

Checkpoint 539. Completed Gyárfás–Sumner review with individually linked source scopes.

The concurrent census is 1,029 active cards: 654 reviewed and 375 pending. The queue has 539 completed records, 502 active and 37 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,029 active cards, covering 26,874 formulas.

Checkpoint 541. Completed Kolmogorov–Loveland randomness definitions and primary-source status review.

The concurrent census is 1,029 active cards: 656 reviewed and 373 pending. The queue has 541 completed records, 504 active and 37 inactive, plus 152 active cards outside it; all active completed hashes match. Publication and formula checks passed under the shared lock on 1,029 active cards, covering 26,946 formulas.
