"""Complete the effective constant-delay classifier with the selected RAM model."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6645'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the effective yes/no target: a total classifier for all finite conjunctive queries, including self-joins and projections.',
 'Specified query syntax, set semantics, empty answers, database word size, exact RAM instructions and all three delay endpoints.',
 'Retained polynomial address space without a linear-space restriction; made the query-dependent constants and deterministic computation explicit.',
 'Distinguished deciding existence of an enumerator from constructing one, and unconditional classification from conditional fine-grained exclusions.',
 'Corrected the mirror-query locator to §7.1 and separated output arity in the 2023 results from atom arity in the preliminary 2025 report.',
 'Checked the author’s 2026 announcement, which still leaves examples unclassified; preserved assessed importance 95 and required a complete Lean-checked answer.',
]
sources=[
 'Read Carmeli–Segoufin, PODS 2023 author PDF, pp. 277–289, §1–2 (model and Theorem 2), partial-classification statements and §7.1 Example 19 and Proposition 20. DOI 10.1145/3584372.3588667. The source explicitly permits memory beyond linear preprocessing space and uses constant-time tuple tables; mirror-query enumeration may store output-sized data. Its hardness statements invoke fine-grained hypotheses.',
 'Read Rouvroy, Enumerating answers of acyclic conjunctive queries with self-joins (Report), dated 2 May 2025, abstract and §1–2 pp. 1–3. The report explicitly calls itself unpolished and restricts its study to atoms of arity at most two. It gives sufficient and necessary conditions with examples outside both, not a complete dichotomy.',
 f'Read Rouvroy’s research page on {DATE}, 2026 BDA26 announcement Constant-Delay Enumeration of Conjunctive Queries with Self-Joins and Projections. Its abstract still states that examples remain unclassified. The PDF is unavailable; the announcement is not treated as a checked published proof or as evidence that the event has already occurred.',
 f'Bounded later-work checks through {DATE} found no total classifier or undecidability proof for the whole stated class. This review checks scope and statements rather than certifying the cited algorithmic proofs.',
]
status='The checked self-join results supply partial positive and conditional negative classifications. The preliminary 2025 report and the author’s 2026 announcement retain unclassified examples. No resolution of the full effective classifier was found. The exact target retains the existing deterministic RAM and permissive polynomial-address-space convention; unconditional membership is not replaced by membership conditional on a fine-grained conjecture.'
complete(identifier,dict(
 criterion='characterization',question_type='yes_no',year=2026,
 formal=r'''Does there exist a total deterministic algorithm which, given any finite conjunctive query \(q\), decides whether all distinct answers to \(q\) can be enumerated on every finite database \(D\) with \(O_q(N)\) preprocessing time and \(O_q(1)\) worst-case delay?

Self-joins and projection are allowed. Here \(N\) is the database size defined below; the enumeration model is the specified deterministic word-RAM. The classifier has no prescribed running-time bound.''',
 definitions=r'''A conjunctive query is finite syntax
\[
q(\bar x)=\exists\bar y\;\bigwedge_{i=1}^{s}R_i(\bar z_i).
\]
The head \(\bar x\) is an ordered list of distinct variables, and \(\bar y\) lists the other variables. Each variable occurs in an atom. Each relation symbol has one fixed positive integer arity within the query, and the length of each argument list agrees with it. A symbol may occur in several atoms (a self-join); a variable may repeat within an atom. There are no constants, negation, disequalities, aggregation, or additional constraints on the database. All relation arities and the complete formula are part of the classifier input, not fixed globally. An empty conjunction has no variables and is the constantly true Boolean query.

A database for the query has domain \([n]=\{1,\ldots,n\}\), for any integer \(n\ge0\), and explicitly lists each relation \(R^D\subseteq[n]^{\operatorname{arity}(R)}\). Each tuple occurs at most once in its relation list; list order is arbitrary. Domain elements outside all relations are permitted. Define the word size of the data by
\[
N=1+n+\sum_R\operatorname{arity}(R)\,|R^D|.
\]
All tuple entries and \(n\) are provided as binary integers. In particular, the domain-size contribution to the resource parameter is \(n\), not merely its binary encoding length. No succinct relation representation or data-access oracle is provided.

An assignment maps query variables to domain elements. It satisfies an atom exactly when the resulting tuple belongs to that relation. The answer set \(q(D)\) consists of head tuples having at least one satisfying extension to \(\bar y\). Different witnesses for the same head tuple give just one answer. An empty head gives either no answer or the one empty tuple, according to whether the query is false or true.

For a fixed query, an enumerator is a finite deterministic word-RAM program, with constants \(B,C\ge1\) independent of the database; \(B\) is an integer. Its word length is \(w=B\lceil\log_2(N+2)\rceil\) bits. The address universe contains \(2^w\) initially zero cells. Each read, write, indirect access, comparison, conditional branch, addition, subtraction, multiplication, integer quotient or remainder by a nonzero divisor, bitwise Boolean operation, or shift costs one operation. Addition, subtraction and multiplication return results modulo \(2^w\); a shift by at least \(w\) returns zero. Larger values occupy multiple words with all operations charged. No random instruction, arbitrary-precision unit-cost arithmetic, database-specific advice or oracle is available.

Every accessed cell and every output operation is charged. Unused addresses require no initialization. There is no further requirement that memory used in preprocessing be linear, or that enumeration use only constant additional memory. The fixed exponent implicit in the address universe may depend on the query and algorithm. Writing an answer writes its head coordinates, or one marker for the empty tuple; the output is append-only.

The program first finishes a preprocessing phase of at most \(CN\) operations, then enumerates exactly \(q(D)\) in any order without repetition and halts. After preprocessing, the time to the first answer, between consecutive answers, and from the last answer to halting is at most \(C\). If there are no answers, it must halt within \(C\) operations after preprocessing. The same constants and program must work on every database for that query.

The classifier is a deterministic Turing machine on a full finite encoding of query syntax, with relation names, variable names and arities encoded by finite binary strings. It halts on every valid query and says yes exactly when an enumerator and constants as above exist; malformed encodings may be rejected. Its input is \(q\), not a database. It need not produce an enumerator or the constants, and its running time has no required bound. The property being classified is actual, unconditional existence of an enumerator. A classification under an unproved complexity hypothesis is not silently substituted for that property. This effective existence proposition is the previously selected precise version of the source’s broader classification request.''',
 answer_criterion=r'''Give a total classifier and a complete Lean-checked proof of its correctness for every query in the stated syntax and enumeration model, or give a complete Lean-checked proof that no such total classifier exists. A positive answer need not effectively construct the enumerators whose existence it classifies.

An algorithm for only a restricted query family, or sufficient and necessary conditions leaving other queries unclassified, is not complete. Exhibiting a query without efficient enumeration does not refute the existence of a classifier: a correct classifier may reject that query. Conditional exclusions must retain their hypotheses and do not by themselves establish an unconditional answer.''',
 source_formulation=dict(text='The source asks for a fine-grained understanding of enumeration for conjunctive queries with self-joins, extending the classical self-join-free tractability picture. This card retains the explicit effective question of deciding which fixed queries admit linear preprocessing and constant delay, in the source’s permissive memory model.',caption='Paraphrase of Carmeli–Segoufin, PODS 2023, introduction and §2; the effective classifier is the selected editorial target.',citation='primary',format='editorial_paraphrase'),
 why='Database queries can have far more answers than input tuples. Constant delay after linear preprocessing gives both output-sensitive total time and a bounded wait for each answer. A complete effective classification would identify exactly which query patterns allow this guarantee, including repeated uses of the same relation.',
 references=[
 ref('primary','Conjunctive Queries With Self-Joins, Towards a Fine-Grained Enumeration Complexity Analysis','Nofar Carmeli; Luc Segoufin',2023,'https://www.di.ens.fr/~segoufin/Papers/Mypapers/enum-cq-selfjoin.pdf','PODS 2023, 277–289, DOI 10.1145/3584372.3588667; §2 model and Theorem 2; §7.1 Example 19 and Proposition 20'),
 ref('report','Enumerating answers of acyclic conjunctive queries with self-joins (Report)','Clément Rouvroy',2025,'https://www.normalesup.org/~rouvroy/papers/Report_M1S1.pdf','Dated 2 May 2025; explicitly preliminary; abstract and §1–2 pp. 1–3, atom-arity restriction and unclassified examples'),
 ref('announcement','Research page: Constant-Delay Enumeration of Conjunctive Queries with Self-Joins and Projections','Clément Rouvroy',2026,'https://www.normalesup.org/~rouvroy/research/index.html','2026 BDA26 entry; joint work with Nofar Carmeli, David Carral and Luc Segoufin; abstract accessed 17 September 2026; PDF unavailable'),
 ],
 context_blocks=[
 block(r'For example, \(q(x,z)=\exists y\,R(x,y)\land S(y,z)\) asks for endpoint pairs linked through some intermediate element. Many choices of the intermediate element can witness the same answer, which still has to be printed just once.'),
 block('The query is fixed while the database varies. Query-dependent constants are therefore allowed, even though the separate classifier receives the query as its input. Its task is to decide an algorithm-existence property, rather than to enumerate answers itself.'),
 block('A query hypergraph has variables as vertices and the variable set of each atom as a hyperedge. It is acyclic if the hyperedges have a join tree in which those containing each variable form a connected subtree. Free-connex acyclicity additionally requires this after adding the head-variable set as an edge. The source recalls the classical linear-preprocessing, constant-delay algorithm for this condition.'),
 block('The corresponding hardness statements for self-join-free queries use hypotheses about Boolean matrix multiplication or hyperclique detection. They should not be read as unconditional proofs that all other queries are intractable.'),
 block('Self-joins permit further tractable structures: §7.1 gives cyclic mirror queries with constant-delay enumeration. Their memory during enumeration may grow with output size. Imposing constant additional workspace would therefore change the class under consideration.'),
 block('The preliminary 2025 report studies acyclic queries with unary or binary atoms, including projections. It develops partial conditions and explicitly leaves queries outside the classified cases. That atom-arity restriction does not cover the arbitrary-arity input of this card.','report'),
 block('The author’s 2026 announcement of joint work on self-joins and projections still reports unclassified examples. Its unavailable manuscript is not treated as a verified complete classification.','announcement'),
 ],
 progress=[
 progress('2023','The PODS paper develops partial classifications and cyclic mirror-query algorithms in a model allowing polynomial memory.'),
 progress('2025-05-02','A preliminary report studies further projected, acyclic self-join queries with unary or binary atoms, leaving cases unclassified.','report'),
 progress('2026','The author’s BDA26 announcement still describes partial conditions and unclassified examples; checked on 17 September.','announcement'),
 ],
),notes,sources,status,summary=[
 'The input to the proposed classifier is any finite conjunctive query, allowing repeated relation symbols and existentially hidden variables.',
 'It must decide whether the query has a deterministic enumerator with linear preprocessing and constant worst-case delay on every database.',
 'Answers use set semantics, are printed without repetition, and the delay includes the first answer and final termination.',
 'The specified RAM permits polynomial address space without a separate linear-memory restriction, and all enumeration constants may depend on the fixed query.',
 'A complete Lean-checked answer must establish a total classifier or prove that none exists; partial or conditional classifications do not finish the target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
