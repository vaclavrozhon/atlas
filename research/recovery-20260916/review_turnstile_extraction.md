# TCS-5427: historical background imported as an open question

Individual source review, 16 September 2026. Disposition: exclude the invalid
open-question extraction and preserve its original card in the archive.

The imported sentence is in §1.2, “Shortcomings of the LNW Reduction,” printed
p. 20:3, of Ai, Hu, Li and Woodruff,
[New Characterizations in Turnstile Streams with Applications](https://doi.org/10.4230/LIPIcs.CCC.2016.20).
It describes the situation before this paper's contribution. The original
locator “PDF p. 2” is also inaccurate for the published version.

The abstract on p. 20:1 and §1.3 on p. 20:4 announce the multipass extension.
Section 5, pp. 20:15–20:20, states and proves Theorem 5.1. For a fixed constant
number of passes, its distributional formulation replaces a randomized
automaton by a deterministic path-independent one, without increasing the
paper's space measure and with arbitrarily small extra error. The paragraph
after the proof uses minimax and randomness reduction to recover a randomized
simulation. In each pass the linear sketch can depend on preceding pass outputs.

The model matters: §2, pp. 20:5–20:7, permits arbitrarily long turnstile streams,
including intermediate vectors outside the final box. Its multipass space
measure sums constituent state-space logarithms along a realized sequence of
passes. Matrices and output maps are nonuniform; the theorem does not establish
a computationally efficient compiler. This is not a claim for growing pass
counts, a polynomial stream-length restriction, or the usual maximum-live-memory
measure with a pass-independent simulation constant.

The recent primary preprint by Jiang, Liu and Yu,
[arXiv:2604.22052v1](https://arxiv.org/abs/2604.22052v1), 23 April 2026,
§1.3, printed p. 5, independently identifies the 2016 work as the multipass
extension. Its own polynomial-length-stream results concern a separate model
restriction. They are not needed for this exclusion and are not substituted
as a new target.

Review coverage: the source abstract, §§1.2–1.3, definitions in §2, all of §5,
and Appendix A were read, together with the 2026 abstract and related-work
paragraph. This is a source-context disposition, not an independent mathematical
certification of every step of the published simulation proof or a Lean
formalization. There is no post-result open multipass question at the imported
location. Under docs/RULES.md's invalid-extraction rule, the review does not
invent a new benchmark theorem merely to populate a card.

The original card is archived byte-for-byte; the archive reason, queue and
review ledger record this disposition. No pre-existing archived body was
reviewed or modified.
