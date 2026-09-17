"""Select semiprime factoring and the cryptographically relevant GapSVP scale."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0656';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A classical reduction from semiprime factoring to polynomial-gap SVP',
 status='source_open',criterion='reductions',question_type='yes_no',
 formal=r'''Do there exist an absolute rational constant \(\varepsilon>0\) and one classical randomized polynomial-time oracle algorithm that factors every integer \(N=pq\), where \(p\ne q\) are primes, using an oracle for Euclidean \(\operatorname{GapSVP}_{n^{2+\varepsilon}}\)?

Here \(n\) is the rank of the lattice in each oracle query, and the algorithm must output the two prime factors with probability at least \(2/3\) on every promised input \(N\). The oracle may answer arbitrarily inside its approximation gap.''',
 definitions=r'''The factoring input is just the binary representation of an integer \(N\ge6\), promised to be the product of two distinct primes. The factors, their bit lengths and any auxiliary information are not supplied. They need not have equal bit length, and the target is worst-case correctness over all such products, not only randomly sampled or balanced ones. Put \(s=\lceil\log_2(N+1)\rceil\). A valid output is a pair of binary integers \((a,b)\), in either order, with \(1<a,b<N\), \(ab=N\), and both entries prime. Under the promise any nontrivial factor determines the required pair.

A well-formed lattice query is an explicit integer matrix \(B\in\mathbb Z^{m\times n}\), with linearly independent columns and \(m\ge n\ge1\), together with a positive rational \(r\). Matrix entries are signed binary integers; \(r\) is given by a binary numerator and positive binary denominator. The dimensions and all entries are included in a length-delimited encoding. Define
\[
\mathcal L(B)=\{Bz:z\in\mathbb Z^n\},\qquad
\lambda_1(\mathcal L(B))=\min_{z\in\mathbb Z^n\setminus\{0\}}\|Bz\|_2,
\]
where \(\|v\|_2=(\sum_i v_i^2)^{1/2}\). An admissible \(\operatorname{GapSVP}_{n^{2+\varepsilon}}\) oracle \(O\) is any total Boolean function obeying
\[
O(B,r)=1\quad\text{if }\lambda_1(\mathcal L(B))\le r,
\qquad
O(B,r)=0\quad\text{if }\lambda_1(\mathcal L(B))>n^{2+\varepsilon}r.
\]
For \(r<\lambda_1\le n^{2+\varepsilon}r\), either answer is permitted. No oracle correctness is required on malformed queries. The real-valued factor in this definition is an exact promise threshold; no numerical approximation oracle is supplied.

The reduction is one uniform probabilistic multitape Turing machine \(R\), with independent fair random bits, and constants \(K,c>0\), such that for every promised \(N\) and every admissible \(O\), every execution of \(R^O(N)\) uses at most \(K(s+1)^c\) bit operations and outputs the prime factors with probability at least \(2/3\). Writing queries, reading their one-bit answers and writing the factors count toward the running time; the oracle's internal computation does not. Adaptive polynomially many queries are allowed. In particular query rank, ambient dimension and full bit length are all polynomially bounded in \(s\). The same fixed \(\varepsilon,K,c,R\) must work for all \(N\) and every completion of the oracle's gap answers. There is no quantum computation, advice, factoring hint or additional oracle.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the existence of the stated classical randomized reduction, including its query encodings, bit complexity and success guarantee for every promised semiprime and every admissible oracle, or a proof that no such fixed ε and reduction exist. An unproved heuristic lattice embedding, an exponential-time reduction, a reduction to exact SVP only, or a quantum factoring algorithm does not establish this target.',
 why='This would connect two major sources of computational hardness: factoring integers and approximating shortest lattice vectors by a large polynomial factor. The selected approximation regime is strong enough to connect onward to classical worst-case-to-average-case reductions used for lattice cryptography.',
 source_formulation=dict(text='Open Problem 4.10 asks for a classical reduction from factoring or discrete logarithms to polynomial-gap SVP and singles out the factor n^(2+ε). This card selects factoring of two distinct primes and a bounded-error polynomial-time oracle reduction.',caption='The Complexity of the Shortest Vector Problem, §4.3, Open Problem 4.10, printed p.17 / PDF p.19.',citation='primary',format='editorial_paraphrase'),
 references=[ref('primary','The Complexity of the Shortest Vector Problem','Huck Bennett',2023,'https://www.cs.umd.edu/~gasarch/open/svp-color.pdf','24 January 2023 full version; §1.1 lattice definitions, §4.1 polynomial-gap worst-case/average-case context and §4.3 Open Problem 4.10, printed pp.17–18 / PDF pp.19–20')],
 context_blocks=[
 block('The source offers factoring and discrete logarithms as alternative starting problems. This card fixes semiprime factoring, so a proof need not also establish a discrete-logarithm reduction.'),
 block('The target is the decision promise problem with a large multiplicative gap. An oracle for exact shortest vectors is substantially stronger and cannot simply be substituted for this oracle.'),
 block('The source highlights n^(2+ε) because known classical reductions connect this approximation regime to learning with errors. The input parameter in that factor is the queried lattice rank, not the number of bits of the integer being factored.'),
 block('Quantum reductions would give no comparable evidence: a quantum algorithm can already factor without a lattice oracle. Requiring a classical reduction is therefore essential to the requested connection.'),
 block('Using lattices as a heuristic component of a factoring algorithm does not by itself prove a worst-case reduction to this approximate decision oracle. Both the embedding guarantee and the polynomial bound must hold for every promised input.'),
 ],
 progress=[progress('2023','The survey explicitly asks for the classical connection and identifies n^(2+ε)-GapSVP as a particularly relevant target.')],
),[
 'Selected semiprime factoring after the optional source-problem question received no reply; applied the announced editorial default, not user confirmation.',
 'Retained the source’s n^(2+ε) scale for some fixed ε > 0 and distinguished lattice rank from factoring input length.',
 'Defined explicit Euclidean lattice queries, exact yes/no thresholds and arbitrary answers throughout the promise gap.',
 'Specified one uniform classical randomized oracle reduction, polynomial bit cost and per-input success for every oracle completion.',
 'Preserved the assessed importance and required a complete Lean-checked reduction or negation.',
],[
 'Read the survey’s §1.1 definitions, §4.1 approximation-scale discussion and all of Open Problem 4.10 with its following classical/quantum and heuristic-factoring qualifications.',
 'Bounded later-work searches through 17 September 2026 did not locate a verified classical polynomial-time reduction matching this target; implementations and heuristic factoring embeddings are not treated as such a result.',
], 'Source-open in Bennett’s Open Problem 4.10. The card selects semiprime factoring and the highlighted n^(2+ε) approximation factor, using an announced editorial default after an unanswered optional question. Quantum factoring and heuristic lattice embeddings do not settle the classical oracle reduction. Bounded later-work checks through 17 September 2026 found no verified matching resolution.',summary=[
 'The input is an integer promised to be the product of two distinct primes.',
 'The goal is to recover its factors with a classical randomized algorithm taking polynomial time in the integer’s bit length.',
 'The algorithm may query Euclidean GapSVP at approximation factor n^(2+ε), for some fixed ε > 0 and query rank n.',
 'It must succeed on every promised semiprime regardless of how the oracle answers inside its approximation gap.',
 'This would connect factoring to a lattice regime relevant for classical cryptographic reductions; a complete Lean-checked proof or refutation is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
