# 3. Obrazové snímače a jejich charakteristiky

## **Vysvětlete princip akumulačního snímání obrazu.**

Snímání záření po delší dobu -> více akumulovaného náboje na jeden obrazový bod Princip:

- 1. Komutátor připojí kondenzátor k obvodu.
- 2. Kondenzátor se rychle nabije.
- 3. Komutátor odpojí obvod a posune se k dalšímu kondenzátoru (respektive světlocitlivému prvku).
- 4. První kondenzátor se začne vybíjet přes fotorezistor. Rychlost vybíjení závisí na odporu a odpor závisí na intenzitě světla.
- 5. Výstupem je obrazový signál úměrný osvětlení.

![](_page_0_Figure_8.jpeg)

**Vysvětlete základní princip funkce obrazového snímače CCD (Charge Coupled Device).**

- Vytváří se náboj v závislosti na míře osvětlení
- Náboj je posouván po sloupcích ven s obvodu jako v registru

#### **Popište, jak dochází k fotogeneraci náboje v buňce CCD a na jakých parametrech bude záviset velikost generovaného náboje.**

- Fotogenerace náboje probíhá tak, že dopadající foton na polovodič vytvoří pár (elektron-díra).
- Elektrony jsou zachyceny v potenciálové jamce (pixelu), kde se akumulují během doby expozice.
- Velikost náboje (tedy počet elektronů) závisí především na:
	- Intenzitě dopadajícího světla
	- Délce expozice (času akumulace)
	- Citlivosti dané buňky (kvantová účinnost, vlastnosti materiálu)

#### **Popište stručně mechanizmus posuvu náboje ve struktuře CCD s použitím diagramu.**

- Postupné připojování napětí na elektrody
- Vytvoření potenciálového reliéfu (vlny)
- Na poslední elektrodě se odečítá signál

![](_page_1_Figure_4.jpeg)

## **Vysvětlete princip snímání barevného obrazu s využitím masky barevných filtrů CFA (Color Filter Array), zejména pak Bayerovu masku.**

- Protože senzor samotný snímá pouze intenzitu světla, filtrem zařídíme, že různé světlocitlivé prvky na senzoru ponesou informaci o různých vlnových délkách (resp. barvách)
- Bayerova maska (viz obr.) má 2x více zelených filtrů než modrých a červených
	- Zelená část nese nejvíc informace o jasu
	- Na zelenou část je oko nejcitlivější

# **Vysvětlete význam a základní postup měření modulační přenosové funkce MTF (Modulation Transfer Function).**

MTF udává jakým způsobem klesá kontrast se stoupajícím prostorovým kmitočtem

Měření: Vyfocení testovacího obrazce -> vykreslení profilu jasu (viz obr.) -> odečtení minim a maxim a dosazení do vzorce

![](_page_1_Figure_13.jpeg)

- **Bmax** maximální jas (intenzita) v signálu po zobrazení testovacího obrazce (tedy špička vlny),
- **Bmin** minimální jas (nejnižší hodnota signálu, "údolí" vlny).

![](_page_1_Figure_17.jpeg)

#### **Jak se projeví nedostatečné prostorové vzorkování při snímání obrazu a jak lze tomuto nežádoucímu jevu předcházet?**

- Objeví se aliasing
- Lze mu předejít anti-aliasingovým filtrem

Aliasing - jev, který vzniká při nedostatečném prostorovém vzorkování obrazu – když frekvence detailů v obraze je vyšší než polovina vzorkovací frekvence **(Nyquistovo kritérium není splněno)**

≥ 2

# 4. Předzpracování obrazu a videosignálu

**Popište význam kvantizace obrazové funkce a jak určíme požadavek na počet kvantizačních stupňů a bitovou hloubku reprezentace obrazu v multimediální technice?**

- Kvantizace je nezbytná pro digitalizaci obrazu
- Z Weberova-Fechnerova zákona víme, že prahový kontrast (tzn. nejmenší kontrast, který dokáže lidské oko rozpoznat) je asi k = 2%
- Není tedy třeba více kvantizačních stupňů
- -

  
2) $\frac{L_{\mathrm{i+1}}}{L_{\mathrm{i}}}=\mathrm{1}+k$

- 
  
4) Finale: $ n=\frac{log\frac{L_{min}}{L_{min}}}{\log{(1+k)}}$ .  

- 
#### **Popište co to je histogram šedotónového digitálního obrazu.**

- Graf zobrazující četnost jednotlivých jasových úrovní v obrazu.
#### **Popište mechanizmus výpočtu 2D diskrétní konvoluce nejlépe graficky.**

![](_page_3_Figure_14.jpeg)

3x3 část z původní grafiky násobíš 3x3 maticí, následně celé sčítáš do jednoho pixelu Výsledkem je stejný počet pixelů!

#### **Co to je korekce gamma a jak bude vypadat základní převodní charakteristika displeje a kamery v televizním systému?**

- Korekce jasu obrazu
- Lidské oko vnímá jas jinak než senzor -> kompenzuje se pomocí gamma korekce

