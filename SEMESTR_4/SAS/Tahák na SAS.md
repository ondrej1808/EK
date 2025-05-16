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
licha x licha = suda, 
suda x licha = licha, 
licha(-x) = -licha(x), 
Suda(-x)=suda(x)
#### Sin a cos vzorečky
##### Součtové vzorce

$$
\sin(a \pm b) = \sin a \cos b \pm \cos a \sin b
$$

$$
\cos(a \pm b) = \cos a \cos b \mp \sin a \sin b
$$

$$
\sinh(a \pm b) = \sinh a \cosh b \pm \cosh a \sinh b
$$

$$
\cosh(a \pm b) = \cosh a \cosh b \pm \sinh a \sinh b
$$

---

##### Redukce druhé mocniny (power reduction)

$$
\sin^2 x = \frac{1 - \cos(2x)}{2}
$$

$$
\cos^2 x = \frac{1 + \cos(2x)}{2}
$$

$$
\sinh^2 x = \frac{\cosh(2x) - 1}{2}
$$

$$
\cosh^2 x = \frac{\cosh(2x) + 1}{2}
$$

---

##### Pythagorova věta

$$
\sin^2 x + \cos^2 x = 1
$$

$$
\cosh^2 x - \sinh^2 x = 1
$$

---

##### Komplexní exponenciály

$$
\sin x = \frac{e^{ix} - e^{-ix}}{2i}
$$

$$
\cos x = \frac{e^{ix} + e^{-ix}}{2}
$$

$$
\sinh x = \frac{e^{x} - e^{-x}}{2}
$$

$$
\cosh x = \frac{e^{x} + e^{-x}}{2}
$$

---

##### Dvojnásobek argumentu

$$
\sin(2x) = 2 \sin x \cos x
$$

$$
\cos(2x) = \cos^2 x - \sin^2 x = 2 \cos^2 x - 1 = 1 - 2 \sin^2 x
$$

$$
\sinh(2x) = 2 \sinh x \cosh x
$$

$$
\cosh(2x) = \cosh^2 x + \sinh^2 x
$$
