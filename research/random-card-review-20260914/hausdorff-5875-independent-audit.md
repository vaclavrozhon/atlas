# TCS-5875: source recovery and resolution audit

Review cutoff: 16 September 2026. Inert report for parent review; no canonical or queue changes.

## Source target

ISAAC2020 article13, actual PDF2, uses an informal polynomial-time-computation sentence and cites reference13. PDF16 identifies Dobbins–Kleist–Miltzow–Rzążewski, WG2018. The preconference full author version arXiv1712.05142v1 (14 December2017), actual PDF24 Section7.1, defines a decision input of two quantifier-free formulas and a rational threshold, then expressly asks forall-exists-R completeness. Updated v3 (11 November2021), PDF25 OpenProblem3, repeats it and notes that the sets may be open.

This justifies recovering the source's classification target; it does not justify asserting an unconditional P lower bound. The draft preserves the original quote by omission and makes the recovered target and conditional P consequence explicit. It does not replace the problem with translations, Gromov-Hausdorff distance, fixed-dimensional improvements, or a numerical output with an invented encoding.

## Primary classification

Jungeblut–Kleist–Miltzow, *The Complexity of the Hausdorff Distance*, DOI10.1007/s00454-023-00562-5, version of record27 September2023, DCG71(2024),177–213. Cached37-page publisher text:

- PDF2–3: Euclidean symmetric distance is the **maximum** of the two directed distances; finite integer-coefficient representations, ordinary bit model.
- PDF6: variable ambient dimension; natural threshold with explicit binary encoding and stated extension to reduced rational fractions; Theorem1.1 strict-universal-existential completeness.
- PDF12–13: expression-tree representation; arithmetic signature has no succinct exponent notation. Integer constants are binary-encodable and variables have finite indices.
- PDF23–25: complete main reduction, Theorem5.1. Read construction, parameter encoding and both truth directions. Auxiliary repeated-squaring coordinates represent the extremely large geometric scale; the algorithm does not write a doubly exponential integer coefficient.
- PDF25 expressly guarantees that **both output sets are nonempty**. In the YES case every source point has an appropriately close target point, with Euclidean norm at most square-root(m) and threshold m. In the NO case the enlarged counterexample ball gives a point whose every target distance exceeds m.
- PDF26/31: epsilon-based directed membership formulation. For the final full-class classification, elementary universal-existential membership suffices; no need to rely on the technically more complicated conversion to strict membership.

Schaefer–Štefankovič, *Beyond the Existential Theory of the Reals*, DOI10.1007/s00224-023-10151-x, online12 December2023; corrected author arXiv2210.00571v6 (3 March2025),51pages:

- PDF2–3 Remark1.1 explains corrections to **bounded-closed signatures**, especially higher levels. It retains the needed unrestricted-domain equality.
- PDF5 Theorem1.2 asserts equality of strict and unrestricted signatures for each level; the paragraph directly after it expressly concludes Hausdorff completeness for the full second level.
- PDF10–11 Proposition2.1 encodes arbitrary matrices using a quartic equation with the final existential block. The polynomial has polynomial description length, using sums of squares of small quadratic polynomials.
- PDF11–13 Theorem2.4 uses an effective real-coefficient Lojasiewicz bound to replace existential exact feasibility by arbitrarily accurate approximate feasibility with a simultaneous bound on witness escape. Read its compactification argument and limiting contradiction. Small typographical slips include “sufficiently large y_k” where the sequence tends to zero; the limit argument requires sufficiently small y_k. These slips do not reverse the displayed limiting inequality.
- PDF14 proof of Theorem1.2 fixes the outer real variables, applies Theorem2.4 uniformly in their values, and merges the newly introduced universal and existential variables into the existing final two blocks. The exponent depends on degree and variable count, not the particular real coefficients produced by fixing outer variables.

The external effective Lojasiewicz theorem is a cited mathematical dependency, not independently reproved or Lean-certified by this review. The main JKM preprocessing and effective real-algebraic bounds also remain source dependencies. This is a substantive statement/encoding/proof-chain audit, not full formal verification.

## Encoding detail and optional normal-form caution

Theorem1.2's displayed strict formula contains a potentially exponential power y^C; source syntax does not allow a binary exponent to count as a constant-size operation. The following direct polynomial-size strict formula fills this encoding detail without the stronger optional Proposition2.6:

Universally quantify one unrestricted real z, then existentially choose u_0>0 with (1+z^2)*u_0<1, variables u_1,...,u_m with 0<u_i<u_(i-1)^2, and x. Require |g(x)|<u_m and |u_0*x_j|<1 for every witness coordinate. Choose m so that 2^m>=C. The encoded conjunction has polynomial length since log C is polynomial in the source size. Absolute-value conditions are pairs of strict inequalities. Every atom is strict and every quantifier has unrestricted real domain; in particular, there is no non-strict guard hidden in a notation such as forall z>0.

