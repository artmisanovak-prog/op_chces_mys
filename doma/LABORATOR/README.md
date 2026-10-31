# LABORATOR · Chceš MYŠ?

Toto je pracovní katalog všech dodaných laboratorních prototypů. Nejde o jeden sjednocený systém. Každý balíček vznikl pro jinou otázku, a proto je zachovávám odděleně, aby sis je mohla sama prohlédnout a rozhodnout se, které směry chceš rozvíjet.

## Rozcestník

Otevři `index.html` v prohlížeči. Katalog popisuje, k čemu jednotlivé nástroje slouží, jak je vyzkoušet, co je na jejich konstrukci užitečné a co zůstává nevyřešené.

## Balíčky v tomto pracovním prostoru

- **Modelové pracoviště** – evidence experimentů, vstupů, modelů, instrukcí a výsledků.
- **Laboratorní prototyp** – práce s pohádkami a ilustracemi, zápis pozorování, vztahů, změn, přenosů a limitů.
- **Základní portál** – jednoduchý vstupní bod pro lokální data a nástroje.
- **ARC Lab** – rozhraní pro organizaci pokusů s ARC úlohami.
- **ARC + Myš / Gemini** – experimentální porovnání podmínek s modelem přes API.
- **Slepý ARC test** – oddělení predikcí od klíče odpovědí a offline vyhodnocení.
- **Lokální ARC evidence** – malá Python aplikace pro evidenci úloh.
- **CASMI CPU baseline** – retrieval baseline pro chemická data MS/MS, oddělená od ARC.
- **CASMI inventura** – kontrola struktury a přítomnosti datových souborů.
- **MOUSE Lab Environment** – experimentální běhové prostředí řízené JSON konfigurací.
- **ARC + MOUSE relational pilot v2** – srovnání několika podmínek na statických ARC JSON úlohách.
- **První ARC-AGI-2 prototyp** – lokální demonstrační aplikace pro práci s mřížkami.
- **Původní malé balíčky** – starší samostatné varianty některých výše uvedených nástrojů; nejsou automaticky totožné s novějšími verzemi.

## Jak číst hodnocení

„Silná stránka“ znamená praktickou vlastnost, kterou nástroj skutečně nabízí. „Otevřený problém“ znamená konkrétní technický nebo metodický limit, ne soud nad hodnotou celého projektu. Samotná existence rozhraní neznamená, že je funkce otestovaná nebo že experiment dosáhl výsledku.

## Provozní rozdíly

- HTML soubory otevři v běžném prohlížeči. Pokud používají `fetch()` k načítání lokálních JSON souborů, otevření přes `file://` může být blokováno; v takovém případě použij GitHub Pages nebo jednoduchý lokální server.
- Záznamy uložené v `localStorage` patří konkrétnímu prohlížeči a zařízení. Pravidelně exportuj zálohu.
- Python aplikace neběží na GitHub Pages. Potřebuje Python a případné závislosti.
- Gemini/API experimenty vyžadují síť a tajný klíč. Nejsou offline soutěžním řešením.
- Statické ARC mřížky nejsou totéž co interaktivní prostředí ARC-AGI-3.
- Do veřejného repozitáře nepatří API klíče, neveřejná soutěžní data ani answer keys.

