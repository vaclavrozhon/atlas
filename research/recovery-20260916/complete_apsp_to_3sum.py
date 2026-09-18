"""Select and specify the APSP-to-integer-3SUM direction."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6946';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A fine-grained reduction from integer APSP to 3SUM',
 status='source_open',criterion='reductions',question_type='yes_no',
 formal=r'''Is there a bounded-error randomized fine-grained Turing reduction from integer all-pairs shortest paths to integer 3SUM? Specifically, for every rational \(\varepsilon\in(0,1)\), does there exist a rational \(\delta\in(0,1)\) such that, for every fixed integer weight exponent \(c\ge1\), one uniform classical randomized oracle algorithm outputs all shortest-path distances of every promised \(n\)-vertex input graph with probability at least \(2/3\), using an exact 3SUM oracle and charged cost
\[
T+\sum_{j=1}^{q}m_j^{\,2-\varepsilon}\le K(n+2)^{\,3-\delta}
\]
on every execution? The constants \(K\), the machine word-size factor and the algorithm may depend on \(\varepsilon,c\), but \(\delta\) must be common to all \(c\). Input weights, queries and the oracle-cost model are defined below.''',
 definitions=r'''An APSP instance is a directed graph on the numbered vertices \([n]\), \(n\ge2\), given by a complete adjacency table. Each ordered pair has a presence flag and, if present, a signed integer edge weight in \([-n^c,n^c]\). The input is promised to have no negative-weight directed cycle. Negative edges, zero-weight cycles and self-loops are allowed. For each ordered pair \((u,v)\), the required output is the minimum weight of a directed walk from \(u\) to \(v\), or an unreachable flag if no such walk exists. The empty walk from a vertex to itself has weight zero. Under the promise every finite minimum is attained by a simple path after deleting cycles and has absolute value at most \((n-1)n^c\). The output is the entire \(n\)-by-\(n\) distance table, not a single distance, the existence of a negative triangle, or a list of paths. A successful execution must output the whole table correctly.

A valid 3SUM query explicitly lists \(m\ge2\) distinct integers \(z_1,\ldots,z_m\in[-m^4,m^4]\). The exact answer is whether some three distinct indices \(i,j,k\) satisfy \(z_i+z_j+z_k=0\) in the integers. For \(m=2\) the answer is no. This single-list polynomial-universe problem fixes the same target convention as the source's 3SUM hypothesis. It does not allow arbitrary real numbers or unit-cost large integers.

For each fixed \(\varepsilon,c\), use a finite sequential classical word-RAM program with \(w=B\lceil\log_2(n+2)\rceil\)-bit words, for an integer constant \(B\ge c+4\) large enough for all its query values and addresses. Signed integers are represented in two's complement. Unit-cost instructions are memory reads and writes, copies, comparisons, branches, Boolean bitwise operations, shifts, addition, subtraction and multiplication modulo \(2^w\), and unsigned quotient and remainder by a nonzero divisor. Shifts by at least \(w\) return zero. One random instruction returns one fresh independent fair bit. Multiword arithmetic charges every constituent operation. There is no nonuniform advice, uncharged lookup table, quantum operation or arbitrary-precision real instruction.

The quantity \(T\) counts all local instructions, including input reads, preprocessing, random bits, the writing of every complete query, one instruction per oracle invocation, and the writing of all output entries. It excludes the oracle's internal computation, which is charged separately by \(m^{2-\varepsilon}\) for a query of length \(m\). The real powers in the cost bound specify resource accounting and are not primitive machine operations. Queries may be adaptive. On every input graph satisfying the promise, every possible oracle-answer sequence and every random tape must lead to termination within the displayed bound and only valid queries. Correctness is required when all oracle answers are exact, with probability taken over the reduction's coins separately for each input. No guarantee is required on graphs violating the no-negative-cycle promise.

The source saving \(\delta\) may depend on the target saving \(\varepsilon\), but not on the weight exponent \(c\). The program and constants may depend on both fixed parameters. There is no required effective compiler from the parameters to a program. Deterministic reductions are permitted as a special case. Multiple calls are allowed, but their whole weighted sum must fit the budget.

A reduction of this kind transfers any fixed subquadratic bounded-error algorithm for the specified 3SUM problem into a fixed subcubic saving for every fixed polynomial APSP weight range. Target-error amplification over the calls costs only logarithmic factors, which can be absorbed by applying the reduction with a slightly smaller target saving. The assertion concerns construction of such an oracle reduction, not merely the truth of the implication between algorithm-existence statements.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of this APSP-to-3SUM reduction. A positive answer must prove the all-pairs output guarantee, exact integer query semantics, the full weighted query budget, all-branch local cost and the exponent saving uniform across fixed weight exponents. The reverse reduction, reductions of both problems to a common third problem, or ordinary polynomial-time reducibility do not suffice.',
 why='APSP and 3SUM support two major collections of conditional algorithmic lower bounds. A reduction from APSP to 3SUM would show that a subquadratic breakthrough for 3SUM also breaks the cubic APSP barrier, linking these two currently separate explanations of algorithmic difficulty.',
 importance=dict(score=88,method='editorial',reason='A direct connection between two central fine-grained hypotheses would reorganize a large network of conditional lower bounds. The direction, uniform exponent saving and integer machine model are essential to that consequence.'),
 source_formulation=dict(text='The survey describes the absence of reductions between the central APSP and 3SUM problems and reviews their separate hardness frameworks. This card selects APSP-to-3SUM, bounded-error randomized Turing reductions, polynomial integer weights and a saving common to every fixed weight exponent. The direction was the announced recommended editorial default after an optional question remained unanswered; it is not recorded as user confirmation. The imported page-16 locator concerns Hitting Set and is corrected here.',caption='Vassilevska Williams, ICM 2018 survey, §2.1 pp.4–6 and §§4–5 pp.12–15; the 2017 open-problems column supplies the explicit reduction convention and comparison.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','On Some Fine-Grained Questions in Algorithms and Complexity','Virginia Vassilevska Williams',2018,'https://people.csail.mit.edu/virgi/eccentri.pdf','§2.1 pp.4–6: hypotheses and absence of reductions; §§4–5 pp.12–15: 3SUM and APSP hardness'),
 ref('column','Some Open Problems in Fine-Grained Complexity','Virginia Vassilevska Williams',2017,'https://www.cs.umd.edu/~gasarch/open/finegrain.pdf','Definition 3.1 p.2; integer hypotheses p.3; Problem 4 pp.4–5 and common Exact Triangle target'),
 ref('triangles','Hardness for Triangle Problems under Even More Believable Hypotheses: Reductions from Real APSP, Real 3SUM, and OV','Timothy M. Chan; Virginia Vassilevska Williams; Yinzhan Xu',2022,'https://arxiv.org/abs/2203.08356v1','Abstract and §1 pp.1–3: separate integer/real hypotheses and common triangle targets'),
 ],
 context_blocks=[
 block('The survey treats APSP and 3SUM as distinct central hypotheses. For integer inputs their benchmarks are cubic and quadratic, so a useful reduction must preserve a fixed saving relative to those different exponents.'),
 block('APSP is fine-grained equivalent to several negative-triangle and distance-product problems. Those equivalences do not identify it with 3SUM, whose arithmetic equality task has a different structure.'),
 block('The 2017 column records Exact Triangle as a common target of APSP and 3SUM. Two reductions into one common target give no reduction from one source problem to the other.','column'),
 block('The 2022 work obtains triangle hardness from real APSP, real 3SUM and OV, carefully distinguishing numeric models. Its shared-target conclusions do not resolve the direct integer APSP-to-3SUM reduction asked here.','triangles'),
 ],
 progress=[progress('2017','The column formalizes fine-grained reductions and discusses relationships among the central hypotheses.','column'),progress('2018','The survey describes the separate 3SUM and APSP hardness frameworks.'),progress('2022-03','The real-input triangle reductions broaden shared hardness sources without establishing this direct reduction.','triangles')],
),[
 'Selected and announced the APSP-to-3SUM editorial default after the optional direction question remained unanswered.',
 'Specified complete integer-weighted directed input, the no-negative-cycle promise and exact all-pairs output.',
 'Matched the source’s fixed polynomial-universe integer 3SUM convention, rather than importing real arithmetic or the separate Las Vegas card.',
 'Defined the adaptive weighted query sum and a source saving independent of the fixed weight exponent.',
 'Corrected the inherited source locator, individually assessed importance and required a complete Lean-checked reduction or refutation.',
],[
 'Read the survey’s §2.1 hypotheses, §§4–5 comparison, and the 2017 Definition 3.1 and Problem 4.',
 'Re-read the 2022 real triangle paper’s abstract and §1, including its distinct integer/real models and common-target statements.',
 'Bounded primary-source searches through 18 September 2026 found no matching direct reduction; shared triangle hardness was not mistaken for a reduction between the two source problems.',
], 'Source-open in the central fine-grained relationship program. This card chooses one direction and exact parameter conventions after an unanswered optional question, rather than claiming those choices were explicitly confirmed. Bounded checks through 18 September 2026 found no resolution of the selected randomized integer reduction. Known common targets and APSP-to-negative-triangle equivalences do not settle it.',summary=[
 'The question asks whether integer all-pairs shortest paths can be reduced to integer 3SUM while preserving fixed exponent savings.',
 'Any subquadratic target saving should yield a subcubic source saving common to all fixed polynomial weight ranges.',
 'The reduction may be randomized and adaptive, but must charge its own work and every oracle query.',
 'A successful run must return every exact shortest-path distance, with probability at least two thirds on each input graph.',
 'Known reductions of both problems to triangle tasks do not give the direct reduction selected here.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
