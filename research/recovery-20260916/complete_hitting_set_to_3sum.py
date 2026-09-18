"""Make the Hitting Set to integer 3SUM reduction precise."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0560';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A fine-grained reduction from logarithmic-dimension Hitting Set to 3SUM',
 status='source_open',criterion='reductions',question_type='yes_no',
 formal=r'''Is there a bounded-error randomized fine-grained Turing reduction from logarithmic-dimension Hitting Set to integer 3SUM, with a common exponent saving across all fixed dimension constants? Precisely, is the following true?

For every rational \(\varepsilon\in(0,1)\), there is a rational \(\delta\in(0,1)\) such that, for every integer \(c\ge1\), there exist a uniform classical randomized oracle algorithm \(\mathcal R_{\varepsilon,c}\) and constants \(K,B\ge1\) with this guarantee: on every Hitting Set input consisting of two lists of \(n\ge2\) subsets of \([\lceil c\log_2n\rceil]\), the algorithm, with an exact 3SUM oracle, gives the correct answer with probability at least \(2/3\), and on every execution has charged cost
\[
T+\sum_{j=1}^{q}m_j^{\,2-\varepsilon}\le K(n+2)^{\,2-\delta}.
\]
Here \(T\) counts all local word-RAM instructions and \(m_j\) is the number of integers in its \(j\)-th oracle query. The exact problems and all cost conventions are below.''',
 definitions=r'''Write \(d=\lceil c\log_2 n\rceil\). The Hitting Set input is two ordered lists \(A=(a_1,\ldots,a_n)\) and \(D=(b_1,\ldots,b_n)\) of subsets of \([d]=\{1,\ldots,d\}\). Repetition and empty sets are allowed. The required decision bit is
\[
\exists i\in[n]\ \forall j\in[n]:a_i\cap b_j\ne\varnothing.
\]
The hitting set must be one of the supplied candidates \(a_i\), not an arbitrary union or an unknown small subset of the universe. Equivalently, each set is a Boolean vector and every selected inner product must be positive. Encode \(n\) and both full Boolean incidence tables explicitly, with one bit stored in each input word. The fixed constant \(c\) is built into the reduction, not supplied as a variable-size input.

A valid integer 3SUM query is a list of \(m\ge2\) distinct signed integers \(z_1,\ldots,z_m\in[-m^4,m^4]\). Its answer is yes exactly when there are three distinct indices \(i,j,k\) with \(z_i+z_j+z_k=0\), using ordinary integer addition. For \(m=2\) the answer is no. The entire query list must be explicitly written. This is the single-list polynomial-integer-universe formulation used in the source's hypothesis, not real 3SUM or the separate three-list Las Vegas formulation.

For fixed \(\varepsilon,c\), the reduction is one finite program working for all \(n\). Use words of \(w=B\lceil\log_2(n+2)\rceil\) bits, where \(B\) is a fixed positive integer chosen large enough to represent the inputs, query values, counters and addresses used by the program. Signed integers use two's-complement representation. Unit-cost instructions are word reads and writes, copies, comparisons, conditional branches, Boolean bitwise operations, shifts, addition, subtraction and multiplication modulo \(2^w\), and unsigned quotient and remainder for a nonzero divisor. Shifts by at least \(w\) yield zero. A random instruction returns one fresh independent fair bit. Arithmetic on longer integers uses multiple words and charges every constituent instruction. There is no arbitrary-real arithmetic, advice, quantum operation or uncharged preprocessing. All input accesses, random bits, query construction, bookkeeping and output writes contribute to \(T\); each oracle invocation also contributes one local instruction. The oracle's internal computation is represented only by the displayed charge \(m^{2-\varepsilon}\).

Queries may depend on previous oracle answers and random choices. For every possible answer sequence and random tape, the algorithm must halt, generate only valid queries, and satisfy the charged bound. Correctness is required when the oracle answers every query exactly. The success probability is per input over the reduction's random bits; it is not an average over Hitting Set instances. The constants \(K,B\) and program may depend on \(\varepsilon,c\). The saving \(\delta\) may depend on \(\varepsilon\), but must not depend on \(c\). No effective compiler from \(\varepsilon,c\) to the program is required.

The weighted sum includes every adaptive call, not just the largest query or the total query-list length. Such a reduction transfers any fixed subquadratic saving for bounded-error integer 3SUM to some fixed subquadratic saving for Hitting Set uniformly across all fixed \(c\): independent repetition of the target solver controls errors across calls, and choosing a smaller target saving absorbs logarithmic amplification overhead. The card asks for the reduction itself, not merely for an unproved logical implication between hardness hypotheses.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of the displayed reduction existence statement. A positive answer must establish exact query semantics, the weighted sum of costs on every execution, per-input success, and a source exponent saving independent of c. A polynomial-time reduction without these bounds, a reduction in the reverse direction, or a conditional obstacle restricted to deterministic reductions is insufficient.',
 why='Hitting Set and 3SUM underpin different families of conditional lower bounds. A reduction preserving fixed exponent savings would connect their hardness assumptions despite the universal quantifier over the second Hitting Set list.',
 source_formulation=dict(text='Problem 6 asks whether Hitting Set can be reduced to 3SUM or APSP. This card retains its 3SUM branch. It selects the logarithmic-dimension Hitting Set convention used by the existing hypothesis cards, with one exponent saving across all fixed dimension constants, rather than the source’s unrestricted-dimension poly(d) convention. This was the announced recommendation after an optional question remained unanswered; no user confirmation is inferred.',caption='Vassilevska Williams, Some Open Problems in Fine-Grained Complexity, Definition 3.1 p.2, computational model and Hypothesis 3 p.3, Problem 6 pp.5–6.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Some Open Problems in Fine-Grained Complexity','Virginia Vassilevska Williams',2017,'https://www.cs.umd.edu/~gasarch/open/finegrain.pdf','Definition 3.1 p.2; word-RAM and 3SUM Hypothesis 3 p.3; Problem 6 pp.5–6'),
 ref('survey','On Some Fine-Grained Questions in Algorithms and Complexity','Virginia Vassilevska Williams',2018,'https://people.csail.mit.edu/virgi/eccentri.pdf','§2.1 computational model and hypotheses; §6 pp.15–16 Hitting Set'),
 ref('barrier','Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility','Marco L. Carmosino; Jiawei Gao; Russell Impagliazzo; Ivan Mihajlin; Ramamohan Paturi; Stefan Schneider',2016,'https://people.csail.mit.edu/virgi/6.1420/papers/nseth.pdf','§5 Theorem 3 and §5.2 Lemma 6 pp.264–265'),
 ],
 context_blocks=[
 block('The source proposes Hitting Set as a potentially easier starting point than Orthogonal Vectors: one candidate must hit every member of the second list, replacing the existential-pair structure of OV.'),
 block('The source defines a fine-grained reduction through both local running time and a sum of target-query costs. Merely mapping a quadratic-time problem to another by a polynomial expansion would not preserve the desired improvement.'),
 block('The nondeterministic-reduction work gives limitations for deterministic or zero-error reductions from SETH-hard problems and separately analyzes Hitting Set. Those results are not a proof that the bounded-error Hitting Set-to-3SUM reduction selected here is impossible.','barrier'),
 block('The later survey still treats Hitting Set as a separate hypothesis and records only one direction of its relation with OV. This card matches the catalogue’s logarithmic-dimension hypothesis quantifiers while retaining an explicit oracle-reduction target.','survey'),
 ],
 progress=[progress('2017','The source poses the Hitting Set-to-3SUM or APSP reduction question.'),progress('2018','The survey retains Hitting Set among the separate fine-grained hypotheses.','survey')],
),[
 'Selected 3SUM as the target and logarithmic dimension as the announced editorial default after the optional scope question remained unanswered.',
 'Required one positive source exponent saving across all fixed dimension constants while allowing separate uniform programs for those constants.',
 'Defined the two-list hitting condition, exact polynomial-universe 3SUM queries and the weighted total oracle budget.',
 'Specified all-branch cost, arbitrary oracle-answer paths, per-input bounded error and the complete classical word-RAM model.',
 'Preserved the individually assessed importance and required a complete Lean-checked reduction or refutation.',
],[
 'Read the full 2017 Definition 3.1, word-RAM convention, integer 3SUM hypothesis and Problem 6.',
 'Re-read the 2018 Hitting Set hypothesis and the 2016 Theorem 3/Lemma 6 barriers without applying them outside their stated reduction models.',
 'Bounded primary-source searches through 18 September 2026 found no verified resolution of the selected randomized reduction. Results on geometric hitting sets and triangle collection do not give this reduction.',
], 'Source-open as a reduction program in the checked sources, with the stated logarithmic-dimension specialization selected editorially after an unanswered optional question. Bounded checks through 18 September 2026 found no matching reduction or refutation. Conditional nondeterministic barriers for other directions or more restricted reductions do not settle this bounded-error target.',summary=[
 'Hitting Set asks whether one supplied set intersects every set in a second supplied list.',
 'The target is a randomized reduction from its logarithmic-dimension version to exact integer 3SUM.',
 'Every fixed subquadratic target saving must yield a source saving common to all fixed logarithmic dimension constants.',
 'The cost bound charges both the reduction’s own work and the sum of all oracle-query costs.',
 'A complete answer must prove or refute this resource-preserving reduction rather than merely relate the problems by ordinary polynomial time.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
