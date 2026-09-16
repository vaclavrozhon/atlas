"""Individual review of standard-order width-four pseudorandomness."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1125'
claim=read_claims(ROOT)[identifier]
refs=[
 ref('primary','Theory of Unconditional Pseudorandom Generators','Pooya Hatami; William M. Hoza',2023,
 'https://eccc.weizmann.ac.il/report/2023/019/revision/2/',
 'Revision 2, 14 April 2023; Definition 1.4.1 and §1.4.1; Definition 3.2.1, Theorem 3.2.6 and Open Problem 3.2.7, printed pp. 48–51'),
 ref('width3','Pseudorandom Generators for Width-3 Branching Programs','Raghu Meka; Omer Reingold; Avishay Tal',2019,
 'https://arxiv.org/abs/1806.04256',
 'STOC 2019 result; abstract distinguishes ordered and arbitrary-order programs'),
 ref('inwsums','On Sums of INW Pseudorandom Generators','William M. Hoza; Zelin Lv',2025,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2025.67',
 'APPROX/RANDOM 2025, 67:1–67:21; §1.1 and Theorems 7–8, pp. 67:5–67:6'),
 ref('weighted','Improved Error Reduction for Weighted PRGs','Ben Chen; Gil Cohen; Dean Doron; Yuval Khaskelberg; Amnon Ta-Shma',2026,
 'https://eccc.weizmann.ac.il/report/2026/064/revision/3/',
 'Revision 3, 4 May 2026; introduction and Theorem 1.1 / Corollary 1.2; the conclusion is a weighted PRG'),
]
notes=[
 'Recovered the source’s constant error 0.1, standard input order, width four and strict little-o seed target.',
 'Specified one uniform polynomial-time generator and seed-length procedure, independent of the branching program.',
 'Defined the layered program, arbitrary transition functions and final accepting set without regularity or permutation assumptions.',
 'Separated a standard PRG from hitting sets and weighted generators, and from lower bounds restricted to the INW template.',
 'Preserved the existing importance and category and added a complete Lean acceptance condition.',
]
sources=[
 'Read ECCC TR23-019 revision 2 §1.4, Definition 3.2.1, Theorem 3.2.6 and Open Problem 3.2.7. The exact error is 0.1 and the order is x_1 through x_n.',
 'Checked the Meka–Reingold–Tal primary abstract: nearly logarithmic seed for width three does not cover width four.',
 'Read Hoza–Lv’s ECCC text and the published APPROX/RANDOM 2025 introduction and Theorems 7–8. The XOR-of-INW upper bound remains log-squared; its lower bound applies to guarantees based only on spectral expansion.',
 'Read ECCC TR26-064 revision 3 abstract, introduction, Theorem 1.1 and Corollary 1.2. The new error reduction produces weighted generators, not the ordinary output distribution required here.',
 'A bounded primary-source search through 16 September 2026 found no resolution. Full proofs of all related theorems were not reconstructed.',
]
status=('The 2023 source poses this exact constant-error width-four target. '
 'The published 2025 Hoza–Lv paper and the May 2026 revised weighted-generator paper still identify the general log-squared barrier. '
 'The checked new results concern a restricted construction or weighted generators, and do not meet this card. '
 'No resolution was found in the bounded review through 16 September 2026.')
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a function \(s:\{2,3,\ldots\}\to\mathbb N\) and a uniform explicit family
\[
G_n:\{0,1\}^{s(n)}\longrightarrow\{0,1\}^{n}
\]
such that
\[
\lim_{n\to\infty}\frac{s(n)}{(\log_2 n)^2}=0
\]
and, for every \(n\ge2\) and every width-at-most-four, length-\(n\), standard-order read-once branching program \(B\),
\[
\left|\Pr_{Y\sim U_{s(n)}}[B(G_n(Y))=1]
-\Pr_{X\sim U_n}[B(X)=1]\right|\le\frac1{10}?
\]
The same \(G_n\) must work for all such programs \(B\).''',
 definitions=r'''For a nonnegative integer \(r\), \(U_r\) denotes the uniform distribution on all \(r\)-bit strings, with \(U_0\) the distribution on the empty string. The seed \(Y\) is the generator's only randomness; its length counts individual independent fair bits.

A length-\(n\) standard-order read-once branching program has nonempty layers \(V_0,\ldots,V_n\), with \(|V_i|\le4\), a start state \(v_0\in V_0\), an accepting set \(F\subseteq V_n\), and transition functions \(\tau_i:V_{i-1}\times\{0,1\}\to V_i\) for \(1\le i\le n\). On input \(x=(x_1,\ldots,x_n)\), it sets \(v_i=\tau_i(v_{i-1},x_i)\), and outputs one exactly when \(v_n\in F\). Transitions may merge states and may differ between layers. No regularity, reversibility or permutation property is assumed. Each bit is read exactly once, in the fixed order \(x_1,\ldots,x_n\).

Uniform explicitness means that there are fixed deterministic Turing machines \(S,G\), a constant \(C>0\) and an integer \(k\ge1\) such that, for every \(n\ge2\), \(S(1^n)\) outputs \(s(n)\), and \(G(1^n,y)\) outputs \(G_n(y)\) for every seed of that length, each in at most \(Cn^k\) bit operations. Neither machine receives \(B\), advice depending on \(n\), or an oracle. A family of unrelated short descriptions or a distribution whose support is found by unbounded search is not explicit in this sense.

The little-o condition requires every positive constant \(\eta\) to have a threshold \(N_\eta\) such that \(s(n)\le\eta(\log_2 n)^2\) whenever \(n\ge N_\eta\). A smaller constant multiplying \((\log n)^2\) does not suffice.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the stated existence assertion. A positive answer must specify the uniform algorithms and prove their polynomial running time, the little-o seed bound, and the additive \(1/10\) error simultaneously for every allowed program and length. A negative answer must refute the unrestricted existence assertion; a limitation of one construction or proof method is insufficient. This binary question has no numerical \(1/100\) acceptance tolerance. A hitting-set guarantee, a weighted average of program outputs, and a theorem only for width three do not establish the required probability comparison.''',
 source_formulation=dict(text=r'The source asks for an explicit constant-error generator whose seed is asymptotically smaller than \((\log n)^2\), for arbitrary width-four programs reading their input bits in standard order.',
 caption='Paraphrase of Open Problem 3.2.7 in the April 2023 revision; explicitness follows §1.4.',citation='primary',format='editorial_paraphrase'),
 why='Four states are enough to make the best general seed bound resist the improvements known for three states. Resolving this precise transition would clarify a central obstacle in pseudorandomness for sequential, space-limited computation. The question is significant even though its constant-width formulation alone is not an assertion that all randomized logarithmic-space computation can be derandomized.',
 references=refs,
 context_blocks=[
 block('A branching program is a sequence of small state machines. Its transition rules can change at every step, so a four-state memory does not make the whole test independent of the input length. A generator must preserve the accepting fraction for every possible sequence of those rules.'),
 block(r'The source records the Nisan and Impagliazzo–Nisan–Wigderson bound \(O(\log(wn/\varepsilon)\log n)\) for width \(w\), length \(n\) and error \(\varepsilon\). At width four and error \(1/10\), this gives \(O((\log n)^2)\), which is the scale the question asks to improve.'),
 block(r'Width two admits seed length \(O(\log(n/\varepsilon))\). For width three, Meka, Reingold and Tal obtain \(\widetilde O(\log n\log(1/\varepsilon))\) in standard order; the tilde suppresses factors polynomial in logarithms of logarithms. These results place the unresolved threshold at a remarkably small number of states.','width3'),
 block('The 2025 Hoza–Lv result analyzes bitwise sums of independent INW outputs and recovers the known seed scale. Its obstruction concerns guarantees that use only the spectral expansion of the graphs in that template. It is compatible with shorter seeds from other constructions, and is not a negative solution of this card.','inwsums'),
 block('A weighted generator estimates an acceptance probability using coefficients attached to generated strings. Those coefficients need not describe the distribution of an ordinary sample. The May 2026 error-reduction theorem improves such weighted generators; its conclusion therefore has a different guarantee from the one required here.','weighted'),
 block('A hitting set has an even weaker requirement: it must contain an accepted string whenever enough uniformly random strings are accepted. That existence guarantee alone does not control the fraction of accepted generated strings. The target here concerns the full additive error in that fraction.'),
 ],
 progress=[
 progress('2023-04-14','Revision 2 poses the width-four, standard-order, constant-error little-o seed question explicitly.'),
 progress('2025','Hoza and Lv retain the log-squared seed scale and prove a restricted XOR-of-INW obstruction.','inwsums'),
 progress('2026-05-04','The revised error-reduction result improves weighted PRGs; it does not supply the ordinary width-four generator required here.','weighted'),
 progress('2026-09-16','Individual review fixes the model and quantifiers and finds no resolution in the bounded later-work check.'),
 ],
),notes,sources,status,summary=[
 'The tests are branching programs that read each input bit once and keep at most four states.',
 'One uniform polynomial-time generator must preserve every test’s acceptance probability within one tenth.',
 'Its seed must be little-o of the square of the logarithm of the output length.',
 'Nearly logarithmic seeds are known for width three, while the general width-four bound remains log-squared in the checked sources.',
 'Recent weighted-generator results and restrictions on INW constructions do not resolve this ordinary-generator question.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
