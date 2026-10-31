# Jak začít v LABORATORU a který nástroj použít

Tento návod je praktický rozcestník podle toho, co chceš udělat. MYŠ zde ber jako pracovní metodu, kterou chceš používat při řešení jiných problémů. Není cílem tohoto katalogu znovu dokazovat, zda MYŠ funguje.

## Nejdřív si vyber typ práce

- **Chci řešit problém a přemýšlet nad vztahy v textu nebo obrazu, bez AI:** začni Laboratoří vztahů MYŠ. Zapiš problém, materiál, co v něm pozoruješ, jaké vztahy jsou důležité a jak by změna jednoho vztahu změnila situaci.
- **Chci, aby do řešení vstoupil jazykový nebo obrazový model:** použij Laboratorní prototyp, pokud je jeho HTML zdroj v repozitáři a endpoint je správně nastavený. Zatím nejde o bezpečný veřejný nástroj pro tajné API klíče.
- **Chci vyřešit úlohu ARC s barevnými mřížkami:** použij ARC nástroje. ARC Lab je pro prohlížení a ruční práci; Python piloty jsou pro generování odpovědí přes konkrétní model a jejich vyhodnocení.
- **Chci jen zaznamenat, co jsem zkusila a jaký výsledek vznikl:** použij Modelové pracoviště. Je to evidence, nikoli model, který problém vyřeší.
- **Chci zkontrolovat, co obsahují datové soubory:** použij CASMI inventuru pouze pro chemická data a odpovídající datové formáty.
- **Chci řešit interaktivní ARC-AGI-3:** žádný statický ARC grid prototyp v tomto katalogu nepovažuj automaticky za hotového soutěžního agenta. To vyžaduje zvláštní napojení na interaktivní prostředí a odpovídající akční smyčku.

## Jak použít MYŠ při řešení jiného problému

1. **Pojmenuj cílový problém.** Ne „otestovat MYŠ“, ale například „najít pravidlo, které řídí změny v těchto obrazových úlohách“ nebo „vysvětlit rozpor v několika dokumentech“.
2. **Vlož skutečný materiál problému.** Text, obrázek, mřížku, data nebo popis situace. Zaznamenej, odkud materiál pochází.
3. **Použij MYŠ tak, jak ji běžně používáš.** Zachovej její vlastní způsob práce. Neredukuj ji automaticky na seznam úhlů, kategorie nebo předem dané šablony.
4. **Převeď výsledek do podoby, kterou problém vyžaduje.** U ARC to může být přesná výstupní mřížka. U analýzy dokumentů to může být vysvětlení vztahů a rozporů. U návrhu řešení to může být konkrétní postup.
5. **Zkontroluj výsledek podle pravidel daného problému.** U ARC porovnej výstupní mřížku se správnou odpovědí. U jiných problémů použij odpovídající kritéria, zdroje nebo praktickou kontrolu. To není zkouška existence MYŠ, ale kontrola, zda vyřešila konkrétní úkol.
6. **Ulož použitelný výsledek a podmínky.** Zaznamenej vstup, postup MYŠ, výstup, případné chyby a co je potřeba udělat dál. Díky tomu lze práci navázat a výsledek použít.

## Co jednotlivé nástroje opravdu dělají

### Laboratoř vztahů MYŠ
Použij ji jako pracovní stůl pro samotné řešení: čti materiál, zapisuj pozorování a vztahy, zkoušej změny a uchovávej výsledky. Podle dokumentace ukládá záznamy v prohlížeči a umožňuje export JSON/CSV. Sama nevolá model a sama neověřuje správnost odpovědi.

**Stav v repozitáři:** README je přítomné, ale původní soubor index.html je podle inventury importu ještě potřeba přenést. Dokud se nepřenese, odkaz na README není spustitelná aplikace.

### Modelové pracoviště
Použij ho jako zápisník běhů: co jsi zadala, jaký nástroj/model jsi použila, jaký výstup vznikl a co z něj chceš zachovat. Není to model ani automatický řešič.

**Stav v repozitáři:** README je přítomné; původní HTML aplikace chybí. Zatím čti návod, ale nepočítej s tím, že lze aplikaci spustit.

### Laboratorní prototyp
Zamýšlený pracovní prostor pro materiály, instrukce, modelový endpoint a deník výstupů. Použij ho tehdy, když potřebuješ, aby model skutečně zpracoval vstup, nikoli pouze když chceš uložit vlastní poznámku. Cloudové API vyžaduje připojení a klíč; tajný klíč nepatří do veřejného HTML ani veřejného repozitáře.

