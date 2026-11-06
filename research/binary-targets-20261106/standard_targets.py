"""Source-backed binary endpoints; executed by revise.py."""

d=original('6575')
quantity=d['formal'].split('Give a real-valued function')[0].replace('determine the universal deterministic competitive-ratio infimum', 'define the universal deterministic competitive-ratio infimum')
revise('6575', 'Deterministic k-server conjecture',
       r'For every integer \(k\ge1\), every finite or infinite metric space \((M,d)\) with at least \(k+1\) points, and every initial configuration \(C_0\in M^k\), do there exist a deterministic online rule \(A\) and a finite \(\beta\ge0\) such that \[\operatorname{cost}_A(\sigma;C_0)\le k\operatorname{OPT}(\sigma;C_0)+\beta\] for every finite request sequence \(\sigma\)? Both parties have exactly \(k\) servers and start at \(C_0\); movement cost is the sum of distances in the model below. The rule and additive constant may depend on the metric and initial placement, but not on the future requests.',
       'Restored actual k-competitiveness from the classical conjecture, distinguishing it from mere attainment of an infimum value.',
       ['The k-server problem serves successive requests by moving one of k servers in a known metric.', 'The online rule sees only requests that have already arrived.', 'The conjecture asks for cost at most k times the offline optimum plus a fixed additive constant.', 'It permits unrestricted computation and both finite and infinite metric spaces.', 'A ratio approaching k without an actual k-competitive rule does not establish the selected assertion.'],
       definitions=quantity+'\n\n'+d['definitions'],
       context={3:r'The selected target is the classical conjecture asserting an actual \(k\)-competitive rule. It implies \(R_{\mathrm{det}}(k)=k\), but an infimum value alone need not give endpoint attainment. The September 2026 preprint claims the actual competitiveness statement; its proof-review caveat is retained below.'},
       refs=['https://www.cs.cmu.edu/~sleator/papers/server-problems.pdf'])

d=original('6576')
quantity=d['formal'][d['formal'].index('An online strategy'):d['formal'].index('The strategy may depend')]
defs=d['definitions'].split('Determination up to universal factors means')[0]
revise('6576', 'Square-root-dimensional Euclidean convex body chasing',
       r'Does there exist a universal constant \(C>0\) such that, for every integer \(d\ge1\), some deterministic online strategy \(A_d\) for convex body chasing in \(\mathbb R^d\) satisfies \[\operatorname{cost}_{A_d}(K_1,\ldots,K_T)\le C\sqrt d\,\operatorname{OPT}(K_1,\ldots,K_T)\] for every finite sequence of nonempty compact convex request sets? The strategy starts at the origin, sees each set before choosing its next point in that set, and pays Euclidean movement. The same strategy must work for every horizon; requests need not be nested, and no additive cost is allowed.',
       'Selected the Euclidean square-root lower-bound scale as the natural competitive upper-bound target, preserving general request sequences and no additive slack.',
       ['Convex body chasing requires moving into each newly revealed convex request set.', 'The objective is total Euclidean movement compared with an offline path starting at the same point.', 'The question asks whether a constant times the square root of dimension is a universal competitive ratio.', 'The requests may be unrelated rather than nested.', 'The target concerns online information and movement, with no computational bound.'],
       definitions=quantity+'\n\n'+defs,
       refs=['https://arxiv.org/abs/1905.11968v3'])

d=original('6577')
defs=d['definitions']
a=defs.index('Joint constant-factor precision means')
b=defs.index('The Borel convention')
defs=defs[:a]+defs[b:]
revise('6577', 'Near-optimal dimension dependence in bandit convex optimization',
       r'Do there exist universal constants \(C>0\) and \(a\in\mathbb N_0\) such that the one-point adversarial bandit convex-optimization minimax regret defined below satisfies \[R^*(d,T)\le C d\sqrt T\bigl(\log_2(d+T+2)\bigr)^a\qquad(d,T\in\mathbb N_{\ge1})?\] Losses take values in \([0,1]\), the adversary is oblivious, and the learner observes only the exact value of its current action. The guarantee is uniform over all normalized convex bodies in the stated model; no smoothness or computation-time restriction is imposed.',
       'Selected the known linear-in-dimension lower-bound scale up to logarithmic factors, rather than an arbitrary regret exponent or a demand for exact logarithmic asymptotics.',
       ['The learner chooses one point and observes one value of the current convex loss.', 'Losses may change adversarially from round to round.', 'Regret compares total loss with the best single point in hindsight.', 'The question asks for dimension times the square root of the horizon, allowing fixed logarithmic factors.', 'The full one-point model and unrestricted convex losses remain in force.'],
       definitions=defs,
       refs=['https://tor-lattimore.com/downloads/cvx-book/cvx.pdf','https://arxiv.org/abs/2006.00475v3'])

