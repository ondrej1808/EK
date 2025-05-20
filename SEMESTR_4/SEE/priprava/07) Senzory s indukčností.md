#### Senzory s indukčností: Napište základní rovnici pro výpočet indukčnosti L a k ní napište diferenciální rovnici pro určení změny indukčnosti. Nakreslete náhradní elektrické zapojení senzoru s L s připojením k vyhodnocovacímu obvodu. Z náhradního elektrického obvodu odvoďte nerovnici pro určení rozmezí pracovních frekvencí.
![[nahradni_model_indukcnos.png]]
- základní rovnice pro indukčnost
$$L=f(S,l,N,\micro)$$
- změna indukčnosti
$$dL=\frac{\partial L}{\partial S}dS+\frac{\partial L}{\partial l}dl+\frac{\partial L}{\partial N}dN+\frac{\partial L}{\partial\micro}d\micro$$
- pracovní kmitočet - odvození intervalu
$$R_d,R_s,\omega L_s<<\omega L<<\frac{1}{\omega C},\frac{1}{omegaC_k},R_k$$
#### Indukčnostní (induktanční) senzor (pasivní): Nakreslete princip činnosti, napište, na kterých parametrech je indukčnost L závislá.
![[pasivni_indukcnost.png]]
- Indukčnost závisí na průřezu jádra (S), délce cívky (L), počtu závitů (N) a permeabilitě (μ). Změnou indukčnosti dochází ke změně impedance cívky, což lze využít pro detekci fyzikálních veličin.
#### Indukčnostní (induktanční) senzor (pasivní) s malou vzduchovou mezerou: Nakreslete princip činnosti a převodní charakteristiku pro změnu indukčnosti se změnou vzduchové mezery
![[airgap_induction_vole.png]]
#### Indukčnostní (induktanční) senzor (pasivní) s posunutím jádra: Nakreslete princip činnosti a převodní charakteristiku L jako funkci posunutí třmene
![[induktrmen.png]]
#### Indukčnostní (induktanční) senzor (pasivní) s potlačeným magnetickým polem : Nakreslete a vysvětlete princip činnosti
![[pasivni_s_potlacenim_inudodm.png]]
- Střídavé magnetické pole indukuje ve vodivém tělese vířivé proudy, které vytvářejí vlastní magnetické pole s opačnou fází.
- To oslabuje budicí pole, a tím dochází ke změně výsledného pole a tedy i ke změně impedance cívky.
#### Indukčnostní (induktanční) senzor (pasivní), vzájemná indukčnost: Nakreslete a vysvětlete princip činnosti senzoru
![[indukcni_vzajemny.png]]
- Oscilátor kmitá díky vzájemné indukčnosti cívek L1 a L2. Při zasunutí feromagnetického jádra se změní indukční vazba, což způsobí zánik oscilací a změnu amplitudy výstupu
#### Indukčnostní (induktanční) senzor (pasivní): Nakreslete můstková zapojení pro vyhodnocování senzorových signálů (výstupem je střídavý signál, stejnosměrný signál, zapojení se synchronním detektorem).
![[oscilacni_indukcni.png]]
- Změna indukčnosti L ovlivňuje výstupní napětí, které lze různými způsoby zesílit nebo usměrnit a použít pro vyhodnocení změny magnetického pole nebo vzdálenosti.
#### Indukční (magnetoinduktivní) senzor elektromagnetický (aktivní): Nakreslete a vysvětlete princip činnosti senzoru, napište rovnici indukčního zákona pro cívku s N závity, nakreslete princip (zjednodušený obvod) pro vyhodnocování výstupního signálu.
![[indukcnostni_trafo_nebo_co.png]]
- Indukční zákon pro cívku s N závity
$$u=-N\frac{d\varPhi}{dt}$$
#### Transfomátorový senzor polohy (LVDT): Nakreslete princip činnosti
![[lvdt.png]]

#### Transfomátorový senzor polohy (LVDT) : Nakreslete zjednodušené obvodové zapojení pro vyhodnocování informace z LVDT senzoru
![[lvdt2.png]]
#### Indukční (magnetoinduktivní) senzor elektrodynamický (aktivní) : Nakreslete princip činnosti senzoru, napište magnetoinduktivní rovnici pro výstupní napětí, nakreslete zjednodušený obvod pro vyhodnocování výstupního signálu
![[magnetoinduktivni.png]]
- magnetoinduktivní rovnice
$$u=Bvl$$
#### Magnetoelastický senzor: Nakreslete a vysvětlete princip činnosti. Nakreslete příklad závislosti permeability, resp. indukčnosti na působící síle (mechanickém namáhání). Nakreslete příklad konstrukce magnetoelastických (lístkových) tenzometrů
![[magnetoelasticky.png]]
#### Magnetosktriční senzor: Nakreslete a vysvětlete princip činnosti
![[magnetostrikcni senzo.png]]
- Wiedemannův jev:
	- Feromagnetická tyč se torzně deformuje, když jí protéká proud a je v podélném magnetickém poli
- Inverzní Wiedemannův jev:
	- Torzně deformovaná tyč v kruhovém magnetickém poli indukuje ve vinutí napětí - vzniká výstupní signál.
#### Magnetoanizotropní senzor: Nakreslete a vysvětlete princip činnosti
![[magnetorezistivni_anizotropni_trpi.png]]
- Magnetoanizotropie vzniká při mechanickém namáhání, které deformuje magnetické pole v materiálu.
- Senzor tvoří primární a sekundární vinutí kolem jádra se symetrickými otvory.
- Bez zatížení:
	- Magnetický tok z primárního vinutí neindukuje napětí ve vinutí sekundárním
- Při deformaci:
	- vznikne magnetická aizotropie, zbýší se magnetická vazba -> na výstupu vzniká napětí úměrné mechanickému namáhání