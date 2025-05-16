#### Napište definice pro: Množství tepla v tělese, Rychlost průtoku tepla tělesem, Teplotní gradient (tepelná vodivost)
- Množství tepla v tělese
$$Q=mcT$$
- Rychlost průtoku tepla tělesem
$$\frac{dQ}{dT}=-kS\frac{dT}{dX}$$
- Teplotní gradient
$$\frac{dT}{dx}$$
#### Odporové kovové teplotní senzory (RTD): Uveďte alespoň 2 typické materiály pro teplotní senzory, uveďte typický teplotní rozsah, napište základní rovnici pro aproximaci průběhu odporu v malém rozmezí teplot (0 - 100°C)
- NI (nižší teplory, nízká cena, nelineární), -60°C - 120 °C
- Pt (vysoká cena, lineární, nejběžnější) - 260°C - 630°C
$$R=R_0(1+\alpha\vartheta+\beta\vartheta^2+\gamma(\vartheta-100)\vartheta^3)$$
- $\vartheta$ - AKtuální teplta ve stupních celsia
- $\alpha, \beta, \gamma$ - Kalibrační koeficienty závislé na materiálu senzoru

#### Vyhodnocování signálu z odporových kovových teplotních senzorů (RTD): Nakreslete zjednodušeně obvodové zapojení pro vyhodnocování teploty
![[rtd.png]]
#### Odporové polovodičové teplotní senzory s termistory: Napište rozdíl mezi termistory NTC, PTC, nakreslete typické převodní charakteristiky, Nakreslete zjednodušené obvodové zapojení pro vyhodnocování teploty
- PTC termistor (Positive temperature coefficient)
	- Odpor roste s rostoucí teplotou, 
	- Používá se například pro chranu obvodů - při přehřátí bvzroste odpor a omezí proud
![[PTC_chka.png]]
- NTC termistor (Negative temperature coefficient)
- Odpor klesá s rostoucí teplotou
- Často se používá jako teplotní čidlo (např. v notebooku, nabíječce😬, baterii)
![[ntc.png]]
#### Odporové polovodičové teplotní senzory monokrystalické : Nakreslete a vysvětlete základní principy činnosti.
- Polovodičový monokrystalický Si senzor (senzor s odporem šíření)
- Princip:
	- Odpor šíření se uplaťnuje v místě styku kovového hrotu s polovodičem
	- Odpor závisí na rezistivitě $\rho$ a poloměru kontaktu $r$
	- Využívá se kladná teplotní součinitel (pro Si v rozmezí přibližně 50 až 150 °C)
	- S rostoucí teplotou klesá pohyblivost volných nosičů náboje.
![[kremik_teplomer.png]]
#### Teplotní senzory s p-n přechodem: Napište základní rovnici popisující proud přechodem (Shockley rovnice), Napište nebo odvoďte rovnici pro teplotní závislost napětí na přechodu p-n na teplotě, Nakreslete teplotní závislost saturačního proudu Is = f (teplota)
- Proud diodou:
	$$I=I_s(e^{\frac{n\frac{U}{kT}}{q}}-1)$$
- závislost napětí na přechodu p-n na teplotě
$$U\approxeq\frac{\frac{kT}{q}}{n}ln\frac{I}{I_S}$$
- Tepotní závislost saturačního proudu $I_S=f(T)$
![[teplotni_zavislost.png]]
#### Citlivost teplotních senzorů s p-n přechodem: Napište princip odvození citlivosti p-n přechodu, Napište typickou číselnou hodnotu citlivosti
- lze odvodit že platí
$$\beta=\frac{dU}{dT}=\frac{k}{nq}ln\frac{I}{I_S}$$
- pro běžné Si je $I_S=10^{-10} \text{ A a } I=10^{-4}\text{ A}$ je
$$\beta=-2,1\text{ mVK}^{-1}$$

#### Teplotní senzory s p-n přechodem: Nakreslete typický průběh teplotní závislosti napětí na přechodu p-n U = f(teplota) pro dva různé proudy I přechodem
![[pn_teplotni.png]]
#### Vyhodnocování informace z teplotního senzoru s p-n přechodem: Nakreslete zjednodušené základní zapojení teploměru s přechodem p-n, vysvětlete proč je nutné používat proudový zdroj pro napájení přechodu p-n, jak je tvořen proudový zdroj na Vašem obrázku
![[zpracovani_teplota_pn_prechod.png]]
- Pro napájení p-n přechodu je nutné použít proudový zdroj, protože:
	- Úbytek napětí na přechodu p-n, závísí na teplotě pouze při konstantním proudu
	- Pokud by proud kolísal, měření napětí by nebylo spolehlivé, protože by se měnilo i v závislosti na proudu$\rightarrow$ vznikla by chyba měření teploty.
	- V zapojení je proudový zdroj vytvořen pomocí operačního zesilovače, referenčního napětí a odporu, které nastavují konstantní proud tekoucí diodou.
	- Dioda slouží jako teplotní čidlo, protože při konstantním proudu má změnu úbytku napětí přibližne -2 mV/°C
	- Výstupní napětí tedy lineárně klesá s rostoucí teplotou, což umožňuje přímé vyhodnocení
