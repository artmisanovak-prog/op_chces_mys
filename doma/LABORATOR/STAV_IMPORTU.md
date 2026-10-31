# Stav importu balíčků do LABORATOR

Aktualizováno: 2026-10-31

## Nahráno do repozitáře

- Katalog `index.html` a přehled `README.md`.
- Nezávislé hodnocení nástrojů v `HODNOCENI_NASTROJU.md`.
- Popisy jednotlivých směrů a provozní limity v samostatných README.
- Gemini pilot: `arc-mys-gemini/arc_mys_experiment.py` a `requirements.txt`.
- Slepý test: `arc-mys-slepy-test/prepare_blind_set.py`, `evaluate_offline.py`, `run_blind_gemini.py` a `requirements.txt`.

## Původní zdrojové soubory, které ještě chybí v repozitáři

Tyto soubory jsou v dodaných ZIP balíčcích, ale v cílové složce zatím nejsou přeneseny:

- `modelove-pracoviste/index.html`
- `laborator-prototyp/index.html`
- `portal-zakladni/index.html`
- `arc-lab/index.html`
- `laborator-vztahu/index.html`
- `mys-lab-environment/index.html`, `ui/style.css`, `ui/app.js`, `engine/run_experiment.py`, ukázková JSON konfigurace a obrazové/textové materiály
- `arc-mys-lokalni/app.py`, ukázková data a spouštěcí soubor
- `casmi/mys_casmi.py` a `casmi-inventura/inventura_dat.py`
- zdrojové skripty starších Gemini, slepého testu 120 a relačního pilotu v2
- obrazové materiály přibalené k laboratorním a ARC pilotním balíčkům

Dokumentace je užitečný popis záměru a omezení, ale nenahrazuje chybějící zdrojový kód. Dokud tyto soubory nejsou nahrány, nepovažuj odkazy na samotné aplikace za potvrzené spustitelné nástroje.

## Co je potřeba udělat při dokončení importu

1. Přenést původní zdrojové soubory z příslušných ZIPů bez změny jejich obsahu.
2. Zachovat odlišné varianty jako samostatné složky, pokud se liší chováním nebo experimentální metodou.
3. Opravit relativní cesty podle nové struktury v `doma/LABORATOR/`.
4. Otevřít každé HTML přes GitHub Pages a ověřit načítání dat, export/import a interní odkazy.
5. Spustit Python skripty na malých demo datech a ověřit chybové stavy.
6. Teprve po skutečném testu označit nástroj jako funkční.

## Důležité rozdíly

- Gemini skripty vyžadují internet a API klíč, takže nejsou offline soutěžním řešením.
- Slepý evaluator může běžet offline, ale samotné generování predikcí potřebuje konkrétní model nebo API.
- Statické ARC mřížky nejsou totéž co interaktivní ARC-AGI-3.
- CASMI/MS-MS je oddělená chemická úloha.
- Žádný výsledek není naměřený jen tím, že byl skript nahrán.
- Nikdy neukládej API klíče, neveřejné testy ani answer keys do veřejného repozitáře.
