# Původní slepý ARC test 120

## Účel
Starší varianta přípravy slepé sady, běhu modelu a offline vyhodnocení. Zachovává se pro porovnání s pozdější verzí evaluatoru a pro dohledání změn v datovém toku.

## Co ověřit
- Zda každá úloha z answer key zůstává ve jmenovateli skóre.
- Jak se zachází s chybějícími predikcemi, duplicitními ID a chybným JSON.
- Zda predikce skutečně neobsahují cílové odpovědi.
- Zda skript správně pracuje s více testovacími příklady na jednu úlohu.

## Důležité
Nepoužívej tento balíček jako autoritativní evaluator, dokud ho neporovnáš s aktuální verzí a neotestuješ na uměle vytvořených případech, kde je správný výsledek známý.
