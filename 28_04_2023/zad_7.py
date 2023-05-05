import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl
import random

random.seed()

def rzut(n):
    arr = []
    for i in range(0, n):
        suma = random.randint(1, 6) + random.randint(1, 6)
        arr.append(suma)
    return arr


ilosc = rzut(6)
rzuty = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(rzuty)
print(ilosc)
plt.hist(ilosc, rzuty, facecolor="g")
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
plt.grid(True)
plt.show()
