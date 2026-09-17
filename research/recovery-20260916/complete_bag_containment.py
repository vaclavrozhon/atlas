"""Complete plain CQ containment over finite natural-number bag databases."""
import sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-0492';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the decidability question for two unrestricted plain conjunctive queries over bag-valued input relations and bag-valued output.',
 'Specified effective input encodings, finite relational signatures, unique-name constants, safe variable syntax and unrestricted finite domains and natural multiplicities.',
 'Made repeated atom occurrences separate product factors, with finite sums over assignments, repeated head variables and Boolean-query/empty-product conventions.',
 'Required one total uniform decision algorithm without a time bound, or an unconditional undecidability proof, fully checked in Lean.',
 'Read the 2025 join-on-free semantics and reduction statements, the CQ-versus-UCQ revision and seminar problem, and the August and September 2026 primary sources.',
 'Distinguished decidability-preserving reductions between bag-bag and bag-set semantics from evaluating the same unchanged queries; preserved importance 92 and category.',
]
sources=[
 'Read Amarilli’s maintained question list on 17 September 2026, exact bag-containment section: asks decidability and complexity; this card retains the already selected decidability component.',
 'Read Kolaitis, Section 4.5 of Dagstuhl Seminar 25081 report, seminar 16–21 February 2025 and publication 6 October 2025. It states the natural-number-semiring problem, traces it to Chaudhuri–Vardi 1993 and separates undecidable extensions.',
 'Read Konstantinidis–Mogavero, ICDT 2025 Article 5: Section 2 pp. 5:3–4 gives the exact sum-product bag-bag semantics including repeated atoms; Section 3 Theorems 2 and 3 change queries when reducing to bag-set and Boolean cases; Theorem 30 p. 5:16 gives CoNExpTime for a join-on-free containee against a general containing query.',
 'Read Marcinkowski–Ostropolski-Nalewaja, arXiv:2503.07219v3, 1 June 2025, abstract and Sections 1–3. Its internal convention is Boolean bag-set queries, with reductions to the bag-bag decision problem noted; ordinary CQ-versus-CQ containment remains open.',
 'Read Marcinkowski–Orda, PODS 2024, arXiv:2503.18003v1 posted 23 March 2025, primary abstract and publication metadata. The stated undecidability modifies the comparison by an input linear function; this is not the unit-coefficient plain containment test.',
 'Read Aref–Libkin–Martens, arXiv:2608.10863, August 2026 primary PDF, Bags discussion, Debunk 3: Performance. It explicitly still lists general CQ bag-containment decidability as unknown, separately from unions and disequalities.',
 'Read Cohen, arXiv:2609.09978v1, 9 September 2026, primary abstract. The new finite counterexample bounds decide equivalence in a combined-semantics model over set-valued relations, not general one-sided bag containment. Its full proof was not independently audited.',
 f'Bounded primary-source searches through {DATE} found no verified resolution of the exact plain-CQ bag-bag decidability target; proofs of the cited theorems were not independently certified.',
]
complete(identifier,dict(
 title='Conjunctive-query containment under bag semantics',criterion='decision',question_type='yes_no',
 formal=r'''Does there exist one deterministic Turing machine that halts on every pair \((q_1,q_2)\) of finite conjunctive queries with the same output arity and correctly decides whether
\[
 \forall\text{ finite bag databases }D\quad
 \forall a\in U_D^r:\qquad q_1(D)(a)\le q_2(D)(a),
\]
with the unrestricted syntax and natural-number sum-product semantics defined below? Both input relations and query answers retain multiplicities.''',
 definitions=r'''A relational signature \(\tau\) is a finite list of relation symbols, each with a specified nonnegative integer arity. It is part of the query input, with no fixed bound on the number of symbols or their arities. Both queries use a common signature; unused relation symbols have no effect. They also use a finite set \(C\) of named constants. A finite bag database \(D\) consists of a finite domain \(U_D\), an injective interpretation \(\iota_D:C\to U_D\) of the constant names, and a function
\[
 D_R:U_D^{\operatorname{arity}(R)}\to\mathbb N
 \quad\text{for every }R\in\tau,
\]
where \(\mathbb N=\{0,1,2,\ldots\}\). The value is the tuple's multiplicity; zero means absence. All natural multiplicities and all finite domain sizes are allowed, without a bound determined in advance. No key, dependency or other integrity constraint is imposed. The domain may be empty when there are no constants. A nullary relation has one possible tuple, the empty tuple.

A conjunctive query has syntax
\[
 q(x_1,\ldots,x_r)\;:\!-\;A_1,\ldots,A_m,
\]
where each \(A_j\) is a positive relational atom \(R_j(t_{j,1},\ldots,t_{j,a_j})\), \(a_j\) is the arity of \(R_j\), and each term is a variable or a named constant. Every variable occurs in at least one body atom. The head \((x_1,\ldots,x_r)\) is a list of variables from the body; variables may repeat in the head. Body variables not in the head are existentially quantified. Distinct variable names may be assigned the same domain element, and a variable may be assigned the value of a constant. Different named constants denote distinct elements. The body is a list of atom occurrences: relation names, variables and entire atoms may repeat. There is no disjunction, negation, inequality, built-in comparison, aggregation syntax, recursion or duplicate-elimination operation. Identifying variables can enforce equality, but no additional predicate is interpreted specially.

Write \(\operatorname{Var}(q)\) for the finite set of variables in \(q\). For an assignment \(h:\operatorname{Var}(q)\to U_D\), extend \(h\) to constants by \(h(c)=\iota_D(c)\), and write \(D(A_j[h])\) for \(D_{R_j}\) evaluated at the instantiated tuple. For every output tuple \(a\in U_D^r\), define
\[
 q(D)(a)=
 \sum_{\substack{h:\operatorname{Var}(q)\to U_D\\
                  (h(x_1),\ldots,h(x_r))=a}}
       \prod_{j=1}^{m}D(A_j[h]).
\]
The arithmetic is ordinary exact addition and multiplication of nonnegative integers. The sum is finite; an empty sum is zero and an empty product is one. Each repeated occurrence contributes its own factor. For example, the bodies \(R(x)\) and \(R(x),R(x)\) give multiplicities \(D_R(a)\) and \(D_R(a)^2\), respectively. Output tuples that violate equalities forced by repeated head variables receive zero.

A Boolean query has \(r=0\) and returns a natural multiplicity at the unique empty tuple; it does not merely report whether a witness exists. An empty body is permitted only with no variables, hence has empty head and returns one. These conventions also define evaluation on empty domains.

Input queries, signatures, variable names and constant names have finite, effectively parseable binary encodings, for example length-prefixed symbol lists and atom lists. The machine receives only these two queries and their signature, not a database or a database-size bound. It must accept exactly when the displayed inequality holds for every database and every output tuple and reject otherwise. It can reject ill-formed encodings immediately. There is no required bound on its running time beyond halting on every input, and there is no noncomputable advice or external oracle. The inequality is exact and one-sided, with no input scale factor or additive slack.''',
 answer_criterion=r'''Give a complete Lean-checked proof that such a total decision algorithm exists, with an implementation and proofs of termination and correctness on every input, or a complete Lean-checked proof that no such algorithm exists.

Enumerating finite counterexample databases only semidecides noncontainment and does not establish decidability. A decision procedure for equivalence, set semantics, or a proper query subclass is insufficient on its own. A theorem about bag-set inputs may be used only together with a proved effective reduction covering the bag-valued input model here. Undecidability after adding unions, inequalities, integrity constraints or a numerical transformation of the query count must likewise be reduced to this exact plain-CQ problem. No approximation tolerance or complexity-class upper bound is requested.''',
 source_formulation=dict(text='The maintained question list asks whether conjunctive-query containment under bag semantics is decidable and what its complexity is. This card selects decidability alone, fixing bag input and output multiplicities over the nonnegative integers as in the seminar problem and the ICDT semantics.',caption='Paraphrase of Amarilli’s bag-containment question and Kolaitis’s Section 4.5 in Dagstuhl Seminar 25081; accessed 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','List of open questions: Decidability of conjunctive query containment under bag semantics','Antoine Amarilli',None,'https://a3nm.net/work/research/questions/#decidability-of-conjunctive-query-containment-under-bag-semantics','Maintained question list; exact section, accessed 17 September 2026'),
 ref('seminar','Semirings in Databases, Automata, and Logic (Dagstuhl Seminar 25081)','Phokion G. Kolaitis (Section 4.5 contributor)',2025,'https://doi.org/10.4230/DagRep.15.2.89','Section 4.5; seminar 16–21 February 2025, report published 6 October 2025'),
 ref('extensions','Bag Semantics Conjunctive Query Containment. Four Small Steps Towards Undecidability','Jerzy Marcinkowski; Mateusz Orda',2024,'https://doi.org/10.1145/3651604','PODS 2024; arXiv:2503.18003v1 abstract, 23 March 2025, supplied linear transformation of the count'),
 ref('joinfree','Bag Containment of Join-On-Free Queries','George Konstantinidis; Fabio Mogavero',2025,'https://doi.org/10.4230/LIPIcs.ICDT.2025.5','Section 2 pp. 5:3–4; Section 3 Theorems 2–3; Theorem 30 p. 5:16'),
 ref('cq_ucq','Bag Semantics Query Containment: The CQ vs. UCQ Case and Other Stories','Jerzy Marcinkowski; Piotr Ostropolski-Nalewaja',2025,'https://arxiv.org/abs/2503.07219v3','1 June 2025 revision; abstract and Sections 1–3, Boolean bag-set convention and unresolved ordinary CQ case'),
 ref('nulls','Time to Move on: Querying without Nulls and Bags','Molham Aref; Leonid Libkin; Wim Martens',2026,'https://arxiv.org/abs/2608.10863','August 2026; Bags discussion, Debunk 3: Performance, general CQ containment still undecided'),
 ref('equivalence','Few Rows Tell Them Apart: Equivalence of Queries Mixing Set and Bag Semantics','Sara Cohen',2026,'https://arxiv.org/abs/2609.09978v1','9 September 2026; primary abstract, equivalence and finite witnesses under combined semantics'),
 ],
 context_blocks=[
 block('With duplicates, a join multiplies tuple multiplicities and projection adds contributions of different assignments. Queries returning the same set of answers can therefore produce different numbers of copies.','joinfree'),
 block('Every proposed counterexample is a finite database with exactly computable counts. Exhaustively searching databases will eventually discover a counterexample when one exists, but gives no stopping rule for true containment.'),
 block('The join-on-free theorem allows existential variables but forbids joins between body atoms through those variables in the contained query. Its decidability result therefore covers more than projection-free queries, while keeping a restriction absent from this target.','joinfree'),
 block('The literature relates bag-bag and bag-set containment by transformations of the query input. This does not justify silently treating the same original relations as sets; repeated atoms can affect the original bag comparison.','joinfree'),
 block('Nearby undecidability results add unions, comparisons or a transformation of the count. The June 2025 CQ-versus-UCQ paper still leaves the ordinary two-CQ inequality open.','cq_ucq'),
 block('The August 2026 discussion continues to identify general CQ bag containment as unresolved.','nulls'),
 block('The September 2026 finite-witness result addresses equivalence in a mixed set/bag framework. Equality of two query functions and a one-sided inequality are distinct decision predicates; that abstract does not provide a general containment decision algorithm.','equivalence'),
 ],
 progress=[progress('1993','Chaudhuri and Vardi pose the bag-containment decidability question, as recorded in the seminar history.','seminar'),progress('2024','Undecidability is established for nearby extensions involving a supplied transformation of a query count.','extensions'),progress('2025-03-21','Join-on-free containment into a general CQ is proved decidable.','joinfree'),progress('2025-06-01','The revised CQ-versus-UCQ paper retains ordinary two-CQ containment as open.','cq_ucq'),progress('2026-08','The SQL semantics discussion still lists general CQ bag-containment decidability as unknown.','nulls'),progress('2026-09-09','Finite witness bounds are proposed for equivalence under combined semantics, a different target.','equivalence')],
),notes,sources,'The August 2026 primary discussion, 2025 seminar problem and maintained question list retain general CQ bag-containment decidability as open. The September equivalence preprint addresses a different predicate and semantics. Bounded primary-source checks through 17 September 2026 found no verified resolution of the exact bag-bag problem here; cited proofs were not independently certified.',summary=[
 'A conjunctive database query produces answer multiplicities by summing products of input multiplicities.',
 'Containment means that the first query never produces more copies of any answer than the second on any finite bag database.',
 'The question asks whether one total algorithm can decide this property from the two unrestricted queries alone.',
 'Restricted joins are decidable and nearby extensions are undecidable, while new equivalence results do not settle this one-sided comparison.',
 'A complete Lean-checked answer must prove a terminating exact decision procedure or unconditional undecidability.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
