# Independent audit of proposed TCS-7148

Checked 16 September 2026 against the full canonical card, docs/RULES.md, the inert parent draft and the listed primary sources. No canonical or queue changes.

## Verdict

I found no algebraic defect in the chosen two-phase formulation, no vacuity of its algorithm class, and no checked theorem resolving that exact existential expected-time assertion. The strongest caveat is source scope: this is a specific textbook initialization and machine model, not an equivalent operational restatement of all simplex algorithms or of the Spielman–Teng two-phase shadow method. Keep the explicit editorial-specialization disclosure and uncertain status. Applying it remains the parent's decision after the pending scope choice.

The quantifier order is correct:
one eligible program and fixed C,k, then all dimensions, normalized centers, objective vectors and noise scales. Its displayed negation correctly quantifies over every eligible algorithm and every proposed polynomial before choosing a bad instance distribution. A lower bound for Bland or for one shadow implementation does not prove that negation.

## Algebra and degeneracy

The split-variable conversion is valid for arbitrary real inequality LPs, including polyhedra with lines and without original vertices. E = D[A,-A,I] has full row rank because it contains D. The correspondence is x = x+ - x-, with slacks s = b - Ax.

The initial artificial basis is feasible because h = |b| is nonnegative. Phase I is always feasible and its objective -sum(z) is bounded above by zero. A terminal basis with positive artificial sum and nonpositive reduced costs certifies original infeasibility.

Positive reduced cost does not require a positive objective increment when the ratio-test step is zero. Explicitly permitting these degenerate pivots is necessary. The stated minimum-ratio exchange preserves feasibility and invertibility, including ties.

Stopping Phase I when every artificial variable is zero is legitimate even if the current tableau has some positive reduced costs: a feasible zero-artificial vector reaches the global upper bound zero on the Phase-I objective.

Cleanup is always possible under the supplied full-row-rank condition. If a zero-valued artificial basic column occupies position i, row i of H_B^{-1} E cannot vanish because E has row rank m. That row vanishes on every E-column already in B, so some nonbasic E-column has a nonzero entry there. Swapping it in is invertible; its new basic value is zero and all other basic values stay unchanged. This preserves feasibility and removes exactly one artificial column. No redundant-row deletion is required.

The usual all-nonpositive reduced-cost certificate is valid for the final standard form. If an improving entering column has no positive component in H_B^{-1} H_j, the resulting nonnegative kernel direction has positive objective. Its projection under x+ - x- is a genuine original improving ray, since a zero projection would have zero objective.

The eligible class is nonempty: a deterministic finite anti-cycling pivot rule, together with the specified cleanup, fits these rules and terminates in exact arithmetic. This observation certifies basic well-posedness only, not a polynomial bound.

## Editorial restrictions that matter

1. Fixed initialization: all instances are transformed by splitting free variables and adding slacks, then use m artificial variables and objective -sum(z). Forbidding every other auxiliary LP, extra inequality and objective change excludes published two-phase constructions. This is materially narrower than unrestricted existence of some simplex method.

2. Machine randomness: finite-time fair-bit programs with rational constants cannot directly produce independent continuously distributed real vectors exactly. Published randomized shadow constructions sample continuous coefficients or directions. A suitable discretization could conceivably preserve their guarantee, but it is not automatic and was not proved in this audit. Do not call the machine convention equivalent to their randomized real-arithmetic model.

3. Every-coin termination is stronger in wording than almost-sure termination. For finite-coin pivot algorithms this can often be enforced by a finite operation cap and a deterministic anti-cycling fallback from the current feasible basis, with an exponential deterministic fallback bound and controlled expectation. Thus it does not make the class empty or immediately false. It still must not be silently identified with a source's convention.

4. The computational objective is all charged operations, not only pivot count. This correctly rules out obtaining a free short path from an arbitrarily expensive pivot-selection oracle. Tape access and exact linear algebra are charged consistently. Input numbers are exact reals, not finite-precision Gaussian samples.

5. The target is exact optimization, with no promise of feasibility, boundedness or genericity. Zero-preserving noise can retain degeneracy with probability one, including zero right-hand sides. The definition correctly addresses this through feasible bases, degenerate pivots and cleanup.

