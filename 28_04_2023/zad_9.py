import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl


# Wykres 1
t = np.arange(1, 21, 1)
plt.plot(t, 1 / t, label="f(x) = 1/x")
plt.title("Wykres funkcji f(x) dla x [1, 20]")
plt.axis([1, len(t), 0, 1])
plt.annotate('Punkt (1,1)',
            xy=(1, 1), xycoords='data',
            xytext=(15, -25), textcoords='offset points',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='left', verticalalignment='top')
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

#Wykres 2
d = np.arange(1, 21, 1)
plt.plot(d, 1 / d, "g>:", label="f(x) = 1/x")
plt.title("Wykres funkcji f(x) dla x [1, 20]")
plt.axis([1, len(d), 0, 1])
plt.annotate('Punkt',
            xy=(5, 0.2), xycoords='data',
            xytext=(25, 25), textcoords='offset points',
            arrowprops=dict(facecolor='green', shrink=0.4),
            horizontalalignment='right', verticalalignment='bottom')
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()