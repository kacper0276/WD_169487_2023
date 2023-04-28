import matplotlib.pyplot as plt
import numpy as np


arr = np.arange(0, 30, 0.1)
plt.plot(arr, np.sin(arr), "r", label="Sin(x)")
plt.plot(arr, np.cos(arr), "b", label="Cos(x)")
plt.title("Wykresy funkcji sinus i cosinus")
plt.legend(loc="upper right")
plt.xlabel('Wartości X')
plt.ylabel('Sin X/ Cos X')
plt.show()