"""Connect the selected logarithmic-dimension OV and HS hypotheses."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6942'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the explicit user choice to connect TCS-6596 and TCS-6599 in logarithmic dimension, with separate uniform programs permitted for each fixed dimension constant.',
 'Defined both predicates and hypotheses in full, including packed inputs, randomized worst-case time, success on every input and the common-saving quantifiers.',
 'Preserved the separate word-length conventions of the completed cards; corrected the HS finite-input address issue in TCS-6599 without changing its eventual word length or asymptotic target.',
 'Made the requested direction OV hardness implies HS hardness explicit, equivalently a general fast-HS implication toward fast OV, with possible loss in the exponent saving.',
 'Distinguished a logical implication from a demand for one particular kind of fine-grained reduction, and recorded the limitations of the conditional NSETH barrier.',
 'Corrected the original source locator from §5 to §6, assessed importance at 86 and required a complete Lean-checked answer.',
]
sources=[
 'Read Vassilevska Williams, On Some Fine-Grained Questions in Algorithms and Complexity, author ICM 2018 survey: §2.1 p. 4 machine convention, §3 Orthogonal Vectors, and §6 pp. 15–16 Hitting Set and the unknown reverse implication. Its literal all-dimensions n^{2-epsilon} poly(d) formulation is not silently identified with the selected fixed-logarithmic-dimension formulation.',
 'Read Carmosino–Gao–Impagliazzo–Mihajlin–Paturi–Schneider, Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility, ITCS 2016 author published PDF, §5 pp. 264–265: Theorem 2, Corollary 2, Theorem 3 and §5.2 Lemma 6 and proof. The conditional obstruction concerns deterministic and zero-error fine-grained reductions, not every bounded-error argument or the unconditional logical implication.',
 'Read Johnson–Martin–Oostveen–Pandey–Paulusma–Smith–van Leeuwen, Complexity Framework for Forbidden Subgraphs I: The Framework, Algorithmica 87, 429–464, published 5 January 2025, DOI 10.1007/s00453-024-01289-2, introduction and §5 Theorem 19. It still uses separate OV and HS hypotheses for the relevant distance problems.',
 'Matched the selected quantifiers and computation conventions to completed TCS-6596 and TCS-6599. The finite-prefix HS address correction is documented separately in fix_hs_input_addresses.py and the review ledger; for each fixed c, its added input-size term is eventually inactive.',
 f'Bounded later-work searches through {DATE} found no proof or refutation of the selected implication. The checked source statements and barrier scope do not constitute independent certification of all cited proofs.',
]
status='The survey leaves the OV-to-HS hardness implication open. The user selected the logarithmic-dimension hypotheses already used in TCS-6596 and TCS-6599, rather than the survey’s literal one-algorithm all-dimensions variant. The checked later work still uses separate assumptions. Conditional barriers to restricted reductions do not refute this unrestricted logical implication.'
complete(identifier,dict(
 title='Does logarithmic-dimension OV hardness imply Hitting Set hardness?',
 criterion='reductions',question_type='yes_no',year=2026,
 formal=r'''Does the implication
\[
\mathrm{OVH}_{\log}\ \Longrightarrow\ \mathrm{HSH}_{\log}
\]
hold for the randomized logarithmic-dimension hypotheses defined below?

These are the hypotheses used in TCS-6596 and TCS-6599: the dimension is \(d=\lceil c\log_2 n\rceil\), and a refutation of either hypothesis may use a separate uniform algorithm for each fixed \(c\), with one common positive exponent saving. Equivalently, does failure of the Hitting Set hypothesis imply failure of the Orthogonal Vectors hypothesis?''',
 definitions=r'''For integers \(n\ge2\) and \(c\ge1\), let \(d=\lceil c\log_2 n\rceil\). An instance consists of two ordered lists \(A=(a^{(1)},\ldots,a^{(n)})\) and \(B=(b^{(1)},\ldots,b^{(n)})\) of vectors in \(\{0,1\}^d\). Repetitions, zero vectors and overlap between lists are allowed, with no promise on weights, intersections or number of solutions. Define ordinary integer inner products by
\[
\langle a,b\rangle=\sum_{j=1}^{d}a_jb_j.
\]
The Orthogonal Vectors predicate is
\[
\mathrm{OV}(A,B)\iff\exists r\in[n]\ \exists s\in[n]:
\langle a^{(r)},b^{(s)}\rangle=0.
\]
The Hitting Set predicate is
\[
\mathrm{HS}(A,B)\iff\exists r\in[n]\ \forall s\in[n]:
\langle a^{(r)},b^{(s)}\rangle>0.
\]
Thus the hitting set must be one supplied vector from \(A\); this is not optimization over arbitrary subsets of a universe. The predicates are not each other’s negations. Both tasks output one decision bit and need not supply a witness.

Both models use explicit packed input: headers \(n,d\), then the two lists in their given order. A vector occupies \(\lceil d/w\rceil\) words, with coordinates from least to most significant bit and unused final bits zero. In the OV model a program fixes any integer \(\lambda\ge2\) and uses
\[
w_{\mathrm{OV}}=\lambda\lceil\log_2(n+d+2)\rceil.
\]
The HS model uses the completed HS card’s fixed eventual word size, with the finite-input correction needed to address the supplied input:
\[
w_{\mathrm{HS}}=
\max\!\left\{\lceil4\log_2(n+2)\rceil,
\lceil\log_2(2nd+n+d+8)\rceil\right\}.
\]
For every fixed \(c\), the second HS term is dominated by the first for all sufficiently large \(n\). It affects only a finite prefix and does not change the asymptotic hypothesis.

A program is finite and independent of \(n\). It has word registers and memory addressed by single words, with all non-input memory initially zero. An operation may read or write a constant number of addressed words, copy, compare, branch, add, subtract or multiply modulo \(2^w\), take integer quotient or remainder with a nonzero divisor, apply bitwise Boolean operations or shift. Shifts discard overflow and return zero for shift counts at least \(w\). In the HS model division or remainder by zero may return zero; OV programs must use nonzero divisors. A fresh independent uniform \(w\)-bit random word costs one step. Compound multiword operations must be charged as their constituent operations. No arbitrary-precision or real arithmetic, input-dependent-width vector instruction, advice or oracle is available. The address universe is \(2^w\) words. Input access, preprocessing, lookup-table construction, randomness and output are all charged.

For \(P\in\{\mathrm{OV},\mathrm{HS}\}\), \(c\ge1\) and a real \(\varepsilon\in(0,1)\), write \(\operatorname{Fast}_P(c,\varepsilon)\) if there exists a uniform randomized program in its respective model which halts on every allowed input and random tape, answers \(P\) correctly with probability at least \(2/3\) on each fixed input, and has constants \(K>0\) and integer \(n_0\ge2\) such that every execution on every input of every size \(n\ge n_0\) takes at most \(Kn^{2-\varepsilon}\) operations. Smaller inputs must also be decided with the stated error and finite runtime. The program, \(K,n_0\), and the OV word multiplier may depend on \(c,\varepsilon\), but not on \(n\). The bound is not merely expected time or average-input time. Deterministic programs are included by ignoring randomness.

Define
\[
\mathrm{OVH}_{\log}\iff
\forall\varepsilon\in(0,1)\ \exists c\ge1:
\neg\operatorname{Fast}_{\mathrm{OV}}(c,\varepsilon),
\]
\[
\mathrm{HSH}_{\log}\iff
\forall\varepsilon\in(0,1)\ \exists c\ge1:
\neg\operatorname{Fast}_{\mathrm{HS}}(c,\varepsilon),
\]
where \(c\) ranges over integers. Equivalently, failure of either hypothesis means that one positive saving works for every fixed \(c\), with separate programs allowed for different \(c\). No effective compiler producing these programs from \(c\), or one program handling all dimensions, is required.

The requested implication can therefore be written as
\[
\left[\exists\varepsilon\in(0,1)\ \forall c\ge1:
\operatorname{Fast}_{\mathrm{HS}}(c,\varepsilon)\right]
\Longrightarrow
\left[\exists\delta\in(0,1)\ \forall c\ge1:
\operatorname{Fast}_{\mathrm{OV}}(c,\delta)\right].
\]
The two savings need not be equal. This is an implication between the stated propositions; it does not impose an additional requirement of a black-box, deterministic, zero-error or any other particular reduction format. The source’s literal all-dimensions bound \(n^{2-\varepsilon}\operatorname{poly}(d)\) with one algorithm is a different uniformity convention and is not used here.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the displayed implication in the stated models, or a complete Lean-checked proof of its logical negation. A negative answer must establish \(\mathrm{OVH}_{\log}\) together with \(\neg\mathrm{HSH}_{\log}\), not merely show that a chosen reduction technique fails.

A positive algorithmic implication may lose a constant amount of exponent saving, but must retain some positive saving uniformly across all fixed dimension constants. It cannot require the HS assumption to supply one algorithm uniform in \(c\), because the selected negation does not promise that. A conditional non-reducibility theorem or a separation only in a different oracle model is not an unconditional refutation of the stated logical implication.''',
 source_formulation=dict(text='The survey records the Hitting Set hardness hypothesis as implying the Orthogonal Vectors hardness hypothesis and leaves the reverse implication unknown. The user selected the fixed logarithmic-dimension formulations of the two existing atlas cards, rather than the survey’s literal all-dimensions algorithm convention.',caption='Paraphrase of the ICM 2018 survey, §6 pp. 15–16; uniformity variant explicitly selected by the user on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 importance=dict(score=86,method='editorial',reason='The implication would connect two central fine-grained hardness assumptions whose different quantifier patterns underlie diameter and radius barriers. Its unrestricted logical scope is stronger than asking whether one familiar reduction works.',basis='Individual assessment of the selected logarithmic-dimension hypotheses, their shared fixed-saving quantifiers and the checked non-reducibility context.'),
 why='Orthogonal Vectors asks for one disjoint pair, while Hitting Set asks for one candidate that intersects every set in the other list. Understanding whether their hardness assumptions imply one another would connect two different sources of fine-grained lower bounds, particularly for graph distance problems.',
 references=[
 ref('primary','On Some Fine-Grained Questions in Algorithms and Complexity','Virginia Vassilevska Williams',2018,'https://people.csail.mit.edu/virgi/eccentri.pdf','Author ICM 2018 survey; §2.1 p. 4 model; §3 OV; §6 pp. 15–16 Hitting Set and the unknown reverse implication; corrected from imported §5'),
 ref('barrier','Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility','Marco L. Carmosino; Jiawei Gao; Russell Impagliazzo; Ivan Mihajlin; Ramamohan Paturi; Stefan Schneider',2016,'https://people.csail.mit.edu/virgi/6.1420/papers/nseth.pdf','ITCS 2016; §5 pp. 264–265, Theorem 2, Corollary 2, Theorem 3 and §5.2 Lemma 6; conditional deterministic/zero-error reduction barrier'),
 ref('later','Complexity Framework for Forbidden Subgraphs I: The Framework','Matthew Johnson; Barnaby Martin; Jelle J. Oostveen; Sukanya Pandey; Daniël Paulusma; Siani Smith; Erik Jan van Leeuwen',2025,'https://link.springer.com/article/10.1007/s00453-024-01289-2','Algorithmica 87, 429–464, published 5 January 2025; introduction and §5 Theorem 19, distinct diameter and radius hypotheses'),
 ],
 context_blocks=[
 block('For OV, both selected vectors are existentially quantified. For HS, one chosen vector must work against every vector in the second list. Complementing HS changes the quantifiers again, so it is not simply the ordinary OV predicate.'),
 block('The source’s known implication points from HS hardness toward OV hardness. This card asks in the opposite direction. In terms of algorithms, the requested direction starts from a general subquadratic HS speedup and concludes a general subquadratic OV speedup.'),
 block('The conditional NSETH barrier concerns deterministic or zero-error fine-grained reductions to problems admitting short nondeterministic and co-nondeterministic verifications. It limits specified reduction methods under a hypothesis; it does not disprove every possible argument for the logical implication.','barrier'),
 block('Later forbidden-subgraph classifications still distinguish the hypotheses used for graph diameter and radius. Their applications help explain why linking the two assumptions would matter, but do not prove the link.','later'),
 ],
 progress=[
 progress('2016','The non-reducibility work gives conditional barriers for deterministic and zero-error reductions involving Hitting Set.','barrier'),
 progress('2018','The survey explicitly leaves the reverse hardness implication unknown.'),
 progress('2025-01-05','The Algorithmica framework still uses distinct OV and HS assumptions for its distance-problem results.','later'),
 ],
),notes,sources,status,summary=[
 'The question asks whether logarithmic-dimension Orthogonal Vectors hardness implies the corresponding Hitting Set hardness.',
 'Both hypotheses forbid one fixed subquadratic exponent saving that works across every fixed logarithmic dimension constant.',
 'Different uniform algorithms may be used for different constants, with bounded error on each input and worst-case running time.',
 'The equivalent algorithmic direction is from a general fast Hitting Set family to a general fast Orthogonal Vectors family, possibly losing some exponent saving.',
 'A complete Lean-checked answer must prove or refute the logical implication; conditional barriers to particular reductions do not settle it.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json'
choices=json.loads(p.read_text())
next(r for r in choices if r['id']==identifier).update(state='applied',applied_on=DATE)
p.write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
