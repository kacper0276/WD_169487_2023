import numpy as np
import pandas as pd
import openpyxl


def zad_1(df):
    print(df["Sprzedawca"].unique())


def zad_2(df):
    print(df.sort_values(by=['Utarg'], ascending=False).nlargest(5, columns='Utarg'))


def zad_3(df):
    print(df.groupby("Sprzedawca").agg({"Utarg": "sum"}))


def zad_4(df):
    print(df.groupby("Kraj").agg({"Utarg": "sum"}))


def zad_5(df):
    print(df[(df["Kraj"] == "Polska") & (df["Data zamowienia"].str.contains("2005"))].agg({"Utarg": "sum"}))


def zad_6(df):
    print(df[df["Data zamowienia"].str.contains("2004")].mean()) # df["Fee"].mean() - liczy średnią


def zad_7(df):
    order_2005 = df[df["Data zamowienia"].str.contains("2005")]
    order_2004 = df[df["Data zamowienia"].str.contains("2004")]
    order_2004.to_csv('zamówienia_2004.csv', header=None, index=False)
    order_2005.to_csv('zamówienia_2005.csv', header=None, index=False)



dfmain = pd.read_csv('data/zamowienia.csv', sep=";")

print(dfmain)

# Podpunkt a
# zad_1(dfmain)

# Podpunkt b
# zad_2(dfmain)

# Podpunkt c
# zad_3(dfmain)

# Podpunkt d
# zad_4(dfmain)

# Podpunkt e
# zad_5(dfmain)

# Podpunkt f
# zad_6(dfmain)

# Podpunkt g
zad_7(dfmain)