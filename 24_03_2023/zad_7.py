import numpy as np
import math
from zad_5 import array


def dodaj(x, y):
    result = np.zeros(shape=(x.shape))
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]
    return result


a = np.sin(array)
b = np.cos(array)

print(f"Macierz a: {a}")
print(f"Macierz b: {b}")
print(dodaj(a, b))
