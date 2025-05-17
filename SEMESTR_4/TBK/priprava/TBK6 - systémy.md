#### Jaké jsou základní komponenty radiových systémů?
- TX = Radiový vysílač
- Anténa
- RX = Radiový přijímač
#### Jak se radiové trasy dělí z pohledu směrovosti přenosů signálů?
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
- PTP = point to point
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
- FDMA - Frequency dividion multiple access
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
- Nosná musí být extrémně stabilní
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
![[iq_modulator.png]]
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
	- Složité potlačení LO=lokální oscilátor, parazitní vyzařování do antény

#### Nakreslete a popište blokové schéma TX s frekvenční konverzí. Jaké jsou výhody a nevýhody této struktury?
![[prima_frekvecni_konverze.png]]
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
- Parametry
	- Účinnost: Aby se IPhone nevybil
	- Komprese $P_{-1dB}$
	- IM produkty - interference, rozšiřování spektra
	- Účinnost a linearita jdou většinou proti sobě
- Linearita
	- Ovlivňuje okrajové stavy x-QAM
	- nelinearity způsobují vyšší bit-error-rate
#### Nakreslete a popište blokové schéma výkonového zesilovače s linearizací typu „pre-distortion“ a „digital pre-distortion“.
![[PD&DPD.png]]
- PD= Pre distortion
	- Používá zesilovač třídy A s mírnou nelinearitou
	- Vstupní signál upravíme tak, aby nebyl nelinearitami ovlivněn
	- Přidáme k vstupnímu signálu kubickou složku takovou (amplituda a fáze musí bý cajk) aby se nelinearitou zesilovače zabila (nezabije nám signál)
- DPD = digital pre distortion
	- Rozbijeme signál digitálně a pak ho teprve modulujeme
	- Přesnější linearizace

#### Nakreslete a popište blokové schéma výkonového zesilovače s linearizací typu „envelope tracking“.
![[ET_nevola_domu_nechyta_GSM.png]]
- Detektor obálky měří okamžitou hodnotu amlitudy signálu
- Spínaný zdroj nastavuje napájení těsně nad výškou obálky, abychom nemuseli na výkonových tranzistorech mít takový úbytek
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
- Potlačení blízkých a vzdálených kanálů (Necheme slyšet blaník, impuls a wifi najednou)
12.            Nakreslete blokové schéma přímozesilujícího přijímače („RF tuned receiver“). Jaké jsou výhody a nevýhody této struktury?  

13.            Nakreslete blokové schéma RX typu superhet s 1 směšováním. Jaké jsou základní principy činnosti? Jaké jsou výhody a nevýhody této struktury? 

14.            Co to je zrcadlové pásmo a jaké způsoby jeho potlačení  se používají?

15.            Nakreslete blokové schéma RX s 2-násobným směšováním a popište funkci.

16.            Nakreslete blokové schéma přijímače s přímou konverzí do základního pásma. Jaké jsou výhody a nevýhody této struktury

17.            K čemu se používají a jak fungují obvody AGC?

18.            Co to je transceiver? Jaký je rozdíl mezi duplexerem a diplexerem? Jak je možné konstruovat diplexery?

19.            Vysvětlete techniky TDD a FDD.