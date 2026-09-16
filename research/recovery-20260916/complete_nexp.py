"""Individual review of Vadhan's quantitative derandomization converse."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1022'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']
refs[0]['locator']='December 2012 published version, §8.2.2, printed page 295 / PDF page 298, Open Problem 8.9'
refs += [
 ref('ikw2002','In search of an easy witness: Exponential time vs. probabilistic polynomial time',
     'Russell Impagliazzo; Valentine Kabanets; Avi Wigderson',2002,
     'https://www.cs.sfu.ca/~kabanets/Research/ikw.html',
     'JCSS 65(4), 672–694; author abstract and the NEXP versus P/poly consequence of promise derandomization'),
 ref('tighter2015','Tighter Connections between Derandomization and Circuit Lower Bounds',
     'Marco L. Carmosino; Russell Impagliazzo; Valentine Kabanets; Antonina Kolokolova',2015,
     'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2015.645',
     'APPROX/RANDOM 2015, pp. 645–658; abstract and §1 discussion of superpolynomial lower bounds and inclusion conventions'),
 ref('tell2019',r'Proving that \(\mathrm{prBPP}=\mathrm{prP}\) is as hard as proving that “almost NP” is not contained in \(\mathrm{P/poly}\)',
     'Roei Tell',2019,'https://eccc.weizmann.ac.il/report/2018/003/revision/5/download/',
     'ECCC TR18-003 revision 5, 7 November 2019, corresponding to IPL journal version; §§1.1–1.2, Theorems 1–3'),
 ref('ae2020','Almost-Everywhere Circuit Lower Bounds from Non-Trivial Derandomization',
     'Lijie Chen; Xin Lyu; Ryan Williams',2020,
     'https://eccc.weizmann.ac.il/report/2020/150/',
     'ECCC TR20-150, abstract; restricted circuit classes, stronger uniform class and almost-everywhere guarantees'),
]
notes=[
 'Recovered the exact implication in Open Problem 8.9, distinguishing it from the neighboring EXP-versus-P/poly question.',
 'Corrected the ambiguous title: nondeterminism belongs to the language class NEXP, while the lower bound is against unrestricted deterministic Boolean circuits.',
 'Defined promise classes, uniform machines, NEXP, circuit gates and size, and the infinitely-often nonmembership convention explicitly.',
 'Separated exponential-in-a-positive-power size from superpolynomial size, and compared later time/size tradeoffs and restricted-circuit results.',
 'Retained assessed importance and category and supplied self-contained acceptance, context, dated progress and five-sentence summary.',
]
sources=[
 'Read Vadhan, published December 2012 version, §8.2.2 printed pp. 293–296, in particular Open Problems 8.8–8.9 and the preceding IKW/Santhanam discussion.',
 'Read the IKW author publication page and the 2015 primary publisher abstract and introductory theorem comparison.',
 'Read Tell revision 5 §§1.1–1.2, Theorems 1–3, including the twofold composition in the nondeterministic time bound and the input-length distinction.',
 'Read ECCC TR20-150 abstract and bounded current search results; its almost-everywhere ACC^0 consequences do not give the present general-circuit NEXP conclusion.',
 'On 16 September 2026 checked relevant recent hardness-versus-randomness survey scope, including ECCC TR26-045. No resolution of the exact quantitative converse was identified; cited proofs were not independently verified.',
]
status=('Vadhan states the quantitative converse as Open Problem 8.9. The original superpolynomial consequence and the inspected later refinements do not establish the selected stretched-exponential size lower bound within NEXP. '
        'In particular, Tell’s parameterized result has a composed time bound, and restricted-circuit almost-everywhere results have different targets. '
        'A bounded primary-source review and later-work search on 16 September 2026 found no resolution of this precise implication. '
        'The input-length convention is made explicit as infinitely-often circuit hardness; no exhaustive literature or proof certification is claimed.')
complete(identifier,dict(
 title=r'\(\mathrm{NEXP}\) circuit hardness from promise derandomization',
 question_type='yes_no',
 formal=r'''Is the following implication true?
\[
\mathrm{prBPP}=\mathrm{prP}
\quad\Longrightarrow\quad
\exists L\in\mathrm{NEXP}\ \exists k\in\mathbb N_{\ge1}\
\forall N\ge1\ \exists n\ge N:
\operatorname{CC}_L(n)>2^{\,n^{1/k}}.
\]
Here \(\operatorname{CC}_L(n)\) is the minimum size of an unrestricted deterministic Boolean circuit computing membership in \(L\) on every binary input of length \(n\). One language and one positive exponent must work for infinitely many lengths. There is no restriction on circuit depth and no uniformity requirement on the circuits.''',
 definitions=r'''A language is a set \(L\subseteq\{0,1\}^*\) of finite binary strings. A promise problem is a pair \(\Pi=(\Pi_{\mathrm{yes}},\Pi_{\mathrm{no}})\) of disjoint subsets of \(\{0,1\}^*\). A machine solves it if it accepts every yes-instance and rejects every no-instance, with the appropriate probability guarantee below. It may answer arbitrarily outside their union, but its time bound holds on all inputs.

The class \(\mathrm{prP}\) consists of promise problems solved by a deterministic finite-program Turing machine in time \(C(n+1)^a\), for constants \(C,a\) depending on the machine. The class \(\mathrm{prBPP}\) allows a probabilistic machine using independent fair random bits and the same type of worst-case time bound on every random tape. Its acceptance probability is at least \(2/3\) on yes-instances and at most \(1/3\) on no-instances. These are uniform machines without advice. Equality of the two classes means that every such randomized promise problem has some deterministic polynomial-time solver; it does not require an efficient compiler transforming programs.

The class \(\mathrm{NEXP}\) is \(\bigcup_{a\ge1}\mathrm{NTIME}(2^{n^a})\), with constant factors in time allowed. A nondeterministic machine accepts a string when at least one computation branch accepts, rejects it when every branch rejects, and halts within its bound on every branch. The class here contains total languages, not promise problems and not languages equipped with an oracle.

A circuit is a finite directed acyclic graph with \(n\) labeled input nodes, Boolean constant nodes, binary AND and OR gates, unary NOT gates, and one designated output. Fan-out is unrestricted. Size counts non-input gates, including constants; it does not count wires or the binary encoding length. The circuit computes \(L\) at length \(n\) if its output equals the membership bit for every \(x\in\{0,1\}^n\). Define \(\operatorname{CC}_L(n)\) as the minimum such size. The minimum is finite because a truth-table construction always exists.

Different lengths can use unrelated circuits, with no algorithm for generating them. All circuit inputs are ordinary data bits: the circuit does not have existential witness inputs or nondeterministic gates. Nondeterminism in the question refers only to the algorithmic class containing \(L\).

The displayed lower bound uses the usual class-nonmembership convention: arbitrarily large hard input lengths suffice. It does not additionally ask for hardness at every sufficiently large length. The exponent \(1/k\) is one positive constant. This expresses the source scale \(2^{n^{\Omega(1)}}\): any fixed positive exponent can be decreased to a reciprocal integer. Polynomial-size hardness alone does not imply this conclusion. The familiar class \(\mathrm{P/poly}\), used in the context, consists of languages with polynomial-size circuit families on every length.

The antecedent is a promise-class equality. Replacing it by the equality of ordinary language classes \(\mathrm{BPP}=\mathrm P\) changes the hypothesis and is not part of this question.''',
 answer_criterion=r'''Supply a complete Lean-checked proof of the stated implication or of its negation, under the precise machine, circuit and input-length conventions above. An affirmative proof may assume only the displayed promise derandomization hypothesis and must obtain one total NEXP language with one positive stretched-exponential exponent. Superpolynomial hardness, hardness for a larger uniform class, or hardness against a restricted circuit class is insufficient. Refuting the implication requires establishing its antecedent together with failure of its conclusion in the unrelativized setting; an oracle separation or a limitation of a proof technique alone is not a refutation. No numerical tolerance alters this proposition.''',
 references=refs,
 source_formulation=dict(text='Does deterministic polynomial-time simulation of every bounded-error randomized promise problem force a language in nondeterministic exponential time to require unrestricted nonuniform Boolean circuits whose size is exponential in a positive power of input length?',
     caption='Editorial paraphrase of Open Problem 8.9',citation='primary',format='editorial_paraphrase'),
 context_blocks=[
     block('Hard functions can be used to replace randomness in algorithms. This question concerns the converse: how much nonuniform computational hardness is forced by the ability to remove randomness from all efficient promise computations? It requests a quantitative strengthening of the known superpolynomial consequence.'),
     block(r'The easy-witness work implies that derandomizing promise computation rules out \(\mathrm{NEXP}\subseteq\mathrm{P/poly}\). That is a major lower bound, but a circuit size such as \(2^{(\log n)^2}\) can already exceed every polynomial while staying below every \(2^{n^\varepsilon}\) with fixed \(\varepsilon>0\).','ikw2002'),
     block('Later refinements obtain hardness in smaller nondeterministic time classes and sharper relationships between time and circuit size. Tell’s general tradeoff includes two compositions of the size function in its time bound. Substituting a stretched-exponential size function therefore does not directly leave the resulting hard language in NEXP.','tell2019'),
     block('Whether a lower bound holds infinitely often or at almost every length is a separate issue from its size. Recent almost-everywhere results for restricted circuits strengthen that axis but do not automatically give the unrestricted-circuit conclusion required here.','ae2020'),
 ],
 why='This would sharpen a central converse in hardness versus randomness: removing efficient randomness would force a substantially stronger kind of circuit hardness than is presently supplied by the standard implication. The distinction matters because quantitative hardness controls the strength of pseudorandom constructions, and nonuniform circuits can exploit information unavailable to a single uniform program.',
 progress=[
     progress('2002','The easy-witness connection establishes a superpolynomial NEXP circuit-hardness consequence of promise derandomization.','ikw2002'),
     progress('2012','The source isolates stretched-exponential NEXP circuit hardness as a separate open quantitative converse.'),
     progress('2015','Uniform and robust variants of derandomization/lower-bound connections were strengthened.','tighter2015'),
     progress('2019','The revised time/size tradeoff reduces a threefold composition to twofold composition; this is not the desired NEXP conclusion at stretched-exponential size.','tell2019'),
     progress('2026-09-16','A bounded review retained the exact converse as source-open and made circuit type and hard-length quantifiers explicit.'),
 ],
),notes,sources,status,summary=[
 'Promise derandomization says that every efficiently randomized promise problem also has a deterministic polynomial-time solver.',
 'The question asks whether this forces a total language in NEXP to require Boolean circuits of size exponential in a positive power of input length.',
 'The circuits are ordinary deterministic nonuniform circuits, while nondeterminism belongs to the language class.',
 'Known superpolynomial lower bounds and later time-size or restricted-circuit refinements do not directly supply the requested quantitative conclusion.',
 'A resolution would sharpen a fundamental connection between eliminating randomness and proving circuit hardness.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