![](_page_4_Figure_3.jpeg)

#### **Jaké přenosové signály pro jas (luma) a barvu (chroma) se používají v televizních soustavách, například PAL a proč?**

- Místo RGB se používá jasová složka a dvě barevné, rozdílové
- Oko je citlivější na jas
- Barva je nanesena na signál jasu pomocí amplitudové modulace

#### **Vysvětlete základní požadavky na digitalizaci složkového signálu televize ve standardním rozlišení podle ITU-R BT.601 ve smyslu vzorkovacího kmitočtu, bitové hloubky a požadovaného bitového toku.**

- Vzorkovací kmitočet pro jas je 13,5 MHz, pro barevné složky 6,75 MHz
- Bitová hloubka 8 bitů
- Bitový tok 216 Mb/s

**Vysvětlete význam barevných vzorkovacích rastrů např. 4:4:4, 4:2:2, 4:1:1, 4:2:0. J:a:b**

- J = šířka bloku jasových vzorků
- a = počet barevných vzorků v horním řádku
- b = počet barevných vzorků v dolním řádku
- 4:4:4 bez podvzorkování
- 4:2:2 horizontálně na polovinu
- 4:1:1 Horizontálně na čtvrtinu
- 4:2:0 Horizontálně i vertikálně na polovinu

![](_page_5_Figure_8.jpeg)

# 4. Komprese obrazu a videa

#### ***Vysvětlete základní rozdíl mezi mezi (matematicky) bezeztrátovou a (matematicky) ztrátovou kompresí obrazu.**

**Bezztrátová** – Rekonstruovaný signál je identický s originálem

**Ztrátová** – Rekonstruovaný signál je oproti originálu zkreslený

### ***Vysvětlete základní princip Huffmanova kodéru s proměnnou délkou kódu VLC (Variable Length Coding), nejlépe pomocí binárního stromu.**

Postup získání Huffmanova kódu:

- 1. Máme nějaké znaky, každý s pravděpodobností výskytu
- 2. Seřadíme znaky dle pravděpodobnosti
- 3. ▪Poledním 2 znakům (nejméně pravděpodobným) přiřadíme 1 (poslednímu) a 0 (předposlednímu)
- 4. Sloučíme tyto dva dohromady aka sečteme jejich pravděpodobnosti
- 5. Zpět na bod 2)
- 6. Po dokončení tohoto binárního stromu odečteme finální kódová slova: Čteme po lonce, od zadu. Viz. obr

![](_page_6_Figure_13.jpeg)

| Znak | Pravděpodobnost | Kódové slovo |
| --- | --- | --- |
| az | 0.4 | 1 |
| a 1 | 0.2 | 01 |
| a3 | 0.2 | 000 |
| a 4 | 0.1 | 0010 |
| as | 0.1 | 0011 |

#### ***Vysvětlete princip transformačního 2D DCT kódování bloků pro kompresi obrazu.**

DCT = Diskrétní Cosinová Transformace

Postup komprese:

- 1. Rozdělení obrazu na bloky 8x8 pixelů
- 2. Aplikace DCT
- 3. Výstupem jsou matice koeficientů. V levém horním rohu je DC složka a pak se po řádcích i sloupcích zvyšuje frekvence AC složek. V pravém dolním rohu je frekvence nejvyšší.

![](_page_7_Figure_6.jpeg)

#### ***Jaká transformace se nejčastěji používá v transformačním kódování bloků obrazu a vysvětlete proč?** 2D DCT

Na rozdíl od DFT má reálné hodnoty koeficientů a lepší kompresní zisk

#### ***Jaká je výhoda využití vlnkové transformace proti rozkladu do harmonických bázových funkcí při kompresi obrazu?**

Mnohem lepší komprese než DCT, Nevytváří blokovou strukturu (ale rozostřuje, co není tak rušivé)

# ***Jak se liší kompresní artefakty, které vznikají při kompresi obrazu podle standardů JPEG a JPEG2000?**

JPEG – Bloková struktura JPEG2000 – Rozostření

# ***Jaké transformace jsou použity ve standardech pro kompresi obrazu JPEG a JPEG2000?**

JPEG – 2D DCT JPEG2000 – Vlnková transformace

### ***Vysvětlete základní princip blokového odhadu pohybu ME (Motion Estimation) při kódování videa s vyu ▪ Rozdělení aktuálního snímku na makrobloky. Předchozí snímek bude sloužit jako reference.**

- 1. V ref. snímku vybereme oblast v okolí aktuálně počítaného makrobloku.
- 2. Ve vybrané oblasti hledáme makroblok, který nejlépe odpovídá aktuálně počítanému makrobloku.
- 3. Nalezený referenční makroblok virtuálně přesuneme na místo v aktuálním snímku a vypočítáme rozdíl obou snímků.
- 4. Dále přenášíme pouze tento rozdíl a pohybový vektor.žitím pohybových vektorů MV (Motion Vectors).

# ***Nakreslete a vysvětlete základní principiální schéma hybridního DPCM/DCT kodéru pro kódování videa.**

