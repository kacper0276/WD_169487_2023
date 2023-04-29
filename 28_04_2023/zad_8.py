import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl

data = pd.read_csv("data/zamowienia.csv", sep=";")
datasuma = data.groupby(by="Sprzedawca", as_index=False).agg({"Utarg": "sum"})

arrsuma = datasuma["Utarg"].values
arrsprzedawca = datasuma["Sprzedawca"].values

print(arrsuma)
print(arrsprzedawca)

plt.pie(arrsuma, labels=arrsprzedawca, autopct=lambda pct:"{:.1f}%".format(pct),textprops=dict(color="black"))
plt.show()