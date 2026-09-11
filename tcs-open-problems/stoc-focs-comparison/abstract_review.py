"""Record decisions made after inspecting the cited publisher abstracts."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parent
DATA='''
FOCS-2021-085|online|Smoothed guarantees against adaptive adversaries for online learning, discrepancy and optimization.
FOCS-2021-095|general|Generalized comparison sorting; graph representation is a constraint on comparisons.
FOCS-2022-066|dist|Main contribution is constant-round correlation clustering in MPC and LOCAL models.
FOCS-2022-073|general|Dynamic balls-into-bins load balancing, not allocation among strategic agents.
FOCS-2022-109|comm|Round/communication lower bounds in the shared-blackboard model.
FOCS-2023-028|crypto|Characterization of secure key agreement using interactive Kolmogorov complexity.
FOCS-2023-085|stream|Space lower bound for approximately counting the length of a stream.
FOCS-2023-138|dist|Round complexity of secure graph algorithms in CONGEST.
FOCS-2024-011|comp|Robust simulation of Turing machines by smooth dynamical systems and decidability of halting.
FOCS-2024-039|general|Instance-optimal sampling in the external-memory I/O model, with sequential estimation applications.
FOCS-2024-040|general|Comparison sorting of pattern-avoiding permutations.
FOCS-2024-048|proof|A one-query linear PCP construction, with succinct-argument applications.
FOCS-2024-122|general|Sorting in an evolving-data model.
FOCS-2024-123|general|Sorting under partial information with matching query and time bounds.
FOCS-2025-004|sched|Online single-machine flow-time scheduling under partial clairvoyance.
FOCS-2025-037|online|Competitive analysis of oblivious/query-commit bipartite matching.
FOCS-2025-043|comb|Structure of Boolean matrices with bounded factorization norm and extremal MaxCut.
FOCS-2025-116|prg|Generating unpredictable permutations with restricted memory.
STOC-2022-006|general|Balls-into-bins load balancing on a graph, not economic allocation.
STOC-2022-054|alg|Uniform guarantees for randomized Hadamard transforms and random projection methods.
STOC-2022-055|avg|Statistical distinguishability thresholds for random geometric and Erdos-Renyi graphs.
STOC-2022-078|cx|Tight circuit complexity of pseudorandom functions and a natural-proofs barrier.
STOC-2022-133|general|General transformations and lower bounds for adaptive dynamic algorithms; graph problems are applications.
STOC-2023-119|code|Local list recovery of linear maps beyond the standard Goldreich-Levin regime.
STOC-2023-122|general|Tight query bounds for noisy comparison sorting and binary search.
STOC-2024-035|comb|Anti-concentration and least singular-value bounds for structured random matrices.
STOC-2024-079|geom|Complexity of equality cases in the Alexandrov-Fenchel inequality for convex polytopes.
STOC-2025-028|fg|Reductions establish a common fine-grained hardness hierarchy across word-RAM problems.
STOC-2025-102|alg|Primality of polynomial ideals, not testing primality of integers.
STOC-2025-143|learn|Interactive agreement on predictions using tractable calibration conditions.
STOC-2025-150|csp|Characterization of CSP sparsification via non-redundancy and chain length.
STOC-2025-152|crypto|Adaptive robustness, ideal security and CCA security of pseudorandom codes.
STOC-2025-156|learn|Classical robust Gaussian mean estimation with unknown heterogeneous covariances.
STOC-2025-177|crypto|Hardness reductions for sparse LWE and LPN, with cryptographic applications.
STOC-2026-014|alg|S-unit equations over finitely presented modules and computational algebra applications.
STOC-2026-016|crypto|Compressed permutation oracle for quantum security proofs of Feistel and related constructions.
STOC-2026-032|comp|Decidability of zero occurrence in linear recurrences over positive-characteristic rings.
STOC-2026-053|avg|Optimal worst-case to average-case reductions for linear problems.
STOC-2026-059|code|Local equivalence and explicit construction of subspace-designable codes.
STOC-2026-123|proof|A bounded arithmetic theory formalizing probabilistic polynomial-time reasoning.
STOC-2026-129|temp|Simultaneous embeddability of temporal sequences of graphs.
STOC-2026-175|cx|Sparsity of polynomial representations of Boolean functions and communication applications.
STOC-2026-210|online|Online algorithms for combinatorial Markov search, generalizing Pandora's box.
'''
out={}
for row in DATA.strip().splitlines():
    id,area,note=row.split('|',2)
    out[id]=dict(area=area,method='LLM_reviewed_abstract',note=note)
assert set(out)==set(json.loads((BASE/'abstract_review_ids.json').read_text()))
(BASE/'abstract_overrides.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
