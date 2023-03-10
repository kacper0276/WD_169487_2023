import random

random.seed()


def guess_the_number():
    all_points_counter = 0
    for i in range(5):
        random_number = random.randint(1, 10)
        number = eval(input("Podaj liczbe: "))
        if number == random_number:
            all_points_counter = all_points_counter + 10
            print( f"Wylosowana liczba to {random_number} Gratulacje dostajesz 10 punktow")
        else:
            all_points_counter = all_points_counter - 1
            print(f"Niestety wylosowana liczba to: {random_number}, tracisz 1 punkt")
    return f"Gratulacje twoja ilosc punktow to {all_points_counter}"


print(guess_the_number())