If g has an exact root, then for every real z choose u_0 sufficiently small to meet the reciprocal bound and all coordinate bounds, then a positive decreasing chain; g(root)=0 is below u_m. Conversely, u_m<u_0^(2^m)<=u_0^C since u_0<1. For every positive tolerance r, choose real z so large that 1/(1+z^2)<r. The asserted witness then has 0<u_0<r and satisfies Theorem2.4’s approximation and escape conditions. Hence exact feasibility follows. Adding the new unrestricted universal z and existential variables preserves the forall-exists prefix. This supplies the reduction needed for full-class hardness, with no exponential formula expansion.

The optional single-degree-six normal form of Proposition2.6, PDF15 equation(6), is **not used as verified evidence**. Its printed formula uses a small initial y_0 but an increasing repeated-squaring chain and terms y_m^2*g(x)+sum x_j^2*y_m^2. This is not a faithful visible rendering of the immediately preceding small-power condition. The PDF was rendered and inspected, so the issue is not merely pdftotext. No conclusion about the stronger normal-form theorem is required for this card; the direct strict conjunction above avoids the problematic display.

## Domain and total-language details

The question concerns actual subsets of R^n given by quantifier-free formulas, not existentially projected input descriptions. Degrees, number of conditions, coefficient lengths and dimension are all variable and charged to input size. There is no closedness or boundedness promise. The original ISAAC paper's closed planar shapes belong to its own intermediate-shape results, not the general background question recovered from its citation.

The draft explicitly totalizes Hausdorff distance in extended nonnegative reals: sup(empty)=0 and inf(empty)=infinity. Thus both empty gives0; exactly one empty gives infinity. This is an editorial convention compatible with the following membership formula for t>=0:

For every epsilon>0 and points a,b, there are points a',b' such that

1. if a is in A, then b' is in B and ||a-b'||^2<t^2+epsilon;
2. if b is in B, then a' is in A and ||b-a'||^2<t^2+epsilon.

These are **separate implications**, never the joint antecedent “a in A and b in B”; that joint antecedent would incorrectly accept exactly one empty set. The predicate remains a polynomial-size forall-exists formula, including the arbitrary-set closure limit. All finite thresholds fail for infinite distance. Negative rational thresholds are directly NO. No emptiness oracle is used. Hardness is unaffected because the principal JKM reduction already outputs nonempty sets.

The exact finite ASCII/tree grammar and unary dimension in the draft are disclosed editorial choices within polynomially interconvertible ordinary encodings. The original formula syntax already explicitly lists its variables and operations; relabeling used variables and removing unused dimensions is polynomial-time. Integer coefficients and rational thresholds are exact binary values, not unit-cost arbitrary reals. Complete expression occurrences are charged; no exponent abbreviation is counted as a succinct circuit. Malformed binary strings are outside each language, and reductions are total finite deterministic machines with bit runtime and output cost.

## Further cautions, not needed for disposition

The corrected Beyond manuscript's introduction PDF3 calls the symmetric distance the “minimum”; this is inconsistent with its own subsequent maximum formula and the exact JKM definition. The draft correctly uses maximum.

Beyond PDF41–43 proves the zero-threshold consequence via closure containment. Its auxiliary construction on PDF42 writes an Euclidean norm bound for witnesses from a cube without the usual dimension factor; the natural repair is a coordinatewise infinity-norm bound or a rescaled cube. This optional proof is not needed for the general-threshold classification and is not treated as independently verified here. The primary JKM reduction and unrestricted signature equality suffice. At threshold zero, **closed** sets have distance zero exactly when they are equal, so the unrestricted zero-threshold theorem must not be silently applied with both sets promised closed.

## Status and bounded later review

Read actual papers and current arXiv revision records: JKM latest authorv2 is25 August2022, superseded for this review by the27 September2023 journal; Beyond latestv6 is3 March2025. The current compendium arXiv2407.18006v1,25 July2024, PDF81 entryA43, records the full classification and distinguishes the separate translation question. A2026 publisher chapter exists (first online1 May2026), but the inspected cached compendium remains the2024 author version; do not claim to have read the2026 chapter's full text.

Bounded primary-source searches through16 September2026 found no withdrawal or contrary theorem about the unrestricted Hausdorff classification. They are not claimed exhaustive. Later point-set-under-translation and geometric-approximation results are different tasks and do not replace this target.

Recommended disposition: archive the historical **classification** as resolved, preserving all original content and explaining the source recovery. State that H lies in P iff P=forall-exists-R, and therefore no polynomial algorithm exists under the usual separation assumption; do not state unconditional nonexistence or solve P-versus-NP by implication. Parent handles disposition and all application steps.
