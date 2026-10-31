# CASMI CPU baseline

## K čemu slouží
Samostatný experimentální nástroj pro CASMI/MS-MS: pracuje s chemickými spektry a využívá retrieval/podobnostní přístup jako referenční baseline. Jde o odlišnou doménu než ARC.

## Jak ho vyzkoušet
Přečti skript, zjisti očekávaný formát spekter a nejprve spusť malý test s daty, jejichž správné přiřazení je známé. Uchovej oddělený testovací vzorek.

## Silné stránky
- CPU přístup může být dostupnější než velký model na GPU.
- Baseline dává referenční bod pro porovnání složitější metody.
- Chemická doména může posloužit jako samostatný test přenositelnosti metod, ale jen s odpovídajícími daty a metrikami.

## Limity
- Retrieval není de-novo generování molekuly.
- Bez nezávisle označeného testu není doložená přesnost.
- Výsledek v CASMI se nesmí zaměňovat za důkaz schopností na ARC nebo obecného uvažování.
