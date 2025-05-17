#### Charakterizujte jednotlivé vrstvy zemské atmosféry z hlediska vlivu na rádiové spoje?
Troposféra - do 11 km
	nejdůležitejší
	silně ovlivněná počasím
		ovlivněna teplotou, tlakem, vlhkostí
Stratosféra - do 60 km
	zde toho moc nelítá, podobné parametry jako troposféra, není tak důležitá
Ionosféra - do 600 km
	obsahuje ionizované částice
	díky nim může dojít odrazu či vedení vlny
#### Jaké jsou příčiny útlumu rádiových vln způsobeného atmosférickými plyny? Naznačte graficky závislost tohoto útlumu na frekvenci (0 – 100 GHz).
Rezonance molekul nekondenzovaných plynů obsažených v atmosféře způsobuje útlum
![[utlumvlnatmo.png]]

#### Jaké jsou řádově hodnoty elektrických parametrů typických zemských povrchů: suchá/vlhká země a slaná voda?
mořská voda $\sigma = 0.9 S/m$
vlhká půda $\sigma = 5*10^{-3} S/m$
suchá půda  $\sigma = 8*10^{-5} S/m$
#### Co je to refraktivita a jakých hodnot nabývá v troposféře?
Refraktivita N
$$
N = (n-1)*10^6
$$
Kde n = index lomu troposféry
Přibližně 325 až 110 N??
#### Definujte standardní atmosféru.
platí $$dN/dh= -40 N/km$$
což znamená že s 50 % pravděpodobností refraktiva klesá s výškou se sklonem 40 N/km
#### Vysvětlete princip troposférické refrakce a uveďte její základní případy.
Je to jako když nám vlna nebo paprsek světla přecházel mezi n1 a n2. 
Vlna se při přechodu mezi troposférou a ionosférou zakřivuje.
základní případy:
![[refrakce.png]]
#### Vysvětlete pojem efektivní poloměr Země.
> Uvažování křivočarého šíření nad zakřivenou zemí je v technické praxi velmi komplikované, proto se zavádí speciální transformace, která určitou změnou křivosti paprsku i povrchu Země „narovná“ zakřivený paprsek

Jsem línej ohýbat paprsek, tak ohnu zemi 
$$R_0 \dot =8500 km$$
#### Co je to a jak vzniká tzv. vlnovodný kanál při šíření rádiové vlny v troposféře?
Je to nekonečně dlouhý kanál okolo Země
Vzniká tak, že se poloměr křivosti paprsku rovná poloměru Země. Vlna se pak teoreticky šíří rovnoběžně s povrchem Země. Přibližně při -157 N/km
#### Popište vliv hydrometeorů na šíření rádiových vln?
Způsobují útlum a tlumí vlnu 
#### Vysvětlete základní princip difrakce a načrtněte závislost přenosu či útlumu na postupném zastiňování rádiového spoje ostrou překážkou.
šíření vlny do oblasti optického stínu
vlny jsou všude (i ve zdech)
![[difrakce.png]]
#### Vysvětlete pojem Fresnelovy zóny.
> oblast prostoru mezi vysílačem a přijímačem, kde vlny, které cestují různými drahami (ne nutně po přímce), interferují s přímou vlnou. Tyto zóny určují, jak moc může překážka ovlivnit příjem signálu.

je to elipsa rozsekaná na podelipsu různých průměrů podle toho jak moc vadí signálu když tam zrovna někdo stojí
Důležitá je 1.zóna, nejvíc ovlivní kolik signálu přenese
#### Načrtněte závislost koeficientu odrazu na úhlu dopadu pro rádiovou vlnu dopadající na rovinné rozhraní.
![[eldjemrdka.png]]
viz ELD
pankrác by vám toho řekl víc
#### Jaký je postup při analýze kritéria volného profilu u pozemního směrového spoje?
Obecně se za splnění kritéria volného profilu považuje nezastínění celého poloměru 1. Fresnelovy zóny pro k e = 4/3 (standardní atmosféra).
#### Popište základní typy a příčiny úniků v troposféře při šíření prostorové vlny u směrového spoje.
1. Ploché úniky (Flat Fading)
    Popis: Útlum je konstantní přes celé frekvenční pásmo přenosu.
    Příčina: Nejčastěji atmosférická refrakce, která vychýlí hlavní směr šíření elektromagnetické energie.
2. Absorpční úniky
    Popis: Zvláštní podskupina plochých úniků.
    Příčina: Absorpce elektromagnetických vln v atmosféře, typicky vlivem dešťových srážek.
