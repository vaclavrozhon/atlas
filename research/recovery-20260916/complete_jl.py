"""Complete the approved application-time target, separate from seed length."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0970'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']+[
 ref('bertinoro2011','Open Problems in Data Streams, Property Testing, and Related Topics',
     'Piotr Indyk; Andrew McGregor; Ilan Newman; Krzysztof Onak (compilers); Question 11 by Jelani Nelson',2011,
     'https://people.cs.umass.edu/~mcgregor/papers/11-openproblems.pdf',
     '14 June 2011 version, printed page 6, Question 11; application time and random-seed questions are separate'),
 ref('sparse2014','Sparser Johnson-Lindenstrauss Transforms','Daniel M. Kane; Jelani Nelson',2014,
     'https://arxiv.org/abs/1012.1577','JACM 61(1), article 4; arXiv full version, abstract and optimal-dimension sparse construction'),
 ref('fast2023','The Fast Johnson-Lindenstrauss Transform Is Even Faster',
     'Ora Nova Fandina; Mikael Møller Høgsgaard; Kasper Green Larsen',2023,
     'https://proceedings.mlr.press/v202/fandina23a.html',
     'ICML 2023, pp. 9689–9715; §§1–2, equation (3), dense-transform and sparse-input distinction'),
 ref('revisited2023','Sparse Dimensionality Reduction Revisited',
     'Mikael Møller Høgsgaard; Lion Kamma; Kasper Green Larsen; Jelani Nelson; Chris Schwiegelshohn',2023,
     'https://arxiv.org/abs/2302.06165v1','13 February 2023 preprint; abstract, dependence of sparsity on ambient dimension and point count'),
 ref('confidence2026','Optimal Confidence Bounds for Sparse Random Projections','Maciej Skorski',2026,
     'https://link.springer.com/article/10.1007/s10994-026-07057-3',
     'Machine Learning 115, article 153, published 20 June 2026; §2.1 Theorem 1 and equation (5), concentration rather than the requested application-time bound'),
]
notes=[
 'Applied the explicit user selection of fast sparse-vector application at optimal output dimension and removed the independent short-seed objective.',
 'Defined the pointwise oblivious JL guarantee, sparse-list input, dense output, arithmetic cost, setup-versus-application distinction and uniform constants.',
 'Retained dependence on ambient dimension alone in the polylogarithmic overhead; no hidden inverse-error or failure-probability factor multiplies the input sparsity.',
 'Compared sparse-matrix multiplication, dense fast transforms and recent concentration improvements without treating restricted lower bounds as a general impossibility.',
 'Preserved the assessed importance and category; supplied contextual motivation, dated source evidence, five-sentence summary and Lean acceptance.',
]
sources=[
 'Read original 2011 workshop PDF page 6 Question 11; its first question has pointwise norm preservation and (s+k)polylog(d) application time, while the second independently asks for a short seed.',
 'Read Kane–Nelson arXiv/JACM abstract and the 2023 Fast JL full PDF §§1–2, including equation (3) and the sparse-input comparison.',
 'Read arXiv:2302.06165v1 abstract and parameter scopes; sparse-column lower bounds do not cover arbitrary structured linear-transform evaluation.',
 'Read the June 2026 confidence paper §2.1 Theorem 1 and equation (5); its claimed concentration refinement retains inverse-distortion dependence in column sparsity and does not assert the selected application-time result.',
 'Bounded later-work search on 16 September 2026 found no resolution of the full parameter range. The reference proofs were not independently audited.',
]
status=('The 2011 source poses the application-time question separately from its seed-length question. The latter was removed by explicit user choice. '
        'Known sparse transforms and the inspected 2023 fast-transform bound do not give the requested sparsity-plus-output bound across all parameters. '
        'The inspected June 2026 paper concerns concentration constants and does not assert such an application algorithm. '
        'A bounded search on 16 September 2026 found no resolution of the selected target; this is a source-scope review, not an exhaustive open-status certificate or verification of every cited proof.')
complete(identifier,dict(
 title='Fast Johnson–Lindenstrauss transforms for sparse vectors',
 question_type='yes_no',
 formal=r'''Do there exist absolute constants \(C_1,C_2>0\), an integer \(q\ge0\), and uniform sampling and application algorithms with the following property? For every integer \(d\ge1\) and every \(0<\varepsilon,\delta<1/2\), the sampling algorithm produces an input-independent representation of a random linear map \(A:\mathbb R^d\to\mathbb R^k\), where
\[
1\le k\le\min\{d,\lceil C_1\varepsilon^{-2}\log_2(1/\delta)\rceil\}.
\]
For every fixed \(x\in\mathbb R^d\), its distribution satisfies
\[
\Pr_A\bigl[(1-\varepsilon)\|x\|_2\le\|Ax\|_2
                 \le(1+\varepsilon)\|x\|_2\bigr]\ge1-\delta.
\]
Given a sampled representation and the list of the \(s\) nonzero coordinates of any \(x\), the application algorithm must return all coordinates of \(Ax\) in at most
\[
C_2(s+k)\bigl(\log_2(d+2)\bigr)^q
\]
operations in the arithmetic model below, for every sampled representation and input. The same constants and algorithms must work for all parameters. The matrix distribution is independent of \(x\), including its support.''',
 definitions=r'''The Euclidean norm is \(\|x\|_2=(\sum_{i=1}^d x_i^2)^{1/2}\), and \(s=\|x\|_0=|\{i:x_i\ne0\}|\) is input sparsity. The input is an arbitrary-order list of distinct indices in \(\{1,\ldots,d\}\) and their nonzero real values, together with \(d\). Coordinates absent from the list are zero. Reading this list and writing the dense length-\(k\) output count toward application time. The zero vector is included, with \(s=0\).

A sampled object represents one genuine linear map on all of \(\mathbb R^d\), not a map chosen after seeing the support or magnitudes of the input. The application algorithm must evaluate that map exactly in real arithmetic. The approximation concerns preservation of length, not numerical evaluation of the matrix product. The probability statement is for each vector fixed independently of the sampled map; it does not claim that one dimension-reducing map preserves every vector simultaneously. No promise bounds the ratio of the largest coordinate to the norm.

Use an arithmetic RAM: a real value occupies one cell, and addition, subtraction, multiplication, division by a nonzero value, square root of a nonnegative value, and comparison each cost one operation. Memory access and operations on integer indices of logarithmic size in the allocated storage also cost one. There is no floor operation on arbitrary real values, arbitrary real-to-integer decoding, or oracle for matrix-vector multiplication. The programs are finite and uniform, with rational built-in constants; \(\varepsilon,\delta\) are real parameter inputs. This is an arithmetic-operation question, not a bound on the bit complexity of arbitrarily precise real coordinates.

The distribution and its representation may be prepared before the input vector is provided. To fix the construction convention, the sampler uses independent fair bits, has expected time and storage bounded by a fixed polynomial in \(d+\varepsilon^{-1}+\lceil\log_2(1/\delta)\rceil\), and terminates with probability one. It outputs a finite read-only representation used by the application algorithm. Setup work is independent of the input vector and is not included in per-vector application time; any subsequent work on the vector, including an input-dependent transformation or preprocessing, is included. Application time is a worst-case bound, not an amortized bound over a favorable collection of vectors. All sampler outcomes with positive probability must define an evaluable map. No logarithmic bound on the number of random bits is requested.

The output dimension \(k\) is selected from the parameters and is fixed before drawing the map. The ceiling handles integer dimensions, and the cap at \(d\) allows the identity when the usual dimension bound would exceed the ambient dimension. The phrase optimal dimension refers to the order of the displayed upper bound, not its best leading constant. The exponent \(q\) and time constant are independent of error and failure probability. In particular, an extra factor depending on \(\varepsilon^{-1}\) or \(\log(1/\delta)\) cannot be hidden in the input-sparsity term unless it is absorbed by the displayed bound.

The source has a separate question about generating the map with \(O(\log(d/\delta))\) random bits. The user explicitly removed that additional objective. The setup convention above makes the retained application question precise without reinstating the short-seed target.''',
 answer_criterion=r'''Supply a complete Lean-checked proof or refutation of the uniform existence assertion, including the distribution, dimension bound, pointwise probability guarantee and worst-case sparse-input application bound in the stated model. An affirmative answer must cover every parameter choice and arbitrary real input vector; a result only for constant distortion, constant failure probability, dense inputs, or special coordinate distributions is insufficient. A negative answer is the full negation and must cover every allowed construction and application algorithm, rather than one chosen sparse-matrix family. A proof about the omitted seed-length objective does not answer this card. The benchmark's numerical-value tolerance does not weaken the prescribed asymptotic guarantees.''',
 references=refs,
 target_revision=dict(date='2026-09-16',previous_formal=old['formal'],
     authorization='User explicitly chose sparse-vector application at optimal JL dimension and removed the separate seed-length objective.',
     scope='Pointwise oblivious norm preservation, application time (s+k)polylog(d); construction/application cost conventions are explicit.'),
 source_formulation=dict(text='The source asks for a distribution of norm-preserving linear maps with the usual Johnson–Lindenstrauss dimension bound, whose product with a sparse input can be evaluated in time proportional to input sparsity plus output dimension, apart from logarithms of the ambient dimension.',
     caption='Editorial paraphrase of the application-time question',citation='bertinoro2011',format='editorial_paraphrase'),
 category_assignment=dict(method='editorial_topic',reason='Fast Euclidean dimension reduction with optimal output dimension; the separate seed-length objective was removed by user choice.'),
 context_blocks=[
     block('Dimension reduction can shorten later computations on high-dimensional data while approximately preserving distances. For sparse data, even scanning every ambient coordinate may waste most of the work. This question seeks a transformation whose application cost follows the amount of input actually present and the amount of output produced.','bertinoro2011'),
     block(r'Sparse Johnson–Lindenstrauss matrices reduce multiplication work by limiting nonzeros per column. Their standard application bound still multiplies input sparsity by a factor of order \(\varepsilon^{-1}\log(1/\delta)\). The existence of such matrices therefore does not establish the requested additive dependence on input sparsity and output dimension.','sparse2014'),
     block('Fast structured transforms use a different route to rapid multiplication. The inspected 2023 improvement retains an ambient-dimension term, which can dominate when the input is sparse. Lower bounds on column sparsity alone do not rule out a different structured map with a faster evaluation algorithm.','fast2023'),
     block('Later sparse-embedding work refines parameter regimes, while the 2026 concentration result targets sharper confidence constants. These developments concern the same geometric primitive, but neither inspected statement supplies the full application-time bound selected here.','revisited2023'),
 ],
 why='An affirmative answer would make optimal Euclidean dimension reduction almost as cheap as reading a sparse vector and writing its sketch. This would strengthen a general primitive used in similarity search, randomized linear algebra and high-dimensional geometry. A general obstruction would identify a computational cost that dimension bounds alone do not reveal.',
 progress=[
     progress('2011','The workshop list poses fast sparse-vector application and short random seeds as separate questions.','bertinoro2011'),
     progress('2014','Sparse transforms achieve the optimal dimension order with an additional inverse-distortion factor in direct sparse-vector multiplication.','sparse2014'),
     progress('2023','Fast-transform and sparse-embedding analyses improve different parameter regimes without supplying the complete selected guarantee.','fast2023'),
     progress('2026-06-20','A concentration refinement for sparse projections was published; its theorem does not assert the requested application-time bound.','confidence2026'),
     progress('2026-09-16','The source and later theorem scopes were checked, and the approved removal of the seed-length objective was recorded.','bertinoro2011'),
 ],
),notes,sources,status,summary=[
 'A Johnson–Lindenstrauss map reduces dimension while approximately preserving the length of each fixed vector with high probability.',
 'The question asks for the optimal output dimension together with application time proportional to input sparsity plus output length, up to logarithms of the ambient dimension.',
 'The map is chosen independently of the input, and the guarantee must hold for all distortion and failure-probability parameters.',
 'Known sparse and fast structured transforms do not by themselves provide this full combination, and the separate short-seed objective has been removed.',
 'A resolution would clarify whether geometric compression can be performed almost at the cost of reading and writing sparse data.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
