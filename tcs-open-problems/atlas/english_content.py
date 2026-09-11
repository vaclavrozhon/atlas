"""English editorial copy used by the public catalogue."""
from profiles import AREAS,CRITERIA
from reviewed import CARDS
CONTEXTS={
'Algebraic and numerical computation':'Computation with polynomials, matrices, and tensors. Central questions compare arithmetic models, identity tests, and lower bounds.',
'Algorithmic game theory and fair division':'Algorithms for strategic participants and scarce resources. Existence, incentives, fairness, and computational efficiency are separate requirements.',
'Algorithms for biological structures':'Discrete models of sequences, evolutionary trees, and self-assembly. Input structure can determine both reconstructability and computational complexity.',
'Approximation algorithms':'How close to the optimum can an efficient algorithm get? The approximation guarantee, instance class, and hardness assumption all matter.',
'Automata and formal languages':'Finite descriptions of languages and transformations. Questions concern expressive power, decidability, and the cost of changing representations.',
'Automated reasoning and unification':'Algorithms for logical constraints and substitutions. The logical and term models can change both complexity and decidability.',
'Average-case complexity':'Hardness under a specified input distribution. Sampling, success probability, and the computational model must be stated precisely.',
'Coding and information theory':'Transmission and recovery of information under noise and limited access. Existence, explicit construction, and efficient decoding are distinct goals.',
'Combinatorics and graph polynomials':'Structural and extremal properties of discrete objects. These properties often control algorithms and explicit constructions.',
'Communication complexity':'How much information must participants exchange on a distributed input? Randomness, entanglement, rounds, and error define the model.',
'Computability and algorithmic information':'The limits of algorithmic solvability and description length. Oracles, uniformity, and representations can change the statement.',
'Computational and circuit complexity':'The power and resource requirements of computational models. A lower bound must cover every algorithm or circuit in the specified class.',
'Computational geometry':'Algorithmic and structural questions about geometric objects. Dimension, degeneracies, and input representation are part of the problem.',
'Computational topology':'Computing invariants and deciding topological properties. Dimension and the finite representation of a space are crucial.',
'Constraint satisfaction':'Systems of local relations. Classifications of templates and approximations identify the boundary between tractability and hardness.',
'Cryptography':'The possibility of secure primitives and protocols. The adversary, security definition, and hardness assumptions are essential parts of a question.',
'Data structures and compressed data':'Representing data for fast queries and updates. Space, preprocessing, and operation costs must be compared in the same model.',
'Database theory and finite model theory':'Logical queries over finite structures. Expressive power and evaluation models determine algorithmic possibilities.',
'Differential privacy':'Algorithms whose output depends only weakly on one record. Privacy parameters, database adjacency, and utility guarantees must be specified together.',
'Distributed and local algorithms':'Computation with restricted local views and communication. Synchrony, identifiers, message sizes, and adversaries define the model.',
'Dynamic graph algorithms':'Maintaining graph properties as the input changes. Update types and worst-case versus amortized guarantees distinguish the problems.',
'Enumeration and counting':'Counting solutions or generating them. Exactness, approximation, delay, and sampling distributions impose different requirements.',
'Existential theory of the reals':'Deciding whether polynomial constraints admit a real solution, and connections to geometric realization problems.',
'Fine-grained complexity':'Precise running-time exponents and conditional reductions. Input parameters and the hypothesis behind a lower bound must be explicit.',
'Games, synthesis and verification':'Checking correctness and constructing strategies in transition systems. Objectives and available information can change complexity.',
'General algorithm design':'General computational problems and design principles. Inputs, required outputs, and the cost model must be distinguished.',
'Graph theory and graph algorithms':'Graph structure and its algorithmic consequences. Restricting the graph class may enable an algorithm or isolate a sharp obstruction.',
'Infinite-state systems and verification':'Finitely described systems with infinitely many configurations. Central questions identify decidability boundaries for reachability and verification.',
'Information-based complexity and numerical algorithms':'How much information is required for numerical approximation? Function access, dimension, and accuracy define the task.',
'Lattices and computational number theory':'Discrete geometry and arithmetic computation. Approximation factors, dimension, and number representations affect complexity and cryptographic applications.',
'Learning theory':'The data and computation needed to predict. Hypothesis classes, noise, distributions, and error guarantees define the learning problem.',
'Online algorithms, bandits and stochastic optimization':'Decisions made before the future is known. Regret and competitive ratios compare performance to a specified benchmark.',
'Optimization and mathematical programming':'Finding optimal or approximate solutions efficiently. Geometry and oracle access determine possible guarantees.',
'Parameterized and exact algorithms':'Exact computation as a function of structure or input size. Bounds must be compared in the same parameter regime.',
'Proof complexity and logic':'The length and power of formal proofs. Existence of short proofs, finding them, and verifying them are separate questions.',
'Property testing and distribution learning':'Decisions and estimates from limited queries or samples. Distance measures and access models are part of the statement.',
'Pseudorandomness and derandomization':'Replacing randomness by explicit structure. Test strength, seed length, and error define the construction target.',
'Quantum computation':'The power of quantum information and computation. Qubits, measurements, oracle access, and approximation error must be distinguished.',
'Randomized search and optimization':'The performance of randomized search processes. Time and quality guarantees must refer to a precisely specified input class.',
'Rewriting, lambda calculus and semantics':'Formal models of programs and computation rules. Normalization, equivalence, and expressiveness describe their basic capabilities.',
'Scheduling and packing':'Allocating limited capacity. Constraint types and optimization objectives determine approximation and running-time boundaries.',
'Streaming and sketching':'Computation with limited memory or compressed summaries. Passes, adaptivity, and update models affect the attainable bounds.',
'Temporal graph algorithms':'Graphs whose edges are available at specified times. Event order changes reachability and invalidates many static-graph arguments.'}
for a in AREAS:AREAS[a]=(a,CONTEXTS[a])
CRITERION_COPY={
'models':('Power of computational models','The question compares the power of models or representations. Resolving it would identify whether their difference changes what can be computed, rather than only the implementation cost.'),
'resources':('Necessary resources','The question concerns the cost of a limited computational or informational resource. A sharp bound would separate a limitation of current algorithms from a limitation every algorithm in the model must face.'),
'assumptions':('Minimal assumptions','The question tests whether an assumption or restriction is necessary. Removing it, or proving it indispensable, would establish the true scope of the result or construction.'),
'characterization':('Structural characterization','The goal is a characterization of a whole class of instances. It could explain a common reason for tractability or hardness rather than supply one more isolated example.'),
'reductions':('Connections between problems','The question asks for a reduction or implication between problems. Such a connection could transfer algorithms or lower bounds and expose a shared source of difficulty.'),
'construction':('Existence and explicit construction','The question asks for an object to exist or to be constructed efficiently. Bridging existence and explicit computation is often essential for using the structure.'),
'tightness':('Sharp bounds and thresholds','The question asks for a sharp boundary or for a concrete gap to be closed. Such a bound identifies the attainable guarantee and provides a target for new techniques.'),
'decision':('Boundary of algorithmic solvability','The question concerns algorithmic solvability in a specified model. Its structural value is to locate the boundary between an effective procedure and a computational or logical obstruction.')}
for k,(label,why) in CRITERION_COPY.items():CRITERIA[k].update(label=label,why=why)

