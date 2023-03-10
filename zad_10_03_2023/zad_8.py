import  random

random.seed()


def multipli_game():
    good_answer = 0
    bad_answer = 0

    for i in range(10):
        number_one = random.randint(1, 9)
        number_two = random.randint(1, 9)
        print(f"{number_one} * {number_two} = ?")
        user_number = eval(input("Podaj wynik tego dzialania: "))
        if number_one * number_two == user_number:
            good_answer = good_answer + 1
            print("Poprawna odpowiedz")
        else:
            bad_answer = bad_answer + 1
            print(f"Bledna odpowiedz, poprawna odpowiedz to: {number_two * number_one}")
    return f"Poprawne odpowiedzi: {good_answer}, bledne odpowiedzi: {bad_answer}"


print(multipli_game())