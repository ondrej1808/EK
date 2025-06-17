import os
os.environ["OMP_NUM_THREADS"] = "4"
os.environ["OPENBLAS_NUM_THREADS"] = "4"

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Parametry materiálů
mu0 = 1.0
eps1 = 1.0
eps2 = 4.0

Z1 = np.sqrt(mu0 / eps1)
Z2 = np.sqrt(mu0 / eps2)
n1 = np.sqrt(eps1)
n2 = np.sqrt(eps2)

R = (Z2 - Z1) / (Z2 + Z1)
T_coef = 2 * Z2 / (Z2 + Z1)

# Parametry vlny
f = 1.0
omega = 2 * np.pi * f
lambda1 = 1.0
c = 1.0
v1 = c / n1
v2 = c / n2

# Prostor a čas
z = np.linspace(2, -2, 300)
t = np.linspace(0, 6, 300)

def heaviside(x, k=100):
    return 1 / (1 + np.exp(-k * x))

fig, (axE, axH) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

axE.set_xlim(z.min(), z.max())
axE.set_ylim(-2, 2)
axE.set_ylabel('E (x)')
axE.set_title('Elektrické pole E(x)')
axE.axvline(0, color='black', linestyle='--', linewidth=1, label='Rozhraní')

axH.set_xlim(z.min(), z.max())
axH.set_ylim(-2, 2)
axH.set_ylabel('H (y)')
axH.set_xlabel('z (šíření)')
axH.axvline(0, color='black', linestyle='--', linewidth=1, label='Rozhraní')

lineE, = axE.plot([], [], color='blue')
lineH, = axH.plot([], [], color='red')

axE.legend()
axH.legend()

def update(frame):
    ti = t[frame]

    E_x = np.zeros_like(z)
    H_y = np.zeros_like(z)

    top = z > 0
    bottom = z <= 0

    phi_inc = omega * (ti - (2 - z[top]) / v1)
    envelope_inc = heaviside(ti - (2 - z[top]) / v1)
    E_inc = np.cos(phi_inc) * envelope_inc

    phi_ref = omega * (ti - z[top] / v1)
    envelope_ref = heaviside(ti - 2 - z[top] / v1)
    E_ref = R * np.cos(phi_ref) * envelope_ref

    E_x[top] = E_inc + E_ref
    H_y[top] = -(E_inc - E_ref) / Z1

    phi_tr = omega * (ti - (-z[bottom]) / v2)
    envelope_tr = heaviside(ti - 2 - (-z[bottom]) / v2)
    E_tr = T_coef * np.cos(phi_tr) * envelope_tr
    E_x[bottom] = E_tr
    H_y[bottom] = -E_tr / Z2

    lineE.set_data(z, E_x)
    lineH.set_data(z, H_y)

    axE.set_title(f'Čas t = {ti:.2f} s')
    return lineE, lineH

ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

# Export do GIF
ani.save("wave_animation.gif", writer=PillowWriter(fps=30))

plt.show()
