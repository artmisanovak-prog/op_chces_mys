# ARC: slepý test a offline vyhodnocení

## K čemu slouží
Balíček odděluje přípravu úloh, generování predikcí a vyhodnocení proti klíči odpovědí. Smyslem je, aby se správná odpověď nepředávala modelu v době, kdy vytváří predikci.

## Typický postup
1. Připrav vstupní ARC JSON soubory a samostatný klíč odpovědí.
2. Vygeneruj slepou sadu bez answer key.
3. Ulož predikce v definovaném formátu.
4. Teprve potom spusť offline evaluator.
5. Zkontroluj počet očekávaných úloh, chybějící predikce, duplicity ID a chyby formátu.

## Silné stránky
- Oddělení predikce a vyhodnocení je metodicky lepší než posuzovat odpovědi během generování.
- Offline evaluator může běžet bez API.
- Výsledek lze znovu vyhodnotit, pokud jsou vstupy a klíč zachovány soukromě.

## Limity a bezpečnost
- „Slepý“ postup nezaručuje, že model dané veřejné úlohy nikdy neviděl při předtrénování.
- Klíč odpovědí se nesmí commitovat do veřejného repozitáře.
- Predikce musí být spojeny s úlohami podle stabilních ID, ne podle pořadí řádků.
- Před interpretací skóre ověř, že chybějící odpovědi nejsou vynechány ze jmenovatele.
