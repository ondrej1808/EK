#### Co je to zvuk
- Podélná tlaková vlna, která vzniká pohybem částic v látce - nejčastěji vzduch
- Změna tlaku v prostoru a čase
#### Jakými veličinami zvuk popisujeme
chat

| Veličina                   | Značka       | Jednotka | Význam / Vzorec                                                                       |
| -------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------- |
| Frekvence                  | \(f\)        | Hz       | Počet kmitů za sekundu                                                                |
| Vlnová délka               | ($\lambda$\) | m        | Vzdálenost mezi dvěma vrcholy vlny                                                    |
| Akustický tlak             | (p)          | Pa       | Okamžitý rozdíl tlaku způsobený zvukovou vlnou                                        |
| Intenzita zvuku            | (I)          | W/m²     | Výkon přenášený zvukem na jednotku plochy                                             |
| Hladina intenzity zvuku    | \($L_I$ \)   | dB       | $$L_I = 10 \log\left( \frac{I}{I_0} \right), \quad I_0 = 10^{-12} \,\text{W/m}^2$$    |
| Hladina akustického výkonu | \($L_w$\)    | dB       | $$L_w = 10 \log\left( \frac{W}{W_0} \right), \quad W_0 = 10^{-12} \,\text{W}$$        |
| Hladina akustického tlaku  | ($L_p$\)     | dB       | $$L_p = 20 \log\left( \frac{p}{p_0} \right), \quad p_0 = 2\cdot 10^{-5} \,\text{Pa}$$ |

#### Co to je akustický tlak, co to je hladina akustického tlaku, jednotky
-  Okamžitá změna tlaku v prostředí (např. ve vzduchu), způsobená průchodem **zvukové vlny**.
	- Jednotka Pa
	- $p_0=2\cdot 10^{-5}\text{ Pa}$ - minimální změna tlaku co lidské ucho zaznamená
- Hladina akustického tlaku je logaritmicky vyjádřený poměr tlaku ku $p_0$
	- Jednotka dB - člověk rozliší přibližně 1 dB
	- $L_p=20\cdot\text{log}(\frac{p}{p_0})$
#### Vlnová rovnice
- pro nějakou veličinu u
$$
\Delta u - \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2} = 0 
$$

<div style="page-break-after: always;"></div>


#### Kulová, rovinná a válcová vlna (řešení vlnové rovnice)
- Rovinná
$$
u(x,t) = A\cdot e^{j(kx - \omega t + \varphi)}
$$
- Válcová
$$
u(r,t) = \frac{A}{\sqrt{r}} e^{j(kr - \omega t + \varphi)}
$$
- Kulová
$$
u(r,t) = \frac{A}{r} e^{j(kr - \omega t + \varphi)}
$$
Odvození pro fajnšmkery:
$\Delta u - \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2} = 0$
$\Delta u = -ku^2$
$\frac{\partial^2 }{\partial t^2} = \omega$
Pak si stačí říct kterým směrem nám ta vlna letí
#### Části lidského sluchu
![[ucho.png]]
- Vnější ucho
	- slouží k ochranně středního ucha a jako akustický filtr
		- Ušní boltec - vertikální prostorovost zvuku
		- Zvukovod - čtvrtvlnný rezonátor
		- Bubínek - přenáší zvuk ze zvukovodu do středního ucha
- Střední ucho
	- V podstatě zajištuje impedanční přizpůsobení a nastavení citlivosti - napínání kůstek svalama
		- Kladívko - je rozvibrováno bubínkem
		- Kovadlinka - přenáší zvuk na třmínek
		- Třmínek - přenáší zvuk do vnitřního ucha 
- Vnitřní ucho
	- v hlemýždi dochází ke kmitočtové analýze (přeměna mechanických vibrací na nervové vzruchy)
		- Mechanicko-elektrochemický převodník
		- Třmínek tlačí na trubici s kapalinou - šnek
		- okénko aby se kapalina mohla hýbat
		- basilární membrána -> Cortiho orgán -> vláskové buňky
		- basilární membrána je rozkmitávána třmínkem
		- Na začátku hlemýždě se detekují vyšší kmitočty
		- Na konci hlemýždě se detekují nižší kmitočty
