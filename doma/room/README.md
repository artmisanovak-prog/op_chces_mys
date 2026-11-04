# MOUSE ROOM

**Malá sada propojených statických nástrojů v `doma/room/`.** Není to velká platforma, nemá backend ani databázi.

## Rozcestník

- [Otevřít ROOM](index.html)
- [Generátor](generator.html)
- [Laboratoř pokusů](laborator.html)
- [Porovnávač](porovnani.html)
- [Technická dokumentace](dokumentace.html)
- [Manifest](manifest.json)

## Princip

- **Karta jako API:** karta je přenosný vstupní objekt. Nástroje z něj skládají zadání a uchovávají původní text.
- **URL jako stav:** generátor umí zakódovat stav formuláře do fragmentu URL. V laboratoři fragment vybírá ID lokálního záznamu, samotná data v URL nejsou.
- **Relativní cesty:** ilustrace a pohádky se odkazují do `../chces_mys/ilustrace/` a `../chces_mys/kriva_pohadka/`. Zdrojová data se nekopírují ani neduplikují.
- **Myš jako záznam:** zdroj, výstup, pozorování, hypotéza a test jsou oddělené položky. Nástroj nerozhoduje za uživatele, co je pravda.
- **Větvení:** větev přebírá zadání a metodiku, ale nepřepisuje výstup ani pozorování rodičovského pokusu.

## Ukládání a přenos

Záznamy jsou ukládány do `localStorage` pod klíčem `mouse_room_records`. Použij export JSON jako zálohu a import JSON na jiném zařízení. Úložiště prohlížeče není totéž co soubor v repozitáři a není automaticky synchronizováno s GitHubem.

## Modely

První verze používá ruční předávání promptů a výstupů. Můžeš použít stejné zadání ve více modelech nebo měnit instrukci při zachování modelu. API klíče nejsou součástí HTML. Přímé API volání by vyžadovalo bezpečné zprostředkování nebo jiný důvěryhodný klient, nikoli tajný klíč v publikovaném kódu.

## Obsah

Ilustrace a pohádky zůstávají v původních složkách:
- [Ilustrace](../chces_mys/ilustrace/README.md)
- [Křivé pohádky](../chces_mys/kriva_pohadka/README.md)

## Stav verze 1.0

Statický prototyp. Neověřuje pravdivost vygenerovaných teorií a sám nevolá modely. Umožňuje připravit strukturované zadání, porovnat vložené výstupy, evidovat testy a přenášet záznamy pomocí JSON.
