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
  backups; completed content lives in `data/cards/`.

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
silently shrink the review scope. At the first authorized source push, this pass
has completed 46 of the 606 baseline cards; 560 remain in the review queue.
Independent concurrent card edits are not automatically credited as this pass’s
completed reviews.

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