#### Termoelektrické kovové teplotní senzory: nakreslete a vysvětlete základní princip činnosti termočlánku
![[termoelektrické teplotni senzory.png]]
- Princip
	- Dva různé kovy jsou spojeny svařením/pájením nebo výjimečně mechanicky. místo kovů lze použí i polovodiče
- Seebackův jev:
	- Jsou-li spojeny dva vodiče z různých kovů do uzavřeného obvodu a mají-li spoje různé teploty $T_1$ a $T_2$, protéká obvodem elektrický proud.
	- Pokud obvod rozpojíme, na svorkách naměříme elektromotorické napětí, které je úměrné rozdílu teplot
#### Termoelektrické teplotní senzory: Uveďte 3 základní typy kovových termočlánků. Uveďte typické materiály, Nakreslete 3 typické charakteristiky.
- Chromel-Konstantan (E křivka)
	- Nejvyšší výstupí napětí ze všech běžných termočlánků
	- Vhodný pro teploty nad 870°C ve vakkuu nebo inertní atmosféře
- Platina-Rhodium (S a R křivky)
	- Vysoká odolnost proti oxidaci a korozi
	- Doporučený rozsah teplot až do 1540°C
- Wolfram-Rhodium (C křivka)
	- Určený pro extrémně vysoké teploty až přes 2760°C
	- Použití: 
		- Metalurgie
		- Vakuové pece
- A co nejčastěji používané K a J termočlánky 😢?
![[termoclanky.png]]

#### Termoelektrické teplotní senzory: Nakreslete zjednodušený princip elektronického zapojení pro vyhodnocování signálu z termočlánků
![[vyhodnocovani_termoclanku.png]]
#### Bezkontaktní senzory infračerveného záření s termoelektrickým článkem: Nakreslete zjednodušeně strukturu jednoho termočlánku na čipu. Jak je zabráněno šíření teploty po ploše čipu
![[infra.png]]
- Termočlánek je umístěn na tenké izolační membráně, která odděluje horký a studený spoj
- Pod membránou je mezra (vzduch nebo vakkuum), která brání tepelnému vedení
- Substrát slouží jako chladič pro studený spoj, čímž udržuje stabilní teplotní rozddíl
- Celkově je konstrukce navržena tak, že teplo z horkého spoje nemohlo unikat po povrchu čipu
#### MEMS bolometr: Nakreslete zjednodušeně strukturu jednoho MEMS bolometru na čipu. Jak je zabráněno šíření teploty po ploše čipu.
![[mems_bolometr.png]]
- Absorbční vtsva bolometru je uchycena na tenkých nosných ramenech (většinou z dielektrika), která mají nízkou tepelnou vodivost.
- Pod ní je vytvořena vzduchová nebo vakkuová mezera (dutina v substrátu), která dále tepelně izoluje bolometr od zbytku čipu
- Tím je zajištěno, že teplo z dopadajícího záření zůstává lokalizováno v bolometru a nešíří se do okolí, což zvyšuje citlivost
#### MEMS bolometr: Nakreslete zjednodušeně strukturu bolometrické matice na čipu
![[dalsi mems bolometr.png]]

#### Teplotní senzor SAW: Nakreslete a vysvětlete princip činnosti, Nakreslete a vysvětlete elektronický vyhodnocovací obvod
Ind
- Využívá teplotní závislosti rychlosti šíření povrchové akustické vlny v materiálu

#### Teplotní senzory pro měření kryogenních teplot: Napište alespoň 4 základní typy teplotních senzorů, Jaké nevýhody mají termočlánkové, Do jakých nejmenších teplot je možné senzory použít.
- Termoelektrické články (termočlánky)
	- Výhody: jendoduché, levné
	- Nevýhody: malé a nestabilí termoelektrické napětí
	- Nejnižší použitelná teplota: přibližně 10 K
- Odporové senzory
	- Kovové (např.: PT100): 10-90 K
	- Uhlíkové: až 1 K, výjimečně až 0,01 K
	- Termistory: do 20 K
- Senzor s p-n přechodem (např. Si dioda)
	- Citlivost: 55 mV/K pro Si
	- Vhodné pro rozsah 1 - 30 K
- Indukční princip
	- vhodné pro velmi nízké teploty: mK až 5 K
- Kapacitní teplotní senzory
	- Princip: změna permitivity s teplotou
- Termočlánky + a -
	- Jsou levné a jednoduché, ale generují nízké a nestabilní napětí, což může komplikovat měření při nízkých teplotách