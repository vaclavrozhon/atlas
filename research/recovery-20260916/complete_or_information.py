"""Preserve the chosen round-dependent OR target and archive its known approximation."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0464';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Round-dependent information leakage for two-bit OR',
 status='resolved',criterion='resources',question_type='function',
 formal=r'''Determine a function \(a:\{2,3,\ldots\}\to\mathbb R\) satisfying
\[
|a(r)-I_r|\le1/100\qquad(r\ge2),
\]
where \(I_r\) is the infimum internal information cost, in bits, of zero-error two-party protocols using at most \(r\) messages to compute \(X\lor Y\). The input bits \(X,Y\) are independent and uniform, Alice knows \(X\), Bob knows \(Y\), and both must learn the answer. No efficiency bound is imposed on specifying or evaluating \(a\). This numerical target admits a known finite approximation procedure.''',
 definitions=r'''A protocol has alternating messages, starting with Alice. The first sender can be fixed without loss for this symmetric input distribution and function. A message is one symbol from a finite alphabet that may depend on the preceding transcript. Alphabet sizes and the number of communicated bits are unrestricted; the bound counts messages, not bits. Early termination can be padded with deterministic empty messages to exactly \(r\) turns. Termination and the next speaker convey no uncounted private information. Each local action depends on the sender's bit, the public transcript and its private randomness. Public randomness is also allowed and is independent of the inputs and private randomness. Protocols have finite trees and may use arbitrary real transition probabilities. There is no restriction on local computational cost.

On every one of the four input pairs, both parties must output the correct OR with probability one. Let \(T\) be the complete message transcript and \(R\) the public random seed. With base-two Shannon entropy and the convention \(0\log_2 0=0\), define
\[
\operatorname{IC}(\pi)=I(X;T\mid Y,R)+I(Y;T\mid X,R),\qquad
I(U;V\mid W)=H(U\mid W)-H(U\mid V,W).
\]
Private random choices remain hidden; they must not be converted into revealed public coins when computing this cost. Public mixtures cannot lower the infimum below the best fixed public seed. Equivalently, \(I_r\) is the infimum over private-coin protocols. For these protocols,
\[
\operatorname{IC}(\pi)=2+H(Y,T)+H(X,T)-2H(X,Y,T).
\]
The cost includes information inevitably disclosed by learning the answer; no output-information term is subtracted. It is the sum of both parties' information gains, not their maximum or external information \(I(X,Y;T)\). The elementary two-message protocol gives a nonempty admissible class and \(0\le I_r\le2\).

The requested approximation is uniform over the entire integer domain \(r\ge2\). A finite evaluation rule or unambiguous mathematical expression with a proved error bound qualifies. Restating the original infimum, reporting only a limiting value as \(r\to\infty\), giving a convergence order with unspecified constants, or checking finitely many rounds does not qualify.''',
 answer_criterion='Supply a function a on every integer r at least two and a complete mathematically correct Lean-checked proof of absolute error at most 1/100 bit for the stated zero-error internal-information infimum. A certified interval of width at most 1/50 bit for every r qualifies via its midpoint. A finite discretization algorithm is allowed regardless of its running time. Archival records known mathematical approximability, not the existence of an already checked Lean development.',
 why='Two-bit OR is a canonical example of how interaction can reduce information disclosure. Its round-dependent optimum separates the amount learned from the number of bits sent, but the unrestricted 1/100-accuracy target is already obtainable by finite optimization.',
 importance=dict(score=61,method='editorial',reason='A canonical information-complexity example that illustrates the value of interaction; the selected numerical tolerance without efficiency restrictions makes this a known approximation task rather than a remaining benchmark barrier.'),
 source_formulation=dict(text='Problem (1.3) asks about information disclosed when computing OR and its dependence on communication rounds. The user selected independent uniform bits, zero error for both parties, the sum of internal information gains, every finite message bound r at least two, and absolute accuracy 1/100. These choices are recorded explicitly rather than inferred from the short source question.',caption='Dagstuhl Seminar 22301, §4 Problem (1.3), printed p.198 / standalone PDF p.19.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Algorithmic Aspects of Information Theory','Alexander Shen, open-problems session',2022,'https://doi.org/10.4230/DagRep.12.7.180','§4 Problem (1.3), printed p.198 / standalone PDF p.19'),
 ref('computable','Information Complexity Is Computable','Mark Braverman; Jon Schneider',2016,'https://doi.org/10.4230/LIPIcs.ICALP.2016.87','§1.1 p.87:2; §3.3 Theorem 11 pp.87:8–87:9; §3.4 finite enumeration'),
 ref('and','From Information to Exact Communication','Mark Braverman; Ankit Garg; Denis Pankratov; Omri Weinstein',2012,'https://eccc.weizmann.ac.il/report/2012/171/','Report dated 2 December 2012, §4.2 pp.8–9 and §7.9 p.31; later STOC 2013'),
 ],
 context_blocks=[
 block('The source asks about two random input bits and the benefit of allowing more messages. Complementing both input bits and the output converts OR to AND while preserving the uniform distribution and information cost.'),
 block('The AND analysis separates the fixed-prior cost from a maximum over input distributions. Its often-quoted value near 1.4923 is the latter; it must not be inserted as the uniform-prior answer to this card. Its unrestricted-round protocol also does not by itself give the whole finite-round curve.','and'),
 block('The message-compression argument in Theorem 11 preserves each speaking turn while reducing a message to at most log₂|X×Y| bits, using public randomness that can subsequently be fixed. Here |X×Y|=4, so four possible messages per turn suffice for the infimum. The following explicit grid certificate is an editorial consequence of that reduction and elementary entropy continuity.','computable'),
 block(r'''For a given \(r\), choose the first integer \(k\ge1\) with \(2^k\ge8r\) and \(6400r(2r+4+k)<2^k\), and put \(M=2^k\). Enumerate all alternating depth-\(r\), four-branch protocol trees whose local transition probabilities are multiples of \(1/M\). Keep exactly those for which each possible final transcript is compatible only with input pairs having one common OR value. This is a finite, decidable zero-error test on rational products. At each node there is a probability row for each of the sender's two possible input bits. Let \(v_r\) be the minimum of \(2+H(Y,T)+H(X,T)-2H(X,Y,T)\) over these finitely many valid tables, under the uniform input distribution. This minimum is nonempty because the elementary two-message protocol belongs to the grid.''','computable'),
 block(r'''To check the grid error, round each probability row down on all but one of its positive entries and put the remainder in the last positive entry. Zeros stay zero, so every resulting transcript support is a subset of an original zero-error support. The total-variation change per message is at most \(3/M\), and that of the complete joint distribution is at most \(\delta=4r/M\le1/2\). All entropy alphabets have at most \(4^{r+1}\) elements. Entropy continuity and \(h_2(\delta)\le\delta\log_2(1/\delta)+2\delta\) bound the change in internal information by
\[
4\bigl(\delta(2r+2)+h_2(\delta)\bigr)
\le\frac{16r(2r+4+k)}{2^k}<1/400.
\]
Consequently \(I_r\le v_r\le I_r+1/400\). Thus the finite expression \(a(r)=v_r\) already meets the requested precision; evaluating its logarithms within another \(1/400\) still does so. This certificate does not provide a short exact formula or an efficient algorithm.''','computable'),
 ],
 progress=[
 progress('2012-12','The AND analysis gives the unrestricted-round optimum and studies how finite-round costs converge; it uses the model in which both participants know the answer.','and'),
 progress('2016-07','The finite-message compression and finite-optimization framework make certified approximation available without an efficiency constraint. Applied to the selected fixed-round model, the grid construction above settles the 1/100 target.','computable'),
 ],
),[
 'Applied the user-confirmed round-dependent numerical target, with independent uniform bits and both-party zero-error output.',
 'Specified message counting, private/public randomness, the sum of internal information costs and absolute bit accuracy.',
 'Checked that Theorem 11 compresses each message without adding speaking turns and that fixing public randomness preserves the infimum.',
 'Gave a finite rational-grid certificate with an explicit terminating choice of precision, support-preserving rounding and a quantified entropy-continuity bound.',
 'Archived only the chosen unrestricted approximation target, not a stronger exact closed-form or efficient-evaluation question; required complete Lean checking for a benchmark answer.',
],[
 'Read Dagstuhl Problem (1.3), the both-party output convention in the ECCC report §4.2, and its fixed-round discussion.',
 'Read ICALP 2016 §1.1, the entire turn-by-turn proof of Theorem 11, and §3.4 on finite enumeration.',
 'Checked the editorial grid consequence directly: four messages, finitely many rows, exact rational support tests, preserved zeros, total-variation accumulation, entropy alphabet sizes and the explicit less-than-1/400 inequality.',
], 'Resolved for the selected numerical tolerance with no running-time bound. Theorem 11 of Braverman–Schneider supplies finite message alphabets; the explicit support-preserving grid argument recorded here yields a certified approximation for every r. This is a consequence of known methods, not a claim that the source states this exact grid formula, that the finite-round optimum has a simple exact formula, or that a Lean proof is already available. Reviewed 18 September 2026.',summary=[
 'Alice and Bob hold independent uniform bits and must both learn their OR without error.',
 'For each message bound r, the target is the least total information they learn about one another’s inputs.',
 'The user selected the whole round-dependent function, with absolute error at most one hundredth of a bit.',
 'Known message compression reduces each turn to four possibilities, allowing a finite probability grid with a certified error bound.',
 'The card is archived because this unrestricted approximation is already available, while exact formulas and efficient evaluation are stronger questions.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],archive_reason='The user-selected finite-round internal-information curve to absolute 1/100 bit, without an efficiency bound, is approximable by known finite-message compression and the explicit finite-grid certificate recorded in the card. Preserve the chosen model as a resolved approximation record; do not claim a simple exact finite-round formula or an existing Lean formalization.')
