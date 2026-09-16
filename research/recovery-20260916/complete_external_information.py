"""Archive the historical equality, refuted by Braverman–Minzer at STOC 2021."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0220'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the complete Banff 2017 question from Sublinear.info Problem 76, separating fixed input length from the number of independent copies.',
 'Defined public transcript, external mutual information, zero error on all inputs and expected communication under the selected distribution.',
 'Kept the original exact universal equality rather than replacing it with the still broader search for an amortized-complexity characterization.',
 'Matched the conjecture to Braverman–Minzer Theorem 1.3 and the stronger zero-error Corollary 1.4 in the published STOC 2021 work.',
 'Read the construction, zero-error certificate-verification upper bound, external-information lower-bound argument and the rare-branch corollary proof; recorded reliance on the cited earlier lower-bound and compression theorems.',
 'Checked the August 2026 similarly titled preprint: its information definition is internal and its communication target allows global error, so it is not a reversal of this external-information separation.',
 'Preserved the existing importance score and archived the completed historical question intact as resolved negatively.',
]
sources=[
 'Read Sublinear.info Problem 76, External Information and Amortized Expected Communication, suggested by Mark Braverman at Banff 2017; page retrieved 16 September 2026, revision oldid=1061. The ordinary HTTP client retrieved the complete page after the browser tool returned 403.',
 'Checked publication metadata for Braverman–Minzer, New Separations Results for External Information, STOC 2021 pp. 248–258, DOI 10.1145/3406325.3451044, published 15 June 2021.',
 'Read arXiv:2103.04049v1, dated 6 March 2021: §1 Theorem 1.3 and Corollary 1.4 pp. 4–5; §2.2 protocol definitions; §4 pp. 20–25, including the AND-OR construction, hint distribution, Lemma 4.4 and Lemmas 4.5–4.8; §5.2 pp. 27–28. The separation already follows from Theorem 1.3 by monotonicity of external information in the permitted error.',
 'For the proof dependency scope, checked the role of the bursting-noise relative-discrepancy result, the cited AND-OR internal-information lower bound and amortized positive-error compression. Their original proofs were not independently reconstructed; this is a published-result archival review, not a complete independent or Lean proof certification.',
 'Read Suruga, Zero-error information equals amortized communication complexity, arXiv:2608.04141v1, submitted 4 August 2026, manuscript dated 6 August: abstract, introductory information definition and main target. It uses internal information and a different error regime. Its claimed new theorems are not needed for this archival decision.',
]
status=('Resolved negatively by Braverman and Minzer, STOC 2021. Their Theorem 1.3 gives total Boolean functions with zero-error amortized expected communication '
 'O(sqrt(k) log^2 k) but external information Omega(k) even when constant error is allowed; hence the zero-error external information is larger as well. '
 'Corollary 1.4 gives the still stronger constant-versus-unbounded separation. The archived card retains the original universal equality. '
 'This review checks the published result and its model/proof scope, and does not claim an independent Lean formalization.')
complete(identifier,dict(
 title='External information and amortized expected communication',
 criterion='characterization',question_type='yes_no',status='resolved',
 formal=r'''Historical question, resolved negatively: for every integer \(\ell\ge1\), every total Boolean function
\[
F:\{0,1\}^{\ell}\times\{0,1\}^{\ell}\to\{0,1\},
\]
and every probability distribution \(\mu\) on its input pairs, is
\[
\operatorname{IC}^{\mathrm{ext}}_\mu(F,0)
=
\lim_{q\to\infty}
\frac{\overline{\operatorname{CC}}_{\mu^{\otimes q}}(F^{\otimes q},0)}{q}\ ?
\]
Both optimizations use randomized two-party protocols that are correct on every input, including pairs of \(\mu\)-probability zero. The expectation in the communication cost is with respect to \(\mu\) and the protocol randomness. The precise model and the known negative answer are recorded below.''',
 definitions=r'''Alice receives \(x\in\{0,1\}^{\ell}\) and Bob receives \(y\in\{0,1\}^{\ell}\). They communicate classical bits interactively, with no restriction on local computation or number of rounds. They may use independent private random bits and shared public random bits independent of the inputs. A protocol is a binary communication tree: the next speaker is determined by the public transcript, and a terminal node has the common output label. Sending a bit costs one; local computation and public randomness cost nothing. No information may be conveyed for free by message timing or termination.

Use finite protocols, with arbitrarily large finite depth and randomness permitted in the optimization. A zero-error protocol has the correct terminal output on every input and every possible random choice. No expected-time or worst-case communication bound is imposed separately; the relevant communication objective is the expected number of transmitted bits. Finite protocols suffice as the standard approximation convention for the infima.

Let \(R\) be the public random string and \(M\) the exchanged-bit transcript, and let \(T=(R,M)\). When \((X,Y)\sim\mu\), the external information cost in bits is
\[
I_\mu(T;X,Y)=I_\mu(M;X,Y\mid R).
\]
The equality uses independence of \(R\) from the inputs. For finite random variables, entropy and conditional entropy are
\[
H(V)=-\sum_v p(v)\log_2 p(v),\qquad
H(V\mid W)=\sum_w p(w)H(V\mid W=w),
\]
with \(0\log_2 0=0\), and \(I(U;V)=H(V)-H(V\mid U)\). Define
\[
\operatorname{IC}^{\mathrm{ext}}_\mu(F,0)
=\inf_{\Pi\text{ computes }F\text{ with zero error}}
I_\mu(T_\Pi;X,Y).
\]
This is information revealed to an observer of the conversation about the joint input. It differs from internal information, which sums what Alice learns about Bob's input and what Bob learns about Alice's input.

For \(q\ge1\), the product task has inputs \(x^q=(x_1,\ldots,x_q)\) and \(y^q=(y_1,\ldots,y_q)\), and must output the entire vector
\[
F^{\otimes q}(x^q,y^q)=(F(x_1,y_1),\ldots,F(x_q,y_q)).
\]
The distribution \(\mu^{\otimes q}\) draws independent pairs \((X_i,Y_i)\sim\mu\); \(X_i\) and \(Y_i\) inside a pair need not be independent. Protocols may mix communication for different coordinates arbitrarily. Put
\[
\overline{\operatorname{CC}}_{\mu^{\otimes q}}(F^{\otimes q},0)
=\inf_{\Pi\text{ computes }F^{\otimes q}\text{ with zero error}}
\mathbb E_{\mu^{\otimes q},\,\Pi}[|M_\Pi|].
\]
Protocols may be chosen separately for each \(F,\mu,q\). Correctness still holds on the entire product input domain, not only on the support of the evaluation distribution.

The limit in the question is well-defined: these nonnegative expected costs are finite and subadditive in \(q\), since independent-copy protocols can be concatenated. Equivalently, the limit is the infimum of the costs divided by \(q\). The normalization is communicated bits per copy.

The known separation uses families \((F_k,\mu_k)\), with input length allowed to depend on \(k\), for which
\[
\lim_{q\to\infty}
\frac{\overline{\operatorname{CC}}_{\mu_k^{\otimes q}}(F_k^{\otimes q},0)}q
=O\!\left(\sqrt{k}\log^2 k\right),
\qquad
\operatorname{IC}^{\mathrm{ext}}_{\mu_k}(F_k,0)=\Omega(k).
\]
The lower bound in the published theorem even permits distributional error \(1/16\), so it applies to its smaller zero-error protocol class. For sufficiently large \(k\), the two quantities are unequal. The publication also strengthens this to bounded amortized cost and arbitrarily large zero-error external information.''',
 answer_criterion=r'''The historical benchmark asks for a complete Lean-checked proof or refutation of the exact displayed universal equality. A negative answer may supply a total function and distribution with a proved strict separation, or a proved family that yields such a witness. The recorded published separation answers the mathematical question negatively, but citing it alone is not a Lean proof. The equality is a binary proposition, so numerical \(1/100\) acceptance slack does not replace it by an approximate equality. The card is archived because the original research question is already resolved.''',
 source_formulation=dict(
 text='Problem 76 asks whether zero-error external information complexity always equals the per-copy limit of expected communication for independent copies, with the same input distribution.',
 caption='Paraphrase of Sublinear.info Problem 76, Banff 2017, revision oldid=1061; the copy index is renamed q to distinguish it from input length.',
 citation='primary',format='editorial_paraphrase'),
 why='The proposed equality would have described the cost of solving many instances using a single-instance information quantity. Its failure shows that joint protocols can exploit structure not captured by zero-error external information alone, even for total functions.',
 references=[
 ref('primary','Problem 76: External Information and Amortized Expected Communication',
 'Mark Braverman',2017,'https://sublinear.info/76',
 'Banff 2017; complete displayed question, revision oldid=1061, retrieved 16 September 2026'),
 ref('separation','New Separations Results for External Information',
 'Mark Braverman; Dor Minzer',2021,'https://doi.org/10.1145/3406325.3451044',
 'STOC 2021, pp. 248–258, published 15 June 2021; full arXiv:2103.04049v1, Theorem 1.3, Corollary 1.4, §§2.2, 4 and 5.2'),
 ref('later','Zero-error information equals amortized communication complexity',
 'Daiki Suruga',2026,'https://arxiv.org/abs/2608.04141v1',
 'Preprint submitted 4 August 2026, manuscript dated 6 August; introductory definition (1) uses internal information, with a different global-error communication target'),
 ],
 context_blocks=[
 block('The original question fixes a distribution for measuring cost, but requires the protocol to be correct even at inputs outside its support. Replacing this by a promise of membership in the support changes the question.'),
 block('The comparison uses external information about the pair of inputs. The well-known positive-error amortization results involving internal information concern a different quantity and cannot be substituted into this equality.','separation'),
 block('Theorem 1.3 separates zero-error amortized expected communication from external information even when the information protocol may make constant error. Monotonicity immediately gives a separation from zero-error external information as well.','separation'),
 block('Corollary 1.4 strengthens the negative conclusion: there are instances with a bounded amortized cost and unbounded zero-error external information. The statement concerns total Boolean functions.','separation'),
 block('The published paper leaves the broader task of characterizing amortized zero-error communication as a separate question. This archived record retains the specific proposed equality rather than adopting that broader target.','separation'),
 block('The similarly titled August 2026 preprint defines information using the internal-information sum and studies a different error convention. Its claims are not needed to establish the historical external-information counterexample.','later'),
 ],
 progress=[
 progress('2017','The equality is listed as Problem 76 after Banff 2017.'),
 progress('2021-06-15','The STOC paper publishes the negative separation, including total Boolean functions.','separation'),
 progress('2026-09-16','The source and published counterexample are matched, the model is made explicit, and the historical record is archived as resolved.','separation'),
 ],
),notes,sources,status,summary=[
 'The historical question compares external information revealed by a zero-error protocol with communication per copy over many independent instances.',
 'Communication is averaged under a fixed input distribution, but correctness is required on every input.',
 'Braverman and Minzer gave total Boolean functions for which amortized communication is strictly smaller than external information.',
 'Their published result refutes the original universal equality, with an even stronger constant-versus-unbounded zero-error separation.',
 'The card preserves that precise historical question and is archived as resolved rather than expanded to a different characterization problem.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],
 archive_reason='Resolved negatively by Braverman–Minzer, STOC 2021, DOI 10.1145/3406325.3451044, Theorem 1.3 and Corollary 1.4; original external-information equality preserved with a completed source/model review.')
