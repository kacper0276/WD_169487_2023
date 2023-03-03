a = eval(input("Podaj liczbę a "))
b = eval(input("Podaj liczbę b "))
c = eval(input("Podaj liczbę c "))

if a in range(1, 11) and (a > b or b > c):
    print("Warunki spełnione ")
else:
    print("Warunki niespełnione")