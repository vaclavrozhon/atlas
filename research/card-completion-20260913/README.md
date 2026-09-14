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
- [input-hashes.json](input-hashes.json) records the baseline of all canonical cards.
- [reviews.jsonl](reviews.jsonl) records substantive editorial decisions, source
  passages checked and the limits of each status check. It contains no full-card
  backups; completed active content lives in `data/cards/`, with subsequently
  deactivated records preserved in `data/archive/cards/`.

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
