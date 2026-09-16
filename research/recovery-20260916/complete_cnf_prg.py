"""Individual review of the sub-log-squared CNF/DNF generator target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1133'
claim=read_claims(ROOT)[identifier]
refs=[
 ref('primary','Theory of Unconditional Pseudorandom Generators','Pooya Hatami; William M. Hoza',2023,
 'https://eccc.weizmann.ac.il/report/2023/019/revision/2/',
 'Revision 2, 14 April 2023; Definition 1.4.1, §1.4.1 and Open Problem 5.3.5, printed p. 90'),
 ref('ac0','Improved Pseudorandom Generators for AC⁰ Circuits','Xin Lyu',2022,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2022.34',
 'CCC 2022, 34:1–34:25; Theorem 1, §3.2 wire-size convention and Theorem 8 for CNFs/DNFs'),
 ref('readk','Pseudorandomness for read-k DNF formulas','Rocco A. Servedio; Li-Yang Tan',2019,
 'https://www.cs.columbia.edu/~rocco/papers/soda19.html',
 'SODA 2019, pp. 621–638; author abstract states the read-k seed bound'),
 ref('hitting','Optimal Hitting Set Generators via A Potential-Descent Framework','Gonen Krak',2026,
 'https://eccc.weizmann.ac.il/report/2026/178/',
 'Submitted 6 September 2026; published on ECCC 13 September 2026; abstract concerns hitting sets for read-once formulas and width-three programs'),
]
notes=[
 'Recovered error 0.1 and the strict little-o bound, rather than fixing an unspecified inverse-polynomial error.',
 'Made polynomial formula size explicit by quantifying every fixed size exponent, with one uniform generator taking the size bound.',
 'Defined CNF and DNF, literal occurrences and formula size, with arbitrary clause width and variable reuse.',
 'Explained complementation equivalence and separated unrestricted formulas from read-k and read-once results.',
 'Preserved the importance and category; specified Lean proof of the complete binary existence target.',
]
sources=[
 'Read the April 2023 survey’s uniformity convention and Open Problem 5.3.5: polynomial size, error 0.1 and seed o(log^2 n).',
 'Read Lyu CCC 2022 Theorems 1 and 8 and §3.2. The formula seed is O(log(m) log(m/epsilon) log log(m)); formula size is measured by wires.',
 'Read Servedio–Tan’s SODA 2019 author abstract: the logarithmic-in-size seed depends polynomially on the read bound and does not cover arbitrary reuse at that scale.',
 'Checked the September 2026 ECCC TR26-178 abstract and publication dates. It claims hitting sets for read-once formulas, not probability preservation for all polynomial-size CNFs. Its full proof was not audited.',
 'Checked the published Hatami–Hoza survey copy, Open Problem 5.2, which retains the same target. A bounded primary-source search through 16 September 2026 found no resolution.',
]
status=('The survey explicitly asks for error 0.1 and seed little-o of log-squared input length for all polynomial-size CNFs and DNFs. '
 'The checked general bound still has a log-squared scale with an additional log-log factor. '
 'Shorter seeds for bounded-read formulas and the September 2026 hitting-set claim have narrower guarantees. '
 'No resolution was found in the bounded review through 16 September 2026; this is not an independent certification of all cited proofs.')
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Does there exist one uniform explicit family of generators
\[
G_{n,m}:\{0,1\}^{s(n,m)}\longrightarrow\{0,1\}^{n}
\qquad(n\ge2,\ m\ge n)
\]
such that both of the following hold?

For every \(n,m\) and every CNF or DNF formula \(F\) on \(n\) Boolean variables with size at most \(m\),
\[
\left|\Pr_{Y\sim U_{s(n,m)}}[F(G_{n,m}(Y))=1]
-\Pr_{X\sim U_n}[F(X)=1]\right|\le\frac1{10}.
\]
For every integer \(c\ge1\),
\[
\lim_{n\to\infty}
\max_{\substack{m\in\mathbb N\\n\le m\le n^c}}
\frac{s(n,m)}{(\log_2 n)^2}=0.
\]
Thus every fixed polynomial size regime has sub-log-squared seed length. The generator depends on \(n,m\), but not on the particular formula.''',
 definitions=r'''A literal is a variable \(x_i\) or its negation \(1-x_i\). A clause is an OR of literals; a CNF is an AND of clauses. A term is an AND of literals; a DNF is an OR of terms. An empty OR is zero and an empty AND is one. Variables may occur in arbitrarily many clauses or terms, and there is no bound on the width of a clause or term.

Size is the number of literal occurrences plus the number of clauses, for a CNF, or plus the number of terms, for a DNF. Each occurrence counts separately. This is the number of wires in the corresponding depth-two circuit when negations are attached to input literals. Counting clauses or terms instead gives the same class of polynomial-size families: after redundant repetitions inside a clause or term are removed, each contains at most \(2n\) literals. The all-polynomial-exponents target is unchanged by that polynomial conversion. A formula using fewer than \(n\) variables is permitted.

\(U_r\) is the uniform distribution on the \(r\)-bit strings, including the singleton empty string when \(r=0\). The generator is deterministic on its parameters and seed. A single uniform pair of deterministic Turing machines computes \(s(n,m)\) from \((1^n,1^m)\) and computes \(G_{n,m}(y)\) from \((1^n,1^m,y)\), respectively. Both run in at most \(C(n+m)^k\) bit operations for fixed \(C>0\) and integer \(k\ge1\). They receive neither the test formula, advice, nor an oracle. On each polynomial-size regime this is polynomial time in \(n\), as in the source's explicitness convention.

The little-o assertion means that for every fixed \(c\ge1\) and every \(\eta>0\), there is \(N\) such that \(s(n,m)\le\eta(\log_2 n)^2\) whenever \(n\ge N\) and \(n\le m\le n^c\). The threshold may depend on \(c,\eta\). The error \(1/10\) is fixed; an inverse-polynomial error guarantee is not an additional requirement.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of this existence assertion. A positive answer must construct the uniform algorithms and verify the running time, the error against every allowed formula, and the little-o seed bound in every fixed polynomial-size regime. It suffices to prove the guarantee for CNFs and derive it for DNFs by complementation, or conversely. A negative answer must disprove the unrestricted statement, rather than only one generator design. This binary target is exact and has no numerical \(1/100\) tolerance. Results for bounded variable occurrence, bounded clause width, hitting sets alone, or a selected collection of test formulas do not meet the full target.''',
 source_formulation=dict(text=r'The source asks for an efficiently computable generator that fools every polynomial-size CNF and DNF to error \(0.1\), using \(o((\log n)^2)\) seed bits.',
 caption='Paraphrase of Open Problem 5.3.5, April 2023 revision; polynomial-size and explicit-family conventions are expanded here.',citation='primary',format='editorial_paraphrase'),
 why='CNFs and DNFs are basic Boolean tests with only two layers, but variables can participate in many overlapping constraints. A seed below the log-squared scale would improve unconditional derandomization for this core model and reduce the cost of enumerating all generator outputs to estimate satisfying fractions.',
 references=refs,
 context_blocks=[
 block('A uniform random assignment satisfies a formula with some probability. The generator must reproduce that probability up to a fixed additive error simultaneously for all formulas under the size bound. It cannot be tailored to the formula whose satisfying fraction will later be estimated.'),
 block('The complement of a CNF is a DNF of the same size after every literal is negated, and conversely. Complementing a Boolean output preserves the absolute difference of expectations. Consequently the two formula types form one equivalent pseudorandomness target, rather than two separate construction problems.'),
 block(r'Lyu’s Theorem 8 records the general bound \(O(\log m\cdot\log(m/\varepsilon)\cdot\log\log m)\). For fixed error and \(m=n^{O(1)}\), it becomes \(O((\log n)^2\log\log n)\). Removing only the final log-log factor would reach log-squared seed length; the card requires an asymptotic improvement beyond that scale.','ac0'),
 block(r'For read-\(k\) DNFs, each variable appears at most \(k\) times. Servedio and Tan obtain seed \(\operatorname{poly}(k,\log(1/\varepsilon))\log M+O(\log n)\) for \(M\) terms. For fixed \(k\) and error this is logarithmic in polynomial formula size, but the unrestricted class allows \(k\) to grow with that size.','readk'),
 block('Averaging a formula over all seeds gives an additive estimate of its satisfying fraction with deterministic cost proportional to the number of seeds times the evaluation cost. This interpretation explains the seed objective. It does not give a relative approximation to very small satisfying fractions or a decision procedure for formulas with only one satisfying assignment.'),
 block('A September 2026 preprint claims optimal hitting-set generators for read-once CNFs and related classes. A hitting set guarantees an accepted output when acceptance density is sufficiently large; it does not approximate that density. Its read-once restriction and weaker success condition both distinguish it from this card. The review checked the claim’s scope, not its full proof.','hitting'),
 ],
 progress=[
 progress('2019','Bounded-read DNFs admit the shorter seed stated by Servedio and Tan; arbitrary variable reuse remains outside that guarantee.','readk'),
 progress('2022','Lyu’s depth-two case matches the known general CNF/DNF seed bound, retaining a log-log factor beyond log-squared at constant error.','ac0'),
 progress('2023-04-14','The source explicitly poses the constant-error sub-log-squared target.'),
 progress('2026-09-13','The new ECCC hitting-set claim concerns read-once formulas, a narrower test class and guarantee.','hitting'),
 progress('2026-09-16','Individual review supplies the missing size, uniformity and error quantifiers; no resolution was found.'),
 ],
),notes,sources,status,summary=[
 'A CNF is an AND of clauses, and a DNF is an OR of terms, with unrestricted reuse of variables.',
 'The target is one uniform polynomial-time generator that preserves satisfying fractions within one tenth.',
 'For every fixed polynomial formula-size bound, the seed must be little-o of log-squared input length.',
 'The checked general seed bound has log-squared length with an additional log-log factor.',
 'Bounded-read constructions and recent hitting-set results do not resolve the unrestricted probability-preservation target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
