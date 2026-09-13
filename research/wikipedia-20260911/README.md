# Otevřené problémy TCS uvedené na Wikipedii

**Follow-up:** the [atlas import and duplicate audit](../wikipedia-import-20260911/README.md)
records 54 retained additions, eight research directions deleted at the user's request,
78 entries already represented, and one resolved entry.
It also corrects the scope of the uncompletable-word and FIFO-feedback questions.
The inventory below remains the frozen Wikipedia discovery record; use the follow-up
for the import decisions and later status corrections.

Průchod anglickou Wikipedií: 11. září 2026. V podkladech je 174 načtených článků; vybraný soupis má **141 položek**.

Jde o zdrojový soupis otázek, které Wikipedie uvádí jako otevřené. Nejde o záruku úplnosti celé Wikipedie ani o úplné ověření současného stavu v odborné literatuře. Zjevné vyřešené případy a nalezené konflikty jsou uvedeny zvlášť v `status-notes.md`. Názvy jsou anglicky, stručné formulace česky.

Zahrnuty jsou algoritmické a výpočetní otázky, vybrané strukturální grafové problémy, fair division a teorie informace. Obecné otázky fyziky, obecné AI a většina čistě matematických domněnek mimo tento rozsah nebyly zařazeny. Související varianty nejsou automaticky nezávislé problémy. Rozdělení do témat je redakční.

Hlavní vstupy: [informatika](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science), [fair division](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_fair_division), [teorie informace](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory), [matematika](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics), kategorie nevyřešených problémů a navázané tematické články.

