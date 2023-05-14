import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import openpyxl
import seaborn as sns

df = pd.read_excel('./data/imiona.xlsx')

dfk = df[(df['Plec'] == 'K') & (df["Rok"] >= 2010) & (df["Rok"] <= 2015)]
dfm = df[(df['Plec'] == 'M') & (df["Rok"] >= 2010) & (df["Rok"] <= 2015)]

dfm = dfm.agg({"Liczba": "sum"}).reset_index()
dfk = dfk.agg({"Liczba": "sum"}).reset_index()

wykres = {"K": dfk[0][0], "M": dfm[0][0]}

print(wykres)

plt.bar("M",dfm[0][0], width=0.5)
plt.bar("K",dfk[0][0], width=0.5)
plt.title("Matplotlib wykres")

plt.show()

sns.barplot(data=wykres, x='Plec', y="Liczba urodzen")
