# Learning consolidation and edit-distance addition

Reviewed on 11 September 2026. The user approved correcting the mislabelled
junta entry, consolidating its source milestone into the existing junta card,
developing the general DNF problem and considering it for the Learning theory
focus prefix. The user also explicitly requested the near-exact edit-distance
question and approved retaining both accuracy–runtime variants.

## Decisions

- **TCS-0023 → TCS-6543:** the March 27, 2018 Wigderson draft defines F_k as
  Boolean functions depending on at most k coordinates immediately before
  Open Problem 17.9 (PDF pp. 232–233). The inherited title about growing-size
  DNF was incorrect. The canonical junta statement and resolution criterion
  remain unchanged. Its context now preserves the source's weaker challenge
  of polynomial-time progress for growing support and its conditional-hardness
  option. These are not asserted to be equivalent to the full
  poly(n,2^k,1/ε) learner. The old ID, bibliography and legacy record remain
  available as a reviewed, retired pointer with a canonical-card link.
- **TCS-5358:** the introduction of Feldman's 2012 paper asks about general
  distribution-free PAC learning of DNF. This source pointer is upgraded in
  place to a full card. Its original quotation and bibliography remain in
  `upgraded_from`. The card requires an improper learner from independent
  labelled examples, without membership queries, with polynomial dependence
  on n, the number of terms, inverse accuracy and log inverse failure
  probability. Its reduction to uniform-example junta learning is documented.
- **Learning focus:** select TCS-5358 as the fourth focus question, replacing
  the two-halfspace problem TCS-6544. Preserve the other four choices, including
  the information-complexity question. The generality and longstanding role of
  DNF motivate this editorial choice; the narrower geometric question remains
  an active candidate. The DNF importance score is 97.
- **New edit-distance card:** use the stable authoring key
  `edit-distance-approximation-scheme-truly-subquadratic`; publication assigned
  persistent ID TCS-7220. For every fixed positive ε, require a randomized
  (1+ε)-estimate on every pair in O(n^(2−δ_ε)) time for some fixed δ_ε>0.
  The word-RAM, integer-alphabet and unit-cost conventions match TCS-6624.
  The new question has importance 96 and follows the existing two focus choices.
  TCS-6624 keeps its constant-factor O(n polylog n) target. Neither stated
  algorithmic guarantee alone implies the other.

## Source checks

- [Wigderson, March 2018 draft](https://www.math.ias.edu/files/mathandcomp.pdf):
  downloaded again; PDF page 233 contains Open Problem 17.9. The local source
  library also holds an August 2019 draft with the same numbered junta problem.
  The newly downloaded 2018 PDF and extracted text are saved in this directory.
- [Feldman 2012](https://proceedings.mlr.press/v23/feldman12b.html):
  checked the publisher page and the previously saved full introduction in
  `research/extractions/PMLR.v23.feldman12b.json`. The general problem is
  distinct from the paper's positive uniform/product-distribution results.
- [Servedio's 2025 PAC survey](https://arxiv.org/html/2511.08791v1):
  checked the model discussion, Theorems 2, 8 and 13, and the improper-learning
  hardness discussion. It retains the general polynomial-time DNF goal.
- [Daniely–Shalev-Shwartz 2016](https://proceedings.mlr.press/v49/daniely16.html)
  and [Daniely–Vardi 2021](https://proceedings.mlr.press/v134/daniely21a.html):
  checked primary abstracts for the required random-SAT and local-PRG
  assumptions. These support conditional evidence only.
- [Iterative Chow Filtering, May 2026](https://arxiv.org/abs/2605.17251):
  checked the abstract. Its quasipolynomial uniform-distribution PQ result
  does not resolve the general DNF card.
- [Rubinstein's 2018 question](https://theorydish.blog/2018/07/20/approximating-edit-distance/):
  Open question 2 explicitly asks for near-exact truly subquadratic
  approximation, separately from the updated constant-factor question.
- [Mao–Rubinstein 2026](https://arxiv.org/html/2603.29702v1):
  checked the introduction, comparison table and Theorem 6.1. The
  quasipolynomial savings over quadratic time do not establish a fixed
  positive saving in the exponent.
- [Andoni–Nosatzki](https://arxiv.org/abs/2005.07678) and
  [Backurs–Indyk](https://arxiv.org/abs/1412.0348): checked the primary
  statements to keep the constant-factor and exact-hardness regimes distinct.

The status review checks statements and model boundaries, not the full proofs
of the cited papers. The mathematical formulations, significance assessments
and consolidation decisions are authored independently. The pre-change target
records and focus selection are retained in `before.json` and
`selection-before.json`; validation results are recorded separately.
