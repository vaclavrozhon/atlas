# Continued review: learning and quantum proofs — 16 September 2026

The full active-card review remains in progress. This is a bounded checkpoint, not completion of the user’s request. Shared reservations and checked-input hashes continued to protect concurrent work.

## Completed root reviews

- **TCS-5443:** proper density learning of arbitrary positive-definite Gaussian mixtures. Fixed-accuracy joint polynomial dependence on component count and dimension, explicit exact-real arithmetic operations, total variation, proper output and complete Lean acceptance. Preserved the absence of separation, weight and conditioning promises. Distinguished SQ lower bounds, conditional Learning with Errors hardness, fixed-component results and sampler outputs. Newly assessed importance: 84.
- **TCS-6448:** QMA versus QCMA. Retained score 95 and ordinary promise-class comparison; fully defined uniform circuits, states, gate set and witness soundness. Checked the April 2026 revision and distinguished standard classical-oracle access from quantum and classical-only oracle models.
- **TCS-2229:** QMA versus QMA(2). Defined product/separable soundness and arbitrary internal entanglement. Added the 2 September 2026 unitary-oracle separation while retaining the unresolved ordinary comparison. Newly assessed importance: 93.
- **TCS-4753:** QMA(2) versus NEXP. Preserved constant acceptance gap and original input scale; separated already characterized precise variants, nonnegative-amplitude models and oracle results. Newly assessed importance: 92.
- **TCS-6449:** quantum versus classical advice. Retained score 87 and total-language scope. Fixed length-only trusted advice, arbitrary preparation complexity, fresh copies, uniform computation and complete Lean quantifiers. Distinguished PP/poly simulation from BQP/poly and the successive oracle-access regimes.

## Pending mathematical choices

TCS-4376 has verified source-model reconstruction but remains pending. The user has been offered the source’s concrete planar local-neighborhood question as an explicitly documented change from the generic classification passage. Its evidence remains `source`, with `needs_specification` and no completion credit.

TCS-4737 remains pending and unchanged while the user selects an exact gate-set convention for perfect completeness. The checked MFCS 2026 source explicitly treats gate-set-indexed classes; approximation does not automatically preserve probability-one acceptance.

Other pending choices are tracked by delegated reviewers: word equations TCS-0163/0171, random-CSP model TCS-5406 and the object type theory for TCS-3655. A request for details or elapsed time is not recorded as authorization to select a target.

## Verification

`make check` passed on an immutable 1,044-card snapshot after correcting the pending graph card’s evidence marker. This covers catalogue rebuild, schema/ranking/taxonomy/activity/export checks and local deployment-fixture tests; the fixture’s Git pushes target temporary local repositories, not a public deployment.

A later full active math pass checked **1,041 cards / 20,990 expressions**. Browser validation checked the five completed cards in **20 cases** (compact/full, desktop/mobile), including canonical-to-published field parity, visible expanded content, rendered mathematics, linked source captions and absence of browser, HTTP or page-overflow errors. Root output hashes matched the completed queue records under lock; targeted whitespace checks passed.

No root commit, staging, push or external deployment was performed. All publication calls rebuild the local reader. Other processes continue editing the shared workspace.
