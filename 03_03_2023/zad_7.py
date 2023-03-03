x = input("Podaj liczby ")
y = []
for i in x.split(" "):
    y.append(int(i))

for i in y:
    print(pow(i,2))