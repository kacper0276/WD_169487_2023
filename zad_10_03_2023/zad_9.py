import math


def printLetterA(a):
    spaces = a - 1
    spaces_between = 0
    for i in range(a):
        if i == 0:
            for j in range(spaces):
                print(" ", end="")
            print("*", end="")
            for j in range(spaces):
                print(" ", end="")
            spaces = spaces - 1
            spaces_between = spaces_between + 1
            print("")

        if i == math.floor(a / 2):
            for j in range(spaces):
                print(" ", end="")
            for j in range(a):
                print("*", end="")
            for j in range(spaces):
                print(" ", end="")
            spaces = spaces - 1
            spaces_between = a
            print("")

        elif ((i < math.floor(a / 2)) or (i > math.floor(a / 2))) and i != 0 :
            for j in range(spaces):
                print(" ", end="")
            print("*", end="")
            for j in range(spaces_between):
                print(" ", end="")
            print("*", end="")
            for j in range(spaces):
                print(" ", end="")
            spaces = spaces - 1
            spaces_between = spaces_between + 2
            print("")


x = eval(input("Podaj wysokosc litery a: "))
printLetterA(x)