d=original('7317')
quantity=d['formal'][d['formal'].index('For each integer'):d['formal'].index('Give an unambiguous')]
defs=d['definitions'].replace('The unknown function \\(h\\) must specify the asymptotic scale, rather than merely rename the defining infimum.', '')
revise('7317', 'Squared-logarithmic randomized k-server competitiveness',
       r'Does there exist a universal constant \(C>0\) such that, for every \(k\ge2\), every finite metric \((X,d)\) with at least \(k+1\) points, and every initial configuration \(C_0\), there are a randomized online strategy \(\mathcal A\) and a finite \(\beta\ge0\) with \[\mathbb E[\operatorname{cost}_{\mathcal A}(\sigma;C_0)]\le C\bigl(\log_2(k+1)\bigr)^2\operatorname{OPT}(\sigma;C_0)+\beta\] for every finite request sequence fixed independently of the strategy’s randomness? The strategy and \(\beta\) may depend on the metric and initial placement; \(C\) may not. The number of metric points is unbounded relative to \(k\).',
       'Selected the squared-logarithmic upper bound matching the source’s known lower scale; did not restore the logarithmic conjecture already refuted before 2026.',
       ['Randomized k-server serves requests using k movable servers in a finite metric.', 'Its expected movement is compared with an offline optimum using the same number of servers.', 'The question asks for a squared-logarithmic competitive ratio in k on every finite metric.', 'The adversary fixes requests independently of the random choices.', 'The constant must not grow with the total number of metric points.'],
       definitions=quantity+'\n\n'+defs,
       context={5:r'The classical deterministic upper bound is linear in \(k\), while the general randomized lower bound is \(\Omega(\log^2 k)\). The selected binary question asks whether that lower scale is achievable on all finite metrics.',7:r'The weaker sublinear-ratio milestone formerly indexed as TCS-4983 would follow from the squared-logarithmic target. Its model is the same oblivious-adversary model with sequence-independent additive cost, rather than a request for computational efficiency.'},
       refs=['https://arxiv.org/abs/2211.05753','https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.65'])

revise('6623', 'Polynomial-sample worst-case trace reconstruction',
       r'For every fixed real deletion probability \(\delta\in(0,1)\), do there exist constants \(C_\delta>0\) and \(a_\delta\in\mathbb N_{\ge1}\) such that \[N_\delta(n)\le C_\delta n^{a_\delta}\qquad\text{for every }n\ge2?\] Here \(N_\delta(n)\), defined below, is the number of independent deletion traces needed to reconstruct every unknown \(n\)-bit string exactly with success probability at least \(2/3\). Processing is unrestricted, and the length and deletion probability are known. Constants may depend on fixed \(\delta\).',
       'Selected the polynomial-sample question explicitly isolated by the sources, preserving worst-case strings and unrestricted processing.',
       ['A deletion trace removes each bit independently and hides the removed positions.', 'Repeated traces all come from the same unknown binary string.', 'The question asks whether polynomially many traces suffice for exact worst-case reconstruction.', 'The deletion probability is any fixed constant strictly between zero and one.', 'Only the number of traces is bounded; reconstruction time is unrestricted.'],
       context={0:'The selected binary target asks whether a polynomial number of traces suffices for every fixed deletion rate. It does not require the optimal sample exponent or a polynomial-time reconstruction algorithm.',5:r'Burudgunte, Valiant and Wang’s July 2026 preprint gives a quasipolynomial sample upper bound for every fixed positive retention probability. Its bound is \(\exp(p^{-7/3}(\log_2 n)^c)\), for retention probability \(p=1-\delta\) and an absolute constant \(c\). This dated theorem does not by itself give a polynomial bound.'},
       refs=['https://arxiv.org/abs/2607.04073'])

