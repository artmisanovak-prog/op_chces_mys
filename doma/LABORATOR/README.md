# LABORATOR · Chceš MYŠ?

Toto je pracovní katalog nástrojů, které mají pomoci použít metodu MYŠ při řešení dalších problémů. Cílem není znovu dokazovat MYŠ, ale vybrat konkrétní problém a použít k němu vhodnou pracovní plochu, model nebo vyhodnocovací nástroj. Balíčky zůstávají oddělené, protože dělají různé věci.

## Začni zde
- [Praktický návod: co který nástroj dělá a kdy ho použít](JAK_ZACIT_A_CO_POUZIT.md)
- [Katalog a vyhledávání](index.html)
- [Nezávislé podrobné hodnocení nástrojů](HODNOCENI_NASTROJU.md)
- [Stav přenosu zdrojových souborů](STAV_IMPORTU.md)

## Co je potřeba rozlišovat
- **Pracovní plocha** eviduje materiál a úvahy, ale nemusí spouštět model.
- **Modelové pracoviště** eviduje vstupy, nástroje, operace a výsledky, ale samo modely nevykonává.
- **Laboratorní prototyp** může volat OpenAI-kompatibilní endpoint; je třeba rozlišit lokální model od cloudového API.
- **Slepý test** odděluje predikce od answer key a vyhodnocuje je až potom.
- **ARC Lab / ARC piloty** pracují se statickými ARC mřížkami; to není totéž jako interaktivní ARC-AGI-3.
- **CASMI/MS-MS** je chemická doména a její metriky se nesmějí míchat s ARC.
- **GitHub Pages** hostuje statické soubory, nikoli Python aplikace.

## Bezpečnost a reprodukovatelnost
Nikdy necommituj API klíče, neveřejná soutěžní data nebo answer keys. Záznam experimentu má obsahovat přesný vstup, model a jeho verzi, prompt, nastavení, surovou odpověď, chyby a pravidla skórování. localStorage není synchronizovaná databáze; pravidelně exportuj zálohu.
