def liczeniePrzeciwprostokatnej(a=3, b=4):
    c = a**2 + b**2
    return math.sqrt(c)

a = eval(input("Podaj parametr a: "))
b = eval(input("Podaj parametr b: "))
print(liczeniePrzeciwprostokatnej(a, b))
print(liczeniePrzeciwprostokatnej())