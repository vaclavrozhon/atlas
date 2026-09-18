"""Specify the selected oracle conversion from two-source extraction to non-malleability."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-2201';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A general oracle conversion from two-source extractors to non-malleable extractors',
 status='uncertain',criterion='reductions',question_type='yes_no',
 formal=r'''Do there exist positive integers \(C,K,d\), a rational constant \(a\in(0,1]\), and one deterministic oracle algorithm \(T\) with the following property? For every choice of integers \(n\ge1\), \(1\le k\le n\) and \(t\ge1\), set
\[
\varepsilon=2^{-t},\qquad
\kappa=C\bigl(k+\lceil\log_2(n+2)\rceil+t\bigr),\qquad
\eta=C\varepsilon^a.
\]
Whenever \(\kappa\le n\) and \(\eta\le1/10\), every one-bit two-source \((k,\varepsilon)\)-extractor \(E:\{0,1\}^n\times\{0,1\}^n\to\{0,1\}\), supplied only as an evaluation oracle, yields a one-bit two-source non-malleable \((\kappa,\eta)\)-extractor
\[
N_E(x,y)=T^E(1^n,k,1^t,x,y),
\]
where each evaluation of \(T^E\) takes at most \(K(n+2^t+2)^d\) bit operations and oracle queries as specified below?''',
 definitions=r'''For a finite distribution \(X\), its min-entropy is \(H_\infty(X)=-\log_2\max_x\Pr[X=x]\). For distributions \(P,Q\) on the same finite set, their statistical distance is \(\operatorname{SD}(P,Q)=\frac12\sum_z|P(z)-Q(z)|\). Let \(U_1\) be a uniform bit independent of every other random variable under discussion.

The oracle promise means that, for every independent pair of distributions \(X,Y\) on \(\{0,1\}^n\) with \(H_\infty(X),H_\infty(Y)\ge k\),
\[
\operatorname{SD}(E(X,Y),U_1)\le\varepsilon.
\]
This is the ordinary two-source property. It does not require uniformity after revealing either full input, and it does not require resistance to tampering. The sources may have arbitrary real probabilities; no sampler, representation or computational bound for them is assumed.

The required non-malleability means that for every independent \(X,Y\) with both min-entropies at least \(\kappa\), and every two functions \(u,v:\{0,1\}^n\to\{0,1\}^n\) such that at least one has no fixed point anywhere on its domain,
\[
\operatorname{SD}\bigl((N_E(X,Y),N_E(u(X),v(Y))),
(U_1,N_E(u(X),v(Y)))\bigr)\le\eta.
\]
On the right, the tampered-output bit has the same marginal distribution as on the left and is independent of \(U_1\). A function \(u\) has no fixed point if \(u(z)\ne z\) for every \(z\). The functions act separately on the two source strings and can be arbitrary, noninjective and computationally unbounded. They may be chosen with knowledge of \(E\) and \(T\). No min-entropy is required of the tampered sources. There is one tampering experiment, with no shared reference string, extra seed or computational indistinguishability relaxation. Neither full original source is included among the outputs in this definition.

The algorithm is a uniform deterministic multitape oracle Turing machine. The two input strings and unary \(n,t\) are explicit, and \(k\) is binary. Its only information about \(E\) comes from queries \((x',y')\) of two length-\(n\) strings, each returning the single bit \(E(x',y')\). All local steps, input and output access and the work to write query strings are counted; receiving an oracle answer costs one further step. Adaptive queries are allowed. The machine receives no table, circuit, code, advice or special structural facts about \(E\), and cannot query extractors at other parameters. It must halt with a single output bit within the displayed budget for every valid parameter triple, every oracle of this arity and every input pair, even when the oracle does not obey the extractor promise. Its output guarantee is required only for promised oracles and the displayed nonvacuous parameter range.

The constants are universal, independent of \(n,k,t,E\). The running-time dependence on \(2^t=1/\varepsilon\) is polynomial; polynomial time in \(n+t\) is not required. The added entropy is \(O(k+\log_2(n/\varepsilon))\) and the error is at most a fixed power of the original error times a constant. Using dyadic errors fixes a finite precision interface without an arbitrary real input. The conclusion ranges over every promised oracle, not just a particular currently known construction. A construction that happens not to query its oracle would count if it proved all these guarantees; no artificial requirement to make an essential query is imposed.

This is an existence question about a general parameter-preserving transformation. It does not ask for the affine-source variant, a seeded-extractor transformation, or a non-malleable code with an efficient inverse.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of the displayed oracle-transformation statement. A positive answer must give universal constants and one oracle algorithm, prove the every-oracle guarantee, account for query construction and preserve the specified entropy and error tradeoff. Matching a single parameter regime by a special-purpose construction does not establish the full transformation.',
 why='A general conversion would explain when improvements in ordinary extraction automatically survive adversarial changes to independent weak sources. It would replace similarities between individual constructions by a reusable relation between the two notions.',
 importance=dict(score=81,method='editorial',reason='A structural extraction question with connections to tamper-resistant cryptography; the explicit conversion target tests a general principle rather than a small numerical improvement to a single construction.'),
 source_formulation=dict(text='The paper asks broadly whether standard extractors can be used to construct non-malleable extractors. The user explicitly selected the two-source evaluation-oracle conversion, one output bit, O(k+log(n/epsilon)) entropy, polynomial-power error and poly(n,1/epsilon) time on 18 September 2026. Those exact quantifiers and losses are an editorial candidate, not a theorem or conjecture stated verbatim by the authors.',caption='Li–Zhong, Definitions 1–4 pp.108:2–3 and §3 p.108:12.',citation='primary',format='editorial_paraphrase'),
 references=[ref('primary','Two-Source and Affine Non-Malleable Extractors for Small Entropy','Xin Li; Yan Zhong',2024,'https://doi.org/10.4230/LIPIcs.ICALP.2024.108','Definitions 1–4 pp.108:2–3; §1.1; §2.2; §3 p.108:12')],
 context_blocks=[block('The paper constructs two-source and affine non-malleable extractors at low entropy, matching known ordinary-extractor parameters in particular regimes. Its conclusion suggests a broader reverse connection from ordinary extraction to non-malleability.'),block('The construction uses internal ingredients of previous extractors and explains why a naive black-box use of a standard component does not give the needed independence. This motivates the distinction between matching parameters in a construction and a conversion for every extractor oracle.'),block('The card chooses the independent-two-source model from the source’s several extraction notions. Its quantitative oracle statement is a user-selected editorial specialization, so its exact current status is recorded as uncertain.')],
 progress=[progress('2024','The paper obtains low-entropy non-malleable constructions and proposes a broader connection with ordinary extractors.')],
),['Recorded the explicitly selected two-source black-box evaluation model and universal parameter losses.','Defined ordinary extraction, joint non-malleability, min-entropy, statistical distance and separate fixed-point-free tampering.','Specified dyadic error, the nonvacuous entropy/error range and complete oracle bit costs.','Marked the exact editorial candidate uncertain and separated special-purpose constructions from the universal guarantee.'],['Read Definitions 1–4, the main parameter statements, the §2.2 black-box obstacle and the complete §3 conclusion of ICALP 2024.','Bounded primary-source searches through 18 September 2026 found work on seeded transformations, non-malleable codes and randomized common-reference-string models, but no verified proof or refutation of this exact oracle conversion.'], 'Uncertain for this precise oracle-conversion statement. The source poses a broader structural question and proves particular constructions, not the selected universal transformation. The user explicitly chose this quantitative specialization on 18 September 2026; bounded later-source checks did not verify its resolution.',summary=['An ordinary two-source extractor produces a nearly uniform bit from two independent weak random strings.','Non-malleability requires that bit to stay nearly uniform even after revealing the output on separately tampered strings.','The selected question asks for one general conversion using only evaluation queries to the original extractor.','It permits a constant-factor logarithmic entropy overhead, a fixed-power increase in error and polynomial time in inverse error.','The exact conversion is an editorial candidate inspired by the source’s broader question, with its present status recorded separately.'],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
