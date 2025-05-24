#### Napište jaké jsou možnosti určení časové odezvy lineárního systému na obecný vstupní signál a uveďte postup výpočtu. Jaké znáte standardizované odezvy a k čemu je lze použít

- Časová odezva $h(t)$ nám říká, jaký signál se objeví na výstupu $y(t)$ s ohledem na daný vstup $u(t)$
- Lze určit:
	- Vyřešením diferinciálních rovnic, které popisují soustavu
	- Zpětnou Laplacovou transformací přenosové funkce $H(s)$
	- Zpětnou Fourierovou transformací kmitočtové charakteristiky $H(j\omega)$
	- Nebo derivací přechodové charakteristiky 
- Využití:
	- Vyřešení diferenciálních rovnic systému, nejdříve je ztransforumjeme, vyřešíme jako algebraickou rovnici, poté zpětně transformuje
	- Dokážeme zjistit odezvu systému na jakýkoliv signál pomocí konvoluce vstupního signálu $u(t)$ a impulsní=časové odezvy $h(t)$, případně součinemem přenosové charakteristiky $H(s)$ a obrazu vstupního signálu $U(S)$
	- Můžeme pomocí integrace zjistit přechodovou charakteristiku (odezva na jednotkový skok aka na Heavisidův impuls) $w(t)=\int_{0}^{t}h(\tau)d\tau$
	- Z obrazu časové odezvy $\mathcal{L}(h(t))=H(s)$ dosazením za $s=j\omega$, dostaneme frekvenční charakteristiku $H(j\omega)$
#### Definujte přenosovou funkci lineárního systému a napište jaké vlastnosti musí takový systém splňovat. Uveďte co lze pomocí přenosové funkce charakterizovat a k čemu to lze využít. Co navíc musí splňovat přenosová funkce stabilního systému a proč?

$$H(s)=\frac{Y(s)}{U(s)}$$
- Přenosová funkce je podíl OBRAZU výstupního signálu $Y(s)$ a OBRAZU vstupního signálu $U(s)$
- Lineárně časově invarientní systém (LTI) je systém, který splňuje:
	- Linearitu
		- Pokud se vstupní signál zvětší tak se lineárně zvětší i výstupní signál
		- $y(t)=S\{u(t)\}=>ay(t)=S\{au(t)\}=aS\{u(t)\}$
	- Princip superpozice
		- $y(t)=S\{au_1(t)+bu_2(t)\}=aS\{u_1(t)\}+bS\{u_2(t)\}$
	- Časovou invariantnost:
		- vlastnosti systému se časem nemění
		- $y(t-t_0)=S\{u(t-t_0)\}$
- Z přenosové funkce lze určit:
	- Odezva na diracův impuls = impulsní odezva $h(t)=\mathcal{L}^{-1}H\{s\}$
	- Frekvenční charakteristika $H(s=j\omega)$
	- Stabilita systému (póly a nuly)
	- Odezva na jednotkový impuls
		- $\mathcal{L}^{-1}\{W(s)\}=\mathcal{L}^{-1}\{sH(s)\}=w(t)$
		- $\frac{d}{dt}\mathcal{L}^{-1}\{H(s)\}=\frac{dh(t)}{dt}=w(t)$
- Přenosová funkce stabilního systému:
	- Má ve tvaru racionáln lomené funkce, kořeny čitatele a jmenovatele (nuly a póly) v levé polorovině imaginární plochy, buďto reálné záporné, nebo komplexně sdružené z s reálnou složkou záporné
	- Pro tyto kořeny vychází časová odezva v nekonečném čase konečná
	- Pro komplexní kořeny je kmitavá, ale stále konečná

Napište přenosovou funkci kmitočtového filtru 2. řádu typu dolní/horní/pásmová propust, případně pásmová zádrž. Definujte jednotlivé parametry a vysvětlete, co určují - ilustrujte graficky v kmitočtové i časové oblasti

- Dolní propust
	$$H_{LP2}(s)=\frac{H_0\omega_0^2}{s^2+\frac{\omega_0}{Q}s+\omega_0^2}$$
	-  $H_0$ je stejnosměrný zisk
	- $\omega_0$ je zlomový kmitočet
	- $Q$ je činitel jakosti
		- Pro $Q<\frac{1}{2}$ máme dva reálné póly
		- Pro $Q=\frac{1}{2}$ máme jeden dvojnásobný pól
		- $Q>\frac{1}{2}$ máme komplexně sdružený pól
		- $Q=\frac{1}{\sqrt2}$ máme speciálné případ komplexně sdruženého pólu, který má reálnou a imaginární složku stejně velkou
		- $H( \infty) =0$
	![[lowpass.png]]
- Horní propust
	![[highpass.png]]
- Pásmová propust
	![[bandpass.png]]
- Pásmová zádrž
	![[notch.png]]

#### Nakreslete toleranční schéma filtru typu DP/HP/PP/PZ, popište význam charakteristických hodnot. Do schématu pak zakreslete typické modulové charakteristiky pro Besselovu/Butterworthovu/Čebyševovu/inverzní Čebyševovu/Cauerovu aproximaci stejného řádu. Porovnejte jejich vlastnosti v kmitočtové i časové oblasti

