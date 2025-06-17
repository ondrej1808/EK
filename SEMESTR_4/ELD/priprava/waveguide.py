import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parametry vlnovodu
a = 1.0  # šířka
b = 0.5  # výška

x = np.linspace(0, a, 100)
y = np.linspace(0, b, 50)
X, Y = np.meshgrid(x, y)

# Parametry vlny
f = 10e9
c = 3e8
fc = c / (2 * a)
beta = 2 * np.pi * np.sqrt(f**2 - fc**2) / c
omega = 2 * np.pi * f

# Počáteční pole
t0 = 0
Ez = np.cos(np.pi * X / a) * np.cos(omega * t0 - beta * X)

fig, ax = plt.subplots()
cont = ax.contourf(X, Y, Ez, levels=50, cmap='RdBu_r')
cbar = fig.colorbar(cont, ax=ax)
ax.set_title("TE10 mód – čas t = 0 ns")
ax.set_xlabel("x")
ax.set_ylabel("y")

# Aktualizační funkce
def update(t):
    ax.clear()
    Ez = np.cos(np.pi * X / a) * np.cos(omega * t - beta * X)
    cont = ax.contourf(X, Y, Ez, levels=50, cmap='RdBu_r')
    ax.set_title(f"TE10 mód – čas t = {t * 1e9:.2f} ns")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    return cont.collections  # nutné pro správné vykreslování

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1e-9, 60), interval=50, blit=False)
plt.tight_layout()
plt.show()
