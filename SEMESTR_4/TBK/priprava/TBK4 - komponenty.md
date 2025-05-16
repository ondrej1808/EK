#### Z jakých typických komponent se VF a mikrovlnné systémy skládají?
- Antény
- Oscilátor
- zesilovač
- atenuátor
- směšovač, modulátory, demodulátory
- Přepínače
- děliče výkonu
#### Proč je u všech důležité impedanční přizpůsobení a pomocí jakých parametrů se obvykle  kvantifikuje?
- Pro minimalizaci odrazů -> ztrát a správné fungování obvodů
- Kvantifikuje se podle parametru RL (Return loss), který chceme aby byl alespoň 10 dB (10% výkon se odráží), (20 dB lepší - 1 % odraženého výkonu) 
	- RL = -$dBS_{11}$
	- nebo dBS22 - odraz od výstupu; VSWR - poměr stojatých vln
#### Co jsou to MMIC?
- Mikrovlné monolitické integrované obvody
- Dneska vysoká integrace, vše v jednom MMIC - zesilovač až složitý demodulátor
#### Jaká jsou nejčastěji používaná propojovací vedení a jaké mají typické parametry?
- Koaxiální kabely
	- Charakteristická impedance 50 (75) $\Omega$
	- Malé průměry (<5 mm)
		- ohebné, vyšší mezní frekvence
		- vysoký útlum
	- Velký průměry (> 30 mm)
		- Tuhé, nízké mezní frekvence
		- nízký vložný útlum
	- mezní frekvence $f_{max}=\frac{c}{\pi(R_0+R_i)\sqrt{\varepsilon_r}}$
		- při této frekvenci se mění rozložení pole, idk sounds like ELD problém
	- Další parametry:
		- C/l - kapacita na délku (pF/m)
		- L/l - indukčnost na délku (uH/m)
		- vnitřní, vnější průměr
		- dielektrikum $\varepsilon_r$
#### Jaká jsou nejčastěji používaná planární konstrukční vedení, jaké mají typické parametry?
![[koplanární_vedení.png]]
![[real_koplanar.png]]
- Koplanární vedení
	- Substrát chceme z co nejmenšíma ztrátama - $tg \space\delta$
	- lze použít i FR4 (cuprextit) - $\varepsilon_r=4;tg\space\delta=0,01$
	- Čím více je stejnorodý (homogenní), tím lépe
	- Profesionální VF substráty, velmi drahé ($tg\space\delta\text{ až }0,001$)
	- Všechny země musí být na stejném potenciálu - hodně vias/prokovů
	- další parametry
		- šířka pásku (mm)
		- tlouštka pásku (um)
		- tloušťka substrátu (mm)
		- délka vedení (mm - cm)
		- odstup zemnící plochy S (desetiny mm)
	- Výhody:
		- Vyrábíme stejně jako PCB
		- Osazování SMD
		- Velmi dobrá zem na horní straně plošnáku (oproti mikropáskovému vedení)
		- můžeme měnit šířku pásku W a odstup zemní plochy S a zachovat tak stejnou Z_0
	- Nevýhody:
		- Zemnění -> prokovy
		- Hůře se realizují filtry, děliče výkonu
#### Jaké jsou standardní typy VF a mikrovlnných konektorů a jaké jsou jejich typické parametry?
- BNC - kHz - MHz
- SMA - lepší pro VF - MHz - GHz - standardní SMA konektor 24 GHz
	- SMA má různé rozměry: 3,5;2,9;2,4;1,8;1,0
	- menší rozměr pro vyšší kmitočty
- Parametry:
	- Impedance - co nejpřesněji $Z_0$
	- Perfektní stínění
	- Co největší opakovatelnost zašroubování a sešroubování
#### Co jsou to adaptéry?
- Změna zástrčka/zásuvka, změna rozměrů konektorů
- koax -> vlnovod a naopak
#### Co jsou to bezodrazové koncovky a jaké mají typické parametry?
- Rezistor co má přesně $Z_0$
- RL > 25 dB - černé těleso
- Širokopásmový 0 - 18 GHz
- Pomocí SMD rezistoru jen do cca 7 GHz, RL jenom > 15 dB, parazitní indukčnost a kapacita
#### Jaké jsou hlavní typy atenuátorů jaké jsou jejich hlavní parametry?
- Funkce - snižují výkon
- Typy:
	- Pevná hodnota
	- Proměnné analogové - spojitě měnitelná hodnota útlumu
	- Proměnné digitální - celočíselný počet hodnot útlumu 
- Parametry:
	- Důležitý parametr je RL
	- $Z_0$
	- L
#### Jaké jsou hlavní typy filtrů a jaké jsou jejich typické parametry?
- Typy:
	- **Pásmová propust**
	- **Pásmová zádrž**
	- Dolní propust
	- Horní propust
- Parametry:
	- Selektivita - jak moc široký band propouští/zadržuje
	- Potlačení interferencí
	- Potlačení šumu
	- EMI / EMC
	- Vysoké IL=insertion loss a nízké RL = return loss pro frekvence, které nechceme
	- Vysoké RL a nízké IL pro frekvence, které chceme 
#### Co jsou to diplexery, jaké jsou jejich typické parametry a kde se používají?
- Speciální filtr co slučuje přijimaný nebo vysílaný signál do antény
- Vysílaný a přijímaný signál musí mít jinou frekvenci
- Parametry: 
	- IL (=insertion loss) pro RX 
	- IL (=insertion loss) pro TX
	- frekvence pásma TX
	- frekvence pásma RX
	- dead band
- Použití: FDMA= radiové transceivery
	- **FDMA** stands for **Frequency Division Multiple Access**. It's a channel access method used in many radio communication systems, especially in older-generation wireless systems like 1G cellular networks.
