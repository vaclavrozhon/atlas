# Graph sampling, inference and colouring checkpoint

16 September 2026. Work continues on the remaining queue; this is not a completion report for the whole atlas.

- **TCS-6621**: retained the degree-uniform heat-bath Glauber mixing question at `q ≥ Δ+2`, with precise state space, vertex-update clock, worst starting state and exact quantifier negation. Read the 2020 source, ICALP 2026 context, 2024 flip comparison, and both August 2026 girth papers. Their update conventions, slack and degree restrictions remain explicit. Score 95 preserved.
- **TCS-6684**: retained the fixed-parameter assortative stochastic-block-model question. Repaired the threshold and overlap formulas, defined uniform worst-case bit complexity and all randomness, and separated expected recovery from high-probability recovery. Conditional matrix-recovery bounds and growing-community algorithms do not settle this target. Score 96 preserved.
- **TCS-3984**: completed the source's super-log-logarithmic palette-hardness question for exactly two-colourable three-uniform hypergraphs. Defined one quasipolynomial reduction, output vertex count, exact completeness and soundness, and the growth quantifiers. Polynomial reductions remain admissible as the stronger alternative explicitly offered by the source. Individual score 87.
- **TCS-7237** and **TCS-6637**: amended already-completed colouring cards after reading the 14 September perfect-completeness preprint. TCS-7237 now records a matching positive theorem claim and is uncertain pending full proof review. TCS-6637 records the claimed fixed-palette hardness without presenting it as an unconditional exclusion of randomized algorithms. The new preprint does not itself state the growing-palette result required by TCS-3984.

The parent took over the three unfinished graph claims after the helper agents hit their service usage limits. All three claims have now been completed and released through the shared queue infrastructure. Two independent external review workers continue; no other worker's active claim was modified.

## Verification

- Canonical schema validation and local publication passed for each new completion.
- Queue output hashes match all five active canonical cards; none retain an active claim. See `graphs-hashes.json`.
- All 25,319 mathematical expressions across 1,032 active cards parsed with the bundled renderer at this checkpoint; see `graphs-math.json`.
- Twenty browser cases passed: five cards, compact/full layouts, desktop/mobile widths. Published fields match canonical data; expanded mathematics and linked source captions render; no horizontal overflow, browser errors or HTTP errors occurred. The browser used a locked local publication snapshot and mocked community-service reads. See `graphs-browser-audit.json`.
- Targeted whitespace checks passed. Cached primary-source hashes and checked passages are in `graphs-sources.json`. The low-degree-code hypergraph comparison additionally uses the primary arXiv abstract and publication metadata at `https://arxiv.org/abs/1311.7407`.
- No external deployment, commit or push was performed. No pre-existing archived card body was read. External theorem statements were checked to the documented scope; this was not an independent audit or Lean formalization of their complete proofs.

Queue snapshot when this report was recorded: 493 completed, 421 pending, one outside active scope, out of 915 initial queue records. Separately, 152 active cards lie outside that initial queue and still require the overall quality pass.
