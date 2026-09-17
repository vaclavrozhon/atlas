# TCS-6692: selected quantitative PRG target

The user selected Vadhan Open Problem 7.13: linear seed in the underlying
OWF input length, retaining distinguishing security s*(epsilon/m)^O(1).
This is not the consolidated 2024 black-box seed-exponent question.
The card remains claimed and pending; no completion has been applied.

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
The complete regular-function 2024 Journal of Cryptology paper has NOT
yet been read: https://link.springer.com/article/10.1007/s00145-024-09507-4.
Search found no general quantitative linear-seed resolution but coverage
needs further focused primary checks before completion.

A new asynchronous secondary scope question was sent: may G depend on
the target parameters s and epsilon, or must one G for f,m satisfy the
whole security curve simultaneously? The former is recommended and closer
to the pointwise (t,epsilon) construction request; no answer yet. The
original selected target is retained regardless. The question and state
are persisted in further-scope-choices.json.

When formalizing, still resolve input representation and full explicitness:
f is efficiently evaluable and length preserving; its description may be
used without imposing a black-box construction restriction. Count the full
description and precision of security/error parameters. Do not replace
polynomial output-time by polynomial 1/epsilon-time without explanation,
and do not require stretch for impossible output lengths below the allowed
linear seed threshold. Do not add the stronger simultaneous-parameter
condition without the user's selection.
