cos = []

while True:
    a = input("Podaj liczbe ")

    if a == "end":
        break

    if a.isdigit():
        cos.append(a)
        print(cos)

print(cos)