#### Funkce vnějšího ucha
- slouží k ochranně středního ucha a jako akustický filtr
#### Funkce středního ucha
- V podstatě zajištuje impedanční přizpůsobení a nastavení citlivosti - napínání kůstek svalama
#### Funkce vnitřního ucha
- v hlemýždi dochází ke kmitočtové analýze (přeměna mechanických vibrací na nervové vzruchy)
#### Křivky stejné hlasitosti
- Vyjadřuje jak hlasitě slyšíme jaké frekvence, vzhledem k tlaku a [[Phon]]
- Převodní charakteristika mezi fyzikálníma veličinama (tlak, frekvence) a vjemovou veličinou Phon, která je určená oproti základnímu tónu 1 kHz při určitém tlaku - 2x hlasitější než referenční tón = 2 Phony
#### Maskování
- Od Krasinskiho: https://youtu.be/f55ZrhtsHaE?si=03LMAYCqKScE2tOV&t=64
- Nějakým zvukem - šum přestimulujeme náš sluch (sníží se citlivost) a poté neslyšíme nějaký přidaný tón - tón je zamaskovaný


<div style="page-break-after: always;"></div>

#### Weberův a Fechnerův zákon
- Weberův zákon popisuje **nejmenší vnímatelný rozdíl** v intenzitě podnětu (tzv. rozdílový práh, ΔS). (k není uplně konstanta)
$$\frac{\Delta S}{S}=k$$
- Frechner navázal na Webera a rozšířil teorii na vztah mezi **subjektivním vnímáním** a **fyzikální intenzitou** podnětu.
	- **Vjem roste logaritmicky s fyzikální intenzitou podnětu.**
	- $R=C*log \text{ S}$
#### Co to je JND
- Just noticeble difference
- Právě postřehnutelný rozdíl pro hladinu akustického tlaku
- kmitočtově závislé, pro každý subjekt jiné, přibližně 1-2 dB pro kmitočet v pásmu nejvyšší citlivosti rozlišíme přibližně 2-3 Hz
#### Princip lokalizace zdrojů zvuku v horizontální rovině
- Zvuk vleze do jednoho ucha, ohýbá se kolem hlavy což ublíží nějakým kmitočtům a spektrálním rozdílům, pak vleze do druhého ucha -> z toho mozek vyhodnotí odkud zvuk přišel
#### Princip lokalizace zdrojů zvuku v mediální rovině
- Filtrace boltcem a zkušenost
- Letadlo nahoře, 🔊linka 118 směr smíchovské nádraží, příští zastávka .. . -> na stanici pod oknem


<div style="page-break-after: always;"></div>


#### Vlnová rovnice pro akustický tlak
$$\Delta p - \frac{1}{c^2} \frac{\partial^2 p}{\partial t^2} = 0
$$
#### Předpoklady pro odvození vlnové rovnice
- prostředí je spojité, stlačitelné, homogenní, izotropní, neviskózní (bez ztrát), v klidu 
- výchylky všech veličin jsou malé (linearizace úlohy) 
- akustické pole se předpokládá za nevírové (pole je gradientní) 
- akustické děje jako adiabatický termodynamický děj - nemění se teplota změnami tlaku
#### Řešení vlnové rovnice pro kulovou a rovinnou vlnu

1. **Rovinná vlna**  
   Pro rovinnou vlnu, která se šíří v $x$-směru, je řešení vlnové rovnice:

   $$
   p(x,t) = A e^{i(kx - \omega t)}
   $$

   Kde $A$ je amplituda, $k$ je vlnové číslo, $\omega$ je úhlová frekvence, $x$ je prostorová souřadnice a $t$ je čas.

2. **Kulová vlna**  
   Pro kulovou vlnu, která se šíří radiálně od bodového zdroje, je řešení vlnové rovnice:

   $$
   p(r,t) = \frac{A}{r} e^{i(k r - \omega t)}
   $$

   Kde $r$ je vzdálenost od zdroje, $A$ je amplituda, $k$ je vlnové číslo, $\omega$ je úhlová frekvence a $t$ je čas. Amplituda klesá s $1/r$.


<div style="page-break-after: always;"></div>

#### Systém elektroakustických analogií, analogické veličiny a prvky
#### Systém elektroakustických analogií

nvm chat věc:

| **Akustická veličina**                                  | **Elektroakustická analogie**            | **Akustický prvek**        | **Elektrický prvek**        |
| ------------------------------------------------------- | ---------------------------------------- | -------------------------- | --------------------------- |
| Akustický tlak $p$                                      | Napětí $V$                               | Akustický odpor $R_a$      | Elektrický odpor $R_e$      |
| Akustický průtok $\dot{m}$                              | Elektrický proud $I$                     | Akustická indukčnost $L_a$ | Elektrická indukčnost $L_e$ |
| Akustická rychlost $v$                                  | Elektrické napětí na kondenzátoru $U$    | Akustická kapacita $C_a$   | Elektrická kapacita $C_e$   |
| Akustická impedanční veličina $Z_a = \frac{p}{\dot{m}}$ | Elektrická impedance $Z_e = \frac{V}{I}$ |                            |                             |
| Akustická energie $E$                                   | Elektrická energie $W$                   | Akustický výkon $P_a$      | Elektrický výkon $P_e$      |

