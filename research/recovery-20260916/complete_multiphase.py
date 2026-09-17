"""Complete the charged word-RAM formulation of the multiphase conjecture."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7338';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the original three charged phases, polynomial number of sets and unrestricted adaptive word-RAM access, with the already selected Las Vegas expected-cost convention.',
 'Specified packed incidence inputs, public size parameters, phase information boundaries and the expectation over randomness inherited from earlier phases.',
 'Defined the normalized overhead directly and expanded the eventual lower bound and its exact negation; a negative answer need not supply one subpolynomial algorithm for every exponent.',
 'Read the original conjecture and distinguished the stronger cell-probe and number-on-forehead variants from the chosen target.',
 'Checked the semi-adaptive result and the 2025–2026 Inner Product advances; none has the unrestricted polynomial SetDisjointness conclusion.',
 'Preserved importance 94 and the Data structures category, with a complete Lean-checked resolution required.',
]
sources=[
 'Read Pătrașcu, STOC 2010, Towards Polynomial Lower Bounds for Dynamic Problems, §1.2 Conjecture 1 and Theorem 2 printed p. 2, §1.3 Theorem 3 and zero-error expected-time convention p. 3, and the distinct communication approach §1.4. The source uses k=Theta(n^gamma); the card retains its previously selected exact representative ceil(n^gamma).',
 'Read Ko–Weinstein, arXiv:1910.13543v1 of 29 October 2019, introduction pp. 1–3, especially Definition 1.3 and Theorem 1.4 p. 3. The query first probes the preprocessing memory and then the update layer, without returning to the former. Its lower bound has this restriction; no equivalence with unrestricted queries is asserted.',
 'Read the primary abstract of Ko, Lower Bounds for Linear Operators, ECCC TR25-155 published 22 October 2025, also arXiv:2509.02730. The claimed multiphase consequence uses Inner Product modulo two, superpolynomially many queries and a communication formulation, rather than the selected polynomial-set disjointness task. Full proof not independently audited.',
 'Read the primary abstract of Ko, Unifying the Landscape of Super-Logarithmic Dynamic Cell-Probe Lower Bounds, ECCC TR25-156 published 22 October 2025. The stated application is an approximately log^(3/2) lower bound for the Inner Product version. Full proof not independently audited.',
 'Read Ko, ECCC TR26-047, report dated 26 March 2026 and publication dated 5 April 2026, abstract and §1.1 Theorem 1.1 pp. 1–2. It states an Omega((log n/log log n)^2) bound for Inner Product over F2. The following paragraph expressly says Disjointness does not satisfy its general lifting criterion. No independent audit of the proof in §3 or Appendix B was undertaken.',
 f'Bounded primary-source searches through {DATE} found no verified unrestricted polynomial lower bound or counterexample for this charged SetDisjointness formulation. Related TCS-0557 is integer 3SUM, TCS-6540 is a static cell-probe question and TCS-7334 is a static set-disjointness space/time conjecture.',
]
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Do there exist real constants \(\gamma>1\) and \(\delta>0\) such that every admissible uniform, always-correct randomized word-RAM algorithm for the following three-phase problem, with \(k=\lceil n^\gamma\rceil\), satisfies
\[
 \tau_A(n)=\Omega(n^\delta)?
\]
Phase I receives \(S_1,\ldots,S_k\subseteq[n]\) and preprocesses them. Phase II receives \(T\subseteq[n]\) and updates the retained state. Phase III receives \(i\in[k]\) and answers whether \(S_i\cap T=\varnothing\). The normalized expected overhead is
\[
 \tau_A(n)=\max\left\{1,\frac{t_1(n)}{kn},\frac{t_2(n)}n,t_3(n)\right\},
\]
where \(t_j(n)\) is the worst-input expected number of instructions used in Phase \(j\), as defined below. The lower bound must hold for all sufficiently large integer \(n\), with no restriction on query adaptivity.''',
 definitions=r'''For each integer \(n\ge1\), let \([n]=\{1,\ldots,n\}\) and \(k=\lceil n^\gamma\rceil\). All subsets, including the empty set and the full universe, are permitted, and repetitions among the \(S_j\) are allowed. The first input is the concatenation of the \(k\) length-\(n\) incidence vectors in index order. The second input is the length-\(n\) incidence vector of \(T\). Each bit string is packed consecutively into words, with known zero padding in the last word. Phase III supplies the integer \(i\). The integer size parameters \(n,k\) are public from Phase I onward; the program is not required to compute \(\lceil n^\gamma\rceil\) from a real constant supplied as an oracle.

A candidate uses a fixed integer \(a\ge2\) and words of
\[
 w=\lceil a\log_2(n+k+2)\rceil
\]
bits. One finite program, with a fixed entry point for each phase, works for every \(n\) in this regime. The program may depend on the fixed regime \(\gamma\); it has no size-dependent advice or free precomputed table. The claim quantifies over every fixed \(a\) and every such uniform program.

The machine has word-sized registers and memory cells, with addresses fitting in one word. Unit-cost instructions are reads, writes, copies, comparisons, branches, addition, subtraction and multiplication modulo \(2^w\), unsigned quotient and remainder with nonzero divisor, bitwise Boolean operations and logical shifts. Shifts by at least \(w\) positions return zero. Producing an independent uniform random \(w\)-bit word also costs one instruction. Multiword computations cost their component instructions. Inputs are presented in explicit memory arrays at the start of their phase; all accesses, initialization performed by the program, table construction, copying, control and output are charged. Other memory initially contains zero. There is no extra free oracle for the sets.

Memory persists between phases. Phase I cannot see \(T\) or \(i\); Phase II cannot see \(i\). Phase III receives only \(i\), public size parameters and the retained memory, including any retained input arrays. Access to that state is charged in the usual way. Every phase may choose its next address adaptively using all information it has read. In particular, the query may alternate arbitrarily between information from the first two phases. There is no layering or nonadaptivity restriction.

Fix the entire input \((S_1,\ldots,S_k,T,i)\) independently of all random words. Each phase must terminate almost surely, and every terminating execution must return the correct disjointness bit. Deterministic algorithms are included. Let \(C_j\) be the random number of instructions in Phase \(j\). Define
\[
 t_1(n)=\max_{S_1,\ldots,S_k}\mathbb E[C_1],\qquad
 t_2(n)=\max_{S_1,\ldots,S_k,T}\mathbb E[C_2],\qquad
 t_3(n)=\max_{S_1,\ldots,S_k,T,i}\mathbb E[C_3].
\]
Each expectation includes the randomness in all preceding phases that determines the retained state, as well as new randomness in the current phase. There is no averaging over inputs and no conditioning on a favorable previous state. Infinite expectations are allowed and make the corresponding overhead infinite. The maxima range over all valid fixed inputs at that size.

The notation \(\tau_A(n)=\Omega(n^\delta)\) means that there exist \(c>0\) and an integer \(n_0\ge1\) such that \(\tau_A(n)\ge c n^\delta\) for every integer \(n\ge n_0\). These two constants may depend on the program and the fixed parameters. In contrast, \(\gamma\) and \(\delta\) must be chosen before quantifying over all programs and word-size constants. Preprocessing is part of the overhead; unrestricted preprocessing with only memory probes charged is a different, stronger-model conjecture.''',
 answer_criterion=r'''Provide a complete Lean-checked proof of this existence claim or of its logical negation in the stated model.

A positive answer must choose universal \(\gamma>1\) and \(\delta>0\) and prove the eventual normalized lower bound against every admissible program and fixed word-size constant, including unrestricted adaptive Las Vegas algorithms.

For a negative answer, prove that for every \(\gamma>1\) and \(\delta>0\) there are an admissible program \(A\) and fixed \(a\ge2\) for which \(\tau_A\) is not \(\Omega(n^\delta)\): for every \(c>0\) and every integer \(N\ge1\), some integer \(n\ge N\) satisfies \(\tau_A(n)<c n^\delta\). The counterexample program may depend on \(\gamma,\delta\). A single algorithm with subpolynomial overhead is sufficient when established in every required regime, but is not the definition of the negation.

A conditional consequence of 3SUM hardness, a lower bound confined to semi-adaptive queries, or a polylogarithmic bound for the Inner Product variant does not alone settle this target. The Lean proof must cover the specified inputs, costs, zero-error convention and quantifier order.''',
 source_formulation=dict(text='Conjecture 1 asks for fixed exponents gamma>1 and delta>0 forcing polynomial overhead in a three-phase word-RAM set-disjointness problem, when the number of stored sets is polynomial in the universe size. This card keeps the previously selected exact number of sets, zero-error expected costs and explicit uniform machine convention.',caption='Paraphrase of Pătrașcu, STOC 2010, §1.2 Conjecture 1 p. 2; expected-time and zero-error conventions are discussed in §1.3 p. 3.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Towards Polynomial Lower Bounds for Dynamic Problems','Mihai Pătrașcu',2010,'https://www.ccs.neu.edu/~viola/classes/papers/PatrascuTowards.pdf','STOC 2010; §1.2 Conjecture 1 and Theorem 2 p. 2; §1.3 Theorem 3 and randomized expected-time convention p. 3'),
 ref('layered','An Adaptive Step Toward the Multiphase Conjecture','Young Kun Ko; Omri Weinstein',2019,'https://arxiv.org/abs/1910.13543v1','29 October 2019; Definition 1.3 and Theorem 1.4 p. 3, semi-adaptive query restriction'),
 ref('linear2025','Lower Bounds for Linear Operators','Young Kun Ko',2025,'https://eccc.weizmann.ac.il/report/2025/155/','Published 22 October 2025; primary abstract, Inner Product communication consequence with superpolynomially many queries; proof not independently audited'),
 ref('dynamic2025','Unifying the Landscape of Super-Logarithmic Dynamic Cell-Probe Lower Bounds','Young Kun Ko',2025,'https://eccc.weizmann.ac.il/report/2025/156/','Published 22 October 2025; primary abstract, superlogarithmic Inner Product bound; proof not independently audited'),
 ref('dynamic2026',r'An \(\Omega((\log n/\log\log n)^2)\) Cell-Probe Lower Bound for Dynamic Boolean Data Structures','Young Kun Ko',2026,'https://eccc.weizmann.ac.il/report/2026/047/','Report dated 26 March, published 5 April 2026; §1.1 Theorem 1.1 and following exclusion of Disjointness from the lifting criterion, p. 2; full proof not independently audited'),
 ],
 why='This staged problem is a candidate for unconditional polynomial operation lower bounds for dynamic data structures, including directed reachability. Its conjectured overhead is much larger than the logarithmic bounds accessible in general models.',
 context_blocks=[
 block('The source charges preprocessing as well as the later update and query, and gives reductions transferring a polynomial overhead to several dynamic problems. It also supplies conditional support from 3SUM hardness.'),
 block('Ko and Weinstein prove a polynomial lower bound when queries have layered adaptivity: after moving to the update layer, they cannot return to the preprocessing layer. The card permits unrestricted alternation.','layered'),
 block('The 2025 linear-operator preprint states partial progress for an Inner Product communication variant with superpolynomially many queries. Both the predicate and the parameter regime differ from this card.','linear2025'),
 block('The 2025 dynamic preprint states a superlogarithmic bound for Inner Product. This is progress at a different asymptotic scale from the required polynomial overhead.','dynamic2025'),
 block(r'The 2026 report states an \(\Omega((\log n/\log\log n)^2)\) Inner Product bound and explicitly excludes Disjointness from its lifting criterion. The theorem statement was checked; its full proof was not independently audited. It does not announce a resolution of this card.','dynamic2026'),
 ],
 progress=[progress('2010','The three-phase word-RAM conjecture and its dynamic-problem consequences are proposed.'),progress('2019-10-29','A polynomial lower bound is obtained for queries with layered adaptivity.','layered'),progress('2025-10-22','Two preprints state progress for communication and dynamic Inner Product variants.','linear2025'),progress('2026-04-05','A report states a nearly log-squared Inner Product lower bound while excluding Disjointness from its lifting criterion.','dynamic2026')],
),notes,sources,'The original word-RAM conjecture remains unresolved in the bounded primary-source review through 17 September 2026. The checked semi-adaptive theorem and 2025–2026 Inner Product claims do not supply an unrestricted polynomial SetDisjointness bound or a counterexample. This records the scope of the checks, not exhaustive certification of openness or independent verification of all preprint proofs.',summary=[
 'First, a data structure receives a polynomial-size family of subsets of a finite universe.',
 'It later receives another subset, and only afterward learns which stored set must be tested for disjointness.',
 'The conjecture requires polynomial overhead in at least one of the three normalized expected phase costs.',
 'The model permits arbitrary adaptive memory access, and recent restricted or Inner Product lower bounds do not cover the full target.',
 'An accepted resolution must be unconditional and completely checked in Lean with the stated quantifiers and zero-error guarantees.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
