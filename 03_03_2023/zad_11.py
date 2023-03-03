import math

a = eval(input("Podaj wysokość diamentu "))

if a < 3 or a > 9:
    print("Niepoprawne wysokości ")

else:

    if a % 2 == 0:
        a = a-1
        pom = math.ceil(a / 2)
        for i in range(1, pom):
            if i == 1:
                print(" " * (pom - i) + "o" * i + " " * (pom - i))
            elif i < pom:
                print(" " * (pom - i) + "o" * pom + " " * (pom - i))
        for j in range(pom, a + 1):
            if j == pom:
                print("o" * a)
            elif j < a:
                print(" " * (j - pom) + "o" * (pom) + " " * (j - pom))
            elif j == a:
                print(" " * (a - pom) + "o" + " " * (a - pom))

    else:
        pom = math.ceil(a/2)
        for i in range(1, pom):
            if i == 1:
                print(" " * (pom - i) + "o" * i + " " * (pom - i))
            elif i < pom:
                print(" " * (pom - i) + "o" * pom + " " * (pom - i))
        for j in range(pom, a + 1):
            if j == pom:
                print("o"*a)
            elif j < a:
                print(" " * (j - pom) + "o" * (pom) + " " * (j - pom))
            elif j == a:
                print(" " * (a - pom) + "o" + " "*(a - pom) )