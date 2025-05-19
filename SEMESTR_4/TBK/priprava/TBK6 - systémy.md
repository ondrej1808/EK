#### Jaké jsou základní komponenty radiových systémů?
	vysílače
	přijímače
	antény
- TX = Radiový vysílač
- Anténa
- RX = Radiový přijímač
#### Jak se radiové trasy dělí z pohledu směrovosti přenosů signálů?
	simplex
		rádiové trasy přenášejí jen v jednom směru
	poloduplex
		radiové trasy přenáší informace v obou směrech
	duplex
		v 1 čase mohou uživatelé současně vysílat i přijímat
- Simplexní - signál pouze jedním směrem
- Poloduplexní - signál oběma směry ale NE najednou
- Plně duplexní - signál oběma směry najednou
- Simplexní
	- PTP - point to point
	- Radiový terminál obsahuje buď RX nebo TX
	- Příklad: FM-rádio, GPS, DVB-T
- Poloduplexní
	- Radiový terminál buďto přijímá nebo vysílá
	- nejčastějí TDD= time division duplexing
	- když je TDD hodně rychlé je to skoro duplex, ale s nižší datovou rychlostí
	- Příklad: Vysílačka, WLAN
- Plný duplex
	- Bez zásadních omezení
	- Provoz typu FDD = frquency division duplexing
	- Vysílání a přijímání je na rozdílných frekvencích
	- Frekvence musí být dostatečně vzdálené
	- Pro sloučení TX a RX do jedné antény se používají diplexery = slučovací filtr
	- Příklady: Vysokorychlostní datové trasy, mobilní komunikace
#### Vyjmenujte a popište základní topologické struktury radiových spojů, uveďte příklady.
	PTP
		point to point
	PTM
		point to multipoint
	broadcast
	cellular
		tzv. buňkové sítě- PTP = point to point
	- Směrové parabolické antény
	- frekvence vyšší GHz (>10 GHz)
	- Aplikace:
		- Nahrazení metalických nebo optických sítí
		- Vysokorychlostní páteřní radiové trasy
		- Propojení základových stanice (BS) mobilních sítí i WLAN
		- Satelitní trasy
- PTM = point to multipoint
	- Master - slave
	- Všesměrová (omni-directional) anténa u mastera
	- Slaves jsou směrovanější antény
	- Terminály mohou být stacionární i mobilní
	- Aplikace: WLAN, mobilní buňkové sítě, senzorové sítě
- Broadcast
	- Podobný PTM
	- Ale provoz je simplexní
	- VKV FM rádio, DVB-T, DAB
- Cellular
	- Systém více speciálních PTM buněk
	- Satcionární základové stanice (BS)
	- Mobilní terminály
	- Zaručení automatického předávání (hand-over) z jedné buňky do druhé
	- Často takké broadcast vrstvy
	- Velmi složité řízení ve frekvenční i časové oblasti

#### Jaké techniky se používají pro současné spojení více účastníků?
	TDMA
		Time Division Multiple Access
		Jednotlivý uživatelé komunikují v různých časových slotech
	FDMA
		Frequency Division Multiple Access
		Jednotlivý uživatelé komunikují v různých frekvenčních slotech
	CDMA
		Code Division Multiple Access
		Super secret vojenská technika. Všichni mají celé spektrum a furt, ale podle kódu si to rozdělí- FDMA - Frequency dividion multiple access
	- Jednotliví uživatelé komunikují ve svém kanálu
	- Uživatelé jsou rozdělení po spektru
	- Příklady: FM rádio, GSM
- TDMA - Time division multiple access
	- Jedotliví uživatelé komunikují v různých časových oknech (slotech)
	- Dělení uživatelů v čase
	- Každý uživatel má 100 % spektra, ale po dobu svého okna
	- WLAN, GSM
- CDMA - code division multiple access
	- Používané v military
	- Každý uživatel komunikuje na 100 % spektru a 100 % času
	- Potřebujeme ale velkou část spektra
	- Je použité ortogonální kódování (každý kód je rozluštitelný od ostatních)
	- Stejné frekvenční pásmo B může být sdíleno vysokým počtem uživatelů
	- Pásmo musí být široké a může být špatně využito
	- WLAN, UMTS

#### Jaké struktury se používají pro generování vysoce stabilních nosných? Nakreslete bloková schémata a popište funkci jednotlivých obvodů.
	PLL nebo DDS
	Phase Lock Loop
![[SEMESTR_4/TBK/image/PLL.png]]


