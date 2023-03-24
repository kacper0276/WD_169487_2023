import numpy as np
import random

random.seed(123)

a = np.random.randint(10, 50, size=(3, 3))
b = np.array([random.randint(10, 50) for x in range(16)]).reshape(4, 4)

print(a)
print(b)

print(f"Minimum rzędu macierzy b: {b.min(axis=1)}")
print(f"Minimum kolumn macierzy b: {b.min(axis=0)}")
print(f"Minimum rzędu macierzy a: {a.min(axis=1)}")
print(f"Minimum kolumn macierzy a: {a.min(axis=0)}")