#### Proč je se ve VF a mikrovlnném oboru používají speciální děliče výkonu?
- asi dostal mrtvici když psal tu otázku, jen jsem to zkopíroval
- Ve VF se nemůžou dva signály jen tak sloučit/rozdělit spojením/rozpojením dvou drátů
	- Vede to na paralelní kombinaci $Z_0$ -> tím pádem se rozbije impedanční přizpůsobení
#### Co jsou to rozbočovače a jaké jsou jejich typické parametry?
- Rozbočovače se používají tehdy kdy potřebujeme připojit nějaký signál na více výstupů
- Parametry:
	- Izolace mezi výstupy, typicky IS> 20dB
	- Fázový posun oproti vstupu
	- útlum jednotlivých výstupů IL závisí na vnitřní ztrátách a kolik výkon se dělí na daný výstup

#### Co jsou to směrové vazby a jaké jsou jejich typické parametry? Proč lze směrovou vazbu použít k měření odrazů?
![[directional_coupler.png]]
- Je to nesymetrický vazební obvod -> používáme ho k oddělení vlny dopadající a prostupující
- Parametry:
	- Insertion loss IL
	- Vazební útlum až 8 - 50 dB
#### Jaké znáte hlavní typy VF a mikrovlnných zesilovačů a jaké jsou jejich typické parametry?
- Typy:
	- úzkopásmové, širkopásmové
	- Nízký výkon, vysoký výkon
	- nízkošumové (LNA=low noise amplifier)
- Parametry:
	- Zisk G
	- Komprese P(-1dB)
	- Frekvenční pásmo
	- Šumové číslo F
	- Stejnosměrné napájení
#### Co jsou to směšovače a k čemu se ve VF a mikrovlnném oboru používají? Na jakém fyzikální  principu fungují, jak lze matematicky popsat? Jaké jsou jejich hlavní parametry?
- Nelineární součástka - která na výstupu produkuje frekvenční součty a rozdíly jednotlivých vstupní složek 
- Použivají se k up-konverzi, nebo down konverzi -> modulace/demodulace na/z nižšího/vyššího signálu
- Také IQ modulátory (in phase, quadrature - kombinace dvou ortogonálních signálů) -> QAM
- matemtický popis -> násobička
$$\begin{aligned}
u_{\mathrm{IF}}(t) &= k_2 V_{\mathrm{LO}} \cos(\omega_{\mathrm{LO}} t) \cdot V_{\mathrm{RF}} \cos(\omega_{\mathrm{RF}} t) \\
&= \frac{1}{2} k_2 V_{\mathrm{LO}} V_{\mathrm{RF}} \left[ \cos\left((\omega_{\mathrm{LO}} + \omega_{\mathrm{RF}}) t\right) + \cos\left((\omega_{\mathrm{LO}} - \omega_{\mathrm{RF}}) t\right) \right]
\end{aligned}$$
- užitečný signál na výstupu má frekvence:
	- $\omega_{IF}=\omega_{LO}+\omega_{RF}$
	- $\omega_{IF}=\omega_{LO}-\omega_{RF}$
- Parametry:
	- Frekvenční rozsah RF, IF, LO
	- Konverzní ztráty (zisk)
	- Izolace mezi RF,IF,LO
	- Útlumy mezi parazitními produkty
#### K čemu se používají VF a mikrovlnné oscilátory? Proč se nejčastěji používají VCO?
- Místní oscilátory pro down-konverzi
- Generace nosné frekvence pro vysílání
- VCO = voltage controlled amplifier
	- Varikap - napěťově závislá kapacita
	- Napětím měníme kapacitu -> změna frekvence LC oscilátoru
#### K čemu se používají násobiče frekvence a jaké jsou jejich hlavní parametry? Na jakém fyzikálním principu fungují?
- Využívají se na syntetizaci vysokých kmitočtů v řádu GHz
- 2x násobiče využívají nelinearitu druhého řádu (power reduction formula):
	- umocníme signál na druhou
	- Využijeme druhou harmonickou, ostatní musíme odfiltrovat
$$\begin{aligned}
v_2 &= k_2 v_1^2 = k_2 V_1^2 \cos^2(\omega_1 t + \psi) \\
&= \frac{1}{2} k_2 V_1^2 \left(1 + \cos(2 \omega_1 t + 2 \psi)\right)
\end{aligned}
$$
- 3x násobiče využívají nelinearitu třetího řádu:
	- Umocníme signál na třetí
	- Využijeme třetí harmonickou, ostatní musíme odfiltrovat 
	$$\begin{aligned}
v_2 &= k_2 v_1^3 = k_2 V_1^3 \cos^3(\omega_1 t + \psi) \\
&= \text{po filtraci} =\frac{1}{4} k_2 V_1^3 \left(\cos(3 \omega_1 t + 3 \psi)\right)
\end{aligned}
$$
- Parametry:
	- Nominální vstupní výkon $P_{in}$
	- Konverzní ztráty
	- Potlačení nežádoucích signálů
#### Jaké znáte hlavní typy VF přepínačů a jaké jsou jejich hlavní parametry? Jaké přepínací komponenty se používají a jak se elektronicky řídí?
- Typy:
	- SPST - single pole single throw = jeden vstup, jeden přepínaný výstup, klasický vypínač 1
	- SPDT - single pole double throw - vypínač šestka
	- SP4T - double pole quad throw
- Přepínací komponenty:
	- FET - polem řízený tranzistor - řídíme stejnosměrným napětím mezi G a S
	- PIN dioda - dáme diodě stejnosměrné předpětí, tím jí otevřeme
- Parametry:
	- Útlum
	- Izolace při rozepnutí