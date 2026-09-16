"""Individual review of Oliveira's Open Problem 5.2."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1097'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
neighbor=json.loads((ROOT/'data/cards/TCS-1096.json').read_text())
claim=read_claims(ROOT)[identifier]
# Reuse the checked common language/axioms and explicit serialization, not the
# neighboring card's mathematical target, induction scheme, or P representation.
common=neighbor['definitions'].split(r'The theory \(S_2^1\) has BASIC')[0]
encoding=neighbor['definitions'].split('Here is an explicit arithmetic encoding')[1].split('For fixed positive integers')[0]
definitions=common+r'''The theory \(T_2^1\) consists of BASIC together with the universal closure over all parameter variables \(\vec a\) of
\[
\bigl(\varphi(0,\vec a)\land
\forall x(\varphi(x,\vec a)\to\varphi(x+1,\vec a))\bigr)
\longrightarrow \forall x\,\varphi(x,\vec a)
\]
for every \(\Sigma_1^b\) formula \(\varphi\). This is successor induction. It differs from the halving induction used in \(S_2^1\). No true-sentence oracle or additional complexity assumption is included among the axioms.

Let \(\theta(x)\) range over all \(\Sigma_1^b\) formulas of this language whose only free variable, if any, is \(x\). In the standard natural numbers each such formula defines an NP predicate: a yes-instance has a polynomial-length binary witness checkable in polynomial time. Conversely NP predicates on binary-encoded natural numbers have such representations. There is no requirement that \(\theta\) be a total function graph. The formula itself is part of the witness in the main question; two formulas agreeing in the standard model need not be treated as interchangeable inside a theory that has not proved their equivalence.

Here is an explicit arithmetic encoding'''+encoding+r'''For external fixed integers \(c,k\ge1\), define the closed upper-bound sentence
\[
\begin{split}
\operatorname{UB}_{c,k}[\theta]\ \equiv\
\forall N\ge1\ \exists g\ \exists C\ \bigl(&
\operatorname{Valid}(n,g,C)\land\ell(C)+\ell(g)\le c\,n^k\\
&\land\forall x\,[
\ell(x)\le n\to
(\operatorname{Eval}(N,n,g,C,x)\leftrightarrow\theta(x))]\bigr),
\end{split}
\]
where every occurrence of \(n\) abbreviates \(\ell(N)\). All auxiliary predicates have the arithmetic expansions specified above. The fixed coefficient and exponent are written as a numeral and a fixed finite product in the language. Quantification over \(N\) implements the source's Log convention: a length is supplied as the binary length of a number, not via an assumption that arbitrary exponential-size truth tables exist in the theory.

Inputs are numbers represented as zero-padded \(n\)-bit strings. The same number therefore has the same membership value at different padded lengths. The circuit can depend on \(n\), but must be correct on every input at that length. It is a deterministic nonuniform circuit, with no witnesses or random bits; NP describes the target predicate rather than the gates.

The formula, coefficient and exponent quantified in the main question are standard finite syntactic objects or standard positive integers outside the theory. For each \(k\), the same \(\theta\) must work for every \(c\). Nonprovability means absence of any finite first-order proof of the displayed upper-bound sentence. It does not mean that \(T_2^1\) proves its negation, and does not by itself assert a circuit lower bound in the standard model.

The explicit circuit description is an editorial serialization of the source's usual finite Boolean circuits. Circuit bit length and gate count are polynomially related, so the all-exponents target is unchanged after adjusting the exponent and coefficient; no exact fixed-exponent equivalence between the two size measures is asserted. The card uses the base arithmetic language rather than the conservative extension by symbols for polynomial-time functions.'''
refs=old['references']
refs[0]['locator']='arXiv:2504.04416v1, 6 April 2025; Open Problem 5.2, printed/PDF p. 17; §5.1.1 Equation (2), §4.1 Log convention, and §2.2.2'
refs += [
 ref('axioms','Bounded Arithmetic, Propositional Logic, and Complexity Theory',
     'Jan Krajíček',1995,'https://www.karlin.mff.cuni.cz/~krajicek/kniha.pdf',
     'Author-hosted scan, printed pp. 68–69 / PDF pp. 84–85; Definition 5.2.1 full BASIC list and Definition 5.2.2 successor induction'),
 ref('bko2020','Consistency of circuit lower bounds with bounded theories',
     'Jan Bydžovský; Jan Krajíček; Igor C. Oliveira',2020,
     'https://lmcs.episciences.org/6576',
     'LMCS 16(2), 12:1–12:16; Theorem 1.1(a),(b), pp. 12:4–12:5, and extensions/open problems on p. 12:7'),
 ref('learn2021','LEARN-Uniform Circuit Lower Bounds and Provability in Bounded Arithmetic',
     'Marco Carmosino; Valentine Kabanets; Antonina Kolokolova; Igor Oliveira',2021,
     'https://eccc.weizmann.ac.il/report/2021/095/',
     'ECCC TR21-095, 8 July 2021; author abstract, theory-dependent unprovability and limited-query learning results'),
 ref('recent2026','Parallelism and Adaptivity in Student-Teacher Witnessing',
     'Ondřej Ježil; Dimitrios Tsintsilidas',2026,'https://arxiv.org/abs/2602.19934',
     'arXiv:2602.19934v1, 23 February 2026; §1.2.5, Figure 2 and Theorem 1.13; no later arXiv revision displayed on review date'),
]
notes=[
 'Recovered Open Problem 5.2 and the source-wide fixed-polynomial, external-coefficient and Log formalization conventions.',
 'Specified the NP predicate as a Sigma-one-b formula, with one formula for each exponent and all positive multiplicative constants.',
 'Reused the common arithmetic vocabulary and explicit circuit serialization from reviewed TCS-1096, while replacing halving induction with successor induction and replacing total P-function graphs with NP formulas.',
 'Visually rechecked all 32 BASIC axioms and the T-two-one induction definition against the book scan.',
 'Separated known NP unprovability for S-two-one from known P-with-NP-oracle unprovability for T-two-one; preserved importance and category.',
]
sources=[
 'Read Oliveira v1 §2.2.2, §4.1, §5.1.1 Equation (2), the neighboring known-results discussion and Open Problem 5.2. Checked the arXiv revision history on 16 September 2026.',
 'Visually read Krajicek book scan printed pp. 68–69, including Definition 5.2.1 all 32 axioms and Definition 5.2.2; checked the transcription inherited from TCS-1096.',
 'Read Bydzovsky–Krajicek–Oliveira published version Theorem 1.1 and its theory/class pairs, plus the paragraph about improving the uniform class. The extra true-sentence axioms in that theorem were not silently added to the present target.',
 'Read the ECCC 2021 learning paper author abstract and the 2026 student-teacher paper §1.2.5. The latter strengthens weaker-theory results, not the NP target for T-two-one.',
 'A bounded current primary-source search on 16 September 2026 found no resolution of the exact target. No independent verification of the cited unprovability proofs or Lean formalization is claimed.',
]
status=('Oliveira v1 states the NP-versus-fixed-polynomial upper-bound unprovability question for T-two-one as Open Problem 5.2. '
        'The 2020 theorem uses NP for the weaker S-two-one theory and the larger class P with an NP oracle for T-two-one. '
        'The checked 2021 and 2026 developments do not supply the missing theory/class pair. '
        'A bounded primary-source search on 16 September 2026 found no matching resolution. '
        'The common arithmetic axioms and explicit serialization were checked; this review does not independently certify the cited proofs.')
complete(identifier,dict(
 title=r'Unprovability of NP circuit upper bounds in \(T_2^1\)',
 question_type='yes_no',
 formal=r'''Is the following unconditional statement true?
\[
\forall k\in\mathbb N_{\ge1}\ \exists\theta(x)\in\Sigma_1^b\
\forall c\in\mathbb N_{\ge1}:\qquad
T_2^1\nvdash\operatorname{UB}_{c,k}[\theta].
\]
The formula \(\theta\) represents an NP predicate. The sentence \(\operatorname{UB}_{c,k}[\theta]\), defined below, says that this predicate has deterministic Boolean circuits of description size at most \(c n^k\) on every positive input length. Thus for each fixed exponent one represented NP predicate must resist every fixed coefficient. The theory, formula class, circuit encoding and formal upper-bound sentence are all specified below.''',
 definitions=definitions,
 answer_criterion=r'''Supply a complete mathematically correct proof checked in Lean of the displayed unprovability statement or its logical negation, for the exact theory and sentence scheme. A positive result must be unconditional and obtain one \(\Sigma_1^b\) formula for each exponent that works against every coefficient. It need not give an efficient algorithm constructing these formulas. A negative result must establish that for some fixed \(k\), every \(\Sigma_1^b\) formula \(\theta(x)\) has some \(c\) for which \(T_2^1\) proves its stated upper bound. Proving a result only for a weaker theory or for a larger class of predicates does not settle this target. This is a claim about finite formal proofs, not a requirement to exhibit a standard-model circuit lower bound; numerical tolerance does not apply.''',
 references=refs,
 source_formulation=dict(text='Show that the bounded-arithmetic theory T-two-one cannot prove fixed-polynomial circuit upper bounds for every language in NP.',
     caption='Editorial paraphrase of Open Problem 5.2',citation='primary',format='editorial_paraphrase'),
 context_blocks=[
     block('A nonuniform circuit upper bound allows a different finite circuit at each input length. A proof of such an upper bound is a stronger demand on a formal theory than the mere possibility that the circuits exist. This question studies that formal provability boundary.'),
     block(r'The theory \(T_2^1\) supports successor induction with NP-definable hypotheses. The related theory \(S_2^1\) uses halving induction. These theories formalize substantial reasoning about efficient computation, but their different induction principles matter for unprovability.','axioms'),
     block(r'The 2020 result establishes nonprovability of infinitely-often circuit upper bounds for NP in \(S_2^1\), and for \(\mathrm P^{\mathrm{NP}}\) in \(T_2^1\). Here \(\mathrm P^{\mathrm{NP}}\) allows a deterministic polynomial-time algorithm to query an NP-complete oracle. Neither result gives the requested NP predicate in the stronger theory.','bko2020'),
     block('The 2026 student-teacher work strengthens some upper-bound unprovability results beyond the basic polynomial-time theory PV. Its stated upper-bound theorem still concerns a theory weaker than the one selected here and does not resolve this NP question.','recent2026'),
     block('For each represented predicate and coefficient, nonprovability of an upper-bound sentence is equivalent to consistency of its negation with the theory. Such a model may be nonstandard. This explains why an unconditional unprovability theorem can be meaningful without already proving the corresponding ordinary circuit lower bound.'),
 ],
 why='This asks whether a theory that supports induction over NP predicates can certify fixed-polynomial circuits for every NP language. An unconditional negative limitation on its proving power would strengthen a central connection between bounded arithmetic and circuit complexity, beyond the known weaker-theory or larger-language-class cases.',
 progress=[
     progress('2020-06-18','The published consistency theorem establishes the neighboring pairs: NP with S-two-one, and P-with-an-NP-oracle with T-two-one.','bko2020'),
     progress('2021-07-08','Learning-based results unify and extend several bounded-arithmetic unprovability theorems.','learn2021'),
     progress('2025-04-06','The survey singles out the NP target for T-two-one as Open Problem 5.2.'),
     progress('2026-02-23','Student-teacher witnessing strengthens some weaker-theory results; the inspected theorem does not settle the selected pair.','recent2026'),
     progress('2026-09-16','The individual review specified the full arithmetic theory, predicate syntax and circuit upper-bound sentence.'),
 ],
),notes,sources,status,summary=[
 'For each fixed polynomial exponent, the question asks for an NP predicate whose circuit upper bounds cannot be proved in T-two-one.',
 'One represented predicate must resist every fixed multiplicative coefficient at that exponent.',
 'The theory uses successor induction for NP formulas, and the card fixes its axioms and the precise circuit upper-bound sentence.',
 'Known results concern NP in a weaker theory or a larger complexity class in T-two-one.',
 'A resolution would clarify limits on formal proofs about efficient nonuniform computation without itself asserting a standard-model circuit lower bound.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
