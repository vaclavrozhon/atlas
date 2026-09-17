# TCS-0734: chosen scope and the 17 September 2026 result

The user selected the first question in §5.4 of Dagstuhl Report 23291:
Gap-ETH-based FPT inapproximability of ordinary Set Cover within
`c * (log n)^0.99`, where `n` is the number of universe elements. The other
questions about disjoint-cover completeness and Densest k-Subgraph are excluded.

During the final status check, ECCC published Guruswami–Ren,
*Almost Optimal FPT Inapproximability for k-SetCover*, TR26-186, revision 1,
on 17 September 2026. The full revision was downloaded and its Introduction,
Definitions 2.1–2.4, Lemmas 2.5–2.6 and the reduction in §3 were read.
The primary revision is
<https://eccc.weizmann.ac.il/report/2026/186/revision/1/>.

The paper's parameter `n` counts candidate sets. Its announced approximation
factor must not simply be copied with `n` relabeled as universe size. Also,
the displayed construction has completeness `m` and soundness `h`: its direct
ratio is `h/m`. The card's conclusion uses that explicit gap, not an assumption
that the soundness threshold itself is already an approximation ratio.

Here is the scope check for the weaker exponent 0.99 selected by the user.
The Introduction gives a reduction from k-Clique, with completeness
`m = binom(k,2)`, `N` candidate sets (one for each source edge), soundness
`h = floor(log N / log log N)`, and polynomial construction size when N is
large enough that `h >= m`. Delete isolated source vertices first. For k at
least three, trivial tiny instances can be handled directly. Then the number
of source vertices is at most `2N`, and the stated enumeration and hash-family
bounds give at most `N^D` universe elements and polynomial total encoding
length, for some fixed constant D, once `N` is large enough.

For every fixed k and positive constant c,

```
h / (m * (log(N^D + 2))^0.99) -> infinity as N -> infinity.
```

The threshold at which this holds is bounded by a computable function of k
for a chosen rational c. Source instances below that threshold can be solved
by brute force with a cost depending only on k. Larger instances have
`h >= m * max(1, c*(log(n+2))^0.99)`, where n is the actual universe size.
Thus an FPT algorithm for the card's gap would yield an FPT algorithm for
k-Clique. The same explicit construction is described through 2-CSP in §3;
the ETH hardness premise is recorded in Lemma 2.5. ETH excludes this FPT
consequence, and the card's sparse deterministic Gap-ETH implies the relevant
deterministic ETH hardness. The selected 0.99 target therefore follows under
the stated assumption.

This records a checked parameter consequence of a newly posted primary
preprint, not an independent formal verification of every supporting theorem.
It does not certify the exact near-logarithmic headline ratio, the sharp
running-time lower bound, the disjoint-cover variant, or a Lean formalization.
The historical card can be archived for its selected conditional target while
retaining these precise provenance limits and its original answer criterion.
