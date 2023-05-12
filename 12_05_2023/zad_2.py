import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl


df = pd.read_excel("./data/imiona.xlsx")

dfm = df[df["Plec"] == 'M']
dfk = df[df["Plec"] == 'K']

dfresm = dfm.groupby(['Imie', 'Plec'])['Liczba'].sum()
dfresk = dfk.groupby(['Imie', 'Plec'])['Liczba'].sum()
print(dfresm[dfresm == max(dfresm)])
print(dfresk[dfresk == max(dfresk)])

dfresm = dfresm.reset_index()
print(dfresm)


