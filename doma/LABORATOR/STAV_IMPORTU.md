# Stav importu balíčků do LABORATOR

Aktualizováno: 2026-10-31

## Nahráno do repozitáře

- Katalog `index.html`, hlavní `README.md` a tento stav importu.
- Nezávislé hodnocení v `HODNOCENI_NASTROJU.md`.
- Dokumentace použití a limitů pro hlavní nástroje a starší varianty.
- Gemini pilot: `arc-mys-gemini/arc_mys_experiment.py` a `requirements.txt`.
- Slepý test: `arc-mys-slepy-test/prepare_blind_set.py`, `evaluate_offline.py`, `run_blind_gemini.py` a `requirements.txt`.
- Lokální ARC evidence: `arc-mys-lokalni/app.py`, demo JSON, `README.txt` a `start_windows.bat`.
- CASMI inventura: `casmi-inventura/inventura_dat.py`.

## Původní zdrojové soubory, které ještě chybí

Tyto soubory jsou v dodaných ZIP balíčcích, ale v cílové složce zatím nejsou přeneseny:

- `modelove-pracoviste/index.html`
- `laborator-prototyp/index.html`
- `portal-zakladni/index.html`
- `arc-lab/index.html`
- `laborator-vztahu/index.html`
- `mys-lab-environment/index.html`, `ui/style.css`, `ui/app.js`, `engine/run_experiment.py`, ukázková JSON konfigurace a obrazové/textové materiály
- `casmi/mys_casmi.py)
- zdrojové skripty starších Gemini, slepého testu 120 a relačního pilotu v2
- obrazové materiály přibalené k laboratorním a ARC pilotním balíčkům

Dokumentace je popis použití a omezení, nenahrazuje chybějící zdrojový kód. Dokud uvedené soubory nejsou nahrány, nepovažuj jejich HTML aplikace nebo skripty za dostupné v repozitáři jen proto, že existuje README.

## Co je potřeba udělat při dokončení importu

1. Přenést původní zdrojové soubory z příslušných ZIPů bez změny jejich obsahu.
2. Zachovat odlišné varianty jako samostatné složky, pokud se liší chováním nebo metodou.
3. Opravit relativní cesty podle nové struktury v `doma/LABORATOR/`.
4. Otevřít každé HTML přes GitHub Pages a ověřit načítání dat, export/import a interní odkazy.
5. Spustit Python skripty na malých demo datech a ověřit chybové stavy.
6. Teprve po skutečném testu označit nástroj jako funkční.

## Důležité rozdíly

- Gemini skripty vyžadují internet a API klíč, takže nejsou offline soutěžním řešením.
- Slepý evaluator může běžet offline, ale generování predikcí vyžaduje konkrétní model nebo API.
- Statické ARC mřížky nejsou totéž co interaktivní ARC-AGI-3.
- CASMI/MS-MS je oddělená chemická úloha.
- Žádný výsledek není naměřený jen tím, že byl skript nahrán.
- Nikdy neukládej API klíče, neveřejné testy ani answer keys do veřejného repozitáře.
