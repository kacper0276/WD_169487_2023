def liczenieSumyCiagu(a1=1, r=1, ile=10):
    suma = a1
    for i in range(ile - 1):
        suma += r
    return suma

a1 = eval(input("Podaj pierwsza wartosc ciagu "))
r = eval(input("Podaj wartosc r"))
ile = eval(input("Ile wyrazow chcesz zsumowac"))
print(liczenieSumyCiagu())