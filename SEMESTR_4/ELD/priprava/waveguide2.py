import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parametry vlnovodu
a = 1.0   # šířka (x)
b = 0.5   # výška (y)
L = 2.0   # délka vlnovodu (z)

# Síť
x = np.linspace(0, a, 50)
y = np.linspace(0, b, 30)
z = np.linspace(0, L, 100)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# Parametry vlny
f = 10e9
c = 3e8
omega = 2 * np.pi * f
fc = c / (2 * a)
beta = 2 * np.pi * np.sqrt(f**2 - fc**2) / c

# Zobrazená složka pole – např. Ex
Ex = np.sin(np.pi * X / a) * np.cos(beta * Z)

# Vytvoření 3D grafu – pouze jedna rovina Y = b/2 (střední průřez)
y_slice_index = np.abs(y - b/2).argmin()
X_slice = X[:, y_slice_index, :]
Z_slice = Z[:, y_slice_index, :]
Ex_slice = Ex[:, y_slice_index, :]

# Vykreslení
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X_slice, Z_slice, Ex_slice, cmap='viridis', edgecolor='none')
ax.set_title("TE10 mód – průřez ve 3D (složka Ex)")
ax.set_xlabel("x [m]")
ax.set_ylabel("z [m]")
ax.set_zlabel("Ex [a.u.]")
fig.colorbar(surf, shrink=0.5, aspect=10)

plt.tight_layout()
plt.show()
