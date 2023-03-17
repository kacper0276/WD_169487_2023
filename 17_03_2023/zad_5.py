import numpy as np


def funkcja(n):
    reverse = np.flip(np.arange(1, n+1))
    print(reverse)
    mat_diag = np.diag(reverse)
    print(mat_diag)


liczba = eval(input("Podaj liczbę: "))
funkcja(liczba)