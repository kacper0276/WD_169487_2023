import numpy as np


def generuj(n, m):
    cos = np.empty(m, dtype='int64')
    cos.fill(n)
    pomoc = np.arange(1, m+1)
    results = np.power(cos, pomoc)
    return results


a = eval(input("Podaj liczbę: "))
b = eval(input("Podaj ile potęg: "))

result = generuj(a, b)
print(result)
