"""
Mamy dany pewien rozkład pociągów, dany jako tablica n krotek (arrival_time, departure_time), przy czym są one
posortowane niemalejąco według arrival_time. Chcemy wiedzieć, czy nasza stacja mająca m peronów jest w stanie
bezkonfliktowo obsłużyć te pociągi, tzn. w żadnym momencie nie będzie “rywalizacji” pociągów o dostępne perony.
Przedstaw algorytm, który poda odpowiedź True lub False na powyższe pytanie.
"""
from queue import PriorityQueue

"""
wstawiam pierwsze m z nich do PQ, 
sortujemy je po departure_time,  jesli sie miesci to usuwamy poprzednik z PQ, nowy tam wrzucamy,
i tak az dojdziemy do konca tablicy pociagóœ
"""


def trains(train_list, perons_number):
    pq = PriorityQueue()
    if perons_number >= len(train_list):
        return True

    for i in range(perons_number):
        pq.put((train_list[i][1], train_list[i]))

    for j in range(perons_number, len(train_list)):
        depart_time, train = pq.get()
        abs(depart_time)
        if train_list[j][0] > depart_time:
            pq.put((train_list[j][1], train_list[j]))
        else:
            return False
    return True


trains_ = [[0, 2], [0, 3], [1, 5],  [1, 6], [5, 9], [7, 8], [9, 10]]
print(trains(trains_, 4))