EN={
'quantum_pcp_hamiltonian':(
'Quantum PCP: a constant promise gap for local Hamiltonians',
r'Are there constants $k$ and $\varepsilon>0$ for which the following promise problem is QMA-hard? The input is $H=\frac1m\sum_{i=1}^m H_i$ on $n$ qubits, with each term acting on at most $k$ qubits and $0\preceq H_i\preceq I$. Distinguish $\lambda_{\min}(H)\le a$ from $\lambda_{\min}(H)\ge b$, promised $b-a\ge\varepsilon$. The reduction must be efficient. This is the normalized Hamiltonian formulation.',
'The classical PCP theorem replaces full verification by inspecting a small part of a proof with a constant gap. Entanglement and local indistinguishability obstruct a direct quantum analogue.',
'This asks whether approximating a quantum system’s energy captures the full difficulty of quantum witness verification. It connects complexity, quantum codes, and local testing.',
['The survey develops the Hamiltonian conjecture and obstacles to quantum PCP constructions.',r'Bafna–Vyas explicitly describe the general conjecture as open. Their classical private PCP uses $O(\sqrt n)$ queries; stronger parameters depend on a product-expansion conjecture. This does not prove Quantum PCP.']),
'strong_qiop_poly':(
'Strong quantum IOPs with polynomial communication',
r'Does every QMA problem admit a strong quantum interactive oracle proof with a constant completeness–soundness gap, $O(1)$ total queried qubits, and $\operatorname{poly}(n)$ communicated qubits? In the strong model the verifier returns the entire message register after each round and retains none of it. Use the precise quantum-access model in Definitions 5.10 and 5.14 of the source.',
'Interaction may make local checking of quantum proofs easier. Query complexity, private quantum memory, and total communication are separate resources.',
'The problem isolates the communication price of an extremely limited quantum verifier. A positive result would eliminate the exponential communication in the present strong construction.',
[r'The general qIOP has polynomial communication but uses a polynomial private quantum resource. The strong construction operates on constantly many qubits but communicates $\exp(\operatorname{poly}(n))$ qubits. Question 1.9 asks for polynomial communication.']),
'qma_vs_qcma':(
'Does a quantum witness have more power than a classical witness?',
r'Is $\mathrm{QMA}=\mathrm{QCMA}$? Both classes have a polynomial-time quantum verifier and bounded error. QMA permits a polynomial-size quantum witness; QCMA permits only a polynomial-length classical string. The question concerns the standard classes without an oracle.',
'A quantum state may encode a proof that has no short classical description. Oracle separations test this idea but do not separate the standard classes.',
'This identifies what kind of information might be intrinsically necessary for efficient verification.',
['A separation relative to a classical oracle is known. The February 2026 paper gives a simpler construction. It leaves the unrelativized class question untouched.']),
'bqp_quantum_advice':(
'Quantum versus classical nonuniform advice',
r'Is $\mathrm{BQP/qpoly}=\mathrm{BQP/poly}$? Advice for inputs of length $n$ depends only on $n$: a state on $\operatorname{poly}(n)$ qubits on the left, or $\operatorname{poly}(n)$ classical bits on the right. The computation must succeed on every input of that length.',
'Advice is not a witness chosen for an individual input. It is one nonuniform information resource shared by an entire input-length class.',
'This distinguishes two basic ways to store auxiliary information for computation. It is different from QMA versus QCMA.',
['The source gives the first separation of these advice classes using a standard classical oracle. It does not claim an unrelativized separation.']),
'total_quantum_communication':(
'A polynomial relation between classical and quantum communication for total functions',
r'For a total Boolean function $F:X\times Y\to\{0,1\}$, let $R^{cc}_{1/3}(F)$ be public-coin randomized communication complexity and $Q^{cc,*}_{1/3}(F)$ quantum communication complexity with unlimited shared entanglement. Is there a universal polynomial $p$ such that $R^{cc}_{1/3}(F)\le p(Q^{cc,*}_{1/3}(F))$ for every total $F$?',
'Partial functions can exhibit exponential quantum savings. Requiring correctness on every input pair may fundamentally restrict that advantage.',
'The problem delineates quantum advantage in a basic distributed model with unrestricted local computation.',
[r'For $F=f\circ\mathrm{AND}_2$, the source proves $D^{cc}(F)=O((Q^{cc,*}(F))^7\log^2 n)$. The polylogarithmic factor and the restriction to AND-composed functions prevent this from settling the general question.']),
'private_selection_gaussian':(
'Optimal private selection using only Gaussian queries',
r'For a finite set $Y$, public losses $\ell_y$ have sensitivity 1 under a one-record change in the database $X$. The only access to $X$ is through adaptive queries $q_i(X)+N(0,1/(2\rho_i))$, with sensitivity at most 1 and $\sum_i\rho_i\le\rho$. Can the algorithm output $\hat y$ satisfying $\mathbb E[\ell_{\hat y}(X)]-\min_y\ell_y(X)=O(\log|Y|/\sqrt\rho)$?',
'The exponential mechanism achieves this error with direct data access. The question is whether noise addition alone can exactly match its guarantee.',
'It tests equivalence between two basic privacy primitives. The remaining polyloglogarithmic gap is a concrete obstacle to an optimal reduction.',
[r'The baseline binary-tree method has error $O(\log^{3/2}|Y|/\sqrt\rho)$.',r'The new algorithm achieves $O(\log|Y|(\log\log|Y|)^{11}/\sqrt\rho)$. Section 1.2 explicitly leaves removal of the $\log\log|Y|$ factor open.']),
'private_selection_laplace':(
'Optimal private selection using only Laplace queries',
r'In the same finite-selection setting with sensitivity-1 losses, an algorithm makes $k$ adaptive sensitivity-1 queries. Its answers are $q_i(X)+\mathrm{Lap}(k)$, where $k$ is the scale. Can it guarantee expected excess loss $O(\log|Y|)$ for arbitrary losses? The algorithm may choose the number of queries.',
'This model corresponds to basic composition for pure privacy. The stronger concentration of Gaussian noise cannot simply be transferred.',
'The cost of pure privacy is a structural model distinction, rather than an arbitrary change of constants. It determines the reach of noise addition as a universal primitive.',
[r'The binary-tree algorithm has error $O(\log^2|Y|)$.','The authors explain why their nearly optimal Gaussian method does not yield a tight Laplace bound and leave this model open.']),
'private_pac_characterization':(
'A combinatorial characterization of private PAC sample complexity',
r'Identify a structural parameter of a concept class $C$ that characterizes realizable $(\varepsilon,\delta)$-DP PAC sample complexity up to specified factors. The source fixes constant accuracy, confidence, and $\varepsilon$, with $\delta$ much smaller than the inverse sample size. A concrete target is a universal upper bound $\operatorname{poly}(\mathrm{VC}(C),\log^*\mathrm{LD}(C))$.',
r'VC dimension characterizes nonprivate learning. Finite Littlestone dimension $\mathrm{LD}$ characterizes the existence of private learning but does not determine its optimal quantitative cost.',
'The problem seeks a privacy analogue of a foundational characterization theorem in learning theory.',
[r'The survey gives lower bound $\Omega(\mathrm{VC}+\log^*\mathrm{LD})$ and upper bound $\min\{O(\log|C|),\widetilde O(\mathrm{LD}^5)\}$. The $\mathrm{VC}=1$ case is nearly understood; the general gap remains.']),
'pessiland':(
'Does average-case hardness of NP imply one-way functions?',
r'Suppose an NP problem is hard on average under a polynomial-time samplable distribution, in the distributional sense specified by the source. Must there be a polynomial-time computable function $f$ for which no PPT algorithm inverts $f(U_n)$ with nonnegligible probability? Failure of this implication would permit the world called Pessiland.',
'Hardness of deciding typical instances and hardness of finding preimages are different requirements. The assumption P ≠ NP alone is weaker and belongs to a separate existing question.',
'It asks whether distributional hardness alone suffices for basic cryptography: a central connection between average-case complexity and cryptographic constructions.',
[r'The revised paper characterizes the remaining obstruction by the gap between approximation factors $\ell^{1-o(1)}$ and $O(\ell)$ for minimum-description-length agnostic learning. Here $\ell$ is advice complexity of sampling. The original April version states a different quantitative claim.']),
'lpn_worst_case':(
'Low-noise LPN from a standard worst-case hardness assumption',
r'LPN samples are $(a,\langle a,s\rangle\oplus e)$ with $a\sim U(\mathbb F_2^n)$, fixed secret $s\in\mathbb F_2^n$, and $e\sim\mathrm{Ber}(\eta)$. For low noise such as $\eta=n^{-1/2}$, seek a reduction from a natural worst-case coding problem to average-case LPN hardness without requiring simultaneous hardness of decoding and distinguishing noisy words of the dual code.',
'LWE has strong connections to worst-case lattice problems. Establishing comparable foundations for LPN at cryptographically useful noise rates is more difficult.',
'A basic security assumption would obtain an explanation through independently studied hardness. The extra assumption in the new reduction makes the remaining target concrete.',
[r'The revision gives a reduction for $\eta=n^{-\alpha}$, any constant $\alpha<1$, from simultaneous worst-case hardness of two tasks on a code and its dual. This advances beyond earlier near-half-noise reductions; the single-assumption target remains stronger.']),
'doubly_efficient_ip':(
'Doubly efficient IP = PSPACE for the full time range',
r'Suppose a language is decided in polynomial space and time $T(n)$. Does it have an interactive proof with a $\operatorname{poly}(n)$-time verifier, a $\operatorname{poly}(T(n))$-time honest prover, and a constant completeness–soundness gap? Soundness must hold against arbitrarily powerful cheating provers. The target includes $T$ beyond the quasipolynomial range.',
'IP = PSPACE alone does not guarantee that producing the proof costs only a polynomial in the original computation time.',
'This asks whether a long, space-efficient computation can be verified without hiding an excessive cost in the honest prover.',
[r'The previous range cited in the paper was $T(n)=n^{O(\sqrt{\log n/\log\log n})}$.',r'The direct construction extends the range to $T(n)=n^{O(\log n)}$. It does not cover arbitrary polynomial-space computation times.']),
'rs_product_expansion':(
'Higher-dimensional product expansion for structured Reed–Solomon codes',
r'Fix $k\ge3$ and $\varepsilon>0$. Let $C_i$ be RS codes over a prime field $\mathbb F_q$, evaluated on multiplicative subgroups of pairwise coprime orders, each of rate below $1-\varepsilon$. Is the tuple $\rho$-product-expanding for some $\rho=\rho(k,\varepsilon)>0$ independent of block lengths? The precise higher-dimensional norm and decomposition are in Definition 4.1.',
r'In two dimensions, a suitable decomposition $M=M_1+M_2$ into column and row codewords must satisfy $|\mathrm{supp}(M)|\ge\rho(n_1|M_1|_{\mathrm{col}}+n_2|M_2|_{\mathrm{row}})$.',
'This is a specific structural obstacle to private PCPs and quantum codes supporting multiplication. The conjecture’s conditions arise from those constructions.',
['The source proves the two-dimensional case. Higher dimensions remain conjectural. It also mentions an AI-generated candidate proof not verified by the authors; that is not treated here as a solution.'])
}
for c in CARDS:
    if c['key'] not in EN:continue
    title,formal,context,why,progress=EN[c['key']]
    c.update(title=title,formal=formal,context=context,why=why,status_note='Literature checked on 10 September 2026; dates and review scope are recorded below.',review_note='The statement and listed results were individually checked against the cited sources. New proofs were not independently verified. The assessment of importance is editorial.')
    for point,text in zip(c['progress'],progress):point['text']=text
