# Selected source checks

The review uses saved questions, source context and the intermediate explanations.
Where a label concealed the actual model, the fuller saved source extraction or
the primary publication was consulted. This is a category review, not a search
for subsequent solutions.

Root checks supplement the source evidence recorded in each agent's review files:

- TCS-0958: [original problem 62](https://sublinear.info/62) specifies a random
  Gaussian input for the rank-one SDP question.
- TCS-0947: [original problem 93](https://sublinear.info/93) explicitly targets
  the local differential privacy model and its lower bounds.
- TCS-0965: [original problem 59](https://sublinear.info/59) asks for an injective
  edit-to-Hamming map with low expansion, including optional efficient decoding.
- TCS-0987: [original problem 21](https://sublinear.info/21) separates its explicit
  RIP-construction questions from related fast Fourier-matrix operations.
- TCS-0453: [original sparse-matrix problem](https://notes.0xparc.org/problems/sparse-matrix-lpn/)
  states column sparsity and minimum nonzero kernel weight before giving LPN as
  motivation.
- TCS-0050–0053 and TCS-0047: [Dagstuhl seminar 15242](https://doi.org/10.4230/DagRep.5.6.28),
  sections 5.1–5.7. In particular, the sign-representation domain is the Boolean
  cube encoded by values 1 and 2; this is a Boolean representation question.
- TCS-0054: [the original tensor-decomposition problem](https://proceedings.mlr.press/v35/bhaskara14b.html)
  concerns algorithmic recovery up to the uniqueness threshold.
- TCS-1877: [white-box learning paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.73)
  defines a learner given the code of a noisy sampler and connects its hardness
  to public-key encryption; the two category interpretations were compared.
- TCS-4039: [bottleneck-complexity paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2018.24)
  explicitly distinguishes the underlying communication model without security
  from the compiler that adds secure computation.

Detailed notes on recovered passages and cautious retained placements also appear
in the `borderline` and `evidence` fields of `*-review-*.json`.

- TCS-5341: [primary PDF, page 2, footnote 2](https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.84/LIPIcs.ITCS.2022.84.pdf#page=2) explicitly asks about HSG-to-PRG conversion. The source title explains why the earlier summary incorrectly described an errorless-procedure target; the corrected summary keeps the actual conversion question.
