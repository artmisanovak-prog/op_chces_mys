ARC Lab starter
Jednostránkový frontend pro ovládání dvou vzdálených modelových endpointů, ARC JSON/ZIP import, chat a A/B porovnání.

Použití
Nahraj index.html do GitHub repozitáře.
Zapni GitHub Pages v Settings → Pages, nebo otevři soubor lokálně.
V aplikaci nastav inference URL a případně chat URL pro Model A i B.
Nahraj ARC JSON nebo ZIP s JSON soubory.
Spusť A/B test a exportuj výsledky CSV.
Omezení a API kontrakt
Toto je frontend. Modelové váhy se do něj nenahrávají a nespouštějí. Modely mohou běžet na vzdálených serverech. Endpoint musí povolit CORS.

Inference POST JSON: {"task_id":"...","task":{"train":[],"test":[]},"include_train":true,"prompt":"..."} Odpověď pro jeden test: {"prediction":[[0,1]]}; pro více testů: {"predictions":[{"output":[[0,1]]}]}. Chat POST JSON: {"message":"...","model":"Model A"}; odpověď {"reply":"..."}.

Veřejný frontend není bezpečné místo pro API klíče. Pro soukromé tokeny použij backend/proxy, který je drží server-side. Python kód generovaný chatem se v této verzi automaticky nespouští. Historie běhů je pouze v paměti stránky. ZIP import využívá JSZip z CDN.

Pozor: některé ARC evaluační JSON soubory záměrně neobsahují správné testovací výstupy. V takovém případě se přesnost nezobrazí; výsledky modelu se přesto exportují.
