# Agnieszka Patro

# wybieram plamę o najwiekszej objętosci, i sprawdzam czy dojade do konca, jesli tak to git
# jesli nie to biore kolejna dużą plamę. Realizuje to przez Priority Queue gdzie wielkość plamy jest moim priorytetem

from zad5testy import runtests
from queue import PriorityQueue


def check_if_in_range(queue, fuel, ropes, last_ref):
    for i in range(last_ref, fuel+1):
        if ropes[i] != 0:
            queue.put((-ropes[i], i))
    return queue


def plan(T):
    result = [0]
    last_refueled = 0
    fuel = T[0]
    T[0] = 0
    queue = PriorityQueue()

    def partition(T, p, r):
        x = T[r]
        i = p - 1
        for j in range(p, r):
            if T[j] <= x:
                i += 1
                T[i], T[j] = T[j], T[i]
        T[i + 1], T[r] = T[r], T[i + 1]
        return i + 1

    def quicksort(T, p, r):
        if p < r:
            q = partition(T, p, r)
            quicksort(T, p, q - 1)
            quicksort(T, q + 1, r)
        return T

    while fuel + 1 < len(T):
        check_if_in_range(queue, fuel, T, last_refueled)
        amount, index = queue.get()
        amount = abs(amount)
        last_refueled = fuel + 1
        fuel += amount
        T[index] = 0
        result.append(index)

    return quicksort(result, 0, len(result)-1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True)