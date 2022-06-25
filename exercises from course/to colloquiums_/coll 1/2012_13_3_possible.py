"""
Proszę napisać funkcję bool possible( char* u, char* v, char* w ), która zwraca prawdę
jeśli z liter słów u i v da się ułożyć słowo w (nie jest konieczne wykorzystanie wszystkich liter)
oraz fałsz w przeciwnym wypadku. Można założyć, że w i v składają się wyłącznie z małych liter
alfabetu łacińskiego. Proszę krótko uzasadnić wybór zaimplementowanego algorytmu.
"""


def possible(first, second, wanted):
    letters_array = [0] * 25

    for letter in first:
        letters_array[97 - ord(letter)] += 1

    for letter in second:
        letters_array[97 - ord(letter)] += 1

    for letter in wanted:
        letters_array[97 - ord(letter)] -= 1
        if letters_array[97 - ord(letter)] < 0:
            return False

    return True


first = "agusia"
second = "martynka"
wanted1 = "marcelka"
wanted2 = "marusia"
print(possible(first, second, wanted1))
print(possible(first, second, wanted2))
