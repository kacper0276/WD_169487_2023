import math

def dodaj_znak(string):
    ile_wyrazow:int = len(string)

    for i in range(ile_wyrazow):
        string[i] = string[i]+"!"
    return string


def dodaj_znak_v2(string):
    new_list = []
    ile_wyrazow:int = len(string)

    for i in range(ile_wyrazow):
        new_list.append(string[i]+"!")
    return new_list


string = ["Wyraz pierwszy", "Wyraz drugi", "A tu dlugie zdanie jakies"]
print(dodaj_znak(string))
print(dodaj_znak_v2(string))
print(string)