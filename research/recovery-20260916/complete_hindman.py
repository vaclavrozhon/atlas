"""Complete the full Hindman-to-omega-jump reversal, preserving its scope."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6649'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved formal provability of omega-jump closure from unrestricted finite-color Hindman over RCA0.',
 'Expanded the base theory, comprehension and induction schemes, set parameters, coded colorings, unbounded finite sums and jump sections.',
 'Distinguished Henkin semantics and formal derivations from full second-order truth and one-instance computability.',
 'Added the July 2026 non-arithmetic cone-avoidance theorem, whose authors explicitly say that it does not settle the reversal.',
 'Replaced generic acceptance language with a complete Lean-checked proof requirement and removed speculative comparison routes.',
 'Preserved the individually assessed importance 95 and corrected source versions and locators.',
]
sources=[
 'Read Carlucci–Kołodziejczyk–Lepore–Zdanowski, arXiv:1701.06095v2 (posted 15 November 2017; manuscript cover 18 September 2018), §1 pp. 1–3, full-HT definition, lower/upper reverse-mathematical bounds and restricted-sum distinctions. Checked journal metadata: Computability 9(2), 139–153 (2020), DOI 10.3233/COM-190264, first online 12 November 2019. The inherited repository PDF now returns 403; the accessible author version supplies the exact locators.',
 'Read Liu–Patey, arXiv:2607.17666v1 (20 July 2026; cover 21 July), abstract and §1 pp. 1–3, Theorems 1.1–1.4, Main Theorem 1.5 and its following limitation paragraph. Non-arithmetic cone avoidance does not give an omega-model separation or rule out multiple applications of HT. The full forcing proof was not independently certified.',
 'Read Liu–Patey, arXiv:2606.12962v2 (2 July 2026), introduction pp. 1–4, including §1.1, the known ACA0+ upper bound for HT and the distinction between ordered variable-word and Carlson–Simpson principles.',
 'Read Le Houérou–Patey, arXiv:2607.28116v1 (30 July 2026; cover 31 July), §1 pp. 1–2 and the start of §2. Its introduction explicitly specifies RCA0 as Robinson arithmetic plus Sigma-1 induction and Delta-1 comprehension, defines omega-jump closure and distinguishes the unordered one-variable principle from HT. Its conservation result does not settle this card.',
 f'Bounded primary-source searches through {DATE} found the new one-application theorem but no proof or model separation for the full selected reversal. Conflicting descriptions of the classical computable-solution jump upper bound in old and new introductions were not used as a new card claim; their shared axiomatic ACA0+ upper bound is sufficient here.',
]
status='The checked July 2026 papers retain ACA0+ as the best known upper theory for full Hindman. The new non-arithmetic cone-avoidance result explicitly leaves equivalence by multiple applications possible. No proof or separation for RCA0+HT proving omega-jump closure was found in the bounded later-work check; the cited proofs were not independently certified.'
complete(identifier,dict(
 criterion='assumptions',question_type='yes_no',year=2026,
 formal=r'''Does the following formal provability statement hold?
\[
\mathrm{RCA}_0+\mathrm{HT}\ \vdash\
\forall X\,\exists Y\,
\bigl[Y_0=X\ \wedge\ \forall j\,(Y_{j+1}=Y_j')\bigr].
\]
Here \(\mathrm{HT}\) is Hindman's theorem for every finite coloring of the positive integers and all nonempty finite sums of distinct members of one infinite set. The conclusion says that every set has its coded \(\omega\)-jump. Equivalently, does full Hindman's theorem imply \(\mathrm{ACA}_0^+\) over \(\mathrm{RCA}_0\)?''',
 definitions=r'''Use classical two-sorted first-order logic, with number variables, set-of-number variables, equality, membership, \(0\), successor \(S\), addition and multiplication. Set equality is extensional. Models may have nonstandard numbers, and their set sort need not contain every subset of their number domain. Thus the logical semantics is Henkin semantics, not full second-order semantics.

The number axioms are Robinson arithmetic: \(Sx\ne0\), \(Sx=Sy\Rightarrow x=y\), \(x\ne0\Rightarrow\exists y\,x=Sy\), \(x+0=x\), \(x+Sy=S(x+y)\), \(x\cdot0=0\), and \(x\cdot Sy=x\cdot y+x\). Write \(1=S0\), define \(x<y\) by \(\exists z\,x+S(z)=y\), and define \(x\le y\) by \(x<y\) or \(x=y\).

A bounded arithmetic formula has only number quantifiers bounded by number terms; set membership and free set parameters are allowed, but quantified set variables are not. A \(\Sigma^0_1\) formula consists of a finite block of existential number quantifiers followed by a bounded formula; a \(\Pi^0_1\) formula uses a universal block instead. The base theory \(\mathrm{RCA}_0\) adds the universal closures of the following schemes, allowing number and set parameters. For every \(\Sigma^0_1\) formula \(\varphi(n)\), it includes
\[
[\varphi(0)\wedge\forall n(\varphi(n)\Rightarrow\varphi(Sn))]
\Rightarrow\forall n\,\varphi(n).
\]
For every \(\Sigma^0_1\) formula \(\varphi(n)\) and \(\Pi^0_1\) formula \(\psi(n)\), it includes
\[
[\forall n(\varphi(n)\leftrightarrow\psi(n))]
\Rightarrow\exists Z\,\forall n\,[n\in Z\leftrightarrow\varphi(n)],
\]
where \(Z\) is not free in either defining formula. This is \(\Delta^0_1\) comprehension.

Functions and finite sequences are represented by their usual arithmetic codes. Fix the pairing \(\langle j,e\rangle=(j+e)(j+e+1)/2+e\), whose division is exact, and a standard effective coding of finite sequences and oracle Turing computations. All statements about a coded finite computation or sequence are interpreted inside the theory. In particular, finite lengths and color counts range over its number sort, rather than only over externally standard integers.

In \(\mathrm{HT}\), quantify over every number \(k\ge1\) and every set coding the graph of a total function \(c:\mathbb N_{>0}\to\{0,\ldots,k-1\}\). There must exist a set \(H\subseteq\mathbb N_{>0}\) and a number \(i<k\) such that \(\forall b\,\exists h>b\,(h\in H)\) and
\[
c(h_0+\cdots+h_{r-1})=i
\]
for every coded strictly increasing finite sequence \(h_0<\cdots<h_{r-1}\) from \(H\) with \(r\ge1\). There is no fixed bound on \(r\), no repeated summand and no extra separation condition on the binary supports of the integers in \(H\).

Fix a standard enumeration of oracle Turing machines. For a set \(A\), the notation \(A'\) denotes the halting set
\[
\{e:\text{the }e\text{-th machine with oracle }A\text{ halts on input }e\}.
\]
The assertion \(B=A'\) is the arithmetic formula saying that membership of \(e\) in \(B\) is equivalent to existence of a coded finite halting computation using the answers supplied by \(A\). It does not assume that the jump set already exists in the model. For a single set \(Y\), define its sections by \(Y_j=\{e:\langle j,e\rangle\in Y\}\). The target requires one such \(Y\) simultaneously recording every finite jump iterate, beginning with \(Y_0=X\). The theory \(\mathrm{ACA}_0^+\) is \(\mathrm{RCA}_0\) plus this closure axiom.

The symbol \(\vdash\) means existence of a finite formal derivation in a sound and complete classical two-sorted first-order proof calculus using the stated axioms and schemes. Equivalent standard encodings of syntax and computation do not alter the question. This is an exact provability proposition, with no bound on proof length or computational resources.''',
 answer_criterion=r'''Supply a complete Lean-checked proof that a finite formal derivation of the displayed closure axiom exists from \(\mathrm{RCA}_0+\mathrm{HT}\), or a complete Lean-checked proof that no such derivation exists. For the latter, a fully verified Henkin model of \(\mathrm{RCA}_0+\mathrm{HT}\) omitting the coded \(\omega\)-jump of some set suffices, together with the soundness argument. A model with standard natural numbers is sufficient but is not required.

Proving the closure axiom in the ambient logic of Lean without verifying the restriction to the stated object theory does not prove this reversal. Neither the known \(\mathrm{ACA}_0\) lower bound, the known \(\mathrm{ACA}_0^+\) upper bound, nor a claim about one computable coloring decides it. A negative answer need not establish equivalence with \(\mathrm{ACA}_0\); any valid separation from the displayed closure axiom settles the question.''',
 source_formulation=dict(
 text='The inherited introduction places Hindman’s theorem between arithmetic comprehension and closure under the omega-th Turing jump over RCA0 and identifies its exact strength as a major open problem. The card retains the specific upper-bound reversal already selected in its previous formulation.',
 caption='Paraphrase of Carlucci–Kołodziejczyk–Lepore–Zdanowski, author version §1 p. 2 and footnotes 2–3.',citation='primary',format='editorial_paraphrase'),
 why='The problem asks how much set existence is forced by a basic theorem about finite sums. A reversal would identify unrestricted finite-sums homogeneity with closure under all finite Turing jumps recorded in one set; a separation would show that this known upper theory is stronger than necessary.',
 references=[
 ref('primary','New bounds on the strength of some restrictions of Hindman’s Theorem','Lorenzo Carlucci; Leszek Aleksander Kołodziejczyk; Francesco Lepore; Konrad Zdanowski',2020,'https://arxiv.org/abs/1701.06095v2','Computability 9(2), 139–153 (2020), DOI 10.3233/COM-190264, first online 12 November 2019; accessible author v2 posted 15 November 2017, cover 18 September 2018; §1 pp. 1–3, especially the bounds and footnotes on p. 2'),
 ref('one','Hindman’s theorem does not code the omega-jump of the empty set in one application','Lu Liu; Ludovic Patey',2026,'https://arxiv.org/abs/2607.17666v1','Version 1, posted 20 July 2026; manuscript dated 21 July; §1 pp. 1–3, Main Theorem 1.5 and its following paragraph explicitly distinguishing multiple applications'),
 ref('words','The reverse mathematics of the Ordered Variable Word theorem','Lu Liu; Ludovic Patey',2026,'https://arxiv.org/abs/2606.12962v2','Version 2, posted 2 July 2026; §1 pp. 1–4, especially §1.1 and the comparison with Hindman’s theorem'),
 ref('conservation',r'\(\Pi^0_4\) conservation of a Carlson-Simpson lemma for 1-variable words','Quentin Le Houérou; Ludovic Patey',2026,'https://arxiv.org/abs/2607.28116v1','Version 1, posted 30 July 2026; manuscript dated 31 July; §1 pp. 1–2, base-theory and jump definitions, distinction from HT, and Main Theorem 1.1'),
 ],
 context_blocks=[
 block('A finite coloring may be arbitrary. Hindman’s theorem supplies one infinite set whose single elements, pair sums, triple sums and every larger finite sum all have the same color. The theorem itself is established; this card asks which axioms its assertion forces.'),
 block(r'The classical bounds are \(\mathrm{ACA}_0^+\Rightarrow\mathrm{HT}\Rightarrow\mathrm{ACA}_0\) over \(\mathrm{RCA}_0\). Ordinary arithmetic comprehension gives each set its next Turing jump. The stronger closure principle collects all finite iterates into one set.'),
 block('Restricted sum lengths can have different strengths. The inherited paper obtains the arithmetic-comprehension lower bound already for sums of at most two elements. Such a lower bound does not supply the whole coded sequence of jumps required here.'),
 block(r'Liu and Patey prove that, for every non-arithmetical set \(C\) and every arithmetical finite coloring, some full Hindman solution \(H\) satisfies \(C\not\le_T H\). Here arithmetical means definable using only number quantifiers, and \(C\le_T H\) means computable with oracle \(H\). In particular, an individual such coloring cannot force every solution to compute \(\emptyset^{(\omega)}\).','one'),
 block('The same authors explicitly state that this does not rule out equivalence with omega-jump closure through multiple applications of Hindman’s theorem. Their result does not construct a model closed under every required instance while omitting the target jump.','one'),
 block('The July conservation paper concerns a different one-variable Carlson–Simpson principle. Its introduction distinguishes the additional block-order condition associated with Hindman’s theorem, so its weaker axiomatic bounds do not settle this card.','conservation'),
 ],
 progress=[
 progress('1987','The classical reverse-mathematical bounds place full Hindman between ACA0 and ACA0+, as recalled in the inherited introduction.'),
 progress('2017–2020','The inherited work sharpens lower bounds for bounded-length sums while retaining the full reversal gap.'),
 progress('2026-07-02','New variable-word results still distinguish their principles from the full Hindman upper-bound question.','words'),
 progress('2026-07-20','Non-arithmetic cone avoidance shows a limitation of one application; the authors explicitly leave the multiple-application reversal open.','one'),
 progress('2026-07-30','A conservation theorem for a neighboring one-variable principle preserves the distinction from full Hindman.','conservation'),
 ],
),notes,sources,status,summary=[
 'Hindman’s theorem finds an infinite set whose nonempty finite sums of distinct elements all have one color.',
 'This card asks whether that theorem forces every set’s complete sequence of finite Turing jumps over the weak base theory RCA0.',
 'The question concerns a formal implication between theories, not whether Hindman’s theorem is true in ordinary mathematics.',
 'A July 2026 result limits what one arithmetic coloring can force a solution to compute but explicitly leaves the full implication undecided.',
 'A complete Lean-checked proof must establish the stated formal derivation or its nonexistence, for example through a verified separating model.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
