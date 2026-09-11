"""Individually written cards. These are distinct from mechanically indexed evidence.

Status is an assessment of cited literature, not an independent verification of proofs.
Each entry records the exact source and review scope; identifiers are assigned by build.py.
"""
CARDS=[]
def ref(key,title,authors,year,url,locator='',pdf_url=''):
    return dict(id=key,title=title,authors=authors,year=year,url=url,locator=locator,pdf_url=pdf_url)
def add(key,title,area,formal,context,why,progress,references,**extra):
    CARDS.append(dict(key=key,title=title,area=area,formal=formal,context=context,why=why,progress=progress,references=references,evidence='reviewed',status='source_open',year=max(r['year'] for r in references),reviewed_on='2026-09-10',status_note='Rešerše k 10. 9. 2026; rozsah a datum doloženého pokroku níže.',review_note='Zadání a uvedené výsledky byly jednotlivě zkontrolovány proti citovaným zdrojům. Důkazy nových prací nebyly nezávisle ověřovány. Hodnocení významu je redakční úsudek.',rank=10000,**extra))
def p(date,text,citation):return dict(date=date,text=text,citation=citation)

qpcp=ref('qpcp','The Quantum PCP Conjecture','Dorit Aharonov; Itai Arad; Thomas Vidick',2013,'https://arxiv.org/abs/1309.7495','Hamiltonian formulation')
privatepcp=ref('privatepcp','Private PCPs from Product Expansion','Mitali Bafna; Nikhil Vyas',2026,'https://eccc.weizmann.ac.il/report/2026/150/','Introduction; Theorem 1.2; Conjecture 1.4','https://eccc.weizmann.ac.il/report/2026/150/download/#page=5')
add('quantum_pcp_hamiltonian','Quantum PCP: konstantní mezera pro lokální Hamiltoniány','Quantum computation',
    r'Existují konstanty $k$ a $\varepsilon>0$, pro něž je následující slibový problém QMA-těžký? Na vstupu je $H=\frac1m\sum_{i=1}^m H_i$ na $n$ qubitech, kde každý $H_i$ působí na nejvýše $k$ qubitů a $0\preceq H_i\preceq I$. Rozhodněte, zda $\lambda_{\min}(H)\le a$, nebo $\lambda_{\min}(H)\ge b$, při slibu $b-a\ge\varepsilon$. Redukce má být efektivní; jde o tuto normalizovanou Hamiltonianovou verzi.',
    'Klasická PCP věta převádí přesné ověřování na kontrolu malé části důkazu s konstantní mezerou. Kvantový protějšek naráží na provázání a na to, že lokální pohled nemusí odhalovat zakódovanou informaci.',
    'Určuje, zda je přibližná energie kvantového systému výpočetně stejně zásadní překážkou jako přesné ověřování kvantového svědka. Propojuje složitost, kvantové kódy a lokální testování.',
    [p('2013','Survey vymezuje Hamiltonianovou domněnku a překážky kvantové analogie PCP.','qpcp'),p('2026-08-19',r'Bafna–Vyas stále uvádějí obecnou domněnku jako otevřenou. Dávají klasické private PCP s $O(\sqrt n)$ dotazy; silnější parametry podmiňují produktovou expanzí. To není důkaz Quantum PCP.','privatepcp')],
    [qpcp,privatepcp],criterion='models',title_en='Quantum PCP conjecture, Hamiltonian version')

