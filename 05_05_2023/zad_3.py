import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# Wygeneruj wykrespowierzchniowy z przykładu z podpunktu 1.2 w 5 różnych kolorystkach: https://matplotlib.org/examples/color/colormaps_reference.html

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# Generowanie danych:
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
# tworzymy punkty o lokalizacji (X Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
# nadajemy tym punktom wartości
# Rysowanie powierzchni:
# surf = ax.plot_surface(X, Y, Z, cmap='Accent', linewidth=0, antialiased=False)
# surf = ax.plot_surface(X, Y, Z, cmap='BuPu', linewidth=0, antialiased=False)
# surf = ax.plot_surface(X, Y, Z, cmap='Blues', linewidth=0, antialiased=False)
# surf = ax.plot_surface(X, Y, Z, cmap='Greys', linewidth=0, antialiased=False)
surf = ax.plot_surface(X, Y, Z, cmap='Oranges_r', linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# Dodanie paska kolorów.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()