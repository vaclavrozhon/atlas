"""Apply the selected parameter-dependent, quantitative linear-seed PRG target."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6692';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained Vadhan 2012 Open Problem 7.13, not the different consolidated black-box seed-exponent optimization question from 2024.',
 'Applied both explicit user choices: seed length O(ell) with security s*(epsilon/m)^O(1), and a construction allowed to depend on s and epsilon.',
 'Specified nonuniform Boolean-circuit inversion and distinguishing security, inversion of any preimage with probability at most one half, and dyadic error parameters.',
 'Made full explicitness polynomial in output length by fixing the polynomial evaluation-size exponent of the supplied function; all construction constants may depend on that fixed exponent but not the individual function or target parameters.',
 'Gave a finite-input compiler formulation, strict stretch above the linear seed threshold, a meaningful positive distinguishing-size regime, and no black-box restriction.',
 'Separated regular-function results and logarithmic improvements for arbitrary functions from the requested linear seed and quantitative security.',
 'Assessed importance individually at 90 and required a complete Lean-checked construction and security proof, or refutation.',
]
sources=[
 'Read Vadhan, Pseudorandomness (2012), Definition 7.1 p. 214, Definitions 7.3 and 7.7, Definition 7.10 p. 220, Theorem 7.11 and quantitative discussion p. 221, and Open Problem 7.13 p. 222 (PDF p. 225, also visually inspected). The inversion probability one half is in the preceding quantitative discussion. Fully explicit means polynomial time in output length. The otherwise unused constant c in the printed problem is not assigned an invented role.',
 'Read Salil Vadhan’s section of the 2024 Luca Trevisan memorial open-problems column, pp. 8–10, especially Open Problems 1–2. The seed-exponent and query-exponent questions there explicitly concern black-box constructions and do not replace the selected quantitative 2012 target.',
 'Read the publisher’s full HTML introduction, comparison table and §1.1 of Mazor–Zhang, Journal of Cryptology 37 Article 25, published 30 May 2024, DOI 10.1007/s00145-024-09507-4. The nonadaptive construction assumes regular or almost-regular functions and its table gives quadratic seed. The ePrint page is the 2021 version; a local PDF request failed with HTTP 403, so no unread local PDF theorem is claimed.',
 'Read the ECCC primary abstract and revision history for Mazor–Pass, Counting Unpredictable Bits, TR23-143 revision 3 of 17 July 2024. It reports a logarithmic-factor efficiency improvement for arbitrary one-way functions, not the linear-seed bound sought here. This review does not independently certify its proof.',
 f'Bounded primary-source searches through {DATE} found no verified resolution of the selected general quantitative linear-seed construction.',
]
complete(identifier,dict(
 title='Linear-seed pseudorandom generators from one-way functions',criterion='construction',question_type='yes_no',year=2012,
 formal=r'''Can every efficiently evaluable length-preserving one-way function be converted into a fully explicit pseudorandom generator with seed length linear in the function's input length, while retaining the following quantitative security?

Precisely, for every integer \(b\ge1\), do there exist integers \(A,K,q,r\ge1\), \(\ell_0\ge4\), and one deterministic compiler \(\mathcal B_b\) such that the following holds? Its input is a Boolean circuit \(F:\{0,1\}^{\ell}\to\{0,1\}^{\ell}\) of size at most \(\ell^b\), integers \(\ell\ge\ell_0\), \(1\le s\le2^{2\ell}\), \(m>A\ell\), and \(1\le e\le2\ell\). Write
\[
 \varepsilon=2^{-e},\qquad
 t=\left\lfloor\frac{s}{K(m2^e)^q}\right\rfloor,
\]
and require \(t\ge1\). Suppose every inversion circuit \(I\) of size at most \(s\) satisfies
\[
 \Pr_{x\leftarrow U_{\ell}}[F(I(F(x)))=F(x)]\le\frac12.
\]
The compiler must produce a circuit \(G:\{0,1\}^{d}\to\{0,1\}^{m}\), with \(1\le d\le A\ell<m\), in at most \(K(m+1)^r\) bit operations, such that every Boolean distinguishing circuit \(T\) of size at most \(t\) satisfies
\[
 \left|\Pr[T(G(U_d))=1]-\Pr[T(U_m)=1]\right|\le\varepsilon.
\]
The construction may depend on \(s\) and \(\varepsilon\): a separate generator is permitted for each requested pair of these parameters.''',
 definitions=r'''The uniform distribution \(U_j\) assigns equal probability to all binary strings of length \(j\). All random variables in the probability expressions are fresh uniform strings of their indicated lengths. The generator itself is deterministic once its seed is fixed.

Circuits are finite directed acyclic Boolean circuits with fan-in-two AND and OR gates, constants, and negations on wires. Size counts AND and OR gates; inputs, constants, fan-out and negations are free, following the source's nonuniform-time convention. A circuit is encoded by a topologically ordered gate list with binary wire indices and polarity bits, followed by the output wires. Negation chains are reduced to a polarity bit. This fixes a polynomial-length representation of a size-\(\ell^b\) function circuit. An inverter has \(\ell\) input and \(\ell\) output bits; a distinguisher has \(m\) input bits and one output bit. Their descriptions may depend arbitrarily on \(F,\ell,s,m,e\). They are not required to be generated by a uniform algorithm. Allowing additional independent random coins does not strengthen either hypothesis or conclusion, since averaging over the coins reduces the relevant bound to deterministic circuits.

Inversion succeeds on any preimage of \(F(x)\), not necessarily the particular sampled \(x\). There is no injectivity, regularity or preimage-size promise on \(F\). The hardness hypothesis is a finite-parameter implication: the compiler is not required to decide whether the supplied circuit really is hard to invert. It must halt with a well-formed generator and the stated seed and time bounds on every input satisfying the syntactic parameter conditions; pseudorandomness is required when the inversion hypothesis holds.

The exponent \(b\) fixes the polynomial evaluation bound of the underlying function. The constants and compiler may depend on \(b\), but not on the particular \(F,\ell,s,m,e\). The integers are supplied in binary and the circuit is explicitly listed. The resource bound is time on a classical multitape Turing machine, including reading the inputs and writing the entire generator circuit. Circuit evaluation consequently also takes polynomial time in \(m\). A uniformly polynomial-time family of functions supplies circuits with some fixed polynomial exponent, so this formulation gives the source's polynomial-output-time explicitness. It does not allow exponential preprocessing hidden in the generator description or polynomial dependence on \(1/\varepsilon\) when that quantity is superpolynomial in \(m\).

The chosen parameter range states the nontrivial quantitative regime. At sufficiently large \(\ell\), every function on \(\ell\)-bit inputs has an inverse-selection lookup circuit smaller than \(2^{2\ell}\); greater claimed hardness would therefore have a false premise. With that upper bound on \(s\), errors smaller than \(2^{-2\ell}\) give a displayed time bound below one. Those cases are not additional positive-time security targets. Restricting error to dyadic values loses at most a constant factor when rounding any desired error downward, which can be absorbed in \(K\). The condition \(m>A\ell\) specifies output lengths beyond the allowed linear seed threshold and ensures genuine stretch. The target is asymptotic in \(\ell\), hence the fixed initial cutoff \(\ell_0\).

Both \(s\) and \(e\) are construction inputs, not only quantities used afterwards to assess a single generator. In particular, the question does not require one generator for a fixed \(F,m\) to satisfy all security-error pairs simultaneously. The compiler may inspect and use the full description of \(F\); no restriction to black-box oracle calls is imposed. The exponent \(q\) in the security loss is fixed before the varying parameters and cannot grow with them. Thus the bound is exactly of the form \(s(\varepsilon/m)^{O(1)}\), up to a fixed multiplicative factor and integer rounding.''',
 answer_criterion=r'''Give a complete Lean-checked construction of the compilers and their constants, together with the uniform polynomial bit-time bound, linear seed bound and stated security implication for every admissible input; or give a complete Lean-checked refutation of this existence statement.

A construction only for permutations, regular functions or another proper subclass is insufficient. Mere existence of some cryptographic generator from a one-way function does not meet the seed-length and quantitative-security requirements. A lower bound restricted to black-box constructions does not refute this unrestricted target. A larger-than-linear seed bound, a security-loss exponent that grows with the input, or unbounded preprocessing is insufficient. The yes-or-no proposition and asymptotic bounds have no numerical approximation tolerance.''',
 source_formulation=dict(text='Vadhan asks whether the conversion from a general one-way function to a fully explicit pseudorandom generator can use a seed linear in the underlying input length while retaining a fixed-polynomial loss in the output length and inverse distinguishing advantage. The user selected this original quantitative target and allowed the construction to depend on the requested security and error.',caption='Paraphrase of Vadhan 2012, Open Problem 7.13 and its preceding quantitative discussion, pp. 221–222. The finite circuit encoding, positive-time parameter regime and dependence on target parameters make the selected scope explicit.',citation='primary',format='editorial_paraphrase'),
 importance=dict(score=90,method='editorial',reason='A linear seed with this quantitative security would connect strong average-case hardness to efficient derandomization without the polynomial seed overhead of the general conversion. It asks for substantially more than the foundational existence equivalence between one-way functions and cryptographic generators.',basis='Individual assessment of the quantitative 2012 question and its distinction from the later black-box efficiency frontier.'),
 why='The amount of true randomness needed by a cryptographic generator can determine whether a hardness assumption yields an efficient deterministic simulation. The question asks whether arbitrary one-way functions support the same linear seed scale available in more structured cases without discarding the quantitative hardness guarantee.',
 references=[
 ref('primary','Pseudorandomness','Salil P. Vadhan',2012,'https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf','Definitions 7.1, 7.3, 7.7 and 7.10; quantitative discussion p. 221; Open Problem 7.13 p. 222, PDF p. 225'),
 ref('consolidated_0856_primary','Open problems in memory of Luca Trevisan: pseudorandom generators from one-way functions','Salil P. Vadhan, section author',2024,'https://www.cs.umd.edu/~gasarch/open/LUCA/luca.pdf','PRG section pp. 8–10, Open Problems 1–2; separate black-box query and seed exponent questions'),
 ref('regular','Simple Constructions from (Almost) Regular One-Way Functions','Noam Mazor; Jiapeng Zhang',2024,'https://doi.org/10.1007/s00145-024-09507-4','Journal of Cryptology 37, Article 25, published 30 May 2024; Introduction comparison table and §1.1; publisher HTML checked'),
 ref('simplification','Counting Unpredictable Bits: A Simple PRG from One-way Functions','Noam Mazor; Rafael Pass',2024,'https://eccc.weizmann.ac.il/report/2023/143/','ECCC TR23-143, revision 3, 17 July 2024; primary abstract and revision history; logarithmic-factor improvement, not a verified linear-seed theorem'),
 ],
 context_blocks=[
 block('The basic existence equivalence between one-way functions and cryptographic generators does not fix the requested quantitative seed overhead. The source singles out linear seed as the missing improvement in the general conversion.'),
 block('The later memorial column poses black-box efficiency-exponent questions. Those provide context, but their model and quantitative target differ from the one retained here.','consolidated_0856_primary'),
 block('The 2024 journal construction assumes regularity or almost regularity. Its nonadaptive PRG has quadratic seed, so it does not settle the selected general-function linear-seed target.','regular'),
 block('Mazor and Pass report a simpler general construction and logarithmic-factor efficiency improvements. Their checked abstract does not claim the quantitative linear-seed conversion required here.','simplification'),
 ],
 progress=[progress('2012','The monograph formulates the quantitative linear-seed question as Open Problem 7.13.'),progress('2024-05-30','The journal version of the regular-function construction is published; its assumptions are more restrictive than this card’s.','regular'),progress('2024-07-17','The latest listed ECCC revision of Counting Unpredictable Bits reports logarithmic-factor improvements for arbitrary functions.','simplification')],
),notes,sources,'The original quantitative target was open in the 2012 source. The checked 2024 primary works concern restricted regular functions, logarithmic improvements, or a distinct black-box efficiency question. Bounded primary-source checks through 17 September 2026 found no verified construction or refutation of this selected parameter-dependent general target; this is not an independent certification of all cited security proofs.',summary=[
 'A one-way function is easy to evaluate but hard to invert even when an inverter may return any preimage.',
 'The task is to construct a pseudorandom generator whose seed has length at most a fixed constant times the input length of that function.',
 'The distinguishing security must retain the original inversion hardness up to a fixed polynomial loss in output length and inverse error.',
 'The construction must run in polynomial output time, and it may use the requested security and error as explicit parameters.',
 'A complete Lean-checked solution must handle arbitrary efficiently evaluable one-way functions rather than only permutations or regular functions.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json';a=json.loads(p.read_text());r=next(r for r in a if r['id']==identifier);r.update(state='applied',applied_on=DATE);r['secondary_choice']['state']='applied';p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
