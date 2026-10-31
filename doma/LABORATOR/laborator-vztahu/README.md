# Laboratoř vztahů MYŠ

## K čemu slouží
Jednostránkové prostředí pro práci s pohádkami, ilustracemi a experimentálními záznamy. Uživatel může odděleně zapisovat pozorování, navržené vztahy, změny podmínek, výsledky, testy přenosu a limity.

## Spuštění
Otevři index.html přes GitHub Pages nebo v moderním prohlížeči. Načtení veřejných textů z GitHubu vyžaduje internet. Záznamy se ukládají do localStorage konkrétního prohlížeče; pravidelně používej export JSON jako zálohu.

## Co umí
- načítat .txt a .md soubory z veřejné složky GitHub repozitáře;
- hledat ilustraci se stejným názvem souboru ve veřejném repozitáři;
- přidat další veřejný repozitář a složku, aniž by se už načtené zdroje automaticky zahodily;
- importovat místní texty nebo JSON;
- zapisovat pozorování, vztahy, změny podmínek, výsledky, testy přenosu a limity;
- upravovat záznamy a exportovat sešit do JSON nebo záznamy do CSV.

## Co nedělá
Nespouští multimodální model, nevolá AI API a sama nedokazuje, že se pravidlo přeneslo. Je to prostředí pro práci s materiálem a evidenci hypotéz. Závěr o přenosu musí vycházet z odděleného testu a výsledků.

## Výchozí zdroj
- Repozitář: artmisanovak-prog/op_chces_mys
- Složka: doma/chces_mys/kriva_pohadka
- Ilustrace: hledá shodný název souboru v repozitáři

## Praktický test
Vyber jeden příběh, odděl pozorování od interpretace, zapiš hypotézu a způsob, jak ji zkusíš vyvrátit. Potom zkus stejnou hypotézu na jiném příběhu a zaznamenej i to, co se nepřeneslo. Nakonec exportuj JSON a ověř, že záznam lze obnovit.
