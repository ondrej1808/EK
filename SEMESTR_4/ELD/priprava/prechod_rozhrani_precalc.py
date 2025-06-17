import os
os.environ["OMP_NUM_THREADS"] = "4"        # pro MKL/OpenMP
os.environ["OPENBLAS_NUM_THREADS"] = "4"   # pro OpenBLAS

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Line3DCollection

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
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-2.1, 2.1)
ax.set_xlabel('E (x)')
ax.set_ylabel('H (y)')
ax.set_zlabel('z (šíření)')
ax.view_init(elev=30, azim=130)

# Rozhraní (rovina z=0)
X_plane, Y_plane = np.meshgrid(np.linspace(-1,1,2), np.linspace(-1,1,2))
Z_plane = np.zeros_like(X_plane)
ax.plot_surface(X_plane, Y_plane, Z_plane, color='black', alpha=0.3)

coll_E = None
coll_H = None

def heaviside(x, k=100):
    return 1 / (1 + np.exp(-k * x))

def update(frame):
    global coll_E, coll_H
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
    envelope_ref = heaviside(ti - 2 - z[top] / v1)
    E_ref = R * np.cos(phi_ref) * envelope_ref

    # Výsledná vlna je **součet** příchozí + odražené, bez přepisování
    E_x[top] = E_inc + E_ref
    H_y[top] = -(E_inc - E_ref) / Z1

    # --- Přenesená vlna (spodní oblast) ---
    phi_tr = omega * (ti - (-z[bottom]) / v2)
    envelope_tr = heaviside(ti - 2 - (-z[bottom]) / v2)
    E_tr = T_coef * np.cos(phi_tr) * envelope_tr
    E_x[bottom] = E_tr
    H_y[bottom] = -E_tr / Z2

    # Odebrat staré kolekce
    if coll_E:
        coll_E.remove()
    if coll_H:
        coll_H.remove()

    # Vytvořit segmenty jako array (N, 2, 3)
    segments_E = np.array([[[0, 0, zi], [Exi, 0, zi]] for zi, Exi in zip(z, E_x)])
    segments_H = np.array([[[0, 0, zi], [0, Hyi, zi]] for zi, Hyi in zip(z, H_y)])

    # Vytvořit nové kolekce čar
    coll_E = Line3DCollection(segments_E, colors='blue', linewidths=1)
    coll_H = Line3DCollection(segments_H, colors='red', linewidths=1)

    ax.add_collection3d(coll_E)
    ax.add_collection3d(coll_H)

    # Explicitně nastav rozsah os, aby se graf nesrazil
    ax.auto_scale_xyz([-1.5, 1.5], [-1.5, 1.5], [np.min(z), np.max(z)])

    ax.set_title(f"t = {ti:.2f} s")
    return coll_E, coll_H

ani = FuncAnimation(fig, update, frames=len(t), interval=16, blit=False)
plt.tight_layout()
plt.show()
