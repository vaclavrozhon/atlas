"""One-time individual editorial assessments, 10 September 2026."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
REVIEWED = {
'0466': (63, 'A concrete test of whether a widely used randomized string primitive can be certified at almost its construction cost; narrower than the general compressed-access barriers.'),
'0467': (83, 'Random access is a basic interface for compressed computation. The linear-space target would remove a persistent overhead for a central repetitiveness measure.'),
'0468': (81, 'Tests whether a fundamental string task can run at the size of its compressed input, including preprocessing; useful beyond one particular index implementation.'),
'0506': (88, 'Seeks a quantitative sample-complexity characterization of private learnability in terms of two basic dimensions, with consequences across hypothesis classes.'),
'0517': (72, 'Probes the color-versus-locality frontier close to a linear palette; an instructive degree-sensitive refinement of distributed symmetry breaking.'),
'0524': (77, 'Breaking the square-root degree barrier for the canonical coloring task would improve a broadly reused distributed primitive.'),
'0525': (66, 'Tests whether fractional matching permits sublinear degree dependence under bipartiteness; a focused separation inside local symmetry breaking.'),
'0611': (81, 'Exact Matching is a central derandomization test even on bipartite graphs. Its importance remains high while the recent claimed solution is assessed.'),
'1141': (75, 'Relates directed reachability structure to near-linear algorithms and isolates a basic obstruction behind shortcutting and parallel graph computation.'),
'1468': (63, 'Asks whether dominance among reported points imposes a genuine extra cost beyond orthogonal reporting; a clean geometric data-structure boundary.'),
'1813': (70, 'Matching the cycle-dependent exponents would expose how graph pattern structure determines communication cost; narrower than a complete subgraph-detection classification.'),
'2997': (80, 'Triangle detection is a basic distributed subgraph task. Its exact round complexity calibrates techniques used for many larger patterns.'),
'6446': (98, 'A defining quantum-complexity conjecture connecting robust verification, approximation hardness, and the structure of many-body Hamiltonians.'),
'6447': (79, 'Tests how far succinct interactive verification can extend to quantum proofs with explicit communication restrictions; affects a broad proof-system design space.'),
'6448': (95, 'Separates quantum from classical witnesses and therefore addresses a basic source of quantum computational power.'),
'6449': (87, 'Asks whether quantum information can encode useful nonuniform computational advice beyond classical advice of comparable size.'),
'6450': (91, 'A general classical-versus-quantum comparison across all total communication problems, with a sharp distinction from promise-problem separations.'),
'6451': (66, 'Determines the statistical power of a standard restricted private-query interface; valuable as a precise mechanism-design benchmark.'),
'6452': (66, 'Determines the limits of the pure-private Laplace query interface, isolating what stronger mechanisms would have to add.'),
'6453': (95, 'Links average-case NP hardness to the existence of a basic cryptographic primitive; resolving it would clarify the foundations of complexity-based cryptography.'),
'6454': (87, 'Would connect worst-case coding hardness to a central average-case cryptographic assumption in a concrete low-noise regime.'),
'6455': (84, 'Tests the efficiency limits of the IP = PSPACE phenomenon when both verifier and prover costs matter, across the full time range.'),
'6456': (78, 'Higher-dimensional expansion for a structured algebraic code family is a reusable ingredient for robust tests and related constructions.'),
'6498': (97, 'Dynamic optimality is a central benchmark for adaptive data structures: one simple online BST would compete with every offline BST on every access sequence.'),
'6499': (89, 'A basic randomized symmetry-breaking question on arbitrary graphs whose resolution would sharpen the global locality frontier.'),
'6500': (93, 'Connects extremal graph density with the optimal size of sparse distance-preserving structures; consequences extend across graph theory and algorithms.'),
'6501': (79, 'Asks whether all-to-all communication suffices for constant-round symmetry breaking, sharply testing the congested-clique model.'),
'6502': (61, 'Isolates the cost of stable item handles in an external-memory priority queue; a useful model distinction with more limited scope than general I/O lower bounds.'),
'6503': (94, 'A widely reusable fine-grained hardness hypothesis underlying trade-offs for many dynamic problems; its consequences reach well beyond matrix-vector multiplication.'),
'6504': (94, 'A canonical deterministic parallel-algorithm and derandomization question for a basic graph optimization problem.'),
'6505': (88, 'A small connectivity promise problem serves as a basic round-complexity benchmark for low-memory massively parallel computation.'),
'6506': (87, 'Matching a logarithmic deterministic bound for MIS would settle a central gap in local symmetry breaking.'),
'6507': (92, 'Combining near-linear work with polylogarithmic depth for directed reachability would resolve a major barrier in efficient parallel graph algorithms.'),
'6508': (81, 'A longstanding concrete stress test for splay-tree adaptivity, already on the elementary deque interface; less sweeping than dynamic optimality.'),
'6509': (76, 'A precise decomposition property of splaying that could illuminate the structural arguments needed for broader adaptive-search conjectures.'),
'6510': (97, 'Truly subcubic exact weighted APSP is a central fine-grained benchmark with consequences for a large family of graph and matrix problems.'),
'6511': (92, 'General Exact Matching is a clean test of removing randomness from algebraic graph algorithms beyond the bipartite setting.'),
'6512': (79, 'A sharply stated linear-cost conjecture for structured access sequences, probing whether splaying exploits an unknown traversal tree.'),
'6513': (87, 'Asks whether a basic measure of reusable string structure can be approximated within a constant, linking compression and approximation complexity.'),
'6514': (68, 'Tests optimality of one particularly simple self-adjusting heap against an established model barrier; a focused algorithm-analysis question.'),
}
LANDMARKS = {
'0001': (100, 'The central boundary between efficiently solving a problem and efficiently checking a proposed solution; consequences span nearly all of TCS.'),
'0002': (96, 'Tests whether efficient certificates exist symmetrically for yes and no answers, with broad implications for complexity and proof systems.'),
'0003': (97, 'Asks whether polynomial-time randomness can always be eliminated, a foundational computational-model comparison.'),
'0004': (94, 'A basic deterministic-versus-nondeterministic space question, captured by directed reachability.'),
'0005': (96, 'A central algebraic complexity separation with broad consequences for arithmetic computation and polynomial families.'),
'0006': (96, 'A major organizing conjecture for approximation thresholds and the limits of efficient optimization.'),
'0007': (98, 'The exponent of matrix multiplication governs a fundamental algebraic primitive and the running times of many other algorithms.'),
'0008': (97, 'Asks whether linear programming admits a running time independent of coefficient bit length in the strongly polynomial sense; a central optimization-model gap.'),
'0009': (80, 'A concrete explicit arithmetic lower-bound target that tests the strength of current algebraic complexity techniques.'),
'0010': (85, 'Superlinear explicit arithmetic lower bounds would break a basic barrier in understanding the cost of polynomial computation.'),
'0011': (92, 'A central existence question for a strong and widely studied fairness guarantee for indivisible goods.'),
'0012': (97, 'Connects worst-case hardness to typical-case hardness, a foundational gap affecting algorithms and cryptography.'),
'0013': (91, 'Efficient explicit tree codes would give a fundamental construction for reliable interactive communication.'),
'0014': (68, 'A sharply defined monotone formula lower-bound target for a basic Boolean function; informative but narrower than unrestricted circuit barriers.'),
'0015': (96, 'An explicit superlinear Boolean circuit lower bound would cross a basic barrier in unrestricted circuit complexity.'),
'0016': (96, 'Strong circuit lower bounds for SAT would establish a sweeping limitation on nonuniform efficient computation.'),
'0017': (88, 'A structural conjecture about formula composition that could turn local lower bounds into stronger general formula lower bounds.'),
'0018': (90, 'Tests whether two-sided efficiently checkable evidence guarantees efficient computation, with relevance to total search and cryptographic candidates.'),
'0019': (84, 'Separates computation with reuse from formula computation, a basic structural distinction in circuit complexity.'),
'0020': (92, 'Tests the power of polynomial-size nonuniform computation against exponential-time computation, a central circuit lower-bound question.'),
'0021': (98, 'Nonuniform circuits for NP probe a foundational hardness boundary even stronger than the uniform P-versus-NP separation.'),
'0022': (97, 'Asks whether worst-case NP hardness suffices for one-way functions, directly connecting complexity theory to the existence of cryptography.'),
'0023': (87, 'Efficiently learning DNF is a central computational learning benchmark whose structure recurs across learning models.'),
'0024': (84, 'Would connect circuit hardness with the power of propositional proof systems, transferring progress between two difficult lower-bound areas.'),
'0025': (94, 'Superpolynomial Frege lower bounds are a central barrier in propositional proof complexity.'),
'0026': (89, 'Tests whether randomness helps space-bounded computation, a fundamental counterpart to polynomial-time derandomization.'),
'0027': (74, 'A basic quantum transformation problem under black-box access, clarifying what an oracle interface permits.'),
'0028': (67, 'Separates two quantum oracle access conventions, a precise model question whose scope is narrower than general quantum speedups.'),
'0029': (90, 'Determines the strongest quantum query advantage when the function has no promise, a basic limit on quantum computation.'),
'0030': (70, 'An oracle benchmark for the reach of efficient-prover interactive verification of quantum computation.'),
'0031': (77, 'A model-relative separation probing the relation between quantum computation and classical interactive proofs.'),
'0032': (65, 'A concrete test of whether a celebrated quantum traversal advantage extends to producing an entire path.'),
'0033': (86, 'Relates quantum query algorithms to polynomial approximation, connecting two core tools for quantum upper and lower bounds.'),
'0034': (77, 'Characterizes simultaneous time and memory limits for basic quantum collision tasks, beyond query complexity alone.'),
'0035': (65, 'A specific sampling benchmark that can clarify the computational meaning of cross-entropy performance.'),
'0036': (97, 'Asks whether quantum polynomial-time computation is more powerful than randomized classical computation.'),
'0037': (95, 'Tests whether quantum computation can efficiently solve every efficiently verifiable search-decision problem.'),
}

def assessment(score, reason):
    return dict(score=score, method='editorial', reason=reason, assessed_on='2026-09-10')

if __name__ == '__main__':
    for path in (BASE / 'cards').glob('*.json'):
        card = json.loads(path.read_text())
        card['importance'] = assessment(*REVIEWED[card['id'].split('-')[1]])
        path.write_text(json.dumps(card, ensure_ascii=False, indent=2))
    overrides = {'TCS-'+key: assessment(*value) for key, value in LANDMARKS.items()}
    (BASE / 'importance_overrides.json').write_text(json.dumps(overrides, ensure_ascii=False, indent=2))