6. Internal algorithmic randomness is independent of external Gaussian perturbations. The algorithm sees the perturbed data and sigma only. The displayed expectation uses the right order: centers are adversarially fixed before noise, and no choice depending on realized Gaussian values enters the outer quantifiers.

Minor wording clarification: write explicitly that eligibility covers every real A,b,c of the prescribed dimensions and every admissible 0 < sigma <= 1; otherwise “every finite real input” could accidentally include invalid sigma. The intended valid-input domain is clear from the preceding formula but should be unambiguous.

## Primary-source findings and precise locators

Roughgarden, Beyond Worst-Case Analysis, arXiv:1806.09817 (2018), cached sparse-simplex-roughgarden2018.pdf/txt:

- Section 5, p. 9 footnote 14 states the important sparsity-preserving extension.
- Page 10, Theorem 3 and the following paragraph identify existing positive results with shadow pivot rules.
- This short discussion does not choose the fixed artificial-variable two-phase class.
- https://arxiv.org/abs/1806.09817

Spielman–Teng, Smoothed Analysis of Algorithms: Why the Simplex Algorithm Usually Takes Polynomial Time:

- Newly cached sparse-simplex-spielman-teng-full.pdf/txt is the author-linked arXiv cs/0111050v7, dated 9 October 2003 in its version stamp. The rendered title page says 26 November 2024; this is not evidence of a new research revision.
- In this checked edition, zero-preserving and relative perturbations appear in Section 6.4, pp. 90–91. Section 6.3 is instead the degeneracy discussion. Do not transfer section numbers blindly to or from JACM.
- Section 3.3, pp. 32–35, constructs a relaxed-right-hand-side LP-prime and an interpolating LP-plus with a new variable and two extra constraints. Algorithm step 4 samples a continuous vector alpha uniformly from a constrained simplex. These operations do not match the draft's initialization and fair-bit machine literally.
- The author's landing page explicitly warns that arXiv and journal theorem/lemma numbering differs.
- https://www.cs.yale.edu/homes/spielman/simplex/index.html
- https://arxiv.org/abs/cs/0111050
- JACM DOI remains 10.1145/990308.990310. The final publisher PDF was not successfully retrieved by this audit; cite the actually checked arXiv locators when using this cache.

Bach–Black–Huiberts–Kafer, Beyond Smoothed Analysis: Analyzing the Simplex Method by the Book, arXiv:2510.21613v2, 26 June 2026:

- Cached sparse-simplex-btb2026.pdf/txt.
- Section 1.2, pp. 3–4, discusses Klee–Minty constructions whose long Bland paths survive zero-preserving noise. This is not a lower bound against every algorithm or every initialization in the card.
- Running-time overview pp. 11–12 retains a fixed matrix but uses right-hand-side perturbations, mean-width/scaling parameters and tolerance-related guarantees.
- Theorem 33, printed/PDF p. 43, concerns a shadow path from a random direction to c + epsilon theta, with bounds depending on M, N, eta and epsilon. It is not a dimension-and-sigma-only exact solver guarantee for the draft's Gaussian distribution.
- https://arxiv.org/abs/2510.21613v2

Bach–Huiberts, Optimal Smoothed Analysis of the Simplex Method, arXiv:2504.04197v2, 23 May 2026:

- Newly cached sparse-simplex-optimal2025.pdf/txt; despite the cache filename, the contents are v2 from 2026.
- Page 2 explicitly defines dense independent Gaussian perturbations of every entry of the joint (A,b) array, with normalized center rows and unperturbed objective.
- Its stronger pivot-count bound therefore does not resolve the zero-preserving question.
- https://arxiv.org/abs/2504.04197v2

The cached Dadush–Huiberts chapter's Goldfarb-shadow exercise can motivate a fixed-shadow obstruction. An exercise is not a checked proof of a universal lower bound for the selected algorithm class.

## Suggested scope sentence

“This card specializes the broader source direction to the fixed artificial-variable two-phase initialization defined below. That class does not encompass every published shadow-vertex initialization, and no equivalence to the unrestricted existence of a sparsity-smoothed polynomial simplex method is asserted.”

Keep any explanatory arguments about cleanup, anti-cycling and probability conversions in the audit, not in the public problem's answer criterion.
