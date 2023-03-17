import numpy as np


def funkcja(n):
    main_result = np.diag([2]*n)
    heleper = 2
    for x in range(n):
        for y in range(n):
            if (not main_result[x][y] == 2) and main_result[x][y] < 2*n :
                main_result[x][y] = main_result[x][y-1] + 2
            elif (not main_result[x][y] == 2) and main_result[x][y] == 2*n :
                main_result[x][y] = main_result[x][y - 1] - 2
    print(main_result)


number = eval(input("Podaj wartość: "))
funkcja(number)