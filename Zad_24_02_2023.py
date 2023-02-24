a = 5

print(type(a))
# Wyświetla typ zmiennej

imie = "Tak"
nazwisko = 'Nie'
full_name = "Tak 'Nie'"
print(imie,nazwisko,sep="")


def zad_1():
    for a in range(0, 4):
        print("********************")
    print("\n")


def zad_2():
    for a in range(0, 3):
        if(a % 2 == 0):
            print("********************")
        else:
            print("*                  *")
            print("*                  *")

    print("\n")


def zad_3():
    for a in range(1, 5):
        print("*"*a)
    print("\n")


def zad_4():
    a = (512 - 282)
    b = (47*48+5)
    c = a / b
    print(c, "\n")


def zad_5(x):
    print(x*1, x*2, x*3, x*4, x*5, sep="---")
    print("\n")


def zad_6():
    x = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym "\
        "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki."\
        "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym."\
        "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum," \
        "a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"


def zad_7():
    a = input("Podaj pierwszą wartość ")
    b = input("Podaj drugą wartość ")
    print("Wynik to {}".format(int(a)*int(b)))
    print("\n")


def zad_8():
    a = input("Podaj wartość w kilogramach ")
    print("Twoja wartość w funtach to: {}".format( int(a)*2.2 ))


zad_1()

zad_2()

zad_3()

zad_4()

x = 7
zad_5(x)

zad_6()

zad_7()

zad_8()
