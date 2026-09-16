TCS-4185 selected-scope audit — 16 September 2026

Ready inert artifact: /tmp/atlas-draft-4185.py.
Exports: fields, notes, sources, status_note, summary.
No canonical card, queue, claim, selection, comments or publication changed.

The parent reported the user's explicit selection of option A. The target is unconditional: for every sampler exponent c ≥ 2, there is a larger reference-description exponent d > c with a witness at infinitely many lengths. The card publicly calls this an editorial formulation because Question 3 does not supply those quantifiers or combine the time, length and likelihood scales through the same c.

Formulation review is revised; scientific status stays uncertain. Approval of scope is not evidence of mathematical openness. Individual importance is 76, replacing the unassessed 50; category and original source provenance are preserved.

Exact predicate:

- A simple sampler is a pair (p,m), m ≥ 1, with |p| + log₂ m < c log₂ n.
- Every one of its 2^m equally likely fair-bit strings must halt within n^c machine transitions and output an n-bit string.
- Sampling is exact, with no rejection/failure mass. Hypotheses range over rational distributions, with simplicity selecting dyadic realizable ones.
- Optimality is the source's strict μ(x) > n^(−c) 2^(−C_U^(n^d)(x)). Failure is therefore ≤, not <.
- Plain complexity is output-program complexity. Missing time-bounded descriptions have complexity +∞ and exponential zero.
- The full negation is ∃U ∃c ∀d>c ∃N ∀n≥N ∀x ∃μ simple-and-optimal. No uniform constructor for μ is demanded.

Machine audit:

The class uses finite deterministic one-tape transducers on p#y#r#, explicit binary output charged one bit per transition, and the source's constant-description-overhead/polynomial-resource universality property. All-machine quantification avoids an unchosen universal transition table. The full two-direction invariance argument is in sources: sampler simulation absorbs m < n^c and additive program constants by enlarging the sampler exponent; reference-description simulation is then absorbed by the freely dependent d. Fixed factors in 2^(−C) are absorbed by inverse-polynomial slack at sufficiently large lengths. This establishes equivalence across these universal machines without claiming exact equality of finite-time complexities.

Source checks:

- Actual CCC 2017 publisher PDF pp. 4–5, 7–8, 11, 14 reread. Article has 18 pages. Definitions 4 and 11 distinguish sampling simplicity and strict optimality. Question 3 on p. 11 leaves the asymptotic regime unspecified.
- Proposition 14's stated ε = 1 boundary is stronger than the ≥ probability bound in its proof. The audit relies only on ε < 1, which is enough for the time-budget warning, and never imports that unchecked strict boundary.
- ECCC preprint Question 3 is in §3, PDF p. 11; corrected the old draft's §4 locator.
- Official displayed slide 14, PDF pp. 52–53, asks under which assumptions such strings exist. No assumption was silently added to the selected unconditional target.
- CiE 2018 Definition 3, PDF p. 5, uses indexed families and prefix complexity; it does not fix this target.
- The 2024 infinite-sequence paper, PDF pp. 1 and 4, uses an explicitly uncomputable predictor. It is not a polynomial-time resolution.
- Bounded later primary search repeated through 16 September 2026; no verified resolution or later primary statement of this exact combination found.

The old upper-case pending branches are absent. The malformed provisional LaTeX was rewritten from source definitions, not patched mechanically. The final payload imports, is JSON serializable, has five English summary sentences, contains no corrupted control characters, and all 96 mathematical expressions render with the reader's bundled KaTeX using their actual inline/display mode. These checks validate the artifact, not a solution proof.
