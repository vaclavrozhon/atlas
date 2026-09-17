"""Review constant-gap Euclidean unique-SVP hardness in an explicit oracle model."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0648';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='NP-hardness of Euclidean unique SVP with a fixed gap greater than one',
 status='source_open',criterion='reductions',question_type='yes_no',
 formal=r'''Is there an absolute rational constant \(\gamma>1\) such that the search problem \(\gamma\text{-uSVP}_2\) is NP-hard under classical randomized polynomial-time oracle reductions?

The input is an explicitly encoded integer lattice basis \(B\), promised to satisfy
\[
\lambda_2(\mathcal L(B))>\gamma\lambda_1(\mathcal L(B)).
\]
The required answer is an exact shortest nonzero lattice vector. The uniqueness gap \(\gamma-1\) must be a positive constant independent of the input dimension and bit length.''',
 definitions=r'''A lattice basis is a matrix \(B\in\mathbb Z^{m\times n}\) with \(m\ge n\ge2\) and linearly independent columns. Dimensions and all entries are explicitly encoded in binary with delimiters; let \(L\) be the total input length. Its lattice is
\[
\mathcal L(B)=\{Bz:z\in\mathbb Z^n\}\subseteq\mathbb R^m.
\]
All lengths use the Euclidean norm \(\|v\|_2=(\sum_i v_i^2)^{1/2}\). The first successive minimum \(\lambda_1\) is the minimum length of a nonzero lattice vector. The second successive minimum \(\lambda_2\) is the smallest radius of a closed ball centered at zero containing two linearly independent lattice vectors. Independence is over \(\mathbb R\). Rank \(n\), ambient dimension \(m\), and coefficient bit length can all grow with the input.

Under the strict gap promise there are exactly two shortest vectors, differing by sign. A valid answer is a binary integer coefficient vector \(z\ne0\) such that \(\|Bz\|_2=\lambda_1(\mathcal L(B))\). Either sign is allowed. The gap concerns independent directions, not merely the second distinct vector, which would always include the negative of a shortest vector. The output target is exact recovery, not an approximation of the shortest length.

Use the following randomized Cook-reduction meaning of NP-hardness for this promise search problem. An admissible oracle is any total function which, on a basis satisfying the promise, returns a valid shortest-vector coefficient vector and, on any other query, can return an arbitrary string or a distinguished failure symbol. Bound every response to a query of length \(L\) by \(4(L+1)^3\) bits. This is only an encoding convention: shortest-vector coefficients for an explicit integer basis have a polynomial bit bound of this size, by bounding an invertible minor and using a basis column as an upper bound on shortest length. The oracle need not be computable or choose the same sign on different bases.

NP-hardness here means that there exist one classical probabilistic multitape oracle Turing machine \(R\) and constants \(K,a>0\) such that for every Boolean 3-CNF formula \(F\) of encoded length \(s\), and for every admissible oracle \(O\), every execution of \(R^O(F)\) uses at most \(K(s+1)^a\) bit operations and
\[
\Pr[R^O(F)=1]\ge2/3\quad\text{if }F\text{ is satisfiable},\qquad
\Pr[R^O(F)=0]\ge2/3\quad\text{otherwise}.
\]
The probability is over independent fair random bits of \(R\). A 3-CNF is a conjunction of clauses, each a disjunction of at most three Boolean variables or their negations. The reduction may make adaptive queries; writing them and reading oracle responses are charged, while the oracle's internal computation is not. On well-formed lattice queries outside the gap promise no correctness is presumed of the oracle, and the reduction must tolerate every permitted response. The constants and \(\gamma\) are fixed before any formula is received. Thus a polynomial-time solver for the promise problem would yield a bounded-error polynomial-time algorithm for every NP language.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of such randomized oracle NP-hardness for some fixed γ > 1, including the reduction, its bit complexity and its guarantee for every admissible oracle, or a proof of the negation of this existence claim. Hardness only for a dimension-dependent gap tending to one, a non-Euclidean norm, a superpolynomial-time reduction or a separate nonstandard lattice-hardness hypothesis does not establish the target. Failure of one proposed reduction does not refute it.',
 why='A constant separation between the shortest lattice direction and every independent competitor is a strong geometric promise. Proving NP-hardness despite that promise would show that isolating a shortest vector does not remove the worst-case difficulty of Euclidean lattice search.',
 source_formulation=dict(text='Open Problem 4.6 asks for randomized NP-hardness of Euclidean unique SVP for some constant uniqueness factor greater than one. The card spells out a bounded-error polynomial-time oracle reduction for the search formulation.',caption='The Complexity of the Shortest Vector Problem, §4.2, Open Problem 4.6, printed p.15 / PDF p.17.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','The Complexity of the Shortest Vector Problem','Huck Bennett',2023,'https://www.cs.umd.edu/~gasarch/open/svp-color.pdf','24 January 2023 full version of the SIGACT News column; §1.1 lattice conventions and §4.2 Unique SVP / Open Problem 4.6, printed p.15, PDF p.17'),
 ref('smallgap','Improved hardness results for unique shortest vector problem','Divesh Aggarwal; Chandan K. Dubey',2016,'https://doi.org/10.1016/j.ipl.2016.05.003','Information Processing Letters 116(10), 631–637; accompanying arXiv preprint 1112.1564, §4 Theorem 4, pp.7–8, gives a gap 1+1/poly(n)'),
 ref('rotations','Just how hard are rotations of Zⁿ? Algorithms and cryptography with the simplest lattice','Huck Bennett; Atul Ganju; Pura Peetathawatchai; Noah Stephens-Davidowitz',2023,'https://eprint.iacr.org/2021/1548','Revision dated 10 April 2023; Theorem 1.1 and hardness discussion pp.2–3; Definition 2.8 p.8'),
 ref('othernorms','Deterministic Hardness of Approximation of Unique-SVP and GapSVP in ℓ_p norms for p>2','Yahli Hecht; Muli Safra',2025,'https://arxiv.org/abs/2510.16991v1','19 October 2025; §1 prior unique-SVP results, and Theorems 1.3–1.4 with p>2 and stronger running-time assumptions'),
 ],
 context_blocks=[
 block('The 2023 source distinguishes ordinary approximate shortest-vector hardness from unique shortest-vector hardness. Its explicitly open target is a fixed Euclidean uniqueness factor greater than one.'),
 block('Aggarwal and Dubey obtain randomized hardness with a uniqueness gap of 1+1/poly(n). Such a gap tends to one and therefore does not supply the fixed positive separation in this card.','smallgap'),
 block('The rotation-lattice reduction proves hardness for constant uniqueness factors if finding shortest vectors in rotations of the integer lattice is hard. Its authors explicitly label that source assumption nonstandard; it is not a reduction establishing NP-hardness.','rotations'),
 block('The October 2025 paper gives new unique-SVP hardness for norms with p>2 under hypotheses on subexponential or quasipolynomial algorithms. Its theorems do not cover p=2. Its related-work discussion also distinguishes fine-grained constant-gap results from polynomial-time NP-hardness.','othernorms'),
 block('The two signs of a shortest vector cannot be separated by a uniqueness promise. The promise instead compares the first two successive minima, and the oracle convention retains arbitrary behavior whenever that promise fails.','rotations'),
 ],
 progress=[progress('2016','Randomized NP-hardness is established for a gap greater than one by an inverse polynomial, rather than by a fixed constant.','smallgap'),progress('2023','The source explicitly retains the constant-gap Euclidean NP-hardness question; the rotation-lattice result supplies a different conditional hardness statement.','rotations'),progress('2025','Deterministic unique-SVP hardness is strengthened in norms p>2 under stronger running-time assumptions; this leaves the selected Euclidean NP-hardness target untouched.','othernorms')],
),[
 'Recovered the exact Euclidean constant-gap target and defined successive minima, the independent-direction promise and exact vector output.',
 'Specified explicit integer bases, both dimension parameters, polynomial output encoding and classical bounded-error oracle NP-hardness.',
 'Required success for every admissible oracle, including arbitrary replies outside the promise; no oracle behavior is silently assumed there.',
 'Checked inverse-polynomial-gap hardness, the distinct rotation-lattice assumption and the 2025 results for p>2.',
 'Preserved the individual importance assessment and required a complete Lean-checked reduction or negation.',
],[
 'Read Bennett’s full §4.2 unique-SVP discussion and Open Problem 4.6, with the source lattice definitions.',
 'Read the Aggarwal–Dubey arXiv preprint abstract and §4 reduction statement, Lemma 5 and Theorem 4; identified the separate 2016 journal publication.',
 'Read the April 2023 rotation-lattice revision’s Theorem 1.1, nonstandard-assumption qualification and Definition 2.8.',
 'Read Hecht–Safra October 2025 §1 prior-work discussion and Theorems 1.3–1.4; checked the available arXiv version and bounded later-work searches through 17 September 2026.',
], 'Source-open in Bennett’s 2023 Open Problem 4.6. The checked 2025 work excludes the Euclidean norm and uses stronger running-time assumptions. Known inverse-polynomial uniqueness gaps, rotation-lattice assumptions and fine-grained reductions do not supply this fixed-gap polynomial-time oracle NP-hardness statement. Bounded checks through 17 September 2026 found no matching resolution.',summary=[
 'The input is an explicit integer lattice basis in Euclidean space.',
 'It promises that every independent direction is longer than a shortest vector by one fixed factor greater than one.',
 'The task is to recover an exact shortest vector, with either sign allowed.',
 'The question asks whether this promise search problem is NP-hard under classical randomized polynomial-time oracle reductions.',
 'Shrinking uniqueness gaps and hardness in other norms do not establish this target, whose full proof or refutation must be Lean-checked.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