d=original('6638')
quantity=d['formal'].split('Approximate \\(\\rho_')[0].replace('determine the real number','define the real number')
defs=d['definitions'].replace('The numerical tolerance applies to this infimum, not to the feasibility or objective guarantee of a proposed schedule.', '')
revise('6638', 'Breaking factor two for unrelated-machine makespan',
       r'Do there exist a fixed real \(\varepsilon\in(0,1)\) and one uniform deterministic polynomial-bit-time algorithm that, on every valid unrelated-machine scheduling instance \(I\) defined below, outputs a feasible schedule \(\sigma\) with \[C_{\max}(\sigma)\le(2-\varepsilon)\operatorname{OPT}(I)?\] The machine count is part of the input, and \(\varepsilon\) is independent of it and of all processing times. No complexity assumption is included.',
       'Restored the source’s fixed improvement below two; an instance-dependent improvement such as 2-1/m does not meet it.',
       ['Each job may have a different processing time on each machine.', 'The objective is the largest total load assigned to any machine.', 'The question asks for a deterministic polynomial-time approximation uniformly better than factor two.', 'The amount of improvement is one fixed positive constant.', 'The input number of machines and the processing-time bit lengths are unrestricted.'],
       definitions=quantity+'\n\n'+defs,
       context={0:r'The selected target restores the original source question: a polynomial-time \((2-\varepsilon)\)-approximation for one fixed universal \(\varepsilon>0\). It does not request a numerical determination of the full approximation-ratio infimum.'},
       refs=['https://arxiv.org/abs/2307.08453'])

d=original('6659')
defs=r'For the context, let \(\mathcal R\) be the set of fixed approximation factors achievable by the uniform randomized, always-feasible, worst-case polynomial-time algorithms below, with success probability at least \(2/3\) on each instance; let \(\rho_{\mathrm{med}}=\inf\mathcal R\). Write \(e=\exp(1)\). '+'\n\n'+d['definitions']
revise('6659', 'Metric k-Median at the coverage-hardness threshold',
       r'For every fixed rational \(\varepsilon>0\), does there exist one uniform randomized polynomial-bit-time algorithm that, on every metric k-Median instance defined below, always outputs a nonempty facility set \(S\subseteq F\) with \(|S|\le k\), and satisfies \[\Pr\!\left[\operatorname{cost}(S)\le\left(1+\frac2e+\varepsilon\right)\operatorname{OPT}\right]\ge\frac23?\] Here \(e=\exp(1)\). The polynomial and program may depend on fixed \(\varepsilon\), but the running time must be polynomial in the full input length on every execution, with unrestricted input \(k\).',
       'Selected approach to the coverage-hardness threshold, retaining positive slack, randomized success and strict facility-budget feasibility.',
       ['Metric k-Median chooses up to k supplied facility locations to minimize total client distance.', 'The metric is an arbitrary explicitly supplied rational distance table.', 'The question asks for every approximation factor strictly above one plus two divided by e.', 'The running time must be polynomial even when k is an input parameter.', 'The output must respect the facility budget on every execution.'],
       definitions=defs,
       context={0:r'The selected binary target is an algorithm for every factor \(1+2/e+\varepsilon\), where \(\varepsilon>0\) is fixed. This matches the familiar coverage-hardness scale from above without assuming that an algorithm attains the exact endpoint.',12:'The requested approximation must refer to the same input class, randomness convention and facility budget. A fixed-parameter runtime, a relaxation-gap example or a guarantee opening extra facilities does not establish this polynomial-time upper bound.'},
       refs=['https://arxiv.org/abs/2503.10972','https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.42'])

