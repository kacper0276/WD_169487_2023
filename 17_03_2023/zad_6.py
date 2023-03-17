import numpy as np


def funkcja(slowo1, slowo2, slowo3):
    len_slowo1 = len(slowo1)
    len_slowo2 = len(slowo2)
    len_slowo3 = len(slowo3)
    iterator_word_2 = 0
    iterator_word_3 = 0
    end_word2 = False
    end_word3 = False

    reverse_word = slowo3[::-1]
    max_width = 0
    if len_slowo3 > len_slowo2:
        max_width = len_slowo3
    else:
        max_width = len_slowo2
    # Zakładam -> 1 słowo pionowo, 2 słowo w poziomo, 3 słowo odwrócone
    main_result = np.empty((len_slowo1, max_width), dtype='str')
    main_result.fill("")
    for x in range(len_slowo1):
        if slowo1[x] == slowo2[iterator_word_2] and (not end_word2):
            main_result[x][0] = slowo1[x]
            for y in range(1, len_slowo2):
                main_result[x][y] = slowo2[y]
            iterator_word_2 = iterator_word_2 - 1
            end_word2 = True
        if slowo1[x] == reverse_word[iterator_word_3] and (not end_word3):
            main_result[x][0] = slowo1[x]
            for y in range(1, len_slowo3):
                main_result[x][y] = reverse_word[y]
            iterator_word_3 = iterator_word_3 - 1
            end_word3 = True
        else:
            main_result[x][0] = slowo1[x]

    print(main_result)


word1 = input("Podaj pierwsze slowo: ")
word2 = input("Podaj drugie slowo: ")
word3 = input("Podaj trzecie slowo: ")

funkcja(word1, word2, word3)