<div style="page-break-after: always;"></div>


![[analogie_zvuk_elektro_mechanika.png]]
#### Systém elektromechanických analogií, analogické veličiny a prvky
- viz [[Audio#Systém elektroakustických analogií]]


<div style="page-break-after: always;"></div>

#### Vlnové číslo
Vlnové číslo $k$ je veličina, která popisuje počet vlnových cyklů na jednotkovou délku ve směru šíření vlny. Je definováno jako:
$$
k = \frac{2\pi}{\lambda}
$$
Kde:
- $k$ je vlnové číslo,
- $\lambda$ je vlnová délka.

Vlnové číslo je také spojeno s frekvencí $f$ a rychlostí zvuku $c$:
$$
k = \frac{2\pi f}{c}
$$
Jednotka vlnového čísla je $\left[\frac{rad}{m}\right]$. Vlnové číslo je důležité pro analýzu šíření vln a interakci vln s prostředím.
#### Co to je deterministický signál
- Má jasně definovaný časový/spektrální popis (matematický) - není náhodný
#### Co to je stochastický signál
- Náhodný signál - šum
#### 3 roviny analýzy hudebních signálů
- dynamická – závislost amplitudy na času 
- melodická – závislost kmitočtu na času 
- harmonická – závislost amplitudy na kmitočtu


<div style="page-break-after: always;"></div>

#### Co to je vibráto a tremolo
- **Vibráto**: Technika, která způsobuje jemné kolísání **výšky tónu** (frekvence). Používá se k "oživení" tónu a přidání emocionálního výrazu. Může být prováděno například zpěvem nebo pohyby prstů na hudebním nástroji.

- **Tremolo**: Efekt, který mění **hlasitost** tónu (intenzitu). Vytváří efekt "třesení" nebo "pulzování" tónu. Používá se například na elektrické kytaře pomocí tremolo baru nebo efektového pedálu, nebo rychlými pohyby smyčce u smyčcových nástrojů.
#### Perkusní a neperkusní tón
- **Perkusní tón**: Tón generovaný nástroji, které se nárazem rozechvějí (např. bicí nástroje).
- **Neperkusní tón**: Tón, který vzniká plynulým, kontinuálním způsobem (např. strunné nástroje, dechové nástroje).

#### Vlastnosti tónu
- délka
- síla (hlasitost)
- barva (timbre)
- výška
- jsou to SUBJEKTIVNÍ veličiny

#### Co je to oktáva
- Oktáva je interval, kdy frekvence jednoho tónu je dvojnásobná oproti jinému tónu.
- V hudební teorii je to nejzákladnější interval mezi dvěma tóny.
- Příkladem je interval mezi tónem C a dalším C v oktávě.


<div style="page-break-after: always;"></div>

#### Princip funkce elektrodynamického měniče jako mikrofon nebo jako reproduktor
- **Mikrofon**: Zvukové vlny pohybují membránou na které je cívka, do které se indukuje elektrický napětí, je tam magnet, který se nehýbe.
- **Reproduktor**: Elektrický signál prochází cívkou, ta je na membráně a přitahuje se k magnetu, který je statický.

#### Princip funkce elektrostatického měniče jako mikrofon nebo jako reproduktor
- **Mikrofon**: Zvukové vlny pohybují lehkou membránou mezi elektrody, což mění kapacitu a vytváří elektrický signál.
- **Reproduktor**: Elektrický signál způsobuje pohyb membrány mezi elektrody, což vytváří zvuk.

#### Náhradní obvody měničů s magnetickým polem
![[menic_magneticke_pole.png]]
- TODO: Popis součástek [[AVT - 3 - menice.pdf#page=18]]
#### Náhradní obvody měničů s elektrickým polem
![[elektrostaticky menic.png]]
- TODO: Popis součástek [[AVT - 3 - menice.pdf#page=7]]



<div style="page-break-after: always;"></div>

#### Co to je jmenovitá impedance reproduktoru
- Jmenovitá impedance reproduktoru je elektrická impedance, kterou vidí zesilovač na svém výstupu, kde je reproduktor připojený
- Obvykle vyjádřena v ohmech, např. 4Ω, 8Ω.

#### Funkce a typy ozvučnice reproduktoru
- **Funkce**: Ozvučnice zvyšuje účinnost reproduktoru (elimance akustického zkratu na okrajích reproduktoru)a upravuje akustickou odezvu.
- **Typy**: Uzavřená ozvučnice, basreflex, otevřená ozvučnice.

#### Typy měřicích mikrofonů
- MEMS
- Elektrostatický

#### Vlnová akustika, princip a meze platnosti
- Vychází z řešení vlnové rovnice (tedy pouze jednoduché geometrie) 
- zkoumání vlastních módů
#### Geometrická akustika, princip a meze platnosti
- intuitivní, nejstarší, pouze pro přechodové stavy v prostoru 
- Přístup k řešení: 
	- metoda paprsků 
	- metoda zrcadlení zdrojů 
	- metoda konečných prvků 
	- metoda hraničních prvků
	
#### Statistická akustika, princip a meze platnosti
- **Princip**: Statistická akustika je zjednodušení založeno na energetických veličinách - hustotě zvukové energie
- **Meze platnosti**: Používá se pro složitá prostředí s mnoha odrazy a difuzními vlnami.
	- podmínky – difúzní pole, pole odražených vln
	- energie dána součtem středních hodnot odražené energie 
	- hustota zvukové energie je všude stejně veliká 
	- úhly příchodu zvukové energie do daného bodu jsou všechny stejně pravděpodobné
	- vyzařování a pohlcování je kontinuální


<div style="page-break-after: always;"></div>

#### Zvukové pole v uzavřené místnosti, dozvuková vzdálenost
![[zvukové pole.png]]
![[zvukové pole vole dozvuk distance.png]]


<div style="page-break-after: always;"></div>

#### Princip studia LE DE
https://hofa-akustik.de/en/blog-en/room-acoustics-live-end-dead-end-explained/
https://www.soundassured.com/blogs/blog/what-is-a-lede-room-design-home-studio-acoustics-setup-guide
- **Koncept rozložení odrazivosti místnosti**: "Live end" (živý konec) označuje část místnosti, kde jsou odrazy zvuku silnější (např. u reproduktorů), zatímco "dead end" (mrtvý konec) má silnější absorpci (např. u posluchače), což pomáhá kontrolovat ozvěny a dozvuk.
    
- **Zlepšení lokalizace a čistoty zvuku**: Absorpce v mrtvém konci snižuje rušivé odrazy, zatímco živý konec zachovává přirozený prostorový dojem, což zlepšuje čitelnost a směrovost zvuku.
    
- **Použití v nahrávacích a poslechových místnostech**: Tato akustická úprava se často používá v domácích studiích a poslechových místnostech pro dosažení vyvážené akustiky – ani příliš „mrtvé“, ani příliš „živé“.

<div style="page-break-after: always;"></div>

### zpracováno od chata - neharmonizováno s přednáškou:
#### Digitální záznam – výhody, nevýhody, vlastnosti
[[avt_zaznamazprac-1.pdf]]
- **Výhody**: 
	- Vysoká kvalita
	- odolnost vůči šumu
	- snadná manipulace s daty
	- Bezeztrátové kopírování 
	- Protichybové zabezpečení 
	- Ochrana proti kopírování 
	- Zdrojové kódování – komprese
- **Nevýhody**: Potřeba velkého úložného prostoru, kompresní ztráty.
- **Vlastnosti**: Diskrétní vzorkování, kvantování, možnost snadného editování.

#### Dithering, noiseshaping, sigma-delta
[[avt_zaznamazprac-1.pdf]]
- **Dithering**: Přidávání náhodného šumu pro zlepšení kvality při nízké bitové hloubce.
- **Noiseshaping**: Přesměrování šumu mimo slyšitelný rozsah.
- **Sigma-delta**: Modulační technika pro záznam signálů s vysokým rozlišením.

#### Protichybové zabezpečení – metody
[[avt_zaznamazprac-1.pdf]]
- **Metody**: Paritní bity, kontrolní součty, kódování opravy chyb (např. Hammingův kód).
- Používají se pro detekci a opravu chyb v digitálních datech.

#### Ochrana proti nelegálnímu kopírování – příklady
[[avt_zaznamazprac-1.pdf]]
- **Příklady**: DRM (Digital Rights Management), šifrování souborů, vodoznaky.
- Cílem je zabránit nelegálnímu šíření digitálního obsahu.

#### Komprese zvuku – princip
[[avt_zaznamazprac-1.pdf]]
- **Princip**: Redukce dat potřebných pro uchování zvuku pomocí odstranění redundance.
- Používá metody jako ztrátová komprese (MP3) a bezztrátová komprese (FLAC).

#### Magnetooptický záznam
[[avt_zaznamazprac-1.pdf]]
- Kombinuje magnetické a optické technologie pro ukládání dat.
- Využívá magnetické pole k záznamu dat na optické diskové médium.

#### Flash – princip záznamu a čtení
[[avt_zaznamazprac-1.pdf]]
- **Princip**: Flash paměť používá elektrická pole k uchovávání nábojů na křemíkových buňkách.
- Umožňuje rychlý přístup a opakované zápisy bez mechanických pohyblivých částí.
