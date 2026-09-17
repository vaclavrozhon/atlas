# OV to Hitting Set implication: pending scope choice

Reviewed 17 September 2026; TCS-6942 is claimed but not completed.

The ICM 2018 survey *On Some Fine-Grained Questions in Algorithms and
Complexity* uses a randomized logarithmic-word RAM (p. 3), defines OV
and its hypothesis in §3, p. 7, and HS in §6, pp. 15–16. The imported
locator “§5” is incorrect: the relevant heading is §6. Hypotheses 4 and 5
use the absence of a single n^(2-epsilon) poly(d) algorithm. The text
introduces superlogarithmic dimensions. Page 16 explicitly records
HS hypothesis implies OV hypothesis and leaves the reverse unknown.

Completed TCS-6596 and TCS-6599 instead use the logarithmic-dimension
formulation: for every saving epsilon there exists a fixed c for which
dimension ceil(c log n) remains hard. Their negations permit separate
programs for each c with a common saving. The literal all-dimensions uniform
algorithm statement is not silently interchangeable with that quantifier
order. An asynchronous choice asks whether to connect those existing
hypotheses (recommended) or retain the survey's literal uniform formulation.

For either selected formulation, the predicate direction is:

- OV: there exists a in A and b in B with integer inner product zero.
- HS: there exists a in A such that every b in B has positive inner product.
- The requested hardness implication OVH implies HSH is equivalently the
  algorithmic implication FastHS implies FastOV, not its reverse.

The claim is an implication between propositions. It does not, without an
additional user choice, require a particular black-box reduction technique.

Read Carmosino et al., ITCS 2016, author published PDF, §5 pp. 264–265:
Theorem 2, Corollary 2, Theorem 3 and §5.2 Lemma 6 with its proof. The
NSETH non-reducibility barrier applies to deterministic and zero-error
fine-grained reductions in its specified model; it does not unconditionally
refute the logical implication or cover all bounded-error arguments.

Read Johnson et al., *Complexity Framework for Forbidden Subgraphs I:
The Framework*, Algorithmica 87:429–464 (5 January 2025),
DOI 10.1007/s00453-024-01289-2, introduction and §5 Theorem 19.
It uses separate OV and HS assumptions for diameter and radius and records
the known HS-to-OV direction. Bounded primary-source searches through the
review date found no resolution of the requested reverse implication.

The source PDFs for the 2018 survey and 2016 barrier are cached as
finegrainsurvey2018 and nseth2016 under the recovery source cache.
