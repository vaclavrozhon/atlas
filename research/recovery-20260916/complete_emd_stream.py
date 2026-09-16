"""Individual completion of the highlighted planar streaming EMD target."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0990'
claim=read_claims(ROOT)[identifier]
refs=[
 ref('primary','Problem 7: Estimating Earth-Mover Distance','Piotr Indyk',2006,
 'https://sublinear.info/index.php?title=Open_Problems:7',
 'Kanpur 2006 question; official offline collection dated 29 April 2017, PDF p. 10, explicitly asks constant approximation with polylogarithmic space'),
 ref('snapshot','List of Open Problems in Sublinear Algorithms','Sublinear.info contributors',2017,
 'https://sublinear.info/sublinear_info.pdf',
 'Offline copy dated 29 April 2017, PDF p. 10: Problem 7 and its sketching update; retrieved 16 September 2026'),
 ref('tradeoff','Efficient Sketches for Earth-Mover Distance, with Applications',
 'Alexandr Andoni; Khanh Do Ba; Piotr Indyk; David P. Woodruff',2009,
 'https://people.csail.mit.edu/indyk/emdStream.pdf',
 'FOCS 2009, 324–330; Theorems 1.1 and 1.2, pp. 1–2; DOI 10.1109/FOCS.2009.25'),
 ref('sketchlower','Sketching and Embedding are Equivalent for Norms',
 'Alexandr Andoni; Robert Krauthgamer; Ilya Razenshteyn',2017,
 'https://arxiv.org/abs/1411.2577v3',
 'Version 3, 15 February 2017; §1.3, Corollary 1.6 and Appendix A; STOC 2015 precursor'),
 ref('distortion2026','Lower Estimates for L1-Distortion of Transportation Cost Spaces',
 'Chris Gartland; Mikhail Ostrovskii',2026,
 'https://arxiv.org/abs/2602.14852v1',
 'Version 1, 16 February 2026; §1.1, Theorem 1.1; STOC 2026 publication DOI 10.1145/3798129.3800785'),
]
notes=[
 'Developed the original question’s expressly highlighted constant-approximation/polylogarithmic-memory existence target.',
 'Retained the planar integer grid and L1 ground metric; each point arrival contributes one unit of mass, including repeated coordinates.',
 'Specified one pass, insertions, arbitrary fixed stream order, uniform randomness, final-output success and worst-case bit space.',
 'Separated final cardinality from grid side length and quantified all constants uniformly in both.',
 'Distinguished the 2009 polynomial-grid-space tradeoff, constant-bit threshold-sketch lower bound and 2026 metric-distortion theorem.',
 'Preserved the assessed importance and category; added complete Lean acceptance and substantive source-grounded context.',
]
sources=[
 'Read the official Sublinear.info offline PDF dated 29 April 2017, p. 10: stream of red and blue points, arbitrary order, L1 norm and the highlighted constant-factor/polylog-space question. The live wiki returned HTTP 403.',
 'Read Andoni–Do Ba–Indyk–Woodruff Theorems 1.1–1.2 and their bit-space derivation: multisets, success 2/3, Delta^epsilon times polylogarithmic storage and arbitrary decoding rather than an L1 metric.',
 'Read Andoni–Krauthgamer–Razenshteyn arXiv 1411.2577v3 §1.3 and Corollary 1.6, with the stated distinction between the norm and positive weighted-set models.',
 'Read Gartland–Ostrovskii arXiv 2602.14852v1 abstract, §1.1 and Theorem 1.1; checked arXiv revision history and the STOC 2026 publisher metadata. This is an embedding-distortion theorem, not a general streaming space lower bound.',
 'A bounded primary-source search through 16 September 2026 found no constant-factor, polylogarithmic-bit-space solution or matching impossibility theorem for the stated insertion stream model.',
]
status=('The source explicitly asks for constant approximation with polylogarithmic memory. '
 'The 2009 result obtains constant approximation using a positive power of the grid side length in its space bound. '
 'The norm-sketching lower bound rules out simultaneously constant approximation and constant sketch size, while the February/June 2026 result sharpens L1 embedding distortion. '
 'Neither checked theorem rules out the allowed polylogarithmic memory for unrestricted streaming algorithms. '
 'No resolution of this target was found through 16 September 2026 in the bounded review; cited proofs were not all independently reconstructed.')
complete(identifier,dict(
 title='Constant-factor streaming approximation of planar Earth Mover Distance',
 criterion='resources',question_type='yes_no',
 formal=r'''Do there exist a uniform randomized one-pass streaming algorithm \(A\), real constants \(C\ge1\), \(B>0\), and an integer \(q\ge1\), such that for every integer \(n\ge1\), every integer \(\Delta\ge2\), and every stream consisting of \(n\) red and \(n\) blue point arrivals in \([\Delta]^2\), the algorithm uses at most
\[
B\bigl(1+\lceil\log_2(n+1)\rceil+\lceil\log_2(\Delta+1)\rceil\bigr)^q
\]
bits of working memory and returns a nonnegative rational number \(\widehat E\) satisfying
\[
\Pr\!\left[
\operatorname{EMD}(R,B_{\mathrm{pts}})
\le\widehat E
\le C\,\operatorname{EMD}(R,B_{\mathrm{pts}})
\right]\ge\frac23?
\]
Here \(R\) and \(B_{\mathrm{pts}}\) are the red and blue multisets, respectively, and
\[
\operatorname{EMD}(R,B_{\mathrm{pts}})
=\min_{\pi:\{1,\ldots,n\}\to\{1,\ldots,n\}\ \mathrm{bijection}}
\sum_{i=1}^n\|r_i-b_{\pi(i)}\|_1.
\]
The constants and algorithm are independent of \(n,\Delta\), coordinates and stream order.''',
 definitions=r'''The grid is \([\Delta]^2=\{1,\ldots,\Delta\}\times\{1,\ldots,\Delta\}\). A point has two integer coordinates, each given in binary. For points \(u=(u_1,u_2)\) and \(v=(v_1,v_2)\), the ground distance is \(\|u-v\|_1=|u_1-v_1|+|u_2-v_2|\). Each arrival contains a color and a point and inserts one unit of mass of that color. Coincident arrivals are allowed and count separately; there are no deletions. The letters \(r_i,b_i\) enumerate occurrences, so a matching pairs occurrences rather than only distinct occupied locations.

There are exactly \(2n\) arrivals, with \(n\) of each color, in an arbitrary order. The parameters \(n\) and \(\Delta\) are supplied in binary before the stream. No coordinates, matching, distance estimate or future updates are supplied in advance. The algorithm must work on every such stream, including ones with all red points before all blue points.

The Earth Mover Distance is the minimum total, unnormalised matching cost. It is an integer between zero and \(2n(\Delta-1)\). The algorithm outputs only an estimate of this value, not a matching. When the two multisets agree, the value is zero and the success condition requires output exactly zero.

Uniform means one finite randomized Turing-machine program for every parameter pair. It has a sequential read-only stream input, finite control, work tapes and access to independent unbiased random bits. It may finish processing an arrival before advancing but cannot reread an earlier arrival or the random-bit source. Every retained random seed, counter, coordinate and auxiliary data structure counts toward working memory. Its computation and final rational-output computation must fit the stated memory bound. Output is written only at the end and cannot be read back as storage.

The space bound is a worst-case bound over all times, all valid streams and all random-bit outcomes. The algorithm must finish processing and halt with an output for every valid stream and every random-bit outcome; no running-time bound beyond termination is imposed. Probability is over the algorithm’s coins for each fixed stream. The order need not be random, and cannot be chosen in response to private random bits.

The output rational is encoded by a binary numerator and positive binary denominator. The required approximation is multiplicative; no additive error depending on \(n\) or \(\Delta\) is allowed. No linearity, mergeability, independent red/blue sketches or embedding representation is imposed on the memory state.''',
 answer_criterion=r'''Give a complete mathematically correct proof checked in Lean of existence of \(A,C,B,q\) satisfying every stated condition, or of the logical negation. A positive answer must prove the uniform memory guarantee and the success probability for all parameter pairs and all valid stream orders. A negative answer must exclude every constant approximation factor and every fixed polylogarithmic space exponent in this model; ruling out one particular sketch representation or constant-size sketches alone is insufficient. The proposition is binary. The approximation factor is an existential universal constant, not a numerical quantity subject to additive \(1/100\) tolerance.''',
 why='Determine whether transportation distance can be estimated from one scan using only polylogarithmic memory, beyond the limitations of standard metric embeddings.',
 references=refs,
 source_formulation=dict(text='Is there a constant-approximation streaming algorithm for planar Earth Mover Distance using space polynomial in the logarithms of the point count and grid side length?',
 caption='Editorial paraphrase of the highlighted question in Problem 7',citation='snapshot',format='editorial_paraphrase'),
 context_blocks=[
 block('Earth Mover Distance measures the cheapest way to move one distribution of mass onto another. In this discrete model each point has unit mass, so transport becomes a minimum-cost red-blue matching. Nearby displacements can be cheap even when few coordinates match exactly.','tradeoff'),
 block('The difficulty is retaining enough global transportation information while discarding almost all arrivals. Storing all points or a full grid histogram usually exceeds the requested memory. The task only asks for the total optimum cost, which may be much easier to summarize than an actual matching.','snapshot'),
 block(r'The source records an \(O(\log\Delta)\)-approximation in polylogarithmic space. Constant approximation requires removing the growing loss without allowing memory to grow as a positive power of the grid size. The two independent parameters are the number of arrivals and the coordinate range.','snapshot'),
 block(r'The 2009 algorithm achieves an \(O(1/\varepsilon)\)-approximation with space \(\Delta^\varepsilon\log^{O(1)}(\Delta n)\) for every fixed \(0<\varepsilon<1\). Thus it gives constant approximation, but its positive power of \(\Delta\) exceeds a fixed polynomial in \(\log\Delta\). Allowing the exponent to shrink does not preserve a constant approximation under this tradeoff.','tradeoff'),
 block(r'Its decoder is more general than taking an \(\ell_1\) distance between embedded vectors. This distinction matters: a geometric lower bound on embedding distortion does not automatically lower-bound the memory required by every possible decoder or streaming state.','tradeoff'),
 block('The sketching/embedding theorem excludes constant-size, constant-approximation threshold sketches for the planar transportation norm and the related weighted-set metric. Constant-size is stricter than the polylogarithmic storage allowed here. That theorem is meaningful partial progress, without settling the displayed proposition.','sketchlower'),
 block(r'Gartland and Ostrovskii’s 2026 result raises the planar-grid \(L_1\)-distortion lower bound to \(\Omega(\log\Delta)\), matching the logarithmic upper bound for embeddings of the full transportation space. Distortion compares all distances under one map into a space with distance given by an integral of absolute differences. The result sharpens this geometric obstruction, not a space bound for the unrestricted algorithm in this card.','distortion2026'),
 block('The related independent-sketch problem gives each point set its own separately computed summary. Here the algorithm maintains one evolving state while receiving both colors. Restrictions or lower bounds for one representation model require an explicit reduction before they can be transferred to the other.','sketchlower'),
 ],
 progress=[
 progress('2004–2006','The original question records logarithmic approximation in polylogarithmic streaming space and asks for constant approximation.','snapshot'),
 progress('2009','A grid-size versus approximation tradeoff yields the first sublinear-grid-space constant approximation.','tradeoff'),
 progress('2014–2017','The sketching/embedding work rules out simultaneously constant-size and constant-approximation threshold sketches for planar EMD.','sketchlower'),
 progress('2026-02-16',r'The new preprint states a matching \(\Omega(\log\Delta)\) lower bound for planar transportation-space \(L_1\) distortion; a conference version appears at STOC 2026.','distortion2026'),
 progress('2026-09-16','The individual review specifies the original insertion stream target and separates known bounds by model.','snapshot'),
 ],
),notes,sources,status,summary=[
 'The stream contains equal numbers of red and blue unit-mass points on a planar integer grid.',
 'Earth Mover Distance is the minimum total L1 cost of matching red occurrences to blue occurrences.',
 'The question asks for one-pass constant-factor estimation with memory polynomial in the logarithms of the point count and grid side length.',
 'The guarantee must hold with constant success probability for every fixed arbitrary stream order.',
 'Known grid-space tradeoffs and embedding or constant-sketch lower bounds do not settle this unrestricted streaming target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
