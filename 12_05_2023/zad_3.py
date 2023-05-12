import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
import seaborn as sb

df = pd.read_excel('./data/imiona.xlsx')
years = [2010, 2011, 2012, 2013, 2014, 2015]

dfk = df[(df['Plec'] == 'K') & (df["Rok"] >= 2010) & (df["Rok"] <= 2015)]
dfm = df[(df['Plec'] == 'M') & (df["Rok"] >= 2010) & (df["Rok"] <= 2015)]

dfm = dfm.groupby(by="Rok").agg({"Liczba": "sum"}).reset_index()
dfk = dfk.groupby(by="Rok").agg({"Liczba": "sum"}).reset_index()

print(dfm.groupby(by="Rok").agg({"Liczba": "sum"}))
print(dfk.groupby(by="Rok").agg({"Liczba": "sum"}))


plt.bar(years, dfm["Liczba"], width=0.5)
plt.bar(years, dfk["Liczba"], width=0.5)

plt.show()