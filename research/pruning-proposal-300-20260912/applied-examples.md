# Applied examples — 12 September 2026

The user approved the five concrete examples discussed in the conversation,
covering six cards: three duplicate records were consolidated, and three other
records were removed. The remaining 294 recommendations in the original
300-card proposal have not been applied by this change.

TCS-5246 was consolidated into [TCS-7222](../../data/cards/TCS-7222.json).
TCS-5312 and TCS-5501 were consolidated into
[TCS-4786](../../data/cards/TCS-4786.json). All three source references and their
relevant context were transferred before removal. Incoming related-problem links
were redirected to retained targets or removed. Existing focus choices and
historical source-key mappings were preserved.

The primary project goal is now **500 problems**, with **Top 100** as a priority
subset receiving secondary editorial attention. The manifest, authoritative
rules, project documentation, reader wording and generated-report descriptions
were aligned. Existing category quotas and ranking behavior were preserved;
the existing Top 1000 view is labelled as legacy rather than an active goal.

Only IDs and removal reasons are recorded below and in
[applied-examples.json](applied-examples.json). No deleted card bodies are archived.

## TCS-0194

Removed on 2026-09-12 after the user approved the concrete examples from the 300-card proposal. Comparing the maximum-entropy method with the Copy lemma concerns the relative power of two proof frameworks. The entropy-cone and information-inequality validity targets themselves provide broader coverage. Editorial selection judgment for the primary 500-problem benchmark, not a claim of resolution.

## TCS-0423

Removed on 2026-09-12 after the user approved the concrete examples from the 300-card proposal. The concrete target is preventing sparse-matrix fill-in during a particular persistence basis-change procedure. The broad title overstates its scope; general multiparameter-persistence complexity is a stronger representative. Editorial selection judgment for the primary 500-problem benchmark, not a claim of resolution.

## TCS-5246

Removed on 2026-09-12 after the user approved the concrete examples from the 300-card proposal. The selected passage asks ordinary graph isomorphism in polynomial time, already represented by TCS-7222. Preserve its refinement-hierarchy reference in that card. The source reference and context were transferred before removal.

## TCS-5312

Removed on 2026-09-12 after the user approved the concrete examples from the 300-card proposal. The NP-hardness question for ordinary truth-table MCSP is already part of TCS-4786. Preserve this paper's total-versus-partial circuit-extension context in the retained card. The source reference and context were transferred before removal.

## TCS-5501

Removed on 2026-09-12 after the user approved the concrete examples from the 300-card proposal. This repeats the NP-hardness frontier for ordinary MCSP represented by TCS-4786. Transfer the sums-of-squares reference without confusing restricted-method lower bounds with NP-hardness. The source reference and context were transferred before removal.

## TCS-5706

Removed on 2026-09-12 after the user approved the concrete examples from the 300-card proposal. The unified locality bound is a distinct BST guarantee, but adds another specialist access-sequence criterion to an already well-represented adaptive-search cluster. Prioritize dynamic optimality and the canonical independent conjectures. Editorial selection judgment for the primary 500-problem benchmark, not a claim of resolution.

## Validation

`make publish`, `make check`, `node tests/pages.cjs` and `node tests/deletions.cjs` passed. The six records are absent from canonical data and the reader; transferred references remain on both retained cards, and incoming links contain no removed IDs. See [validation results](applied-examples-validation.json).
