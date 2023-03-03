a = eval(input("Podaj wysokość wieży "))

if a > 10:
    print("Za wysoka wieża ")

else:
    for i in range(1, a+1):
        print("A"*i)