d=original('6664')
defs=r'Let \(\mathcal F_{n,d}\) denote the polynomial threshold functions specified below, and let \(M(n,d)=\max_{f\in\mathcal F_{n,d}}I(f)\). '+'\n\n'+d['definitions']
revise('6664', 'Asymptotic Gotsman–Linial conjecture',
       r'Does there exist a universal constant \(C>0\) such that, for every integer \(n\ge1\), every \(1\le d\le n\), and every Boolean function \(f:\{-1,1\}^n\to\{-1,1\}\) represented as the sign of a real polynomial of degree at most \(d\), \[I(f)\le C d\sqrt n?\] Here \(I(f)\) is total influence, the expected number of input coordinates whose flip changes the output at a uniformly random input. The precise polynomial and tie conventions are defined below. The same constant must work for growing degrees as well as fixed degrees.',
       'Restored the surviving asymptotic Gotsman–Linial upper bound, not the disproved exact-maximizer conjecture.',
       ['A polynomial threshold function is the sign of a low-degree real polynomial on the Boolean cube.', 'Total influence counts sensitive coordinates on average over uniform inputs.', 'The conjecture asks for a universal bound proportional to degree times the square root of dimension.', 'Its constant must be independent of both parameters.', 'The stronger assertion identifying an exact symmetric maximizer is a different, disproved claim.'],
       definitions=defs,
       context={0:r'The selected target is the asymptotic Gotsman–Linial conjecture \(I(f)=O(d\sqrt n)\), uniformly in dimension and degree. It is distinct from the stronger, disproved assertion that one particular symmetric function is an exact maximizer.',10:'A proof or refutation of this universal upper bound answers the card. Determining the full extremal function after a refutation is not required.'},
       refs=['https://arxiv.org/abs/2108.02288'])

d=original('6674')
quantity=d['formal'][d['formal'].index('\\[R(m)'):d['formal'].index('The question includes')]
revise('6674', 'Constant-factor truthful-in-expectation scheduling',
       r'Does there exist a universal constant \(K\ge1\) such that, for every machine count \(m\ge2\), some family of truthful-in-expectation mechanisms handles every finite job count \(n\ge1\) and every finite nonnegative real processing-time matrix \(t\) with \[\mathbb E[C(M_{m,n}(t),t)]\le K\operatorname{OPT}(t)?\] Here \(C(\sigma,t)\) is the makespan of assignment \(\sigma\), as defined below. The factor is independent of \(m,n,t\); arbitrary correlated random assignments and payments are allowed, and computation is unrestricted.',
       'Selected the source’s constant-versus-growing incentive-loss question, preserving truthfulness in expectation rather than universal truthfulness.',
       ['Machines report their private processing times for the jobs.', 'A truthful-in-expectation mechanism makes honest reporting optimal for expected utility.', 'The question asks whether expected makespan can stay within a universal constant of the offline optimum.', 'The constant must be independent of the number of machines and jobs.', 'Payments and correlated randomness are allowed, with no computation restriction.'],
       definitions=quantity+'\n\n'+d['definitions'],
       refs=['https://arxiv.org/abs/1507.08708','https://link.springer.com/chapter/10.1007/978-3-540-92185-1_46'])

d=original('6676')
defs=r'For context, let \(\mathcal R\) be the real factors achieved by a uniform deterministic polynomial-bit-time algorithm on every valid instance, and let \(\rho_{\mathrm{prec}}=\inf\mathcal R\). '+'\n\n'+d['definitions']
revise('6676', 'Breaking factor two for precedence-constrained makespan',
       r'Do there exist a fixed \(\varepsilon\in(0,1)\) and one uniform deterministic polynomial-bit-time algorithm that, for every instance of nonpreemptive precedence-constrained scheduling on identical parallel machines, outputs a feasible schedule \(S\) with \[C_{\max}(S)\le(2-\varepsilon)\operatorname{OPT}?\] Processing times are positive binary-encoded integers, the precedence graph is arbitrary and acyclic, and the number of machines is part of the input. The constant \(\varepsilon\) cannot depend on the instance. No complexity assumption is imposed.',
       'Selected a fixed improvement below the classical factor-two barrier, preserving arbitrary durations, precedences and an input machine count.',
       ['Precedence constraints require some jobs to finish before others start.', 'Jobs run without interruption on identical parallel machines.', 'The question asks for a polynomial-time approximation uniformly better than factor two.', 'The improvement must be a fixed positive constant independent of the machine count.', 'Unit-job and fixed-machine special cases do not cover this full model.'],
       definitions=defs,
       context={5:r'The binary target asks whether \(\rho_{\mathrm{prec}}<2\). A strict inequality is equivalent to an actual fixed-factor improvement; there is no endpoint-attainment issue at a value strictly below two.',9:'The selected question concerns the existence of a universal fixed improvement below two. A conditional inapproximability result supplies only a conditional negative answer unless its assumption is also proved.'},
       refs=['https://theory.epfl.ch/osven/Ola%20Svensson_publications/SICOMP11b.pdf'])

