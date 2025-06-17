import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Fyzikální konstanty
mu0 = 1
eps1 = 1  # menší permitivita (např. vzduch)
eps2 = 4  # větší permitivita

# Výpočet impedance a vlnového čísla
Z1 = np.sqrt(mu0 / eps1)
Z2 = np.sqrt(mu0 / eps2)
n1 = np.sqrt(eps1)
n2 = np.sqrt(eps2)

# Reflexní a transmisní koeficienty
R = (Z2 - Z1) / (Z2 + Z1)
T = 2 * Z2 / (Z2 + Z1)

# Simulační parametry
x = np.linspace(-2, 2, 1000)
t = np.linspace(0, 10, 200)
k1 = 2 * np.pi * n1
k2 = 2 * np.pi * n2
omega = k1  # omega = k * c, ale c = 1 zde

# Příprava grafu
fig, axs = plt.subplots(2, 1, figsize=(10, 6))
line_E, = axs[0].plot([], [], 'b-', label='E pole')
line_H, = axs[1].plot([], [], 'r-', label='H pole')
axs[0].set_title('Elektrické pole E (stojatá vlna vlevo + šíření vpravo)')
axs[1].set_title('Magnetické pole H')
for ax in axs:
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.grid(True)
    ax.legend()

# Funkce pro výpočet pole
def calc_fields(ti):
    E = np.zeros_like(x)
    H = np.zeros_like(x)

    left = x < 0
    right = x >= 0

    # Vlevo: superpozice dopadající a odražené vlny = stojatá vlna
    E[left] = np.cos(k1 * x[left] - omega * ti) + R * np.cos(-k1 * x[left] - omega * ti)
    H[left] = (np.cos(k1 * x[left] - omega * ti) - R * np.cos(-k1 * x[left] - omega * ti)) / Z1

    # Vpravo: přenesená vlna
    E[right] = T * np.cos(k2 * x[right] - omega * ti)
    H[right] = T * np.cos(k2 * x[right] - omega * ti) / Z2

    return E, H

# Aktualizace pro animaci
def update(frame):
    ti = t[frame]
    E, H = calc_fields(ti)
    line_E.set_data(x, E)
    line_H.set_data(x, H)
    return line_E, line_H

ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)
plt.tight_layout()
plt.show()
