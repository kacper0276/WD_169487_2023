import numpy as np

a = np.array([x for x in range(9)]).reshape(3, 3)

print(f"Wygląd macierzy: {a}")

for x in range(len(a)):
    print(a[x], end=" ")
