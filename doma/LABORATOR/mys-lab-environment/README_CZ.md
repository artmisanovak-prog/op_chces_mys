# MOUSE Lab Environment

## K čemu slouží
Experimentální běhové prostředí, které odděluje konfigurační soubor pokusu, materiály, běh skriptu a uložené výsledky. Experiment lze popsat JSON konfigurací a výstupy ukládat strojově čitelně.

## Jak ho vyzkoušet
Začni souborem `experiment.example.json` a dokumentací. Ověř, jaké modelové backendy jsou skutečně implementované. Spusť nejprve malý běh na několika úlohách a zkontroluj JSONL/summary výstupy. Pokud backend vyžaduje API, jde o online experiment; offline běh funguje pouze s lokálně dostupným backendem a daty.

## Silné stránky
- Konfigurace experimentu je oddělena od kódu.
- Ukládání výsledků umožňuje pozdější srovnání a audit.
- Kontextové materiály mohou být spravované samostatně.

## Otevřené otázky
- Přítomnost konfiguračního pole neznamená, že každý modelový backend funguje.
- Nutno ověřit obnovení přerušeného běhu, validaci výstupu a chování při chybách.
- Není to automaticky oficiální ARC-AGI-3 agent ani hotová soutěžní implementace.
