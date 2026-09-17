"""Complete the polynomial explicit-order construction target for DNA minimizers."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7370';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the imported exact construction target, DNA alphabet, explicit total-order output, unary window parameter and polynomial bound in 4^k+w.',
 'Defined the order as a permutation with a rank function, zero-based overlapping windows, leftmost tie breaking and the finite probability formula for density.',
 'Specified one deterministic finite-tape Turing machine, exact global optimality and bit-cost accounting including the full output and all preprocessing.',
 'Distinguished expected density over independent random DNA from randomized algorithmic success, and density from its optional normalization by w+1.',
 'Read the original GreedyMini open question and the cached January 2026 OptMini primary PDF, including its explicit continuing complexity question and constant-time-arithmetic caveat.',
 'Separated exact finite-parameter optimization from selected small-parameter formulas, asymptotic density limits, and the August 2026 empirical selection scheme.',
 'Preserved importance 84 and the Lean-checked yes/no criterion; recorded the explicit-order polynomial model as a retained editorial specialization, not a verbatim source bound.',
]
sources=[
 'Read Golan–Tziony–Kraus–Orenstein–Shur, GreedyMini, Bioinformatics 41(Suppl 1), i275–i284, 15 July 2025, DOI 10.1093/bioinformatics/btaf251, full primary PMC text: preliminaries, density convention, Section 3 and Section 5 open questions. The source separately asks the complexity of minimum-density construction and efficient generation. Its computation model assumes unit-cost arithmetic on quantities fitting a constant number of words.',
 'Read the locally saved primary PDF of Shur–Tziony–Orenstein, Generating minimum-density minimizers, bioRxiv DOI 10.64898/2026.01.25.701585v1, posted 28 January 2026, stored in research/random-card-review-20260914/sources/minimizer-opt2026.pdf/txt. Read abstract, Sections 1–2, Lemma 3, Theorem 1 and Section 5. Theorem 1 has time O(2^(sigma^k)*min(sigma^(w+k),w*sigma^(2k))) under its footnote assumption of constant-time arithmetic; it does not establish polynomial bit time in the explicit order size. Section 5 expressly asks whether polynomial dependence on w can avoid double-exponential dependence on k. Fresh full-text requests returned HTTP 403; the reviewed PDF is the saved primary version, corroborated by current primary metadata/abstract.',
 'Read Shur, On Minimizers of Minimum Density, arXiv:2506.05277v1, 5 June 2025: abstract, preliminaries, Theorem 4 and Sections 4–5. Its exact algorithm remains exponential in the number of k-mers; its all-window conclusions cover listed small alphabet/length pairs and do not provide a uniform polynomial algorithm for arbitrary DNA k. The live arXiv history lists v1.',
 'Read the primary abstract and publication metadata of Groot Koerkamp, The Anti-Lexicographic SUS-Anchor: An Empirically Optimal Selection Scheme, WABI 2026 Article 22, 27 August 2026. The reported near-optimality is empirical and the main selection scheme has k=1 in a broader class. It is not a theorem of exact optimal DNA minimizer orders for all k,w>=2. No full proof audit of this paper was performed.',
 'Bounded searches through 17 September 2026 found no verified polynomial-in-(4^k+w) bit algorithm or unconditional nonexistence result. A large search space or the cost of a general-purpose ILP solver is not a hardness proof for this special parameter-only task; no such inference is made.',
]
complete(identifier,dict(
 title='Polynomial-time construction of minimum-density DNA minimizers',criterion='construction',question_type='yes_no',
 formal=r'''Do there exist a constant \(K>0\), an integer \(C\ge1\), and one uniform deterministic algorithm \(A\) such that, for every pair of integers \(k,w\ge2\), it outputs a total order \(\rho\) of all \(4^k\) DNA strings of length \(k\) satisfying
\[
d_{k,w}(\rho)=\min_{\pi}d_{k,w}(\pi)
\]
in at most \(K(4^k+w)^C\) bit-computation steps? The minimum ranges over all total orders of those same strings, and \(d_{k,w}\) is the density defined below. The input encodes \(k\) in binary and \(w\) in unary; the output explicitly lists the \(4^k\) strings from lowest to highest rank. The constants and algorithm are independent of \(k,w\).''',
 definitions=r'''The alphabet is exactly \(\Sigma=\{A,C,G,T\}\). A \(k\)-mer is a string in \(\Sigma^k\); reverse complements are not identified. A total order is represented by a list \(\rho=(u_0,\ldots,u_{4^k-1})\) containing each \(k\)-mer exactly once. Its rank function is \(R_\rho(u_i)=i\). This rank, rather than alphabetical order of letters, determines the minimizer.

For a string \(X\in\Sigma^{k+w}\), positions are indexed from zero. For \(0\le i\le w\), put \(X_i=X[i]\cdots X[i+k-1]\). Define the selected absolute positions in two consecutive windows by
\[
p_0^\rho(X)=\min\operatorname*{arg\,min}_{0\le i<w}R_\rho(X_i),
\qquad
p_1^\rho(X)=\min\operatorname*{arg\,min}_{1\le i\le w}R_\rho(X_i).
\]
Each window contains \(w\) overlapping \(k\)-mers and \(k+w-1\) characters. The outer minimum chooses the smallest position if the least-ranked \(k\)-mer appears more than once. This is leftmost tie breaking in both windows. Define
\[
d_{k,w}(\rho)=4^{-(k+w)}
\left|\left\{X\in\Sigma^{k+w}:p_0^\rho(X)\ne p_1^\rho(X)\right\}\right|.
\]
Thus the density is the probability that the selected position changes after one window shift, when all \(k+w\) letters are independent and uniform over \(\Sigma\). It also equals the limiting expected fraction of positions selected on a long independent uniform DNA string. The finite formula above fixes the quantity without requiring an unspecified limiting convention. The density is not the rescaled density factor \((w+1)d_{k,w}\), a density measured on one supplied genome, or an average over random orders.

Optimality is exact: the output order must have density no greater than that of every competing total order for these same \(k,w\). Any order attaining the minimum is acceptable; the algorithm need not enumerate all optimal orders or print the density. Since the comparison is over a nonempty finite set of orders, a minimum exists. Mere computability by exhaustive search is not the requested result.

The computational model is a deterministic Turing machine with a fixed finite number of tapes and a fixed finite alphabet. Each step reads and writes only a constant number of tape cells and moves each head by at most one cell. Its input is the standard binary expansion of \(k\), a separator, and a string of \(w\) unary symbols. Encode the four DNA letters by four fixed two-bit codes; the output is the concatenation of the \(4^k\) entries, each of length \(k\) letters, whose boundaries are therefore determined by the input. The entire output has \(2k4^k\) bits. Input reading, initialization, arithmetic on every bit, all intermediate computations and all output writes count toward the running time. There is no advice, external oracle, uncharged preprocessing or precomputed table depending on the input parameters. The machine is fixed for all parameter pairs, and the bound is worst-case. No additional space restriction is imposed.

The polynomial resource parameter \(4^k+w\) expresses the number of explicitly output \(k\)-mers together with the unary window size. It is not the binary encoding length of the input. Including the factor \(k\) from the output's bit length changes polynomial bounds only by a polynomial factor. The algorithm is deterministic; the randomness in the density definition specifies the mathematical objective and is not a probability of algorithmic success. The DNA alphabet, explicit output and bit-cost polynomial target are the retained editorial specialization of the source's broader efficient-generation question.''',
 answer_criterion=r'''Give a complete mathematically correct proof checked in Lean of the stated existence proposition or its logical negation. A positive answer must specify one uniform algorithm and prove that it returns a globally minimum-density total order for every \(k,w\ge2\), within the stated polynomial bit-time bound.

Empirically small density, a fixed additive or multiplicative density approximation, optimality only for selected parameter pairs, or asymptotic optimality in a limit of parameters is insufficient. An exponential exact algorithm does not satisfy the resource bound. A conditional complexity lower bound establishes only its conditional conclusion; a large search space alone is not a refutation. There is no numerical tolerance on this exact algorithm-existence question.''',
 source_formulation=dict(text='GreedyMini asks the complexity of the minimum-density problem and whether optimal minimizers can be generated efficiently. OptMini later gives an exact exponential algorithm and asks whether, retaining polynomial dependence on the window size, the double-exponential dependence on k can be avoided. This card preserves the previously imported, specific target of polynomial bit time in the explicit DNA order size and unary window size; it is not presented as equivalent to every possible improvement raised by those sources.',caption='GreedyMini, Section 5; OptMini, Theorem 1 and Section 5, January 2026 version.',citation='primary',format='editorial_paraphrase'),
 why='Minimizers choose seeds used throughout sequence processing, and lower density reduces the number retained under the same window guarantee. The question asks whether a provably best order can be generated efficiently relative to its explicit representation, separating exact optimization from practical low-density designs.',
 references=[
 ref('primary','GreedyMini: generating low-density DNA minimizers','Shay Golan; Ido Tziony; Matan Kraus; Yaron Orenstein; Arseny Shur',2025,'https://pmc.ncbi.nlm.nih.gov/articles/PMC12261476/','Bioinformatics 41(Suppl 1), i275–i284, 15 July 2025; preliminaries and Section 5 complexity/generation questions; DOI 10.1093/bioinformatics/btaf251'),
 ref('optmini','Generating minimum-density minimizers','Arseny Shur; Ido Tziony; Yaron Orenstein',2026,'https://doi.org/10.64898/2026.01.25.701585','28 January 2026 v1; Sections 1–2, Lemma 3, Theorem 1 with arithmetic-cost footnote, Section 5; reviewed from saved primary PDF'),
 ref('asymptotic','On Minimizers of Minimum Density','Arseny Shur',2025,'https://arxiv.org/abs/2506.05277v1','5 June 2025; Theorem 4 and Sections 4–5; exact exponential search and selected small-parameter/asymptotic results'),
 ref('sus','The Anti-Lexicographic SUS-Anchor: An Empirically Optimal Selection Scheme','Ragnar Groot Koerkamp',2026,'https://doi.org/10.4230/LIPIcs.WABI.2026.22','WABI 2026 Article 22, published 27 August; primary abstract and metadata, empirical and model scope'),
 ],
 context_blocks=[
 block('A minimizer samples the lowest-ranked short string in each sliding window. Repeated choices of the same position reduce the number of distinct sampled positions while preserving coverage of every window.'),
 block('GreedyMini provides practical low-density designs but its discussion separately asks for the complexity of guaranteed minimum-density construction.'),
 block('The 2025 theoretical study obtains exact search and analyzes optimality for particular small alphabet and substring-length pairs. These special cases do not provide a polynomial construction for all DNA parameters.','asymptotic'),
 block('OptMini makes exact search practical on more small instances, with a theorem exponential in the number of distinct k-mers. Its discussion still identifies faster optimal generation as an open complexity question, and its time theorem assumes constant-cost arithmetic.','optmini'),
 block('The 2026 SUS-anchor work reports strong empirical density for a broader selection scheme. Its near-optimal experimental results do not certify exact optimal minimizer orders for every finite parameter pair.','sus'),
 block('The card fixes the output representation and bit model to give efficient generation a precise meaning. It requests one optimal full order, not every optimizer or a succinct rule with unspecified construction cost.','optmini'),
 ],
 progress=[progress('2025-06-05','An exact exponential method and small-parameter optimality results are presented in a theoretical preprint.','asymptotic'),progress('2025-07-15','GreedyMini publishes practical low-density generation and states the optimal-generation complexity question.'),progress('2026-01-28','OptMini gives an exact exponential algorithm and explicitly retains the question of faster optimal generation.','optmini'),progress('2026-08-27','The SUS-anchor paper reports empirical near-optimality in a broader sampling setting, without the card’s universal exact construction guarantee.','sus')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified resolution of the precise polynomial bit-time construction target. The January 2026 OptMini theorem remains exponential in the number of k-mers and its discussion explicitly retains the complexity question; the August result is empirical and concerns a different selection setting. The saved primary OptMini v1 was read because fresh full-text requests were blocked. The review checks definitions and theorem scope, not complete proofs of every cited claim.',summary=[
 'A DNA minimizer is determined by a total order on all strings of one fixed length.',
 'Its density is the probability that the selected position changes between consecutive random windows.',
 'The question asks for an exactly optimal order in deterministic time polynomial in its explicit size and the window parameter.',
 'Known exact search remains exponential in the number of distinct short strings, while practical low-density schemes have different guarantees.',
 'A complete Lean-checked answer must prove or refute the uniform polynomial bit-time construction for every allowed pair of parameters.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
