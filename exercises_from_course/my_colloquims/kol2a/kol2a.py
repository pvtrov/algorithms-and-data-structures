"""
Agnieszka Patro

1. przechodzę po tablicy P i zapisuje sobie index poczatkowy na ktorym byla dana stacja     -> O(n)
2. sortuje sobie tą tablice po numerze punktu przyjmuje      ->  O(nlogn)
3. tworzę sobie tablice przystanków w której każdy element to:
    [nr. przystanku, ilosc punktów kontrolnych od ostatniego przysanku, index początkowy]  -> O(n)
5. rozwiązaniem jest "funkcja" (robie to sobie w tablicy ale chce ładnie w opisie zapisać):
        ( nie wiem czy to zaimmplementuje ale wydaje mi sie że coś takiego jest rozwiązniem zadania)
        find_stops = najmniejsza ilość kontrolerów które mija Marian dojeżdżając do danego punktu P

        find_stops[p] = [[min. ilość; index ostatniej zmiany; poostała ilość przystanków do zmiany od ostatniej zmiany; kto prowadził do stacji P]]

        niech f = find_stops1

        cofam sie o trzy (bo max moga na jednej zmianie przejechac 3 stacje) i sobie sprawdzam kazdy przypadek,
        ile przejedzie najmmniej przejedzie marian tych przystanków i dodaje to do mojej tablicy find_stops.
        potem z ostatnich elementów tablicy find_stops wybieram to gdzie mam minimum i wracam  po find_stops[1] by
        uzyskac stacje na których sie zmieniamy.
        jako że cofam sie tylko o 3 to wydaje mi sie że jest to złozoność O(3n) wiec -> O(n) wiec sumarycznie caly algorytm
        powinien zajmowac O(nlogn) czasu
        dodatkowo używam O(n) dodatkowej pamieci
"""
from kol2atesty import runtests


def make_me_switch_stops(P):
    P_with_index = [[0, 0, 0] for _ in range(len(P))]       # musze tu dołożyć O(n) pamięci bo nie moge dodac elementu do krotki a w tablicy P są krotki :)
    for i in range(len(P)):
        P_with_index[i] = [P[i][0], P[i][1], i]
    P_with_index.sort()
    switch_stops = []

    counter = 0
    for i in range(len(P_with_index)):
        if not P_with_index[i][1]:
            counter += 1
        elif P_with_index[i][1]:
            switch_stops.append([P_with_index[i][0], counter, P_with_index[i][2]])
            counter = 0
        else:
            print("error, there's no False or True")
            exit(1)

    return switch_stops


def drivers( P, B ):
    switch_stops = make_me_switch_stops(P)
    find_stops = [[0, 0, 0, 0] for _ in range(len(switch_stops))]
    find_stops[0] = [0, None, 2, False]  # min ilosc, ostatnia stacja, il do konca, czy marian prowadził

    for i in range(1, len(find_stops)):
        if i >= 3:
            find_stops[i] = 1
        else:
            for j in range(len(find_stops[i-1])):
                find_stops[i] = 1

    print(switch_stops)






    return []

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = False )