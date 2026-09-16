# Independent audit of proposed TCS-5326 scope

Checked 16 September 2026. No canonical, queue, selection, comment, commit, or publication changes. This file does not modify the parent-owned draft.

## Conclusion

The checked Rao–Sinha and Ganor–Kol–Raz separations do not refute the proposed O((I+1) log n) bound when n means input bits per participant. No proof or refutation of this exact editorial combination was established in this bounded audit. Keep status uncertain; do not promote it to a uniquely source-specified current conjecture.

The primary MFCS 2016 paper, introduction p. 57:2, explicitly leaves open a small-loss two-party compression direction, with logarithmic input-size loss as an example. It does not fully specify the selected joint-transcript error, worst-case clock, finite-coin convention, or formula. Its later multiparty PIC theorem uses a different measure.

## Rao–Sinha: parameters and source inconsistency

Primary: Anup Rao and Makrand Sinha, Simplified Separation of Information and Communication, ECCC TR15-057 revision 3, 14 December 2017.

Source: https://eccc.weizmann.ac.il/report/2015/057/
Cached pic-compression-raosinha2017.pdf and .txt.

Theorem 1.1, p. 2, together with its low-information protocol in Section5/Figure5.1 pp.19–20: a protocol with communication O(m log k), information O((log k + log log m) 2^((2 log m)/k)), and error at most 4/log m. Here m renames the paper's parameter n, avoiding confusion with card input bit length.

Corollary 1.3, p. 2: choose m = 2^k, obtaining information O(log k), communication 2^O(k), and error at most 4/k; constant-error protocols require Omega(k) communication.

Section 3, p. 8: each participant receives a function [k]^{<m} -> [k] and a Boolean function [k]^m -> {0,1}. An explicit binary truth-table encoding has
\[
N=k^m+\lceil\log_2 k\rceil\sum_{r=0}^{m-1}k^r
\]
bits per participant. Hence log_2 N = Theta(m log k); at m = 2^k, log_2 N = Theta(2^k log k). This is our elementary encoding calculation from the source definition, not a quoted theorem.

More strongly than merely comparing lower bounds, the original protocol from Theorem 1.1 already has communication O(log N). Running it unchanged gives exact transcript simulation within the proposed O((I+1) log N) allowance for this family.

Warning about attribution: p. 3 says that input length satisfies log log log N = Theta(k). Under the explicit section 3 encoding and the corollary's m = 2^k, the calculation instead yields log log N = Theta(k). The preceding paragraph introduces a different parameter t through k = 512 * 2^(4t), which would explain a triple logarithm expressed in t. Do not silently repair or repeat the p. 3 sentence as a checked numerical fact. Use the definition-based calculation above. This inconsistency does not alter the non-refutation conclusion.

## GKR external-information separation for relations

Primary: Anat Ganor, Gillat Kol and Ran Raz, Exponential Separation of Communication and External Information, ECCC TR15-088, published 31 May 2015; subsequently STOC 2016, pp. 977–986, DOI 10.1145/2897518.2897535.

Source: https://eccc.weizmann.ac.il/report/2015/088/
Newly cached pic-compression-gkr-external2015.pdf and .txt.

Section 1.1.1, p. 3, Theorem 1: some distribution makes every protocol of cost at most 2^k have error at least 1 - 2^(-k). Theorem 2 gives a zero-error protocol with external information O(k) for every input distribution.

The immediately following paragraph says input length is quadruple exponential in k, while the low-information protocol's communication is triple exponential. Section 2, p. 4, defines the full hidden-layers input functions on the large tree. The logarithm of input bit length is therefore still triple exponential, far larger than the quoted 2^k lower bound.

The relation/Boolean distinction alone does not save the card: universal transcript compression covers protocols for relations as well. Here it is the actual input-length dependence that prevents this known separation from refuting the bound.

## Suruga 2026

Primary: Daiki Suruga, Zero-error information equals amortized communication complexity, arXiv:2608.04141v1, submitted 4 August 2026 at 18:47:42 UTC. PDF title-page date: 6 August 2026. The arXiv record checked on 16 September shows only v1.

Source: https://arxiv.org/abs/2608.04141
Cached pic-compression-suruga2026.pdf and .txt.

Equation (3), p. 3, defines prior-free information complexity; setting error to zero gives IC_0. This is not the information cost of one prescribed protocol under one prescribed distribution.

Theorem 1, p. 4: for a fixed relation f, amortized expected communication with fixed global error epsilon tends to (1 - epsilon) IC_0(f). Theorem 2, p. 4: amortized worst-case communication has liminf/limsup between (1 - epsilon) IC_0(f) and IC_0(f).

Corollary 1 and the following paragraph, p. 4: combined with the GKR relation separation, this refutes the general constant-factor direct-sum assertion under global error. The text still distinguishes the open total-function separation issue.

Section 2, p. 9, states relation-output, abort, expected-cost and worst-case conventions. Footnote 2 restricts the distributional worst-case maximum to the distribution's support.

These are many-copy amortized characterizations. They do not give the proposed one-copy simulator of every supplied transcript, do not use the same fixed I_mu(pi) benchmark, and do not replace the missing logarithmic-input-length simulation theorem. This preprint is relevant context, not a resolution of TCS-5326.

## Model and negation review

The current draft's quantifier order and full negation are correct. The negative side must defeat every absolute constant, allowing bad n, mu and pi to depend on that constant. Failure of one construction is insufficient.

Including the original shared random string in T = (R,M), and comparing the joint law (X,Y,T_A,T_B) against (X,Y,T,T), specifies a meaningful internal transcript-simulation target. It preserves agreement and correlation with inputs. The simulation may generate the original public randomness as an output component instead of reusing its own actual public tape.

The finite-tree convention blocks uncharged information through timing or the next speaker's identity. A worst-case bound over pairs outside the support of mu introduces no special obstacle when transferring a support-bounded simulation: truncate at the intended cap everywhere, leaving on-support executions meeting that cap unchanged.

Finite fair coins are an explicit editorial convention, not asserted verbatim by the MFCS source. Arbitrary real input distributions are coherent with existential, nonuniform finite protocols and free local work. Do not imply an effective finite encoding of every real distribution.

Two earlier textual errors were sent to the parent and are now fixed: the unrestricted-advice/quantum sentence, and the erroneous exclusion of refutations on product-distribution or public-coin subclasses. A refutation on either subclass refutes universality; only a positive theorem on a subclass is insufficient.

Minor clarification: explicitly choose real K >= 1, or integer K >= 1 (equivalent by rounding). Also avoid portraying expected communication as an absolute unrelated model barrier. An expected-cost theorem with the same asymptotic bound and error slack can be truncated using Markov's inequality, obtaining worst-case cost with a larger absolute constant and slightly larger error. An expected-cost bound only at the exact threshold, with no conversion, is insufficient by itself.

The original logarithmic-loss phrase does not certify the exact constant and all conventions. Retain the draft's explicit editorial disclosure and uncertain status.
