"""Complete simultaneous single-exponential time and polynomial space for SVP."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6619'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved exact Euclidean shortest-vector search, allowing classical randomization, with both resource bounds on the same algorithm.',
 'Specified full rational basis encoding, lattice rank versus ambient dimension, integer-coordinate output and the exact squared-norm success condition.',
 'Charged all stored bits, retained randomness, precision, preprocessing and output time; required worst-case resources on every tape and success separately on every valid basis.',
 'Made the constants absolute and allowed any fixed exponential base; the target is not specifically a base-two running time.',
 'Checked the 2026 memory-saving proposal at its actual algorithm and complexity sections, which do not establish the required all-lattices exact-success theorem.',
 'Distinguished conditional cryptographic time-space evidence from an unconditional negative result and added complete Lean-checked acceptance; preserved importance 95.',
]
sources=[
 'Read Micciancio–Voulgaris, ECCC TR10-014 revision 1 (3 March 2012), abstract, introduction, §2 lattice-problem and precision conventions, and §6 p. 22. The explicit open question asks for simultaneous single-exponential time and polynomial space. The paper permits polynomial dependence on coefficient precision and ambient dimension. Checked the journal metadata: SIAM Journal on Computing 42(3), 1364–1391 (2013), DOI 10.1137/100811970.',
 f'Read Micciancio’s live Lattice Links SVP and Enumeration pages on {DATE}, including the exact-algorithm comparison and polynomial-space open problem. These pages are undated and their practical-performance discussion is not used as current quantitative evidence.',
 'Read Koyuncu–Linker–Ozel, JP Journal of Geometry and Topology 32(1), 19–31, DOI 10.17654/0972415X26002, published 6 January 2026, abstract, §3 pp. 26–27 and §4 pp. 27–29. The PDF was available through web extraction although direct download returned 403. Step 6 leaves a stopping threshold unspecified; the polynomial-memory regime assumes replacement of most stored vectors and does not give an input-uniform exact-success probability and bit-time theorem. This scope assessment does not purport to refute all mathematical claims of the paper.',
 'Read the primary abstract and revision metadata for Albrecht–Lai–Postlethwaite, ePrint 2026/187, received 5 February and revised 7 June 2026, and Albrecht’s explanatory article dated 12 June. Checked CRYPTO 2026 publication metadata, pp. 232–262, DOI 10.1007/978-3-032-35377-1_8. The implications rely on space-time hardness conjectures and are not unconditional resource lower bounds; the full reduction proof was not certified.',
 f'Bounded primary-source searches through {DATE} found recent deterministic-hardness and approximation work and the above memory-saving proposal, but no algorithm meeting the selected exact simultaneous bounds. No NP-hardness statement is treated as ruling out exponential time.',
]
status='The checked primary sources continue to distinguish single-exponential algorithms using exponential space from polynomial-space enumeration. The January 2026 proposal does not provide the universal exact-success and bit-resource theorem required here, and the CRYPTO 2026 result relies on conjectured time-space hardness. No resolution of the stated target was found in the bounded search.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',year=2026,
 formal=r'''Do there exist one randomized classical algorithm \(A\) and absolute integers \(C,d\ge1\) such that, for every rational lattice basis \(B\in\mathbb Q^{m\times n}\) with linearly independent columns and total binary encoding length \(L\), the algorithm finds an exact shortest nonzero vector of \(\Lambda(B)\) with probability at least \(2/3\), while using simultaneously at most
\[
2^{Cn}L^d\quad\text{bit operations}
\qquad\text{and}\qquad
L^d\quad\text{bits of working space}?
\]
Both bounds must hold on every random tape. The exponent parameter \(n\) is lattice rank, and every \(m\ge n\ge1\) and every valid coefficient encoding are included.''',
 definitions=r'''The input explicitly gives \(m,n\) and every entry of \(B\), in column or row order fixed by the encoding. A rational entry is a signed binary numerator divided by a positive binary denominator, using canonical integer encodings and unambiguous boundaries. Reduction to lowest terms is not required. The bit length \(L\) includes all entries and dimension data; the input is not a generating circuit or an oracle. Full column rank and \(m\ge n\ge1\) are promises. No behavior on unpromised inputs is required for the target.

The rank-\(n\) lattice is
\[
\Lambda(B)=\{Bz:z\in\mathbb Z^n\}\subseteq\mathbb R^m.
\]
The columns are linearly independent over the rationals, equivalently over the reals, so \(Bz\ne0\) for every nonzero integer coordinate vector \(z\). With the Euclidean norm \(\|v\|_2=(\sum_{i=1}^m v_i^2)^{1/2}\), define
\[
\lambda_1(\Lambda(B))=
\min_{z\in\mathbb Z^n\setminus\{0\}}\|Bz\|_2.
\]
Full rank makes this a discrete lattice in its linear span, so the positive minimum is attained.

Successful output is a finite binary encoding of a nonzero integer vector \(z\in\mathbb Z^n\) with \(\|Bz\|_2=\lambda_1(\Lambda(B))\). Equivalently, it satisfies the exact rational inequalities
\[
\forall u\in\mathbb Z^n\setminus\{0\},\qquad
\sum_{i=1}^m(Bz)_i^2\le\sum_{i=1}^m(Bu)_i^2.
\]
Any minimizer is acceptable, including either sign and any of several shortest vectors. The integer coordinates refer to the input basis. An approximate length, a short vector with a factor greater than one, or a real-valued coordinate approximation is not this output. The algorithm may report failure or return a nonoptimal vector on unsuccessful executions; all executions remain subject to both resource bounds.

Use a uniform probabilistic multitape Turing machine with read-only input, write-only output and a one-way stream of independent fair random bits. Working space counts every used work-tape bit, including saved random bits, counters, intermediate vectors, basis transformations and precision data. The random source cannot be revisited as free writable storage. No external writable memory, preprocessing oracle or nonuniform advice is available. Input and final output tapes are not counted as working storage, but every operation reading or writing them counts toward time. All arithmetic is charged in bit operations; arbitrary-precision arithmetic is not a unit-cost instruction.

The success probability is at least \(2/3\) separately for every fixed valid input, over the machine’s internal random bits. The time and space bounds are worst-case over those bits, including unsuccessful executions, and include preprocessing and all precision management. The same constants \(C,d\) apply to all ranks, ambient dimensions and coefficient lengths. Different fixed polynomial exponents for time and space can be absorbed into one \(d\). A deterministic algorithm qualifies as a special case.

No uniqueness, reduced-basis, random-lattice or special-lattice promise is imposed. The desired exponential base is any absolute constant \(2^C\); no particular base such as two is required. The task is an exact search-algorithm existence proposition, not a separate numerical approximation of \(\lambda_1\).''',
 answer_criterion=r'''Supply an algorithm and complete Lean-checked proofs of both simultaneous resource bounds and its exact success probability on every valid rational basis. Alternatively, supply a complete Lean-checked proof that no algorithm and absolute constants \(C,d\) satisfy the displayed requirements.

A single-exponential algorithm using exponential space, a polynomial-space algorithm with \(2^{\Theta(n\log n)}\) time, a heuristic or average-case guarantee, or an approximation algorithm does not settle the question. A counterexample to one enumeration or sieving procedure does not rule out all algorithms. A lower bound conditional on an unproved lattice-hardness assumption is not an unconditional negative resolution.''',
 source_formulation=dict(text='The inherited paper’s open-problems section asks for an algorithm using single-exponential time and polynomial space simultaneously. Micciancio’s SVP problem page singles out that question for shortest-vector search. The card retains exact Euclidean SVP and its previously selected randomized, worst-case resource convention.',caption='Paraphrase of Micciancio–Voulgaris, ECCC revision 1, §6 p. 22, and the author’s SVP page, Open Problems.',citation='primary',format='editorial_paraphrase'),
 why='The problem asks whether exact lattice search can retain a single-exponential time bound while avoiding an exponentially large stored collection. It separates two major resource regimes in lattice algorithms and helps clarify which memory assumptions matter when interpreting lattice-based computational hardness.',
 references=[
 ref('primary','A Deterministic Single Exponential Time Algorithm for Most Lattice Problems based on Voronoi Cell Computations','Daniele Micciancio; Panagiotis Voulgaris',2013,'https://eccc.weizmann.ac.il/report/2010/014/revision/1/','ECCC TR10-014 revision 1, 3 March 2012; §2 precision convention and §6 p. 22; SIAM Journal on Computing 42(3), 1364–1391 (2013), DOI 10.1137/100811970; STOC 2010 precursor'),
 ref('problem','Shortest Vector Problem (SVP) — Lattice Links','Daniele Micciancio',None,'https://cseweb.ucsd.edu/~daniele/LatticeLinks/SVP.html',f'Undated author-maintained page, accessed {DATE}; Exact Algorithms and the first item under Open Problems'),
 ref('enumeration','Lattice Enumeration Algorithms','Daniele Micciancio',None,'https://cseweb.ucsd.edu/~daniele/LatticeLinks/Enum.html',f'Undated author-maintained page, accessed {DATE}; Provable algorithms and the distinction from heuristic pruning'),
 ref('sheaf','A Sheaf-Theoretic and Etalé Space Approach to the Shortest Vector Problem: Orthogonalization, Coboundary Maps, and Memory-Efficient Sieving','Selcuk Koyuncu; Patrick Linker; Cenap Ozel',2026,'https://pphmjopenaccess.com/jpjgt/article/download/3968/1901/11504','JP Journal of Geometry and Topology 32(1), 19–31; published 6 January 2026; DOI 10.17654/0972415X26002; §3 pp. 26–27 and §4 pp. 27–29, especially the stopping step and conditional memory regime'),
 ref('hinted','Hardness of hinted ISIS from the space-time hardness of lattice problems','Martin R. Albrecht; Russell W. F. Lai; Eamonn W. Postlethwaite',2026,'https://eprint.iacr.org/2026/187','Received 5 February 2026, revised 7 June; primary abstract and revision metadata; CRYPTO 2026, 232–262, DOI 10.1007/978-3-032-35377-1_8; author explanation dated 12 June 2026'),
 ],
 context_blocks=[
 block('A lattice contains all integer combinations of its basis vectors. Those combinations may be much shorter than any input column, so finding the shortest nonzero combination is not the same as inspecting the basis.'),
 block(r'The inherited Voronoi-cell algorithm achieves deterministic single-exponential time with exponential storage. Its open-problems section explicitly asks whether the same broad time scale can be combined with polynomial space.'),
 block(r'Polynomial-space enumeration has proved bounds of the form \(n^{O(n)}=2^{O(n\log n)}\). Practical pruning can improve observed performance but does not supply the missing universal \(2^{O(n)}\) bound.','enumeration'),
 block('The January 2026 sheaf-based proposal describes a memory-saving regime and an iteration scheme. The inspected sections do not specify and prove an all-input stopping bound with exact success probability while retaining polynomial bit space, so they do not establish this card’s theorem.','sheaf'),
 block('The 2026 hinted-ISIS work relates cryptographic assumptions to conjectured time-space hardness of lattice problems. It provides conditional evidence and implications, rather than a proof that the algorithm on this card cannot exist.','hinted'),
 ],
 progress=[
 progress('2010–2013','The Voronoi-cell work obtains deterministic single-exponential algorithms with exponential space and states the simultaneous polynomial-space question.'),
 progress('2015','The enumeration overview records refined practical preprocessing with the same superexponential proved time scale.','enumeration'),
 progress('2026-01-06','A sheaf-based proposal discusses memory reduction without establishing the full exact all-input resource-and-success theorem.','sheaf'),
 progress('2026-06-07','The revised hinted-ISIS manuscript studies consequences of conjectured space-time hardness; published at CRYPTO 2026.','hinted'),
 ],
),notes,sources,status,summary=[
 'An input basis generates a lattice by taking all integer combinations of its rational columns.',
 'The algorithm must output coordinates of an exactly shortest nonzero Euclidean lattice vector, with success probability at least two thirds.',
 'One uniform algorithm must use single-exponential time in the lattice rank and polynomial working space in the full input length simultaneously.',
 'Both resource bounds include preprocessing, arithmetic precision and unsuccessful random executions.',
 'A complete Lean-checked proof must establish those guarantees or their impossibility; exponential storage, approximation and heuristic memory savings do not meet the target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
