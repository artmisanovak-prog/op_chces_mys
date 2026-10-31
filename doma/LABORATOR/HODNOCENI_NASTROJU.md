# Nezávislé čtení nástrojů v LABORATORU

Tento dokument posuzuje balíčky jako samostatné technické a výzkumné nástroje. Nehodnotí, zda „správně vystihují MYŠ“, a nepředpokládá, že všechny musí být součástí jednoho systému. Rozlišuje zamýšlené použití, praktickou hodnotu a otevřené technické či metodické otázky.

Poznámka ke zdrojům: hodnocení vychází z dostupných README, rozhraní a skriptů v dodaných ZIP balíčcích. Kde zdrojový soubor v repozitáři chybí, samotný popis nepovažuji za důkaz, že je aplikace v repozitáři spustitelná. Silná stránka znamená vlastnost konstrukce nebo pracovního postupu, nikoli prokázaný vědecký výsledek.

## 1. Laboratoř vztahů MYŠ

**K čemu slouží:** Kvalitativní pracovní plocha pro čtení pohádek a prohlížení ilustrací. Uživatel zaznamenává pozorování, navržený vztah, změnu podmínek, výsledek, přenos do jiného kontextu a limit interpretace. Materiály lze načítat z veřejných složek GitHubu nebo z místních souborů. Záznamy se ukládají do localStorage a lze je exportovat jako JSON nebo CSV.

**Jak ji vyzkoušet:** Vyber jeden příběh a odděleně napiš, co je přímo pozorovatelné, jaký vztah navrhuješ, co by se změnilo po zásahu a co by ukázalo, že hypotéza neplatí. Pak zkus stejný vztah u jiného příběhu. Exportuj záznam a zkontroluj, zda lze později rekonstruovat původní úvahu.

**Co je dobře navržené:** Umožňuje zaznamenat nejen závěr, ale také podmínky, přenos a hranice platnosti. Export do JSON je vhodný pro další analýzu, CSV pro přehled záznamů. Lze pracovat bez modelu a API.

**Co je nedořešené:** Různí lidé mohou pole „pozorování“, „vztah“ nebo „výsledek“ chápat různě, takže záznamy nejsou automaticky srovnatelné. localStorage je vázané na konkrétní prohlížeč a zařízení. Načítání z GitHubu vyžaduje internet. Nástroj sám neověřuje, zda se vztah opravdu přenesl; zaznamenává provedený test, nikoli automatický důkaz.

**Nezávislé zhodnocení:** Největší potenciál je v rozlišení pozorování, interpretace a ověření. Pro výzkumné použití by pomohlo verzované schéma záznamu, identifikátory zdrojů a možnost porovnat dvě interpretace téhož materiálu.

## 2. Modelové pracoviště

**K čemu slouží:** Evidence toku práce: vstupní data → model nebo nástroj → operace → výstup a skóre → další varianta. Umí evidovat různé typy vstupů, popis modelů, role nástrojů, výstupy, skóre, poznámky a historii. Pracovní prostor lze exportovat a importovat jako JSON.

**Jak ho vyzkoušet:** Založ jednu ARC úlohu jako vstup, přidej dvě položky modelů (například baseline a varianta s instrukcí) a zaznamenej jejich výstupy jako dvě oddělené operace. Ulož i prompt, verzi modelu, podmínky a surový výstup, ne pouze výsledné skóre.

**Co je dobře navržené:** Odděluje data, modely/nástroje a běhy. Historie může uchovat více pokusů namísto přepsání poslední odpovědi. Export/import usnadňuje zálohu a přesun pracovního prostoru.

**Co je nedořešené:** Aplikace sama modely nespouští, neparsuje chemické struktury a automaticky nevyhodnocuje ARC mřížky. localStorage není synchronizovaná databáze. Pro reprodukovatelnost by záznam měl obsahovat identifikátor či hash vstupu, přesnou verzi modelu, parametry, časový limit a stav chyby.

**Nezávislé zhodnocení:** Je to evidence, ne výpočetní engine. Přínos závisí na tom, zda se zaznamenávají surové výstupy a přesné podmínky. Bez jednotného schématu se může změnit v hromadu poznámek, které nejdou spolehlivě porovnat.

## 3. Laboratorní prototyp

**K čemu slouží:** Prototyp pro knihovnu materiálů, výběr více textů, konfiguraci OpenAI-kompatibilního endpointu, test připojení a deník běhů. Endpoint může být cloudový nebo lokální, pokud skutečně implementuje očekávané API.

