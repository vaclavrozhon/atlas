"""Fix the visualization coordinates and bounded-alphabet quantifiers."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0178';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Bounded-alphabet approximation of the β = 0 entropy face',
 status='source_open',criterion='construction',question_type='yes_no',
 formal=r'''Does there exist an integer \(K\ge2\) such that every point \(z\) on the face
\[
F=\{(\alpha,\beta,\gamma,\delta)\in S:\beta=0\}
\]
can be approximated arbitrarily closely by points of the relative interior of \(S\) obtained from normalized entropy vectors of four jointly distributed variables, each taking at most \(K\) values? The body \(S\), its coordinates and normalization are defined below. One common \(K\) must work for the entire face and for every positive accuracy.''',
 definitions=r'''For a joint distribution of four finite-valued variables \(A,B,C,D\), its entropy vector is the 15-tuple \(h=(H(X_U))_{\varnothing\ne U\subseteq\{A,B,C,D\}}\). Entropy is in bits, \(H(Y)=-\sum_y p_y\log_2p_y\), with \(0\log_2 0=0\). All joint probabilities may be arbitrary nonnegative reals. Let \(\Gamma_4^*\subseteq\mathbb R^{15}\) be the set of these entropy vectors over all finite alphabets, and let \(\overline{\Gamma_4^*}\) be its Euclidean closure.

For any real vector \(h\), use the linear expressions
\[
H(U\mid V)=H(UV)-H(V),\quad
I(U;V\mid W)=H(UW)+H(VW)-H(W)-H(UVW),
\]
where juxtaposition denotes union of coordinate sets and \(H(\varnothing)=0\); write \(I(U;V)=I(U;V\mid\varnothing)\). Define the following linear coordinate map \(N:\mathbb R^{15}\to\mathbb R^{15}\), in this exact order:
\[
N(h)=\bigl(J,I(A;B\mid C),I(A;C\mid B),I(B;C\mid A),
I(A;B\mid D),I(A;D\mid B),I(B;D\mid A),
I(C;D\mid A),I(C;D\mid B),I(C;D),I(A;B\mid CD),
H(A\mid BCD),H(B\mid ACD),H(C\mid ABD),H(D\mid ABC)\bigr),
\]
where \(J=I(A;B\mid C)+I(A;B\mid D)+I(C;D)-I(A;B)\). This is an invertible linear coordinate map; its expressions also apply to vectors that are only almost entropic.

For \(z=(\alpha,\beta,\gamma,\delta)\), put
\[
v(z)=(-\alpha,2\beta,\delta,\delta,2\beta,\delta,\delta,\gamma,\gamma,0,0,0,0,0,0).
\]
The body in the question is exactly
\[
S=\{z\in\mathbb R_{\ge0}^4:\alpha+\beta+\gamma+\delta=1,
\ N^{-1}(v(z))\in\overline{\Gamma_4^*}\}.
\]
These are the coordinates of the source's visualization. In particular, its \(\beta=0\) requires both \(I(A;B\mid C)=0\) and \(I(A;B\mid D)=0\) in the core vector. Its labels must not be replaced by similarly named coordinates in another presentation. This normalization makes the joint-entropy coordinate of \(N^{-1}(v(z))\) equal to 4.

The relative interior \(\operatorname{relint}S\) means the interior in the affine hull of \(S\), using the Euclidean topology. Explicitly, \(y\in\operatorname{relint}S\) if some open ball around \(y\), intersected with that affine hull, is contained in \(S\). Distances in the question use the Euclidean norm on \(\mathbb R^4\).

For an integer \(K\ge2\), let \(E_K\) consist of those \(y\in S\) for which there is a joint probability table on \(\{1,\ldots,K\}^4\), with entropy vector \(h\) and \(h(ABCD)>0\), such that
\[
N\!\left(\frac{4h}{h(ABCD)}\right)=v(y).
\]
Unused alphabet symbols and zero-probability atoms are allowed. Thus normalization rescales the actual entropy vector along its ray; it does not require the unscaled distribution to have exactly four bits of joint entropy. The equalities defining the core must hold exactly. Applying a projection, convolution or other entropy-region transformation to a bounded-alphabet table does not alone establish membership in \(E_K\).

The assertion is precisely
\[
\exists K\ge2\ \forall z\in F\ \forall\varepsilon>0\ \exists y\in E_K\cap\operatorname{relint}S:
\quad\|y-z\|_2<\varepsilon.
\]
The distributions may depend on \(z\) and \(\varepsilon\), but \(K\) may not. There is no computability, running-time or rational-probability requirement. Allowing \(K\) to depend on the point or the accuracy is a different question.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of the displayed quantified assertion. A positive answer must establish one finite alphabet bound for the whole face. A negative answer must show that every proposed bound fails for some face point and some positive accuracy. Numerical gaps in a sampled visualization alone prove neither direction.',
 why='This question tests whether the boundary geometry of a four-variable entropy region can be captured uniformly with bounded finite probabilistic models. It distinguishes genuine restrictions on alphabet size from gaps created by numerical exploration.',
 source_formulation=dict(text='Problem (2.2) asks whether the β = 0 face in Csirmaz’s visualization can be approximated from the interior with bounded alphabets. This card selects a common bound for the entire face, uses entropy rays normalized by joint entropy, and interprets interior as relative interior of the specified body. The optional uniform-versus-pointwise choice received no reply; the announced recommendation is an editorial choice, not a user confirmation.',caption='Dagstuhl Seminar 22301, §4 Problem (2.2), printed p.199 / standalone PDF p.20, with reference [4] fixing the visualization coordinates.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Algorithmic Aspects of Information Theory (Dagstuhl Seminar 22301)','Phokion G. Kolaitis; Andrej E. Romashchenko; Milan Studený; Dan Suciu, editors; problem posed by László Csirmaz',2023,'https://doi.org/10.4230/DagRep.12.7.180','July 2022 seminar; report published 3 February 2023; §4 Problem (2.2), printed p.199 / standalone PDF p.20; reference [4]'),
 ref('visual','Visualizing the entropy region','László Csirmaz',2022,'https://github.com/lcsirmaz/entropy-rules/blob/089f64bb/visual/DESCRIPTION.md','Pinned revision referenced by the seminar; natural-coordinate table, “A 3-dimensional cross-section,” equation (1), and total-entropy normalization H = 4'),
 ref('convolution','Entropy region and convolution','František Matúš; László Csirmaz',2013,'https://arxiv.org/abs/1310.5957v1','Checked 22 October 2013 preprint; §7 symmetrization and barycentric coordinates, pp.13–15; bounded-support numerical experiment pp.14–15; later journal version 2016'),
 ],
 context_blocks=[
 block('The seminar reports entropic points on the face with at most eight states per variable and an apparent gap to the interior in numerical experiments. It asks whether bounded alphabet size obstructs approaching the face.'),
 block('The visualization defines a symmetric core by setting six natural coordinates to zero and equating several others. Its β coordinate is attached to I(A;B | C) and I(A;B | D); the exact displayed coordinate order removes ambiguity with the article’s notation.','visual'),
 block('The core is a closed convex cone inside the almost-entropic region, and fixing joint entropy gives the three-dimensional body. Almost-entropic closure membership must be distinguished from realization by a particular bounded-alphabet distribution.','visual'),
 block('The article’s numerical experiment starts with finite probability tables and then applies entropy-region transformations and symmetrization before normalizing. Those operations justify almost-entropic core points but do not assert preservation of the original alphabet size or exact entropic realization of every transformed point.','convolution'),
 block('The selected uniform quantifiers require one alphabet bound for all points on the face. This is explicitly stronger than allowing a separate bound for each target point and is the recorded editorial interpretation of the broad wording.'),
 ],
 progress=[progress('2013','The checked preprint defines and numerically investigates a symmetrized three-dimensional slice of the almost-entropic region.','convolution'),progress('2022','The seminar records the bounded-alphabet approximation question and directs readers to the visualization’s coordinates.')],
),[
 'Recovered all fifteen natural coordinates from the pinned visualization, correcting the potential interchange of β labels across sources.',
 'Specified the almost-entropic closure, normalized body, exact core equalities, relative interior and Euclidean accuracy.',
 'Adopted the announced uniform alphabet-bound default and recorded it as editorial; normalized actual entropy rays rather than requiring an artificial exact unscaled entropy.',
 'Distinguished bounded-alphabet entropy vectors from transformed almost-entropic numerical points.',
 'Preserved assessed importance and required a complete Lean-checked proof or refutation with the correct uniform quantifier order.',
],[
 'Read Dagstuhl Problem (2.2) with the preceding definition of the slice and reference [4].',
 'Fetched and read the pinned visualization DESCRIPTION.md, including every natural coordinate and the normalization formula.',
 'Read §7 of the 2013 convolution preprint and its account of transformed samples from distributions with at most eleven values per variable.',
 'Bounded searches through 18 September 2026 found no matching resolution; this is a source-open designation with explicit interpretation limits, not independent certification of all literature.',
], 'The 2022 report poses the bounded-alphabet approximation problem as open. No resolution matching the selected uniform, normalized-realization formulation was found in the bounded source review through 18 September 2026. The report does not explicitly settle uniform versus pointwise alphabet bounds; the selected quantifiers and normalization are documented editorial choices. Numerical pictures and almost-entropic transformations are not treated as certificates of bounded-alphabet approximation.',summary=[
 'A symmetric three-dimensional slice of the four-variable almost-entropic region has a distinguished face labeled β = 0.',
 'The question asks whether every point of that face is a limit of interior points represented by normalized entropy vectors of bounded-alphabet distributions.',
 'One finite bound on the alphabet size must work for the whole face and for every requested accuracy.',
 'The source reports small-alphabet points on the face but an apparent gap in numerical exploration of the interior.',
 'The card fixes the visualization’s coordinate convention and distinguishes actual entropy realizations from transformed almost-entropic samples.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
