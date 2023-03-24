import numpy as np

basic = np.arange(1, 13)
print(basic)

reshape_matrix_1 = basic.reshape(3, 4)
print(reshape_matrix_1)

reshape_matrix_2 = basic.reshape(4, 3)
print(reshape_matrix_2)

reshape_matrix_3 = basic.reshape(2, 6)
print(reshape_matrix_3)

print("Spłaszczona macierz 3x4: ")
for x in reshape_matrix_1.flat:
    print(x, end=" ")

print("")
print("Spłaszczona macierz 4x3: ")
for x in reshape_matrix_2.flat:
    print(x, end=" ")

print("")
print("Spłaszczona macierz 2x6: ")
for x in reshape_matrix_3.flat:
    print(x, end=" ")

print("")
if(reshape_matrix_1.all() == reshape_matrix_2.all() and reshape_matrix_1.all() == reshape_matrix_3.all() and reshape_matrix_3.all() == reshape_matrix_2.all()):
    print("TAK, są identyczne")