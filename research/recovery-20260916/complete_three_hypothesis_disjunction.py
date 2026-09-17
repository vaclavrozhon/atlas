"""Make the source's disjunctive fine-grained hypothesis explicit."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6950';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the exact disjunction as one yes/no target; it is not a demand to establish all three hypotheses or merely a reduction between problems.',
 'Used the original sources’ classical randomized integer word-RAM setting and made the error, time and uniformity conventions explicit.',
 'Specified fixed-width SAT, polynomial-weight exact APSP and integer 3SUM, including the order of all exponent quantifiers.',
 'For APSP adopted the modern forall-epsilon/exists-weight-exponent convention already used in TCS-6937, rather than silently requiring one universal hard weight exponent.',
 'Distinguished this source’s randomized hypotheses from deterministic SETH, Las Vegas 3SUM and arbitrary-real APSP variants on related cards.',
 'Checked the original disjunction, the 2022 real-input alternative and the conditional scope of the 2026 APSP universe reduction.',
 'Individually assessed importance and required a complete Lean-checked proof or refutation of the disjunction.',
]
sources=[
 'Read Vassilevska Williams, On Some Fine-Grained Questions in Algorithms and Complexity, author-hosted ICM 2018 survey https://people.csail.mit.edu/virgi/eccentri.pdf: Sections 2.1–2.2, Hypotheses 1–3 and model, PDF pp.4–6; Section 6, Two Problems Harder than CNF-SAT, 3-SUM and APSP, PDF p.19. The disjunction uses randomized algorithms, integer inputs and logarithmic-size words; 3SUM Hypothesis 2 fixes universe [-n^4,n^4].',
 'Read Abboud–Vassilevska Williams–Yu, Matching Triangles and Basing Hardness on an Extremely Popular Conjecture, SIAM Journal on Computing 47(3):1098–1122 (2018), DOI 10.1137/15M1050987, primary author-hosted journal PDF. Read the hypotheses and Conjecture 1 on p.1099 and Section 1.1, Theorem 1.1 on p.1100. The paper explicitly includes randomized algorithms and gives conditional consequences, not a proof of its conjecture. Preliminary version STOC 2015.',
 'Read Chan–Vassilevska Williams–Xu, arXiv:2203.08356v1, 16 March 2022, abstract and Introduction, Hypotheses 1–2 and the statement distinguishing integer from real inputs. Its weaker real-APSP/real-3SUM/OV disjunction is a different hypothesis and does not settle the retained one.',
 'Read Fischer, Universe Reduction for APSP: Equivalence of Three Fine-Grained Hypotheses, arXiv:2603.27736v1, 29 March 2026: abstract; Hypothesis 1.1 and footnotes 1–3, printed p.1; and Theorem 1.13 scope. The weaker order forall epsilon exists c is explicit. Its three equivalent hypotheses concern different APSP weight regimes and the equivalence is conditional, not an equivalence of SETH, APSP and 3SUM.',
 'Bounded primary-source searches through 17 September 2026 found no verified proof or refutation of the displayed disjunction. The mathematical assertions in the contextual progress record were checked at their stated theorem/definition level; complete published reduction proofs were not independently reconstructed or Lean-certified.',
]
complete(identifier,dict(
 title='Disjunction of randomized SETH, integer APSP and 3SUM hypotheses',
 criterion='resources',question_type='yes_no',
 importance=dict(score=92,method='editorial',reason='A proof would supply one shared foundation for many fine-grained lower bounds without deciding which of the three core problems is hard; a refutation would require major algorithmic improvements for all three.'),
 formal=r'''Is the following disjunction true in the uniform randomized word-RAM models defined below?
\[
H_{\mathrm{SAT}}\ \lor\ H_{\mathrm{APSP}}\ \lor\ H_{\mathrm{3SUM}},
\]
where
\[
\begin{aligned}
H_{\mathrm{SAT}}&:\quad
 \forall\varepsilon\in\mathbb Q\cap(0,1)\ \exists k\ge3:
 \neg\operatorname{FastSAT}(k,\varepsilon),\\
H_{\mathrm{APSP}}&:\quad
 \forall\varepsilon\in\mathbb Q\cap(0,1)\ \exists c\ge1:
 \neg\operatorname{FastAPSP}(c,\varepsilon),\\
H_{\mathrm{3SUM}}&:\quad
 \forall\varepsilon\in\mathbb Q\cap(0,1):
 \neg\operatorname{Fast3SUM}(\varepsilon)?
\end{aligned}
\]
The quantified \(k,c\) are integers. The predicates assert algorithms with respective time bounds \(K2^{(1-\varepsilon)n}(L+1)^d\), \(Kn^{3-\varepsilon}\), and \(Kn^{2-\varepsilon}\), and success probability at least \(2/3\) on each input. Each time bound holds on every random tape.''',
 definitions=r'''For \(\operatorname{FastSAT}(k,\varepsilon)\), an input is an explicit Boolean CNF formula on exactly its \(n\) occurring variables \(x_1,\ldots,x_n\). It is a conjunction of clauses, each containing at most the fixed \(k\) literals; a literal is a variable or its negation. Empty clauses are false and an empty conjunction is true. Repeated clauses and literals are allowed, with no density, occurrence or satisfiability promise. The output is one exactly specified bit: whether an assignment in \(\{0,1\}^n\) makes the formula true. The encoding explicitly lists \(n\), the number of clauses, each clause length and its signed variable indices. To fix its bit length \(L\), encode each nonnegative integer \(a\) by \(1^b0\) followed by the \(b\)-bit binary expansion of \(a+1\), where \(b=\lfloor\log_2(a+1)\rfloor+1\); a sign uses one bit. All records must be present, with no trailing bits, all variable indices valid and every declared variable occurring. The input bits are supplied as an explicit array. A fast SAT predicate asserts existence of one finite program, integers \(d\ge1,B\ge8\), and \(K\ge1\) giving the stated bound on all such formulas. These choices may depend on \(k,\varepsilon\). Malformed strings are rejected in polynomial time. Cases with no occurring variables are decided directly.

For \(\operatorname{FastAPSP}(c,\varepsilon)\), an input is an explicit adjacency matrix of a directed graph on \(n\ge2\) numbered vertices, with a presence flag and a signed integer weight for each ordered vertex pair. Present weights belong to \([-n^c,n^c]\). The graph is promised to have no negative-weight directed cycle. Absent edges have a flag rather than a large finite cost; self-loops, negative edges, equal distances and zero-weight cycles are allowed. The output is the entire \(n\times n\) matrix of exact shortest-walk distances, using a separate unreachable flag. Empty walks have cost zero. Under the promise each finite distance is attained and has magnitude at most \((n-1)n^c\). The algorithm succeeds only when the whole matrix is correct. The fast predicate asserts existence of a finite program, a word-size factor \(B\ge c+4\), and \(K\ge1\), all depending at most on \(c,\varepsilon\). No path listing or behavior on a graph violating the promise is required.

For \(\operatorname{Fast3SUM}(\varepsilon)\), an input is an explicit list of \(n\ge2\) distinct integers from \([-n^4,n^4]\). The required bit is whether three distinct indices \(i,j,\ell\) satisfy \(a_i+a_j+a_\ell=0\), using ordinary integer addition. For \(n<3\) the answer is no. The program, \(K\ge1\) and word-size factor \(B\ge8\) may depend on \(\varepsilon\), but not on the list or \(n\). This fixes the single-set, polynomial-universe integer formulation; it is not a question about arbitrary real inputs or solely the number of comparisons.

For SAT set \(N=L+2\); for APSP and 3SUM set \(N=n+2\). A word has \(w=B\lceil\log_2N\rceil\) bits. Programs are sequential classical word RAMs with a fixed finite instruction list, one-word addresses and initially zero work cells. Unit-cost instructions are reads, writes, copies, comparisons, conditional branches, bitwise Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and unsigned quotient and remainder by a nonzero divisor. Shifts by at least \(w\) return zero; division by zero is invalid. Larger quantities use multiple words with every constituent operation charged. Signed input integers use two's-complement encoding; the chosen word-size bounds accommodate all input values and required outputs. A random instruction supplies one fresh independent fair bit. Every access, random bit, preprocessing step, lookup-table construction and output write counts. There is no advice, oracle, unit-cost arbitrary-precision operation or quantum operation. The address space contains \(2^w\) cells; the logarithmic-word convention is explicit also for SAT, rather than silently allowing exponential-space address words.

For every fixed input, the required correctness probability is over the algorithm's coins, not an input distribution. The time guarantee holds for every coin sequence. Deterministic algorithms are included. Constants and programs in each fast predicate are fixed before choosing an input. The exponent saving is any positive fixed constant; rational savings below one capture existence of any such saving by decreasing it if needed. The SAT polynomial factor may depend on the fixed clause width. In \(H_{\mathrm{APSP}}\), the hard weight exponent \(c\) may depend on \(\varepsilon\); one absolute \(c\) working for every saving is not required.

The disjunction permits any one, two or all three hypotheses to hold. Its negation requires all three to fail: one SAT saving that works for every fixed clause width, one APSP saving that works for every fixed polynomial weight exponent, and one 3SUM saving. The three savings may differ, and the algorithms for different fixed widths or weight exponents may differ. No effective compiler from a width or weight exponent to its algorithm is required.

These are the source's randomized integer variants. In particular, \(H_{\mathrm{SAT}}\) is not defined by copying the deterministic Turing-machine SETH card, and \(H_{\mathrm{3SUM}}\) is not defined as the literal negation of the separate Las Vegas expected-time, three-list card. The polynomial-integer APSP quantifier order agrees with the explicitly stated modern convention on its separate hypothesis card.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of this disjunction or its logical negation. A positive proof need not identify a particular true disjunct constructively, but must establish that at least one holds in the specified models. A refutation must establish failure of all three hypotheses with their full quantifier order and correctness/time requirements; the algorithms and positive savings need not be the same for the three tasks.

Proving only a conditional lower bound from the disjunction, relating two hypotheses, or improving algorithms by logarithmic or other subpolynomial factors does not resolve this target. There is no additive numerical tolerance and no requirement of a prescribed minimum saving such as one hundredth.''',
 source_formulation=dict(text='The survey asks for a more robust foundation for fine-grained hardness by considering the conjecture that at least one of SETH, the APSP Hypothesis and the 3SUM Hypothesis holds. The primary paper states this as Conjecture 1 and explicitly allows randomized algorithms.',caption='ICM 2018 survey, Section 6, PDF p.19; Abboud–Vassilevska Williams–Yu, Conjecture 1, SIAM Journal on Computing 47(3), p.1099.',citation='primary',format='editorial_paraphrase'),
 why='Many precise algorithmic lower bounds rest on one of these three separate assumptions. Establishing their disjunction would support results that are hard under all three while requiring less than any individually chosen hypothesis. Refuting it would require fixed-exponent algorithmic advances across satisfiability, weighted shortest paths and integer sum detection.',
 references=[
 ref('primary','On Some Fine-Grained Questions in Algorithms and Complexity','Virginia Vassilevska Williams',2018,'https://people.csail.mit.edu/virgi/eccentri.pdf','ICM 2018 author survey; Sections 2.1–2.2, Hypotheses 1–3, PDF pp.4–6; Section 6, Two Problems Harder than CNF-SAT, 3-SUM and APSP, PDF p.19'),
 ref('origin','Matching Triangles and Basing Hardness on an Extremely Popular Conjecture','Amir Abboud; Virginia Vassilevska Williams; Huacheng Yu',2018,'https://doi.org/10.1137/15M1050987','SIAM Journal on Computing 47(3):1098–1122; Conjecture 1, p.1099, and Theorem 1.1, p.1100; preliminary version STOC 2015; primary author-hosted journal PDF read'),
 ref('real','Hardness for Triangle Problems under Even More Believable Hypotheses: Reductions from Real APSP, Real 3SUM, and OV','Timothy M. Chan; Virginia Vassilevska Williams; Yinzhan Xu',2022,'https://arxiv.org/abs/2203.08356v1','16 March 2022; Introduction, Hypotheses 1–2, integer-versus-real scope; STOC 2022, DOI 10.1145/3519935.3520032'),
 ref('quantifiers','Universe Reduction for APSP: Equivalence of Three Fine-Grained Hypotheses','Nick Fischer',2026,'https://arxiv.org/abs/2603.27736v1','29 March 2026; Hypothesis 1.1 and footnotes 1–3, printed p.1; abstract and Theorem 1.13, conditional equivalence of APSP variants; STOC 2026'),
 ],
 related=['TCS-6595','TCS-6937','TCS-0557','TCS-6949'],
 context_blocks=[
 block('A disjunction is a weaker assumption than choosing any one of its component hypotheses. Consequently, a consequence proved separately from each component also follows from the disjunction.'),
 block('The original work supplies common hard triangle problems and derives conditional consequences. These reductions motivate the joint assumption; they do not prove that it is true.','origin'),
 block('Later work obtains related hardness from a different disjunction involving real-number inputs and Orthogonal Vectors. That variation must retain its own model and is not substituted here.','real'),
 block('The 2026 universe-reduction paper compares three APSP variants under additional assumptions. Its title does not refer to establishing equivalence among SETH, APSP and 3SUM.','quantifiers'),
 ],
 progress=[progress('2015','The original STOC paper introduces the disjunction and derives consequences through triangle problems.','origin'),progress('2018','The journal version states Conjecture 1 explicitly; the ICM survey records it as a shared basis for fine-grained hardness.'),progress('2022-03-16','A different, weaker real-input/OV disjunction supports further conditional triangle hardness.','real'),progress('2026-03-29','The APSP universe-reduction preprint specifies the weight-exponent quantifier order and conditional relationships among APSP variants.','quantifiers')],
),notes,sources,'The source explicitly conjectures the randomized disjunction. A bounded primary-source review through 17 September 2026 found no verified resolution of the displayed formulation. The 2022 real-input alternative and the 2026 conditional equivalences of APSP variants do not prove or refute it. Current-status review is bounded and is separate from the completed statement review.',summary=[
 'The question asks whether at least one of three core fine-grained hardness hypotheses is true.',
 'They concern fixed-width Boolean satisfiability, exact shortest paths with polynomially bounded integer weights, and integer 3SUM.',
 'The selected variants allow classical randomized word-RAM algorithms with bounded error and worst-case running time.',
 'Refuting the disjunction requires a fixed positive exponent saving for all three tasks, with the clause-width and weight-range quantifiers respected.',
 'A complete Lean-checked proof or refutation is required; existing conditional reductions do not settle the assertion.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
