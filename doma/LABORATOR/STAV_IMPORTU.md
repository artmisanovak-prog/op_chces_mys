# Stav importu balíčků do LABORATOR

Aktualizováno: 2026-10-31

## Nahráno do repozitáře

- `index.html`: vyhledatelný katalog nástrojů, jejich zamýšleného použití, silných stránek a otevřených problémů.
- `README.md`: přehled pracovního prostoru a provozní rozdíly.
- Samostatné popisy pro modelové pracoviště, laboratorní prototyp, základní portál, ARC Lab, Gemini pilot, slepý test, lokální ARC evidenci, CASMI baseline, CASMI inventuru, MOUSE Lab Environment, relační pilot v2 a starší varianty.
- `arc-mys-gemini/arc_mys_experiment.py` a `requirements.txt`.
- `arc-mys-slepy-test/prepare_blind_set.py`, `evaluate_offline.py`, `run_blind_gemini.py` a `requirements.txt`.

## Co ještě není importováno

Původní HTML zdrojové soubory pro `modelove-pracoviste`, `laborator-prototyp`, `portal-zakladni`, `arc-lab` a `mys-lab-environment` zatím nebyly přeneseny z ZIPů. Totéž platí pro některé další Python zdroje a ukázková data. Jejich popisné README tedy zatím slouží jako dokumentace návrhu, ne jako potvrzení, že je v této složce k dispozici celý spustitelný balíček.

## Proč je to uvedeno zvlášť

Nechci vytvářet dojem, že lze otevřít nástroj, když jeho zdrojový soubor v repozitáři ještě není. Katalogové odkazy vedou na existující dokumentaci; chybějící zdroje se mají doplnit z původních ZIPů, nikoli nahradit falešnými soubory nebo domyšlenými implementacemi.

## Kontroly před použitím

- Gemini skripty vyžadují `google-genai` a klíč v proměnné prostředí / Kaggle Secrets.
- `prepare_blind_set.py` vybírá úlohy, jejichž testovací výstup je v lokálním zdrojovém JSON přítomen; nepoužívej jej přímo na veřejný test bez výstupů.
- `evaluate_offline.py` očekává klíč odpovědí a predikce ve specifickém JSON/JSONL formátu.
- Žádný výsledek není naměřený jen tím, že byl skript nahrán.
