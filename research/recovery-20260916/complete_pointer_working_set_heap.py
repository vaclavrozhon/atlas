"""Review constant updates with insertion-age extraction on a pointer machine."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0474';claim=read_claims(ROOT)[identifier]
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
notes=[
 'Retained the restored insertion-count definition of working-set size, exact deterministic online behavior, and the joint total-cost bound for every finite sequence.',
 'Specified legal operations, supplied handles, insertion age unaffected by decrease-key, empty-queue responses and tied priorities as opaque ordered keys.',
 'Clarified constant-size pointer records and registers, charged allocation and bitwise auxiliary counters, with no address arithmetic, word tricks or uncharged preprocessing.',
 'Read the final ESA 2026 publication, updating the July preprint reference while retaining its inverse-Ackermann decrease-key factor and explicit open question.',
 'Read the July stack-like heap and working-set equivalence theorems; its comparison-model statement and nonconstant insertion bound are not conflated with the requested pointer-machine guarantee.',
 'Preserved importance, excluded meld and maintained a complete Lean-checked proof-or-refutation criterion.',
]
sources=[
 'Read Iacono, Working set heaps with decrease-key, §5.1, printed p.16 of Adaptive and Scalable Data Structures, Dagstuhl Seminar 25191, DOI 10.4230/DagRep.15.5.1. It discusses multiple working-set conventions. The saved card had already selected insertion count; that convention is retained rather than silently replacing it by all-operation count.',
 'Read van der Hoog–Iacono–Rotenberg–Rutschmann, Near-Optimal Working-Set Heaps and Dijkstra on Pointer Machines, final ESA 2026 Article 45, DOI 10.4230/LIPIcs.ESA.2026.45, published 25 August 2026: Introduction p.45:3, pointer-machine definition p.45:4, Definition 2 and Theorem 3 p.45:5. The theorem has constant amortized Push, inverse-Ackermann amortized DecreaseKey, constant worst-case Peek, and worst-case O(1+log Gamma) Pop. The Introduction explicitly leaves removal of the inverse-Ackermann overhead open. The formal node model has constant auxiliary bits and pointers, with unbounded total node count.',
 'Read Haeupler–Hladik–Rozhon–Tarjan, Heaps and Their Working Sets, arXiv:2607.24621v1, 27 July 2026: Theorem 1.3 and Lemma 1.4 pp.4–5, Theorem 1.5 p.5 and Theorem 3.3 p.10. The working-set variants are compared in an amortized sense, whereas the stack-like guarantee is stronger. For every fixed iteration depth, the insertion overhead is an iterated log-star function, not a constant. The formal construction theorem is stated in the comparison model.',
 'Bounded primary-source searches through 17 September 2026 found the final ESA publication and the July stack-like construction, but no verified solution of the joint constant-insertion, constant-decrease pointer-machine target. The review checks theorem scopes and models, not every implementation proof.',
]
complete(identifier,dict(
 formal=r'''Does there exist one deterministic online priority queue in the pointer-machine model below and an absolute constant \(C\ge1\) such that every legal sequence \(\sigma\) of \(M\ge1\) operations, starting with an empty queue, has total charged cost
\[
W_A(\sigma)\le C\left(M+\sum_{x\text{ extracted in }\sigma}\log_2\Gamma_\sigma(x)\right)?
\]
The operations are insert, find-min, decrease-key and extract-min, and
\[
\Gamma_\sigma(x)=1+\#\{\text{insertions strictly between the insertion and extraction of }x\}.
\]
Those later insertions count even if their items were already removed. All answers must be exact, and the same program and constant must work for every finite sequence and every ordered key domain.''',
 definitions=r'''An insertion creates a new item carrying a supplied opaque key and returns a handle to it. A handle is a pointer identifying that live item; subsequent decrease-key requests supply it directly. Decrease-key replaces the key by a supplied no-larger key and does not change the item’s original insertion time. It is legal only for a live handle. Find-min returns a minimum live item without removing it. Extract-min returns and removes a minimum live item, invalidating its handle. On an empty queue either minimum operation returns an empty symbol. Melding queues, arbitrary deletion and increasing keys are not requested.

Keys have a total-order comparison interface. If application priorities can coincide, a fixed tie label may be included in the supplied opaque key so comparisons also settle ties. The queue can copy references to supplied keys and compare them, but cannot inspect their representation, extract an integer from them or manufacture auxiliary keys for storing counters. Item identity is separate from priority; repeated insertions create distinct items. Each operation must finish and return its answer before the next request is supplied. The program receives neither future requests nor the total sequence length.

A pointer machine is a finite program with a fixed constant number of pointer registers and finite control. Memory consists of records, each with at most a fixed constant number of pointer fields, auxiliary bits and references to supplied keys. These constants belong to the implementation and are independent of the sequence length and heap size. Pointers may be copied, compared for equality, followed or changed; the null pointer is allowed. A primitive step performs one such constant-size action, one comparison of two supplied keys, a Boolean operation on constantly many auxiliary bits, allocation or disposal of one record, or a constant-size input/output action. A request supplies its constant number of key references and handles to the registers. New records have fixed initial contents. The machine begins with a fixed constant-size empty representation.

No address arithmetic, array indexing by a computed integer, unbounded integer operation or word-parallel bit operation is available. A large counter may be represented by multiple records, but traversing and changing its bits is charged. There is no separate space bound; allocating and manipulating every auxiliary record costs time. All initialization and maintenance work is included in \(W_A\), including work between requests. The empty sequence has zero operation cost.

The number \(\Gamma_\sigma(x)\) is a performance parameter defined from the history, not supplied free to the program. It is always at least one. The \(M\) term pays the constant part of each extraction and all other operations. The inequality is a joint amortized guarantee, not a worst-case constant bound on each update. It must hold even if many items remain in the queue at the end; future deletions cannot be used to pay for already completed work.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed existence claim or its unconditional logical negation. A positive proof must specify the pointer-machine implementation, establish the exact online interface, and prove the one total-cost inequality for every legal finite sequence. Any potential argument must justify its initial and final contributions, including sequences that leave items in the queue.

A negative proof must rule out every deterministic implementation in this model, not just a particular heap design. A word-RAM solution, a guarantee without decrease-key, an unbounded inverse-Ackermann update factor, or a nonconstant insertion overhead does not satisfy the joint target. Any use of a different working-set definition must prove the required transfer while preserving all operation charges. No lower bound under an unproved assumption is an unconditional refutation.''',
 source_formulation=dict(text='The seminar asks for a pointer-model heap combining a working-set extraction guarantee with constant decrease-key. The later ESA paper makes the insertion-age convention explicit and leaves removal of its inverse-Ackermann decrease-key overhead open.',caption='Iacono, Dagstuhl Seminar 25191, §5.1 p.16; van der Hoog et al., ESA 2026, Introduction p.45:3, Definition 2 and Theorem 3 p.45:5. The previously selected insertion-count and joint amortized conventions are retained.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Adaptive and Scalable Data Structures — Working set heaps with decrease-key','John Iacono (problem contributor)',2025,'https://doi.org/10.4230/DagRep.15.5.1','Dagstuhl Seminar 25191, §5.1, printed p.16'),
 ref('pointer','Near-Optimal Working-Set Heaps and Dijkstra on Pointer Machines','Ivor van der Hoog; John Iacono; Eva Rotenberg; Daniel Rutschmann',2026,'https://doi.org/10.4230/LIPIcs.ESA.2026.45','Published 25 August 2026; Introduction p.45:3, pointer model p.45:4, Definition 2 and Theorem 3 p.45:5'),
 ref('stack','Heaps and Their Working Sets','Bernhard Haeupler; Richard Hladík; Václav Rozhoň; Robert E. Tarjan',2026,'https://arxiv.org/abs/2607.24621v1','27 July 2026; Theorems 1.3 and 1.5, Lemma 1.4, and Theorem 3.3'),
 ],
 context_blocks=[
 block('The extraction charge depends on how recently the item entered the queue. Keeping many old items while repeatedly inserting and immediately extracting a new minimum should cost only a constant per pair of operations.'),
 block('A priority decrease can concern an old item and must coexist with this temporal adaptivity. Efficient extraction without cheap priority changes does not meet the goal.'),
 block('The final ESA 2026 construction gives constant insertion and an insertion-age extraction bound, but its decrease-key cost retains an inverse-Ackermann factor. Its Introduction explicitly identifies removal of that factor as open.','pointer'),
 block('The July comparison-model construction gives constant decrease-key and a stronger stack-like extraction guarantee. It pays a slowly growing insertion cost for every fixed depth of its iterated construction, so the stated theorem does not provide simultaneous constant updates.','stack'),
 block('The July equivalence theorem relates several amortized working-set definitions while preserving other operation charges. The card fixes insertion count directly and does not require the stronger stack-like property.','stack'),
 ],
 progress=[progress('2025','The pointer-model working-set/decrease-key problem is stated at Dagstuhl.'),progress('2026-07-27','A comparison-model heap combines constant decrease-key with stack-like extraction and a nonconstant iterated-log-star insertion overhead.','stack'),progress('2026-08-25','The final ESA publication gives the inverse-Ackermann pointer-machine update bound and explicitly retains the overhead-removal question.','pointer')],
),notes,sources,'The exact joint constant-update target remains open in the final ESA 2026 publication and was not resolved by the checked July comparison-model tradeoff. Bounded primary-source checks through 17 September 2026 found no verified resolution. This review checks formulations, models and theorem scopes, not every implementation proof.',summary=[
 'The queue must support insertion, minimum lookup, priority decrease and minimum extraction online.',
 'An extraction is charged logarithmically in the number of insertions since that item arrived.',
 'The target combines that adaptive extraction cost with constant amortized charges for every other operation.',
 'The computation uses pointers, constant auxiliary bits and key comparisons; the checked recent results retain a growing factor in an update bound.',
 'A complete Lean-checked construction or unconditional refutation must cover every finite operation sequence.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
