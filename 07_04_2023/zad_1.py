import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

data = pd.read_excel("data/imiona.xlsx")

for_year = data.groupby(by="Rok").agg({"Liczba": "sum"})

print(for_year)

# Wykres słupkowy
# wykres = for_year.plot.bar(rot=0)
# wykres.set_ylabel("Ile urodzeń")
# wykres.set_xlabel("Jaki rok")
# wykres.legend()
# plt.title("Urodzenia dzieci w danym roku")
# plt.show()

wykres = for_year.plot.line(rot=0)
wykres.set_ylabel("Ile urodzeń")
wykres.set_xlabel("Jaki rok")
wykres.legend()
plt.title("Urodzenia dzieci w danym roku")
plt.show()
