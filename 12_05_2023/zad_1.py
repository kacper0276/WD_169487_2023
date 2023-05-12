import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl

df = pd.read_excel("./data/imiona.xlsx")
counter = 0
result = []

for x in range(len(df["Imie"])):
    if df["Imie"][x][0] == 'K':
        result.append(df["Imie"][x])

result = np.unique(result)
print(len(result))

# Inna metoda
df_od_k = df[df["Imie"].str[0] == 'K']
df_unique = df_od_k["Imie"].unique()
print(len(df_unique))
