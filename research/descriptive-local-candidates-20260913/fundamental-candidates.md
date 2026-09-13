# Two structural candidates

Literature check: 13 September 2026. These recommendations respond to the
request for more fundamental questions. They concern general decomposition
and derandomization principles. No canonical cards were added.

## Weiss's amenable-action hyperfiniteness conjecture

Does every Borel action of a countable amenable group on a standard Borel
space have a hyperfinite orbit equivalence relation? Here hyperfinite means
that the orbit relation is the union of an increasing sequence of Borel
equivalence relations, each with finite classes. The action need not be free.

This is a central question about whether group amenability forces Borel
finite approximation. The measure-theoretic analogue is known, while the
pointwise Borel statement remains open. The introduction of
[Grebik, Marks, Rozhon, and Shinko, August 2026](https://arxiv.org/html/2608.22565#S1)
explicitly identifies the question as open and explains the connection to
LOCAL ball carving and the polynomial-growth work of Bernshteyn and Yu.
The recent intermediate-growth results do not settle the general question.

Editorial assessment: the strongest foundational candidate in this search.
Its connection to distributed computing is through decomposition methods;
the conjecture itself does not assert a LOCAL round bound.

## Universal derandomization on subexponential-growth graph classes

Fix a bounded-degree graph class F with a common growth bound
b(r) = exp(o(r)): every radius-r ball in every graph of F has at most b(r)
vertices. Does every LCL problem with randomized LOCAL complexity O(log n)
on F also have deterministic LOCAL complexity O(log* n) on F?

[Grebik and Vidnyanszky, Problem 9.9](https://arxiv.org/html/2502.15347#S9)
poses this speedup question, alongside its distributed-LLL formulation.
Their Definition 8.1 specifies the uniform growth assumption. Merely saying
that each finite graph has some subexponential bound would be vacuous.

Remark 4.13 explains the descriptive connection: Bernshteyn's correspondence
and the Borel LLL already yield Borel solutions from randomized O(log n)
algorithms on subexponential-growth graphs. The proposed deterministic
speedup would provide a general algorithmic counterpart. The same survey
proves O(log* n) deterministic Brooks coloring as a special case.

Editorial assessment: the stronger fit if direct LOCAL relevance is required.
It treats an entire complexity regime across all LCL tasks. It is related to
the existing general distributed-LLL card, but asks for a different speedup
under geometric restrictions.

## Status of this check

Targeted current literature searches found no later resolution of the
speedup question. The August 2026 source explicitly retains Weiss's question.
Keyword searches of canonical cards and deletion reasons found no matching
target. These are source-grounded recommendations, not completed card audits.
