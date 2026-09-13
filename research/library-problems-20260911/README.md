# Individually reviewed additions from the expanded library

The library review produced five new completed cards. Read the [full source-question inventory](../../library/discovery-20260911/problem-extraction/questions.md) for historical and unchecked entries as well as the selected problems.

| ID | New target | Discovery source | Status evidence |
| --- | --- | --- | --- |
| TCS-7223 | Linear-size Boolean circuits for integer multiplication | Goldreich, Computational Complexity, Appendix B.2.1 | Viola’s 2026 author manuscript explicitly retains the question |
| TCS-7224 | Polynomial-time exact computation of addition-chain length | Erickson, Recursion lecture, p. 13 | Koziel et al. (2016) distinguish single-target complexity; a 2025 primary article retains it as unknown |
| TCS-7225 | PZK versus SZK | Goldreich, Foundations of Cryptography I, §4.3.1.5 | Bouland et al. (2020) give an oracle separation; Gur et al. (2024) retain ordinary class equality as open |
| TCS-7226 | Woodall dijoin-packing equality | Schrijver, Survey Question 34 | Cornuéjols–Liu–Ravi (2025) retain the conjecture and give a constant-factor packing algorithm |
| TCS-7227 | Packing property implies MFMC | Schrijver, Survey Question 68 | Abdi–Schwarcz v2 (July 2026) retain the general conjecture and report finite verification |

These are dated editorial literature checks through 11 September 2026, not independent formal verification of the cited proofs. Each card includes its full model, acceptance criterion, substantive explanation, references and individual importance rationale. Canonical content is English.

## Novelty and scope

The search covered all serialized fields of the then-current catalogue, including archived and excluded records, followed by manual comparison of the relevant matches. See [search matches](novelty-search.json) and [individual comparisons](novelty-audit.json). The catalogue changed concurrently during this work; the final comparison used those newer records too.

- Fourier-transform lower bounds were **not added**: TCS-7175 already covers the target. The book’s weaker superlinear milestone does not warrant another card.
- TCS-7174 asks for optimal multiplication time on a deterministic multitape Turing machine. TCS-7223 instead asks about nonuniform Boolean gate count. The archived multiplication-related passages concern reversible pebbling and a particular matrix-transposition reduction.
- Scholz–Brauer (TCS-7170) is a structural inequality for addition-chain lengths, not an algorithm for computing the exact length of an arbitrary binary input.
- Streaming zero knowledge (TCS-1929) has a different verifier model from the ordinary class equality in TCS-7225.
- No Woodall/dijoin-packing or Conforti–Cornuéjols/packing-property/Mengerian target was found. Both were selected for their direct packing–covering, integrality and algorithmic significance within optimization.

The source inventory deliberately retains solved historical questions and uncertain leads without importing them as open cards. Examples include Hirsch, matching extension complexity, finite-domain CSP dichotomy, deterministic polylogarithmic distributed symmetry breaking, and the classical-oracle QMA/QCMA separation. Schrijver’s official errata supplies several corrections, including the missing metric assumption in Survey Question 35.

## Files and validation

- Publication log: the five stable IDs and canonical keys.
- `author_cards.py`: authored card content; publishes each completed card through the standard locked publisher.
- Verification evidence: primary references and status statements from the completed cards.
- Validation: catalogue preservation, card/export checks and final check results.
- Browser checks: all five cards rendered with definitions and references, mobile layout, and no requests into the private library.
- `catalog-before.json.gz`: catalogue snapshot from the start of this review. Other sessions’ additions and edits are preserved and are not counted as this review’s work.

The personal library, raw text and source extraction stay outside `atlas/site`. Only normal card data and public bibliographic references are published to the reader. The Top 100 selection uses the existing editorial choices; new importance scores do not automatically promote these additions into it.