**Stav v repozitáři:** README je přítomné; původní HTML aplikace chybí. Nelze zatím tvrdit, že je spustitelná.

### Základní portál
Použij ho jako rozcestník mezi nástroji. Neřeší problém za tebe a není centrální databází.

**Stav v repozitáři:** README je přítomné; původní HTML aplikace chybí.

### ARC Lab Starter
Použij ho k vizuální kontrole statických ARC úloh a k ručnímu přemýšlení nad pravidlem. Pokud chceš automaticky získat odpověď, musí být navíc připojený model nebo řešicí kód.

**Stav v repozitáři:** README je přítomné; původní HTML aplikace chybí.

### ARC + Gemini pilot
Použij ho, když chceš poslat statické ARC zadání modelu Gemini přes API a získat jeho predikci. Vyžaduje internet a API klíč. Výstup potom musí být převeden na přesnou mřížku a vyhodnocen. Tento nástroj není offline agent pro ARC-AGI-3.

**Stav v repozitáři:** Python skript a dokumentace jsou uvedené jako importované. Začni na několika necitlivých ukázkových úlohách a ověř požadovaný formát dat a výstupu.

### Slepý ARC test a offline evaluator
Použij je ve dvou oddělených krocích: nejprve vytvoř a ulož predikce, potom spusť evaluator proti oddělenému klíči. Evaluator odpovědi nevytváří; pouze kontroluje již uložené predikce. Klíč odpovědí nesmí být v kontextu modelu ani ve veřejném repozitáři.

**Stav v repozitáři:** skripty jsou uvedené jako importované. Nejdřív je spusť na malé sadě a ověř chybějící predikce, párování ID a výpočet skóre.

### Lokální ARC evidence
Použij ji pro lokální prohlížení úloh a ukládání poznámek. Vyžaduje Python na počítači; GitHub Pages Python nespustí. Není to automatický řešič.

**Stav v repozitáři:** aplikace a demo jsou uvedené jako importované. Je potřeba prakticky ověřit spuštění a ukládání na cílovém počítači.

### MOUSE Lab Environment a relační pilot v2
Použij je, pokud chceš běh experimentu popsat konfigurací a porovnávat varianty vstupu či instrukcí. Nejde o povinný mezikrok při každém použití MYŠ. Je to pomocná infrastruktura pro opakované běhy. Statické ARC vstupy nejsou interaktivní ARC-AGI-3.

**Stav v repozitáři:** dokumentace existuje, ale některé hlavní zdrojové soubory podle inventury importu chybí. Nepovažuj balíček za spustitelný, dokud nejsou přeneseny a ověřeny zdrojové soubory.

### CASMI CPU baseline a CASMI inventura
Tyto nástroje patří do chemického projektu se spektry MS/MS, ne do řešení ARC. Inventura kontroluje strukturu dat. Baseline se pokouší řadit chemické kandidáty. Používej je pouze tehdy, pokud chceš pracovat s tímto chemickým problémem.

**Stav v repozitáři:** inventura a její README jsou přítomné. U CASMI baseline je potřeba ověřit dostupnost skriptu, závislosti, vstupní data a přesnost na označených příkladech.

## Co je připravené a co ne

Nahrané README znamená, že je dostupný návod, nikoli nutně samotný nástroj. Pythonový skript může mít syntakticky správný kód, ale stále nemusí fungovat s tvými daty nebo na tvém zařízení. HTML soubor se musí otevřít, načíst své materiály a úspěšně provést zamýšlenou akci. Každý nástroj proto potřebuje svůj skutečný test.

Aktuální seznam chybějících zdrojových souborů je v [STAV_IMPORTU.md](STAV_IMPORTU.md). Ten je důležitější než zelený štítek nebo název karty v katalogu.

## Doporučený postup bez programování

1. Otevři [katalog](index.html) a tento návod.
2. Rozhodni se, jaký konkrétní problém chceš řešit.
3. Použij příslušný nástroj jen tehdy, když je jeho zdrojový soubor skutečně přítomný a funguje.
4. Pokud je k dispozici jen README, ber to jako popis plánovaného nástroje, ne jako hotovou aplikaci.
5. Po každém kroku si ulož výsledek a exportuj lokální data. localStorage se automaticky nesynchronizuje mezi telefonem a počítačem.

