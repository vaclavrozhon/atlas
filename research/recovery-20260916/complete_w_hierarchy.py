"""State the full adjacent-level strictness conjecture using the textbook model."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6731'
claim=read_claims(ROOT)[identifier]
notes=[
 'Located the explicit all-adjacent-level conjecture after Theorem 13.21, rather than narrowing the draft to its first illustrative pair.',
 'Defined uniform deterministic parameterized many-one reductions with computable time and parameter functions.',
 'Expanded circuit depth, weft, exact-weight satisfiability and the order of the fixed-depth quantifiers in W[t].',
 'Distinguished strictness at every positive level from FPT versus W[1], completeness results and oracle separations.',
 'Required an unconditional Lean-checked proof of the full conjecture or an equality at a particular adjacent pair.',
 'Assessed the structural importance of distinguishing levels of parameterized intractability individually.',
]
sources=[
 'Read Cygan et al., Parameterized Algorithms, author manuscript dated 30 May 2016: §13.1, Definition 13.1 and Theorems 13.2–13.3, printed pp. 424–427/PDF pp. 440–443; §13.3, circuit definitions, Definition 13.16, Theorems 13.18–13.21 and the final explicit W[t] != W[t+1] for every t>=1 conjecture, printed pp. 435–439/PDF pp. 451–455. The draft locator marked the section start, not the final conjecture.',
 'Read Bottesch, On W[1]-Hardness as Evidence for Intractability, arXiv:1712.05766v3, 19 July 2018: abstract, introduction §1.3, printed/PDF p. 5, and §5, Theorem 19 and its following discussion, printed/PDF p. 13. These are level-dependent oracle separations, not unconditional separations and not one oracle simultaneously separating every pair. The initial v1 download was superseded by the checked v3.',
 f'Bounded primary-source searches through {DATE} for hierarchy strictness, adjacent-level separation and later parameterized-complexity work found no unrelativized resolution. Search hits proving hardness or defining other strict hierarchies were not treated as evidence for separation here. This is not an exhaustive literature certification.',
]
status='The textbook explicitly conjectures strictness at every positive adjacent level. Later oracle constructions provide only relativized evidence and do not prove the unrelativized conjecture. No proof or counterexample to the full target was found in the bounded review through '+DATE+'.'
complete(identifier,dict(
 criterion='decision',question_type='yes_no',
 formal=r'''Is the \(W\)-hierarchy strict at every positive level?
\[
\forall\,t\in\mathbb N_{\ge1},\qquad
W[t]\subsetneq W[t+1].
\]
The classes use uniform deterministic fixed-parameter many-one reductions and exact-weight satisfiability of bounded-depth Boolean circuits, as defined below. Equivalently, for every \(t\ge1\), is there a parameterized decision problem in \(W[t+1]\) that does not belong to \(W[t]\)?''',
 definitions=r'''A parameterized decision problem is a set \(P\subseteq\{0,1\}^{*}\times\mathbb N\). An input is a finite binary string \(x\) together with a nonnegative integer \(k\), its parameter. The input length \(L\) includes both \(x\) and the binary encoding of \(k\), with delimiters. Membership is an exact yes/no question.

A fixed-parameter many-one reduction from \(P\) to \(Q\) is one uniform deterministic algorithm \(R\), total computable functions \(f,g:\mathbb N\to\mathbb N\), and an integer \(c\ge0\), such that \(R(x,k)\) halts in at most \(f(k)(L+1)^c\) steps and outputs a pair \((y,\ell)\) satisfying
\[
(x,k)\in P\ \Longleftrightarrow\ (y,\ell)\in Q,
\qquad \ell\le g(k).
\]
The algorithm, functions and exponent are fixed for the reduction; in particular, \(c\) cannot grow with \(k\). Functions \(f,g\) may grow arbitrarily fast but must be computable. Time is measured on a deterministic multitape Turing machine over fixed finite alphabets, counting input access, arithmetic and output writing. No random bits, length-dependent advice or oracle are available. This is a single-output reduction, not an adaptive sequence of queries to \(Q\).

A Boolean circuit is a finite directed acyclic graph with at least one input node and a designated output node of outdegree zero. Nodes of indegree zero are distinct Boolean input variables. Each other node is either a NOT gate of indegree one or an AND or OR gate of indegree at least two, with the usual Boolean semantics. Gates have unrestricted fan-out. A gate is large if its indegree exceeds two. The depth of the circuit is the maximum number of edges on a path from an input node to the designated output. Its weft is the maximum number of large gates on such a path. Unused input nodes are allowed and still count among the input variables.

For an explicit encoding, order all \(N\) nodes topologically, put the \(n\) input nodes first, and give the integers \(n,N\) and the output-node index, followed by each remaining gate's type, indegree and list of distinct predecessor indices. Predecessors must have smaller indices. Encode each integer \(u\ge0\) by \(1^{h}0w\), where \(w\) is the binary representation of \(u+1\) and \(h=|w|\); encode gate types NOT, AND, OR by integers \(1,2,3\). All listed integers use this code, and there are no trailing bits. Invalid encodings are no-instances in the circuit problems below.

For fixed integers \(t,d\ge1\), let \(\operatorname{WCS}_{t,d}\) be the parameterized problem consisting of pairs \((C,k)\) where \(C\) is an encoded circuit of weft at most \(t\) and depth at most \(d\), and some assignment to its input nodes has exactly \(k\) ones and makes its output one. The parameter is \(k\) alone. Circuits exceeding either structural bound, or having fewer than \(k\) input nodes, are no-instances.

Define
\[
W[t]=\{P:\ \exists\,d\ge1\text{ such that }P
\text{ has a fixed-parameter many-one reduction to }
\operatorname{WCS}_{t,d}\}.
\]
The integer \(d\) may depend on the problem \(P\) and level \(t\), but it is a fixed constant independent of the input and its parameter. The reduction may also depend on \(P,t,d\). This quantifier does not allow depth growing as a function of \(k\).

The inclusions \(W[t]\subseteq W[t+1]\) follow directly from the weft bounds. Strict inclusion means that at least one problem belongs to the larger class and not the smaller one. The formal target quantifies over all fixed positive integers \(t\); it does not require an algorithm that constructs witnesses from \(t\).

For comparison, FPT consists of parameterized problems decidable within \(f(k)(L+1)^c\) deterministic time for some computable \(f\) and constant \(c\). Separating FPT from \(W[1]\) is a distinct statement and does not by itself establish the requested adjacent-level separations.''',
 answer_criterion=r'''Supply a complete Lean-checked proof that \(W[t]\subsetneq W[t+1]\) for every integer \(t\ge1\), with the classes and reductions above; or supply a complete Lean-checked refutation, proving \(W[t]=W[t+1]\) for at least one particular \(t\ge1\). A proof for just finitely many strict inclusions does not establish the universal positive answer. Completeness or hardness for one of these classes, an oracle-relative separation, or a separation conditional on an unproved hypothesis does not settle the target. No claim about collapse of all other levels is required for a negative answer.''',
 source_formulation=dict(
 text='The textbook states the expectation that every positive level of the W-hierarchy differs from its next level. It illustrates the first pair with Independent Set and Dominating Set.',
 caption='Paraphrase of the paragraph after Theorem 13.21, §13.3, printed p. 439/PDF p. 455 of the author manuscript dated 30 May 2016.',
 citation='primary',format='editorial_paraphrase'),
 why='Parameterized completeness places many natural problems into different levels of a common hierarchy, but a level label alone does not prove a difference in computational power. Establishing strictness would show that these levels capture distinct forms of parameterized intractability. An equality would instead identify a new general reduction principle connecting problems currently treated as having different complexity.',
 importance=dict(score=91,method='editorial',assessed_on=DATE,
 reason='A foundational structural conjecture for parameterized complexity, interpreting the distinction between canonical complete problems and every higher level of the W-hierarchy.',
 basis='Individual reading of the textbook’s explicit all-level conjecture, reduction model and later oracle evidence.'),
 references=[
 ref('primary','Parameterized Algorithms','Marek Cygan; Fedor V. Fomin; Łukasz Kowalik; Daniel Lokshtanov; Dániel Marx; Marcin Pilipczuk; Michał Pilipczuk; Saket Saurabh',2016,
 'https://parameterized-algorithms.mimuw.edu.pl/parameterized-algorithms.pdf',
 'Author manuscript dated 30 May 2016; §13.1 Definition 13.1 and §13.3 Definition 13.16, Theorems 13.18–13.21 and following conjecture; printed pp. 424–427 and 435–439; published book 2015'),
 ref('oracle','On W[1]-Hardness as Evidence for Intractability','Ralph C. Bottesch',2018,
 'https://arxiv.org/abs/1712.05766v3',
 'Version 3, 19 July 2018; §1.3 p. 5 and §5, Theorem 19 and following discussion, p. 13'),
 ],
 context_blocks=[
 block(r'With the desired solution size as parameter, Independent Set is \(W[1]\)-complete and Dominating Set is \(W[2]\)-complete. The source gives a reduction from the former to the latter. A reduction in the reverse direction would identify these two classes.'),
 block(r'For higher levels, the source supplies complete weighted satisfiability problems using alternating layers of conjunctions and disjunctions. Completeness describes their position in the hierarchy without proving that the positions are distinct.'),
 block(r'The unrestricted target is stronger in scope than separating one chosen pair. It asks whether every adjacent positive pair differs, while leaving the separate FPT boundary to its own question.'),
 block(r'Bottesch constructs, for each level, a suitable oracle separating the relevant adjacent relativized classes. The oracle may depend on the level, and such results do not prove a separation without an oracle.','oracle'),
 ],
 progress=[
 progress('2016-05-30','The checked textbook version explicitly formulates strictness of every positive adjacent level.'),
 progress('2018-07-19','The revised oracle-evidence paper records separate relativized separations for all levels.','oracle'),
 progress(DATE,'The review expands the original all-level target and checks the distinction between completeness, relativization and an unconditional hierarchy theorem.'),
 ],
),notes,sources,status,summary=[
 'The W-hierarchy groups parameterized decision problems by reductions to exact-weight satisfiability for restricted Boolean circuits.',
 'The question asks whether each positive level is strictly contained in the next.',
 'The circuit depth is fixed for each target problem, and reductions may spend arbitrary computable time in the parameter times a fixed polynomial in input length.',
 'Independent Set and Dominating Set illustrate the first two levels, whose known completeness does not itself separate them.',
 'A solution must prove all adjacent separations or prove equality at one particular adjacent pair; oracle-based evidence is insufficient.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
