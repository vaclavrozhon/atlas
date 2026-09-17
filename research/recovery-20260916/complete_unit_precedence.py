"""Complete exact unit-job scheduling for every fixed machine count."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-0935'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the every-fixed-machine-count question from the source, rather than selecting only three machines or making the machine count an unrestricted input parameter.',
 'Defined discrete unit slots, arbitrary precedence DAGs, simultaneous execution, makespan and the empty instance.',
 'Specified deterministic polynomial bit time with an exponent allowed to depend on the fixed machine count.',
 'Applied the default absolute 1/100 numerical-output convention and explained polynomial-time rounding to the integral optimum.',
 'Checked the SODA 2025 subexponential result and January 2026 journal metadata, distinguishing exact and approximate algorithms and machine-eligibility variants.',
 'Preserved importance 84 and the substantive relation to TCS-6676, whose target instead concerns approximation with a variable machine count and arbitrary positive durations.',
]
sources=[
 f'Read Antoine Amarilli’s live research-question section “Complexity of makespan scheduling of unit jobs with precedence constraints” on {DATE}, including the fixed k definition, the k=1 and k=2 cases, explicit polynomial-time question for k>2 and link to Nederlof et al. The source page is undated; the access date was not treated as an original posing date.',
 'Read Nederlof–Swennenhuis–Węgrzycki, arXiv:2312.03495v1 (6 December 2023), abstract and §1 pp. 1–3, Open Question 1 and Theorem 1.1. Checked the SODA 2025 publisher abstract and metadata: pp. 535–552, online 7 January 2025, DOI 10.1137/1.9781611978322.16. Publisher-deposited Crossref metadata confirms ACM Transactions on Algorithms online 3 January 2026, DOI 10.1145/3785365; the journal PDF was inaccessible, so full statement locators refer to the checked preprint.',
 'Read Das–Wiese, ESA 2022 Article 40, abstract and §1 pp. 40:1–40:2, covering exact two-machine solvability, the fixed-machine open question and quasipolynomial approximation schemes.',
 'Read Guruswami–Ren–Tang, arXiv:2607.26590v1 (29 July 2026), introduction pp. 1–2. Its hard unit-job model assigns each job to a prescribed machine in advance, unlike free assignment on identical machines here.',
 f'Bounded primary-source searches through {DATE} found no polynomial-time solution or unconditional impossibility theorem for every fixed number of machines. Results adding delays, generalized precedences, prescribed machines or special precedence structures do not settle the target.',
]
status='Amarilli’s current source retains the fixed-machine polynomial-time question. The exact subexponential advance appeared at SODA 2025 and online in ACM Transactions on Algorithms in January 2026; it does not give polynomial time even for three machines. No resolution of the all-fixed-machine-count target was found in the bounded later-work review.'
complete(identifier,dict(
 title='Polynomial-time unit-job precedence scheduling on fixed machines',
 criterion='resources',question_type='yes_no',
 formal=r'''For every fixed integer \(k\ge3\), can the minimum makespan of unit-duration jobs with arbitrary precedence constraints be computed in deterministic polynomial time on \(k\) identical machines?

For a finite directed acyclic graph \(G\), let \(\mu_k(G)\) be the least number of time slots needed to execute all its vertices as jobs, using at most \(k\) jobs per slot and executing every job strictly after its predecessors. The precise target is
\[
\forall k\ge3\ \exists A_k,C_k,c_k\ \forall G,
\]
where \(A_k\) is one uniform deterministic algorithm, \(C_k,c_k\ge1\) are integers, and on every valid \(L\)-bit encoding of \(G\), \(A_k\) halts in at most \(C_k(L+1)^{c_k}\) steps and outputs a rational number \(a\) satisfying
\[
|a-\mu_k(G)|\le\frac1{100}.
\]
The numerical output convention is equivalent here to computing the optimum integer exactly, by rounding in polynomial bit time.''',
 definitions=r'''The input graph is \(G=([n],E)\), with \(n\ge0\). It has no loops, parallel arcs or directed cycles. An arc \((u,v)\) means that job \(u\) must finish before job \(v\) starts. All transitive consequences are enforced; the input need not already be transitively closed. There is no restriction on the height, width, indegrees or outdegrees of this graph.

Each job has duration one and can run on any of \(k\) identical unit-speed machines. For an integer \(T\ge0\), a schedule of length \(T\) is a function
\[
s:[n]\to\{0,\ldots,T-1\}
\]
such that \(|s^{-1}(t)|\le k\) for every slot \(t\), and \(s(u)<s(v)\) for every arc \((u,v)\). Job \(v\) executes throughout the half-open interval \([s(v),s(v)+1)\). Distinct jobs in the same slot are assigned to distinct machines; such assignments always exist because of the cardinality bound. A successor may start when a predecessor finishes, but they cannot execute in the same slot.

The makespan optimum \(\mu_k(G)\) is the minimum \(T\) admitting such a schedule. Idle capacity is allowed. For the empty graph it is zero; for \(n>0\) it is an integer between one and \(n\), since a topological order yields a sequential feasible schedule. The model is offline: the whole graph is supplied before computation. There are no release dates, extra deadlines, communication delays, machine eligibility restrictions, setup costs, preemption or migration during a job.

The graph is encoded by \(1^n0\) followed by its \(n^2\) adjacency bits in row-major order, including zero diagonal entries. Require no trailing bits. Its length is \(L=n+1+n^2\). Invalid encodings, including cyclic graphs, must be rejected within the same polynomial time bound. The machine count \(k\) is fixed for the algorithm and is not another input field.

Computation uses a deterministic multitape Turing machine with one fixed finite program, fixed finite tape alphabets, read-only input and initially blank work tapes. Each transition accesses the cells under its heads and moves each head by at most one cell. All parsing, arithmetic and output are charged. No advice, randomness or oracle is allowed.

An output rational is specified by a signed integer numerator \(p\) and a positive integer denominator \(q\), with value \(a=p/q\). Use one sign bit for \(p\), followed by self-delimiting binary codes for \(|p|\) and \(q\); the code for a nonnegative integer \(b\) is the binary representation of \(b+1\), prefixed by its bit length in unary and a zero separator. All output bits count toward the running time. Rounding \(p/q\) to its unique nearest integer can be performed in polynomial time in these bit lengths, and the \(1/100\) error bound guarantees that this integer is \(\mu_k(G)\). An exact integer output also qualifies by taking denominator one.

The quantifiers permit the program, multiplicative constant and polynomial exponent to depend on \(k\). Each program must work on every graph size and every permitted graph. The card does not require one exponent independent of \(k\), a polynomial bound when \(k\) is part of the input, or an effective compiler producing \(A_k\) from \(k\). A positive result only for \(k=3\) would settle the first unresolved case but would not by itself establish the displayed assertion for all larger fixed counts.

The requested output is the optimum value; outputting an optimal schedule is sufficient but is not an additional requirement. A multiplicative approximation with a fixed nonzero relative error is generally too coarse to recover this integer optimum.''',
 answer_criterion=r'''Supply a complete Lean-checked proof of the all-fixed-\(k\) algorithm-existence proposition, with the full correctness, output precision and polynomial bit-time bounds; or supply a complete Lean-checked proof of its negation. A negative answer must identify one fixed \(k\ge3\) for which no such polynomial-time algorithm exists. NP-hardness with the machine count supplied as input is insufficient. NP-completeness for one fixed count gives only a conditional negative answer unless \(\mathrm P\ne\mathrm{NP}\) is also proved. A subexponential exact algorithm or a quasipolynomial approximation scheme does not meet the polynomial-time requirement.''',
 source_formulation=dict(
 text='The source fixes a number k of processors, repeatedly removes at most k currently available vertices from a precedence DAG, and asks whether the minimum number of rounds can be computed in polynomial time for k greater than two.',
 caption=f'Paraphrase of Amarilli’s unit-job makespan question, read {DATE}; the fixed count and discrete rounds are explicit in the source.',
 citation='primary',format='editorial_paraphrase'),
 why='With unit-duration jobs and identical machines, the only remaining source of scheduling difficulty is the interaction between a partial order and limited parallel capacity. Polynomial solvability for each fixed machine count would identify a major tractable boundary in precedence scheduling. The three-machine case has resisted classification since the classical scheduling complexity literature, despite the recent subexponential advance.',
 references=[
 ref('primary','List of open questions: Complexity of makespan scheduling of unit jobs with precedence constraints',
  'Antoine Amarilli',None,
  'https://a3nm.net/work/research/questions/#complexity-of-makespan-scheduling-of-unit-jobs-with-precedence-constraints',
  f'Undated live research-question section; accessed {DATE}; fixed processor count, discrete scheduling model and polynomial-time question'),
 ref('exact','A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints',
  'Jesper Nederlof; Céline M. F. Swennenhuis; Karol Węgrzycki',2025,
  'https://doi.org/10.1137/1.9781611978322.16',
  'SODA 2025:535–552, online 7 January 2025; checked arXiv:2312.03495v1, 6 December 2023, §1 Open Question 1 and Theorem 1.1, p. 1. Journal version: DOI 10.1145/3785365, online 3 January 2026'),
 ref('approximation','A Simpler QPTAS for Scheduling Jobs with Precedence Constraints',
  'Syamantak Das; Andreas Wiese',2022,'https://doi.org/10.4230/LIPIcs.ESA.2022.40',
  'ESA 2022, Article 40; abstract and §1, pp. 40:1–40:2, exact two-machine case and fixed-machine approximation results'),
 ref('assigned','Inapproximability of Unique-Machine Precedence Scheduling for Unit-Length Jobs',
  'Venkatesan Guruswami; Xuandi Ren; Shaoxuan Tang',2026,'https://arxiv.org/abs/2607.26590v1',
  'Version 1, 29 July 2026; §1 pp. 1–2, prescribed machine assignments and distinction from identical-machine scheduling'),
 ],
 context_blocks=[
 block('One machine needs exactly one slot per job. Two machines admit a polynomial-time exact algorithm. The source asks about every larger fixed count, with three as the first unresolved case.'),
 block(r'The checked exact-algorithm preprint proves a running time of \((1+n/k)^{O(\sqrt{nk})}\). For fixed \(k\), this is subexponential in the number of jobs, but its exponent is not bounded as required for polynomial time. The work appeared at SODA 2025 and online in journal form in January 2026.','exact'),
 block('Quasipolynomial-time approximation schemes for fixed machine counts provide schedules whose lengths are close in relative terms to optimum. They neither give polynomial running time nor determine the exact optimum from a fixed relative error.','approximation'),
 block('When the number of machines is unrestricted input, the decision problem is NP-hard. That theorem does not settle polynomial solvability separately at every fixed machine count.','exact'),
 block('The July 2026 unit-job hardness paper studies a different model in which the machine for every job is prescribed. Here a job may use any identical machine, so that hardness does not resolve this target.','assigned'),
 ],
 progress=[
 progress('2022','The checked approximation paper records exact solvability on two machines and the open fixed-machine question.','approximation'),
 progress('2023-12-06','The preprint gives the subexponential exact algorithm and explicitly retains the three-machine classification question.','exact'),
 progress('2025-01-07','The subexponential result is published in the SODA proceedings.','exact'),
 progress('2026-01-03','Publisher-deposited metadata dates the journal version online.','exact'),
 progress(DATE,'The live source still asks for polynomial time at each fixed larger count; the review makes that quantifier order and numerical output criterion explicit.'),
 ],
),notes,sources,status,summary=[
 'Every job takes one time slot, and a directed acyclic graph specifies which jobs must finish before others start.',
 'At most k jobs may run simultaneously on k identical machines.',
 'The question asks for polynomial-time computation of the minimum number of slots for every fixed k greater than two.',
 'The polynomial and algorithm may depend on k, but must handle all job counts and precedence graphs.',
 'The recent exact subexponential algorithm improves the general upper bound without establishing the requested polynomial time.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
