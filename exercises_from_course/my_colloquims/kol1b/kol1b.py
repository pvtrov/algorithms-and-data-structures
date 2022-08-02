# Agnieszka Patro 405677
# 1. Tworzę sobie kubełki w zależnośći od ilośći liter w danym słowie      < O(n) >

# 2. W każdym kubełku sprawdzam sobie sobie dla słów czy są anagramami, czyli:

#   * biore pierwsze słowo jakie mam, zliczam sobie ilosc jego liter jak w countsorcie,
#     potem biore następne i w funkcji check_if_anagram przechodze po tym słowie odejmując liczniki liter
#     ( tak jak w count sorcie ), jeśli licznik jakiejs litery jest większy od 0 to znaczy ze słowo nie jest anagramem

#   < O( (n+28) * ilość słów) > ale ~= O(n), [ta ilość słów w przypadku gdy zaden nie jest anagramem drugiego]

# dodatkowo jeśli jakies słowo jest anagramem pierwszego sprawdzanego słowa to wtedy usuwam go z kubełka żeby nie
# sprawdzac go kilka razy < daje mu jakąś wartość np 0 >

# jestem prawie pewna że złożoność całego algorytmu to O(n)

import copy
from kol1btesty import runtests


def check_if_anagram(counted_array, checking_word):     # tutaj sprawdzam dla kazdego oddzielnego słowa
    for letter in checking_word:
        counted_array[ord(letter)-97] -= 1

    if max(counted_array) > 0:
        return False
    else:
        return True


def count_letters(array):
    max_counter = -1

    for word in range(len(array)):
        counter = 0
        if array[word] != 0:
            count_array = [0] * 28
            first_word = array[word]

            for i in range(len(first_word)):
                count_array[ord(first_word[i])-97] += 1

            for i in range(len(array)):
                if array[i] != 0:
                    checking_array = copy.copy(count_array)
                    if check_if_anagram(checking_array, array[i]) is True:
                        counter += 1
                        array[i] = 0
        if counter > max_counter:
            max_counter = counter

    return max_counter


def f(T):
    max_bucket = max(len(T[i]) for i in range(len(T)))
    buckets = [[] for _ in range(max_bucket+1)]

    for i in range(len(T)):                       # tworzę sobie te kubełki
        buckets[len(T[i])].append(T[i])

    max_popular = -1
    for bucket in buckets:                        # sprawdzam w kazdym buckecie czy te słowa są anagramami
        if len(bucket) > 1:
            popular = count_letters(bucket)
            if popular > max_popular:
                max_popular = popular

    return max_popular


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
