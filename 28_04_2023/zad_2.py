import matplotlib.pyplot as plt
import numpy as np

t = np.arange(1, 21, 1)
plt.plot(t, 1 / t, "g>:", label="f(x) = 1/x")
plt.title("Wykres funkcji f(x) dla x [1, 20]")
plt.axis([1, len(t), 0, 1])
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()