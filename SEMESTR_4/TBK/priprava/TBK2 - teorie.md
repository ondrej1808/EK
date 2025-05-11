#### Za jakých podmínek přestává být použitelná většina parametrů zavedených v „teorii obvodů“ (zejména napětí a proud) a proč?
- Když je polovina vlnové délky přenášeného signálu srovnatelná s rozměry obvodů
#### Jaký je rozdíl mezi vlnami šířícími se ve volném prostředí a vlnami vedenými?
- Vlny které se šíří ve volném prostředí se s rostoucí vzdáleností rozptylujou, ať už má anténna jakoukoliv směrovost
	- Výkon se s přibívající vzdáleností snižuje -> Inverse square law -> plocha koule roste s druhou mocninou poloměru
- Vlna vedenná je vedena nějakým vedením
	- E a H jsou koncentrovány kolem nějaké metalické struktury
	- Přenášený výkon je soustředěný -> nerozptyluje se do volného prostoru
	- Výkon se uvnitř vodiče nešíří
#### Jaká vedení s videm TEM se nejčastěji používají?
- TEM = Transversálně elektromagnetický mód - E a H jsou kolmé ke směru šíření
- Koaxiální
- mikropáskové
#### Jaký výkon (na libovolné frekvenci) se šíří uvnitř vodičů a jaký vně vodičů?
- **Uvnitř** vodičů se výkon **nešíří**
- **Vně** vodičů se **šíří** celý výkon
#### Co jsou to napěťové vlny, jaké přinášejí zjednodušení? Jaký je vztah napěťových vln a napětí na vedení?
- Napěťová vlna je celkové **rozložení E v rovinně xy**
- Pro koaxiální kabel ($\text{C}_1$ je vnitřní průměr vodiče, $\text{C}_2$ je vnější průměr izolace mezi vodičem a stíněnním):
$$\widehat V=\int_{C_1}^{C_2}\widehat{\overrightarrow E}\cdot d\overrightarrow l$$
- Dvě vlny: 
	- $\widehat{{\text{V}}}^+$ - vlna dopadající
	- $\widehat{{\text{V}}}^-$ - vlna odražená
- Vztah mezi napěťouvou vlnou a napětím: 
	- Dosasím do $\widehat{{\text{V}}}(\text{z})$ tak dostanu časový průběh napětí v místě
	- Nesmím zapomenout že všude na vedení je zároveň odražená $\widehat{{\text{V}}}^-$ a dopadající vlna $\widehat{{\text{V}}}^+$
- Zjednodušení které přináší:
	- Nemusíme počítat E v x, y pro každé z
	- Jednodušší popis vedenných vln
	- Umožňují definici parametrů: $S,T,\Gamma$
	
#### Jaké je řešení telegrafní rovnice?
- Telegrafní rovnice popisuje rozložení napětí a proudu podél vedení
- Telegrafní rovnice:
$$\frac{d^2\widehat{{\text{V}}}(z)}{dz^2}+\widehat{k} ^2\widehat{{\text{V}}}(z)=0$$
- Řešení Telegrafní rovnice za podmínky $\lambda^2+\widehat{k} ^2=0$
$$\widehat{V}(z)=\widehat{V}^+e^{-j\widehat{k}z}+\widehat{V}^-e^{+j\widehat{k}z}$$
	- $\widehat{V}(z)^+$ je dopadající napěťová vlna
	- $\widehat{V}(z)^-$ je odražená napěťová vlna
	- $\widehat{k}$ je konstanta šíření
