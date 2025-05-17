- Je to v píčí dalších 45 otázek, lets gooooooooooooooooooooooooooo

#### Co vyjadřuje teorém reciprocity antény?
- Anténa je ekvivalentní jako přijímač nebo vysílač
#### Jak je definována vstupní impedance antény?
![[vatupni_impedance_anteny.png]]
- $Z_A=(R_{ztr}+R_{vyz})+jX_A$ je impedance antény
- $Z_G=R_G+jX_G$ je vnitřní impedance zdroje/generátoru
#### Co je to vyzařovací odpor antény?
- Fiktivní odpor, který modeluje jak efektivně anténa vyzařuje elektromagnetickou energii do prostoru
#### Jak lze pomocí náhradního obvodového schématu antény vyjádřit vyzářený výkon?
$$P_{vyz}=\frac{|U_g|^2}{2}\Big[\frac{R_{ztr}}{(R_{vyz}+R_{ztr}+R_g)^2+(X_A+X_g)^2}\Big]$$
- Pokud je obvod přizpůsobený: $R_{vyz}+R_{ztr}=R_g;X_A=-X_g$ tak:
$$P_{vyz}=\frac{|U_g|^2}{8}\Big[\frac{R_{vyz}}{(R_{vyz}+R_{ztr})^2}\Big]$$

#### Jak lze pomocí náhradního obvodového schématu antény vyjádřit výkon ztracený na anténě přeměnou na teplo?
$$P_{ztr}=\frac{|U_g|^2}{2}\Big[\frac{R_{ztr}}{(R_{vyz}+R_{ztr}+R_g)^2+(X_A+X_g)^2}\Big]$$
- Pokud je obvod přizpůsobený: $R_{vyz}+R_{ztr}=R_g;X_A=-X_g$ tak:
$$P_{vyz}=\frac{|U_g|^2}{8}\Big[\frac{R_{ztr}}{(R_{vyz}+R_{ztr})^2}\Big]$$

#### Definujte podmínky impedanční přizpůsobení antény.
$R_{vyz}+R_{ztr}=R_a=R_g;X_A+X_g=0$
#### Jakým způsobem lze vypočítat ztráty vlivem impedančního nepřizpůsobení antény k napáječi?
- Reflection $R$:
$$R=\frac{Z_A-Z_0}{Z_A+Z_0}$$
- Ztáty vlivem nepřízousibení $L_I$
$$L_I=-10\text{log}(1-|R|^2)$$

#### Jak je definována šířka frekvenčního pásma antény?
![[prizusob_antenu.png]]
- Pásmo, kde je činitel odrazu v dB, menší než -20 dB

#### Jaký je význam vzdálené zóny antény a jak ji lze určit?
- vzdálená zóna = far field = ff
- Je to vzdálenost, ve které se nám přilétající elmag. vlna zdá jako rovinná, i když ze zdroje letí vlna kulová
- Za touto vzdáleností umíme anténu popsat podle předešlých parametrů
- $D$ je největší rozměr antény (úhlopříčka (TBK 5. úloha), průměr (talíř anténa), ...)
$$d_{ff}=\frac{2D^2}{\lambda}$$


#### Jaké jsou vlastnosti/parametry izotropického zářiče?
- Září do všech směru stejně
- hustota vyzařovaného výkonu se rozkládá do kulové vlny -> klesá z druhou mocninou vzdálenosti
#### Definujte směrovou charakteristiku antény a popište odpovídající základní pojmy.
- Vyjadřuje kolik výkunu v jakém směru anténa vyzařuje, obecně funkce vzdálenosti, úhlu a azimutu (opět TBK 5. úloha)
- Většinou vykreslujeme jen řezy - polárně nebo kartézsky
 ![[vyzar_polarne.png]]
![[vyzarovak.png]]
- Vrchol vyzařováku normujeme k 0 dB
- HPBW - half power beam width - říká nám jak moc úzce anténa vyzařuje pro poloviční výkon
- FNBW - šířka hlavního svazku
- Zpětné svazky nám říkají jak anténa září dozádu
#### Nakreslete dva základní kolmé řezy směrovou charakteristikou půlvlnného dipólu.
![[dipol.png]]
#### Definujte směrovost antény a popište její význam.
$$D(\vartheta,\varphi)=\frac{U(\vartheta,\varphi)}{U_0}$$$$D_{max}=\frac{4\pi U_{max}}{P_{vyz}}$$
- Je to intenzita vyzařování v určitém směru, vtažená na intenzitu vyzařování izotropického zářiče 
#### Definujte zisk antény a popište jeho význam.
$$G=\eta D=\frac{4\pi U}{P_V}$$
$$G=10\text{log}G$$
- $P_V$ je výkon co posíláme do antény
- Zisk antény je poměr výkonu na vstupu bezeztrátové antény ku výkonu na vstupu dané reálné antény za podmínky, že intenzita vyzařování obou antén je v daném směru a vzdálenosti shodná.

