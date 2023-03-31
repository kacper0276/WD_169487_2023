import numpy as np
import pandas as pd
import openpyxl


def zad_1(df):
    print("Punkt a:")
    print(df[df['Liczba'] > 1000])


def zad_2(df):
    print("Punkt b: ")
    print(df[df['Imie'] == 'KACPER'])


def zad_3(df):
    print("Punkt c: ")
    suma = df.sum()
    print(suma["Liczba"])


def zad_4(df):
    print("Punkt d: ")
    print(df.groupby(['Rok']).agg({'Liczba': ['sum']}))


def zad_5(df):
    print("Punkt e: ")
    print(df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)].agg({'Liczba': ['sum']}))


def zad_6(df):
    print("Punkt f: ")
    print(f"Urodzeni chłopcy {df[df['Plec'] == 'M'].agg({'Liczba': ['sum']})}")
    print(f"Urodzone dziewczynki {df[df['Plec'] == 'K'].agg({'Liczba': ['sum']})}")


def zad_7(df):
    print("Podpunkt f: ")
    m = df[df.Plec == "M"]
    k = df[df.Plec == "K"]

    m1 = m.groupby(df.Imie).sum()
    k1 = k.groupby(df.Imie).sum()
    print(m1["Liczba"].idxmax())
    print(k1["Liczba"].idxmax())


def zad_8(df):
    result = df.groupby(['Imie', 'Rok', 'Liczba'], as_index=False)['Liczba'].max()
    print(result)


dfmain = pd.read_excel('data/imiona.xlsx')

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
# zad_7(dfmain)

# Podpunkt h
zad_8(dfmain)