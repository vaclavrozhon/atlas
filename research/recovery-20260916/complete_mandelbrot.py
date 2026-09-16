"""Complete the compact-set computability question without a time bound."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6105'
claim=read_claims(ROOT)[identifier]
notes=[
 'Replaced the truncated motivational sentence by a precise unconditional compact-set computability assertion.',
 'Defined the complex quadratic orbit, the Mandelbrot set, finite dyadic approximations and the Hausdorff metric.',
 'Specified a single ordinary total Turing program for all requested precisions, with no running-time bound or real oracle.',
 'Distinguished set approximation from exact point membership, signed-distance computability and the Blum–Shub–Smale model.',
 'Checked the 2021 author problem-session handout and the 2025 MFCS quadratic-family application; neither supplies an unconditional resolution.',
]
sources=[
 'Read Hoyrup–Nava Saucedo–Stull, ICALP 2018 Article 129, introduction pp. 129:1–129:2 and §1.1 pp. 129:2–129:3. The Mandelbrot sentence continues over the page break and is motivation, not a theorem proved by that paper.',
 'Read Hertling, Oberwolfach Computability Theory problem session, 27 April 2021, complete handout, especially the set-computability, enumerability and four-conjectures slides. It explicitly separates ordinary distance computability from the stronger two-sided version.',
 'Checked the Wiley abstract and bibliographic record of Hertling, Mathematical Logic Quarterly 51(1), 2005, pp. 5–18, DOI 10.1002/malq.200310124. The author-repository PDF was blocked by a connection check; no claim of reading that full paper is made.',
 'Read Neumann, MFCS 2025 Article 79, abstract and §5 pp. 79:15–79:16, including Theorem 22. The quadratic-family completeness result remains conditional on hyperbolicity. The full general escape-problem proof was not independently reconstructed.',
 'Bounded primary-source searches through 16 September 2026 found no unconditional algorithm or noncomputability proof for the specified compact-set target. Results about area, individual Julia sets and robust-input partial decisions were not treated as resolutions.',
]
status=('The source’s ordinary compact-set computability question remains the selected target. '
 'Hertling’s conditional result is restated in his 2021 problem-session handout, and Neumann’s 2025 quadratic-family result still invokes the hyperbolicity conjecture. '
 'No unconditional resolution was found in this bounded review; exact membership in a different real-computation model does not decide this question.')
complete(identifier,dict(
 title='Computability of the Mandelbrot set',
 criterion='decision',question_type='yes_no',
 formal=r'''Is the Mandelbrot set a computable compact subset of the plane?

Precisely, does there exist a single deterministic Turing machine \(A\) such that for every integer \(k\ge0\), \(A(k)\) halts and outputs a finite nonempty set \(S_k\) of points with dyadic rational coordinates satisfying
\[
d_H(S_k,M)\le 2^{-k},
\]
where
\[
M=\{c\in\mathbb C:\ (z_j(c))_{j\ge0}\text{ is bounded}\},\qquad
z_0(c)=0,\quad z_{j+1}(c)=z_j(c)^2+c?
\]
The assertion is unconditional and places no complexity bound on \(A\).''',
 definitions=r'''Identify \(\mathbb C\) with \(\mathbb R^2\) and use the Euclidean norm \(|\cdot|\). Boundedness of the orbit means that there exists a finite real \(R\ge0\), depending on \(c\), such that \(|z_j(c)|\le R\) for every integer \(j\ge0\). For this family, equivalently,
\[
M=\{c:\ \forall j\ge0,\ |z_j(c)|\le2\}.
\]
The set \(M\) is nonempty, closed and contained in the closed disk of radius two, hence compact.

A dyadic rational is an integer divided by a nonnegative integer power of two, encoded by signed binary integers for numerator and exponent. The output \(S_k\) is an explicit finite list of pairs of such numbers; repetitions may be removed. No bound on the list length is imposed. The accuracy input \(k\) has its ordinary finite binary encoding.

For two nonempty compact subsets \(X,Y\) of the plane, their Hausdorff distance is
\[
d_H(X,Y)=\max\left\{
\sup_{x\in X}\inf_{y\in Y}|x-y|,
\sup_{y\in Y}\inf_{x\in X}|x-y|
\right\}.
\]
Thus every reported point must be within the stated accuracy of \(M\), and every point of \(M\) must be within that accuracy of a reported point. A close picture on a selected finite grid without a proved global error guarantee is insufficient.

The machine is an ordinary algorithm operating on finite strings. It receives only \(k\); it has no oracle for complex numbers, set membership, the halting problem or a dynamical conjecture. One finite program must work at every precision, rather than a separately chosen program or advice string for each \(k\).

This is the standard computable-analysis notion for a fixed compact set. Equivalently, its distance function
\[
\operatorname{dist}(q,M)=\inf_{c\in M}|q-c|
\]
must be uniformly computable: a machine, given any rational point \(q\in\mathbb Q^2\) and \(k\ge0\), returns a rational number within \(2^{-k}\) of this distance. The equivalence uses the fixed compact bound on \(M\). The question does not ask for a total exact membership decision on arbitrary real inputs, for a polynomial running time, for the area of \(M\), or for its boundary alone.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the existence of \(A\) with the stated all-precision Hausdorff guarantee. A positive answer must prove both termination and the approximation bound for every \(k\). A negative answer must rule out all ordinary Turing programs with this behavior. An implication from an additional unproved conjecture or an undecidability result for exact real membership does not settle the assertion. This is a binary computability question: a fixed numerical tolerance such as \(1/100\) does not replace the requirement to handle every \(2^{-k}\).''',
 source_formulation=dict(
 text='The source identifies the computability of the Mandelbrot set as an unresolved question in the study of effectively approximable planar sets and relates it to complex dynamics.',
 caption='Paraphrase of the introduction, pp. 129:1–129:2, with the computable-analysis interpretation made explicit.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=90,method='editorial',
 reason='This classical question asks whether a basic explicitly defined fractal admits a single rigorous algorithm for approximation at every precision.',
 basis='Individual assessment of its central role in computable analysis, its connection with major questions in complex dynamics and the distinction between numerical visualization and effective global approximation.'),
 why='The defining iteration is simple and finite images are ubiquitous, yet those facts do not establish a uniform algorithm with certified error at every resolution. The problem tests whether the global geometry of a natural dynamical parameter set is effectively recoverable from its definition.',
 references=[
 ref('primary','Semicomputable Geometry',
 'Mathieu Hoyrup; Diego Nava Saucedo; Don M. Stull',2018,
 'https://doi.org/10.4230/LIPIcs.ICALP.2018.129',
 'ICALP 2018, Article 129; introduction pp. 129:1–129:2 and §1.1 pp. 129:2–129:3'),
 ref('hertling','Is the Mandelbrot set computable?',
 'Peter Hertling',2005,'https://doi.org/10.1002/malq.200310124',
 'Mathematical Logic Quarterly 51(1), pp. 5–18; abstract and bibliographic record checked; conditional result also checked in the author’s 2021 handout'),
 ref('handout','Is the Mandelbrot set computable?',
 'Peter Hertling',2021,'https://web.math.wisc.edu/logic/conf/OW21/questions/Hertling.pdf',
 'Oberwolfach Workshop Computability Theory, problem session, 27 April 2021; slides on computable sets, enumerability and four conjectures'),
 ref('escape','Deciding Robust Instances of an Escape Problem for Dynamical Systems in Euclidean Space',
 'Eike Neumann',2025,'https://doi.org/10.4230/LIPIcs.MFCS.2025.79',
 'MFCS 2025, Article 79, published 20 August 2025; abstract and §5 pp. 79:15–79:16, Theorem 22'),
 ],
 context_blocks=[
 block('The source uses this question as motivation for computable geometry. Its main results concern semicomputable triangles, so the existence of that paper does not constitute progress resolving the Mandelbrot question.'),
 block('The author’s later handout distinguishes one-sided information from a complete approximation algorithm: the exterior can be effectively enumerated as an open set, while the boundary and hyperbolic components satisfy other enumerability properties. These individual statements do not by themselves provide the target distance computation.','handout'),
 block(r"The relevant hyperbolicity conjecture asserts that every \(c\) in the interior of \(M\) gives a quadratic map with an attracting periodic cycle. Here a periodic point \(z\) of period \(r\) is attracting when \(|(f_c^r)'(z)|<1\), for \(f_c(z)=z^2+c\). Hertling shows that this conjecture would imply computability, including a stronger two-sided distance notion. The conjecture is not an assumption of this card.",'handout'),
 block('The 2021 handout lists ordinary distance computability separately from the stronger two-sided assertion. Accordingly this card asks only for the ordinary compact-set approximation target and does not add a requirement to recognize the entire interior.','handout'),
 block('The 2025 escape-problem paper supplies an alternative conditional result for the quadratic family. Its Theorem 22 identifies the robust instances reached by its reduction and retains the hyperbolicity condition; it does not claim an unconditional approximation algorithm for the whole Mandelbrot set.','escape'),
 block('The 2025 paper also distinguishes the bit-based approximation question from exact membership in the Blum–Shub–Smale real-computation model. A negative result for the latter is not a negative answer to the finite Hausdorff-approximation question specified here.','escape'),
 ],
 progress=[
 progress('2005','Hertling publishes computability results for associated sets and a conditional positive result under hyperbolicity.','hertling'),
 progress('2018','The source records Mandelbrot computability as an open motivating problem.'),
 progress('2021-04-27','Hertling’s problem-session handout explicitly separates ordinary and two-sided distance computability.','handout'),
 progress('2025-08-20','The MFCS escape-problem application retains a hyperbolicity condition for the quadratic family.','escape'),
 progress('2026-09-16','The review fixes an unconditional, all-precision Hausdorff target and finds no unconditional resolution in the checked primary sources.'),
 ],
),notes,sources,status,summary=[
 'The Mandelbrot set consists of complex parameters whose quadratic iteration starting at zero remains bounded.',
 'The question asks for one ordinary program that approximates the entire set to every requested accuracy.',
 'Its output must be a finite set of dyadic points with a proved Hausdorff error bound, and no running-time bound is imposed.',
 'Known positive results depend on a hyperbolicity conjecture, including the checked 2025 application to escape problems.',
 'The selected unconditional approximation question differs from exact real membership, computing area and producing images without certified error.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