#### Jaký je zisk izotropického zářiče a půlvlnného dipólu?
- Zisk izotropického zářiče je G = 1 \[-] = 0 dBi
- Zisk půlvnlného dipólu je G = 1,5 = 1,75 dBi
- dBi je vtažená log hodnota k izotropickému zářiči, který má G = 1 \[-]
#### Definujte efektivní aperturu antény.
= efektivní plocha antény
$$P_p=w_{dop}A_{ef}$$
- $P_p$ je výkon na impedančně přizpůsobeném výstupu z antény dodávaný na zátěž
- $w_{dop}$ je plošná hustota výkonu co dopadá na anténu

#### Jaký je vztah mezi ziskem a efektivní aperturou antény?
$$A_{ef}=\Big(\frac{\lambda^2}{4\pi}\Big)G$$
#### Popište základní typy polarizace antén.
![[polarizace.png]]
#### Co je to charakteristická funkce anténní řady?
- Popisuje jak se změní vyzařovací diagram, když složíme více antén do řady/pole
- Závisí na vzdálenosti antén a fázovému posunu vln, které vyzařují
#### Jakým způsobem lze ovlivňovat směrovou charakteristiku anténní řady?
- Můžeme měnit vzdálenost antén a fázový posun vln které vyzařují
#### Jaké jsou ztráty při šíření vln z izotropického zářiče ve volném prostoru (vakuu) a jaká je jejich fyzikální příčina?
- Nejde o klasické ztráty, že by se přeměnila energie vlny na teplo, ale s tím jak se kulová vlna rozpíná do prostoru tak se její energie ředí
- Prostě klasické inverse square law
- Free space loss = $FSL=20\text{log}(\frac{4\pi d}{\lambda})$
#### Jaká jsou omezení platnosti ideální přenosové rovnice (Friisova vztahu)?
- Antény musí být od sebe vzdálené minimálně $d_{\text{far field}}$ - vzdálenost far fieldu
- Mezi anténami nesmí být žádné překážky
- Nesmí nastávat odrazy od okolního prostředí, resp. musí být ve volném prostředí
#### Popište základní výkonovou bilanci rádiového spoje.
- Tu popisuje friisův vztah
$$P_R=P_{p0}=P_T+G_{Tx}+G_{Rx}-FSL-L$$
$$L=L_{Vost}+L_{Post}$$
![[vykon_bilance.png]]

#### Vysvětlete pojem „rezerva na únik“ ve výkonové bilanci rádiového spoje.
- Je to rozdíl mezi přijatým výkonem a signal to noise ratio
- Tato rezerva je zaručena tím kdo postaví radiovou trasu, počítá s tím že výstupní signál na vzdory vněším vlivů neklesne pod SNR
#### Popište základní mechanizmy šíření vln v zemské atmosféře pro pozemní rádiové spoje.
![[vlny_sireni.png]]
- Přízemní povrchová vlna 
	- šíří se podél rozhraní země-vzduch
	- Funguje do jednotek MHz
	- Radionavigace, místní spoje, rozhlas
- Přízemní prostorová vlna
	- desítky MHz
	- šíří se přímo nebo odrazy (od krajiny atd.)
- Vlnovodným kanálem
	- Využívá se refrakčních/ohybových vlastností jevů v troposféře
	- Tento jev se vyskytuje na frekvencích nad cca 500 MHz
- Troposférická vlna
	- odraz, rozptyl na nehomogenitách v troposféře
	- k zemi se zpět odráží jen malá část energie
	- frekvence stovky MHz až  jednotky GHz
- Ionosférická vlna
	- Významná pro dálkové spoje (USA - Evropa)
	- Frekvence cca do 30 MHz (vln. délka je kolem 10 m)
	- Komplikovaný návrh, ionosféra dělá přes rok brikule
