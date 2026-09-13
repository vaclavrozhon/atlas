# Numerical and function questions — 12 September 2026

The latest user decision selects an **exact witness-based answer for BB(6)**:
an explicit six-state machine with Lean-checked halting and universal runtime
maximality proofs. Its runtime specifies the integer without a simple formula
or decimal expansion. This supersedes the numerical approximation criterion for
TCS-6685 only; see [bb6-exact-witness.json](bb6-exact-witness.json).

The user requested a catalogue wording review, explicitly preferring “determine
ω” to the binary test “ω=2”, and authorized reconsideration of the preceding
specification deletions. A subsequent instruction added numbers and curves to
the manifest and selected Lean acceptance at accuracy 0.01. The user subsequently
confirmed absolute error and explicitly extended it to integer targets:
1/100 for every numerical value, pointwise on a function's stated domain.
Approximations need not be integer-valued or give a simple exact expression for
the target. Asymptotic targets keep their stated matching-bound precision.

Changed 23 active cards: 16 binary questions became quantitative targets,
six existing real-value/curve cards received the acceptance precision, and the
Shannon capacity of C₇ draft received complete numerical definitions. Restored
six of the 95 cards removed in the preceding specification cleanup. The other
89 retain their model, source or substantive-target gaps. The three vacated
focus choices for planar k-sets, binary rate–distance and Gaussian interference
were reinstated with their former importance assessments.

The subsequent integer-precision correction updates TCS-6558, TCS-6685,
TCS-7201 and TCS-7204. It replaces the initial exact-output requirement with
certified real approximations or intervals at absolute error 1/100, while
preserving each model. See [integer-precision-correction.json](integer-precision-correction.json).
The original pass counts and validation snapshot below remain dated records;
the correction has its own validation result.

| Cards | New target |
| --- | --- |
| TCS-0007 | Determine the matrix multiplication exponent ω over C; the infimum need not be attained. |
| TCS-6589, TCS-6590 | Determine the symmetric and asymmetric subtour-LP integrality gaps. |
| TCS-6659, TCS-6638, TCS-6676, TCS-7322 | Determine optimal polynomial-time approximation ratios in the existing models. |
| TCS-7252 | Determine the universal triangle covering-to-packing ratio. |
| TCS-6575 | Determine the deterministic k-server competitive function. |
| TCS-7317, TCS-6623, TCS-7297 | Determine constant-factor asymptotics of randomized competitiveness, trace samples and edit-distance distortion. |
| TCS-7288, TCS-7290, TCS-6664 | Determine extremal functions for influence adaptivity, sunflower-free families and threshold-function influence. |
| TCS-6558 | Determine the maximum reset-threshold function for every state count, with absolute error 1/100 after the user's correction. |
| TCS-6519, TCS-6607, TCS-6665 | Keep the capacity curves and specify numerical acceptance. |
| TCS-6634, TCS-7197, TCS-7200 | Keep the voting/fairness optimization constants and specify numerical acceptance. |
| TCS-6610 | Complete the strong-power definition and normalization of Shannon capacity of C₇. |
| TCS-0318, TCS-1010 | Restore the planar k-set extremal function and binary rate–distance curve. |
| TCS-6606, TCS-7210, TCS-7211, TCS-7214 | Restore Gaussian interference, discrete interference, two-way capacity and distributed lossy rate–distortion as weighted functions. |

This is an editorial broadening, not an equivalence claim. A counterexample to
an old threshold need not determine the new value; conversely a 0.01-accurate
answer need not settle an exact conjecture. The source conjectures remain in
context, while formal statements, titles and answer criteria describe the new
targets. All approximation-ratio infima quantify over one globally uniform
algorithm per achieved factor, avoiding a meaningless per-input-size choice of
algorithm. Supremum and infimum targets do not silently require attainment.

Genuine existence, decidability and class-comparison questions remain binary,
including P versus NP, VP versus VNP, EFX existence and computability of Shannon
capacity. Constant-existence questions such as Fourier entropy–influence and
matroid secretary also remain meaningful qualitative barriers; this permission
does not require inventing an exact optimal constant for every inequality.
Drafts whose models are not yet recovered were not promoted through a wording
substitution. This was a catalogue inventory and quantitative-wording screen
with selected individual model reviews, not a new complete review of every
draft or every problem's current open status.

The restoration reverses the earlier requirement for a predetermined answer
grammar. The counted quantities and operational regions were meaningful; a
closed form need not be anticipated to admit the question. An answer still
has to determine values with the required precision, rather than copy the
defining extremum or provide an uncertified plot. Weighted capacity functions
use bits per joint channel use; Gaussian rates use a real channel use, and
distributed source-coding rates use a source pair. The latter's domain excludes
infeasible distortion targets and leaves distortion constraints exact.

Existing sources and evidence levels are preserved. Representative primary
definition checks include the [matrix multiplication paper](https://arxiv.org/abs/2404.16349v3),
the [synchronizing-automata survey](https://arxiv.org/abs/2608.24245),
the [k-set problem entry](https://topp.openproblem.net/p7), and
[network information theory notes, version 4](https://arxiv.org/abs/1001.3404v4),
Lectures 6, 13 and 18. The historical notes are used for definitions, not as a
current-status source. Restoring the Gaussian card preserves its uncertain
status and the qualifications around claimed capacity results.

No Lean formalization or mathematical solution was produced. In particular,
source evidence that an exact question is open does not establish that its
relaxed numerical target is open. Each affected real-value card records that
limitation separately from its precise acceptance criterion.

- [changes.json](changes.json): the 29 individual edits/restorations and reasons.
- [deleted-reconsideration.json](deleted-reconsideration.json): dispositions of all 95 preceding deletions, retaining IDs and reasons rather than card archives.
- [summary.json](summary.json): scope, counts, precision conventions and edit fingerprints.
- [validation.json](validation.json): publication and check results.

The [manifest](../../docs/MANIFEST.md), [rules](../../docs/RULES.md), publisher
and reader now support numerical values and curves explicitly. Canonical JSON
cards remain the only publication inputs.
