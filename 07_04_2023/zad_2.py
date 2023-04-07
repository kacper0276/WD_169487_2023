import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt


data = pd.read_excel("data/imiona.xlsx")

chlopcy = data[data["Plec"] == "M"]
dziewczynki = data[data["Plec"] == "K"]
for_year_c = chlopcy.groupby(by="Rok").agg({"Liczba": "sum"})
for_year_d = dziewczynki.groupby(by="Rok").agg({"Liczba": "sum"})

only_count_m = for_year_c["Liczba"]
only_count_d = for_year_d["Liczba"]


width = 0.5
label = data["Rok"].unique()

plt.bar(label + width/2, only_count_m, width=0.5, label='values_A')
plt.bar(label - width/2, only_count_d, width=0.5, label='values_B')
plt.xlabel("Jaki rok")
plt.ylabel("Ile urodzeń")
plt.legend()
plt.title("Urodzenia dzieci w danym roku")
plt.show()