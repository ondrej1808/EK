import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parametry prostředí
mu0 = 1
eps1 = 1       # horní oblast (z > 0)
eps2 = 4       # dolní oblast (z < 0)

Z1 = np.sqrt(mu0 / eps1)
Z2 = np.sqrt(mu0 / eps2)
n1 = np.sqrt(eps1)
n2 = np.sqrt(eps2)
R = (Z2 - Z1) / (Z2 + Z1)
T = 2 * Z2 / (Z2 + Z1)

# Záporný směr šíření (shora dolů): z = 2 → -2
z = np.linspace(2, -2, 60)
t = np.linspace(0, 12, 300)

k1 = 2 * np.pi * n1
k2 = 2 * np.pi * n2
omega = k1  # protože c = 1

# Inicializace grafu
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-2.1, 2.1)
ax.set_xlabel('E (x)')
ax.set_ylabel('H (y)')
ax.set_zlabel('z (šíření)')
ax.view_init(elev=20, azim=135)

quiv_E = None
quiv_H = None

# Výpočet polí
def calculate_fields(ti):
    E_x = np.zeros_like(z)
    H_y = np.zeros_like(z)

    top = z > 0  # oblast 1 (horní)
    bottom = z <= 0  # oblast 2 (dolní)

    # Vlna se šíří směrem -z → fáze je -kz - wt
    # Dopředná (příchozí), odražená, přenesená
    E_x[top] = np.cos(-k1 * z[top] - omega * ti) + R * np.cos(k1 * z[top] - omega * ti)
    #H_y[top] = (np.cos(-k1 * z[top] - omega * ti) - R * np.cos(k1 * z[top] - omega * ti)) / Z1

    E_x[bottom] = T * np.cos(-k2 * z[bottom] - omega * ti)
    #H_y[bottom] = T * np.cos(-k2 * z[bottom] - omega * ti) / Z2

    H_y[top] = - (np.cos(-k1 * z[top] - omega * ti) - R * np.cos(k1 * z[top] - omega * ti)) / Z1
    H_y[bottom] = - T * np.cos(-k2 * z[bottom] - omega * ti) / Z2

    return E_x, H_y

# Aktualizace animace
def update(frame):
    global quiv_E, quiv_H
    ti = t[frame]
    E_x, H_y = calculate_fields(ti)

    if quiv_E:
        quiv_E.remove()
    if quiv_H:
        quiv_H.remove()

    origin = np.zeros_like(z)

    # E (modrá šipka ve směru x)
    quiv_E = ax.quiver(origin, origin, z,
                       E_x, origin, origin,
                       length=0.2, normalize=False, color='blue')

    # H (červená šipka ve směru y)
    quiv_H = ax.quiver(origin, origin, z,
                       origin, H_y, origin,
                       length=0.2, normalize=False, color='red')

    ax.set_title(f"t = {ti:.2f}")
    return quiv_E, quiv_H

# Rozhraní z = 0 (rovinná plocha XY)
X_plane, Y_plane = np.meshgrid(np.linspace(-1, 1, 2), np.linspace(-1, 1, 2))
Z_plane = np.zeros_like(X_plane)
ax.plot_surface(X_plane, Y_plane, Z_plane, color='black', alpha=0.3)

ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=False)
plt.tight_layout()
plt.show()
