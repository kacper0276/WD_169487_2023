import numpy as np

b = np.arange(1, 10).reshape(3, 3)

print(b)
# b.flat - tzw. 'Spłaszczanie macierzy'
for x in b.flat:
    print(x, end=" ")