qiop=ref('qiop','Quantum Interactive Oracle Proofs','Baocheng Sun; Thomas Vidick',2026,'https://arxiv.org/abs/2601.12874','Definitions 1.1–1.2; Theorems 1.5, 1.7; Question 1.9','https://arxiv.org/pdf/2601.12874#page=4')
add('strong_qiop_poly','Silné kvantové IOP s polynomiální komunikací','Quantum computation',
    r'Má každý problém v QMA silný quantum IOP s konstantním rozdílem completeness a soundness, $O(1)$ celkovým počtem dotazovaných qubitů a $\operatorname{poly}(n)$ komunikovanými qubity? V silném modelu verifikátor po každém kole vrací celý registr zprávy a nemůže si jeho část ponechat. Použije se model a kvantový přístup z definic 5.10 a 5.14 zdroje.',
    'Interakce může usnadnit lokální kontrolu kvantového důkazu. Zásadní je rozlišit počet čtených qubitů, velikost soukromého kvantového registru a délku komunikace.',
    'Izoluje cenu velmi slabého kvantového verifikátoru. Pozitivní výsledek by odstranil exponenciální komunikaci ze současné konstrukce a dal nový prostředek pro delegování kvantového ověřování.',
    [p('2026-01-19',r'Obecný qIOP má polynomiální komunikaci, ale používá polynomiálně velký soukromý kvantový zdroj. Silná konstrukce pracuje s konstantně mnoha qubity a vyžaduje $\exp(\operatorname{poly}(n))$ komunikace. Otázka 1.9 žádá polynomiální délku.','qiop')],[qiop],criterion='resources')

qadvice=ref('qadvice','Separating Quantum and Classical Advice with Good Codes','John Bostanci; Andrew Huang; Vinod Vaikuntanathan',2026,'https://eccc.weizmann.ac.il/report/2026/020/','Introduction','https://eccc.weizmann.ac.il/report/2026/020/download/')
add('qma_vs_qcma','Má kvantový svědek větší sílu než klasický?','Quantum computation',
    r'Rozhodněte, zda $\mathrm{QMA}=\mathrm{QCMA}$. Obě třídy používají kvantový verifikátor s polynomiálním časem a konstantní chybou; QMA dovoluje polynomiálně dlouhý kvantový svědek, QCMA pouze klasický řetězec. Jde o běžné třídy bez orákula.',
    'Kvantový stav může reprezentovat důkaz, který nelze stručně popsat klasickými bity. Orákulové separace testují tuto intuici, samy však neoddělují standardní třídy.',
    'Jde o základní otázku o tom, jaký druh informace může být nezbytný pro efektivní ověření tvrzení.',
    [p('2025–2026','Byla získána separace vzhledem ke klasickému orákulu. Práce z února 2026 dává jednodušší konstrukci; obecná neorákulová otázka tím zůstává nedotčena.','qadvice')],[qadvice],criterion='models')
add('bqp_quantum_advice','Kvantová versus klasická neuniformní rada','Quantum computation',
    r'Platí $\mathrm{BQP/qpoly}=\mathrm{BQP/poly}$? Rada pro vstupy délky $n$ smí záviset pouze na $n$: vlevo je to stav na $\operatorname{poly}(n)$ qubitech, vpravo $\operatorname{poly}(n)$ klasických bitů. Výpočet musí fungovat pro každý vstup dané délky.',
    'Rada není svědek volený podle konkrétního vstupu. Měří neuniformní informační zdroj dostupný celé délkové vrstvě.',
    'Odděluje dva základní způsoby ukládání pomocné informace pro výpočet. Je to jiná otázka než QMA versus QCMA.',
    [p('2026-02-10','Zdroj konstruuje první separaci těchto poradních tříd pomocí standardního klasického orákula. Pro třídy bez orákula separaci netvrdí.','qadvice')],[qadvice],criterion='models')

andpaper=ref('andpaper','Quantum–Classical Equivalence for AND-Functions','Sreejata Bhattacharya; Farzan Byr amji; Arkadev Chattopadhyay; Yogesh Dahiya; Shachar Lovett'.replace('Byr amji','Byramji'),2026,'https://eccc.weizmann.ac.il/report/2026/013/','Introduction; communication model, PDF p. 9; revision 1','https://eccc.weizmann.ac.il/report/2026/013/revision/1/download/')
add('total_quantum_communication','Polynomiální vztah klasické a kvantové komunikace pro totální funkce','Communication complexity',
    r'Pro každou totální booleovskou funkci $F:X\times Y\to\{0,1\}$ označme $R^{cc}_{1/3}(F)$ veřejně randomizovanou komunikační složitost a $Q^{cc,*}_{1/3}(F)$ kvantovou složitost s neomezeným sdíleným provázáním. Existuje univerzální polynom $p$ takový, že $R^{cc}_{1/3}(F)\le p(Q^{cc,*}_{1/3}(F))$ pro všechny takové $F$?',
    'U částečných funkcí může být kvantová úspora exponenciální. Požadavek správnosti na všech dvojicích vstupů může situaci zásadně měnit.',
    'Vymezuje kvantovou výhodu v jednom z nejčistších distribuovaných modelů, bez omezení lokálního výpočtu.',
    [p('2026',r'Pro $F=f\circ\mathrm{AND}_2$ zdroj dokazuje $D^{cc}(F)=O((Q^{cc,*}(F))^7\log^2n)$. Polylogaritmický faktor a omezení na AND-složení brání použít tento výsledek jako řešení obecné otázky.','andpaper')],[andpaper],criterion='resources')

