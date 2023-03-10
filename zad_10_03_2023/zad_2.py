def prostopadlaCzyRownolegla(a1, a2):
    if a1 == a2:
        return "Rownolegla"
    elif a1*a2 == -1:
        return "Prostopadla"

a1 = eval(input("Podaj parametr a1: "))
a2 = eval(input("Podaj parametr a2: "))
print(prostopadlaCzyRownolegla(a1, a2))