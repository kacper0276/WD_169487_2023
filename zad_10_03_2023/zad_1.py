def badanieMonotonicznosci(a):
    if a > 0:
        return "Rosnąca"
    elif a == 0:
        return "Stala"
    else:
        return "Malejaca"

a = eval(input("Podaj parametr a: "))
print(badanieMonotonicznosci(a))