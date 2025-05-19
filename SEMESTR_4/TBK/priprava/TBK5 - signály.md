#### Jaké jsou výhody přenosu informací v digitální formě oproti analogové formě?
- Výhody digitální:
	- Pro velkou škálu SNR je zachovaná perfektní kvalita přenášeného signálu
	- Komprese, šifrování, klíčování - nemožné u analogu
	- díky tomu že můžeme mít menší SNR -> menší vysílané výkony
- Výhody analogové:
	- Při malých SNR lze furt signál přijmout je zašuměný, ale do určité míry slyšitelný -> lidský hlas, letadla - kvalita digitálního signálu při určitém SNR skokově klesá k nule

#### Co to je koncepce modulované nosné a proč se v radiových bezdrátových komunikacích používá?
- Stavba antén na nízkých kmitočtech je nesmyslná (anténu co má km nikdo nechce)
- tím pádem musíme namudolovat vysokofrekvenční signál tak abychom mohli mít malou anténu GHz -> cm

#### Jaké znáte nejčastěji používané digitální modulace? Pomocí jakých parametrů se informace přenášejí?
![[modulace.png]]
- Buďto modulujeme:
	- Amplitudu
	- Frekvenci
	- Fázi

#### Co jsou to IQ modulace, jaký je jejich matematický popis.
![[iq_modulace_princip.png]]
- In phase quadrature modulation = ve fází kvadraturní modulace
- Příklad 4 - QAM
- Wifi 6 používá 1024 - QAM
- Vynásobíme spolu dva ortogonální signály (nejčastěji sin a cos)
- Změnou amplitudy jednotlivých signálů definujeme různé symboly v IQ grafu
	- třeba 1* sin a -2* cos
#### Nakreslete blokové schéma a popište funkci analogového IQ modulátoru.
![[iq-modulator.png]]
- Digitální signály I a Q převedeme do analogové podoby, vyfitrujeme
- Zároveň vyrábíme nosný sin a cos
- Za stálého míchání I a Q signály smísíme příslušně se sin a cos
- Výsledné signály složíme do jednoho a vysíláme
#### Nakreslete blokové schéma a popište funkci analogového IQ demodulátoru.
![[iq-demodulátor.png]]
- Na vstupu rozdělíme signál do dvou směšovačů 
- Směšovače pracují jako násobičky, když násobíme vstupní signál cosinem tak to zabije sin část vstupního signálu a vyplyvne 2x frekvenci cos, pro druhý to funguje totožně
$$
\begin{aligned}
v_I^{\text{IF}}(t) &= \left[ v_I(t) \cos(\omega_0 t) + v_Q(t) \sin(\omega_0 t) \right] \cos(\omega_0 t) \\
&= v_I(t) \cos^2(\omega_0 t) + v_Q(t) \sin(\omega_0 t) \cos(\omega_0 t) \\
&= \frac{1}{2} v_I(t) \left( 1 + \cos(2\omega_0 t) \right) + \frac{1}{2} v_Q(t) \left( \sin(0) + \cos(2\omega_0 t) \right) \\
&= \text{filtrace} = \frac{1}{2} v_I(t)
\end{aligned}
$$
- Pak už jen přefiltrujeme a ADCčkujeme
#### Co je to OFDM a jaké jsou výhody a nevýhody této modulace?
##### OFDM = Orthogonal Frequency Division Multiplexing
- Modulační technika využívající mnoho ortogonálních podnosičů.
- Používá se v systémech jako Wi-Fi, LTE, 5G, DVB-T, DAB.
	- Každý podnosič přenáší část dat paralelně.
###### Výhody
- Odolnost vůči únikům = změny amplitudy přijatých VF signálů vznikajících jako důsledek odrazů EM vln při šíření a atmosférickými vlivy - podrobnost dále v kurzu.
- Vysoká spektrální účinnost (nosné se překrývají).
- Podpora vysokorychlostního přenosu dat.
###### Nevýhody
- Vysoký PAPR (Peak-to-Average Power Ratio) – náročné na zesilovače.
- Citlivost na chyby frekvenční a fázové synchronizace.
- Horší odolnost vůči Dopplerovu jevu (např. při pohybu).
#### Co to je _BER_ a jaká je obecně závislost _BER_ na _Eb/N0_? Načrtněte (od ruky) závislosti pro QPSK a 16-QAM.
![[QPSK&16-QAM-bit-error-rate.png]]
- BER = bit error rate
	- vyjadřuje počet chybně přenesených bitů k celkovému počtu bitů
	- Maximální hodnota určuje kvalitu služby
- $E_b/N_0$ vyjadřuje energii na bit/symbol
	- $\frac{E_b}{N_0}=T_bB\cdot SNR$