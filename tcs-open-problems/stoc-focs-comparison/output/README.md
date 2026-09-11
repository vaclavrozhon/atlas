**Datum**

2026-09-09

**Období**

Posledních pět dokončených ročníků každé konference: STOC 2022–2026; FOCS 2021–2025. Jde o označení ročníků, ne shodné kalendářní okno.

**Jednotky**

Konference: publikované výzkumné články. Katalog: záznamy indexu otevřených otázek. Srovnávají se podíly, nikoli absolutní množství problémů.

**Korpus**

1 546 článků s DOI a abstraktem z oficiálních metadat ACM/IEEE. STOC 907; FOCS 639. Vyloučeny dvě keynote položky STOC 2024 a veškerá front/back matter.

**Katalog**

4 695 záznamů ve 43 oblastech. Zachováno původní zařazení. Velká část katalogu vznikla automatickou extrakcí; nebyl zde znovu ověřován aktuální otevřený status ani přetříděn.

**Třídění**

Vlastní orientační zařazení do jedné hlavní oblasti; nejde o oficiální taxonomii konferencí. Kandidátní pravidla doplnila kontrola názvů všech 1 546 článků modelem; u 43 vybraných nejednoznačných případů byla provedena kontrola abstraktu. Žádný nezávislý expertní audit.

**Srovnatelnost třídění**

Názvy 43 kategorií jsou stejné jako v katalogu. Katalog a články byly tříděny odlišně; rozdíly proto obsahují i vliv metodiky, zejména u obecné zbytkové kategorie a mezi překrývajícími se obory.

**Překryvy**

Každý článek se počítá jednou. Kvantová kryptografie se typicky řadí do kryptografie, kvantové kódy do kvantového počítání. Nula znamená žádný článek s tímto hlavním štítkem; nevylučuje přítomnost tématu.

**Konvence oblastí**

Enumerace a počítání zahrnuje diskrétní sampling a mixing související s počítáním. Spojité log-concave sampling patří k optimalizaci. Důkazová složitost zahrnuje PCP/IOP a některé SoS lower bounds. Average-case zahrnuje planted modely a výpočetní prahy; statistické odhadování zpravidla teorii učení.

**Výpočet**

Podíl oblasti = počet jejích článků / 1 546. Katalogový podíl = počet jejích záznamů / 4 695. Rozdíl je katalog minus články v procentních bodech. Ročníky se váží počtem publikovaných článků.

**Poměr**

Poměr zastoupení = katalogový podíl / konferenční podíl. Pro nulu v konferenčním podílu je poměr nevyplněný. Očekávané počty při konferenčních podílech jsou pouze ilustrace jiné skladby, nikoli doporučená kvóta.

**Citlivost období**

Soubor common_years_2022_2025.csv opakuje výpočet pro shodné ročníky 2022–2025 obou konferencí (1 218 článků).

**Interpretace**

STOC/FOCS představují publikační profil dvou selektivních konferencí, nikoli reprezentativní vzorek celé TCS nebo míru významu oborů. Katalog čerpá i ze specializovaných konferencí, knih a sbírek.

**Kontrola zdrojů**

FOCS 2025 accepted-papers-with-abstracts obsahoval starý seznam 2024 a nebyl použit. Čerpáno z vlastních IEEE proceedings metadat. FOCS 2023 má 142 publikovaných článků; předběžný seznam přijatých článků není jednotkou této statistiky.

**Stejné názvy**

Dva články STOC 2022 s názvem Hypercontractivity on high dimensional expanders mají různé autory a DOI, proto jsou dvěma položkami.

**Reprodukce**

Z pracovní složky postupně spustit parse.py, abstract_review.py, review.py, classify.py, build.py. Skripty používají původní cache; pro obnovení cache slouží fetch.py. Existující katalog se neupravuje.