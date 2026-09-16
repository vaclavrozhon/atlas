# TCS-3655: source scope and remaining choice

Checked 16 September 2026 by `third-strings-862815`. Update: the user selected variant 1 on 16 September 2026. The canonical card is now completed in that explicitly recorded variant; the following research notes preserve the preceding scope analysis.

## Recovered mathematical content

[Kaposi, Kovács and Lafont](https://drops.dagstuhl.de/storage/00lipics/lipics-vol175-types2019/LIPIcs.TYPES.2019.6/LIPIcs.TYPES.2019.6.pdf) is a TYPES 2019 paper **published 24 September 2020**, as confirmed by its [proceedings record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.TYPES.2019.6). Its Corollary 58 constructs finitary inductive-inductive types from indexed W-types in models of extensional type theory. Definition 1 assumes a countable predicative universe hierarchy, dependent products, dependent sums, unit types, identity types, UIP and equality reflection. Section 5 treats infinitary branching as a separate proposed extension. The UIP-free question therefore concerns the finitary theory unless explicitly broadened.

The signature language in §2 has a universe of sort codes, decoding, dependent function types with an inductive sort as domain, and external parameter products. Later sorts may be indexed by earlier sorts; constructors may mention preceding constructors. There are no equality constructors in the IIT signature language. External parameter types may be arbitrary types in the surrounding model; restricting them to sets would remove part of the issue.

The target requires **full dependent elimination**, not just ordinary simultaneous induction. For the example with `Con : Type` and `Ty : Con → Type`, full motives have the form

```
Conᴰ : Con → Type
Tyᴰ  : (Γ : Con) → Conᴰ Γ → Ty Γ → Type.
```

The type eliminator depends on the result of the context eliminator:

```
elimCon : (Γ : Con) → Conᴰ Γ
elimTy  : (Γ : Con) → (A : Ty Γ) → Tyᴰ Γ (elimCon Γ) A.
```

This is the recursive-recursive dependency emphasized on pp. 6:2–4. The simpler motive `Ty → Type` does not have it. Remark 47 in §4.2.2 and the final passage on p. 6:29 explicitly retain the UIP-free problem. They do not fix a replacement foundational theory or the precise strength of its computation equations.

## Concrete variants requiring a choice

1. **Intensional base:** a generic construction in intensional Martin-Löf type theory with cumulative universes, dependent products and sums, unit and natural-number types, intensional identity types, indexed W-types and function extensionality; without UIP or equality reflection. Require full dependent eliminators with propositional constructor computation equations. This is a concrete candidate specialization, not an equivalent restatement established by the source.
2. **Cubical base:** a generic construction in a fixed cubical type theory with ordinary inductive families, allowing its cubical composition structure and univalence; again require full dependent eliminators with propositional constructor equations. This admits primitives absent from the first base. Nondefinability in the first would not disprove constructibility in the second.

Judgmental computation equations would be a stronger requirement than propositional ones. The extensional source does not distinguish them in the same way because its equality-reflection rule identifies the two notions. A choice must therefore state which equations count as success. Neither variant should be silently recorded as the uniquely intended source question.

For either variant, a Lean acceptance proof must represent the chosen object theory and its permitted rules, or a precise class of its models. Lean's native equality inhabits its proof-irrelevant proposition sort; using it directly as the object theory's identity type would reintroduce uniqueness of identity proofs.

## Checked partial results and false matches

[Hugunin, FoSSaCS 2019](https://jashug.github.io/papers/ConstructingII.pdf), §2 Theorem 1, proves that an earlier particular construction with its simple eliminator entails UIP. This is a limitation of that construction, not impossibility of every reduction. Section 3 constructs a particular example in cubical type theory with simple elimination. It is not a generic theorem for the full eliminator required by this card.

[Szumi Xie's ConTyWithoutK artifact](https://gist.github.com/szumixie/cf092edec50ad11b91c2d7d086582b15), updated 17 May 2026, treats one closed finitary context/type signature, using cubical Agda. Its `DAlg` motive and `indTy` type have the full dependent shape. However, it is not parameterized by arbitrary IIT signatures and contains four statements postulated as “provable” at lines 157–159 and 179–181. The checked snapshot is revision `fc32088bd31bcc59e3266dde2ab00c184a025820`; it was read for scope, not typechecked. This is a relevant recent partial artifact, not a checked resolution of the generic source question.

The bounded search found no primary result resolving the full generic question in a specified UIP-free foundation. Source text, the Hugunin paper, and the artifact snapshot are saved with hashes in [strings-sources.json](strings-sources.json).
