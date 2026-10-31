# ARC + MYŠ: Gemini pilot

## K čemu slouží
Skriptový pilot pro srovnání několika podmínek při řešení statických ARC úloh s modelem dostupným přes Gemini API. Typicky se porovnává základní model s variantami, které dostávají jiné instrukce nebo materiál související s MYŠ.

## Jak ho vyzkoušet
Přečti nejprve skript a seznam požadovaných knihoven. Nastav API klíč jako proměnnou prostředí nebo bezpečný secret, nikdy přímo do veřejného souboru. Začni malým vzorkem a ověř, že ukládá surové odpovědi, chyby a výsledky pro každou podmínku.

## Co je na tom užitečné
- Umožňuje formulovat srovnání mezi podmínkami místo spoléhání na jednotlivé příklady.
- API model není nutné stahovat a provozovat lokálně.
- Skript lze upravit pro opakovatelné pokusy.

## Limity
- Vyžaduje síť a API klíč, proto není offline soutěžním řešením.
- Výsledky závisí na modelu, verzi, promptu a nastavení API.
- Stejné úlohy a srovnatelné limity musí dostat všechny podmínky.
- Statické ARC JSON úlohy nejsou interaktivní ARC-AGI-3.
- Pilotní výsledek bez opakování a kontroly chyb nelze prezentovat jako obecný důkaz.