**Jak ho vyzkoušet:** Přidej jeden krátký text, nastav endpoint a otestuj připojení. Potom spusť stejný požadavek dvakrát s různými instrukcemi. Zkontroluj, zda deník zachytil model, prompt, materiály, čas, nastavení, chybu a výstup.

**Co je dobře navržené:** Propojuje materiály, instrukci, skutečný modelový požadavek a deník. Umožňuje pracovat s více materiály v jednom kontextu. Lokální OpenAI-kompatibilní endpoint může fungovat bez externího API, pokud model i server skutečně běží lokálně.

**Co je nedořešené:** Cloudové volání z prohlížeče může narazit na CORS a API klíč není bezpečné vystavovat na veřejné stránce. Kompatibilní endpoint nemusí podporovat obrazové vstupy ani stejné parametry jako jiná API. U obrázků mohou být uloženy jen cesty/URL, které mohou přestat fungovat. Výstupy modelu je třeba validovat podle konkrétní úlohy.

**Nezávislé zhodnocení:** Jde o jeden z nejpraktičtějších prototypů pro pokusy s různými modely, ale zároveň je zde zásadní bezpečnost klíčů a přesné ověření schopností endpointu. Pro offline provoz musí být lokálně dostupný model, jeho váhy i všechny závislosti.

## 4. ARC Lab Starter

**K čemu slouží:** HTML rozhraní pro prohlížení ARC mřížek, zadávání nebo porovnávání řešení a organizaci práce s úlohami. Není to samo o sobě inteligentní řešič.

**Jak ho vyzkoušet:** Otevři ukázkovou úlohu, ověř všechny trénovací páry i testovací vstup, proveď ruční pokus a zkontroluj, co se uloží a zda lze výstup znovu načíst a exportovat.

**Co je dobře navržené:** Vizuální kontrola může usnadnit hledání chyb v datech a formulaci pravidla. Rozhraní může zkrátit cestu od úlohy k experimentálnímu záznamu.

**Co je nedořešené:** Je třeba odlišit vizualizaci, ruční řešení, modelovou predikci a automatické skórování. Nutno ověřit více testovacích příkladů, rozměry mřížek, chybné JSON a export. Statické ARC úlohy nejsou totéž co interaktivní ARC-AGI-3.

**Nezávislé zhodnocení:** Hodnota je v inspekci a ergonomii. Pro vědecký experiment musí být výstupy svázané se stabilním ID úlohy, verzí vstupu a přesným vyhodnocením.

## 5. ARC + MYŠ / Gemini pilot

**K čemu slouží:** Python skript volá Gemini přes API a porovnává experimentální podmínky na stejných statických ARC úlohách, například základní instrukci a variantu s jiným postupem či kontextem.

**Jak ho vyzkoušet:** Nejprve na 3–5 úlohách ověř formát datasetu, počet volání a ukládání surových odpovědí. Potom spusť baseline a experimentální variantu na stejné sadě. API klíč nastav jako tajný údaj prostředí, nikoli do kódu. Hodnoť přesnou shodu mřížky.

**Co je dobře navržené:** Srovnání podmínek je lepší než vybírat jednotlivé úspěšné příklady. Lze zachovat surové odpovědi a model není nutné instalovat lokálně.

**Co je nedořešené:** Vyžaduje internet a API klíč. Výsledek závisí na modelu, promptu, kontextu a chybách API. Podmínky musejí být srovnatelné i co do počtu tokenů a pokusů. Je nutné předem určit metriky, včetně zacházení s chybějícími odpověďmi.

**Nezávislé zhodnocení:** Vhodné pro levný první test konkrétní hypotézy, nikoli pro tvrzení o obecném přenosu pravidel. Negativní výsledek je také užitečný, pokud je experiment správně kontrolovaný.

## 6. ARC: slepý test a offline evaluator

**K čemu slouží:** Odděluje vytvoření sady bez odpovědí, inference a následné offline vyhodnocení proti samostatnému klíči.

**Jak ho vyzkoušet:** Vytvoř malou sadu, nech model vytvořit predikce pouze z trénovacích párů a testovacího vstupu, ulož predikce a teprve poté spusť evaluator. Otestuj také chybějící odpověď, duplicitní ID a chybnou mřížku.

**Co je dobře navržené:** Odděluje predikci od skórování. Offline evaluator nevyžaduje model ani API a uložené predikce lze znovu vyhodnotit.

