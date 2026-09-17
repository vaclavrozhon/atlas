# TCS-7352: known arbitrary-precision computation

Scope choice pending, 17 September 2026. The active record is reserved and
has not been counted as completed.

The current card permits an unambiguous mathematical expression for an
approximation with absolute error at most 1/100, with no running-time bound.
The gap between recently printed lower and upper numbers is not enough to
establish that this target remains scientifically open.

Raghavendra and Steurer, *Towards Computing the Grothendieck Constant*,
SODA 2009, pp. 525–534, DOI 10.1137/1.9781611973068.58:

- Theorem 1.3, author PDF p. 2, explicitly states computation to arbitrary
  additive error eta in time exp(exp(O(1/eta^3))).
- Section 3.6, author PDF p. 7, replaces the unbounded matrix search by a
  bounded-dimensional optimization and a finite linear program obtained
  from a net. The net size and dimension depend only on the error.
- The nearby UGC assumption belongs to the hardness result, Theorem 1.1,
  and is not a hypothesis of Theorem 1.3.
- The source's finite program optimizes the reciprocal comparison factor;
  its normalization, discretization error and inversion must be included
  in any eventual complete Lean formalization.
- Sections 3.1–3.3 give the conversion and approximation prerequisites.
  These passages and the computation proof outline were read. The full
  analytic proof and all discretization constants have not been
  independently reconstructed, and no numerical LP has been evaluated.

Primary author-hosted PDF:
https://www.dsteurer.org/paper/grothendieck.pdf
The downloaded canonical redirect is hosted at:
https://www.bayesianestimation.org/paper/grothendieck.pdf
The author publication list confirms SODA 2009.
The publisher's December 2013 online date is not the conference year.

The 2026 bound source is arXiv:2608.11158v2, 12 August 2026, by Saha,
Li, Xue, Chaudhuri, Klivans, Kothari and Meka. Its introduction uses the
more quantitative upper improvement 3.47e-4; its abstract uses the weaker
1e-4. Together with the stated lower bound 6*pi/11, neither displayed
interval has width at most 1/50. These are preprint claims, not results
independently verified in this review.

The older reference needs its venue corrected from STOC 2011 to FOCS 2011.
The inspected preprint is arXiv:1103.6161v3, 17 August 2011; the eventual
Forum of Mathematics, Pi article appeared in 2013.

The user was asked whether to archive the known unrestricted-accuracy task
or explicitly retain it as a Lean formalization task, as was separately
authorized for TCS-6607. No response has yet been received. Do not silently
replace the 1/100 criterion by an exact-value or computational-efficiency
target.
