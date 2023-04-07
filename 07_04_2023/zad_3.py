import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

data = pd.read_excel('data/imiona.xlsx')
year = data['Rok'].unique()

last_five_years = np.array([year[len(year) - 1], year[len(year) - 2], year[len(year) - 3], year[len(year) - 4], year[len(year) - 5]])

chlopcy = data[data["Plec"] == "M"]
dziewczynki = data[data["Plec"] == "K"]
for_year_c = chlopcy.groupby(by="Rok").agg({"Liczba": "sum"})
for_year_d = dziewczynki.groupby(by="Rok").agg({"Liczba": "sum"})

only_count_m = for_year_c["Liczba"]
only_count_d = for_year_d["Liczba"]

only_count_m = only_count_m.reset_index(drop=True)
only_count_d = only_count_d.reset_index(drop=True)

array_numbers_m = []
array_numbers_d = []

for i in range(13, 18):
    array_numbers_m.append(only_count_m[i])
    array_numbers_d.append(only_count_d[i])

# Wykres dla chłopców
plt.pie(array_numbers_m, labels=last_five_years)

# Wykres dla dziewczynek
plt.pie(array_numbers_d, labels=last_five_years)

plt.show()

