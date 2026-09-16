"""Apply the selected unrestricted-message MPC join target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6380'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user choice of general MPC messages rather than the atomic-tuple model.',
 'Recovered the source’s constant-round, data-complexity regime, p^3 <= m, balanced initial distribution, receive-only load and uncharged local computation/output.',
 'Defined set-valued relations, full natural join, arbitrary fixed arities and the fractional edge-cover linear program.',
 'Expanded the soft-O target into an explicit polylogarithmic factor, consistent with the source’s body rather than lost typographic tildes in the extraction.',
 'Specified finite word encodings, unrestricted message content, explicit output and a joint high-probability correctness/load guarantee.',
 'Separated the published boat-query lower bound for tuple-based algorithms from the broader selected assertion, and checked the 2026 kappa-Join scope.',
]
sources=[
 'Read Tao, ICDT 2020 Article 25, §1.1 pp. 25:1–25:2 and §§1.2–1.3 p. 25:3. The source fixes p^3 <= m, constant-size schemas and high-probability loads.',
 'Read Hu, PODS 2021 Cover or Pack, abstract and model; checked the fuller Hu–Tao JACM 2024 Article 6 abstract, §1.1 pp. 6:3–6:4 and Theorem 1 p. 6:7.',
 'The JACM theorem explicitly quantifies over tuple-based MPC and requires receipt of all witness input tuples before output. Its rho=2 boat query has Omega(N/p^(1/3)) load, not a lower bound proved for arbitrary coded messages.',
 'Read Frisk–Fan–Koutris, arXiv:2603.10177v1 (10 March 2026), abstract, §§1–2 and §5, pp. 14–16. The upper bound uses the reduced quasi vertex-cover; the proposed matching lower bound remains a conjecture in the tuple-based model.',
 'Bounded primary-source searches through 16 September 2026 found no resolution for the user-selected general-message assertion. No independent reconstruction of the long boat-query lower-bound proof is claimed.',
]
status=('The source’s general edge-cover load target remains the selected question in unrestricted-message MPC. '
 'The 2024 JACM result refutes its atomic-tuple version, but expressly limits the lower bound to that model. '
 'The March 2026 kappa-Join preprint also states its lower-bound conjecture for tuple-based algorithms. '
 'No matching result for arbitrary message encodings was found in this bounded review.')
complete(identifier,dict(
 title='Fractional-edge-cover load for general-message parallel joins',
 criterion='resources',question_type='yes_no',
 formal=r'''For every fixed finite natural-join schema \(Q\), is there a randomized MPC algorithm computing its full join in a constant number of communication rounds with load
\[
\widetilde O_Q\!\left(\frac{m}{p^{1/\rho(Q)}}\right)
\]
on every database instance of total input size \(m\), using \(p\) machines with \(2\le p\) and \(p^3\le m\)?

Precisely, for every \(Q\) and every fixed word-size multiplier \(a\ge1\), must there exist one algorithm \(A_{Q,a}\), constants \(C_{Q,a}>0\), and integers \(R_{Q,a},d_{Q,a}\ge1\), such that it halts within \(R_{Q,a}\) rounds on every execution and, for each valid instance and initial distribution, with probability at least \(1-p^{-2}\) both outputs exactly the join and has load at most
\[
C_{Q,a}\frac{m}{p^{1/\rho(Q)}}
       \bigl(\log_2(m+2)\bigr)^{d_{Q,a}}?
\]
Messages may encode arbitrary information; they are not restricted to complete input tuples. This broader model is the explicit user choice.''',
 definitions=r'''A schema is a finite nonempty attribute set \(V\) and a finite indexed list of nonempty subsets \(e_1,\ldots,e_r\subseteq V\) with union \(V\). Attribute names, arities, relation names and \(r\) are fixed independently of \(m,p\). Schemas may have repeated subsets. An instance supplies a finite set \(R_i\) of tuples on \(e_i\) for each \(i\). A tuple on \(e_i\) assigns one domain value to each attribute in \(e_i\). Relations have set semantics; duplicate copies within a relation do not contribute multiplicity. The total input size is \(m=\sum_i|R_i|\). The output is the full relation
\[
J_Q(R_1,\ldots,R_r)
=\{t:V\to\mathrm{dom}:\ \forall i,\ t|_{e_i}\in R_i\}.
\]
Every attribute is output; there is no projection, aggregation or bag multiplicity.

The fractional edge-cover number depends only on the schema:
\[
\rho(Q)=\min\left\{\sum_{i=1}^r x_i:
x_i\ge0,\quad
\forall v\in V,\ \sum_{i:v\in e_i}x_i\ge1\right\}.
\]
It is finite and at least one. The variables \(x_i\) are real weights on relation schemas, not data values or relation sizes.

For a precise finite encoding, fix an integer \(a\ge1\) and let a machine word contain \(w=a\lceil\log_2(m+2)\rceil\) bits. Domain values are arbitrary \(w\)-bit strings, with equality of strings deciding attribute matches. A tuple occupies a constant number of words depending only on \(Q\), including its relation tag. Quantification over every fixed \(a\) gives the usual polynomial-size-domain word convention. A message word can contain any \(w\)-bit string computed by its sender; its interpretation is not restricted to a tuple, identifier, count or comparison result.

There are \(p\) machines with distinct indices \(1,\ldots,p\), each able to communicate directly with every other machine. The total input is initially partitioned without replication, with each machine holding at most \(2\lceil m/p\rceil\) tagged tuples. The algorithm must work for every such partition. All machines know \(Q,a,m,p\), the encoding and their own index, but receive no other instance-specific advice, preprocessing or statistics for free.

Each synchronous round consists of arbitrary finite local computation followed by message transmission. All messages in the transmission phase must have been prepared before receiving any message from that phase. A machine may send different messages to different recipients, and later rounds may depend on earlier messages. The load is
\[
\max_{\text{round }j,\ \text{machine }u}
\{\text{number of words received by }u\text{ in round }j\}.
\]
Headers and transmitted metadata count; a word sent to several recipients is received separately by each. Local computation, local storage, outgoing traffic as a separate metric, and local output are uncharged. There is no additional memory cap or running-time requirement, but each local phase must terminate.

Output uses a local emission operation on an explicitly written full tuple. Every output tuple must appear on at least one machine, no non-result tuple may appear on any machine, and repeated emissions of a valid tuple are allowed. A factorized representation, tuple count or emptiness bit is not the required output. A machine may derive and emit a tuple from arbitrary received information; it need not have received all its witness input tuples as intact records.

The algorithm is a single finite effective program for each fixed \(Q,a\), with independent private random bits and no advice depending on \(m,p\) or the data. Its joint correctness/load event has probability at least \(1-p^{-2}\) on every instance. All constants in the displayed bound may depend on \(Q,a\), but not on relation contents, input size, machine count or initial partition. The one-machine case is trivial and does not affect the target. The source's polynomial slack condition \(p^3\le m\) is retained rather than enlarged to all machine counts.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the quantified existence assertion. A positive answer must cover every fixed schema, arbitrary data skew and every valid initial distribution, with the required full output and simultaneous round/load guarantee. A negative answer must show that the target fails for at least one fixed schema in the general-message model. An impossibility restricted to transmitting whole tuples or to a single round is insufficient. This is a binary resource-existence question; no numerical \(1/100\) approximation convention relaxes its bound or exact join output on successful runs.''',
 source_formulation=dict(
 text='The source asks whether arbitrary join schemas admit constant-round MPC algorithms matching the fractional-edge-cover load scale, up to the polylogarithmic factors used in its algorithmic bounds. It gives such an algorithm for binary-relation schemas.',
 caption='Paraphrase of §1.2, p. 25:3, with the model of §1.1. The general-message interpretation was explicitly selected after reviewing the later tuple-based lower bound.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=77,method='editorial',
 reason='The question asks whether the central structural parameter governing worst-case join output can also govern communication for arbitrary schemas when messages may be coded.',
 basis='Individual assessment of the broad database-query class, the constant-round load target and the unresolved gap between general communication and tuple-based lower bounds.'),
 why='Parallel join processing must distribute related information so that machines can produce all compatible output tuples. The fractional edge-cover number captures a fundamental structural feature of the query. Whether it still suffices for communication with unrestricted messages separates a general information limit from limitations of algorithms that move database rows intact.',
 references=[
 ref('primary','A Simple Parallel Algorithm for Natural Joins on Binary Relations',
 'Yufei Tao',2020,'https://doi.org/10.4230/LIPIcs.ICDT.2020.25',
 'ICDT 2020, Article 25, published 11 March 2020; §1.1 pp. 25:1–25:2 and §§1.2–1.3 p. 25:3'),
 ref('boat','Parallel Acyclic Joins: Optimal Algorithms and Cyclicity Separation',
 'Xiao Hu; Yufei Tao',2024,'https://doi.org/10.1145/3633512',
 'JACM 71(1), Article 6, February 2024; abstract; §1.1 pp. 6:3–6:4; Theorem 1 p. 6:7; author copy https://cs.uwaterloo.ca/~xiaohu/papers/jacm.pdf'),
 ref('cover','Cover or Pack: New Upper and Lower Bounds for Massively Parallel Joins',
 'Xiao Hu',2021,'https://doi.org/10.1145/3452021.3458319',
 'PODS 2021, 20–25 June; preliminary cyclic-query lower bounds and acyclic-query algorithms'),
 ref('kappa','κ-Join: Combining Vertex Covers for Parallel Joins',
 'Simon Frisk; Austen Fan; Paraschos Koutris',2026,'https://arxiv.org/abs/2603.10177v1',
 'Version 1, 10 March 2026; abstract, §§1–2 and §5, pp. 14–16, including Conjecture 5.3 and the explicit tuple-based restriction'),
 ],
 context_blocks=[
 block('The source focuses on data complexity: a schema is fixed, while its input relations grow. It measures communication received by the busiest machine, and treats local processing and emission of output tuples as free. Its binary-relation result uses three rounds and the edge-cover load scale up to polylogarithmic factors.'),
 block('The source distinguishes one-round bounds from constant-round algorithms. Its one-round structural parameter can exceed the fractional edge-cover number, so a one-round lower bound does not answer the multiround question.'),
 block(r'The later JACM result gives a cyclic boat schema with \(\rho=2\) for which tuple-based algorithms need load \(\Omega(m/p^{1/3})\) in the relevant machine regime. This exceeds the proposed scale \(\widetilde O(m/p^{1/2})\). The restriction to tuple-based algorithms is explicit in both its model and theorem.','boat'),
 block('In that restricted model, input rows are atoms, and reporting an output tuple requires receiving all of its input witnesses. This card allows arbitrary encodings and inferences instead. Consequently the published restricted lower bound is not presented as a refutation of the selected target.','boat'),
 block('The same JACM article obtains the edge-cover scale for acyclic joins and distinguishes their behavior from cyclic queries in the tuple-based setting. Thus the failure of the universal tuple-based claim does not negate the established special cases.','boat'),
 block('The March 2026 κ-Join preprint gives a schema-dependent load bound based on a reduced quasi vertex-cover parameter. It conjectures matching lower bounds for tuple-based algorithms and explicitly says that general tightness remains unresolved. It does not establish the claimed edge-cover bound for arbitrary coded messages.','kappa'),
 ],
 progress=[
 progress('2020-03-11','The source states the arbitrary-schema question and gives a three-round algorithm for binary relations.'),
 progress('2021','PODS introduces stronger cyclic-query load lower bounds in the tuple-based framework.','cover'),
 progress('2024-02','The JACM article explicitly separates cyclic and acyclic behavior and states the boat-query lower bound for tuple-based MPC.','boat'),
 progress('2026-03-10','The κ-Join preprint proposes a new general schema parameter and a tuple-based tightness conjecture.','kappa'),
 progress('2026-09-16','The user selects unrestricted messages; the review fixes word, output, load and round conventions and preserves the restricted status of known lower bounds.'),
 ],
),notes,sources,status,summary=[
 'A natural join returns every assignment of values that belongs to all input relations on their shared attributes.',
 'The question asks whether every fixed schema can be processed in constant MPC rounds with load matching its fractional-edge-cover scale up to polylogarithmic factors.',
 'The selected model permits arbitrary encoded messages and requires explicit full output, with free local computation and receive-only communication cost.',
 'A published stronger lower bound rules out the analogous target for algorithms that treat rows as indivisible tuples.',
 'That restricted lower bound and the checked 2026 results do not settle the general-message assertion retained here.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
