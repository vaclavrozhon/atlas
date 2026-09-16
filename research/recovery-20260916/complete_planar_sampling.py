"""User-selected planar matching specialization of the determinant sampling card."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research/card-completion-20260913'))
from complete_review import complete, ref, block, progress
from review_queue import read_claims

identifier = 'TCS-3075'
old = json.loads((ROOT / 'data/cards' / f'{identifier}.json').read_text())
claim = read_claims(ROOT)[identifier]
references = old['references'] + [
    ref('quadratic2023','Quadratic Speedups in Parallel Sampling from Determinantal Distributions',
        'Nima Anari; Callum Burgess; Kevin Tian; Thuy-Duong Vuong',2023,
        'https://arxiv.org/abs/2203.11190','STOC 2023; inspected full arXiv version, Theorem 11 and §6'),
    ref('isoperimetry2024','Fast parallel sampling under isoperimetry',
        'Nima Anari; Sinho Chewi; Thuy-Duong Vuong',2024,
        'https://proceedings.mlr.press/v247/anari24a.html','COLT 2024; abstract and §1.3, Eulerian tours and asymmetric determinantal processes'),
    ref('autospec2025','Parallel Sampling via Autospeculation',
        'Nima Anari; Carlo Baronio; CJ Chen; Alireza Haqi; Frederic Koehler; Anqi Li; Thuy-Duong Vuong',2025,
        'https://arxiv.org/abs/2511.07869','November 2025 preprint; introduction, §1.1 and Theorem 27; expected-time bound and planar application'),
    ref('counting2026','Planar Perfect Matching Counting is as Hard as Determinants',
        'Radu Curticapean; Jiaheng Wang',2026,
        'https://arxiv.org/abs/2606.03975v1','2 June 2026 preprint; abstract, arithmetic complexity of weighted counting'),
]
notes = [
    'Applied the explicit user choice of approximately uniform planar perfect matching sampling; preserved the broader original determinant-counting direction as provenance.',
    'Specified simple unweighted planar graph inputs, the perfect-matching promise, edge-incidence output, unconditional total variation, failure mass and independent fair random bits.',
    'Fixed worst-case Boolean circuit depth, polynomial circuit size in n and inverse error, and logarithmic-space uniformity with the inverse-accuracy parameter padded explicitly.',
    'Updated the source history through autospeculation and distinguished counting, finding one matching, and distributional sampling; individually assessed the previously unassessed importance.',
]
sources = [
    'ITCS 2021 original full PDF: §1 lists planar perfect matchings and §7 asks for RNC sampling beyond arborescences; PRAM and parallel counting conventions inspected.',
    'Quadratic Speedups full arXiv PDF: Theorem 11 and §6 give the planar matching sampling bound; this is not polylogarithmic depth.',
    'COLT 2024 full PDF abstract and §1.3: later RNC applications include Eulerian tours and asymmetric determinantal point processes, without asserting this planar matching result.',
    'Autospeculation full author PDF, introduction and §1.1: explicitly retains the planar sampling question and reports an improved soft-O(n^(1/4)) bound via prior analysis; its expected-time convention was kept explicit.',
    '16 September 2026 bounded web search and June 2026 counting-paper abstract: weighted counting arithmetic hardness is a different objective, not a parallel sampling resolution.',
    'The prior user response authorizes selecting planar perfect matchings and recording the narrowing; exact bit-model/error conventions are explicit editorial specifications.',
]
status = ('Open in the inspected November 2025 autospeculation preprint, which explicitly distinguishes parallel planar matching sampling from already parallelizable counting. '
          'The source reports a soft-O(n^(1/4)) expected parallel-time application, still above the polylogarithmic target. '
          'The 2024 RNC results for Eulerian tours and asymmetric determinantal processes resolve other parts of the inherited broad direction. '
          'A bounded search on 16 September 2026 found no resolution of the selected planar approximate-sampling assertion. '
          'The June 2026 weighted counting paper concerns arithmetic operation counts and does not settle this target. '
          'This review checked model definitions and result scopes, not all source proofs or a Lean formalization.')

complete(identifier,dict(
    title='Parallel sampling of planar perfect matchings',
    question_type='yes_no',
    formal=r'''Do there exist constants \(C,k\ge1\) and a uniform family of randomized Boolean circuits \((A_{n,t})_{n\ge0,t\ge1}\) that, for every simple unweighted planar graph \(G\) on \([n]\) with at least one perfect matching, output a distribution \(\mu_{G,t}\) satisfying
\[
d_{\mathrm{TV}}(\mu_{G,t},U_G)\le2^{-t},
\]
with circuit size at most \(C(n+2^t+2)^k\) and depth at most \(C(\log_2(n+2)+t)^k\)?
Here \(U_G\) is uniform over all perfect matchings of \(G\), and the complete input, output, uniformity and failure conventions are defined below. The same constants and uniform circuit generator must work for every graph and precision. This is the user-selected approximately uniform RNC sampling target.''',
    definitions=r'''A graph is finite, undirected, loopless and without parallel edges; its vertices are \([n]\). Planarity means it admits an embedding in the plane with edges meeting only at shared endpoints. The input is the upper-triangular Boolean adjacency matrix in the lexicographic order of unordered vertex pairs. An embedding is not supplied. The promise is that the graph is planar and has at least one perfect matching. Inputs outside this promise still obey the resource bounds, but carry no distributional correctness requirement.

A perfect matching is a set of present edges incident to every vertex exactly once. Write \(\mathcal M(G)\) for this finite nonempty set and \(U_G(M)=1/|\mathcal M(G)|\) for \(M\in\mathcal M(G)\). The empty graph has the single empty perfect matching. Disconnected promised graphs are allowed; no bipartiteness, positive-degree lower bound or edge weights are assumed.

The accuracy parameter is a positive integer \(t\), defining error \(\varepsilon=2^{-t}\). These dyadic errors specify arbitrary requested accuracy up to a factor of two. Each circuit has the adjacency bits as ordinary inputs and independent unbiased random bits as additional inputs. Gates are AND and OR of fan-in two and NOT of fan-in one, together with constants; fan-out is unrestricted. Size counts gates, random inputs and output wires. Depth is the longest gate path and is a worst-case bound, independent of the random bits. The output consists of an edge-incidence vector indexed by all unordered vertex pairs and a failure flag. A nonmatching vector or a raised failure flag is interpreted as the single symbol \(\bot\).

Both output measures live on the finite set \(\mathcal M(G)\cup\{\bot\}\), with \(U_G(\bot)=0\), and
\[
d_{\mathrm{TV}}(\mu,U_G)=\frac12\sum_{z\in\mathcal M(G)\cup\{\bot\}}|\mu(z)-U_G(z)|.
\]
Thus failure probability is charged to the error and the approximation is unconditional; conditioning on success cannot conceal a large failure probability. The graph itself is fixed when taking this distribution.

Uniformity means that one deterministic machine, given unary \(n\) and unary \(2^t\), generates the description of \(A_{n,t}\) using \(O(\log(n+2)+t)\) work space and polynomial time in \(n+2^t\). Padding the inverse-accuracy parameter states precisely the permitted polynomial dependence on \(1/\varepsilon\); it does not require a bound polynomial merely in its binary bit length. No graph-dependent advice, counting oracle or exact-real random primitive is free. The circuit must implement all needed computation. Boolean depth and size give a precise standard parallel model corresponding to polynomially many bit processors. For inverse-polynomial error, the displayed bounds are polynomial size and polylogarithmic depth in graph size.

The generator, constants and exponent are chosen before \(n,t,G\). An affirmative answer is one such family. A negative answer is the full negation over all uniform families and fixed constants. Finding one perfect matching or computing their number is not the requested sampling task. The source's broader list of determinant-counted objects has been narrowed to this one user-selected graph distribution.''',
    answer_criterion=r'Supply a complete Lean-checked construction and proof of the asserted uniform circuit family, including worst-case depth, size, fair-bit implementation and the total-variation bound for every promised graph and every \(t\ge1\); or prove the full negation of that existence assertion. A result only about counting, finding one matching, a restricted graph family, conditional-on-success accuracy or sublinear but non-polylogarithmic depth is insufficient. The explicit sampling error \(2^{-t}\), not the default tolerance for numerical-value answers, governs this proposition. An experimental sampler or citation alone is not a Lean proof.',
    target_revision=dict(date='2026-09-16',previous_title=old['title'],previous_formal=old['formal'],authorization='User explicitly selected planar perfect matching sampling and requested that the narrowing be recorded.',scope='Approximately uniform sampling, polynomial work in graph size and inverse error, and polylogarithmic parallel depth. Other determinant-counted distributions are contextual history.'),
    source_formulation=dict(text='The original source lists several determinant-counted combinatorial distributions and asks for parallel randomized sampling algorithms. This card selects its planar perfect matching example, as explicitly authorized by the user.',caption='Editorial paraphrase; user-authorized specialization',citation='primary',format='editorial_paraphrase'),
    references=references,
    context_blocks=[
        block('Planar perfect matchings are among the combinatorial objects whose counts can be evaluated through determinants. Efficient parallel counting does not automatically give efficient parallel sampling, because the familiar conditional choices can depend sequentially on previous choices. The target asks whether this dependence can be removed for the entire matching distribution.', 'primary'),
        block('The selected question requires almost uniform random output, not simply the discovery of an arbitrary matching. It isolates one unresolved member of the source’s broader list; subsequent RNC results for other distributions do not answer it.', 'isoperimetry2024'),
        block(r'The 2023 work gives parallel planar matching sampling in roughly square-root time, suppressing logarithmic factors. The later autospeculation preprint reports an application with expected time \(\widetilde O(n^{1/4})\), and explicitly retains the polylogarithmic question. These bounds are recorded with their source conventions rather than promoted to the worst-case Boolean-depth target.', 'autospec2025'),
        block('The June 2026 result on planar matching counting studies weighted arithmetic complexity relative to determinants. It provides neither the distributional sampler nor a lower bound ruling out the sampler requested here.', 'counting2026'),
    ],
    why='This is a concrete test of whether counting and sampling remain equivalent under strong parallel-time constraints. Planarity makes exact counting tractable, so the remaining issue isolates the cost of coordinating random choices rather than the hardness of evaluating the partition function. A resolution would clarify a central boundary in parallel randomized algorithms.',
    importance=dict(score=81,method='editorial',reason='A representative unresolved separation between parallel counting and parallel sampling, with a precise combinatorial distribution and substantial general significance beyond one sampling implementation.'),
    progress=[
        progress('2021','The arborescence paper lists planar perfect matchings among the outstanding determinant-based parallel sampling tasks.','primary'),
        progress('2023',r'Theorem 11 gives exact planar matching sampling in \(\widetilde O(\sqrt n)\) parallel time using polynomially many processors.','quadratic2023'),
        progress('2024','RNC sampling results resolve the directed Eulerian-tour and asymmetric determinantal-process applications, not this selected planar matching task.','isoperimetry2024'),
        progress('2025-11',r'The autospeculation preprint reports an expected \(\widetilde O(n^{1/4})\) planar application and continues to identify polylogarithmic sampling as open.','autospec2025'),
        progress('2026-09-16','The bounded update checked later weighted-counting work and found no resolution of the selected sampling target.','counting2026'),
    ],
),notes,sources,status,summary=[
    'The input is a planar graph with at least one perfect matching, and the desired output is an almost uniform random perfect matching.',
    'The sampler must use polynomially many Boolean gates and polylogarithmic depth, with explicit dependence on the requested total-variation error.',
    'Failure probability counts toward the error and the circuit uses only independent fair random bits.',
    'Parallel counting and finding one matching do not themselves produce this distribution, while known faster samplers still have non-polylogarithmic parallel bounds.',
    'The problem tests a central boundary between counting and sampling under parallel resource constraints.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
