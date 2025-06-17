import os
os.environ["OMP_NUM_THREADS"] = "4"        # pro MKL/OpenMP
os.environ["OPENBLAS_NUM_THREADS"] = "4"   # pro OpenBLAS
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
c = 1.0  # zvoleno pro jednoduchost
v1 = c / n1
v2 = c / n2

# Prostor a čas
z = np.linspace(2, -2, 300)
t = np.linspace(0, 6, 300)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-2.1, 2.1)
ax.set_xlabel('E (x)')
ax.set_ylabel('H (y)')
ax.set_zlabel('z (šíření)')
ax.view_init(elev=30, azim=130)

# Rozhraní
X_plane, Y_plane = np.meshgrid(np.linspace(-1,1,2), np.linspace(-1,1,2))
Z_plane = np.zeros_like(X_plane)
ax.plot_surface(X_plane, Y_plane, Z_plane, color='black', alpha=0.3)

quiv_E = None
quiv_H = None

def heaviside(x, k=100):
    #return 0.5 * (np.sign(x) + 1)
    return 1 / (1 + np.exp(-k * x))
def update(frame):
    global quiv_E, quiv_H
    ti = t[frame]

    E_x = np.zeros_like(z)
    H_y = np.zeros_like(z)

    top = z > 0
    bottom = z <= 0

    # --- Příchozí vlna (horní oblast) ---
    phi_inc = omega * (ti - (2 - z[top]) / v1)
    envelope_inc = heaviside(ti - (2 - z[top]) / v1)
    E_inc = np.cos(phi_inc) * envelope_inc

    # --- Odražená vlna (horní oblast), postupně od t=2 ---
    phi_ref = omega * (ti - z[top] / v1)
    envelope_ref = heaviside(ti-2 - z[top] / v1)
    E_ref = R * np.cos(phi_ref) * envelope_ref

    # Výsledná vlna je **součet** příchozí + odražené, bez přepisování
    E_x[top] = E_inc + E_ref
    H_y[top] = -(E_inc - E_ref) / Z1

    # --- Přenesená vlna (spodní oblast) ---
    phi_tr = omega * (ti - (-z[bottom]) / v2)
    envelope_tr = heaviside(ti-2 - (-z[bottom]) / v2)
    E_tr = T_coef * np.cos(phi_tr) * envelope_tr
    E_x[bottom] = E_tr
    H_y[bottom] = -E_tr / Z2

    # Vymazat staré šipky
    if quiv_E:
        quiv_E.remove()
    if quiv_H:
        quiv_H.remove()

    origin = np.zeros_like(z)

    # E šipky modré v ose x
    quiv_E = ax.quiver(origin, origin, z,
                       E_x, origin, origin,
                       length=0.12, normalize=False, color='blue')
    # H šipky červené v ose y
    quiv_H = ax.quiver(origin, origin, z,
                       origin, H_y, origin,
                       length=0.12, normalize=False, color='red')

    ax.set_title(f"t = {ti:.2f} s")
    return quiv_E, quiv_H

ani = FuncAnimation(fig, update, frames=len(t), interval=16, blit=False)
plt.tight_layout()
plt.show()
