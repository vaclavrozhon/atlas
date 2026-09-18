"""Select a robust PSPACE-hardness target for succinct decision-tree depth."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-5189';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='PSPACE-hardness of a factor-two gap in decision-tree depth',
 status='source_open',criterion='reductions',question_type='yes_no',
 formal=r'''Is the following promise problem PSPACE-hard under deterministic polynomial-time many-one reductions? The input is an explicitly given Boolean circuit \(C\) on \(n\ge1\) input variables and an integer \(k\) with \(1\le k\le n\). Writing \(f_C:\{0,1\}^n\to\{0,1\}\) for the function computed by \(C\), the two promised cases are
\[
\text{YES}:D(f_C)\le k,\qquad
\text{NO}:D(f_C)>2k,
\]
where \(D(f_C)\) is the minimum worst-case depth of a deterministic decision tree that computes \(f_C\) exactly on every input.''',
 definitions=r'''A deterministic decision tree is a finite rooted binary tree. Each internal node names an input variable \(x_i\), its two outgoing edges are labeled zero and one, and each leaf carries an output bit. On input \(x\), the tree follows the edge labeled \(x_i\) at a node querying \(x_i\). Its depth is the maximum number of internal nodes on a root-to-leaf path. The tree computes \(f_C\) if its output is \(f_C(x)\) for every \(x\in\{0,1\}^n\). The minimum depth over such trees is \(D(f_C)\in\{0,\ldots,n\}\); constant functions have depth zero. Queries are adaptive, but the tree has no randomness or computational error. The objective is depth, not number of leaves or total number of nodes.

The circuit is a directed acyclic graph over AND and OR gates of fan-in two, NOT gates of fan-in one, optional Boolean constants, and one specified output. Its input variables are explicitly listed, including any unused variables. Encode it by a topologically ordered node list with gate types and binary predecessor indices, followed by the output index. Encode \(k\) in binary. The input size \(L\) is the total number of bits in this description. No bound polynomial in \(n\) on circuit size is promised; computational resources for a reduction are measured in the length of its own input, and its entire output description must be polynomially long.

For the promise problem, a pair \((C,k)\) with \(k<D(f_C)\le2k\) lies outside the promise. A solver may behave arbitrarily there. Invalid encodings are also outside the promise.

PSPACE is the class of languages \(A\subseteq\{0,1\}^*\) decidable by a deterministic Turing machine that halts on every input and uses at most polynomially many work-tape cells. The asserted hardness means that for every \(A\in\mathrm{PSPACE}\), there exists one deterministic polynomial-time Turing machine \(R_A\) that maps every string \(z\) to a valid pair \((C_z,k_z)\) within the promise and satisfies
\[
z\in A\Longrightarrow D(f_{C_z})\le k_z,\qquad
z\notin A\Longrightarrow D(f_{C_z})>2k_z.
\]
The reduction may depend on \(A\), but not on \(z\) except through its computation. It has no advice or oracle. This is a many-one promise reduction, not a Turing reduction allowed multiple adaptive calls to an approximation oracle.

The selected gap is multiplicative and fixed independently of \(n\). An additive constant gap does not establish it. An algorithm outputting an integer \(a\) with \(D(f_C)\le a\le2D(f_C)\) on all circuits would distinguish the promised cases by comparing \(a\) with \(2k\), but the card asks specifically for the displayed hardness assertion, not for a complete classification of every approximation guarantee.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of PSPACE-hardness for the stated factor-two promise problem under polynomial-time many-one reductions. Exact hardness or hardness for a constant additive error alone is insufficient. A conditional consequence such as “a polynomial-time approximation would imply P = PSPACE” must be supported by a reduction meeting the stated gap, rather than assumed.',
 why='The exact decision-tree depth of a succinctly represented function is PSPACE-hard. A multiplicative-gap result would show that this difficulty survives coarse approximation of the number of input bits that must be inspected, rather than depending on a single critical query.',
 importance=dict(score=75,method='editorial',reason='Robust hardness of deterministic query depth is a substantive metacomplexity question linking succinct representations, adaptive query algorithms and PSPACE beyond exact threshold computation.'),
 source_formulation=dict(text='The source asks about approximating decision-tree complexity after treating both truth-table and circuit representations. It already gives hardness for any constant additive error. This card selects the circuit representation and a factor-two PSPACE-hardness promise under polynomial-time many-one reductions. The fixed factor is an editorial specialization; the optional choice received no reply and the recommendation was announced before application.',caption='Loff–Milovanov, STACS 2025, §4 open question 4, p.66:12; definitions and exact hardness in §§2–3.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','The Hardness of Decision Tree Complexity','Bruno Loff; Alexey Milovanov',2025,'https://doi.org/10.4230/LIPIcs.STACS.2025.66','Definitions 1–5 pp.66:2–66:3; Propositions 6–9 pp.66:3–66:4; Theorems 10–11 and uniformity convention pp.66:4–66:5; §4 question 4 p.66:12'),
 ],
 context_blocks=[
 block('The paper distinguishes the truth-table input of length 2ⁿ from a circuit that may describe the same function much more succinctly. For an explicit truth table, dynamic programming computes exact depth in polynomial time in that table length.'),
 block('For circuit input, the source proves PSPACE membership and PSPACE-hardness of exact depth computation. Its truth-table lower bound instead concerns NC¹-hardness under a much weaker reduction model. Those two statements must not be interchanged.'),
 block('The final open-question discussion explains that constant additive approximation retains the exact problem’s hardness. It asks for stronger approximation results without fixing a multiplicative factor. The factor-two gap here makes one such direction explicit.'),
 block('The lower-bound task concerns the minimum depth of an exact tree. Hardness for learning a tree from samples, minimizing its leaf count, or allowing classification mistakes would concern other problems.'),
 ],
 progress=[progress('2025-02','STACS 2025 establishes exact circuit-depth PSPACE-hardness and records the stronger approximation question, beyond constant additive error.')],
),[
 'Selected circuit input and an explicit factor-two promise from the broad approximation question; recorded the specialization as an unanswered editorial default.',
 'Defined exact deterministic query depth, circuit encoding, total description length, promise boundary and the allowed reduction model.',
 'Distinguished depth from tree size and circuit input from the full truth table.',
 'Checked the exact and additive-approximation results without promoting them to a multiplicative gap.',
 'Individually assessed importance and required a complete Lean-checked proof or refutation.',
],[
 'Downloaded and read STACS 2025 definitions, Propositions 6–9, Theorems 10–11 and the reduction discussion.',
 'Read §4 question 4 p.66:12, including its constant-additive-error observation.',
 'Bounded primary-source searches through 18 September 2026 found no later resolution matching this circuit-input factor-two promise; source titles about tree-size minimization were not treated as depth results.',
], 'The 2025 source proves exact circuit-input PSPACE-hardness and retains stronger approximation as an open direction. The selected factor-two many-one promise specialization was not found resolved in the bounded review through 18 September 2026. It is an explicit editorial target rather than a factor stated verbatim in the source. The known constant-additive-error observation does not establish it.',summary=[
 'Given a Boolean circuit, decision-tree depth is the fewest input-bit queries needed in the worst case to compute its function exactly.',
 'The question asks whether distinguishing depth at most k from depth greater than 2k remains PSPACE-hard.',
 'The function is supplied by a circuit, whose binary description is the input-size measure.',
 'Exact computation and constant additive approximation are already hard in the cited source, while a multiplicative gap needs a stronger result.',
 'The card fixes a factor-two many-one promise and keeps this distinct from truth-table algorithms and tree-size minimization.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
