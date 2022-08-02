"""
Aga Patro, 405677;
Kompletnie nie wiem czy uda mi sie to zaimplementować ale:

wybieram podejście zachłanne:
tworzę PriorityQueue w której zapisuje:
(aktualna wartość w obszarze n, [index początkowy, ilość straty sniegu od zachodu, ilość straty od wschodu]
wybieram dojazd od tej strony od której mniej sniegu stracę, następnie aktualizuje dane w PQ
wydaje mi sie ze to powinno byc jakies O(nlogn)
.
.
.
od wschodu -> od 0
od zachodu -> od len(s)-1
"""

from queue import PriorityQueue
from egz1atesty import runtests


def update_queue_from_east(S, index, priority, days):
    for i in range(len(S)):
        if S[i] != 0:
            S[i] -= 1

    for i in range(len(S) - days):
        val, infos = priority.get()
        if infos[0] < index:
            continue
        else:
            val = S[infos[0]]
            infos = [infos[0], sum_from_east(S, infos[0]), sum_from_west(S, infos[0])]
            priority.put((-val, infos))


def update_queue_from_west(S, index, priority, days):
    for i in range(len(S)):
        if S[i] != 0:
            S[i] -= 1

    for i in range(len(S) - days):
        val, infos = priority.get()
        if infos[0] > index:
            continue
        else:
            val = S[infos[0]]
            infos = [infos[0], sum_from_east(S, infos[0]), sum_from_west(S, infos[0])]
            priority.put((-val, infos))


def sum_from_west(S, index):
    if index == len(S)-1:
        return 0

    sums = [0] * len(S)
    sums[-1] = S[-1]
    for i in range(len(S)-2, -1, -1):
        sums[i] = S[i] + sums[i+1]
    return sums[index+1]


def sum_from_east(S, index):
    if index == 0:
        return 0
    sums = [0] * len(S)
    sums[0] = S[0]
    for i in range(1, len(S)):
        sums[i] = S[i] + sums[i-1]
    return sums[index-1]


def do_zeroes(S, index, side):
    if side == "E":
        for i in range(index):
            S[i] = 0
    else:
        for i in range(index+1, len(S)):
            S[i] = 0


def snow_( S ):
    priority_snow = PriorityQueue()
    for i in range(len(S)):
        priority_snow.put((-S[i], [i, sum_from_east(S, i), sum_from_west(S, i)]))

    max_snow_sum = 0
    counter = 0

    while not priority_snow.empty():
        value, infos = priority_snow.get()
        if value == 0:
            break
        max_snow_sum += abs(value)
        S[infos[0]] = 0
        counter += 1
        if infos[1] < infos[2]:   # od wschodu stracę mniej
            do_zeroes(S, infos[0], "E")
            update_queue_from_east(S, infos[0], priority_snow, counter)
        else:
            do_zeroes(S, infos[0], "W")
            update_queue_from_west(S, infos[0], priority_snow, counter)

    return max_snow_sum


def snow(S):
    S.sort()
    S.reverse()

    max_ = 0
    day = 0
    for i in range(len(S)):
        S[i] -= day
        if S[i] <= 0:
            break
        max_ += S[i]
        day += 1

    return max_


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
#