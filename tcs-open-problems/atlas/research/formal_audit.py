"""Individually specified resolution criteria for the approved editorial cards."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from publish import publish, CARDS

CRITERIA = {
 'TCS-6446': 'Prove QMA-hardness for some fixed locality and positive constant normalized promise gap under polynomial-time many-one reductions, or prove that no such constants give QMA-hardness. An inverse-polynomial gap alone does not settle the proposition.',
 'TCS-6448': 'Prove QMA is contained in QCMA, or prove the existence of a promise problem in QMA outside QCMA. A separation relative to an oracle does not settle these unrelativized classes.',
 'TCS-6449': 'Prove that polynomial classical advice suffices for every language decidable with polynomial quantum advice, or prove a separation of the two unrelativized advice classes.',
 'TCS-6450': 'Establish one polynomial bound valid for every finite total Boolean communication problem, or prove that no universal polynomial bound holds. Promise problems and restricted subclasses do not suffice.',
 'TCS-6451': 'Construct an algorithm and a universal constant bounding expected excess loss by the displayed rate for every admissible loss family and privacy budget, or prove that no such uniform bound is possible in the Gaussian-query model.',
 'TCS-6452': 'Construct a query-only algorithm with the displayed expected-loss guarantee for every finite loss family, or prove that no universal constant in that guarantee is possible. Allowing another way to read the database changes the problem.',
 'TCS-6455': 'Prove the specified verifier/prover time guarantees for every polynomial-space language and its time bound, or prove the negation of that universal statement. Improving only a restricted range of T is partial progress.',
 'TCS-0611': 'Establish a deterministic polynomial-time decision algorithm for every bipartite instance, or prove that none exists. The April 2026 claimed algorithm would establish the positive answer if its proof is valid; this catalogue has not independently verified it.',
 'TCS-2997': 'Determine a function f(n) with an O(f(n))-round randomized algorithm and an Omega(f(n)) worst-case lower bound for every randomized algorithm in the stated model, up to constant factors. Either a faster algorithm or a stronger lower bound alone is partial progress.',
 'TCS-6501': 'Construct one randomized algorithm whose round bound is constant on every input graph, with the stated high-probability guarantee, or prove that constant rounds cannot suffice for all graphs in this model.',
 'TCS-6506': 'Give one deterministic LOCAL algorithm with a uniform O(log n) bound over all graphs and valid identifiers, or prove that no such algorithm exists. Constants must not depend on maximum degree.',
 'TCS-6499': 'Give one randomized LOCAL algorithm with a uniform o(log n) round bound and the stated success probability on all graphs, or prove that no such algorithm exists. A degree restriction does not settle the proposition.',
 'TCS-6500': 'Prove the required graph families exist for every fixed k, or refute the universal claim for at least one fixed k. Proving the k=4 case alone would resolve the first unknown case but not the whole conjecture.',
 'TCS-1468': 'Construct a data structure meeting both the stated space bound and worst-case reporting bound for every point set and rectangle, or prove that these bounds cannot be achieved together in the specified model.',
 'TCS-6504': 'Construct a logspace-uniform polynomial-size, polylogarithmic-depth circuit family for general-graph perfect-matching search, or prove that none exists. Quasipolynomial size or a bipartite-only algorithm does not meet the target.',
 'TCS-0466': 'Give a deterministic O(n log n)-time verifier for every supplied string and modulus, or prove that no such verifier exists in the stated word-RAM model. Certifying a replacement composite fingerprint does not answer this question.',
 'TCS-6502': 'Construct a deterministic priority queue satisfying every stated operation and space bound with all stable-handle costs charged, or prove that no such structure exists in the fixed external-memory model.',
 'TCS-6505': 'Prove the logarithmic lower bound for every fixed sublinear-memory exponent and every admissible randomized algorithm, or refute that universal lower bound. An o(log n)-round algorithm for one fixed exponent would suffice for a refutation.',
 'TCS-6503': 'Give an algorithm with a fixed positive polynomial saving in the total time, including preprocessing, or prove that no such randomized algorithm exists. A subpolynomial saving does not refute the OMv conjecture.',
 'TCS-6507': 'Construct an algorithm meeting the work, depth, and error guarantees simultaneously on all directed inputs, or prove that no such algorithm exists in the specified PRAM model. Work measured by transitive-closure size is insufficient.',
 'TCS-1141': 'Give a randomized algorithm and one absolute constant C meeting the displayed guarantee in near-linear time on every directed graph, or prove that no constant approximation is possible with that time bound.',
 'TCS-6508': 'Prove a universal O(n+m) total bound for the specified splay implementation, or prove that the ratio between total cost and n+m is unbounded over legal initial trees and operation sequences.',
 'TCS-6498': 'Prove one universal constant competitive bound with the stated additive initialization term, or prove that the ratio cost_splay/(OPT+n) is unbounded over initial trees and access sequences.',
}

EDITS = {
 'TCS-2997': {
  'formal': r'For arbitrary simple undirected n-vertex networks, determine the optimal worst-case randomized round complexity of triangle detection in CONGEST, up to constant factors. Each vertex initially knows its distinct O(log n)-bit identifier and its neighbors, and may send a separate O(log n)-bit message in each direction of every incident edge per synchronous round. On a triangle-free graph all vertices must output NO; otherwise at least one must output YES. The joint answer must be correct with probability at least 2/3 on every input and identifier assignment. The algorithm is uniform, has private random bits, and may know n. The currently established bounds are $\Omega(\log\log n)$ and $\widetilde O(n^{1/3})$.',
  'question_type': 'asymptotic_complexity'},
 'TCS-6501': {
  'formal': r'Is there a randomized algorithm that, on every n-vertex simple input graph, finds a maximal independent set in O(1) rounds in the Congested Clique model, with success probability at least $1-n^{-c}$ for every requested fixed $c>0$? Processor v initially knows its identifier and incident input edges. Every ordered pair of processors may exchange an O(log n)-bit message per synchronous round, whether or not the input edge exists. Each processor outputs whether it belongs to an independent set that dominates every vertex outside it. The algorithm must be uniform across inputs; it cannot be chosen after seeing the graph.'},
 'TCS-6505': {
  'formal': r'For every fixed $0<\delta<1$, must every randomized MPC algorithm distinguishing one n-cycle from two vertex-disjoint (n/2)-cycles use $\Omega(\log n)$ rounds in the worst case over even n and input placement? Each machine has $O(n^\delta)$ words and total memory is O(n) words. Require success probability at least $1-n^{-c}$ for each requested fixed $c>0$. An $o(\log n)$-round algorithm for one fixed $\delta<1$ would refute this lower-bound conjecture.'},
 'TCS-1141': {
  'title': 'Can reachability diameter be approximated within a constant in near-linear time?',
  'formal': r'For an unweighted directed graph $G=(V,E)$, define $D(G)=\max\{d_G(u,v):d_G(u,v)<\infty\}$. Is there an absolute constant $C\ge1$ and one randomized word-RAM algorithm that, on every input, returns an estimate $D(G)/C\le\widehat D\le D(G)$ with probability at least 2/3 in $\widetilde O(n+m)$ worst-case time? Here $n=|V|$, $m=|E|$, words have $\Theta(\log n)$ bits, and self-distances are included, giving D(G)=0 on an edgeless graph. The constant and the hidden logarithmic exponent are independent of G.'},
}

APPEND = {
 'TCS-6446': 'Input terms and thresholds have polynomial-bit descriptions and m is polynomial in n. QMA-hardness means hardness for every QMA promise problem under polynomial-time many-one reductions.',
 'TCS-6448': 'Use uniform polynomial-time quantum verification, completeness at least 2/3 and soundness at most 1/3, with no shared advice or oracle. Classes here contain promise problems; the witness may depend on the whole input.',
 'TCS-6449': 'The quantum computation is uniform and polynomial time, with error at most 1/3 on every input. Advice size is bounded by one polynomial. There is no computability restriction on the length-indexed advice family and no oracle.',
 'TCS-6450': 'X and Y are arbitrary finite sets. Cost is the worst-case total number of communicated bits or qubits, and error at most 1/3 is required on every input pair. Public random bits and prior entanglement, respectively, are not charged as communication.',
 'TCS-6451': 'The guarantee is uniform over all finite candidate sets of size at least two and all positive rho. Query choice can depend on public losses and earlier answers; all database access must pass through the stated Gaussian oracle. The expectation is over all algorithm and oracle randomness. No computation-time bound is imposed.',
 'TCS-6452': 'The algorithm chooses a finite positive integer k from public information before reading any answers. Each noise draw is independent with density exp(-|z|/k)/(2k). Query choices may depend on earlier answers. The expectation includes oracle and algorithm randomness; the hidden constant is independent of the candidate set and losses. No computation-time bound is imposed.',
 'TCS-6455': 'Use uniform classical randomized verification with completeness at least 2/3 and soundness at most 1/3. For every polynomial-space decider with time-constructible bound T(n) at least n, a protocol with the stated bounds is sought. Polynomial exponents may depend on the decider, but not on n.',
 'TCS-6506': 'Nodes may know n and the maximum degree; the time guarantee must still be O(log n) uniformly over degrees.',
 'TCS-6499': 'Nodes may know n and the maximum degree. Both the algorithm and the asymptotic time bound are uniform over input graphs and valid identifier assignments.',
 'TCS-1468': 'The target is deterministic exact reporting with polynomial preprocessing time, using the usual word-RAM operations: arithmetic, multiplication, bitwise Boolean operations, shifts, comparisons, and indirect addressing on a constant number of words.',
 'TCS-6504': 'Use Boolean circuits with bounded fan-in and logspace-uniform descriptions. An output lists matching edges or a distinguished symbol for nonexistence.',
 'TCS-6507': 'For definiteness fix a CREW PRAM: concurrent reads are allowed, and concurrent writes to one cell are prohibited. Word operations are arithmetic, multiplication, bitwise operations, shifts, comparisons, and indirect addressing on a constant number of logarithmic-size words. The target permits the polylogarithmic overhead of simulating common alternative PRAM conventions.',
}

if __name__ == '__main__':
 for path in sorted(CARDS.glob('*.json')):
  c=json.loads(path.read_text()); identifier=c['id']
  if identifier not in CRITERIA: continue
  c.update(EDITS.get(identifier, {}))
  c.setdefault('question_type','yes_no')
  c['answer_criterion']=CRITERIA[identifier]
  c['formulation_reviewed_on']='2026-09-10'
  if identifier in APPEND and APPEND[identifier] not in (c.get('definitions') or ''):
   c['definitions']=((c.get('definitions') or '')+'\n\n'+APPEND[identifier]).strip()
  path.write_text(json.dumps(c,ensure_ascii=False,indent=2))
  publish()