revise('6857', 'Polynomial mixing of the self-avoiding-walk pivot chain',
       r'Do there exist constants \(C>0\) and \(a\in\mathbb N_{\ge1}\) such that \[t_{\mathrm{pivot}}(n)\le Cn^a\qquad\text{for every integer }n\ge1?\] The chain below acts on rooted \(n\)-step self-avoiding walks in the square lattice, uses the five specified pivot symmetries, and counts every attempted pivot including rejection. Mixing means total-variation distance at most \(1/4\) from the uniform law, from every starting walk.',
       'Selected rapid mixing as the concrete qualitative convergence target, without changing the pivot chain or its proposal clock.',
       ['A self-avoiding lattice walk never visits the same vertex twice.', 'A pivot step rotates or reflects a suffix and rejects self-intersecting proposals.', 'The question asks whether this chain reaches its uniform stationary distribution in polynomially many attempted pivots.', 'The mixing guarantee is from every starting walk.', 'Fast implementation of one pivot does not itself prove a mixing bound.'],
       context={0:'Example B.5 fixes the square lattice and five allowed symmetries, proves irreducibility, and leaves convergence behavior open. The selected question is whether worst-start total-variation mixing takes polynomially many attempted pivots.'},
       refs=['https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf'])

d=original('7322')
defs=r'For context, let \(\mathcal R\) be the set of ratios achievable by the deterministic polynomial-bit-time algorithms defined below, and let \(\rho_{\mathrm{SCS}}=\inf\mathcal R\). '+'\n\n'+d['definitions']
revise('7322', 'Factor-two approximation for shortest common superstring',
       r'Does there exist one uniform deterministic polynomial-bit-time algorithm that, given any explicit finite list of strings over an explicitly given finite alphabet, outputs a common superstring of length at most twice the minimum possible length? All occurrences are forward contiguous substrings. The input, zero-optimum convention and full bit-cost model are defined below. The algorithm need not use the maximum-overlap greedy rule.',
       'Selected the established factor-two approximation endpoint for general algorithms, retaining the distinction from the greedy conjecture.',
       ['A common superstring contains every input string as a contiguous substring.', 'The objective is its total number of symbols.', 'The question asks for a deterministic polynomial-time algorithm within factor two of optimum.', 'The input alphabet and every string are explicit.', 'The target permits any algorithm and is separate from analyzing one greedy heuristic.'],
       definitions=defs, refs=['https://eccc.weizmann.ac.il/report/2026/157/'])

