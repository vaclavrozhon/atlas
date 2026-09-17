"""Review job-shop makespan approximation with only machines and accuracy as parameters."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6814';claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the general reentrant job-shop model from the source: a job can revisit machines arbitrarily many times and can omit machines.',
 'Specified explicit operation lists, positive binary integer durations, fixed machine assignments, chain precedence, nonpreemption and arbitrary waiting.',
 'Defined feasibility, optimal makespan, rational start-time output and a deterministic uniform bit-computation model.',
 'Expressed requested accuracies as 1/q for all positive integers q and required one computable parameter function F(m,q) times a polynomial in the complete encoding length.',
 'Made the polynomial exponent independent of machine count, accuracy and maximum operations per job; the latter must not enter the parameter-only factor.',
 'Corrected the source edition to the July 2018 accepted revision while retaining the 2017 import provenance.',
 'Distinguished the 2003 bounded-operations scheme from the open target, and checked 2026 transaction/conflict-graph work without transferring its guarantees.',
 'Replaced provisional importance 50 by an individual assessment of 86 and retained the parameterized-algorithms category for this parameter-dependence question.',
]
sources=[
 'Read Mnich–van Bevern, Parameterized complexity of machine scheduling: 15 open problems, arXiv:1709.01670v3 of 23 July 2018, accepted Computers & Operations Research 100:254–261 (2018), DOI 10.1016/j.cor.2018.07.020: Section 2.1.1 job-shop definition, Section 2.1.2 nonpreemption convention, approximation definitions and Section 5.2/Open Problem 13 on PDF p.7. Multiple operations of the same job may require the same machine. The question explicitly removes n_max from the approximation scheme’s parameter dependence.',
 'Read the primary SIAM abstract and metadata for Jansen–Solis-Oba–Sviridenko, Makespan Minimization in Job Shops: A Linear Time Approximation Scheme, SIAM Journal on Discrete Mathematics 16(2):288–300 (2003), DOI 10.1137/S0895480199363908. It fixes both machine count and operations per job. The precise F(m,n_max,epsilon)+O(n) dependency is also stated in the directly read 2018 survey. The 2003 full proof was not newly accessed, and its arithmetic running-time convention is not recast as an identical bit bound.',
 'Read Baccaert–Vandevoort–Ketsman, Bounding the Makespan of Transaction Schedules, ICDT 2026 Article 10, primary PDF: Introduction and Section 7 related-work discussion, which cites job-shop approximation for fixed machine count and maximum job length and explicitly distinguishes its transaction-serializability model. Its transaction results do not remove the maximum-operations parameter here.',
 'Read the primary abstract/history of Tellache–Azerine, arXiv:2609.04161v1, 3 September 2026, on job-shop scheduling with conflict graphs. It reports additional conflict constraints, formulations, a special polynomial case and heuristic experiments, not a universal parameterized approximation scheme. This abstract-level check is not a proof audit.',
 'Bounded searches through 17 September 2026 found no verified scheme depending only on machine count and reciprocal accuracy or a matching unconditional refutation. Known exact NP-hardness and parameterized exact algorithms do not alone decide approximation-scheme existence. The deterministic bit model, explicit encoding and reciprocal-integer accuracy grid make the source’s informal polynomial notation precise.',
]
complete(identifier,dict(
 title='Job-shop approximation parameterized only by machines and accuracy',criterion='resources',question_type='yes_no',
 formal=r'''Do there exist a total computable function \(F:\mathbb N_{\ge1}^2\to\mathbb N_{\ge1}\), an integer \(c\ge1\), and one uniform deterministic algorithm \(A\) such that, for every number of machines \(m\ge1\), accuracy parameter \(q\ge1\), and job-shop instance \(I\) defined below, \(A(I,q)\) returns a feasible schedule \(S\) satisfying
\[
C_{\max}(S)\le(1+1/q)\operatorname{OPT}(I)
\]
in at most \(F(m,q)(L+1)^c\) Turing-machine steps, where \(L\) is the complete binary input length? The number of operations per job is unbounded and may not be an additional parameter of \(F\).''',
 definitions=r'''An instance has machines \(1,\ldots,m\) and jobs \(1,\ldots,n\), with \(m,n\ge1\). Job \(j\) is an explicitly listed sequence of \(\ell_j\ge1\) operations. Its \(h\)-th operation has a prescribed machine \(\mu_{j,h}\in\{1,\ldots,m\}\) and a positive integer processing time \(p_{j,h}\), encoded in binary. Let \(N=\sum_{j=1}^n\ell_j\) be the total number of operations. A job may use the same machine repeatedly and may skip other machines. Neither \(\ell_j\) nor \(\max_j\ell_j\) is bounded as a function of \(m\). All jobs are available at time zero.

A schedule assigns a nonnegative real start time \(s_{j,h}\) to every operation. Each operation runs without interruption for exactly \(p_{j,h}\) time units on its prescribed machine. Job order must be respected:
\[
s_{j,h+1}\ge s_{j,h}+p_{j,h}
\qquad(1\le h<\ell_j).
\]
For any two distinct operations assigned to the same machine, their half-open processing intervals \([s_{j,h},s_{j,h}+p_{j,h})\) are disjoint. Equivalently, one operation must finish no later than the other starts. These are all feasibility constraints. Jobs may wait between consecutive operations; operations cannot be split, migrated to another machine or processed in parallel. There are no release dates, deadlines, setup times, inter-job precedence constraints or extra conflict-resource requirements.

The makespan and optimum are
\[
C_{\max}(S)=\max_{j,h}(s_{j,h}+p_{j,h}),
\qquad
\operatorname{OPT}(I)=\min_{S\text{ feasible}}C_{\max}(S).
\]
A feasible serial schedule exists. For these integer durations an optimal schedule with integer start times exists, so the displayed minimum is attained and is positive. The optimization domain nevertheless permits real start times. The algorithm must output one rational start time for each of the \(N\) operations, with signed binary numerator and positive binary denominator, in the input operation order. The output itself must be feasible and obey the approximation ratio; merely estimating the optimal value is insufficient.

The input contains binary encodings of \(m,n,q\), every \(\ell_j\), and all pairs \((\mu_{j,h},p_{j,h})\), with unambiguous separators. Their entire bit length is \(L\). Jobs and operations are listed individually; multiplicities, long repeated routes and durations are not expanded into unit-time jobs, and routes are not supplied by a succinct grammar. Processing times can be arbitrarily large relative to \(N\), so a bound polynomial in their numerical sum is not by itself a polynomial bound in \(L\).

The algorithm is one fixed deterministic multitape Turing machine with a fixed finite tape alphabet and finitely many tapes. A step reads and writes a constant number of cells and moves each head by at most one cell. All preprocessing, exact rational/integer arithmetic on individual bits, input reading and output writing are counted. There is no advice, uncharged parameter preprocessing, oracle or randomness. The function \(F\) is total computable, meaning that some fixed machine halts on every positive pair \((m,q)\) and outputs its value; no particular growth bound on \(F\) is imposed. The exponent \(c\) is one absolute constant, independent of \(m,q,I\).

The reciprocal-integer accuracy grid specifies an approximation scheme: for any desired rational \(0<\epsilon\le1\), choosing \(q=\lceil1/\epsilon\rceil\) gives ratio at most \(1+\epsilon\). This does not restrict the scheme to one fixed approximation ratio. The parameter-only factor may depend on machines and accuracy, but not on the number of jobs, maximum route length, processing-time magnitudes or other input features. Those features can contribute to the fixed polynomial in the full bit length. “Fixed-machine” means that each fixed \(m,q\) yields a polynomial-time guarantee; one uniform algorithm must still handle all \(m,q\).''',
 answer_criterion=r'''Give a complete mathematically correct proof checked in Lean of the stated existence proposition or its logical negation. A positive answer must specify one uniform algorithm, a total computable parameter bound \(F\), an absolute polynomial exponent, and prove feasibility, approximation and running time for every valid instance and every \(q\ge1\).

A scheme whose nonpolynomial factor also depends on the maximum number of operations per job, or whose input-length exponent depends on \(m\) or \(q\), does not meet the target. Neither exact optimization hardness, a heuristic with good observed schedules, a scheme only for nonreentrant routes, nor an algorithm for a different shop model settles it. A conditional impossibility theorem establishes only its conditional conclusion. There is no additive numerical tolerance on this algorithm-existence question.''',
 source_formulation=dict(text='Open Problem 13 asks whether general job-shop makespan admits a (1+epsilon)-approximation in f(m,epsilon) times a polynomial, removing the maximum number of operations per job from the known parameter dependence. The source’s model expressly permits repeated visits to a machine. This card specifies the full explicit binary input length and a reciprocal-integer accuracy parameter to make its resource claim precise.',caption='Mnich–van Bevern, 23 July 2018 revision, Sections 2.1 and 5.2, Open Problem 13 on p.7.',citation='primary',format='editorial_paraphrase'),
 why='Machine count alone is a natural measure of shop complexity, but long job routes can still encode difficult interactions. An approximation scheme with no separate route-length parameter would clarify whether near-optimal schedules remain tractable on a fixed shop even when individual jobs revisit machines many times.',
 importance=dict(score=86,method='editorial',assessed_on=DATE,reason='A general approximation-scheme question for a central scheduling model, testing whether machine count and accuracy suffice despite arbitrarily long reentrant job routes. Its significance is the removal of an entire structural parameter, not a small improvement to one approximation ratio.'),
 references=[
 ref('primary','Parameterized complexity of machine scheduling: 15 open problems','Matthias Mnich; René van Bevern',2018,'https://arxiv.org/abs/1709.01670v3','23 July 2018 accepted revision; Sections 2.1, 2.3 and 5.2, Open Problem 13, PDF p.7; Computers & Operations Research 100:254–261, DOI 10.1016/j.cor.2018.07.020'),
 ref('bounded','Makespan Minimization in Job Shops: A Linear Time Approximation Scheme','Klaus Jansen; Roberto Solis-Oba; Maxim Sviridenko',2003,'https://doi.org/10.1137/S0895480199363908','SIAM Journal on Discrete Mathematics 16(2):288–300; primary abstract, fixed machines and fixed operations per job; parameter dependence also discussed in the 2018 survey'),
 ],
 context_blocks=[
 block('General job-shop routes are ordered lists of machine-specific operations. A small number of machines does not limit the number of times a job can return to them.'),
 block('Jansen, Solis-Oba and Sviridenko obtain an approximation scheme when both the machine count and the maximum number of operations per job are fixed. This additional route-length parameter is exactly what the question seeks to remove.','bounded'),
 block('The survey contrasts the job-shop dependency with schemes for open-shop and flow-shop models. Their different ordering and route assumptions prevent those guarantees from automatically answering the job-shop question.'),
 block('A polynomial-time approximation scheme for each fixed machine count can still have an input exponent depending on accuracy. The requested bound places all machine-count and accuracy dependence in one computable multiplicative factor.'),
 block('Exact optimization hardness does not exclude an approximation scheme. Likewise, exact fixed-parameter tractability for different parameter combinations does not establish the requested dependence.'),
 ],
 progress=[progress('2003','The linear-time approximation scheme requires fixed machine count and fixed maximum operations per job.','bounded'),progress('2018-07-23','The accepted survey revision states Open Problem 13, asking for a scheme parameterized only by machines and accuracy.')],
),notes,sources,'The 2018 accepted survey explicitly poses this parameter-dependence question. Bounded primary-source checks through 17 September 2026 found no verified resolution for arbitrary reentrant job routes. The 2003 scheme fixes an extra route-length parameter; checked recent transaction and conflict-graph papers use different constraints and do not supply the required scheme. This review verifies statements and model scope without independently checking every cited proof.',summary=[
 'Each job is a prescribed sequence of nonpreemptive operations on specified machines, with repeated machine visits allowed.',
 'The objective is to finish all jobs within a factor arbitrarily close to the optimum makespan.',
 'The requested running time is a fixed polynomial in the complete input length times a computable function of machine count and accuracy.',
 'Known schemes use the additional parameter of maximum operations per job, which must be removed here.',
 'A complete Lean-checked answer must establish or refute this uniform approximation scheme for arbitrarily long job routes.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