steinke=ref('steinke','Open Problem: Selection via Low-Sensitivity Queries','Thomas Steinke',2025,'https://differentialprivacy.org/open-problem-selection/','Problems 1–2')
selection=ref('selection','Nearly-Optimal Private Selection via Gaussian Mechanism','Ethan Leeman; Pasin Manurangsi',2026,'https://doi.org/10.4230/LIPIcs.FORC.2026.4','Definitions 1–2; Theorem 5; §1.2','https://drops.dagstuhl.de/storage/00lipics/lipics-vol368-forc2026/LIPIcs.FORC.2026.4/LIPIcs.FORC.2026.4.pdf')
add('private_selection_gaussian','Optimální soukromý výběr jen pomocí gaussovských dotazů','Differential privacy',
    r'Pro konečnou množinu $Y$ jsou dány veřejné ztráty $\ell_y$ s citlivostí 1 vůči změně jednoho záznamu v databázi $X$. Přístup k $X$ je možný jen adaptivními dotazy $q_i(X)+N(0,1/(2\rho_i))$, s citlivostí $q_i$ nejvýše 1 a $\sum_i\rho_i\le\rho$. Lze vrátit $\hat y$ s $\mathbb E[\ell_{\hat y}(X)]-\min_y\ell_y(X)=O(\log|Y|/\sqrt\rho)$?',
    'Exponenciální mechanismus dosahuje požadované chyby při přímém přístupu k datům. Otázka testuje, zda lze jeho výkon plně získat jen přidáváním šumu.',
    'Rozhoduje o ekvivalenci dvou základních primitiv DP. Zbylá polyloglogaritmická mezera má konkrétní význam: přesná redukce by zachovala optimální užitečnost.',
    [p('2025-05-02',r'Výchozí stromový postup má chybu $O(\log^{3/2}|Y|/\sqrt\rho)$.','steinke'),p('FORC 2026',r'Nový algoritmus zlepšuje chybu na $O(\log|Y|(\log\log|Y|)^{11}/\sqrt\rho)$. §1.2 výslovně ponechává odstranění faktoru v $\log\log|Y|$ otevřené.','selection')],[selection,steinke],criterion='tightness')

add('private_selection_laplace','Optimální soukromý výběr jen pomocí Laplaceova šumu','Differential privacy',
    r'Za stejného modelu konečného výběru s 1-citlivými ztrátami smí algoritmus položit $k$ adaptivních 1-citlivých dotazů. Dostává pouze $q_i(X)+\mathrm{Lap}(k)$, kde $k$ je měřítko rozdělení. Lze pro libovolné ztráty zaručit očekávanou nadbytečnou ztrátu $O(\log|Y|)$? Počet dotazů může algoritmus zvolit.',
    'Laplaceovský model odpovídá základní kompozici čistého soukromí. Silnější koncentrace gaussovského šumu nelze automaticky přenést.',
    'Cena čistého soukromí je strukturální rozdíl modelu, nikoli uměle vytvořená změna konstanty. Určuje rozsah použitelnosti univerzálního primitiva přidávání šumu.',
    [p('2025',r'Stromový algoritmus dává chybu $O(\log^2|Y|)$.','steinke'),p('FORC 2026','Autoři vysvětlují, proč jejich téměř optimální gaussovská metoda nedává ostrou mez pro Laplaceův model; otázku ponechávají otevřenou.','selection')],[steinke,selection],criterion='models')