d=original('7328')
defs=d['definitions'].split('Call any function')[0]
revise('7328', 'Log-log amortized decrease-key in standard pairing heaps',
       r'Does there exist a universal constant \(C>0\) such that the standard two-pass pairing heap defined below satisfies \[W(\mathcal S)\le C\left(a(\mathcal S)+b(\mathcal S)\log_2(N+2)+c(\mathcal S)\log_2\log_2(N+4)\right)\] for every finite legal operation sequence \(\mathcal S\) starting from empty heaps and having at most \(N\ge1\) live items in total? Here \(a\) counts make-heap, insert, meld and find-min operations, \(b\) counts delete-min, and \(c\) counts decrease-key. The fixed algorithm and work measure \(W\) are defined below.',
       'Selected the log-log decrease-key charge, keeping simultaneous constant insert/meld charges and logarithmic delete-min charges rather than borrowing incompatible analyses.',
       ['A pairing heap maintains a priority queue using links between heap-ordered trees.', 'This card fixes the standard two-pass delete-min and cut-and-link decrease-key operations.', 'It asks whether decrease-key has a log-log amortized charge.', 'Insert and meld must simultaneously keep constant charges, while delete-min has a logarithmic charge.', 'The global live-item bound and all operation sequences remain part of the guarantee.'],
       definitions=defs,
       criterion=r'Give a complete, mathematically correct Lean-checked proof or refutation of the displayed total-work bound for the specified standard two-pass pairing heap. A positive answer must use one universal constant with all three simultaneous operation charges. A negative answer must prove that for every proposed constant there are a live-item bound and a legal sequence violating the inequality; a finite example with a larger constant-factor cost is insufficient. The algorithm is fixed, so proving a bound for a modified heap does not answer the question.',
       context={1:r'Fredman proved an amortized \(\Omega(\log\log N)\) lower bound for decrease-key when the other operations have \(O(\log N)\) amortized charges, as stated in Iacono’s Introduction and Figure 1. This also rules out a smaller decrease-key charge under the stricter constant insert/meld convention here. The card asks for the matching \(O(\log\log N)\) upper charge for the fixed standard two-pass heap, simultaneously with its stated charges for every other operation. The lower-bound scope is checked through the later primary papers, not a new audit of Fredman’s full proof.'},
       refs=['https://arxiv.org/html/1110.4428v3','https://arxiv.org/html/2607.23118v1'])

revise('7337', 'Sharp register lower bound for obstruction-free set agreement',
       r'For every integer pair \(n>k\ge1\), must any deterministic obstruction-free one-shot \(k\)-set-agreement protocol for \(n\) named processes use at least \(n-k+1\) shared atomic read/write registers? Equivalently, is \(R(n,k)\ge n-k+1\) throughout the domain, with \(R\) and the register, validity and progress conventions below? The matching upper bound is known; no restriction on register width or local computation is added.',
       'Restored the source’s n-k+1 register conjecture at obstruction-freedom parameter one, replacing full-function numerical determination.',
       ['Set agreement lets processes decide at most k distinct values that were actually proposed.', 'Obstruction-freedom guarantees completion when one process eventually runs alone.', 'The question asks whether n minus k plus one shared registers are always necessary.', 'It concerns one invocation, named processes and arbitrarily large read/write registers.', 'The matching known upper bound makes this a sharp space conjecture.'],
       context={2:r'Ellen, Gelashvili and Zhu conjecture the general bound \(n-k+x\) for \(x\)-obstruction-freedom. This card selects \(x=1\), restoring the resulting \(n-k+1\) lower-bound assertion. A smaller-register protocol for one parameter pair would refute it.'},
       refs=['https://arxiv.org/abs/1711.02455v5'])

d=original('7356')
defs=d['definitions']
a=defs.index('The accuracy requirement is absolute error')
defs=defs[:a]+r'For the context, put \(\rho_{\mathrm{TSP}}=\inf\mathcal R\), where \(\mathcal R\) is the set of achievable factors defined above. No complexity assumption is imposed. A hardness argument conditional on an unproved assumption does not by itself refute the algorithmic assertion.'
revise('7356', 'Four-thirds approximation for metric TSP',
       r'Does there exist one uniform classical randomized polynomial-bit-time algorithm that, on every symmetric rational metric TSP instance \(I\) defined below, always returns a feasible tour and satisfies \[\mathbb E[\operatorname{cost}_I(A(I))]\le\frac43\operatorname{OPT}(I)?\] Running time must be polynomial in the full distance-matrix encoding length on every random execution. The guarantee is against the optimum integral tour, with no restriction to a particular linear relaxation or rounding method.',
       'Selected the natural four-thirds algorithmic target, keeping it distinct from the existing subtour-LP integrality-gap card.',
       ['Metric TSP seeks a shortest tour visiting every point and returning to its start.', 'The distances are arbitrary symmetric rational metrics supplied explicitly.', 'The question asks for a randomized polynomial-time approximation with expected factor four-thirds.', 'Every execution must return a feasible tour within the polynomial time bound.', 'A bound on a particular linear relaxation is a related but different question.'],
       definitions=defs,
       refs=['https://arxiv.org/abs/2007.01409v6'])