Hybridní kódovač kombinuje:

**DPCM** (časová predikce) – využívá rozdíl mezi aktuálním a předchozím snímkem,

**DCT** (diskrétní kosinová transformace) – převádí obrazové bloky do frekvenční oblasti.

Postup kódování:

Predikce obrazu pomocí pohybové kompenzace.

Výpočet rozdílu (chybového signálu) mezi vstupem a predikcí.

**DCT** – transformace rozdílu do frekvenční oblasti.

**Kvantizace** – redukce přesnosti (ztrátová komprese).

**Entropické kódování** – bezeztrátové kódování kvantovaných hodnot.

Rekonstrukce v kódovači (IDCT + přičtení predikce) pro potřeby další predikce.

**Pohybová kompenzace** – určení pohybových vektorů.

Režimy:

**Intra (I)** – bez predikce, jen DCT.

**Inter (P, B)** – s predikcí z jiných snímků.

![](_page_8_Figure_15.jpeg)

***Vysvětlete hlavní principiální rozdíly v subjektivních a objektivních metodách hodnocení kvality komprimovaného obrazu IQA (Image Quality Assessment) a videa. Objektivní:**

- Full reference Porovnávání originálu s komprimovaným obrazem
- Porovnávají se pixely jedna ku jedné
- Velmi jednoduché, velmi nepřesné
- MSE (mean square error), SNR a PSNR (Peak signal-to-noise ratio)
- Reduced reference Z originálu jsou extrahované pouze nějaké charakteristiky, a ty porovnáváme s komprimovaným obrazem.
- No reference bez reference, duh

#### **Subjektivní:**

- Promítání komprimovaného obrazu skupině pozorovatelů na referenčním monitoru. Pozorovatelé hodnotí kvalitu a výsledek se průměruje.
- Nevýhody: Časově náročné, nákladné, nelze automatizovat
- Výhoda: Nejpřesnější

# 6. Obrazové displeje

#### ***Vysvětlete, čím je ovlivněn rozsah reprodukovaných barev na daném rozbrazovači a jak souvisí s definovaným barevným prostorem, např. ITU-R Rec. BT. 601, 709, 2020, sRGB, Adobe RGB.**

Pokud je obraz zaznamenaný dle gamutu Rec. BT. 2020 (současně nejlepší) tak se nemůže zobrazit v plném rozsahu na zobrazovači se starším standardem.

#### ***Vysvětlete principinální rozdíl zobrazovačů podle způsobu vzniku obrazu (a) přímo vyzařující (světelné zdroje) a (b) nepřímo vyzařující (světelné ventily, modulátory). Jaké typy displejů podle technologie patří do jednotlivých skupin?**

Přímo vyzařující =Jednotlivé body září, a přímo tvoří obraz

- CRT, OLED, PDP, FED, SED… Nepřímo vyzařující = Mojí nějaké podsvícení, které je modulováno
- LCD, DMD, LCoS…

***Vysvětlete základní princip funkce obrazového displeje založeného na technologii LCD (Liquid Crystal Display). Jaké jsou výhody a nevýhody této technologie?**

- Zdroj světla -> Rozptylové elementy -> polarizace -> tekuté krystaly -> barevné filtry -> polarizace 2
- Molekuly v tekutých krystalech nabývají různých uspořádání dle intenzity elektrického pole

#### **Výhody:**

- Vysoká životnost (>10let)
### **Nevýhody:**

- V závislosti na konkrétní technologii může klesat jas nebo barevnost spolu se zorným úhlem
- V závislosti na konkrétní technologii menší barevný rozsah
- Dotykem obrazovky se deformuje obraz (IPS to nedělá -> dotykové displeje)

#### ***Vysvětlete základní princip funkce obrazového displeje založeného na technologii OLED (Organic Light-Emitting Diode). Jaké jsou výhody a nevýhody této technologie?** OLED = organic LED

Podobné LCD ale namísto krystalů je zde organický PN přechod

## **Výhody:**

- Nepotřebuje podsvícení
- Malá tloušťka a hmotnost
- 90% barevný rozsah
- Teoreticky nekonečný kontrastní poměr (černá = vypnutá LED)

# **Nevýhody:**

- Malá životnost organických složek (řádově jednotky let)
- Náročná technologie zpracování
- Náročná technika řízení jasu

## ***Vysvětlete základní princip funkce projekčního zobrazování založeného na technologii DLP (Digital Light Processing) respektive DMD (Digital Micromirror Device).**

- DMD čip je de facto ploška s miliony malých zrcátek, které buď odráží světlo do objektivu, nebo na pohlcující plochu (tzn. Buď svítí nebo ne)
- Tyto zrcadla se dokáží překlápět extrémně rychle a pomocí toho můžeme modulovat jas
- Před zdrojem světla je ještě filtrové kolo, kde se modrý, zelený a červený filtr velmi rychle mění
- Promítá se tedy nejdřív modrá, pak zelená a pak červená část obrazu

![](_page_11_Figure_0.jpeg)