**Co je nedořešené:** Veřejná úloha mohla být v předtrénování modelu. Klíč musí být fyzicky oddělen a nikdy nesmí být ve veřejném repozitáři ani modelovém kontextu. Je nutné ověřit, že jmenovatel zahrnuje všechny úlohy a že chybějící odpovědi nejsou tiše vynechány.

**Nezávislé zhodnocení:** Metodicky je správný evaluator důležitější než další grafické rozhraní. Chybný jmenovatel nebo párování ID dokáže vytvořit přesvědčivé, ale falešné skóre.

## 7. Lokální ARC evidence a první ARC-AGI-2 prototyp

**K čemu slouží:** Jednoduchá Python aplikace pro lokální prohlížení ARC úloh a zaznamenávání pozorování či odvozených pravidel.

**Jak ji vyzkoušet:** Použij demo data, spusť aplikaci podle README nebo skriptu pro Windows a ověř načítání úloh, ukládání záznamů a jejich opětovné otevření. Teprve potom přidej vlastní dataset.

**Co je dobře navržené:** Python může pracovat s lokálními soubory bez API. Malý prototyp dovoluje ověřit workflow bez velké infrastruktury.

**Co je nedořešené:** Demo data nedokazují kompatibilitu se všemi ARC úlohami. Postup pro Windows není automaticky pohodlný na telefonu ani v Kaggle. Není to soutěžní agent ani interaktivní ARC-AGI-3 implementace.

**Nezávislé zhodnocení:** Vhodné jako inspekční pomůcka. Pro soutěžní výkon je potřeba oddělený agent a přesně definované rozhraní soutěžního prostředí.

## 8. MOUSE Lab Environment

**K čemu slouží:** Experimentální běhové prostředí řízené JSON konfigurací. Odděluje konfiguraci, zdrojové materiály, běh a výstupy, aby se varianty nemusely ručně přepisovat v kódu.

**Jak ho vyzkoušet:** Začni ukázkovou konfigurací, ověř skutečně implementovaný backend a spusť nejmenší možný běh. Zkontroluj, zda se ukládá konfigurace, predikce, chyby a souhrn. Ověř také chování při přerušení a opakovaném spuštění.

**Co je dobře navržené:** Konfigurace oddělená od kódu usnadňuje srovnávání podmínek. Strojově čitelné výstupy podporují audit a další analýzu.

**Co je nedořešené:** Konfigurační pole nezaručuje funkční adaptér pro libovolný model. Je nutné rozlišit lokální model, API model a simulovaný běh. Offline provoz vyžaduje předem dostupné váhy, balíčky a data. Statický ARC runner není automaticky kompatibilní s ARC-AGI-3.

**Nezávislé zhodnocení:** Má smysl, pokud se používá pro opakovatelné experimenty. Nejdřív ale musí být jasné, které části se opravdu vykonávají a které jsou jen deklarované v konfiguraci.

## 9. ARC + MOUSE relační pilot v2

**K čemu slouží:** Srovnává několik podmínek na statických ARC JSON úlohách a může oddělit vliv instrukce, textového kontextu a ilustrací.

**Jak ho vyzkoušet:** Začni několika úlohami. Ověř, že každá podmínka dostává srovnatelný základní vstup a že se odpovědi neposílají modelu. Ulož surové odpovědi, chyby a offline skóre.

**Co je dobře navržené:** Více podmínek umožňuje testovat konkrétní vysvětlení místo neurčitého tvrzení, že kontext pomáhá. Oddělené vyhodnocení umožňuje zachytit i negativní efekt.

**Co je nedořešené:** Malý vzorek má vysokou nejistotu. Je třeba předem stanovit metriky, pravidla pro více predikcí a srovnatelnost délky kontextu. API varianta není offline. Nejde o interaktivní ARC-AGI-3 řešení.

**Nezávislé zhodnocení:** Silou je ablace různých podmínek. Rizikem je zpětně vybrat jen ty metriky nebo typy úloh, které vyšly dobře. Podmínky a metriky stanov před spuštěním.

## 10. CASMI CPU baseline

**K čemu slouží:** Chemický retrieval nástroj pro řazení kandidátních molekul podle hmotnostní shody a vztahů v MS/MS spektrech. Je oddělený od ARC a běží na CPU.

