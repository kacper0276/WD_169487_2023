import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

data = pd.read_csv("data/zamowienia.csv", sep=";")

pogrupowane = data.groupby(by="Sprzedawca").agg({"Utarg": "sum"}).apply(list)
df = pogrupowane.reset_index()
sprzedawcy = df["Sprzedawca"]
suma = df["Utarg"]


plt.bar(sprzedawcy, suma, color=['g', 'r', 'b', 'g', 'b', 'g', 'r', 'b', 'r'])
plt.legend()
plt.xlabel("Sprzedawcy")
plt.ylabel("Łączny utarg")
plt.show()
