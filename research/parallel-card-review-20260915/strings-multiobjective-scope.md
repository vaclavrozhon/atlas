# TCS-4302: unresolved precision / synthesis scope

Update: the user selected exact threshold achievability on16September2026, and the strings worker completed TCS-4302. The unresolved-choice discussion below is historical; see the completed canonical card and boson-foundations-checkpoint.md.

Checked 16 September 2026 by `third-strings-862815`. Canonical card remains unchanged and its claim remains held pending the user's target choice.

## Checked source

Marta Kwiatkowska, *Model Checking and Strategy Synthesis for Stochastic Games: From Theory to Practice*, ICALP 2016, https://doi.org/10.4230/LIPIcs.ICALP.2016.4 .

- §2, Definitions 1 and 3: finite, turn-based, complete-observation stochastic games; randomized strategies with unrestricted countable memory, including stochastic memory updates.
- §3, Definitions 5 and 7: conjunctions of probability constraints with non-strict lower or upper thresholds; coalition semantics gives one controller strategy against all opposing strategies. The discussion later extends reachability path formulas to LTL.
- §4, pp. 6–7: verification decides whether a strategy exists, while synthesis constructs a strategy witness.
- §5, p. 9: optimal strategies need not exist; infinite memory can be needed. Existing algorithms therefore compute epsilon-approximations of Pareto sets and corresponding epsilon-optimal strategies.
- p. 10: stopping-game approximation extends from reachability to LTL through deterministic Rabin automata; the very next sentence states the general synthesis question.

The imported card has only the historical synthesis sentence and a generic `decision` tag. It does not select exact threshold achievability, approximate synthesis, or a representation for a potentially infinite-memory strategy. Silently replacing the synthesis question by a decision predicate would materially narrow the target.

## Concrete choices relayed to root

1. Exact rational-threshold achievability: decide whether an unrestricted randomized history strategy simultaneously guarantees all LTL probabilities against every adversary. This is a precise decision subproblem, but explicitly narrows synthesis.
2. Source-style epsilon Pareto approximation plus effective epsilon-strategy construction. The finite approximation and output strategy representation must be specified.
3. Pair exact achievability with actual synthesis in an explicit effective representation. This demands a computational representation of strategies rather than only their abstract mathematical existence.

The quantifier over abstract strategies can allow real-valued distributions and infinite history dependence. A required finite-state strategy or rational-only probabilities are extra restrictions, not harmless encoding conventions unless an equivalence theorem is proved.

## Later primary check

Graf, Lin and Majumdar, *Solving Qualitative Multi-Objective Stochastic Games*, AAMAS 2026, author version https://arxiv.org/abs/2602.12927v1 . Abstract and introduction: conjunctions of almost-sure/nonzero reachability and safety are PSPACE-complete; unrestricted Boolean qualitative combinations have a different determinacy/complexity behavior. Introduction still records undecided general randomized quantitative cases. This does not settle arbitrary rational probability thresholds for LTL, nor remove the choice between exact synthesis and approximation. Full PDF inspected and cached in the batch source snapshots.
