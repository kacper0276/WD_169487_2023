import numpy as np


def funkcja(tablica, kierunek = "poziom"):
    size = tablica.shape
    pion_wielkosc = size[1]
    poziom_wielkosc = size[0]
    print(poziom_wielkosc)
    if kierunek == "poziom":
        if poziom_wielkosc % 2 == 0:
            return np.vsplit(tablica, poziom_wielkosc/2)
        else:
            return "Dlugosc nie pozwala na ciecie"
    elif kierunek == "pion":
        if pion_wielkosc % 2 == 0:
            return np.hsplit(tablica, pion_wielkosc/2)
        else:
            return "Dlugosc nie pozwala na ciecie"
    else:
        return "Nie poprawny typ "


array = np.arange(20).reshape(4, 5)
print(array)
direction = input("Podaj kierunek: poziom lub pion: ")

print(funkcja(array, direction))
