#### Spojitý signál: s(t)
#### Diskrétní signál: s\[k]

#### Komplexní sdružení $s^*$
$s(t) = Re(s) + Im(s)$
$s^*(t)=Re(s)-Im(s)$
$s(t)\cdot s^*(t)=|s(t)|^2$
#### Operátor $Av()$
- Obecně:
$$Av(s(t))=\lim_{T\rightarrow\infty}\frac{1}{2T}\int_{-\infty}^{\infty}s(t)\space dt$$
- Pro periodické signály - stačí integrovat přes jeho periodu:
- EXTRÉMNĚ užitečné pro výpočet výkonu !
$$Av(s(t))=\frac{1}{T_0}\int_{(T_0)}s(t)\space dt$$
#### Energetický signál 
- má konečnou energii, ale nekonečný výkon
- Finitní singál je vždy energetický
#### Výkonový signál 
- má konečný výkon, ale nekonečnou energii
- Periodický signál je vždy výkonový

| Vzorečky vole    | Pro spojitý signál:                                                                                                  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| Energie          | $$E=\int_{-\infty}^{\infty}\|s(t)\|^2 dt=\int_{-\infty}^{\infty}s(t)\cdot s^*(t) dt$$                                |
| Výkon            | $$P=Av{(\|s(t)\|^2})=\lim_{T\rightarrow\infty}\frac{1}{2T}\int_{-\infty}^{\infty}\|s(t)\|^2 dt$$                     |
| Vzájemná energie | $$E_{1,2}=\int_{-\infty}^{\infty}s_1(t)\cdot s_2^*(t) dt$$                                                           |
| Vzájemný výkon   | $$P=Av{(s_1(t)\cdot s_2^*(t)})=\lim_{T\rightarrow\infty}\frac{1}{2T}\int_{-\infty}^{\infty}s_1(t)\cdot s_2^*(t) dt$$ |

<div style="page-break-after: always;"></div>

#### Korelační funkce
$$R_{12}(\tau)=\int_{-\infty}^{\infty}s_1(t+\tau)\cdot s_2^*(t)\space dt$$
#### Autokorelační funkce
- Pokud je signál reálný tak $R(\tau)$ je sudá
- Pro energetický signál:
$$R(\tau)=\int_{-\infty}^{\infty}s(t+\tau)\cdot s^*(t)\space dt$$
	 - Autokorelační funkce v nule je energie signálu$R(\tau = 0) = E$
- Pro výkonový signál:
$$R(\tau)=Av(s(t+\tau)\cdot s^*(t))\space dt$$
	- Autokorelační funkce v nule je výkon signálu   $R(\tau = 0) = P$

#### Fourierova řada - koeficienty
- Rozložení periodického signálu s periodou $T_0$ na harmonické
$$s_1(t)=\sum_{n=-\infty}^{\infty}c_{1,n}\cdot e^{j n \omega_0 t}$$
$$\omega_0=\frac{2\pi}{T_0}$$
	$$c_{1,n}=\frac{1}{T_0}\int_{0}^{T_0}s_1(t)\cdot e^{-jn\omega_0t}\space dt$$
- Nultý koeficient odpovídá stejnosměrné složce
$$c_{1,0}=s_{DC}$$
- Z nultého koeficientu = stejnosměrné složky můžeme určit energii/výkon stejnosměrné složky

<div style="page-break-after: always;"></div>


#### Vlastnosti sudých a lichých fcí
suda x suda = Suda, 
licha x licha = licha, 
suda x licha = licha, 
licha(-x) = -licha(x), 
Suda(-x)=suda(x)
#### Sin a cos vzorečky
![[Pasted image 20250404141305.png]]
![[Pasted image 20250404141405.png]]
![[Pasted image 20250404141433.png]]
![[Pasted image 20250404141440.png]]
![[Pasted image 20250404141513.png]]
![[Pasted image 20250404141521.png]]
![[Pasted image 20250404141622.png]]
![[Pasted image 20250404141642.png]]
![[Pasted image 20250404141706.png]]
![[Pasted image 20250404141733.png]]
