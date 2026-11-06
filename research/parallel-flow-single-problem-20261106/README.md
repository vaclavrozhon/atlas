# Single-problem parallel flow card

The owner requested that TCS-4763, **Work-efficient parallel approximate flow**,
ask one problem and be selected green. The card now asks only for a uniform
randomized parallel approximation of **undirected vertex-capacitated maximum
flow**, with nearly-linear total work and polylogarithmic depth. This is the
second branch of its previous formulation. The cost-budget alternative and
all disjunctive acceptance conditions have been removed. The title, stable ID,
category pair, ranking score and mathematical conventions of the chosen branch
are retained.

The primary source explicitly includes this target in
[Open Problem 8.1](https://arxiv.org/html/2510.20456v1#S8) (Open Problem 1 in
the FOCS conference version). Ordinary undirected edge-capacitated maximum flow
already has the requested parallel bounds in
[SODA 2024](https://arxiv.org/abs/2402.14950), so simplifying away the vertex
capacities would change the intended target to an earlier solved problem.
The vertex-capacitated version was chosen to retain one original max-flow
question. This targeted source check does not resume the deferred catalogue
status audit. The complete previous card and its status review are preserved
in `TCS-4763-before.json`.

The static default changes from red to green, making 504 static green cards.
The live service already contains a green choice for this card at revision 1;
no selection POST is needed. Existing shared choices and category assignments
must remain unchanged by publication. The card retains its move button between
Distributed, parallel and sublinear algorithms and Graph algorithms.

Validation passed: isolated catalogue/publication/ranking/taxonomy/selection/
archive checks (`make check`), all 39,694 active-card math expressions, and
all 14 service tests plus the service build. The source proposal contains
504 green and 645 red cards across 35 categories; its manifest is
`d51d7cb1b88fe12850c9`. Sites version 13 was successfully deployed before the
reader update. Only this card's source-default color changed.
