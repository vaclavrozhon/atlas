Independent audit of TCS-0184 — 16 September 2026

The proposed target is faithful to Dagstuhl Problem (5.2), once the convention is made explicit: the input integer polymatroid is an exact, unscaled entropy function in bits; the output matroid rank is a positive scalar multiple of one exact finite-alphabet entropy function. There is one common scalar for all subsets. No verified resolution or counterexample to this target was found in the bounded review. The inspected newer results do not justify archival as resolved.

The original Problem (5.2) is on printed p. 201/PDF p. 22 of the actual 25-page report, not at the inherited collection-PDF pointer. It says a k/m approximation is a restriction of the free expansion of m times g retaining at least k/m of every block. Printed p. 199/PDF p. 20, Problem (2.3), explicitly distinguishes finite-support entropy from countably supported entropy. The seminar took place in July 2022, while the publisher records publication on 3 February 2023. Preserve the problem year as seminar provenance and give the publication date accurately.

Source: [Dagstuhl report](https://doi.org/10.4230/DagRep.12.7.180).

Scaling and finite support

Kühne–Yashfe, arXiv:2206.03465v3, 25 July 2025, Section 2.2 p. 7, fixes logarithm base 2. Definition 2.3 and the paragraph immediately following it, p. 8, explicitly distinguish:

- an entropic matroid, whose rank satisfies r(S) = lambda H(X_S) for all S with one real lambda > 0;
- an entropic polymatroid, whose rank is H(X_S) without that scalar.

The report does not spell out a logarithm base in the question itself. Taking bits is an explicit conventional completion supported by the same author's later precise definition; do not claim that arbitrary changes of base preserve the integer-input promise without explanation.

Locator correction: in this cached v3, the finite-support statement is **Theorem 4.4 on p. 20**, not Lemma 4.2. Definition 4.2 is the probability-space representation definition on pp. 19–20. Theorem 4.4 is stated for connected matroids of rank at least two; it forces the representing variables to be uniform and finitely supported. Its source statement should not be cited as directly covering every disconnected matroid.

For the existential finite-support convention needed here, the extension to arbitrary finite matroids is sound. Restrict an existing scaled entropy representation to each connected component. In every component of rank at least two, Theorem 4.4 makes each singleton uniform with entropy 1/lambda, so its support size is the same integer q = 2^(1/lambda). There are finitely many variables, hence finite joint support. Replace each rank-one component by a shared uniform q-symbol variable and each loop by a constant, and take the component representations independently. Additivity realizes the whole rank with the original common lambda. If there is no rank-at-least-two component, independent shared binary variables for the rank-one components and constants for loops suffice, with lambda = 1. Thus requiring existence of a finite-support output does not exclude any matroid admitted by the discrete proportional-entropy definition. This reduction is an elementary audit argument, not a claimed Lean formalization.

The current institutional bibliography lists the journal version as Duke Mathematical Journal 175(8), 1363–1451, June 2026, DOI 10.1215/00127094-2025-0047. The inspected file remains the 61-page arXiv v3; retain its locators and do not imply the journal PDF was read.

Sources: [checked arXiv edition](https://arxiv.org/abs/2206.03465v3), [author institution publication record](https://cris.huji.ac.il/en/publications/on-entropic-and-almost-multilinear-representability-of-matroids/).

Free expansion and quantifiers

The proposed formula

r_m(A) = min over S subset [n] of (m g(S) + |A minus union of X_i for i in S|)

with pairwise disjoint blocks of size m g({i}) matches Definition 5, pp. 6–7, of Chen–Yeung, arXiv:1407.7405v2, 28 September 2016. This source expressly allows zero-size blocks. Taking T as an actual subset of the expansion ground set and retaining the restricted rank on every A subset T is correct. The retention requirement is exactly |T intersect X_i| >= k g({i}), since the original block has m g({i}) elements.

Allow 1 <= k <= m and k/m > 1-epsilon for every positive real epsilon, with m,k,T,lambda and the output distribution depending on g and epsilon. Ratio 1 is allowed; no reduced-fraction requirement is needed. There is no uniform upper bound or computable selection requirement on m, alphabet sizes, scalar, probability values or witness distribution. Input distributions likewise need not be uniform or rational. The zero polymatroid and empty blocks are harmless. Arbitrary finite alphabets and arbitrary real probabilities should remain available in the exact entropy predicates.

Its Proposition 6 on p. 7 concerns **almost-entropic** membership: I rendered and visually inspected the PDF and confirmed closure bars on both entropy regions. The bars disappear from plain text extraction. It therefore does not already solve the exact-output question.

Source: [checked 2016 edition](https://arxiv.org/abs/1407.7405v2).

Why the 2024 strict characteristic-set example is not a counterexample

Chen–Cheng–Bai, arXiv:2306.17041v3, 30 January 2024, Section V.A, Definition 11, Example 10 and Question 1, all on PDF p. 11, distinguish the characteristic set of an integer polymatroid from that of its free expansion at a fixed alphabet size. Example 10 has a binary-entropic integer polymatroid whose free expansion is U_(2,5), which is not binary-entropic.

This example does not defeat arbitrary output scaling. The same U_(2,5) is represented by the five points of the projective line over the four-element field. Applying those linear forms to a uniform pair of field elements gives H(Y_A) = 2 r(A) in bits, so lambda = 1/2 realizes its rank. Thus this particular example has a full retained entropic expansion with m = k = 1. This is only a scope check on the supposed counterexample, not an argument for the universal target.

The free-expansion minimum in the 2024 text appears to have a domain typo; use the unambiguous 2016 definition, with S ranging over the original polymatroid ground set.

Source: [checked 2024 edition](https://arxiv.org/abs/2306.17041v3).

Later primary checks

- Geva Yashfe, **On the recognition problem for limits of entropy functions**, arXiv:2509.06302v1, 8 September 2025: actual PDF abstract and Theorem 1, p. 1, plus finite-entropy and almost-entropy definitions in Section 2.2. This proves undecidability of membership in the closure, even for integer vectors/matroids. It neither supplies the requested restrictions nor rules out their existence for exact entropic inputs. An undecidability conclusion is not a negation of this nonalgorithmic existence question.
- Guillermo Matera, **Entropy approximations of algebraic matroids over finite fields**, arXiv:2509.15348v1, 18 September 2025: actual PDF abstract p. 1, Theorem 1.1 p. 2, and the normalized-entropy construction in Section 4. It approximates an algebraic matroid by entropy polymatroids, with normalized entropy H/log(q); the direction and exactness differ from this problem. It does not produce exact entropic restrictions of free expansions of arbitrary exact entropic integer polymatroids. No full proof check of its quantitative estimate is claimed.
- Mohammad Hossein Kalantari and Shahram Khazaei, **Four-Entropic Matroids Are Quaternary**, arXiv:2608.20553v2, 3 September 2026 (v1 20 August): actual PDF abstract p. 1 and Theorem 1.1 p. 2. The preprint claims equivalence of four-symbol entropic representation and representability over the four-element field. This fixes q=4; the problem here permits arbitrary finite alphabets and a variable common scale. The statement does not settle the target. The proof was not audited.
- Shahram Khazaei, **Folded-Algebraic Matroids: Characteristic Rigidity and Almost-Entropic Separation**, arXiv:2609.01664v1, 31 August 2026: actual PDF abstract pp. 1–2, Theorem 1.1 p. 3, Theorem 1.2 p. 4, and Definition 2.6/Theorem 2.7 p. 8. The claimed separation is almost-entropic versus folded-algebraic representation. Exact entropic output and the free-expansion retention condition are not its conclusion. The proof was not audited.
- Kaizhe He and Qi Chen, **Entropy Functions on Two-Dimensional Faces of Polymatroid Region Spanned by a Matroid and a Rank-One Matroid**, arXiv:2602.03363v2, 6 June 2026 (v1 3 February): actual PDF abstract p. 1 and classification statements Theorems 16–17 near the end. This concerns entropy on specified two-dimensional faces; it does not establish the universal approximation assertion or its negation. The proof was not audited.

Sources: [recognition](https://arxiv.org/abs/2509.06302v1), [algebraic approximation](https://arxiv.org/abs/2509.15348v1), [four-symbol result](https://arxiv.org/abs/2608.20553v2), [folded-algebraic result](https://arxiv.org/abs/2609.01664v1), [face classification](https://arxiv.org/abs/2602.03363v2).

Bounded verdict: keep the original target with qualified open status. None of the inspected papers gives a verified solution. The review checks exact definitions, source scope and a simple alleged-counterexample calculation; it is not exhaustive and does not independently verify the cited general proofs. No canonical card, queue, selection, completion or publication was modified. Existing assessed importance 74 and category should remain unchanged.


Cached PDF manifest

```json
[
  {
    "path": "research/random-card-review-20260914/sources/entropic-matroid-algebraic2025.pdf",
    "bytes": 419431,
    "sha256": "98b5bf6f20914f9a4aeb22adfb48751979cfe25f1fa4f5c321732a3b11e37bb0"
  },
  {
    "path": "research/random-card-review-20260914/sources/entropic-matroid-chen2024.pdf",
    "bytes": 1179523,
    "sha256": "0cc3349b1ca4ce6f7728f080a5a6c0684f2ed3b316cf7ca555867a7d3d404fd2"
  },
  {
    "path": "research/random-card-review-20260914/sources/entropic-matroid-dagstuhl2022.pdf",
    "bytes": 2225959,
    "sha256": "6f5e8518f011f3f96b8070343057e29835dd813661502d909a784199ab7d182a"
  },
  {
    "path": "research/random-card-review-20260914/sources/entropic-matroid-faces2026.pdf",
    "bytes": 342506,
    "sha256": "478f2df9d58b7be082a517aae7e631104082bb45ac0f0c9dbe382be254185915"
  },
  {
    "path": "research/random-card-review-20260914/sources/entropic-matroid-folded2026.pdf",
    "bytes": 526705,
    "sha256": "d4905fa886a52a89e60cb659a8de53556b5d9037ac42eb3420369326ce321632"
  },
  {
    "path": "research/random-card-review-20260914/sources/entropic-matroid-four2026.pdf",
    "bytes": 427226,
    "sha256": "43e3dfbf8d3757b3fb6a3e03f6fbcd01bbf120d0b242117cec3985dc6499579d"
  },
  {
    "path": "research/random-card-review-20260914/sources/entropic-matroid-ky2025.pdf",
    "bytes": 740554,
    "sha256": "f2b074a599c64f9c40bb8b102d53f792ac6ddc92e13d8a3d7f063a7fd88a2016"
  },
  {
    "path": "research/random-card-review-20260914/sources/entropic-matroid-partition2016.pdf",
    "bytes": 377399,
    "sha256": "5d5d304c212882f8bb6c79033beaa98a62251a0b6f7b3c17b19fb2e3e750ea1a"
  },
  {
    "path": "research/random-card-review-20260914/sources/entropic-matroid-recognition2025.pdf",
    "bytes": 602149,
    "sha256": "079329f1c54faf86e1d743640adef11ebe5e942b97f483da0f7db57365c64740"
  }
]
```
