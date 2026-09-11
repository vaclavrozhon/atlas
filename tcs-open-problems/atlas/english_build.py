"""Apply the English-only preference to the initial builder copy."""
from pathlib import Path
f=Path(__file__).parent/'build.py'
d={
'Význam této konkrétní otázky zatím nebyl samostatně posouzen. ':'The significance of this particular question has not yet been individually assessed. ',
'Převzato z předchozího katalogu. Aktuální otevřenost není doložena novou rešerší.':'Imported from the previous catalogue. Current open status has not been established by a new review.',
'Původní indexový záznam; nejde o hotovou podrobnou kartu. Definice modelu, samostatná formalizace a vývoj výsledků čekají na dopracování.':'Legacy index record, not a completed research card. Model definitions, a self-contained statement, and a progress review remain to be written.',
'Krátká citace otázky je níže. ':'A short source quotation appears below. ',
'Záznam zachycuje otázku ze zdroje; samostatné úplné zadání zatím není dopracováno. ':'This record locates a question in the source; a complete self-contained statement has not yet been written. ',
'Přesné definice použitého modelu jsou na odkazované stránce článku.':'The model definitions are on the linked page of the paper.',
'Citace je zkrácená; chybějící kvantifikátory a parametry je nutné číst v odkazovaném originálu.':'The quotation is truncated. Missing quantifiers and parameters must be read in the linked original.',
'Celá vybraná věta autorů':'Complete selected source sentence',
'Zkrácený úryvek autorů (nejvýše 25 slov)':'Truncated source excerpt (at most 25 words)',
'PDF str.':'PDF p.',
'Konkrétní výchozí model:':'Source of the specific model:',
'Lokalizace otázky:':'Question location:',
'Otázka doložena ve zdroji z roku ':'Question recorded in a source from ',
'; navazující výsledky a dnešní otevřenost nejsou jednotlivě ověřeny.':'; subsequent results and present open status have not been individually checked.',
'V této práci je doložena otázka označená autory jako otevřená nebo domněnka. Tento bod datuje formulaci, nikoli nově ověřenou horní či dolní mez.':'The source contains an explicitly unresolved question or conjecture. This entry dates the formulation; it is not a newly verified upper or lower bound.',
'Zdrojová karta, nikoli dokončená odborná rešerše. Tematické zařazení a důvod výběru jsou heuristické. Chybí individuální výklad modelu, specifické zdůvodnění významu a ověření novějších výsledků.':'Source note, not a completed research review. Topic and selection criterion are heuristic. An individual model explanation, problem-specific importance assessment, and review of later results remain to be completed.',
'Podrobné karty mají jednotlivě napsané zadání, kontext, důvod významu a doložené výsledky. Zdrojové karty jsou průběžné rešeršní záznamy a nesplňují ještě stejnou úroveň. Původní index zůstává pro dohledatelnost.':'Detailed cards have individually written statements, context, significance, and documented results. Source notes are unfinished research records and do not yet meet that standard. The legacy index is retained for traceability.',
'Otevřená podle zdroje znamená pouze otevřená k datu daného zdroje. Datum sestavení katalogu 10. 9. 2026 není důkazem, že otázka dosud nemá řešení. U starých úryvků mohou chybět podmínky nebo novější výsledek.':'Open in the source means open at the date of that source. The build date, 10 September 2026, does not establish current open status. Old excerpts may omit conditions or subsequent results.',
'Nové hledání zvýhodňuje oblasti slabě zastoupené oproti posledním pěti uskutečněným STOC a FOCS. Konferenční podíly jsou vodítko pro sběr; počty článků a počty otevřených problémů nejsou stejná veličina.':'New searches prioritize areas underrepresented relative to the last five completed STOC and FOCS editions. Conference shares guide collection; paper counts and open-problem counts are different quantities.',
'Jako důvod výběru sledujeme sílu modelu, nezbytné zdroje, ostrou mez, strukturální charakterizaci, explicitní konstrukci nebo minimální předpoklady. U zdrojových karet jde o heuristický filtr; u podrobných karet o individuální vysvětlení.':'Selection considers model power, necessary resources, sharp bounds, structural characterizations, explicit constructions, and minimal assumptions. Source notes use a heuristic screen; detailed cards give an individual explanation.',
'Automatický výběr připouští nejvýše jednu novou kartu na název práce; shodné formulace a blízké duplicity ze stejného zdroje vyřazuje. Sémantická deduplikace celého souboru ještě není úplná.':'Automatic selection allows at most one new card per paper title and rejects identical formulations and close duplicates within a source. Collection-wide semantic deduplication remains incomplete.',
'Krátké citace zůstávají v jazyce zdroje. Novější související literatura, pokud je uvedena, je pomůcka pro další rešerši a není sama dokladem vyřešení. Vlastní poznámky a uložené karty se ukládají lokálně v prohlížeči.':'Short quotations retain the source language. Later related literature, where listed, is a research aid rather than evidence of resolution. Personal notes and saved cards are stored locally in your browser.'
}
s=f.read_text()
for a,b in d.items():s=s.replace(a,b)
f.write_text(s)
