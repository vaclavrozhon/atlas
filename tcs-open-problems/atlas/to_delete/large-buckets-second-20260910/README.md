# Druhý průchod velkých kategorií — 10. září 2026

**2 134 → 1 591 kandidátů; dalších 543 předběžných vyřazení.**

Uživatel požadoval dalších 500–1000 vyřazení a každou položku jednotlivě vysvětlit v konverzaci. Všech 543 položek bylo postupně vypsáno s vlastním konkrétním důvodem. Trvalý úplný seznam je v [DECISIONS.md](DECISIONS.md).

Průchod znovu přečetl uložené otázky a zdrojová témata všech 2 134 zbývajících velkých kandidátů. Rozhoduje samostatný význam cíle: hlavní bariéra versus pomocná míra, konkrétní metoda, restrikční varianta, neurčený program nebo další formulace již zastoupené otázky. Není použit automatický bodový práh ani kvóta vyřazení v kategorii. Neúplný zápis sám není důvodem odmítnout rozpoznatelný zásadní problém. Jde o redakční úsudky a předběžné přesuny; nejde o čerstvé čtení každého článku, kontrolu současné otevřenosti ani konečný výběr 50 položek na kategorii.

| Kategorie | Před | Vyřazeno | Zbývá |
|---|---:|---:|---:|
| Quantum computation | 185 | 57 | 128 |
| Computational geometry and metric spaces | 312 | 100 | 212 |
| Computational complexity | 183 | 45 | 138 |
| Algorithms & data structures | 351 | 80 | 271 |
| Learning theory | 175 | 48 | 127 |
| Cryptography | 88 | 20 | 68 |
| Distributed, parallel and sublinear algorithms | 223 | 51 | 172 |
| Automata and formal languages | 195 | 46 | 149 |
| Semantics, logic and verification | 229 | 49 | 180 |
| Optimization and numerics | 193 | 47 | 146 |
| **Celkem** | **2134** | **543** | **1591** |

Předchozí velký archiv (2 069) a malý archiv (1 835) zůstávají samostatně aktivní. Malých aktivních kandidátů zůstává 1 104, všech aktivních kandidátů 2 695. Všech 7 156 uložených ID, formulace, zdroje, stavové informace a poznámky zůstávají zachované. Žádná individuálně dokončená karta ani schválený fundamentální návrh nebyl tímto průchodem vyřazen.

- `records.json`: úplné aktuální karty těsně před aplikací tohoto průchodu.
- `catalog-before.json.gz`: úplný katalog před přesunem, včetně starších archivů.
- `manifest.json`: živé rozhodnutí, důvod, původní bucket, pořadí a vazby na ponechané cíle.
- `decisions.csv`: všechna jednotlivá rozhodnutí, původní otázka i zdroj.
- `all-reviewed.csv`: všech 2 134 vstupních kandidátů a výsledek tohoto průchodu.
- `validation.json`: kontrola zachování, obnovy, publikace a prohlížeče.

## Obnovení

Spouštějte z adresáře atlasu:

```bash
python3 to_delete/large-buckets-second-20260910/restore.py --dry-run TCS-0032
python3 to_delete/large-buckets-second-20260910/restore.py TCS-0032
python3 to_delete/large-buckets-second-20260910/restore.py --all
```

Obnova mění stav na `retained` a publikuje pod společným zámkem. Nepřepisuje novější text starým snapshotem a neobnovuje jiné vyřazovací průchody. Ve čtečce jsou položky nadále dostupné přes Archive a přímá stabilní ID.

## Zachycená oprava zařazení

TCS-6572 (polynomiální simplexové pravidlo) byl během souběžné individuální recenze automaticky přesunut z optimalizace do Beyond worst-case kvůli smoothed-analysis referenci. Explicitní override obnovuje původní schválenou kategorii podle nejhoršího případu v otázce. Tabulka počítá původních 2 134 posuzovaných kandidátů; bezprostřední publikační snapshot již zachycuje tuto chybu (2 133 velkých a 1 105 malých). Snapshoty zůstávají beze změny, oprava je v manifestu oddělená od 543 vyřazení.
