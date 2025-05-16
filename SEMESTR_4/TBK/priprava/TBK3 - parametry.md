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
#### Jaký je význam s-parametrů v dB?
- Vyjadřuje poměr výkonů 
- dB lépé zahrnují velký počet řádů
#### Vyjádření VF výkonu v dBm. Jaké jsou výhody tohoto vyjádření?
- Vyjadřuje výkon oproti referenční hodnotě 1 mW
- Opět jsme pomocí dvouciferného čísla schopni zahrnout výkon od pW až po kW
#### Jaká je definice vložného přenosu a útlumu lineárně a v dB?
- [wiki-insertion loss](https://en.wikipedia.org/wiki/Insertion_loss)
- [wiki-insertion gain](https://en.wikipedia.org/wiki/Insertion_gain)
- [[TBK 4 komponenty 25.pdf#page=5|prednáška]]
- Vložný útlum = insertion loss
- Význam: výkonové zesílení, které má komponenta když ji vložíme do obvodu 
$$IL=-|s_{21}|^2$$
$$IL(dB)=-20\cdot \text{log}_{10}(|s_{21}|)$$
- Vložný přenos = insertion gain (*nenašel jsem v přednášce*)
- Význam: výkonový zisk, který získáme když do obvodu přidáme tento prvek
$$IG=|s_{21}|^2$$
$$IG(dB)=20\cdot \text{log}_{10}(|s_{21}|)$$
#### Proč je šum jedním z parametrů omezujících radiové komunikace?
- Šumový práh nám určuje jak nízký signál jsem ještě schopni rozlišit 

#### Co to je fázový šum a jaký vliv má na přijímané signály?
- šum v bezprostřední blízkosti nosné způsobený náhodnými změnami fáze

#### Definice šumového čísla pomocí _SNR_. Jaká je definiční podmínka?
##### SNR = signal to noise ratio definice
- $\text{S}$ = signal výkon
- $\text{N}$ = noise výkon
$$\text{SNR}=\frac{\text{S}}{\text{N}}$$
$$\text{SNR(dB)}=\text{S}_{dBm}-\text{N}_{dBm}$$
- Vzorečky nahoře platí pro spektrální čáru - jednu nosnou bez modulaci
- Pokud máme modulovaný signál, tak musíme zahrnout celý band - pásmo s šíčkou pásma $\text{B}$
- PSD = Power signal density
$$\text{S}=\int_{f_{nosná}-B/2}^{f_{nosná}+B/2}PSD_{sig}df$$
##### Šumové číslo F pomocí SNR
$$F=\frac{\frac{S_1}{N_1}}{\frac{S_2}{N_2}}$$
- $S_1$ = úroveň signálu na vstupu
- $N_1$ = šum na vstupu 
- $S_2$ = úroveň signálu na vstupu
- $N_2$ = šum na vstupu
##### **Podmínka**:
- Platí pouze pro $N_1=kT_0B$ - šumové vyzařování absolutně černého tělesa
- $T_0=290 K \approxeq 20 °C$
- B = Bandwith
- k = Štefan - Boltzmanova konstanta
![[snr_šum.png]]
##### Použití SNR definice šumového čísla F
- Systémové výpočty
- Rozhodující pro **B**it **E**rror **R**ate=BER
- Každá modulace potřebuje nějaký minimální SNR a BER, aby správně fungovala
#### Výkonová definice šumového čísla. Co to je „noise added“ a jak se počítá?
- signály $S_1$ a $S_2$ nahrazeny ziskem $G=S_2 / S_1$
- Vyjadřuje celkový šumový výkon $N_2$ dělený zesíleným šumoem bezodrazové koncovky
$$F=\frac{N_2}{GN_1}=\frac{GN_1+N_a}{GN_1}=1+\frac{N_a}{GkT_0B}$$
$$F(dB)=10\cdot\text{log}(F)$$
- $N_\alpha$ = Noise added - výkon, který přidává šumový dvoubran
![[vykon_sum_f.png]]

#### Jak lze realizovat šumový výkon _N0=kT0B_?
- Buďto bezodrazovou koncovkou (BK) - má teplotu $T_0$
	- přesná impedance $Z_0=50\space\Omega$
	- Velmi vysoké RL = return loss
	- Frekvence = 10ky - 100ky GHz
- nebo anténou namířenou na černou plochu o teplotě $T_0$
#### Jak je definována ekvivalentní šumová teplota _Te_? Odvoďte přepočetní vztah na _F_.
- Výhodné pro řešení šumu antén
- z šumového dvojbranu jakoby vyjmeme všechno co šumí a nahradíme to jednou šumovou součástkou na vstupu a budeme se tvářit že je dvojbran bezšumový
- tento vyjmutý šum spočtem jako $N_a=kT_eBG$
- Pokud chceme vyjádřit $T_e$ potřebujeme celkové $F$ a z něj vyjádříme $N_a$
$$F=1+\frac{N_A}{kT_0BG}$$
$$N_A=(F-1)kT_0BG$$
- Dosadíme za $N_a=kT_eBG$
$$kT_eBG=(F-1)kT_0BG$$
$$T_e=(F-1)T_0$$
#### Jaké je šumové číslo dobře přizpůsobených pasivních ztrátových komponent a proč?
- Atenuátory, filtry, kabely, VF přepínače
- Z definice: šum na výstupu s připojenou bezodrazovou koncovkou na vstupu
$$N_2=kT_0B$$
- Pasivní ztrátové komponenty mají vždy nějaký útlum $L=1/G$
- Šumové číslo F poté bude:
$$F=\frac{N_2}{GN_1}=\frac{kT_0B}{kT_0B/L}=L$$
- Šumové číslo F se rovná útlumu pasivního ztátového dvoubranu
![[šum_passive_component.png]]
#### Odvoďte vztah pro šumové číslo kaskády dvou 2-branů.
![[šum_kaskáda.png]]
- Na jedné straně bezodrazová koncovka co šumí $N_1=kT_0B$
- Poté první dvojbran má vložený šum $N_{a1}=(F_1-1)kT_0BG_1$
- Druhý dvojbran má vložený šum $N_{a2}=(F_2-1)kT_0BG_2$
- Celkový šum bude $N_2 = k T_0 BG_1 G_2+G_2N_{a1}+N_{a2}$
$$N_2=kT_0BG_1G_2+G_1(F_1-1)kT_0BG_2+(F_2-1)kT_0BG_2$$
$$N_2=kT_0B[G_1G_2+G_1G_2(F-1)+G_2(F_2-1)]$$
$$\frac{N_2}{GkT_0B}=G_1G_2+G_1G_2(F-1)+G_2(F_2-1)$$
$$F_C=\frac{N_2}{GkT_0BG_1G_2}=\frac{G_1G_2+G_1G_2(F-1)+G_2(F_2-1)}{G_1G_2}$$
$$F_C=F+\frac{F_2-1}{G_1}$$
- výsledný vztah se nazývá Frisův vztah
#### Co to je šumová teplota antény? Jak se uplatňuje při výpočtech radiových tras?
- Šumová teplota je obecně teplota při které by ideální rezistor šuměl daným výkonem $kT_0B$
- Šumová teplota antény je v podstatě teplota pozadí, které anténna vidí, na zemi se bere tato teplota jako 300 K
- Ale pro satelitní komunikaci to prakticky může být 0K, ve vesmíru nic moc není -> není tam zdroj šumění -> mezi satelitama se dobře komunikuje asi, nemusíme mít tak vysoký vysílaný výkon, abychom u dalšího satelitu oproti šumovému prahu poznali
#### Jaké typické nelineární obvody znáte?
- Směšovač
- Zesilovač
- Limitery - omezovač 🫨
#### Jaká se používá typická aproximace nelineárních charakteristik 2-branu?
- Pomocí polynomu
- $a+bx+cx^2+...$

#### Jaké jsou typické nelineární produkty při 1 vstupním sinovém signálu? Jaké VF obvody tyto produkty využívají?
- Harmonické složky -> 2. a 3. harmonické
- Násobič frekvence 2x, 3x
- VF detektory - detekují stejnosměrnou složku
- Zesilovače
#### Jak vzniká komprese u nelineárních VF obvodů (např. zesilovačů) a jakým parametrem se obvykle popisuje?
- Je to nelineární produkt 3. řádu, který vzniká omezeným napájecím napětím - aktivní součástka se saturuje
- popisujeme ho parametrem $P_{-1dB}$ = výstupní výkon, kdy se liší realný výkon od ideálního lineárního o -1 dB
![[komprese_p1db.png]]
#### Jaké jsou typické nelineární produkty při 2 vstupních sinových signálech? Jaké VF obvody tyto produkty využívají?
- Vznikají 2. a 3. harmonické vstupního signálu
- Také vznikají intermodulační produkty, které mají frekvenci součtu a rozdílu vstupních kmitočtů
	- IM produkty 2. řádu
	- IM produkty 3. řádu
- Tyto produkty využívají směšovače pro up-konverzi nebo down konverzi
![[intermodulacni_produkty.png]]
#### Co jsou to IM produkty 2.  a 3. řádu?
- 2. řád
	- Jsou to složky, které vznikají z ze součtu a rozdílu frekvencí základních signálů
- 3. řád
	- vznikají z rozdílu druhé harmonické a frekvence druhého signálu
	- 2a-b & 2b-a -> viz obrázek nad
#### Co je to IP2 a IP3 jak se tyto parametry využívají v praxi?

![[IP3.png]]
- IP2 = Second order intercept point
	- Bod kde by se protkla tečna charakteristiky výkonu výstupní složky a výstupní IM2 složky
	- používá se pro zjištění výkonu IM2 při daném výstupním výkonu
	- Je to paramter nelineárního prvku (směšovač) => našli bychom ho v datasheetu
	- $P_{IM2}=2\cdot P_{out}-IP2=IP2-P_{out}$
	- $O_{IM2}=P_{out}-P_{IM_2}=IP2-P_{out}$ = offset/odstup výkonové charakteritiky základní složky a složky IM2
- IP3 = Third order intercept point
	- Bod kde by se protkla tečna charakteristiky výkonu výstupní složky a výstupní IM3 složky
	- používá se pro zjištění výkonu IM3 při daném výstupním výkonu
	- Je to paramter nelineárního prvku (směšovač) => našli bychom ho v datasheetu
	- $P_{IM3}=3\cdot P_{out}-2\cdot IP3$
	- $O_{IM3}=P_{out}-P_{IM_3}=2IP3-2P_{out}$ = offset/odstup výkonové charakteritiky základní složky a složky IM2

#### Jaký je vliv produktů IM3 na radiové komunikace?
- Mají frekvence blízké budících frekvenci a tím rušit sousední kanály nebo budící kanál
#### Proč je v případě standardních radiových komunikací vliv IM2 obvykle zanedbatelný?
- Složka má dostatečný odstup od budící frekvence a můžeme jí odfiltrovat

#### Jak lze jednoduše snížit výkon produktů IM2 a IM3 a proč?
- Snížením výstupního výkonu nelineárního prvku, jelikož se dostáváme do lineárnější části charakteristiky, kde je výkonový odstup složek mnohem vyšší

Příklady:

1.               Výkony ve W převeďte do dBm


| _P_ [W]   | 7.10-15 | 4.10-6 | 0,00084 | 0,6 | 32  | 155 |
| --------- | ------- | ------ | ------- | --- | --- | --- |
| _P_ [dBm] |         |        |         |     |     |     |

2.               Výkony v dBm převeďte do W


| _P_ [dBm] | -164 | -25 | -6  | 9   | 24  | 38  |
| --------- | ---- | --- | --- | --- | --- | --- |
| _P_ [W]   |      |     |     |     |     |     |

3.               Výkon signálu na vstupu radiového přijímače se 2 směšováním je 5.10-12 W. Vypočtěte výkon _Pindem_ ve W i dBm na vstupu demodulátoru.

![](data:image/wmf;base64,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)

            (správné hodnoty jsou: 3,16.10-8W,  -45 dBm)         

4.   Vztah pro výpočet šumového čísla kaskády přijímače je:
![[priklad_retezec.gif]]
$$F_c=F_1+\frac{F_2-1}{G_1}+\frac{F_3-1}{G1G2}$$

Všechny proměnné se dosazují v lineárním vyjádření. Vypočtěte celkové šumové číslo _Fc_  a zisk _Gc_ v \[-] i \[dB]. Hodnoty proměnných jsou následující:
$G_1=-3,5 \space dB\space F_1=3,5 dB$
$G_2=-13 \space dB\space F_2=1,9 dB$
$G_3=15,5 \space dB\space F_3=5,5 dB$
Správné hodnoty jsou: $G_C=+25 dB; F_C=5,74 dB;F_C=3,753$ 

5. Na vstupu kaskády RX dle příkladu ad.4. je připojena anténa s šumovou teplotou _TA_=150K, šumová šířka pásma zařízení je _B_=10MHz. Vypočtěte celkovou ekvivalentní systémovou šumovou teplotu _Ts_ se započtením vlivu antény, celkový šumový výkon na vstupu _Pnin_ , celkový šumový výkon na výstupu _Pnout_ .

Šumová teplota RX je: $T_{RX}=(F_C-1)T_0$ (správná hodnota je 798K)

Celková systémová teplota$T_S=T_A+T_RX$ (správná hodnoty je 948K)

Celkový ekv. vstupní šumový výkon: $P_{nin}=kT_SB$ (správná hodnota je 1,31.10-13W resp. -98,8dBm)

Celkový výstupní šumový výkon: $P_{nout}=kT_0BG_C$ (správná hodnota je 4,17.10-11W resp. -73,8dBm)

6. VF zesilovač má při _P-1dB_=20dBm IM parametry  _IP2_=44dBm,  _IP3_=33dBm.  Vypočtěte výkony a odstupy IM produktů pro výstupní výkony _Pout_=20dBm a 0dBm.

Výkon IM produktu 2. řádu pro nastavený výkon: $P_{IM2}=2\cdot P_{out}-IP2=IP2-P_{out}$

Odstup IM produktu 2. řádu pro nastavený výkon je: $O_{IM2}=P_{out}-P_{IM_2}=IP2-P_{out}$

Výkon IM produktu 3. řádu pro nastavený výkon:  $P_{IM3}=3\cdot P_{out}-2\cdot IP3$
Odstup IM produktu 3. řádu pro nastavený výkon je: $O_{IM3}=P_{out}-P_{IM_3}=2IP3-2P_{out}$

| _Pout_ [dBm]→ | 0   | 20  |
| ------------- | --- | --- |
| _PIM2_ [dBm]  |     |     |
| _OIM2_ [dB]   |     |     |
| _PIM3_ [dBm]  |     |     |
| _OIM3_ [dB]   |     |     |
