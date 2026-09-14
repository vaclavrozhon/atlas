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
part of this census. The expanded queue therefore has 614 entries: at this
checkpoint 150 completed, 463 pending and one out of active scope. The live counts
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
entrywise low-rank target under P different from NP). There are now 1,057 active
cards. Their model choices, resolution scope and full content are preserved. The
completion helper requires an explicit archival reason for an inactive outcome,
validates its content and immediately invokes the activity workflow.

TCS-6529 was also completed and archived after matching the planar Earth Mover
distortion target to the published STOC 2026 resolution. At this checkpoint
there are 594 detailed active cards and 463 pending active reviews in the queue.

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
