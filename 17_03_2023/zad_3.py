import numpy as np


def funkcja(n):
    number_add = 1
    a = np.empty(shape=(n, n))
    for i in range(n):
        for j in range(n):
            a[i][j] = number_add
            number_add = number_add + 1
    return a


def prostsze(n):
    b = np.arange(1, n*n+1).reshape(n, n)
    return b


number = eval(input("Podaj liczbę: "))
returned_array = funkcja(number)
print(returned_array)

proste = prostsze(number)
print(proste)