# Modelové pracoviště

## K čemu slouží
HTML pracovní plocha pro zaznamenávání experimentů s modely: co bylo vstupem, jaké instrukce byly použity, jaký model nebo endpoint běžel a jaký výstup vznikl. Je to především evidence a organizace práce, ne automatický benchmark.

## Jak ho vyzkoušet
Otevři `index.html` v prohlížeči. Založ jeden malý pokus, zapiš přesně vstup a instrukci, přidej výsledek a exportuj záznam. Po zavření stránky ověř, zda se data drží v localStorage a zda je lze obnovit importem.

## Co je na návrhu užitečné
- Experimenty lze popsat bez nutnosti hned programovat celý běhový systém.
- Odděluje konfiguraci pokusu od závěru, který si z výsledku vyvodíš.
- Export/import může pomoci přenášet evidenci mezi zařízeními.

## Co je potřeba ověřit
- Jestli jednotlivá pole skutečně pokrývají model, verzi, parametry, chyby a opakování běhu.
- Zda export obsahuje vše potřebné pro reprodukci, nikoli jen poznámky.
- localStorage není synchronizovaná databáze ani automatická záloha.
- Pokud nástroj model pouze eviduje, neznamená to, že model sám spouští.

## Kdy se hodí
Když porovnáváš několik variant instrukcí nebo kontextu a potřebuješ později zjistit, co přesně se mezi běhy změnilo.
