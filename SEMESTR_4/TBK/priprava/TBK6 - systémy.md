1.               Jaké jsou základní komponenty radiových systémů?
	vysílače
	přijímače
	antény

2.               Jak se radiové trasy dělí z pohledu směrovosti přenosů signálů?
	simplex
		rádiové trasy přenášejí jen v jednom směru
	poloduplex
		radiové trasy přenáší informace v obou směrech
	duplex
		v 1 čase mohou uživatelé současně vysílat i přijímat

3.               Vyjmenujte a popište základní topologické struktury radiových spojů, uveďte příklady.
	PTP
		point to point
	PTM
		point to multipoint
	broadcast
	cellular
		tzv. buňkové sítě
4.               Jaké techniky se používají pro současné spojení více účastníků?
	TDMA
		Time Division Multiple Access
		Jednotlivý uživatelé komunikují v různých časových slotech
	FDMA
		Frequency Division Multiple Access
		Jednotlivý uživatelé komunikují v různých frekvenčních slotech
	CDMA
		Code Division Multiple Access
		Super secret vojenská technika. Všichni mají celé spektrum a furt, ale podle kódu si to rozdělí
5.               Jaké struktury se používají pro generování vysoce stabilních nosných? Nakreslete bloková schémata a popište funkci jednotlivých obvodů.
	PLL nebo DDS
	Phase Lock Loop
	![[PLL.png]]
[Nech si PLL vysvětlit od pana docenta](https://youtu.be/6VL0LILP1Wk?si=9izyjpdEHj1ZrV3G&t=2059)
	Krystalový oscilátor generuje fixní stabilní frekvenci
	VCO (Vnější oscilátor) generuje dost nestabilní frekvenci -> vnějším napětím můžu regulovat co za frekvenci.
	FD porovnává tyto dvě frekvence a podle toho nastavuje VCO
	Dále obsahuje děliče frekvence (OCXO má mnohem nižší frekvenci než VCO)
	Direct Digital Synthesis
	![[dds.png]]
[Nech si DDS vysvětlit od pana docenta](https://youtu.be/6VL0LILP1Wk?si=Rwz3gmCC5ku7AgjX&t=2744)
	Výstupní frekvence je definována fCLK a nastaveným krokem akumulátoruVýstupní frekvence je definována fCLK a nastaveným krokem akumulátoru
6.               Nakreslete a popište blokové schéma TX s přímou digitální modulací. Jaké jsou výhody a nevýhody této struktury?
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
		složité potlačení LO
7.               Nakreslete a popište blokové schéma TX s frekvenční konverzí. Jaké jsou výhody a nevýhody této struktury?
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
8.               Jaké parametry TX ovlivňují koncové výkonové zesilovače? Jaké jsou základní požadavky na ně kladené?
	Výkonové zesilovače PA zajišťují dostatečný výstupní výkon.
	 linearita a účinnost TX. 	
9.               Nakreslete a popište blokové schéma výkonového zesilovače s linearizací typu „pre-distortion“ a „digital pre-distortion“.
	![[PDDPD.png]]
[PDPDPDPDDPDDPDPDDPDDPDDP](https://youtu.be/6VL0LILP1Wk?si=7QnHJvA0mRn9_NbF&t=5306)
	Vstupní signál je upraven tak, aby výstupní signál nebyl nelinearitou PA ovlivněn.
	Ke vstupnímu signálu je nutné přičíst kubickou složku s vhodnou amplitudou a fází	

10.            Nakreslete a popište blokové schéma výkonového zesilovače s linearizací typu „envelope tracking“.
	![[enveleope tracking.png]]
	envelope == obálka signálu
	 Detektor obálky měří okamžitou amplitudu signálu 
	 Řízený spínaný regulátor nastavuje DC napájecí napětí na hodnotu těsně nad potřebnou saturační úrovní 
	 PA tak pracuje stále poblíž saturace
11.            Jaké nejdůležitější požadavky jsou kladené na VF a mikrovlnné přijímače?
	musí zajistit vysokou selektivitu příjmu velmi slabých i velmi silných signálů.
	Selektivní příjem 1 požadovaného kanálu
12.            Nakreslete blokové schéma přímozesilujícího přijímače („RF tuned receiver“). Jaké jsou výhody a nevýhody této struktury?  
	![[rftunerdreciever.png]]
	Výběr pracovního kanálu je prováděn pevným / přeladitelným filtrem.
	Přímozesilující RX vykazují špatnou selektivitu i rozsah přeladění.
13.            Nakreslete blokové schéma RX typu superhet s 1 směšováním. Jaké jsou základní principy činnosti? Jaké jsou výhody a nevýhody této struktury? 
	![[rx_superčhet.png]]
	Laditelný LO nastavíme přeladění na směšovači.
	$$w_{IF}=w_{LO}-w_{RF}$$
	RX typu superhet řeší většinu problémů příjmu i za velmi náročných podmínek. Na druhé straně přináší problémy se zrcadlovým příjmem.
14.            Co to je zrcadlové pásmo a jaké způsoby jeho potlačení  se používají?
	Postranní pásmo obsahující nazrcadlený signál od užitečného pásma na filtru IF.
	Potlačení:
		Preselektor
		Vícenásobné směšování
		Potlačení typ >60 dB
15.            Nakreslete blokové schéma RX s 2-násobným směšováním a popište funkci.
	![[rx2times.png]]
	1. IF Filtr má vysokou frekvenci. Zrcadlové pásmo lze díky tomu dobře filtrovat (je dál).
	2. IF filtr je na nižší frekvenci aby se signálem dalo pracovat lépe (ADC nemají rádi big RF)
	[[TBK 6 systémy 20.pdf#page=33]]
	červený text s frekvencema mu do testu nepište.
16.            Nakreslete blokové schéma přijímače s přímou konverzí do základního pásma. Jaké jsou výhody a nevýhody této struktury
	![[rxdirect.png]]
	Výhody:
		širokopásmový příjem
		levné, jednoduché, nic to nežere
	Nevýhody:
		LO může proniknout do antény, nelze filtrovat
		přináší problémy se zrcadlovým příjmem
17.            K čemu se používají a jak fungují obvody AGC?
	 přispívají k efektivnímu příjmu slabých i silných signálů
	 automatic gain-control
	 Řídí zisk zesilovačů tak, aby ani silná anténa blízko vysílači nepoškodila křechčí obvody z ním.
18.            Co to je transceiver? Jaký je rozdíl mezi duplexerem a diplexerem? Jak je možné konstruovat diplexery?
	V zařízeních pro přenosy poloduplex a plný duplex je nutné sloučit TX a RX do 1 antény
	prostě transciever + reciever
	konstruuje z duplexerů (VF přepínače)
	dixplexer = speciální slučovací filtr
19.            Vysvětlete techniky TDD a FDD.
	TDD
		Time division duplexing
		duplexery
		jeddoduché
		omezená přenosvá rychlost
	FDD 
		Frequency division duplexing
		dipluxery
		jdou s tím dělat brikule