##### Dolní propust
- Vlevo nenormalizovaná, vpravo normalizovaná (normujeme k hraničnímu kmitočtu $\omega_p$)
![[LP&NLP.png]]
- $a_p$ \[dB\] je útlum na zlomovém kmitočtu $\omega_p$
- $a_s$ \[dB\] je útlum na kmitočtu, který chceme potlačit $\omega_s$

##### Horní propust
- Vlevo nenormalizovaná, vpravo normalizovaná (normujeme k hraničnímu kmitočtu $\omega_p$)
![[HP&NHP.png]]
- $a_p$ \[dB\] je útlum na zlomovém kmitočtu $\omega_p$
- $a_s$ \[dB\] je útlum na kmitočtu, který chceme potlačit $\omega_s$
##### Pásmová propust
![[BP.png]]
- $a_p$ \[dB\] je útlum na zlomových kmitočtech
- $a_s$ \[dB\] je útlum na kmitočtu, který chceme potlačit 
- $\omega_{-p},\omega_{p}$ jsou zlomové kmitočty, kde je pokles přenosu $-a_p$
- $\omega_m=\sqrt{\omega_{-p}\omega_{p}}$ je geometrický střed propustného pásma
- $\Delta\omega_p$ je šířka propustného pásma
##### Pásmová zádrž
![[Pásmová zádrž.png]]
- $a_p$ \[dB\] je útlum na zlomových kmitočtech
- $a_s$ \[dB\] je útlum na kmitočtu, který chceme potlačit 
- $\omega_{-s},\omega_{s}$ jsou zlomové kmitočty, kde je pokles přenosu 
	- $-a_s$ je útlum zadrženého pásma 
- $\omega_m=\sqrt{\omega_{-s}\omega_{s}}$ je geometrický střed zadrženého pásma
- $\Delta\omega_s$ je šířka zadrženého pásma
![[filtry2.png]]
![[filtry_včase.png]]
- Ve frekvenční oblasti:
	- Cauer má největší útlum v přechodovém pásmu, ale pro nepropustné pásmo útlum neklesá
	- Inverzní čebyšev je podobný jako Cauer, ale v propustném pásmu není izoextremální (nepohupuje se), v přechodném pásmu má menší spád než Cauer a pro nepropustné pásmo dělá stejné věci jako Cauer
	- Čebyšev je v propustném pásmu izoextremnální, ale poté s rostoucí frekvencí útlum stále klesá
	- Butterworth je pěkný, ale neklesá zas tak rychle (6. řád 120 dB/dek)
	- Bessel vypadaá jako posunutý butterworth, klesá pomaleji
- V časové oblasti - odezva na jednotkový skok
	- Cauer a čebyšev mají velmi pomalou odezvu a vzhledem k sudému řádu filtru je v ustáleném stavu jen $1/\sqrt2$
	- Butterworth a inverzní čebyšev mají podobnou odezvu, překmitávají
	- Bessel má nejlepší odezvu, velmi rychle se ustálí

#### Nakreslete principiální zapojení zpětnovazební (ZV) struktury a odvoďte vztah pro výstupní signál. Uveďte základní dělení ZV obvodových struktur a vliv záporné ZV na vstupní a výstupní odpor zesilovače.
![[zv.png]]
$$u_1=u_i+u_{\beta},u_{\beta}=u_o\beta$$
$$u_o=u_1A=(u_i+\beta u_o)A=\frac{u_iA}{1-\beta A}$$
$$A'=\frac{u_o}{u_i}=\frac{A}{1-\beta A}=\frac{A}{F}$$
- Druhy podle velikosti vratného rozdílu
	- Záporná zpětná vazba $\beta A<0$
	- Bez vazby $\beta A=0$
	- Stabilní kladná zpětná vazba $0 < \beta A < 1$
	- Kladná zpětná vazba (oscilátor) $\beta A=1$
	- Nestabilní kladná zpětná vazba $\beta A>1$
- Druhy podle obvodového zapojení
	- sériová:
		- napěťová
		- vstupní odpor: $R_{in}=R_i(1+\beta A)$
		- výstupní odpor: $R_{out}=\frac{R_o}{1+\beta A}$
		![[seriova_napetova_zv.png]]
		- proudová
		![[seriova_proudova.png]]
	- paralelní:
		- napěťová
		- vstupní odpor: $R_{in}=\frac{R_i}{1-\beta A}$
		- výstupní odpor: $R_{out}=R_o(1-\beta A)$
		![[paralelni_napetova_zv7.png]]
		- proudová
		![[paralelni_proudova_zv.png]]

#### Jak se zjišťuje stabilita ZV soustav a co musí platit pro stabilní systém? Vysvětlete pojem fázová jistota a doplňkový zisk. Co je to kmitočtová kompenzace zesilovače a proč se používá.

- Vyšetřuje se pomocí Nyquistova kritéria, odpojíme vstupy zesilovacího členu, zpětnou vazbu zatížíme tak aby platilo:
$$\beta A=\frac{U_o(s)}{U_1(s)}\cdot\frac{U_{\beta}(s)}{U_o(s)}=\frac{U_{\beta}}{U_1(s)}$$
- $R_Z$ určíme tak aby byla zpětná vazba zatížena stejně jako při nerozpojeném ZV systému
![[nyquist.png]]
- Kmitočtová charakteristika v ReIm rovinně nesmí obkroužit jedničku na reálné ose jinak je soustava nestabilní
![[real_imaginery.png]]




