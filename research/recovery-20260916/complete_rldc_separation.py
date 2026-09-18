"""Archive the constant-alphabet symbol-query length separation."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6739';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A polynomial length separation between three-query RLDCs and LDCs',
 status='resolved',criterion='construction',question_type='yes_no',
 formal=r'''Do there exist a fixed finite alphabet \(\Sigma\), constants \(0<\rho<1/100\), \(0<\Delta\le1\) with \(2\rho<\Delta\), real exponents \(0<a<b\), a constant \(K\ge1\), and an integer \(k_0\), such that for every integer \(k\ge k_0\):

1. Some three-query relaxed locally decodable code \(C_k:\{0,1\}^k\to\Sigma^{n_k}\), with relative distance at least \(\Delta\) and decoding radius \(\rho\), has \(n_k\le Kk^a\).
2. Every three-query locally decodable code \(E:\{0,1\}^k\to\Sigma^n\) with decoding radius \(\rho\) has \(n\ge k^b/K\).

Both types of decoder have success probability at least \(2/3\), with the relaxed guarantees specified below. Queries return whole alphabet symbols. The selected constant-alphabet variant has a positive resolution in the cited 2025 work.''',
 definitions=r'''The alphabet is \(\Sigma=\{1,\ldots,s\}\) for one integer \(s\ge2\) independent of message length. A code is an injective map from \(k\)-bit messages to words of length \(n\). Its relative distance is \(\min_{x\ne x'}\Delta_H(C(x),C(x'))/n\), where \(\Delta_H\) counts coordinates with different symbols. A received word \(w\) is within decoding radius \(\rho\) of \(C(x)\) if \(\Delta_H(w,C(x))\le\rho n\); the corruption is arbitrary and may depend on the message.

A three-query decoder is a randomized procedure given the desired bit index \(i\in\{1,\ldots,k\}\) and oracle access to \(w\), which reads at most three coordinates of \(w\) on every run. Each query returns one entire symbol of \(\Sigma\). Later queries may depend on earlier answers. Equivalently, for each \(k,i\), the decoder specifies a probability distribution over the finite set of depth-at-most-three decision trees with symbol queries. No computational-time or uniform construction bound is imposed; all code maps and decoders, including nonlinear ones, are eligible.

An ordinary LDC decoder outputs a bit and, for every message \(x\), every received word within radius \(\rho\) of \(E(x)\), and every index \(i\), satisfies
\[
\Pr[D^w(i)=x_i]\ge2/3.
\]
No perfect decoding condition on uncorrupted ordinary LDCs is added to this lower-bound domain.

A relaxed LDC decoder outputs \(0\), \(1\), or a distinguished rejection symbol \(\bot\), and must satisfy all three conditions:

1. For every \(x,i\), \(\Pr[D^{C(x)}(i)=x_i]=1\).
2. For every \(x\), every \(w\) within radius \(\rho\) of \(C(x)\), and every \(i\), \(\Pr[D^w(i)\in\{x_i,\bot\}]\ge2/3\).
3. For every such \(x,w\), at least \(9k/10\) of the indices satisfy \(\Pr[D^w(i)=x_i]\ge2/3\).

The third condition means an integer number of good indices at least \(\lceil9k/10\rceil\); their set may depend on \(x,w\). All probabilities refer only to the decoder's internal randomness, with the message and corruption fixed. The distance condition \(2\rho<\Delta\) ensures uniqueness of the nearby codeword on the construction side.

All displayed constants are fixed before \(k\) varies. The lower bound quantifies over all blocklengths and all ordinary LDC maps and decoders over the same alphabet and radius. The selected exponents need only have a positive fixed gap. Restricting to a particular encoding or requiring the very same code map on the two sides would be a different question.

This card explicitly permits a nonbinary constant alphabet. Converting its symbols to binary strings can increase the number of bit queries, so the stated result does not establish a separation for three bit queries.''',
 answer_criterion='The historical target is a complete mathematically correct Lean-checked proof or refutation of the displayed constant-alphabet polynomial length separation. The cited construction and lower bound give a positive mathematical resolution; this source review does not claim that their proofs have been formalized in Lean. The resolved record is archived rather than retained as a new open benchmark.',
 why='Allowing a decoder to reject on a small set of message positions can reduce coding redundancy by a polynomial factor while retaining local recovery on most positions. The separation establishes that relaxation changes achievable parameters in the constant-alphabet symbol-query model.',
 importance=dict(score=81,method='editorial',reason='A polynomial length separation establishes a structural distinction between two central notions of local decoding; the constant-alphabet and query conventions are essential to its scope.'),
 source_formulation=dict(text='The textbook asks for a length separation between local decoding and its relaxed version, describing bit probes. This archived card selects the later constant-alphabet symbol-query variant resolved by Gur–Minzer–Weissenberg–Zheng. The alphabet extension is explicit and is not asserted equivalent to the binary formulation. The optional choice received no reply; the recommended archival specialization was announced and applied as an editorial decision.',caption='Goldreich, §13.4.4, printed pp.395–396 / PDF pp.422–423; resolved constant-alphabet variant: Corollary 1.11 of the December 2025 preprint.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Introduction to Property Testing (April 2017 manuscript)','Oded Goldreich',2017,'https://www.wisdom.weizmann.ac.il/~oded/PDF/pt-v3.pdf','§13.4.4, printed pp.395–396 / PDF pp.422–423; binary bit-probe model and polynomial length separation question'),
 ref('lower','A Near-Cubic Lower Bound for 3-Query Locally Decodable Codes from Semirandom CSP Refutation','Omar Alrabiah; Venkatesan Guruswami; Pravesh K. Kothari; Peter Manohar',2023,'https://arxiv.org/abs/2308.15403v1','Checked 29 August 2023 preprint; Appendix A Definition A.1 and Theorem A.2 p.22, extending the lower bound to general finite alphabets'),
 ref('separation','3-Query RLDCs are Strictly Stronger than 3-Query LDCs','Tom Gur; Dor Minzer; Guy Weissenberg; Kai Zhe Zheng',2025,'https://arxiv.org/abs/2512.12960v1','15 December 2025 preprint; Definition 1.4 p.4, Theorems 1.9–1.10 and Corollary 1.11 p.5, Remark 1.12 p.6; Theorem 11.3 and decoder pp.80–83'),
 ref('binary','Relaxed vs. Full Local Decodability with Few Queries: Equivalence and Separations for Linear Codes','Elena Grigorescu; Vinayak M. Kumar; Peter Manohar; Geoffrey Mon',2025,'https://arxiv.org/abs/2511.02633v2','Checked 25 November 2025 revision; introduction’s binary linear three-query equivalence; distinguished from optimal blocklength separation'),
 ],
 context_blocks=[
 block('The original question compares achievable lengths at the same query count. It is stronger than finding a particular code that has a relaxed decoder but lacks an ordinary decoder.'),
 block('The 2023 lower bound applies to arbitrary constant alphabets: for fixed decoding radius and advantage it implies blocklength at least a constant times k³/log⁶ k. It is not restricted to linear codes.','lower'),
 block('The 2025 preprint constructs three-query RLDCs of length at most k² times a fixed power of log k over a constant alphabet. Its Theorem 11.3 allows sufficiently small fixed radius and gives recovery on a fraction tending to one as the corruption fraction tends to zero, so the fixed nine-tenths success-rate convention is covered.','separation'),
 block('Together, the two bounds give fixed separated polynomial exponents after absorbing logarithmic factors. Corollary 1.11 records the resulting length separation.','separation'),
 block('The relaxed decoder in the construction first reads a symbol carrying the claimed message bit and then chooses the remaining checks. Adaptivity is permitted in this card and must not be silently excluded.','separation'),
 block('The binary linear three-query setting has an equivalence theorem. The separation paper itself highlights this obstruction and uses a constant alphabet that need not be binary. Neither result establishes the binary three-bit-query length separation.','binary'),
 ],
 progress=[progress('2017','The textbook records the conjectured length separation and the gap between available upper and lower bounds.'),progress('2023','A near-cubic three-query LDC lower bound is established, including a constant-alphabet extension.','lower'),progress('2025-11','The binary linear three-query relaxed and ordinary models are shown to have closely related parameters.','binary'),progress('2025-12','The constant-alphabet three-query RLDC construction yields a polynomial length separation.','separation')],
),[
 'Selected and explicitly recorded the constant-alphabet symbol-query archival variant; did not claim resolution of the binary bit-query formulation.',
 'Specified fixed alphabet, radius, minimum distance, polynomial exponent gap, adaptive query interface and all relaxed correctness conditions.',
 'Checked the original lower bound’s arbitrary-alphabet extension and the new construction’s small-radius recovery guarantee.',
 'Distinguished a blocklength separation from code-property separation and from the binary linear equivalence result.',
 'Individually assessed importance, retained the historical Lean acceptance criterion without claiming a Lean proof, and archived the mathematically resolved selected variant.',
],[
 'Read Goldreich §13.4.4 including the bit-probe wording and explicit polynomial separation discussion.',
 'Downloaded Alrabiah–Guruswami–Kothari–Manohar 2023 and read Appendix A Definition A.1 and Theorem A.2.',
 'Read the December 2025 preprint’s Definition 1.4, Theorems 1.9–1.10, Corollary 1.11, Remark 1.12, Theorem 11.3 and the adaptive decoder and recovery discussion.',
 'Read the November 2025 binary linear equivalence abstract and introduction; checked later source metadata through 18 September 2026 without treating a preprint as a Lean-certified theorem.',
], 'Resolved positively in the selected constant-alphabet symbol-query model by the December 2025 preprint: a near-quadratic RLDC upper bound and the near-cubic general LDC lower bound give a polynomial length separation. The statement and model match were reviewed through 18 September 2026; this is not an independent formal verification of the full proofs. The binary three-bit-query version is explicitly outside this archival disposition.',summary=[
 'Ordinary local decoding must recover every requested message bit despite a fixed fraction of corrupted code symbols.',
 'Relaxed decoding may reject at some positions while still recovering at least nine tenths of the positions reliably.',
 'The selected question asks for a polynomial blocklength advantage with three queries over the same fixed finite alphabet.',
 'The December 2025 construction and the earlier near-cubic lower bound resolve this symbol-query variant positively.',
 'The card is archived with an explicit distinction from the binary three-bit-query question.',
],archive_reason='The selected constant-alphabet three-symbol-query length separation is resolved by Gur–Minzer–Weissenberg–Zheng (December 2025), using the Alrabiah–Guruswami–Kothari–Manohar near-cubic LDC lower bound. The binary bit-query version is explicitly not claimed resolved; the archival specialization was announced as an unanswered editorial default.',expected_sha256=claim['input_sha256'],claim_token=claim['token'])
