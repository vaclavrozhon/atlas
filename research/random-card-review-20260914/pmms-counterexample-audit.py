"""Independent finite audit of the first table in Gölz arXiv:2609.08954v1.

This exhausts complete allocations and all two-part partitions using integers.
It is a reproducible source check, not a Lean proof or a test of the website.
"""
from fractions import Fraction
from itertools import product
import hashlib
import json
from pathlib import Path

VALUES = (
    (143, 133, 137, 22, 20, 21, 29, 38, 2),
    (159, 140, 133, 15, 8, 1, 1, 35, 2),
    (135, 133, 134, 13, 11, 20, 28, 40, 2),
)
N, M = len(VALUES), len(VALUES[0])
assert all(len(row) == M and all(v > 0 for v in row) for row in VALUES)
UTILITY = [
    [sum(row[g] for g in range(M) if mask & (1 << g))
     for mask in range(1 << M)]
    for row in VALUES
]
BENCHMARK = []
for i in range(N):
    row = []
    for union in range(1 << M):
        candidate, best = union, 0
        while True:
            # Every submask occurs once; union ^ candidate is its complement.
            best = max(best, min(UTILITY[i][candidate],
                                 UTILITY[i][union ^ candidate]))
            if candidate == 0:
                break
            candidate = (candidate - 1) & union
        row.append(best)
    BENCHMARK.append(row)

count, feasible, best_ratio, best_assignment = 0, 0, Fraction(-1), None
witness_digest = hashlib.sha256()
for assignment in product(range(N), repeat=M):
    count += 1
    bundles = [sum(1 << g for g in range(M) if assignment[g] == i)
               for i in range(N)]
    assert sum(bundles) == (1 << M) - 1
    assert all((bundles[i] & bundles[j]) == 0
               for i in range(N) for j in range(i))
    violations, ratios = [], []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            own = UTILITY[i][bundles[i]]
            mm = BENCHMARK[i][bundles[i] | bundles[j]]
            if mm > 0:
                ratios.append(Fraction(own, mm))
            if own < mm:
                violations.append((i, j, own, mm))
    feasible += not violations
    if violations:
        witness_digest.update(json.dumps([assignment, violations[0]],
                                        separators=(",", ":")).encode() + b"\n")
    ratio = min(ratios)
    if ratio > best_ratio:
        best_ratio, best_assignment = ratio, assignment

assert count == 3 ** 9 == 19683
assert feasible == 0
assert best_ratio == Fraction(186, 187)
report = dict(
    source="https://arxiv.org/abs/2609.08954v1",
    source_locator="Section 2, first valuation table, PDF page 2",
    values=VALUES, agents=N, goods=M,
    complete_allocations_checked=count, pmms_allocations=feasible,
    best_pmms_ratio=str(best_ratio), attaining_assignment=best_assignment,
    violation_witness_sha256=witness_digest.hexdigest(),
    arithmetic="exact integer comparisons; exact fractions only for the ratio",
    scope="Independent exhaustive source audit; not a Lean formalization.",
)
target = Path(__file__).with_name("pmms-counterexample-audit.json")
target.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report))
