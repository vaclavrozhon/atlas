# Atlas manifest

Atlas benchmarks AI research on significant open problems in theoretical
computer science. Scientific importance and a clear mathematical target guide
selection.

Our primary goal is a benchmark of **500 problems**. The **Top 100** is a
priority subset of those same 500, with secondary editorial attention. Selection
and review should primarily develop the full Top 500. Both use the same category
order and ranking within each category. A 1,000-problem benchmark is no longer
an active goal.

Cards have exactly two editorial activity states: **active** and **inactive**.
Active cards live in `data/cards/`. Inactive cards retain their complete content
in `data/archive/cards/`, with stable IDs and reasons in `data/archive/index.json`.
Deactivation moves a card into the archive; it does not erase it.

All routine improvement, source checking, formulation review, ranking, selection,
validation and publication work targets **active cards only**. Inactive cards
are treated as absent from the working atlas: do not spend time reviewing,
repairing, updating or importing them. The archive is excluded from the reader,
exports and benchmark quotas. Consult or reactivate an archived card only when
the user explicitly asks; preserve its identity and record the new decision.
Activity is separate from the card's scientific status or evidence level.
This decision of **13 September 2026** supersedes the earlier policy of deleting
card contents and retaining only IDs and reasons.

We allow questions asking for **a number, a function or a curve**, as well as
yes/no questions. For example, “determine the matrix multiplication exponent
ω” is a valid target; it need not be restricted to “is ω = 2?”.

Accepted benchmark answers must be proved in **Lean**. By default, for numerical
targets, **including integers**, the required absolute accuracy is
**0.01 (exactly 1/100)**. Explicitly approved exact targets use their card's
answer criterion instead.
For a function or curve, including an integer-valued function, that bound must
hold at every point of the card's stated domain, in its stated units. The answer
may be a real approximation or a certified interval; it need not be an integer,
a decimal expansion or a simple exact expression for the target. Numerical
evidence alone is insufficient. Exact answers also qualify, and asymptotic bounds
use the precision specified by the card.

For **BB(6)**, the accepted answer is an explicit six-state machine, a proof that
it halts, and a proof that no halting machine in the same class runs longer.
Its runtime specifies BB(6) exactly. A simple closed form or decimal expansion
of that runtime is not required.

The numerical tolerance defines benchmark acceptance. It does not turn an
approximation into a proof of an associated exact conjecture. Definitions,
models and quantifiers remain precise even when the accepted answer has a
numerical tolerance. We do not require a closed form or a predetermined syntax
for a number or curve.

The detailed editorial, source and repository requirements are in
[RULES.md](RULES.md). This manifest records the user's decisions of
12–13 September 2026; it does not claim that the catalogue is already formalized.
