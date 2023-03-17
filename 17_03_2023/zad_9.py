import numpy as np

tablica = np.empty(25, dtype='int64')

def fibonacci(n):
    a = 0
    b = 1
    iterator = 1
    tablica[0] = 1

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            tablica[iterator] = b
            iterator = iterator + 1
        return tablica.reshape(5,5)


print(fibonacci(25))
