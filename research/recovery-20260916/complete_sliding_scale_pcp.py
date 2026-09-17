"""Complete the inverse-polynomial-error endpoint of sliding-scale PCPs."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7268';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the existence of some inverse-polynomial soundness exponent, constant symbol-query count, logarithmic randomness and polynomial proof length and alphabet.',
 'Made the fixed-proof-before-randomness quantifiers explicit, with perfect completeness and soundness against every proof without computational restrictions.',
 'Used padded length and alphabet bounds and a padded uniform random tape to specify all input lengths without free nonuniform advice.',
 'Retained the admitted card’s permission for adaptive queries; the source definition itself presents nonadaptive queries, and no equivalence between those conventions is assumed.',
 'Defined explicit 3-CNF encodings, paid bit-time and symbol-oracle access, excluding an interactive prover, cryptographic soundness and unbounded symbol sizes.',
 'Checked the source conjecture and theorem, the 2025 quasi-linear constant-error result, and two March 2026 revisions; preserved importance 94 and complete Lean acceptance.',
]
sources=[
 'Read Dinur–Harsha–Kindler, arXiv:1505.06362v1, submission record 23 May 2015 (downloaded PDF title page carries 18 August 2018): Definition 1.1 p. 1, Conjecture 1.3 and Main Theorem 1.4 p. 2. The former asks for a constant number of symbol queries; the latter uses polyloglog queries at inverse-polynomial error. The source defines nonadaptive predicates; the admitted card already permits adaptive queries and retains that convention explicitly.',
 'Read Bafna–Minzer–Vyas–Yun, Quasi-Linear Size PCPs with Small Soundness from HDX, STOC 2025, primary MIT repository abstract and publication metadata dated 15 June 2025. It gives two queries and arbitrarily small constant soundness, not inverse-polynomial soundness with all other parameters simultaneously fixed as required here.',
 'Read Amireddy–Behera–Srinivasan–Sudan–Willumsgaard, arXiv:2511.03703v3, revised 24 March 2026: abstract, Section 2 and Theorem 2.3, and the PCP-theorem discussion. The new single-composition construction has constant soundness in its theorem; its subexponential-size basic ingredient is also not the polynomial-size inverse-error endpoint. No full proof audit was performed.',
 'Read Hair–Sahai, ECCC TR25-153 Revision 1 of 29 March 2026: Section 7 p. 16, Conjecture 7.1. The polynomial-alphabet inverse-polynomial-error constant-query statement is still explicitly a conjecture used for the stronger lattice-hardness corollary. Its hardness theorem does not prove that conjecture.',
 f'Bounded primary-source checks through {DATE} found no verified construction or unconditional negation covering the selected target. Existing linear-size PCP and ETH-to-Gap-ETH cards concern different quantitative requirements.',
]
complete(identifier,dict(
 criterion='construction',question_type='yes_no',
 formal=r'''Do there exist positive integers \(a,b,d,q\), real constants \(c>0\) and \(K>0\), and one uniform deterministic oracle Turing machine \(V\) satisfying the following conditions? For every encoded 3-CNF formula \(F\) of bit length \(N\), set
\[
 r_N=\left\lceil a\log_2(N+2)\right\rceil,\qquad
 M_N=(N+2)^b,\qquad \Sigma_N=\{0,1,\ldots,M_N-1\}.
\]
Given \(F\), a uniformly random string \(R\in\{0,1\}^{r_N}\), and oracle access to a fixed proof \(\pi\in\Sigma_N^{M_N}\), the verifier makes at most \(q\) symbol queries, halts in at most \(K(N+2)^d\) bit operations, and accepts or rejects. It must have perfect completeness and inverse-polynomial soundness:
\[
\begin{aligned}
 F\text{ satisfiable}&\ \Longrightarrow\ 
   \exists\pi\ \forall R:\ V^\pi(F,R)=1,\\
 F\text{ unsatisfiable}&\ \Longrightarrow\ 
   \forall\pi:\ \Pr_R[V^\pi(F,R)=1]\le (N+2)^{-c}.
\end{aligned}
\]
All constants and the verifier are independent of \(F\) and \(N\).''',
 definitions=r'''A Boolean literal is a variable or its negation. A 3-CNF formula is a finite conjunction of clauses, each a disjunction of at most three literals. Satisfiability means that some assignment of Boolean values to all variables appearing in the formula makes every clause true. The empty conjunction is true and an empty clause is false; repeated literals and repeated clauses are allowed.

Fix the following explicit encoding. For a nonnegative integer \(z\), let \(\operatorname{bin}(z)\) be its binary expansion, with \(\operatorname{bin}(0)=0\), and encode it by \(1^t0\operatorname{bin}(z)\), where \(t\) is the expansion length. Encode a formula by its clause count, then for each clause its length in \(\{0,1,2,3\}\), then its literals. A literal is one sign bit followed by the code of its positive integer variable index. There is no additional declared variable count and no trailing data. The parameter \(N\) is the length of this entire binary representation, including indices and delimiters. Invalid encodings may simply be rejected and are not part of the completeness and soundness requirements.

The proof has \(M_N\) addressable locations, each containing one symbol from \(\Sigma_N\). A query specifies one index in \(\{1,\ldots,M_N\}\) and returns that symbol encoded in \(\lceil\log_2 M_N\rceil\) bits. The same index always gives the same answer. A query reads one whole symbol, not one arbitrary subset of the proof or an unbounded-length answer. Repeated requests count again toward the query limit. The verifier has no other access to the proof; it may not scan the proof without paying queries. Forming addresses and reading or processing the returned bits count toward its bit running time.

The proof is chosen before \(R\) and is fixed throughout the verification. On a satisfiable formula, the same witnessing proof must be accepted for every random string. On an unsatisfiable formula the error bound holds for every possible proof, including proofs produced with unlimited computation and proofs unrelated to any satisfying assignment. No proof may depend on the subsequently sampled verifier randomness. The verifier may choose later query addresses using earlier answers, as allowed by the existing card; it is otherwise deterministic once the input, random string and oracle are fixed. A standard nonadaptive verifier satisfying these guarantees would in particular meet the target, but nonadaptivity is not an additional requirement here.

Using exactly the displayed proof length, alphabet and random-tape length is a padding convention. Shorter proofs and smaller alphabets can be embedded in these bounds and unused random bits can be ignored. Positive integer exponents absorb constant polynomial factors and logarithmic ceiling effects. The common exponent \(b\) bounds both proof length and alphabet size; it need not be optimal. There is no required relation between \(a,b,c\) beyond positivity. The query bound \(q\) is a fixed integer, while each queried symbol contains \(O(\log(N+2))\) bits. Thus the target permits more than a constant number of proof bits, but not a growing number of queried symbols.

The verifier is a single finite classical program, with no advice, cryptographic assumption, trusted setup, interaction or quantum operations. All of its computation, including parsing, computing the displayed parameters, reading randomness, generating query addresses and computing the decision, must satisfy the polynomial bit-time bound for every valid formula, proof and random string. The construction of a witnessing proof need not be efficient; the assertion is its existence. There is no separate honest prover participating during verification.

Only some fixed positive exponent \(c\) is requested. The question does not demand an optimal exponent, a two-query verifier, an alphabet of constant size, or proof length linear in the formula size. The near-linear-size constant-error PCP problem is a different parameter target.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the existence of the constants and uniform verifier, including the two proof/randomness quantifier orders, the resource bounds on every execution, perfect completeness and the stated information-theoretic soundness; or give a complete Lean-checked proof of the logical negation.

A positive result must achieve polynomial length, polynomial alphabet, logarithmic randomness, constant symbol-query complexity and inverse-polynomial error simultaneously. A constant-error construction, an error exponent tending to zero, a superconstant query bound, or a superpolynomial-size proof is insufficient without an additional proved transformation establishing every required bound. A negative answer must exclude every choice of the fixed constants and every permitted verifier, including adaptive verifiers. Conditional implications under unproved assumptions do not unconditionally decide the target.''',
 source_formulation=dict(text='Conjecture 1.3 asks for a constant-query PCP whose alphabet grows polynomially with inverse error while the randomness remains logarithmic. The selected endpoint asks for some inverse-polynomial error and polynomial-size alphabet and proof. Main Theorem 1.4 reaches inverse-polynomial error with a polyloglogarithmic, rather than constant, number of queries.',caption='Paraphrase of Dinur–Harsha–Kindler, Conjecture 1.3 and Main Theorem 1.4; the card retains its explicit adaptive-query convention.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Polynomially Low Error PCPs with polyloglog n Queries via Modular Composition','Irit Dinur; Prahladh Harsha; Guy Kindler',2015,'https://arxiv.org/abs/1505.06362v1','Submission 23 May 2015; downloaded PDF title page dated 18 August 2018; Definition 1.1 p. 1, Conjecture 1.3 and Main Theorem 1.4 p. 2'),
 ref('hdx','Quasi-Linear Size PCPs with Small Soundness from HDX','Mitali Bafna; Dor Minzer; Nikhil Vyas; Zhiwei Yun',2025,'https://dspace.mit.edu/entities/publication/9bbf3cdb-ea42-4d50-8d98-7b0f2c30432e','STOC 2025, pp. 45–53; primary abstract, publication metadata 15 June 2025'),
 ref('composition','Ideals, Macaulay Bases, and PCPs','Prashanth Amireddy; Amik Raj Behera; Srikanth Srinivasan; Madhu Sudan; Sophus Valentin Willumsgaard',2026,'https://arxiv.org/abs/2511.03703v3','24 March 2026 revision; abstract, Section 2, Theorem 2.3 and Section 7'),
 ref('later','SVP_p is Deterministically NP-Hard for all p > 2, Even to Approximate Within a Factor of 2^{log^{1−ε} n}','Isaac M. Hair; Amit Sahai',2026,'https://eccc.weizmann.ac.il/report/2025/153/revision/1/','Revision 1, 29 March 2026; Section 7 p. 16, Conjecture 7.1 and its separate use as an assumption'),
 ],
 why='Achieving very small verification error while reading only a constant number of logarithmic-size proof symbols would strengthen the quantitative reach of PCP theory and its hardness-of-approximation consequences.',
 context_blocks=[
 block('The usual PCP theorem provides constant error with constant local access. The selected endpoint asks for error falling as a fixed inverse power of input size without increasing the number of queried symbols.'),
 block('The modular-composition result achieves the desired inverse-polynomial error but still makes a polyloglogarithmic number of queries. This does not provide a fixed query constant.'),
 block('The 2025 high-dimensional-expander construction improves proof size while permitting arbitrarily small constant error. Fixing any such constant does not produce the input-dependent error required here.','hdx'),
 block('The March 2026 Macaulay-basis revision reduces the number of composition steps in a PCP construction. Its stated constant-soundness result and larger basic proof ingredient do not establish this endpoint.','composition'),
 block('The March 2026 lattice-hardness revision still states the polynomial-error constant-query PCP assertion as a conjecture and uses it conditionally for a stronger consequence.','later'),
 ],
 progress=[progress('2015-05-23','The source gives inverse-polynomial soundness with a polyloglogarithmic number of symbol queries.'),progress('2025-06-15','The STOC 2025 construction obtains quasi-linear proof size and two queries with arbitrarily small constant soundness.','hdx'),progress('2026-03-24','The revised Macaulay-basis construction gives a PCP theorem with one composition step, retaining constant soundness.','composition'),progress('2026-03-29','The revised lattice-hardness paper records the inverse-polynomial-error endpoint as Conjecture 7.1.','later')],
),notes,sources,'The source conjecture and the explicit restatement in the 29 March 2026 lattice-hardness revision remain unresolved in the bounded primary-source check through 17 September 2026. The recent constant-error and composition results do not establish all selected parameters simultaneously. This review does not independently audit their full proofs.',summary=[
 'A PCP verifier checks a fixed proof by inspecting a few selected symbols.',
 'The target asks for constant symbol queries, logarithmic randomness, and polynomial proof length and alphabet size.',
 'Satisfiable formulas must have a proof accepted on every random string.',
 'For an unsatisfiable formula, every proof must be accepted with probability at most a fixed inverse power of the input length.',
 'A complete Lean-checked resolution must achieve or rule out all of these guarantees simultaneously for one uniform verifier.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
