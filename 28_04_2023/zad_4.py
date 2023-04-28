import matplotlib.pyplot as plt
import numpy as np


arr = np.arange(0, 30, 0.1)
plt.plot(arr, -np.sin(arr), color="orange", label="Sin(x)")
plt.plot(arr, np.sin(arr) + 2, color="#33A5FF", label="Sin(x)")
plt.title("Wykresy sin(x), sin(x)")
plt.legend(loc="upper right")
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()