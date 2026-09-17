"""Review the nonuniform linear gate-count question for exact multiplication."""
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7223'; claim=read_claims(ROOT)[identifier]
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
notes=[
 'Retained exact multiplication of two unsigned n-bit integers and nonuniform bounded-fan-in Boolean circuits of linear gate count.',
 'Repaired the broken output formula and the malformed formal quantifier; specified all 2n output bits, free constants and wires, and unrestricted depth and fan-out.',
 'Distinguished nonexistence of an O(n) bound from a lower bound that must hold at every sufficiently large length.',
 'Read the multiplication question in Goldreich’s available May 2007 draft, corrected the locator to that actually read version, and rechecked Viola’s 2023–2026 manuscript.',
 'Added the 2019 network-coding conditional lower bound without presenting its unproved hypothesis as an unconditional result.',
 'Preserved importance and required a complete Lean-checked proof of the full upper-bound proposition or its unconditional negation.',
]
sources=[
 'Read Goldreich, Computational Complexity: A Conceptual Perspective, May 2007 author draft, Appendix B.2.1, printed p.521, directly after Open Problem B.2, at https://www.wisdom.weizmann.ac.il/~oded/CC/r6.pdf. The passage explicitly asks whether integer multiplication has linear-size circuits. The original 2008 printed-book p.472 locator was not independently checked and is replaced by the accessible draft locator. The author’s book page confirms publication in May 2008.',
 'Read Viola, Mathematics of the Impossible, freshly retrieved author manuscript with copyright 2023–2026, Section 4.2, Definition 4.4 and Theorem 4.5, printed p.64. It explicitly retains the linear-size question. Its statement about the size of the smallest known construction is not a proved superlinear lower bound. No first-posed date of 2026 is inferred from the revision notice.',
 'Read Afshani–Freksen–Kamma–Larsen, Lower Bounds for Multiplication via Network Coding, ICALP 2019, Article 10: abstract and Introduction pp.10:1–2, Conjecture 1 and Theorem 1 p.10:2. The O(n log n) upper bound is reported there; the matching lower bound assumes the undirected k-pairs conjecture and is stated for bounded input and output degree. The review does not independently check its full proof or resolve that conjecture.',
 'Bounded primary-source checks through 17 September 2026 found no verified unconditional resolution of the selected unrestricted-depth multiplication-circuit question; the current Viola manuscript still states it explicitly.',
]
complete(identifier,dict(
 formal=r'''Do there exist a real constant \(C>0\) and an integer \(n_0\ge1\) such that, for every integer \(n\ge n_0\), some Boolean circuit with at most \(Cn\) gates computes the exact product of every pair of unsigned \(n\)-bit integers, outputting all \(2n\) product bits? The gates are binary AND and OR and unary NOT; fan-out and depth are unrestricted, and the circuit family need not be uniform.''',
 definitions=r'''The \(2n\) inputs are bits \(a_0,\ldots,a_{n-1},b_0,\ldots,b_{n-1}\), representing
\[
a=\sum_{i=0}^{n-1}a_i2^i,\qquad b=\sum_{i=0}^{n-1}b_i2^i.
\]
The ordered output bits \(c_0,\ldots,c_{2n-1}\) must satisfy
\[
\sum_{j=0}^{2n-1}c_j2^j=ab
\]
on every input, including inputs with leading zeros. A circuit is a finite directed acyclic graph whose internal gates apply the stated Boolean operations. Constant sources 0 and 1 are available. Size counts operation gates, excluding input nodes, constant sources and output wires. Wires may copy a bit to arbitrarily many gates or outputs without an additional charge. There is no randomness, approximation or restriction on depth.

Write \(M(n)\) for the minimum gate count of such a circuit at width \(n\). The proposition is \(M(n)=O(n)\). The same \(C\) bounds all sufficiently large widths, but each width may use a different circuit, with no requirement to compute the family’s descriptions. A machine instruction multiplying entire words is not one Boolean gate. Any other fixed functionally complete bounded-fan-in Boolean basis changes this linear-size question only by constant factors.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed proposition or its logical negation. A positive proof must establish one constant \(C\), a threshold \(n_0\), and the existence of correct circuits at every \(n\ge n_0\). It need not give a uniform algorithm constructing their descriptions.

A negative proof must establish
\[
\forall C>0\;\forall n_0\ge1\;\exists n\ge n_0:\ M(n)>Cn.
\]
It may give a stronger asymptotic lower bound, but such a stronger bound at every sufficiently large length is not required. A fixed linear lower bound, a bound only for restricted depth or wiring, or the failure of one multiplication construction does not settle the target. A conditional lower bound proves only its conditional statement.''',
 source_formulation=dict(text='Goldreich asks whether the exact product of two binary integers can be computed by linear-size Boolean circuits. Viola’s current author manuscript explicitly retains the same question.',caption='Goldreich, May 2007 author draft, Appendix B.2.1, printed p.521, after Open Problem B.2; Viola, §4.2, printed p.64. The explicit basis and quantifiers make this nonuniform gate-count target precise.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Computational Complexity: A Conceptual Perspective (May 2007 author draft)','Oded Goldreich',2007,'https://www.wisdom.weizmann.ac.il/~oded/CC/r6.pdf','Appendix B.2.1, printed p.521, multiplication question immediately following Open Problem B.2; published book 2008'),
 ref('viola','Mathematics of the Impossible (author manuscript)','Emanuele Viola',2026,'https://www.ccs.neu.edu/home/viola/papers/moti.pdf','§4.2, Definition 4.4 and Theorem 4.5, printed p.64; copyright 2023–2026; retrieved 17 September 2026'),
 ref('network','Lower Bounds for Multiplication via Network Coding','Peyman Afshani; Casper Freksen; Lior Kamma; Kasper G. Larsen',2019,'https://doi.org/10.4230/LIPIcs.ICALP.2019.10','Abstract and Introduction pp.10:1–2; Conjecture 1 and Theorem 1 p.10:2'),
 ],
 context_blocks=[
 block('Binary addition has linear gate complexity. Whether multiplication enjoys the same bound is an explicit candidate for separating two elementary arithmetic tasks in an unrestricted circuit model.'),
 block('The full product is required. Computing only a residue or selected output bits, or counting whole-word multiplication instructions, measures a different task.'),
 block(r'The 2019 paper reports an \(O(n\log n)\) multiplication construction and proves a matching lower bound under the undirected network-coding conjecture, in its bounded-degree circuit model. The hypothesis is essential to that lower bound.','network'),
 block('Viola’s current manuscript still asks whether linear-size multiplication is possible and establishes equivalence with linear-size squaring. The manuscript’s revision year is not the date when this longstanding question originated.','viola'),
 block('The target allows a different circuit at each input width. It therefore differs from TCS-7174, which asks about uniform running time on a multitape Turing machine.'),
 ],
 progress=[progress('2007','The available book draft explicitly states the linear-size multiplication question.'),progress('2019','A network-coding conjecture is used to obtain a conditional multiplication-circuit lower bound.','network'),progress('2026','The current author manuscript explicitly retains the linear-size question.','viola')],
),notes,sources,'No verified unconditional resolution was identified in bounded primary-source checks through 17 September 2026. Viola’s current author manuscript explicitly retains the question. The network-coding lower bound cited here is conditional, and the review does not independently validate its full proof.',summary=[
 'The input consists of two unsigned binary integers of the same width.',
 'The circuit must output every bit of their exact product on every input.',
 'The question is whether a constant times the input width always suffices in AND, OR and NOT gates.',
 'Known near-linear constructions and a conditional lower bound leave the unrestricted linear-size question unresolved in the checked sources.',
 'A complete Lean-checked proof of the circuit-family existence claim or its unconditional negation is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
