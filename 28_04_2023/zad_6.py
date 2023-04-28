import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl

data = pd.read_excel("data/imiona.xlsx")
groupdataM = data[data.Plec == "M"].groupby(by="Rok", as_index=False).agg({"Liczba": "sum"})
groupdataK = data[data.Plec == "K"].groupby(by="Rok", as_index=False).agg({"Liczba": "sum"})

print(groupdataM["Liczba"])



etykiety = [groupdataM]
wartosci = [groupdataK]
c = ["#000000", "#104390"]
plt.bar(etykiety, wartosci)
# plt.xticks(rotation=45)
plt.ylabel('Ilość narodzin')
plt.xlabel('Rok')
plt.show()