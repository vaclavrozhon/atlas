# TCS-0708 scope review, 18 September 2026

The card remains pending. Read Vakili's COLT 2024 open-problem paper in full:
Sections 2–4 define episodic regret and ask both for no regret and for optimal
rates, under a pointwise RKHS bound on transition probabilities. A domain,
reference measure for continuous transition densities, kernel class, complexity
parameters and precise uniform rate still need selection. Merely saying all
kernels does not supply the regularity needed for a meaningful universal rate.

The first optional recommendation in this review was a finite-state/action
specialization with the whole rational Gram matrix and rewards known, and no
computation limit. On further examination this is not a reliable open target.
For fixed finite horizon and episode count, there are finitely many observation
histories. Behavioral policies are finitely many real probability vectors;
transition feasibility, finite-kernel RKHS norm bounds and expected performance
have descriptions by polynomial equalities and inequalities. Real quantifier
elimination can in principle describe the minimax value. The recommendation
was therefore corrected in a second optional question: preserve the broader
source question as needing specification, or deliberately archive that finite
computational target. No answer has yet been received. This observation is a
scope warning, not an independent formal proof audit or a resolved disposition.

Relevant primary sources checked:

- Sattar Vakili, *Open Problem: Order Optimal Regret Bounds for Kernel-Based
  Reinforcement Learning*, COLT 2024, §§2–5, PDF pp.1–4:
  https://proceedings.mlr.press/v247/vakili24a/vakili24a.pdf
- Sattar Vakili and Julia Olkhovskaya, *Kernelized Reinforcement Learning with
  Order Optimal Regret Bounds*, NeurIPS 2023, arXiv:2306.07745v2:
  introduction, §2.3 Assumption 1 and §3 domain-partition scope. Its particular
  spectral and domain assumptions must be checked before importing a resolution
  of the broader 2024 question.
- Jasmine Bayrooti, Sattar Vakili, Amanda Prorok and Carl Henrik Ek,
  *No-Regret Thompson Sampling for Finite-Horizon Markov Decision Processes
  with Gaussian Processes*, NeurIPS 2025, arXiv:2510.20725:
  §3 Assumption 1 places a joint Gaussian-process model on reward and transition
  functions. That is not merely the fixed pointwise RKHS transition-probability
  assumption in the 2024 source. No equivalence or general resolution is claimed.

All three PDFs and extracted texts are in this review's source cache. The
original card has not been replaced by an invented finite-domain open theorem.

Update, 18 September 2026: the user answered both scope questions, selecting
the finite full-kernel model and then explicitly selecting archival of that
known computational target. The finite variant is now specified and archived
by `complete_finite_kernel_regret.py`. The source-level infinite-domain question
is not claimed resolved. The reduction uses compact transition and behavioral
policy sets, finite trajectory polynomials, Bellman maxima and effective real
quantifier elimination; exact zero testing handles multiplicative approximation
at zero. Basu's survey §2.1 and Theorem 2.1 were read as the primary background
for this editorial application of the standard theorem. No Lean proof was
constructed or independently audited in this review.