3. Frekvenčně selektivní úniky (Multipath Fading)
    Popis: Útlum se mění v závislosti na frekvenci – tedy různá frekvenční složka signálu je útlumena různě.
    Příčina: Vícecestné šíření – v místě příjmu se skládají primární (přímá) a druhotné (odražené, difraktované apod.) vlny.
#### Jaké jsou zásadní rozdíly mezi pevným a mobilním pozemním rádiovým spojem z hlediska šíření signálu?
| Hledisko                      | Pevný pozemní spoj                              | Mobilní pozemní spoj                              |
|------------------------------|--------------------------------------------------|---------------------------------------------------|
| **Geometrie**                | Stanice ve stálých, známých pozicích            | Jedna nebo obě stanice se pohybují                |
| **Stabilita prostředí**      | Stabilní, neměnné podmínky                      | Rychle proměnlivé prostředí                       |
| **Typ úniků (fading)**       | Plochý fading (např. refrakce)                  | Frekvenčně selektivní fading (vícecestné šíření) |
| **Dynamika signálu**         | Pomalu proměnlivý signál                        | Rychlé výkyvy signálu                             |
| **Vliv prostředí**           | Minimální, často přímá viditelnost              | Silné odrazy, stínění, difrakce                   |
| **Modelování šíření**        | Deterministické modely (např. Fresnel, difrakce)| Empirické/semi-empirické modely (statistika)     |
| **Typ přenosu**              | Bod–bod                                         | Bod–mnohobod                                      |
| **Antény**                   | Směrové antény (např. parabolické)             | Omnidirekční nebo sektorové antény               |
| **Přesnost plánování**       | Vysoká, lze přesně spočítat výkonovou bilanci   | Nižší, důraz na pokrytí a adaptivitu             |
#### Popište šíření prostorové vlny nad rovinnou zemí. (Nezapomeňte uvést základní průběh spádové křivky.)
- Dochází k interferenci přímé a odražené vlny.    
- Úroveň signálu periodicky kolísá s maximy a minimy.    
- Spádová křivka vykazuje přechod ze spádu 20 dB/dekádu na 40 dB/dekádu po překročení Fresnelova zlomu.    
- Reálné prostředí vyhlazuje ostré změny, ale základní trend zůstává.
- ![[sireninadrovinnouzemi.png]]
#### Definujte Fresnelův zlom a jeho význam po mobilní bezdrátový spoj.
Jde o vzdálenost, při které je dráhový rozdíl přímého a odraženého paprsku roven polovině vlnové délky.
$$d_0 = \frac{4h_1h_2}{\lambda}$$
#### Vysvětlete základní mechanizmy šíření rádiové vlny v městské zástavbě.
V městské zástavbě se rádiová vlna šíří zejména odrazy od budov, difrakcí na hranách a rozptylem na nerovnostech povrchů. Dochází k vícecestnému šíření (multipath), které způsobuje interferenci a úniky signálu. Přímá viditelnost bývá často narušena, a proto přenos závisí na nepřímých cestách.
#### Charakterizujte základní empirický model šíření vlny v zástavbě a uveďte příklady spádového koeficientu.
Empirický model šíření vlny v zástavbě popisuje průměrný útlum signálu jako funkci vzdálenosti bez nutnosti znát detaily prostředí. Útlum roste podle vzorce $L(d) = L(d_0) + 10n \log_{10}(d/d_0)$, kde $n$ je spádový koeficient. Typické hodnoty $n$ jsou 2 pro volný prostor, 3–5 pro městskou zástavbu a až 6 uvnitř budov.

#### Porovnejte výhody/nevýhody empirického a deterministického přístupu k modelování šíření vln v zástavbě.
|                         | Empirický model                       | Deterministický model                               |
| ----------------------- | ------------------------------------- | --------------------------------------------------- |
| **Přesnost**            | Nižší, dává průměrné výsledky         | Vysoká, zohledňuje konkrétní geometrii prostředí    |
| **Potřeba dat**         | Minimální, nevyžaduje detailní mapy   | Vyžaduje podrobné 3D modely a parametry materiálů   |
| **Výpočetní náročnost** | Nízká, vhodné pro rychlé odhady       | Vysoká, nutné numerické výpočty (např. ray tracing) |
| **Využití**             | Plánování pokrytí, statistické odhady | Přesný návrh spojů v konkrétním prostředí           |
