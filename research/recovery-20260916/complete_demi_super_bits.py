"""Specify Rudich's existential strengthening with signed nondeterministic advantage."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-1956'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the unnumbered open problem after Conjecture 21; Conjecture 21 itself asks only for existence of demi-bits.',
 'Defined one-bit-stretch nonuniform polynomial-size generators and nondeterministic circuits, including witness-input size.',
 'Preserved the signed uniform-minus-generated advantage in super-hardness; an absolute-value definition would be trivially defeated by range membership.',
 'Retained exponential-in-a-positive-power hardness at every sufficiently large length for both primitives, with independently quantified exponents.',
 'Kept the existential implication rather than requiring the same generator or an efficient uniform transformation.',
 'Checked the 2026 range-avoidance work and its explicitly stronger stretch assumption; assessed the question’s importance individually.',
]
sources=[
 'Read Tzameret–Zhang, ITCS 2024 Article 95: introduction pp. 3–4, §3.1 size convention p. 11, §3.2 Definition 8 p. 12, §3.4 Definition 11 p. 13, §3.5 Definitions 15–16 and 19–20 pp. 14–15, the unnumbered open problem after Conjecture 21 p. 15, and §3.6 distinguishing infinitely-often security. The source attributes the question to Rudich 1997.',
 'Read the same source’s introduction and §3.5 discussion of stretching: demi-bit stretching to sublinear additional output does not yield super-hardness, a pseudorandom function generator, or the asserted natural-proof consequence without further work.',
 'Read Ren–Wang–Zhong, ITCS 2026 Article 111, published 23 January 2026: abstract, §1.1 pp. 2–3 including footnote 2, §1.2 and §1.3 pp. 3–5 including the 10n-output main theorem. The paper assumes larger-stretch demi-bit generators, notes that generic stretching is only partially understood, and derives range-avoidance/proof-complexity consequences, not super-bits.',
 f'Bounded primary-source searches for demi-bit to super-bit implications through {DATE} found the original open question and the 2026 consequences, without a claimed resolution. Cited proofs were not independently certified.',
]
status=('The 2024 paper explicitly leaves the demi-bit-to-super-bit implication open. Its stretching theorem preserves the weaker demi-hardness notion. The checked ITCS 2026 work assumes larger stretch and derives different consequences. No resolution of the existential implication was found in the bounded later-work check.')
complete(identifier,dict(
 criterion='reductions',question_type='yes_no',
 formal=r'''Does existence of a demi-bit imply existence of a super-bit?

Let \(\mathcal G\) be the set of nonuniform polynomial-size Boolean circuit families \(G=(G_n)_{n\ge1}\) with
\[
G_n:\{0,1\}^{n}\longrightarrow\{0,1\}^{n+1}.
\]
For a nondeterministic circuit \(D\) on \(n+1\) ordinary input bits, write
\[
\alpha(D)=\Pr_{y\sim U_{n+1}}[D(y)=1],\qquad
\beta(D,G_n)=\Pr_{x\sim U_n}[D(G_n(x))=1].
\]
Define the two positive-integer hardness measures
\[
H_{\mathrm{dh}}(G_n)=\min\{s:\exists D,\ |D|\le s,\ 
\alpha(D)\ge1/s,\ \beta(D,G_n)=0\},
\]
\[
H_{\mathrm{nh}}(G_n)=\min\{s:\exists D,\ |D|\le s,\ 
\alpha(D)-\beta(D,G_n)\ge1/s\}.
\]
Is the following implication true?
\[
\bigl[\exists G\in\mathcal G\ \exists\varepsilon>0\ \exists N\
\forall n\ge N:\ H_{\mathrm{dh}}(G_n)\ge2^{n^\varepsilon}\bigr]
\ \Longrightarrow\
\bigl[\exists H\in\mathcal G\ \exists\delta>0\ \exists N'\
\forall n\ge N':\ H_{\mathrm{nh}}(H_n)\ge2^{n^\delta}\bigr].
\]
The premise defines a demi-bit and the conclusion a super-bit. The two families, hardness exponents and cutoffs may differ.''',
 definitions=r'''For \(m\ge1\), \(U_m\) is the uniform distribution on all binary strings of length \(m\). The seed is sampled uniformly even if several seeds give the same output; generated outputs therefore have their actual multiplicities, not a uniform distribution on the range.

A Boolean circuit is a finite directed acyclic graph with input nodes, constant \(0\) and \(1\) nodes, unary NOT gates and fan-in-two AND and OR gates. Fan-out is unrestricted. Outputs are designated nodes. Size counts all nodes, including ordinary input nodes, witness input nodes and constants; designating an output does not create an extra node. This fixes a bounded-fan-in basis for the source's gate-count convention.

A family belongs to \(\mathcal G\) if there are fixed integers \(C\ge1,d\ge0\) such that every \(G_n\) is a deterministic circuit of size at most \(C(n+1)^d\), with exactly \(n\) ordinary inputs and \(n+1\) output bits. Different lengths may have unrelated circuit descriptions. No algorithm generating these descriptions is required, so a polynomial-time-uniform construction is a stronger optional conclusion.

A nondeterministic circuit is represented by a deterministic single-output circuit \(D_0(y,z)\), with \(n+1\) ordinary input bits \(y\) and some finite number \(w\ge0\) of witness bits \(z\). Its acceptance predicate is
\[
D(y)=1\quad\Longleftrightarrow\quad
\exists z\in\{0,1\}^{w}\ D_0(y,z)=1.
\]
The witness is existential, not random; there is no averaging over witnesses. The size \(|D|\) is the size of \(D_0\), including all its witness inputs. The adversary may depend arbitrarily on \(n\) and on the generator. There are no oracle gates or restrictions on its depth.

Each minimum ranges over integers \(s\ge1\) and all such finite circuits. It exists: the range has at most \(2^n\) elements, so its complement in \(\{0,1\}^{n+1}\) has density at least one half and is recognized by some finite Boolean circuit. Taking a sufficiently large \(s\) makes that circuit an admissible witness for either minimum.

A demi-hardness witness must reject every generated string, while accepting at least a \(1/s\) fraction of uniformly random strings. A super-hardness witness may accept generated strings, but must accept uniform strings more often by at least \(1/s\). The order of subtraction is part of the definition. There is no absolute value and no symmetric requirement on the opposite difference. Nondeterministic acceptance is not closed under complementing the circuit's output gate.

The lower bound \(2^{n^\varepsilon}\), for some fixed positive real \(\varepsilon\), is required for every sufficiently large \(n\), with one exponent for the whole family. Neither hardness only against polynomial-size circuits nor hardness at merely infinitely many lengths is the premise in this question. The card asks about existence of the two families; it does not demand that every demi-bit already be a super-bit or impose a black-box or uniform conversion procedure.''',
 answer_criterion=r'''Supply a complete Lean-checked proof or refutation of the displayed existential implication. An affirmative answer must obtain a polynomial-size one-bit-stretch super-bit family with some positive hardness exponent from the existence of a demi-bit family as defined. A negative answer must establish existence of a demi-bit and nonexistence of every super-bit family in the same ordinary model. Showing only that one particular demi-bit is not itself a super-bit, or proving a limitation of one conversion method, is insufficient. The proposition is binary; numerical \(1/100\) tolerance does not change the signed advantage, zero-error condition or eventual hardness bounds.''',
 source_formulation=dict(text='After defining demi-hardness and the demi-bit existence conjecture, the source asks whether the existence of this weaker primitive implies existence of a super-bit.',
 caption='Paraphrase of the unnumbered open problem immediately after Conjecture 21, §3.5 p. 95:15 of ITCS 2024 Article 95; Definitions 15–16 and 19–20 give the security parameters.',
 citation='primary',format='editorial_paraphrase'),
 why='The problem compares two basic notions of pseudorandomness against nondeterministic tests. Resolving the implication would determine whether a hitting requirement with no false positives on generated strings can yield the stronger distributional guarantee used in nondeterministic natural-proof barriers. It connects foundational generator assumptions, circuit lower-bound methods and proof complexity, rather than only improving a parameter in one construction.',
 importance=dict(score=85,method='editorial',reason='A long-standing implication between foundational nondeterministic pseudorandomness primitives, with consequences for natural-proof barriers and proof-complexity generators; generic stretching still falls short of the requested security upgrade.',assessed_on=DATE,basis='Individual review of the ITCS 2024 definitions and open problem, together with the assumptions and scope of ITCS 2026 consequences.'),
 references=[
 ref('primary','Stretching Demi-Bits and Nondeterministic-Secure Pseudorandomness','Iddo Tzameret; Lu-Ming Zhang',2024,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2024.95',
 '§3.1–3.5 pp. 95:11–95:15; Definitions 8, 11, 15–16, 19–20; unnumbered open problem after Conjecture 21 on p. 95:15; §3.6'),
 ref('later','Hardness of Range Avoidance and Proof Complexity Generators from Demi-Bits','Hanlin Ren; Yichuan Wang; Yan Zhong',2026,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.111',
 'Published 23 January 2026; §1.1 pp. 111:2–111:3, footnote 2; §1.2 and §1.3 pp. 111:3–111:5, larger-stretch main theorem'),
 ],
 context_blocks=[
 block(r'Every demi-hardness distinguisher also witnesses super-hardness, so \(H_{\mathrm{nh}}(G_n)\le H_{\mathrm{dh}}(G_n)\). Consequently every super-bit is a demi-bit. The question asks for the reverse implication at the level of existence.'),
 block('With the subtraction reversed, a nondeterministic test could guess a seed and check whether the input is its generated output. It would accept all generated strings and at most half of uniformly random strings. This explains why standard absolute-value indistinguishability is not the target.'),
 block('The 2024 stretching theorem increases the number of demi-bits by a sublinear amount. Increasing output length while retaining demi-hardness does not establish the super-hardness guarantee.'),
 block('The source relates super-bits to pseudorandom function generators secure against nondeterministic adversaries and to barriers for nondeterministic natural properties. Obtaining these consequences directly from demi-bits remains a separate question.'),
 block('The 2026 range-avoidance theorem uses demi-bit generators with larger stretch and superpolynomial hardness. Its introduction explicitly distinguishes the stretch it assumes from the generic stretching available from a single demi-bit.','later'),
 ],
 progress=[
 progress('1997','Rudich introduces the two primitives and their comparison, as recorded in the 2024 source.'),
 progress('2024','Tzameret and Zhang prove generic sublinear demi-bit stretching while explicitly retaining the super-bit implication as an open question.'),
 progress('2026-01-23','Ren, Wang and Zhong derive range-avoidance and proof-complexity consequences under larger-stretch demi-bit assumptions.','later'),
 progress(DATE,'The review fixes the signed advantage, nonuniformity, hardness scale and existential implication; no general resolution is found in the bounded check.'),
 ],
),notes,sources,status,summary=[
 'A demi-bit is a polynomial-size generator that adds one output bit and resists nondeterministic tests rejecting every generated output.',
 'A super-bit also resists tests that accept generated outputs but accept uniformly random strings noticeably more often.',
 'Both notions here require hardness at least exponential in a fixed positive power of the seed length for every sufficiently large length.',
 'The question asks whether existence of the weaker generator guarantees existence of the stronger one, allowing different nonuniform circuit families.',
 'Known stretching and range-avoidance results give consequences of demi-bits without supplying this security upgrade.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
