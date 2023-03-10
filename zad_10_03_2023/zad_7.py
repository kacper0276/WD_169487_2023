import math


def digitalRoot(a):
    suma = 0
    while a > 0:
        suma = suma + math.floor(a % 10)
        a /= 10
    return math.floor(suma)


number = eval(input("Podaj liczbe: "))
print(f"digital root liczby {number} to {digitalRoot(number)}")