#### Jaký je rozdíl mezi vlnovou impedancí a charakteristickou impedancí?
[[TBK 2 teoretické základy 25.pdf#page=15|Přednáška]]
- Charakteristická impedance:
$$\widehat Z_0=\frac{\widehat{V}(z)}{\widehat{I}(z)}=\sqrt{\frac{R+j\omega L}{G+j\omega C}}$$
- Vlnová impedance
$$\widehat Z=\frac{\widehat{E}_x(z)}{\widehat{H}_y(z)}=\sqrt{\frac{j\omega\mu}{j\omega\varepsilon+\sigma}}$$
- Rozdíl:
	- Charakteristická impedance je uvařena z fázorů napětí a proudu, můžeme z ní spočítat proud $I=\frac{V}{Z_0}=\frac{V^++V^-}{Z_0}$
	- Vlnová impedance je uvařena z fázorů intenzity el. proudu a intenzity magnetického pole, ve vzduchu je vlnová impedance $120\pi\approxeq377\space\Omega$
#### Definice koeficientů odrazu a přenosu na vedení s impedancí **_Z**_0_. Jak se mění koeficient odrazu podél vedení (popište v polárním diagramu)?
[[TBK 2 teoretické základy 25.pdf#page=17|Přednáška]]
##### Koeficient odrazu $\Gamma$
- Koeficient odrazu je komplexní číslo, jehož velikost je menší nebo rovno jedné
- Vyjadřuje jak velká část vlny se odrazila vzhledem k vlně dopadající
$$\widehat \Gamma=\frac{\widehat{V}^-}{\widehat{V}^+}=\frac{\widehat{V}_m^-e^{-j\widehat kz}}{\widehat{V}_m^-e^{-j\widehat kz}}=\widehat{\Gamma}_0e^{+j2\widehat kz}=\Big| \Gamma_0 \Big|e^{j\varphi_0}e^{+j2\widehat kz}$$
- Většinou určujeme rovnou z impedance $Z_0=50\space\Omega\text{ a } Z_L$
$$\Gamma = \frac{\widehat Z_L-Z_0}{\widehat Z_L+Z_0}$$
- Transformace koeficientu odrazu $\Gamma$ po vedení
	- Na bezeztrátovém vedení není žádný útlum amplitudy ($\alpha = 0$ ve vlnovém fázoru $\widehat k$), tím pádem:
	- $\widehat k = \beta - j\alpha = \beta$
	- $\widehat\Gamma_0=\Big|\widehat\Gamma_0\Big|e^{j\varphi_0}e^{j2\beta z}$
	- exponenciála $e^{j2\beta z}$ nám říká jak se mění koeficent $\Gamma$ s délkou nějakoého vedení (Gamma nás zajímá vždy na začátku z=0, nebo na konci z = d)
	- Jelikož je v argumentu dvojka, tak se exponenciála na polárním diagramu opakuje každý $z = 2/\beta$
	- Jak můžeme tušit z elmag. pole, tak $\beta = 2\pi / \lambda$ takže pro $\lambda / 2$ se fáze=argument exponenciály otočí o $2\pi$=360°, tedy pro $\lambda / 4$ to bude 180°=$\pi / 2$
	- Tohoto můžeme využít v mikrovlné technice, kde $\lambda/4$ jsou jednotky mm až jednotky cm, např. pro transformaci L -> C, nebo změna SHORT na OPEN (ideální zkrat na ideální odraz)
	- No a to stačí nějak nakreslit do polárního diagramu:
![[polarni_diagram_koeficient_odrazu_gamma.png]]
##### Koeficient přenosu **T**
- Réalně se objevuje jen v jednom slidu přednášky: [[TBK 2 teoretické základy 25.pdf#page=20|Přednáška]]
- ????? Tipuju že to bude něco jako prošlá vlna ku celkové  $\frac{\widehat V_T}{\widehat V}$
$$\widehat T=\frac{2\widehat Z_1}{\widehat Z_1 + Z_0}$$
![[koeficient_prenosu.png]]
#### Proč je ve VF a mikrovlnné oblasti vhodnější vyjádření koeficientů odrazu **Γ** a koeficientů přenosu **_T_** než impedance **_Z_** nebo admitance **_Y_**?
- [[TBK 2 teoretické základy 25.pdf#page=21|Přednáška str. 21]]
- Protože pro Z a Y, bychom potřebovali měřit napětí a proud a to je při těchto frekvencích nemožné
- Vstupní kapacita 1 pF @ 1 GHz = > 159 ohmů
- VF měřiče proudu neexistují
- $\Gamma$ a **B** umíme měřit i na vysokých kmitočtech -> odědlíme dopadající nebo odraženou vlnu směrovou vazbou a změříme její výkon (dBm) -> známe zátěž=měřicí přístroj $Z_0 = 50\space\Omega$
#### Co je to Smithův diagram (SD), jaké jsou typy SD a jak jsou definovány? Jak a proč jsou SD často normované a jaké jsou výhody použití SD?
[[TBK 2 teoretické základy 25.pdf#page=22|Přednáška str. 22]]
- Co je Smithův diagram? 
	- Smithův diagram je reprezentace komplexního čísla v logaritmických osách
	- Nekonečno na iImaginární ose je ohlé do nekonečna na reálné ose
	- Zahrnuje jak nulu, tak nekonečno, což je jeho výhoda oproti klasické kartézské soustavě
	- Výhodou je že pokud chceme přepočítat $\Gamma <-> Z <-> Y$, tak stačí jen změnit pozadí grafu a dostaneme daný parametr.
	- Aby mohli být použity pro různé $Z_0$, tak se střed diagram k $Z_0$ normuje, tak že ve středu je diagram 1
- Druhy smithova diagramu:
	- Impedanční - Z
	- Admitanční - Y (zrcadlově převrácený Z)
	- Polární - $\Gamma$
- Výhody:
	- Graficky můžeme přecházet mezi veličinami bez nutnosti přepočtu
	- Graficky můžeme navrhovat přizpůsobovací obvody -> pohyb po kružnicích konst. poloměru

#### Do impedančního SD zakreslete: zkrat **_Z_**=0, otevřený konec **_Z_**=∞, **_Z_**=50Ω, kružnici **_R_**=20 Ω, impedanci **_Z_**=(100-j30)Ω
- Legenda:
	- Červený puntík je Z=0
	- Oranžový puntík je Z = 50 $\Omega$
	- Fialový puntík je Z = 100 - j30 $\Omega$
	- Zelený puntík je Z = $\infty$
![[smith_priprava3.png]]
#### Do admitančního SD zakreslete: zkrat **_Y_**=∞, otevřený konec **_Y_**=0, kružnici **_G_**=20ms
- Legenda:
	- Růžový puntík Y = $\infty$ 
	- Zelený puntík Y = 0
	- Červená kružnice G = 20 mS 
![[smith_admitance.png]]
#### Co jsou to s-parametry a jaký je jejich význam ve VF a mikrovlnné technice? Porovnejte se z- a y-parametry.
[[TBK3 - parametry#page=5|Přednáška str. 5]]
- S parametry:
	- Od slova scattering
	- Jsou definovány přes dopadené $a$ a odražené $b$ vlny
$$a_i=\frac{\widehat V^+}{\sqrt{2 Z_0}}$$
$$b_i=\frac{\widehat V^-}{\sqrt{2 Z_0}}$$
	- Vychází z matice pro daný n-bran (pro dvou portové zařízení matice 2x2)
	- index označuje číslo portu daného n-branu = co je to za port
	$$\begin{align*}
\begin{bmatrix}
b_1 \\
b_2
\end{bmatrix}
&=
\begin{bmatrix}
S_{11} & S_{12} \\
S_{21} & S_{22}
\end{bmatrix}
\begin{bmatrix}
a_1 \\
a_2
\end{bmatrix}
\end{align*}
$$
	- Druhá mocnina $a$ nebo $b$ má význam výkonu
- Porovnání:
	- S parametry se dají dobře měřit (= výkonové zesílení/útlum) - jsou definovaný pomocí $Z_0$
	- Z a Y můžeme z s parametrů přepočítat, měřit neumíme -> museli bychom měřit napětí a proud což ve vf nelze
#### Co to je parametr _RL_ a k čemu se používá? Jaký je jeho fyzikální význam?
- RL = return loss = $20\cdot log_{10}(s_{11})$
- Logaritmicky v dBm popisuje jak moc výkonu se odráží
- Má význam, jak moc daný vstup tlumí odrazy
	#### Jaký je vliv odrazů na přenesený výkon? Napište vztah.
$$P_{out}=P_{in}-P_{odrazy}$$

#### Co to je impedanční přizpůsobení? Proč je ve VF a mikrovlnné oblasti tento koncept nutný? Co nastává, pokud není dodržen?
- Impedanční přizpůsobení je minimalizace vzniku odrazů
- Pokud máme dobře přizpůsobený obvod, přenášíme maximální výkon, ztráty jsou minimální
- Pokud jsou např. generátor a anténa nepřizpůsobené, tak se od antény bude odrážet výkon zpět do generátoru
- Pokud bychom měli nepřizpůsobenou deep space anténu tak nám generátor s přijatého odraženého výkon shoří, tuším že anténny co řídí Voyagery mají vysílaný výkon až 400 kW = 200 rychlovarek, litr vody ohřeje z nuly na 100°C za 1 sekundu.
#### Co jsou to přizpůsobovací obvody a kde se používají?
- Přizpůsobovací obvod zajišťuje, aby impedance na jeho vstupu byla stejná jako ze zdroje a na výstupu stejná jako další zařízení do něj zapojené
- Používáme jako mezičlen pro dvě zařízení, které mají různé $Z_0$
#### Jaké komponenty se nejčastěji používají pro návrh a konstrukci přizpůsobovacích obvodů a proč?
- Cívky a kondenzátory, jelikož nezpůsobují žádné ztráty
- Pro mikrovlné frekvence stačí i kus vedení, viz [[TBK2 - teorie#Definice koeficientů odrazu a přenosu na vedení s impedancí **_Z**_0_. Jak se mění koeficient odrazu podél vedení (popište v polárním diagramu)?|Jak se mění charakteristická impedance s délkou vedení?]]

#### Výpočty:

- Pro moduly koeficientu odrazu uvedené v tabulce vypočtěte odpovídající poměry stojatých vln _PSV_,  útlumy odrazů _RL_ a hodnoty přenosu přes rozhraní _GT_.
$$PSV=SWR=\frac{V_{max}}{V_{min}}=\frac{1+|\hat\Gamma|}{1-|\hat\Gamma|}$$
$$RL=-20\cdot \text{log}|\hat\Gamma|$$
$$G^T=1-|\hat\Gamma|^2$$

| \|Γ\| | _PSV=SWR_ | _RL_ [dB] | _GT_ [dB] |
| ----- | --------- | --------- | --------- |
| 0,07  |           |           |           |
| 0,15  |           |           |           |
| 0,25  |           |           |           |
| 0,48  |           |           |           |
| 0,74  |           |           |           |
| 0,96  |           |           |           |
