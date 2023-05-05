import matplotlib.pyplot as plt
import numpy as np

# Wygeneruj z pomocą dokumentacji wykres słupkowy z przykładu z podpunktu 1.3 wykorzystując 4 różne kombinacje wyglądu.

# Konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
fig = plt.figure(figsize=(8, 3))
# ax1 = fig.add_subplot(121, projection='3d')
# ax2 = fig.add_subplot(122, projection='3d')
ax3 = fig.add_subplot(222, projection='3d')
ax4 = fig.add_subplot(211, projection='3d')
ax5 = fig.add_subplot(212, projection='3d')
ax6 = fig.add_subplot(221, projection='3d')

# Wygenerowane dane
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
# ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_title('Wykres zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax2.set_title('Wykres nie zacieniony')
ax3.bar3d(x, y, bottom, width, depth, top, shade=True, color='salmon')
ax3.set_title("Wykres 3")
ax4.bar3d(x, y, bottom, width, depth, top, shade=False, color='hotpink')
ax4.set_title("Wykres 4")
ax5.bar3d(x, y, bottom, width, depth, top, shade=True, color='yellow')
ax5.set_title("Wykres 5")
ax6.bar3d(x, y, bottom, width, depth, top, shade=False, color='w')
ax6.set_title("Wykres 6")
plt.show()
