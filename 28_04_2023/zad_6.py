import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl

data = pd.read_excel("data/imiona.xlsx")
groupdataM = data[data.Plec == "M"].groupby(by="Rok", as_index=False).agg({"Liczba": "sum"})
groupdataK = data[data.Plec == "K"].groupby(by="Rok", as_index=False).agg({"Liczba": "sum"})
groupdata = data.groupby(by="Rok", as_index=False).agg({"Liczba": "sum"})

arrM = groupdataM["Liczba"].values
arrK = groupdataK["Liczba"].values
arr = groupdata["Liczba"].values
year = groupdataM["Rok"].values

# Wykres z słupkowego 1 podpunkt
plt.bar(year - 0.2, arrK, color="b", width=0.25, label="Kobiety urodzone w każdym roku")
plt.bar(year + 0.2, arrM, color="r", width=0.25, label="Mężczyźni urodzeni w każdym roku")

# Wykres liniowy 2 podpunkt
plt.plot(year, arrK, color="#000", label="Podpunkt 2 Kobiety")
plt.plot(year, arrM, color="y", label="Podpunkt 2 Mężczyźni")

# Wykres liniowy 3 podpunkt
plt.bar(year + 0.4, arr, color="#260291", width=0.25, label="Podpunkt 3")

plt.legend()
plt.xticks(year)
plt.ylabel('Ilość narodzin')
plt.xlabel('Rok')
plt.show()
