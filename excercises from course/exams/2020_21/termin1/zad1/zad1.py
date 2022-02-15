from zad1testy import runtests

"""
W tym zadaniu nie wolno korzystać z wbudowanych funkcji sortowania!
Mówimy, że tablica T ma współczynnik nieuporządkowania równy k (jest k-Chaotyczna), jeśli spełnione są łącznie dwa warunki:
1. tablicę można posortować niemalejąco przenosząc każdy element A[i] o co najwyżej k pozycji
(po posortowaniu znajduje się on na pozycji różniącej się od i co najwyżej o k),
2. tablicy nie da się posortować niemalejąco przenosząc każdy element o mniej niż k pozycji.
Proszę zaproponować i zaimplementować algorytm, który otrzymuje na wejściu tablicę liczb rzeczywistych T i zwraca jej współczynnik nieuporządkowania. Algorytm powinien być jak najszybszy
oraz używać jak najmniej pamięci. Proszę uzasadnić jego poprawność i oszacować złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję:
def chaos_index( T ):
...
przyjmującą tablicę T i zwracającą liczbę całkowitą będącą wyznaczonym współczynnikiem nieuporządkowania.
"""
"""
iteruje po tablicy i sprawdzam ktory element nie pasuje, jesli jakis nie jest w odpowiednim miejscu to go przesuwam
 licząc k
 O(n*k)
"""


def move(array, i, k):
    array[i], array[i-1] = array[i-1], array[i]
    k += 1
    if i > 2:
        if array[i-1] < array[i-2]:
            return move(array, i-1, k)

    i += 1
    if i < len(array)-1:
        if array[i] < array[i-1]:
            return move(array, i, k)
        else:
            return k, array

    elif i == len(array)-1 and array[i] < array[i-1]:
        array[i], array[i-1] = array[i-1], array[i]
        k += 1
        return k, array

    else:
        return k, array


def chaos_index( T ):
    max_k = 0

    for i in range(1, len(T)):
        if T[i] < T[i-1]:
            k, T = move(T, i, 0)
            if max_k < k:
                max_k = k

    return max_k




runtests( chaos_index )
