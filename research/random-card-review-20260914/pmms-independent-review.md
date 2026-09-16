# Independent bounded review of TCS-1119

Date: 16 September 2026. Reviewer: /root/pv_sources. No canonical card, queue, selection or publication files were changed.

**Recommendation:** archive the original universal-existence question as resolved negatively, with the complete historical card preserved. This recommendation is supported by checking the stated counterexample and proof, not merely the preprint's abstract. Identify the result as Gölz's 8 September 2026 preprint; do not describe it as peer-reviewed or Lean-verified.

## Scope match

The saved original is *Fair Division of Indivisible Goods: A Survey*, arXiv:2202.07551v2, 4 March 2022. Section 1.1, printed/PDF p. 2, explicitly adopts nonnegative additive valuations unless stated otherwise and defines allocations as disjoint bundles whose union is the whole item set. Section 5, pp. 7–8, defines ordinary pairwise maximin share by repartitioning the actual union of two agents' allocated bundles. Open Problem 8 on p. 8 asks universal existence. It is not an epistemic-PMMS question.

Gölz, *PMMS Allocations Need Not Exist for 3 Agents with Additive Valuations*, arXiv:2609.08954v1, submitted 8 September 2026, Section 1 and Definition 1 on p. 1, uses exactly that complete-allocation and additive-goods model. The counterexample has three agents, nine goods and strictly positive integers. Thus it belongs even to the positive rational subclass of the original nonnegative-real domain. There is no valuation, completeness, agent-count or exactness gap.

## Proof inspection

Read the integer table and Theorem 1 on p. 2, the two partition tables and elimination argument on p. 3, and both lemmas covering the cases where agent 2 does or does not receive item c on pp. 4–7.

The necessary EFX condition is legitimate here because every singleton value is strictly positive: if removing a good from another bundle still leaves more than the agent's own value, the alternative partition obtained by transferring that good has both sides strictly above the current value. The swap argument also has the correct strict inequalities: a gain strictly between zero and the envy gap makes both new bundles strictly better.

Checked the preliminary one-large-good and nonempty-small-bundle arguments, Lemma 1's exhaustive allocations of the four b-items, and Lemma 2's exclusions of the other large goods for agent 2. In Lemma 2 the weighted upper bound is 134; item weights for b1,b2,b3,b4,d are 57,51,62,86,6. The listed forbidden subsets exclude precisely the remaining cases beyond the final case distinction. Checked the numerical lower/upper bounds and the strict gains in the subsequent branches. No logical error or missing case was identified in this bounded proof reading.

The final makeweight argument is valid: each agent has exactly two tied favorite bundles in each base partition P or Q, each base bundle is a favorite of two agents, and the relevant favorite union splits into values t-1 and t+1. Since every agent values d at 2, adding d to the lower-valued side gives t+1 on both sides, violating exact PMMS for the corresponding nonrecipient.

## Independent finite checks

Ran a separate set-based Python computation with direct integer summation, independent of the parent's bitmask/maximin implementation. It verified:

- Both P/Q bundle-value tables.
- All six explicitly supplied favorite-union splits, their disjointness, their unions, and their t-1/t+1 values.
- The per-agent small-item totals 132,62,114 and the weights/total above.
- All 3^9 = 19,683 complete assignments of goods to agents.
- Exactly 78 assignments satisfy EFX.
- Exactly four satisfy EFX and have no single-item exchange whose utility gain is strictly between zero and the relevant envy gap.
- Every one of those four assignments extends P or Q, and the paper's explicit favorite-union split plus makeweight violates PMMS.

The four surviving assignments in good order (a1,a2,a3,b1,b2,b3,b4,c,d), using agent indices 0,1,2, were:

    (0,1,2,0,2,0,2,1,1)
    (0,1,2,0,2,0,2,1,2)
    (1,0,2,0,1,1,0,2,0)
    (1,0,2,0,1,1,0,2,1)

This check corroborates the proof's structural reduction without merely repeating the parent's all-pair-splits maximin computation. It is not a formal proof certificate or Lean formalization.

## Exact files inspected

- research/random-card-review-20260914/sources/pmms-golz2026.pdf, 13 pages, SHA-256 2b2c3c571104c94a7aa39ba8249e1185712284585ad10d49a32e5e1cec32508b
- research/random-card-review-20260914/sources/pmms-survey2022.pdf, SHA-256 c9c1905f8c3f2db85e32662e061385a1118a7a5e170bb79b7f1728fc113215c2
- https://arxiv.org/abs/2609.08954v1 metadata: submission 8 September 2026, matching the cached source.

The separate approximation counterexample and claimed 78/79 bound on p. 8 are outside this independent audit and are unnecessary for resolving the exact existence question. The epistemic-PMMS and EFX existence questions must not be archived as consequences of this result.
