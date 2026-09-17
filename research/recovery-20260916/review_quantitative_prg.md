# TCS-6692: selected quantitative PRG target

The user selected Vadhan Open Problem 7.13: linear seed in the underlying
OWF input length, retaining distinguishing security s*(epsilon/m)^O(1).
This is not the consolidated 2024 black-box seed-exponent question.
The user’s parameter-dependence choice has been applied and the card was
completed on 17 September 2026 by complete_quantitative_prg.py.

Read published Vadhan 2012 PDF, definitions 7.1, 7.3, 7.7, 7.9 and 7.10,
Theorem 7.11 and discussion pp. 220–222, Open Problem 7.13 p. 222.
PDF p. 225 was rendered and visually inspected on 17 September 2026.
Source cache: sources/third-20260915/vadhan-published2012.pdf/.txt.

Key exact conventions:

- Nonuniform time means Boolean circuit size, counting AND and OR gates
  but not inputs and negations. Definition 7.1 explicitly fixes this.
- A PRG has strict stretch d<m (Definition 7.3).
- Fully explicit means polynomial time in output length m (Definition 7.7).
- One-wayness in Definition 7.10 is against nonuniform algorithms. The
  quantitative preceding discussion uses inversion probability 1/2 and
  a reduction costing t*(m/epsilon)^O(1).
- The problem statement literally includes an otherwise unused phrase
  "and a constant c". This is present in the rendered source, not an OCR
  error. Do not silently assign it an unsupported mathematical role.
- The seed bound O(ell) is quantitative, not just an asymptotic PRG
  existence consequence from arbitrary OWFs.

Read the 2024 Luca memorial column pp. 8–10, authored section on PRGs
and OWFs, Open Problems 1–2. It discusses separate black-box query and
seed exponents, with then-known exponent interval [1,3]. Regular OWF
constructions have additional structural assumptions. Cache luca2024.txt.
The publisher's full HTML introduction, comparison table and §1.1 of the
2024 Journal of Cryptology article were subsequently read. Its nonadaptive
construction has quadratic seed and a regularity assumption. The local ePrint
PDF request returned HTTP 403; no unread local theorem is claimed.

The user explicitly selected a construction allowed to depend on s and epsilon.
The final finite-input formulation uses a supplied circuit of size ell^b for
any fixed exponent b, one uniform compiler for that exponent, linear seed,
and time polynomial in the output length. Construction constants may depend
on b, but not the particular circuit or target parameters. Security is against
nonuniform circuits, with inversion success at most one half and distinguishing
size floor(s / (K*(m/epsilon)^q)). The output length exceeds the linear seed
threshold. Dyadic errors and s <= 2^(2*ell) cover the positive-time asymptotic
regime; outside that hardness range an inverse-selection lookup circuit exists.
The model does not impose a black-box restriction or the stronger requirement
that one generator satisfy all parameter pairs simultaneously.

Also read the primary ECCC abstract and revision history of Mazor–Pass,
Counting Unpredictable Bits, TR23-143 revision 3 of 17 July 2024. It reports
logarithmic-factor efficiency improvements, not the selected linear-seed
quantitative result. Bounded primary checks through 17 September 2026 found
no verified resolution. These status checks do not certify all cited proofs.