dpPAC=ref('dppac','Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?','Kobbi Nissim; Uri Stemmer; Eliad Tsfadia',2026,'https://proceedings.mlr.press/v336/nissim26a.html','Open Questions 1–2; Theorems 2–3','https://raw.githubusercontent.com/mlresearch/v336/main/assets/nissim26a/nissim26a.pdf#page=3')
add('private_pac_characterization','Kombinatorická charakterizace vzorkové složitosti soukromého PAC učení','Differential privacy',
    r'Určete strukturální parametr třídy konceptů $C$, který až na přesně vymezené faktory charakterizuje počet vzorků pro realizovatelné $(\varepsilon,\delta)$-DP PAC učení. Zdroj fixuje konstantní přesnost, spolehlivost a $\varepsilon$; $\delta$ má být výrazně menší než převrácený počet vzorků. Konkrétní cíl je obecná horní mez $\operatorname{poly}(\mathrm{VC}(C),\log^*\mathrm{LD}(C))$.',
    r'VC dimenze popisuje neprivátní učení. Konečnost Littlestoneovy dimenze $\mathrm{LD}$ charakterizuje existenci soukromého učení, ale sama neřeší jeho optimální počet vzorků.',
    'Hledá analogii jednoho ze základních charakterizačních teorémů učení pod požadavkem soukromí.',
    [p('COLT 2026',r'Survey uvádí dolní mez $\Omega(\mathrm{VC}+\log^*\mathrm{LD})$ a horní $\min\{O(\log|C|),\widetilde O(\mathrm{LD}^5)\}$. Pro $\mathrm{VC}=1$ je situace téměř určena; obecná mezera zůstává.','dppac')],[dpPAC],criterion='characterization',existing_id='TCS-0506')

pessiland=ref('pessiland','A Sharp Characterization of Pessiland','Shuichi Hirahara; Mikito Nanashima',2026,'https://eccc.weizmann.ac.il/report/2026/052/','Revision 1, 23 June 2026','https://eccc.weizmann.ac.il/report/2026/052/revision/1/download/')
add('pessiland','Implikuje průměrná těžkost NP jednosměrné funkce?','Average-case complexity',
    r'Předpokládejme, že existuje problém v NP a polynomiálně vzorkovatelná distribuce, na níž není rozhodování efektivní v průměrném případě v distribučním smyslu zdroje. Musí existovat polynomiálně vyčíslitelná funkce $f$, pro kterou žádný PPT algoritmus neinvertuje $f(U_n)$ s nezanedbatelnou pravděpodobností? Neúspěch této implikace by dovoloval svět zvaný Pessiland.',
    'Těžkost rozhodování na běžných vstupech a těžkost nalezení předobrazu jsou odlišné požadavky. Pouhý předpoklad P ≠ NP je ještě slabší a představuje jinou, již evidovanou otázku.',
    'Určuje, zda samotná distribuční těžkost stačí pro základní kryptografii. Je to hlavní most mezi average-case complexity a kryptografickými konstrukcemi.',
    [p('2026-06-23',r'Revidovaná práce charakterizuje zbývající překážku mezerou mezi aproximačními faktory $\ell^{1-o(1)}$ a $O(\ell)$ v úloze minimální délky popisu při agnostickém učení. Parametr $\ell$ je advice complexity vzorkování. Původní dubnová verze má jiné kvantitativní tvrzení.','pessiland')],[pessiland],criterion='reductions')