Každý záznam v JSON a CSV obsahuje odkaz na konkrétní načtenou revizi, datum revize a lokalizátor zdrojové pasáže; JSON také ukládá její kontext. Zdrojové články jsou archivovány v `pages.json` s původním wikitextem. Text Wikipedie pochází od jejích přispěvatelů a podléhá [CC BY-SA](https://en.wikipedia.org/wiki/Wikipedia:Copyrights).

## Složitost a derandomizace

1. **[P versus NP](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Platí P = NP?

2. **[NP versus coNP](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Platí NP = coNP?

3. **[P versus PSPACE](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Platí P = PSPACE?

4. **[NC versus P](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Platí NC = P?

5. **[L versus NL](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Platí L = NL?

6. **[L versus P](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Platí L = P?

7. **[L versus RL](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Platí L = RL?

8. **[P versus BPP](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Lze efektivní randomizované rozhodování obecně derandomizovat?

9. **[PH versus PSPACE](https://en.wikipedia.org/wiki/Polynomial_hierarchy)** — Platí PH = PSPACE?

10. **[Non-collapse of the polynomial hierarchy](https://en.wikipedia.org/wiki/Polynomial_hierarchy)** — Má polynomiální hierarchie nekonečně mnoho různých úrovní?

11. **[Berman–Hartmanis conjecture](https://en.wikipedia.org/wiki/Berman%E2%80%93Hartmanis_conjecture)** — Jsou všechny NP-úplné jazyky navzájem polynomiálně izomorfní?

12. **[Hartmanis–Stearns conjecture](https://en.wikipedia.org/wiki/Hartmanis%E2%80%93Stearns_conjecture)** — Musí reálné číslo s rozvojem počitatelným v reálném čase být racionální nebo transcendentní?

13. **[Exponential Time Hypothesis (ETH)](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Vyžaduje 3-SAT exponenciální čas v počtu proměnných?

14. **[Strong Exponential Time Hypothesis (SETH)](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Blíží se optimální exponenciální základ pro k-SAT s rostoucím k hodnotě 2?

15. **[Unique Games Conjecture](https://en.wikipedia.org/wiki/Unique_games_conjecture)** — Platí tvrzená NP-těžkost rozlišení téměř splnitelných a téměř nesplnitelných unique games?

16. **[Small-Set Expansion Hypothesis](https://en.wikipedia.org/wiki/Small_set_expansion_hypothesis)** — Platí hypotéza výpočetní obtížnosti rozpoznávání expanze malých množin?

17. **[Deterministic polynomial identity testing](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Existuje deterministický polynomiální algoritmus pro obecný PIT?

18. **[ACC0 versus TC0](https://en.wikipedia.org/wiki/ACC0)** — Lze funkci majority počítat obvody ACC0?

19. **[TC0 versus NC1](https://en.wikipedia.org/wiki/TC0)** — Jsou TC0 a NC1 různé?

20. **[NEXP outside nonuniform TC0](https://en.wikipedia.org/wiki/Circuit_complexity)** — Existuje jazyk v NEXP bez polynomiálně velkých obvodů TC0?

## Důkazy a booleovské funkce

21. **[Frege proof-size lower bounds](https://en.wikipedia.org/wiki/Proof_complexity)** — Lze pro explicitní tautologie dokázat superpolynomiální dolní meze velikosti Fregeho důkazů?

22. **[Optimal and p-optimal propositional proof systems](https://en.wikipedia.org/wiki/Proof_complexity)** — Existuje optimální, respektive p-optimální výrokový důkazový systém? *Dvě související otázky uvedené v jedné položce; nezaměňovat s p-bounded systémy, jejichž existence je ekvivalentní NP = coNP.*

23. **[Effective polynomial simulation of Extended Frege by Resolution](https://en.wikipedia.org/wiki/Proof_complexity)** — Simuluje rezoluce Extended Frege v oslabeném smyslu effective polynomial simulation? *Jde o odborně definovanou oslabenou simulaci, nikoli běžnou polynomiální simulaci.*

24. **[Weak automatability of Resolution](https://en.wikipedia.org/wiki/Proof_complexity)** — Jaké standardní předpoklady obtížnosti by vyvrátila slabá automatizovatelnost rezoluce?

25. **[Log-rank conjecture](https://en.wikipedia.org/wiki/Log-rank_conjecture)** — Je deterministická komunikační složitost polynomiálně omezená logaritmem hodnosti komunikační matice?

26. **[Fourier Entropy–Influence conjecture](https://en.wikipedia.org/wiki/Entropy_influence_conjecture)** — Je Fourierova entropie booleovské funkce nejvýše konstantním násobkem jejího celkového vlivu?

## Kvantové výpočty a kryptografie

27. **[BQP versus NP](https://en.wikipedia.org/wiki/BQP)** — Jaký je vztah BQP a NP, zejména obsahuje BQP celou NP?

28. **[QMA versus QCMA](https://en.wikipedia.org/wiki/QMA)** — Je kvantový certifikát silnější než klasický certifikát ověřovaný kvantovým algoritmem?

29. **[Quantum PCP conjecture](https://en.wikipedia.org/wiki/NLTS_conjecture)** — Je aproximace energie lokálního Hamiltoniánu s konstantní relativní chybou QMA-těžká?

30. **[No low-energy sampleable states conjecture](https://en.wikipedia.org/wiki/NLTS_conjecture)** — Existují lokální Hamiltoniány, jejichž všechny nízkoenergetické stavy nemají efektivně klasicky vzorkovatelné výsledky měření?

31. **[Efficient nonabelian Hidden Subgroup Problem](https://en.wikipedia.org/wiki/Hidden_subgroup_problem)** — Existuje efektivní kvantový algoritmus pro HSP nad obecnými konečnými grupami?

32. **[Existence of one-way functions](https://en.wikipedia.org/wiki/One-way_function)** — Existují jednosměrné funkce?

33. **[Existence of secure public-key cryptography](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Lze prokázat existenci bezpečné kryptografie s veřejným klíčem? *Otázka nepodmíněné existence, nikoli existence prakticky používaných schémat.*

## Algebra a výpočetní teorie čísel

34. **[Classical polynomial-time integer factorization](https://en.wikipedia.org/wiki/Integer_factorization)** — Lze celá čísla faktorizovat v klasickém polynomiálním čase?

35. **[Classical polynomial-time discrete logarithm](https://en.wikipedia.org/wiki/Discrete_logarithm)** — Lze diskrétní logaritmus obecně počítat v klasickém polynomiálním čase?

36. **[Polynomial-time exact Shortest Vector Problem](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Existuje klasický nebo kvantový polynomiální algoritmus pro přesný SVP?

37. **[Square-root sum problem](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Lze v Turingově modelu polynomiálně rozhodnout porovnání součtu odmocnin s daným číslem?

38. **[VP versus VNP / permanent circuit lower bounds](https://en.wikipedia.org/wiki/Arithmetic_circuit_complexity)** — Vyžaduje permanent superpolynomiálně velké aritmetické obvody nad polem charakteristiky různé od 2?

39. **[Shub–Smale tau-conjecture](https://en.wikipedia.org/wiki/Smale%27s_problems)** — Je počet různých celočíselných kořenů polynomu polynomiálně omezen délkou jeho aritmetického výpočtu?

40. **[Scholz conjecture on addition chains](https://en.wikipedia.org/wiki/Scholz_conjecture)** — Platí Scholzova horní mez pro délku sčítacího řetězce pro 2^n − 1?

41. **[Baillie–PSW primality-test counterexample](https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test)** — Existuje složené číslo, které projde Baillieho–PSW testem prvočíselnosti?

## Algoritmy, datové struktury a optimalizace

42. **[Dynamic optimality of splay trees](https://en.wikipedia.org/wiki/Splay_tree)** — Dosahují splay stromy na každé posloupnosti přístupů ceny v konstantním poměru k optimálnímu BST?

43. **[Traversal conjecture for splay trees](https://en.wikipedia.org/wiki/Splay_tree)** — Zpracuje splay strom preorder jiné struktury na stejných klíčích v lineárním čase?

44. **[Deque conjecture for splay trees](https://en.wikipedia.org/wiki/Splay_tree)** — Mají deque operace implementované splay stromem konstantní amortizovanou cenu?

45. **[Split conjecture for splay trees](https://en.wikipedia.org/wiki/Splay_tree)** — Má posloupnost rozdělení splay stromu v součtu lineární cenu?

46. **[Optimal deterministic minimum spanning tree complexity](https://en.wikipedia.org/wiki/Minimum_spanning_tree)** — Jaká je optimální deterministická složitost MST v obecném porovnávacím modelu?

47. **[Depth-first search in NC](https://en.wikipedia.org/wiki/Depth-first_search)** — Lze nějaký DFS strom obecného grafu zkonstruovat v NC? *Nejde o DFS s předepsaným lexikografickým pořadím sousedů.*

48. **[Faster X + Y sorting](https://en.wikipedia.org/wiki/X_%2B_Y_sorting)** — Lze součty všech dvojic ze dvou n-prvkových množin seřadit rychleji než O(n² log n)?

49. **[Optimal average-case Shellsort complexity](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Jaká je nejlepší průměrná složitost Shellsortu s pevnou deterministickou posloupností mezer?

50. **[Optimal integer multiplication complexity](https://en.wikipedia.org/wiki/Multiplication_algorithm)** — Je O(n log n) optimální bitová složitost násobení n-bitových čísel?

51. **[FFT lower bounds](https://en.wikipedia.org/wiki/Fast_Fourier_transform)** — Vyžaduje diskrétní Fourierova transformace v obecných příslušných modelech Ω(n log n) operací?

52. **[Matrix multiplication exponent: omega = 2?](https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication)** — Je exponent násobení matic roven 2?

53. **[Strongly polynomial linear programming](https://en.wikipedia.org/wiki/Linear_programming)** — Existuje silně polynomiální algoritmus pro lineární programování?

54. **[Polynomial-time simplex pivot rule](https://en.wikipedia.org/wiki/Linear_programming)** — Existuje pivotovací pravidlo zajišťující polynomiální nejhorší čas simplexové metody?

55. **[Polynomial diameter of polytopes](https://en.wikipedia.org/wiki/Linear_programming)** — Je průměr grafu polytopu polynomiálně omezen jeho dimenzí a počtem stěn?

56. **[Deterministic k-server conjecture](https://en.wikipedia.org/wiki/K-server_problem)** — Existuje k-kompetitivní deterministický algoritmus pro k-server v libovolné metrice?

57. **[Exact pancake numbers](https://en.wikipedia.org/wiki/Pancake_sorting)** — Jaký je nejhorší minimální počet prefixových otočení potřebných k setřídění permutace délky n?

58. **[1/3–2/3 conjecture](https://en.wikipedia.org/wiki/1/3%E2%80%932/3_conjecture)** — Obsahuje každý konečný netotální poset dvojici s pravděpodobností pořadí v náhodné lineární extenzi mezi 1/3 a 2/3?

59. **[Gold partition conjecture](https://en.wikipedia.org/wiki/1/3%E2%80%932/3_conjecture)** — Lze vybrat dvě navazující porovnání tak, aby pro každý výsledek platilo t0 ≥ t1 + t2, kde ti je počet zbývajících lineárních extenzí po i porovnáních?

## Jemná složitost a enumerace

60. **[Truly subquadratic 3SUM](https://en.wikipedia.org/wiki/3SUM)** — Existuje pro obecný 3SUM algoritmus O(n^(2−ε)) pro konstantní ε > 0? *Původní přísná kvadratická domněnka byla vyvrácena; tato silnější úspora exponentu zůstává otázkou.*

61. **[Truly subquadratic edit distance](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Lze přesnou editační vzdálenost dvou n-znakových řetězců počítat v O(n^(2−ε))?

62. **[Truly subcubic all-pairs shortest paths](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Existuje obecný algoritmus pro vážené APSP v O(n^(3−ε))?

63. **[Online matrix-vector multiplication conjecture](https://en.wikipedia.org/wiki/Online_matrix-vector_multiplication_problem)** — Lze n online násobení booleovské n×n matice vektorem provést v celkovém O(n^(3−ε))?

64. **[Output-polynomial monotone dualization](https://en.wikipedia.org/wiki/Monotone_dualization)** — Lze vypsat všechny minimální transverzály hypergrafu v čase polynomiálním ve velikosti vstupu a výstupu? *Zahrnuje ekvivalentní formulace přes minimální hitting sets, monotónní dualizaci a přesné učení s výstupem CNF i DNF.*

## Geometrie a grafové algoritmy

65. **[Polynomial-time graph isomorphism](https://en.wikipedia.org/wiki/Graph_isomorphism_problem)** — Lze izomorfismus obecných grafů rozhodnout v polynomiálním čase?

66. **[Graph canonization versus graph isomorphism](https://en.wikipedia.org/wiki/Graph_canonization)** — Je kanonizace grafů polynomiálně ekvivalentní testování izomorfismu?

67. **[Exact bounded clique-width recognition](https://en.wikipedia.org/wiki/Clique-width)** — Lze pro každé pevné k rozpoznat grafy s clique-width nejvýše k v polynomiálním čase?

68. **[Polynomial-time planar treewidth](https://en.wikipedia.org/wiki/Treewidth)** — Lze treewidth rovinných grafů počítat v polynomiálním čase?

69. **[Simultaneous Embedding with Fixed Edges (two graphs)](https://en.wikipedia.org/wiki/Simultaneous_embedding)** — Lze existenci SEFE pro dva grafy rozhodnout v polynomiálním čase?

70. **[Polynomial-time simple closed quasigeodesic](https://en.wikipedia.org/wiki/Theorem_of_the_three_geodesics)** — Lze na konvexním mnohostěnu najít jednoduchou uzavřenou kvazigeodetiku v polynomiálním čase?

71. **[Klee's measure problem in dimension at least three](https://en.wikipedia.org/wiki/Klee%27s_measure_problem)** — Jaká je optimální složitost výpočtu objemu sjednocení osově rovnoběžných boxů v dimenzi alespoň tři?

72. **[Optimal higher-dimensional Euclidean MST complexity](https://en.wikipedia.org/wiki/Euclidean_minimum_spanning_tree)** — Jaká je optimální složitost eukleidovské MST ve vyšších pevných dimenzích?

73. **[Gilbert–Pollak conjecture](https://en.wikipedia.org/wiki/Gilbert%E2%80%93Pollak_conjecture)** — Je nejhorší poměr délky eukleidovské MST a Steinerova stromu v rovině roven 2/√3?

74. **[Dürer's edge-unfolding conjecture](https://en.wikipedia.org/wiki/Net_(polyhedron))** — Má každý konvexní mnohostěn nepřekrývající se síť získanou řezáním podél hran?

75. **[Subquadratic universal point sets for planar graphs](https://en.wikipedia.org/wiki/Universal_point_set)** — Existují univerzální bodové množiny velikosti o(n²) pro přímkové kresby všech n-vrcholových rovinných grafů?

76. **[k-sets and halving lines](https://en.wikipedia.org/wiki/K-set_(geometry))** — Jaký je optimální asymptotický počet k-množin a půlících přímek bodové množiny v rovině?

77. **[GNRS conjecture](https://en.wikipedia.org/wiki/GNRS_conjecture)** — Mají všechny vlastní minorově uzavřené třídy grafů vložení do ℓ1 s konstantním zkreslením?

78. **[Strong Papadimitriou–Ratajczak conjecture](https://en.wikipedia.org/wiki/Greedy_embedding)** — Má každý polyedrický graf rovinné greedy vložení s konvexními stěnami?

79. **[Bounded slope number for maximum-degree-four graphs](https://en.wikipedia.org/wiki/Graph_drawing)** — Je slope number grafů maximálního stupně čtyři omezen konstantou?

80. **[Bounded book thickness implies bounded queue-number?](https://en.wikipedia.org/wiki/Queue_number)** — Je queue-number omezen nějakou funkcí book thickness?

81. **[Three-page book embedding with fixed vertex order](https://en.wikipedia.org/wiki/Book_embedding)** — Jaká je složitost testování třístránkového book embedding při pevném pořadí vrcholů?

82. **[NP membership of exact minimum-weight triangulation](https://en.wikipedia.org/wiki/Minimum-weight_triangulation)** — Je rozhodovací verze přesné minimum-weight triangulation v NP? *NP-těžkost je známá; otevřená je příslušnost do NP při přesných eukleidovských vahách.*

## Automaty, logika a vyčíslitelnost

83. **[Polynomial-time parity games](https://en.wikipedia.org/wiki/Parity_game)** — Existuje polynomiální algoritmus pro paritní hry?

84. **[Černý conjecture](https://en.wikipedia.org/wiki/Synchronizing_word)** — Má každý n-stavový synchronizující DFA synchronizační slovo délky nejvýše (n−1)²?

85. **[Generalized star-height problem](https://en.wikipedia.org/wiki/Generalized_star-height_problem)** — Potřebuje některý regulární jazyk při povoleném doplňku hvězdovou výšku alespoň dvě?

86. **[Separating words problem](https://en.wikipedia.org/wiki/Separating_words_problem)** — Kolik stavů DFA je v nejhorším případě třeba k rozlišení dvou různých slov délky n?

87. **[Polynomial bounds for uncompletable words of codes](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Existuje pro neúplné proměnně dlouhé kódy polynomiální mez délky nejkratšího nedoplnitelného slova? *Oslabená otázka související s Restivovou domněnkou; původní obecná domněnka je vyvrácená.*

88. **[Universality classification of elementary cellular automata](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Jaký je přesný status Turingovy univerzality zbývajících elementárních celulárních automatů?

89. **[Barendregt–Geuvers–Klop conjecture](https://en.wikipedia.org/wiki/Pure_type_system)** — Je každý slabě normalizující čistý typový systém také silně normalizující?

90. **[Decidability of multiplicative-exponential linear logic](https://en.wikipedia.org/wiki/Linear_logic)** — Je odvoditelnost v MELL rozhodnutelná?

91. **[Skolem problem](https://en.wikipedia.org/wiki/Skolem_problem)** — Je rozhodnutelné, zda daná lineární rekurentní posloupnost nabývá nuly?

92. **[Hilbert's tenth problem over the rationals](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)** — Je rozhodnutelná existence racionálního řešení diofantické rovnice?

93. **[Tarski's exponential function problem](https://en.wikipedia.org/wiki/Tarski%27s_exponential_function_problem)** — Je teorie reálných čísel s exponenciálou rozhodnutelná?

94. **[Matrix mortality for 2×2 integer matrices](https://en.wikipedia.org/wiki/Matrix_mortality_problem)** — Je rozhodnutelné, zda semigrupa generovaná danými celočíselnými 2×2 maticemi obsahuje nulovou matici?

95. **[Word equations in NP](https://en.wikipedia.org/wiki/Word_equation)** — Patří rozhodování řešitelnosti slovních rovnic do NP?

96. **[Single-exponential shortest solutions of word equations](https://en.wikipedia.org/wiki/Word_equation)** — Mají splnitelné slovní rovnice vždy řešení délky nejvýše exponenciální v délce vstupu?

97. **[Word equations with linear length constraints](https://en.wikipedia.org/wiki/Word_equation)** — Je řešitelnost slovních rovnic s lineárními omezeními délek rozhodnutelná?

98. **[A logic capturing PTIME on unordered structures](https://en.wikipedia.org/wiki/Descriptive_complexity_theory)** — Existuje přirozená logika zachycující PTIME na neuspořádaných konečných strukturách?

99. **[Infinite-domain CSP dichotomy](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)** — Platí předpokládaná dichotomie P/NP-těžkost pro CSP reduktů konečně omezených homogenních struktur?

100. **[Busy Beaver BB(6)](https://en.wikipedia.org/wiki/Busy_beaver)** — Jaká je přesná hodnota časové busy-beaver funkce pro šest stavů a dva symboly? *Nezaměňovat s již určeným BB(5) ani s nevyčíslitelností obecné funkce.*

## Fair division

101. **[EFX existence for arbitrary numbers of additive agents](https://en.wikipedia.org/wiki/Envy-freeness_up_to_any_item)** — Existuje vždy úplná EFX alokace pro libovolný počet agentů s aditivními hodnotami?

102. **[Polynomial-time EFX for three additive agents](https://en.wikipedia.org/wiki/Envy-freeness_up_to_any_item)** — Lze EFX alokaci pro tři aditivní agenty najít v polynomiálním čase? *Samotná existence pro tři aditivní agenty je vyřešená.*

103. **[Optimal polynomial-time EFX approximation](https://en.wikipedia.org/wiki/Envy-freeness_up_to_any_item)** — Jaký nejlepší aproximační poměr EFX lze efektivně garantovat pro aditivní agenty? *Číselné dosavadní meze z Wikipedie zde nepřebírám jako aktuální.*

104. **[Exact EFX with sublinearly many unallocated goods](https://en.wikipedia.org/wiki/Envy-freeness_up_to_any_item)** — Lze dosáhnout přesného EFX při ponechání pouze o(n) nerozdělených statků?

105. **[Constant-k EFkX allocations](https://en.wikipedia.org/wiki/Envy-freeness_up_to_any_item)** — Existuje univerzální konstanta k zaručující EFkX alokaci pro libovolný počet aditivních agentů?

106. **[Polynomial-time EF1 + Pareto optimality for goods](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_fair_division)** — Lze EF1 a Pareto-optimální alokaci aditivních statků najít v polynomiálním čase?

107. **[Complexity of deciding MMS-allocation existence](https://en.wikipedia.org/wiki/Maximin_share)** — Jaká je přesná složitost rozhodnutí, zda instance připouští MMS alokaci?

108. **[Optimal multiplicative MMS guarantee for goods](https://en.wikipedia.org/wiki/Maximin_share)** — Jakou největší konstantní část MMS lze vždy garantovat pro aditivní statky?

109. **[Optimal multiplicative MMS guarantee for chores](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_fair_division)** — Jaký je optimální univerzální aproximační poměr MMS pro aditivní povinnosti?

110. **[Optimal ordinal MMS guarantee](https://en.wikipedia.org/wiki/Maximin_share)** — Jaké nejmenší d(n) vždy zaručí 1-out-of-d MMS pro n aditivních agentů?

111. **[Existence of pairwise-MMS allocations](https://en.wikipedia.org/wiki/Maximin_share)** — Existuje vždy pairwise-maximin-share-fair alokace aditivních statků?

112. **[Necessary envy-freeness with a fixed number of agents](https://en.wikipedia.org/wiki/Envy-free_item_allocation)** — Jaká je složitost nalezení nutně envy-free alokace při konstantním počtu agentů a ordinálních preferencích?

113. **[Query complexity of complete envy-free cake-cutting](https://en.wikipedia.org/wiki/Envy-free_cake-cutting)** — Jaká je optimální dotazová složitost envy-free rozdělení celého dortu?

114. **[Envy-free proportional cake-cutting with free disposal](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_fair_division)** — Jaká je dotazová složitost při povolení nerozděleného zbytku a požadavku proporcionality?

115. **[Bounded connected envy-free proportional cake-cutting](https://en.wikipedia.org/wiki/Envy-free_cake-cutting)** — Existuje pro alespoň čtyři agenty konečně omezený dotazový protokol pro souvislé envy-free a proporcionální rozdělení s povoleným zbytkem?

116. **[Minimum cuts in finite envy-free cake-cutting](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_fair_division)** — Kolik řezů stačí k envy-free rozdělení celého dortu protokolem s konečným počtem dotazů?

117. **[Connected proportional division of a partly burnt cake](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_fair_division)** — Jaká je optimální složitost souvislého proporcionálního rozdělení dortu se smíšenými kladnými a zápornými hodnotami?

118. **[Approximate envy-free division of a partly burnt cake](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_fair_division)** — Jaká je složitost souvislého aproximovaně envy-free rozdělení částečně spáleného dortu?

119. **[Competitive equilibrium for almost all budgets](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_fair_division)** — Existuje při dvou aditivních agentech tržní rovnováha pro téměř všechny vektory rozpočtů?

120. **[Fair allocation with bounded sharing](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_fair_division)** — Jaká je složitost spravedlivého rozdělení, jestliže smí být sdíleno nejvýše k předmětů?

## Teorie informace a kódování

121. **[Capacity of a general wireless network](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory)** — Jaká je kapacitní oblast obecné bezdrátové sítě?

122. **[Broadcast-channel capacity](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory)** — Jaká je obecná kapacitní oblast broadcast kanálu?

123. **[Two-user interference-channel capacity](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory)** — Jaká je obecná kapacitní oblast dvouuživatelského interferenčního kanálu?

124. **[Two-way-channel capacity](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory)** — Jaká je obecná kapacitní oblast obousměrného kanálu?

125. **[Capacity of ALOHA](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory)** — Jaká je kapacita obecného modelu náhodného přístupu ALOHA?

126. **[Feedback capacity of queue channels](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory)** — Kdy zpětná vazba zvyšuje kapacitu FIFO frontového kanálu pro obecná rozdělení doby obsluhy?

127. **[Quantum-channel capacity](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory)** — Jak určit kvantovou kapacitu obecného kvantového kanálu?

128. **[Lossy distributed source coding](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory)** — Jaká je optimální oblast rychlostí pro oddělené ztrátové kódování korelovaných zdrojů?

129. **[Binary deletion-channel capacity](https://en.wikipedia.org/wiki/Deletion_channel)** — Jaká je kapacita binárního mazacího kanálu v závislosti na pravděpodobnosti smazání?

130. **[Computability and complexity of graph Shannon capacity](https://en.wikipedia.org/wiki/Shannon_capacity_of_a_graph)** — Jaká je algoritmická složitost výpočtu Shannonovy kapacity grafu?

131. **[Shannon capacity of C7](https://en.wikipedia.org/wiki/Shannon_capacity_of_a_graph)** — Jaká je přesná Shannonova kapacita sedmicyklu?

132. **[Length–query tradeoff for locally decodable codes](https://en.wikipedia.org/wiki/Locally_decodable_code)** — Jaký je optimální vztah délky lokálně dekódovatelného kódu a počtu dotazů dekodéru?

## Strukturální grafy a související kombinatorika

133. **[Hadwiger conjecture](https://en.wikipedia.org/wiki/Hadwiger_conjecture_(graph_theory))** — Má každý graf s chromatickým číslem k úplný graf K_k jako minor?

134. **[Erdős–Hajnal conjecture](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Hajnal_conjecture)** — Vynutí zákaz jednoho indukovaného podgrafu polynomiálně velkou kliku nebo nezávislou množinu?

135. **[Gyárfás–Sumner conjecture](https://en.wikipedia.org/wiki/Gy%C3%A1rf%C3%A1s%E2%80%93Sumner_conjecture)** — Jsou grafy bez pevného indukovaného stromu a pevné kliky chromaticky omezené?

136. **[Cereceda's reconfiguration conjecture](https://en.wikipedia.org/wiki/Cereceda%27s_conjecture)** — Lze každé dvě (d+2)-obarvení d-degenerovaného grafu propojit kvadraticky mnoha změnami barvy vrcholu?

137. **[Graph reconstruction conjecture](https://en.wikipedia.org/wiki/Reconstruction_conjecture)** — Je každý jednoduchý graf s alespoň třemi vrcholy určen multisetem svých vrcholově smazaných podgrafů?

138. **[Edge reconstruction conjecture](https://en.wikipedia.org/wiki/Reconstruction_conjecture)** — Je graf s alespoň čtyřmi hranami určen multisetem svých hranově smazaných podgrafů?

139. **[List edge-coloring conjecture](https://en.wikipedia.org/wiki/List_edge-coloring)** — Rovná se pro každý graf seznamový chromatický index jeho chromatickému indexu?

140. **[Aanderaa–Karp–Rosenberg evasiveness conjecture](https://en.wikipedia.org/wiki/Aanderaa%E2%80%93Karp%E2%80%93Rosenberg_conjecture)** — Vyžaduje rozhodnutí každé netriviální monotónní grafové vlastnosti v nejhorším případě dotaz na každou možnou hranu?

141. **[Erdős–Rado sunflower conjecture](https://en.wikipedia.org/wiki/Sunflower_(mathematics))** — Stačí pro vynucení slunečnice pevné velikosti exponenciálně mnoho k-prvkových množin v parametru k?
