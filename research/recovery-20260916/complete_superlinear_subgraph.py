"""Complete and archive the selected historical linear-round question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-4231'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user choice to retain the source’s concrete linear-versus-superlinear question and archive its published negative resolution.',
 'Recovered ordinary CONGEST from the conclusion, despite the original paper’s broadcast-CON­GEST title.',
 'Specified a fixed pattern, connected simple host networks, non-induced embeddings, initial knowledge, message size, bounded-error detection and the order of quantifiers.',
 'Matched the target to SPAA 2018 Theorem 1.2; a fixed k=2 already supplies a superlinear lower bound and no growing pattern is needed.',
 'Read the full original lower-bound construction and embedding/simulation proof, using the published version for corrected problem definitions.',
 'Preserved the broader classification as provenance rather than silently replacing the selected historical target.',
]
sources=[
 'Read Korhonen–Rybicki, OPODIS 2017 Article 4, §3 model and §8 p. 4:14. The proceedings appeared 28 March 2018; the question expressly concerns ordinary CONGEST.',
 'Read Fischer–Gonen–Kuhn–Oshman, SPAA 2018, Theorem 1.2, §2 Definition 1 and §3.1–3.3. Published definition is non-induced subgraph detection with existential positive output.',
 'Read Fischer–Gonen–Oshman, arXiv:1711.06920v1 (18 November 2017), all of §3 pp. 5–13: fixed pattern, host family, embedding Lemma 3.1 and the complete set-disjointness simulation.',
 'Checked that distinct k-subset labels force the same endpoint indices on both sides of an embedding, that the communication cut has O(k*n^(1/k)) edges, and that the host has Theta(n) vertices for fixed k.',
 'The early preprint has inconsistent induced-subgraph/acceptance wording in its preliminaries and inaccurate additive vertex counts. The published definition and explicit construction resolve the scope; only the verified asymptotic counts are used here.',
 'The standard randomized set-disjointness communication lower bound is an established dependency, not independently re-proved here. No Lean formalization is claimed.',
]
status=('Resolved negatively by Fischer, Gonen, Kuhn and Oshman, SPAA 2018, Theorem 1.2. '
 'For each fixed k>=2 there is a fixed O(k)-vertex pattern requiring Omega(n^(2-1/k)/(B*k)) rounds, even in diameter-three hosts. '
 'Taking k=2 and B=Theta(log n) rules out a linear-round algorithm even with bounded error. '
 'The user selected this historical threshold question, rather than the still broader full classification.')
complete(identifier,dict(
 title='Linear-round detection of every fixed subgraph',
 status='resolved',criterion='resources',question_type='yes_no',
 formal=r'''Is the following statement true?
\[
\forall\text{ finite simple graphs }H\text{ with }|V(H)|\ge1,\quad
\exists A_H\ \exists C_H>0\quad
\forall n\ge2:
\]
the distributed algorithm \(A_H\) detects a non-induced copy of \(H\) in every connected \(n\)-vertex simple undirected network, with success probability at least \(2/3\), and halts in at most \(C_H n\) rounds of CONGEST as defined below.

The pattern \(H\) is fixed before the algorithm and constant are chosen; it does not grow with the host size \(n\). This is the concrete linear-round question selected from the source, not a request for the exact complexity of every pattern.''',
 definitions=r'''The network is a connected finite simple undirected graph \(G=(V,E)\), with \(n=|V|\). Each vertex is a processor. Vertices have distinct identifiers in \(\{1,\ldots,n^3\}\). Initially a processor knows \(n\), the complete fixed pattern \(H\), its own identifier and the identifiers of its neighbors. It has no additional information about edges not incident to it.

Communication is synchronous. In each round a processor first performs arbitrary finite local computation and then sends a possibly different message of at most
\[
B(n)=\lceil\log_2(n+1)\rceil
\]
bits in each direction along each incident edge. Messages are received by the end of that round and may affect subsequent rounds. Local memory and computation are uncharged. The same finite algorithm \(A_H\) is used by all processors and for all host sizes; it may use independent private random bits. It must meet its round bound for every graph, identifier assignment and random tape. Choosing another fixed constant multiple of the logarithmic bandwidth gives the same linear-round question.

A copy of \(H\) is an injective map \(\varphi:V(H)\to V(G)\) such that \(\{\varphi(u),\varphi(v)\}\in E(G)\) whenever \(\{u,v\}\in E(H)\). Nonedges of \(H\) impose no requirement, so the copy need not be induced. Vertex identifiers are not pattern colors.

At termination each processor outputs zero or one. If a copy exists, the probability that at least one processor outputs one is at least \(2/3\). If no copy exists, the probability that all processors output zero is at least \(2/3\). This is a joint guarantee for the whole execution, not a separate error bound at each vertex. A processor need not lie in a detected copy or output its vertices. The task does not require every processor to learn the answer.

The constant \(C_H\) may depend on the pattern and algorithm but not on \(n\), the host graph or its identifiers. Its existence must hold for every finite pattern. A single fixed pattern for which no such algorithm and constant exist refutes the statement. Allowing randomization makes the assertion at least as permissive as its deterministic version; the published lower bound refutes both.''',
 answer_criterion=r'''For the historical benchmark assertion, an accepted answer would be a complete Lean-checked proof or refutation with these quantifiers and this detection model. A negative answer must establish a superlinear obstruction for one fixed finite pattern, rather than only for patterns whose size grows with \(n\), induced detection, listing all copies, or a more restricted broadcast model. The published negative resolution is recorded below; this archive entry does not assert that its proof has been formalized in Lean. The assertion is binary, with no numerical \(1/100\) tolerance.''',
 source_formulation=dict(
 text='After asking about general subgraph detection, the conclusion explicitly asks whether every constant-size target can be detected in a linear number of CONGEST rounds, or whether some target needs superlinear time.',
 caption='Paraphrase of the first subgraph-detection question in §8, p. 4:14; this is the user-selected historical target.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=80,method='editorial',
 reason='The threshold distinguishes local pattern recognition from a substantial bandwidth bottleneck, even for fixed patterns and small-diameter networks.',
 basis='Individual historical assessment of a general structural question resolved by a nearly-quadratic family of distributed lower bounds.'),
 why='Without message-size limits, a fixed connected pattern can be checked from bounded-radius neighborhoods. The historical question asked whether small messages could nevertheless force more than a linear number of rounds. Its negative resolution demonstrates a strong communication obstruction for a task with a very local combinatorial description.',
 references=[
 ref('primary','Deterministic Subgraph Detection in Broadcast CONGEST',
 'Janne H. Korhonen; Joel Rybicki',2017,
 'https://doi.org/10.4230/LIPIcs.OPODIS.2017.4',
 'OPODIS 2017, Article 4; published 28 March 2018; §3 model and §8, p. 4:14'),
 ref('resolution','Possibilities and Impossibilities for Distributed Subgraph Detection',
 'Orr Fischer; Tzlil Gonen; Fabian Kuhn; Rotem Oshman',2018,
 'https://doi.org/10.1145/3210377.3210401',
 'SPAA 2018, 16–18 July; Theorem 1.2, §2 Definition 1 and §3.1–3.3; author copy https://www.cs.tau.ac.il/~roshman/papers/FGKO18.pdf'),
 ref('full','Superlinear Lower Bounds for Distributed Subgraph Detection',
 'Orr Fischer; Tzlil Gonen; Rotem Oshman',2017,
 'https://arxiv.org/abs/1711.06920v1',
 'Version 1, 18 November 2017; Theorem 1.1 and full §3 construction and proof, pp. 5–13; published model wording takes precedence over preliminary inconsistencies'),
 ],
 context_blocks=[
 block('The source studies deterministic algorithms in broadcast CONGEST, where each processor sends the same message to every neighbor. Its concluding open question explicitly switches to general CONGEST, where messages may differ by neighbor. That distinction is retained in this card.'),
 block('The source discusses linear upper bounds for several familiar pattern classes, including cliques. Such examples did not imply a common upper bound for every fixed graph. The question concerns existence of an algorithm separately for each fixed pattern.'),
 block(r'The published resolution constructs, for every fixed \(k\ge2\), a pattern \(H_k\) with \(O(k)\) vertices whose detection requires \(\Omega(n^{2-1/k}/(Bk))\) rounds. Both the pattern and hard host networks can have diameter three.','resolution'),
 block(r'At \(k=2\) and logarithmic bandwidth this is \(\Omega(n^{3/2}/\log n)\), which grows faster than \(n\). Thus a fixed pattern already refutes the selected assertion; the separate near-quadratic bound obtained with a growing \(k\) is not needed.','resolution'),
 block('Detection, listing, induced detection and requiring every processor to know the global answer are distinct tasks. The matched theorem concerns the non-induced existential-output detection convention used here. It applies to bounded-error randomized algorithms and therefore also to deterministic ones.','resolution'),
 block('The November 2017 preprint contains the detailed construction behind the later published result. Its preliminary definition has inconsistent wording; the publication states the non-induced problem correctly. The source and resolution appeared during overlapping publication cycles.','full'),
 ],
 progress=[
 progress('2017','The OPODIS source asks whether all fixed patterns admit linear-round detection in general CONGEST.'),
 progress('2017-11-18','A preprint gives a fixed-pattern family with superlinear detection lower bounds.','full'),
 progress('2018-07-16','The SPAA publication states the negative resolution as Theorem 1.2.','resolution'),
 progress('2026-09-16','The user retains this historical threshold question; the individual review matches the model and archives the resolved card.','resolution'),
 ],
),notes,sources,status,summary=[
 'The historical question asks whether every fixed graph can be detected in any connected network in a linear number of CONGEST rounds.',
 'Detection is non-induced, allows bounded-error randomization and requires only some processor to report a copy when one exists.',
 'The pattern and algorithm are fixed independently of the size of the host network.',
 'The published 2018 result gives a fixed pattern requiring on the order of n to the three-halves divided by log n rounds, refuting the assertion.',
 'This resolved threshold question is archived rather than replaced by the broader classification of all pattern complexities.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],
 archive_reason='User selected the historical linear-round question on 16 September 2026. Resolved negatively by Fischer–Gonen–Kuhn–Oshman, SPAA 2018 Theorem 1.2, already for fixed k=2 and ordinary logarithmic-bandwidth CONGEST.')
