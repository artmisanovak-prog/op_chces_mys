# ARC + MOUSE: relační pilot v2

## K čemu slouží
Pilotní skript pro srovnání několika podmínek na statických ARC JSON úlohách. Rozlišuje například samotný model, relačně formulované instrukce, přidání textového kontextu a přidání ilustrací. Cílem je zjistit, zda konkrétní přidaná informace mění výkon, ne předem potvrdit účinnost MOUSE.

## Jak ho vyzkoušet
Přečti skript a konfiguraci, ověř formát vstupních úloh a oddělení testovacích odpovědí. Spusť nejprve 3 až 5 úloh pro kontrolu technického toku. Teprve po úspěšné kontrole spusť plánovaný vzorek. Ulož model, datum, prompt, parametry, surové odpovědi, chyby API a skóre.

## Silné stránky
- Více podmínek dovoluje rozlišovat přínos instrukce, textu a obrázků.
- Offline vyhodnocení snižuje riziko hodnocení podle dojmu.
- Pilot je relativně malý, a proto může být vhodný k odhalení problémů v metodice.

## Limity
- Jde o statické ARC úlohy, ne o interaktivní ARC-AGI-3.
- Malý vzorek má vysokou nejistotu; skóre se nesmí zobecňovat.
- API varianta vyžaduje internet a tajný klíč.
- Je nutné zkontrolovat, zda jsou všechny podmínky srovnatelné z hlediska tokenů, vstupů a opakování.