**Jak ho vyzkoušet:** Ověř vstupní soubory a verze knihoven. Spusť malý test na známých příkladech a zkontroluj submission CSV, audit důkazů a běhovou zprávu. Přesnost měř pouze na oddělených označených datech.

**Co je dobře navržené:** Baseline poskytuje srovnávací bod, CPU běh snižuje potřebu GPU a audit může vysvětlit pořadí kandidátů. Explicitní zacházení s chybějícími informacemi je lepší než domýšlení hodnot.

**Co je nedořešené:** Retrieval vybírá z referenční knihovny a není de-novo generováním. Přesnost není doložena existencí skriptu. Výsledky CASMI nelze vydávat za důkaz obecného uvažování ani míchat s ARC skóre.

**Nezávislé zhodnocení:** Je to doménově specifická baseline. Případný přenos metod mezi doménami by vyžadoval vlastní hypotézu a metriky pro každou z nich.

## 11. CASMI inventura dat

**K čemu slouží:** Kontroluje soubory, sloupce, chybějící hodnoty a rozložení dat před chemickým experimentem.

**Jak ji vyzkoušet:** Spusť ji na kopii dat a porovnej výpis s očekávaným schématem. Ověř povinné sloupce, datové typy a počty chybějících hodnot.

**Co je dobře navržené:** Odhaluje strukturální problémy dříve, než se zamění za chybu modelu, a odděluje kontrolu dat od měření výkonu.

**Co je nedořešené:** Přítomnost sloupce nepotvrzuje správnost hodnot. Chybějící hodnoty mohou mít různý význam. Inventura není evaluator.

**Nezávislé zhodnocení:** Je to podpůrný nástroj, ale důležitý. Kontrola dat dokáže zabránit falešným závěrům způsobeným chybnými vstupy.

## 12. Základní portál

**K čemu slouží:** Statický rozcestník k dalším HTML nástrojům a datovým složkám.

**Co je dobře navržené:** Jednotlivé nástroje mohou zůstat oddělené a statické HTML lze hostovat na GitHub Pages.

**Co je nedořešené:** Odkaz neznamená, že soubor existuje nebo funguje. localStorage se automaticky nesdílí mezi stránkami, prohlížeči a zařízeními. Relativní cesty se mohou rozbít při přejmenování složek.

**Nezávislé zhodnocení:** Rozcestník je užitečný, pokud usnadňuje orientaci a nepředstírá jednotný systém tam, kde existují samostatné prototypy. Interní odkazy by se měly automaticky kontrolovat.

## 13. Starší varianty

Starší Gemini materiály, slepý test 120, CASMI CPU Tool a první ARC prototyp je vhodné zachovat, dokud není jasné, co se mezi verzemi změnilo. Mohou se lišit prompty, formáty, algoritmem nebo skórováním. Nejsou automaticky zbytečné duplikáty, ale ani automaticky nové metody.

Při porovnání zaznamenej: změny algoritmu či instrukce, změny pouze v rozhraní, změny datasetu, způsob skórování a možnost reprodukovat starý výsledek. Pokud dvě verze dělají totéž, jedna může zůstat jako archivní reference. Pokud se liší, rozdíl pojmenuj a otestuj.

## 14. Testy, které pomohou posoudit všechny balíčky

1. **Spustitelnost:** lze nástroj otevřít nebo spustit podle návodu bez ruční opravy?
2. **Uložení:** zůstane záznam po obnovení stránky a lze jej exportovat a importovat?
3. **Reprodukovatelnost:** lze zjistit přesné vstupy, instrukci, model a parametry?
4. **Chybové stavy:** co se stane při chybějícím souboru, chybném JSON, odpojení API nebo prázdné odpovědi?
5. **Metodika:** jsou baseline a experimentální podmínka opravdu srovnatelné?
6. **Skórování:** lze výsledek nezávisle přepočítat a jsou zahrnuty i neúspěšné či chybějící odpovědi?
7. **Offline provoz:** funguje nástroj bez internetu, nebo jen jeho část? Je model opravdu lokální?
8. **Bezpečnost:** nejsou API klíče, odpovědní klíče nebo soukromé materiály ve veřejném repozitáři?
9. **Přenos dat:** funguje import mezi zařízeními a verzemi nástroje?
10. **Odkazy:** vede každý interní odkaz na existující soubor a správnou verzi?

Tyto testy nezávisí na tom, jakou teorii chceš obhajovat. Pomáhají rozlišit zajímavý nápad, použitelné rozhraní a skutečně ověřenou metodu.