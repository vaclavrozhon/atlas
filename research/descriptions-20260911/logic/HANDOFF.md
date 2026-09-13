# Description handoff: logic agent

Completed 415 individually authored five-sentence descriptions: 149 automata, 180 semantics/logic/verification, and the explicitly assigned last 86 distributed records.

Schema QA: all files parse, IDs match, exactly five sentences each, nonempty source URLs, 75–107 words per description, no duplicate exact sentences. All description writes used atomic temporary-file replacement.

No changes to catalogue statuses, evidence, cards, categories, UI, or shared modules. Historical source quotations are not treated as present-status verification.

## Source and formulation exceptions

- TCS-0121: Later local source ESA2026.121 reference2 cites Almagor-Arbel-Sheinvald, Determinization of min-plus weighted automata is decidable, SODA2026 pp247–257, DOI10.1137/1.9781611978971.11. The legacy question may be superseded; catalogue status unchanged.
- TCS-5701: The cited source explicitly labels Conjecture 16 false and provides a counterargument; this inherited active record is not an unresolved conjecture. Existing status is unchanged.
- TCS-6185: The source immediately follows the historical open passage with Our paper fills this gap and its positive contributions.
- TCS-6323: The cited abstract explicitly resolves the quoted historical complexity gap; the existing catalogue status is unchanged.
- TCS-6995: The imported all-subsets statement requires a formulation review: a synchronizing automaton with an absorbing state cannot avoid a subset containing that state. The source excerpt does not supply the needed global assumption.
- TCS-0871: The original source remark already establishes undecidability of inclusion; the universality part is separate.
- TCS-0899: The source includes a correction to the claimed higher-order orthogonal baseline; description incorporates it.
- TCS-1487: The cited FSCD 2026.26 page explicitly says the following section answers the quoted canonicity question affirmatively; status unchanged.
- TCS-1796: The source immediately answers universal bounded-message implementability negatively and develops a characterization/decision direction instead; no catalogue status change.
- TCS-2815: The harvested excerpt does not specify payoff and strategy conditions for the infinite-horizon equilibrium existence claim; the description intentionally treats it as the source-specific research direction.
- TCS-4116: The source states and proves Theorem 15 immediately after calling this an open problem: finding a Nash equilibrium in acyclic cost-sharing network games is PLS-hard. Catalogue status was not changed.
- TCS-5600: Historical 2018 elementary-upper-bound question is superseded by Czerwinski et al., The reachability problem for Petri nets is not elementary, JACM2021, cited in locally saved MFCS2025.22 reference9; catalogue status unchanged.
- TCS-5876: The general quotation omits rounding assumptions; retained source-setting wording rather than asserting periodicity for every arbitrary bounded-effect rounding rule.
- TCS-5911: Selected passage is a broad verification research direction rather than a uniquely specified open decision problem. Description reflects that scope.
- TCS-5975: The quoted introduction is followed by undecidability for polynomial dynamic weights, including finite and upward-closed targets; source also studies decidable/decisive subclasses. No status change.
- TCS-5976: The source immediately answers the previously cited expressiveness question: HD VASSs lie strictly between deterministic and nondeterministic ones in every fixed dimension, including one. No status change.
- TCS-6283: Own source abstract and introduction explicitly refute the historical log^k n optimality conjecture for k>=3 with improved algorithms; catalogue status unchanged.
- TCS-6333: Own source resolves relational completeness for plain KA without tests and leaves the KAT extension conjectural; wording separates those scopes.
- TCS-6359: Own source proves EXPSPACE-completeness of sr-expression refinement after the historical open-question passage; full spr signature and axiomatization are separate.
- TCS-6418: Historical 2011 simultaneous time/message MST construction question is superseded: locally saved DISC2022.19 abstract cites synchronous near-optimal MST algorithms by Pandurangan et al. STOC2017 and Elkin PODC2017. Its remaining question TCS-2870 concerns asynchronous KT0. No catalogue status change.
- TCS-3003: Own source CCC2021.34 abstract explicitly answers negatively: there exists a GSF-local propagating property with no proximity-oblivious tester. No catalogue status change.
- TCS-4404: Restored directed treewidth assumption from source abstract; ordinary undirected support treewidth would not suffice.
- TCS-5296: Source uses communication/message size within its one-round broadcast/sketch model; description avoids strengthening the truncated statement into a universal claim for every LCL.
- TCS-5346: Own source abstract immediately gives first algorithms meeting the quoted sublinear-passes/sublinear-space goal through O(nk)-space n/k-pass tradeoff. No status change.
- TCS-5503: Own source abstract answers broadcaster sufficiency negatively via the Delayed Lossy-Link model, even without crashes. No status change.
- TCS-5537: Recovered footnote10 context: n^(1/3)-to-sqrt(n) gap is SINGLE matroid basis with independence queries, not main matroid intersection bound.
- TCS-6022: Question27 omits the word parallel in isolation; immediately preceding discussion specifies RNC sampling and says the BEST reduction is polynomial-time but not known in NC. Description restores RNC scope.
