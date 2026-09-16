# TCS-6734: scope clarification and adopted formulation

The initial source review below was recorded on 16 September 2026 while the card
was pending. The user subsequently explicitly selected the NP-complete branch.
The completed card now adopts deterministic compression with an unconditional
upper bound and the conditional kernel implication PK(Q) ⇒ NP ⊆ coNP/poly.
It documents this refinement and retains uncertain status for its precise scope.
The claim was completed using its shared token; the queue records completion.
The initial ambiguity audit is retained below as historical context.

The source's phrase “natural problems” has no formal definition. The review
cannot silently substitute all parameterized languages, require NP-completeness,
or strengthen a conditional kernel lower bound into an unconditional one.
The optional scope question was answered by the user: the NP-complete variant was selected.

## Recovered definitions

For a fixed parameterized language Q ⊆ {0,1}* × N, input (x,k) uses unary k.
A deterministic polynomial compression is one uniform polynomial-time map,
measured in |x|+k, into a fixed language R ⊆ {0,1}*, producing y of length
polynomial in k and preserving membership exactly. R is unrestricted; it need
not belong to NP or even be decidable in the source definition.

A polynomial kernel instead outputs (x',k') for the same Q, preserving membership,
with |x'|+k' bounded polynomially in k. Both polynomial exponents and constants
are fixed independently of input and parameter.

If unparameterized Q is NP-hard and R belongs to NP, polynomial compression
already implies polynomial kernelization. The unrestricted target R is therefore
essential to the unresolved comparison. For a nontrivial Q in NP, an unconditional
proof that no polynomial kernel exists would imply P ≠ NP: under P = NP, a
polynomial-time decider can output fixed YES/NO instances. The checked sources
do not explicitly select this stronger unconditional demand.

## Checked primary sources

- Cygan et al., Parameterized Algorithms, author manuscript 30 May 2016:
  Definition 2.1, printed pp.18–19; Definition 15.8, p.531; §15.1.2, p.533
  (PDF pages 34–35, 547, 549). The last passage asks about “natural problems”.
  https://parameterized-algorithms.mimuw.edu.pl/parameterized-algorithms.pdf
- Fomin, Lokshtanov, Saurabh, Zehavi, Kernelization, author draft 1 June 2018,
  published book 2019: Theorem 1.6, p.16; Appendix A.1, p.501
  (PDF pages24,509). The T-Cycle discussion retains the separation question.
  https://fedorvf.github.io/BookKer/book_kernels.pdf
- Lafond and Luo, Preprocessing Complexity for Some Graph Problems Parameterized
  by Structural Parameters, arXiv2306.12655v1, 22 June2023, §7 pp.21–22;
  journal version Discrete Applied Mathematics371(2025),46–59.
  https://arxiv.org/abs/2306.12655v1
- Wahlström, STACS2013, Theorem7, printed349, and following discussion349–350:
  randomized cubic compression for K-Cycle is not a deterministic separation.
  https://doi.org/10.4230/LIPIcs.STACS.2013.341
- Antipov and Kratsch, Boundaried Kernelization via Representative Sets,
  IPEC2025, §1 p.6:2: still distinguishes randomized Steiner Cycle compression
  from a polynomial kernel; its boundaried lower bounds concern another model.
  https://doi.org/10.4230/LIPIcs.IPEC.2025.6

Bounded later searches through the review date did not find a matching
separation. This is not a certificate of exhaustive current openness.

Still to choose: an exact admissible class replacing the informal naturalness
condition, deterministic versus randomized compression, and an explicit lower
bound assumption or unconditional requirement. Merely difficult formulation
is not grounds to remove the card or record it as completed.

The choices listed in the original audit above have now been fixed explicitly in the completed card; they are not outstanding blockers.