[Nech si PLL vysvětlit od pana docenta](https://youtu.be/6VL0LILP1Wk?si=9izyjpdEHj1ZrV3G&t=2059)
	Krystalový oscilátor generuje fixní stabilní frekvenci
	VCO (Vnější oscilátor) generuje dost nestabilní frekvenci -> vnějším napětím můžu regulovat co za frekvenci.
	FD porovnává tyto dvě frekvence a podle toho nastavuje VCO
	Dále obsahuje děliče frekvence (OCXO má mnohem nižší frekvenci než VCO)
	Direct Digital Synthesis
	![[dds.png]]
[Nech si DDS vysvětlit od pana docenta](https://youtu.be/6VL0LILP1Wk?si=Rwz3gmCC5ku7AgjX&t=2744)
	Výstupní frekvence je definována fCLK a nastaveným krokem akumulátoruVýstupní frekvence je definována fCLK a nastaveným krokem akumulátoru- Nosná musí být extrémně stabilní
![[pll.png]]
- PLL = phase locked loop = fázový závěs
	- OCXO = over controlled crystal oscilator
		- Extrémně stabilní , ale jen nízké frekvence (< 100 MHz)
	-  $f_{out}=f_{ref}N_1N_2$
	- z OCXO je přivedena frekvence do fázového detektoru, do kterého je zároveň přivedena vydělená výstupní frekvece
	- Pulsy, které vychází z fázového detektoru jsou přefiltrovány a výsledné napětí řídí VCO (napětím řízený oscilátor), který generuje výsledný kmitočet
	- Pokud by se VCO chtěl rozhodit tak ho fázový detektor kopne aby se dal zpátky do richtigu

- DDS = direct digital synthesis
![[DDS.png]]
- Prostě robíme rovnou z chipu výstupní frekvenci, tím že v určité časy posíláme do DA převodníku napětí, které má mít v tom čase výstupní kmitočet
- Poté odfiltrujeme, abychom se zbavili aliasingu

#### Nakreslete a popište blokové schéma TX s přímou digitální modulací. Jaké jsou výhody a nevýhody této struktury?
	![[TXprima.png]]
[Nech si to vysvětlit od šéfa](https://youtu.be/6VL0LILP1Wk?si=Lbv0BKxDVXLBXb_2&t=3354)
	FIL1 → potlačuje parazitní IM produkty modulátoru 
	PA → určuje výstupní výkon 
	FIL2 → potlačuje IM produkty PA
	LPF = Low Pass Filter
	I = in channel (nosná)
	Q = quadrature (nosná posunuta o 90°)
	Výhody:
		umožňuje širokopásmové přeladění
		malé rozměry, nízký příkon
	Nevýhody:
		kvadraturní chyby na vyšších f
		složité potlačení LO![[iq_modulator.png]]
- Výstupní signál:
$$s_{TX}=v_I(t)cos(\omega_0t)+v_Q(t)sin(\omega_0t)$$
- I a Q signály z digitální podoby převedeme do analogové, vyfiltrujeme a za stálého směšování smísíme ve směšovači s sin/cos. Poté smíšené složky složíme dohromady, vyfiltrujeme IM produkty, zesílíme a vyfiltrujeme další IM produkty a poté vyšleme anténou
- Výhody:
	- Moderní jednoduchá struktura
	- Širokopásmové přeladění
	- 1xPLL, malé rozměry, nízky DAC příkon
	- Vstupní signály jsou v base band -> malé nároky na DAY
- Nevýhody
	- Kvadraturní chyby na vyšších GHz frekvencích
	- Složité potlačení LO = lokální oscilátor, parazitní vyzařování do antény

#### Nakreslete a popište blokové schéma TX s frekvenční konverzí. Jaké jsou výhody a nevýhody této struktury?
![[TXfrekvence.png]]
[Šéf ti řekne jak to je drahý](https://youtu.be/6VL0LILP1Wk?si=BTjNT8L6mVCKGYPS&t=3939)
$$\omega_0=\omega_{IF}+\omega_{LO}$$
	Výhody:
		Nižší kvadraturní chyby
		Lze potlačit vyzařování LO
		Lineárnější
	Nevýhody:
		složitější
		větší, vyšší příkon, cena
		2x LO
- basically si modulaci vyřešíme na nižším kmitočtu a pak za stáleho směšování up-konvertujeme frekvenci na vyšší, kterou vysíláme
- Výhody:
	- Na nízkých frekvencíh jsou nižší kvadraturní chyby
	- Lze dokonale potlačit vyzařování LO do výstupního signálu a do antény
	- Lepší linearita mofulátoru
- Nevýhody
	- Složitější struktura
	- 2x LO
	- Vetší rozměry, DC příkon, cena

#### Jaké parametry TX ovlivňují koncové výkonové zesilovače? Jaké jsou základní požadavky na ně kladené?
	Výkonové zesilovače PA zajišťují dostatečný výstupní výkon.
	 linearita a účinnost TX. 	
	 - Parametry
		- Účinnost: Aby se IPhone nevybil
		- Komprese $P_{-1dB}$
		- IM produkty - interference, rozšiřování spektra
		- Účinnost a linearita jdou většinou proti sobě
- Linearita
	- Ovlivňuje okrajové stavy x-QAM
	- nelinearity způsobují vyšší bit-error-rate
#### Nakreslete a popište blokové schéma výkonového zesilovače s linearizací typu „pre-distortion“ a „digital pre-distortion“.
![[PDDPD.png]]
[PDPDPDPDDPDDPDPDDPDDPDDP](https://youtu.be/6VL0LILP1Wk?si=7QnHJvA0mRn9_NbF&t=5306)
	Vstupní signál je upraven tak, aby výstupní signál nebyl nelinearitou PA ovlivněn.
	Ke vstupnímu signálu je nutné přičíst kubickou složku s vhodnou amplitudou a fází	
![[PD&DPD.png]]
- PD= Pre distortion
	- Používá zesilovač třídy A s mírnou nelinearitou
	- Vstupní signál upravíme tak, aby nebyl nelinearitami ovlivněn
	- Přidáme k vstupnímu signálu kubickou složku takovou (amplituda a fáze musí bý cajk) aby se nelinearitou zesilovače zabila (nezabije nám signál)
- DPD = digital pre distortion
	- Rozbijeme signál digitálně a pak ho teprve modulujeme
	- Přesnější linearizace

#### Nakreslete a popište blokové schéma výkonového zesilovače s linearizací typu „envelope tracking“.
![[enveleope tracking.png]]
	envelope == obálka signálu
	 Detektor obálky měří okamžitou amplitudu signálu 
	 Řízený spínaný regulátor nastavuje DC napájecí napětí na hodnotu těsně nad potřebnou saturační úrovní 
	 PA tak pracuje stále poblíž saturace
- Prakticky se velmi těžko realizuje - složitý obvod
- Široce používaný v mobilních komunikacích

#### Jaké nejdůležitější požadavky jsou kladené na VF a mikrovlnné přijímače?
- Přijímané signály můžou mít velmi nízké úrovně
	- Protože vysíláme nízkými výkony
	- Velké FSL= free space loss
- V okolí můžou existovat
	- Další FDMA kanály
	- jiné bezdrátové služby
	- Rušivé signály
	- Dycky šum
- Selektivní příjem jednoho kanálu
- Potlačení blízkých a vzdálených kanálů (Necheme slyšet blaník, impuls a wifi najednou)	musí zajistit vysokou selektivitu příjmu velmi slabých i velmi silných signálů.
	Selektivní příjem 1 požadovaného kanálu

#### Nakreslete blokové schéma přímozesilujícího přijímače („RF tuned receiver“). Jaké jsou výhody a nevýhody této struktury?  
![[rftunerdreciever.png]]
	Výběr pracovního kanálu je prováděn pevným / přeladitelným filtrem.
	Přímozesilující RX vykazují špatnou selektivitu i rozsah přeladění.
#### Nakreslete blokové schéma RX typu superhet s 1 směšováním. Jaké jsou základní principy činnosti? Jaké jsou výhody a nevýhody této struktury?
![[rx_superčhet.png]]
	Laditelný LO nastavíme přeladění na směšovači.
	$$w_{IF}=w_{LO}-w_{RF}$$
	RX typu superhet řeší většinu problémů příjmu i za velmi náročných podmínek. Na druhé straně přináší problémy se zrcadlovým příjmem.
#### Co to je zrcadlové pásmo a jaké způsoby jeho potlačení  se používají?
	Postranní pásmo obsahující nazrcadlený signál od užitečného pásma na filtru IF.
	Potlačení:
		Preselektor
		Vícenásobné směšování
		Potlačení typ >60 dB
#### Nakreslete blokové schéma RX s 2-násobným směšováním a popište funkci.
![[rx2times.png]]
	1. IF Filtr má vysokou frekvenci. Zrcadlové pásmo lze díky tomu dobře filtrovat (je dál).
	2. IF filtr je na nižší frekvenci aby se signálem dalo pracovat lépe (ADC nemají rádi big RF)
	[[TBK 6 systémy 20.pdf#page=33]]
	červený text s frekvencema mu do testu nepište.
#### Nakreslete blokové schéma přijímače s přímou konverzí do základního pásma. Jaké jsou výhody a nevýhody této struktury
![[rxdirect.png]]
	Výhody:
		širokopásmový příjem
		levné, jednoduché, nic to nežere
	Nevýhody:
		LO může proniknout do antény, nelze filtrovat
		přináší problémy se zrcadlovým příjmem
#### K čemu se používají a jak fungují obvody AGC?
	 přispívají k efektivnímu příjmu slabých i silných signálů
	 automatic gain-control
	 Řídí zisk zesilovačů tak, aby ani silná anténa blízko vysílači nepoškodila křechčí obvody z ním.
#### Co to je transceiver? Jaký je rozdíl mezi duplexerem a diplexerem? Jak je možné konstruovat diplexery?
	V zařízeních pro přenosy poloduplex a plný duplex je nutné sloučit TX a RX do 1 antény
	prostě transciever + reciever
	konstruuje z duplexerů (VF přepínače)
	dixplexer = speciální slučovací filtr
#### Vysvětlete techniky TDD a FDD.
TDD
	Time division duplexing
	duplexery
	jeddoduché
	omezená přenosvá rychlost
FDD 
	Frequency division duplexing
	dipluxery
	jdou s tím dělat brikule