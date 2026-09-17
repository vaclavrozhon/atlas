# Positional equilibria: source scope and 2026 results

TCS-0571 is reserved pending an objective-class choice. Its source is Antonio
Casares, Automata Exchange 24.2, dated 1 July 2024. The complete short entry
was read on 17 September 2026. It asks separately about reachability, Büchi
and parity objectives, on edge-colored multiplayer graphs.

The proposed baseline is a finite deterministic turn-based arena with no dead
ends, complete observation, one designated initial vertex and arbitrary finite
player count. Pure positional strategies depend only on the current vertex;
profitable deviations may use the complete history. A profile that works
simultaneously from every vertex is a stronger target and is not presumed.
The source does not explicitly spell out arena cardinality or the initial
vertex convention; the question sent to the user includes these choices.

Fresh primary source:

- Mona Alluwaym, James C. A. Main, Sven Schewe, *Simple Nash Equilibria for
  Qualitative Multiplayer Games*, MFCS 2026, LIPIcs 386, 85:1–85:17,
  published 21 August 2026, DOI 10.4230/LIPIcs.MFCS.2026.85.
- Full arXiv:2607.07151v1, 8 July 2026, cached as positional2026.pdf/.txt.
  Read introduction, §2 strategy definitions, §3 Examples 1 and 3,
  Theorems 2 and 4, Theorem 10 and conclusion. Publisher abstract and PDF
  were opened; locator numbers above refer to the author version.

Scope distinctions essential for the later review:

1. Memoryless in this paper permits randomization. Positional means both
   memoryless and pure. The main positive theorem establishes memoryless
   randomized equilibria; it does not establish the proposed pure target.
2. Example 1 mixes reachability/Büchi players with safety/coBüchi players.
   Its negative result is for everywhere NE and subgame-perfect equilibrium.
   It is not a counterexample to ordinary all-reachability NE from one start.
3. Example 3 uses 1–3 **Muller** objectives on the set of infinitely visited
   vertices. A Mostowski hierarchy class must not be silently identified
   with parity labels on the original arena: an automaton/product
   translation may add memory, changing the positional question.
4. The conclusion explicitly leaves pure positional NE, everywhere NE and
   SPE open when every player has a reachability objective (or every
   player a safety objective).
5. Theorem 10 gives pure positional equilibria when all reachability targets
   and unsafe vertices are absorbing. General targets need not be absorbing.
6. The preprint's displayed Theorem 4 omits "memoryless" in its sentence.
   Its surrounding section, example and conclusion supply that restriction;
   do not copy the sentence as a claim that ordinary unrestricted NE fail.

Do not archive based on the abstract, a secondary summary, or a theorem
about a stronger equilibrium notion. Do not change the question to randomised
strategies, absorbing targets or a prescribed winning payoff vector.
