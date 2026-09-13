# Two candidates connecting descriptive combinatorics and locality

Reviewed on 13 September 2026 in response to the request for roughly two new
problems, with particular attention to Anton Bernshteyn's work. These are
research candidates; no canonical cards or selections were changed.

## Recommended questions

1. **Borel versus Baire solvability of LCLs on grids.** For a fixed integer
   \(d\geq 2\), is
   \(\mathtt{BOREL}(\mathbb Z^d)=\mathtt{BAIRE}(\mathbb Z^d)\)?
   The source is Question 6.3 in
   [Berlow–Bernshteyn–Lyons–Weilacher](https://arxiv.org/html/2501.17445v4#S6.SS2),
   repeated as the first question of Problem 7.2 in
   [Bernshteyn's ICM 2026 survey](https://epubs.siam.org/doi/10.1137/25M1807563).
   The unknown direction is BAIRE to BOREL.

2. **Factor-of-i.i.d. versus universal measurable solvability on grids.** For a
   fixed integer \(d\geq 2\), is
   \(\mathtt{FIID}(\mathbb Z^d)=\mathtt{MEASURE}(\mathbb Z^d)\)?
   This is Question 6.4 in the
   [same grid paper](https://arxiv.org/html/2501.17445v4#S6.SS2) and the grid part
   of Problem 7.1 in the
   [ICM survey](https://epubs.siam.org/doi/10.1137/25M1807563).
   The unknown direction is FIID to MEASURE.

### Model and quantifiers to preserve

Use the group-action LCL model: a finite window in \(\mathbb Z^d\), a finite
label alphabet, and allowed patterns on that window. A solution obeys the
patterns at every translated window. BOREL quantifies over every free Borel
action on a standard Borel space; BAIRE over every free Borel action on a
Polish space. They require Borel and Baire-measurable solutions respectively.
MEASURE quantifies over every free Borel action on a standard probability
space, without assuming that the action preserves the measure. FIID asks for
a measurable solution on the free part of the shift on
\([0,1]^{\mathbb Z^d}\), with product Lebesgue measure. FIID does not require a
finite coding radius. These conventions are Definitions 1.1, 1.3, 1.5, 1.9,
and 1.16 of the grid paper. Keep the dimension parameter; selecting only
\(d=2\) would be an editorial specialization.

## Why these fit the request

Editorial judgment: both ask for a structural boundary between entire classes
of local problems and would add a new topic to the atlas's distributed
category. The first concerns topological regularity; the second concerns the
scope of constructions from independent randomness.

The LOCAL connection is supplied by Bernshteyn's transfer theorems: sufficiently
fast deterministic algorithms yield Borel solutions, and sufficiently fast
randomized algorithms yield measurable and Baire-measurable solutions.
For group actions, continuous solvability has an exact characterization by
sublogarithmic deterministic LOCAL algorithms. This motivates studying the
larger descriptive classes, without identifying either proposed equality with
a finite-round LOCAL bound. See
[the 2022 survey, Sections 2.3–2.4](https://arxiv.org/html/2208.02903#S2.SS3)
and [the foundational paper, Section 2.B](https://arxiv.org/html/2004.04905v7#S2.SS2).

## Status and duplicate checks

Both questions are explicitly retained in the published ICM 2026 survey.
Targeted searches through the review date and the authors' current publication
lists did not locate a subsequent resolution. This is a literature check,
not an independent audit of all cited proofs.

Do not substitute the old FIID-versus-FFIID equality on grids: the grid paper
already separates those classes (Theorem 1.18; ICM Theorem 6.3). Likewise,
MEASURE-versus-BAIRE equality on grids is already refuted (Theorem 1.8).

Searches of canonical cards, deletion reasons, and the historical ID registry
found no matching candidate. Existing TCS-6554 concerns finite distributed
LLL round complexity, so it is not a duplicate of either question.

## Source record

The `sources/` directory contains retrieved arXiv HTML and extracted text:

- Grid paper: arXiv:2501.17445v4, 6 May 2025.
- Bernshteyn's Notices survey: arXiv:2208.02903v1, 4 August 2022.
- Foundational LOCAL/LLL paper: arXiv:2004.04905v7, 28 June 2023.
- Bernshteyn–Weilacher on finite asymptotic separation index:
  arXiv:2308.14941v2, 7 March 2025; consulted for alternatives.
- Bernshteyn–Yu on Borel LLL: arXiv:2412.11571v2, 27 May 2026;
  consulted for subsequent developments.

The ICM chapter, *Complexity of Local Problems*, DOI
10.1137/25M1807563, was read through the browser tool at the publisher. Direct
shell retrieval returned HTTP 403, so no local full-text copy is claimed.