lpn=ref('lpn','Towards Worst-case Hardness for Low-Noise LPN','Divesh Aggarwal; Rishav Gupta; Hai Hoang Nguyen; Kel Zin Tan; Prashant Nalini Vasudevan',2026,'https://eccc.weizmann.ac.il/report/2026/095/','Revision 1, 8 September 2026','https://eccc.weizmann.ac.il/report/2026/095/revision/1/download/')
add('lpn_worst_case','Opřít nízkošumové LPN o běžnou worst-case těžkost','Cryptography',
    r'LPN poskytuje vzorky $(a,\langle a,s\rangle\oplus e)$, kde $a\sim U(\mathbb F_2^n)$, tajemství $s\in\mathbb F_2^n$ je pevné a $e\sim\mathrm{Ber}(\eta)$. Pro nízké šumy, například $\eta=n^{-1/2}$, hledejte redukci z přirozené worst-case úlohy kódování na průměrnou těžkost LPN, která nevyžaduje současnou těžkost dekódování a rozlišování šumových slov duálního kódu.',
    'U LWE existují silné vazby na mřížky. Pro LPN je obtížné získat obdobný základ při šumu vhodném pro kryptografické aplikace.',
    'Základní bezpečnostní předpoklad by dostal vysvětlení přes nezávisle studovanou těžkost. Konkrétní mezera v nové redukci ukazuje, který další předpoklad je třeba odstranit.',
    [p('2026-09-08',r'Revize dává redukci pro $\eta=n^{-\alpha}$, každé konstantní $\alpha<1$, ze současné worst-case těžkosti dvou úloh na kódu a jeho duálu. Jde o skutečný posun oproti dřívějším redukcím s téměř polovičním šumem; jednopředpokladový cíl zůstává silnější.','lpn')],[lpn],criterion='assumptions')

ip=ref('ip','Towards a Doubly Efficient IP=PSPACE','Liyan Chen; Matthew M. Hong; Yael Tauman Kalai; Zoe Xi',2026,'https://eccc.weizmann.ac.il/report/2026/102/','Revision 1; Introduction','https://eccc.weizmann.ac.il/report/2026/102/revision/1/download/')
add('doubly_efficient_ip','Dvojitě efektivní IP = PSPACE v plném časovém rozsahu','Proof complexity and logic',
    r'Nechť jazyk rozhoduje stroj v polynomiálním prostoru a čase $T(n)$. Má interaktivní důkaz, jehož verifikátor běží v $\operatorname{poly}(n)$ a poctivý dokazovatel v $\operatorname{poly}(T(n))$, s konstantní completeness–soundness mezerou? Zvukovost musí platit proti libovolně mocnému podvodnému dokazovateli. Cíl má platit i za kvazipolynomiálním rozsahem $T$.',
    'Rovnost IP = PSPACE sama negarantuje, že vytvoření důkazu bude stát jen polynomiální násobek původního výpočtu.',
    'Testuje, zda lze dlouhý prostorově úsporný výpočet ověřovat bez skryté nepřiměřené práce na straně poctivého dokazovatele.',
    [p('FOCS 2025',r'Předchozí dosažený rozsah citovaný novou prací byl $T(n)=n^{O(\sqrt{\log n/\log\log n})}$.','ip'),p('2026-06-21',r'Nová přímá konstrukce rozšiřuje rozsah na $T(n)=n^{O(\log n)}$. Obecný časový rozsah tím pokryt není.','ip')],[ip],criterion='resources')

add('rs_product_expansion','Vícedimenzionální produktová expanze strukturovaných Reed–Solomonových kódů','Coding and information theory',
    r'Pro pevné $k\ge3$ a $\varepsilon>0$ uvažujme RS kódy $C_i$ nad prvočíselným tělesem $\mathbb F_q$, vyhodnocené na multiplikativních podgrupách párově nesoudělných řádů, s rychlostí menší než $1-\varepsilon$. Je jejich $k$-tice $\rho$-produktově expandující pro $\rho=\rho(k,\varepsilon)>0$ nezávislé na délkách? Přesná norma a rozklad v $k$ dimenzích jsou v definici 4.1 zdroje.',
    r'Ve dvou dimenzích požadavek říká: vhodný rozklad $M=M_1+M_2$ na sloupcová a řádková kódová slova splňuje $|\mathrm{supp}(M)|\ge\rho(n_1|M_1|_{\mathrm{col}}+n_2|M_2|_{\mathrm{row}})$.',
    'Je to konkrétní strukturální překážka konstrukce private PCP a kvantových kódů podporujících násobení; podmínky domněnky odpovídají tomuto použití.',
    [p('2026-08-19','Zdroj prokazuje případ k = 2. Vyšší dimenze označuje jako domněnku; uvádí také kandidátní důkaz vytvořený AI, který autoři neověřili. Takový kandidát není v katalogu pokládán za vyřešení.','privatepcp')],[privatepcp],criterion='construction')
