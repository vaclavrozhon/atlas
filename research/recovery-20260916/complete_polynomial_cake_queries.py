"""Complete the worst-case exact, complete envy-free cake-cutting target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6633';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the inherited deterministic polynomial-query existence target for complete exact envy-free allocation with disconnected pieces.',
 'Specified arbitrary nonatomic Borel probability measures, exact query access, all valid cut-oracle responses, and a uniform finite protocol with unrestricted finite local computation.',
 'Separated the source’s September 2026 single-exponential preprint bound from the polynomial target and the inherited average-case result from worst-case correctness.',
 'Required a complete Lean-checked protocol and universal bound or a refutation; positive envy, partial allocation and bounded but superpolynomial protocols do not qualify.',
 'Preserved the individually assessed importance score of 95 and removed detailed construction discussion from the problem context.',
]
sources=[
 'Read Ye–Bai, Cutting Down the Tower, arXiv:2609.05191v1, submitted 4 September 2026: Theorem 1.1 p. 3, model §2 p. 5, recursion and query count §4.6 pp. 22–23, polynomial-query open question §5 pp. 23–24, and exact-query implementation Appendix C pp. 28–29. The source permits unrestricted local computation and announces n^{O(1)}*2^n queries. Its complete collection of subroutine proofs was not independently certified.',
 'Read Brânzei–Nisan, The Query Complexity of Cake Cutting, NeurIPS 2022: §3 Robertson–Webb model, including restriction to discovered cut marks; exact connected and approximate allocation distinctions in the introduction.',
 'Read Procaccia, Thou Shalt Covet Thy Neighbor’s Cake, IJCAI 2009, model §2 and Theorem 3.1 (quadratic lower bound). The paper allows disconnected allocations and unrestricted query-based protocols; the lower bound does not exclude polynomial query complexity.',
 'Read the publisher abstract and metadata for Chèze, Social Choice and Welfare 67 (2026), published online 26 September 2025, DOI 10.1007/s00355-025-01633-7. The probability is over its uniform full-independence valuation model, not a worst-case arbitrary-profile guarantee.',
 f'Checked the arXiv submission history and bounded later-work searches through {DATE}; no later revision or verified polynomial worst-case resolution was found.',
]
complete(identifier,dict(
 title='Polynomial query complexity of exact envy-free cake cutting',criterion='construction',question_type='yes_no',
 formal=r'''Do there exist absolute integers \(C,d\ge1\) and one uniform deterministic Robertson–Webb protocol which, for every integer \(n\ge1\) and every profile of \(n\) nonatomic additive cake valuations, makes at most \(Cn^d\) queries and produces a partition \((A_1,\ldots,A_n)\) of the entire cake satisfying
\[
 \mu_i(A_i)\ge\mu_i(A_j)\qquad\text{for every }1\le i,j\le n?
\]
Every allocated piece may be a finite union of intervals. The allocation must be complete and exactly envy-free on every profile and for every valid choice of cut-query responses.''',
 definitions=r'''The cake is \([0,1]\). Agent \(i\)'s valuation \(\mu_i\) is an arbitrary nonatomic Borel probability measure: it is nonnegative and countably additive, \(\mu_i([0,1])=1\), and \(\mu_i(\{x\})=0\) for every point \(x\). A piece is a finite union of intervals, with endpoints assigned consistently to make the pieces disjoint. Endpoints have zero value for every agent. Measures need not have densities, and there is no bound on density, number of breakpoints or description complexity. No distribution over profiles is assumed.

The protocol receives \(n\) and accesses valuations only through these exact oracles:

\(\operatorname{Eval}(i,x,y)\), for known marks \(0\le x\le y\le1\), returns \(\mu_i([x,y])\).

\(\operatorname{Cut}(i,x,\alpha)\), for a known mark \(x\) and a requested real value \(0\le\alpha\le\mu_i([x,1])\), returns some \(y\in[x,1]\) such that \(\mu_i([x,y])=\alpha\). This returned coordinate becomes a known mark. Initially only \(0\) and \(1\) are known. Nonatomicity guarantees existence of an answer. If an interval has zero value, a cut may have several valid positions; every such response must preserve the guarantee. The protocol must issue only valid queries.

Each evaluation or cut call counts as one query. The protocol may combine interval values by additivity and use previously learned values without paying again. It may query one agent at a mark obtained from another. The final allocation must use endpoints among the known marks; arbitrary newly guessed endpoints are not available as free cuts.

Uniformity means one finite program for all \(n\). Between queries it may use integer computation, store and copy exact real answers, perform real addition, subtraction, multiplication and division by a nonzero number, and compare real numbers exactly. Its program has rational real constants and may perform arbitrary finite loops and finite searches. Only the number of oracle calls is bounded; no time, memory or bit-precision bound is imposed on this local computation. It must nevertheless terminate after finitely many operations on every allowed execution. This specifies a query model with exact real arithmetic, not a Turing computation of the digits of arbitrary valuation reals.

The output lists, for each agent, finitely many intervals with known endpoints. Their union covers \([0,1]\), and no interior point belongs to two agents' pieces. Shared boundary points are assigned to one incident piece. Empty pieces are allowed, but no positive-length residue may be discarded, even if all agents value it at zero.

Envy-freeness compares all pieces using the evaluating agent's own measure. It requires every displayed inequality exactly, with no additive or multiplicative fairness error. It does not require a connected piece per agent or impose any incentive-compatibility condition. The query bound is worst-case over both valuation profiles and valid oracle responses. There is no randomization or favorable-profile exception.''',
 answer_criterion=r'''Give a complete Lean-checked construction of one protocol and constants satisfying the statement, with proofs of query validity, termination, complete allocation, exact envy-freeness and the uniform polynomial query bound; or give a complete Lean-checked refutation of this existence claim in the specified model.

A protocol with an arbitrary finite bound depending on \(n\), a polynomial average-case or approximate-fairness guarantee, or a protocol leaving cake unallocated is insufficient. A lower bound for one particular procedure does not rule out all polynomial-query protocols. This is an existence question about an exact fairness property and an asymptotic resource bound, so numerical approximation of envy does not meet the answer criterion.''',
 source_formulation=dict(text='The September 2026 preprint improves the general exact complete-allocation query bound to a single exponential and explicitly asks whether subexponential or polynomial protocols are possible. This card retains the inherited polynomial worst-case target; the separate average-case result in its original reference does not answer that target.',caption='Paraphrase of Ye–Bai, arXiv:2609.05191v1, §5 pp. 23–24; query model §2 and Appendix C. This preserves the card’s existing exact, complete, disconnected-allocation scope.',citation='primary',format='editorial_paraphrase'),
 why='The question asks how much preference information is necessary to divide a continuous resource exactly without anyone preferring another person’s share. A polynomial query bound would separate the information needed for fairness from the enormous bounds in existing general protocols.',
 references=[
 ref('primary','Cutting Down the Tower: Single-Exponential Envy-Free Cake Cutting','Qilin Ye; Yannan Bai',2026,'https://arxiv.org/abs/2609.05191v1','Submitted 4 September 2026; Theorem 1.1 p. 3, model §2 p. 5, §4.6 pp. 22–23, open questions §5 pp. 23–24, exact oracle implementation Appendix C pp. 28–29'),
 ref('query','The Query Complexity of Cake Cutting','Simina Brânzei; Noam Nisan',2022,'https://proceedings.neurips.cc/paper_files/paper/2022/file/f7a7bb369e48f10e85fce85b67d8c516-Paper-Conference.pdf','NeurIPS 2022; introduction and §3, Robertson–Webb query and output-mark conventions'),
 ref('lower','Thou Shalt Covet Thy Neighbor’s Cake','Ariel D. Procaccia',2009,'https://www.cs.umd.edu/~gasarch/TOPICS/cake/lbenvyfreesq.pdf','IJCAI 2009, pp. 239–244; model §2 and Theorem 3.1, quadratic query lower bound'),
 ref('average','Envy-free cake cutting: a polynomial number of queries with high probability','Guillaume Chèze',2026,'https://doi.org/10.1007/s00355-025-01633-7','Social Choice and Welfare 67, pp. 1–20; published online 26 September 2025; publisher abstract specifies the uniform full-independence distribution on valuation profiles'),
 ],
 context_blocks=[
 block('The reported September 2026 bound is a fixed polynomial times two to the number of agents. It handles complete exact allocations and arbitrary nonatomic valuations, but remains exponential. The preprint itself keeps polynomial query complexity as an open direction.'),
 block('The quadratic lower bound is compatible with the polynomial target. It concerns general query protocols rather than merely showing that one historical procedure asks many questions.','lower'),
 block('The inherited high-probability result measures probability over a specified random valuation model. It does not ensure polynomially many queries for every fixed profile.','average'),
 block('Exactness, completeness and permission to allocate disconnected pieces all matter. Approximate allocations and connected allocations have different query-complexity questions. Counting only final cuts also differs from counting all preference queries used to find them.','query'),
 ],
 progress=[progress('2009','A general quadratic query lower bound is proved.','lower'),progress('2022','The query-complexity study distinguishes exact and approximate fairness and the role of connected allocations.','query'),progress('2025-09-26','The average-case polynomial-query result is published online.','average'),progress('2026-09-04','A preprint reports a single-exponential general bound and retains polynomial complexity as an open question.')],
),notes,sources,'The September 2026 primary preprint explicitly retains polynomial query complexity as open after reporting a single-exponential general upper bound. The inherited polynomial result concerns random valuation profiles, and the general quadratic lower bound does not rule out the target. Bounded checks through 17 September 2026 found no verified resolution; the full new preprint proof has not been independently certified.',summary=[
 'The cake is a continuous interval whose value may differ arbitrarily between agents.',
 'The task is to allocate all of it exactly without any agent preferring another agent’s piece.',
 'Preferences are learned only through exact value and cut queries, and disconnected pieces are allowed.',
 'One deterministic protocol must use polynomially many queries on every profile, although computation between queries is unrestricted.',
 'A complete Lean-checked solution must prove the full protocol guarantee or rule out every such polynomial query bound.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