revise('7396', 'Linear-query lower bound for sparse binary matrix rank estimation',
       r'Do there exist a fixed integer \(d\ge2\), a fixed rational \(\varepsilon\in(0,1/2)\), constants \(c>0\) and \(n_0\ge1\), such that \[Q_d(n,\varepsilon)\ge cn\qquad\text{for every integer }n\ge n_0?\] Here \(Q_d(n,\varepsilon)\) is the minimum randomized adaptive row/column-query cost, defined below, for estimating the rank over \(\mathbb F_2\) of every \(n\)-by-\(n\) matrix having at most \(d\) ones per row and column, to additive error \(\varepsilon n\) with success probability at least \(2/3\).',
       'Restored the source’s linear-query obstruction in some fixed nontrivial degree and accuracy regime; did not claim hardness for every degree, which fails at degree one.',
       ['The matrix is binary and has bounded numbers of ones in each row and column.', 'One query reveals the complete nonzero list of a selected row or column.', 'The question asks whether some fixed sparsity and accuracy regime forces linearly many queries.', 'Queries may be adaptive and all computation between them is free.', 'The target is additive rank estimation, not exact rank or sublinear total machine time.'],
       refs=['https://sublinear.info/index.php?title=Open_Problems%3A68'])

revise('7384', 'Polynomial-query adaptive tolerant monotonicity testing',
       r'For every pair of fixed rational constants \(0<a<b\le1/2\), do there exist constants \(C_{a,b}>0\) and \(q_{a,b}\in\mathbb N_0\) such that \[Q(n;a,b)\le C_{a,b}(n+1)^{q_{a,b}}\qquad\text{for every }n\ge1?\] Here \(Q(n;a,b)\) is the randomized adaptive value-query complexity, defined below, of accepting Boolean functions at uniform distance at most \(a\) from monotonicity and rejecting those at distance at least \(b\), with success probability at least \(2/3\). Computation between queries is unrestricted.',
       'Selected polynomial-query adaptive testing as the qualitative efficiency question; kept positive tolerance and did not transfer nonadaptive lower bounds.',
       ['A monotone Boolean function never decreases when input coordinates increase.', 'A tolerant tester must accept functions close to monotone, not just exactly monotone ones.', 'The question asks whether adaptive tests need only polynomially many value queries for every fixed tolerance gap.', 'Both thresholds are positive constants and the input distribution defining distance is uniform.', 'Nonadaptive lower bounds do not automatically refute this assertion.'],
       refs=['https://arxiv.org/abs/2309.12513'])

d=original('4592')
guarantee=d['formal'][d['formal'].index('Retain the source'):d['formal'].index('The parameters range')]
guarantee=guarantee.replace('Retain the source’s deterministic Boolean target-function model:', 'The target labels are deterministic:')
defs=d['definitions']
a=defs.index('A computable nondecreasing positive integer function')
b=defs.index('This exact-real arithmetic model')
defs=defs[:a]+defs[b:]
revise('4592', 'Quasipolynomial accuracy exponent for Gaussian agnostic halfspace learning',
       r'Do there exist constants \(C,K>0\) and one uniform randomized learner in the real-arithmetic model below such that, for every dimension \(n\ge2\), rational inverse excess error \(t\ge3\), and permitted Boolean target, its training cost plus output-evaluation cost is at most \[K n^{C\log_2 t}\] on every execution, and it succeeds with probability at least \(2/3\)? '+guarantee,
       'Selected the n^(O(log(1/epsilon))) possibility explicitly posed by the source, retaining deterministic target labels, improper output and exact-real computation.',
       ['The learner receives Gaussian examples labeled by an arbitrary fixed Boolean function.', 'Its predictor must perform almost as well as the best affine halfspace.', 'The question asks whether the dimension exponent can grow only logarithmically with inverse excess error.', 'Training and prediction evaluation are both charged in the specified real-arithmetic model.', 'Statistical-query restrictions or general stochastic labels cannot silently replace this model.'],
       definitions=defs, refs=['https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2014.793'])
