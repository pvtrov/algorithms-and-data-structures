"""
W ramach obchodów międzynarodowego święta cyklistów organizatorzy przewidzieli górską
wycieczkę rowerową. Będzie się ona odbywać po bardzo wąskiej ścieżce, na której rowery mogą
jechać tylko jeden za drugim. W ramach zapewnienia bezpieczeństwa każdy rowerzysta będzie
miał numer identyfikacyjny oraz małe urządzenie, przez które będzie mógł przekazać
identyfikator rowerzysty przed nim (lub -1 jeśli nie widzi przed sobą nikogo). Należy napisać
funkcję, która na wejściu otrzymuje informacje wysłane przez rowerzystów i oblicza rozmiar
najmniejszej grupy (organizatorzy obawiają się, że na małe grupy mogłyby napadać dzikie
zwierzęta). Dane są następujące struktury danych:
struct Cyclist {
int id, n id; // identyfikator rowerzysty oraz tego, którego widzi
};
Funkcja powinna mieć prototyp int smallestGroup( Cyclist cyclist[], int n ), gdzie
cyclist to tablica n rowerzystów. Funkcja powinna być możliwie jak najszybsza. Można założyć,
że identyfikatory rowerzystów to liczby z zakresu 0 do 108
(osiem cyfr napisanych w dwóch
rzędach na koszulce rowerzysty) i że pamięć nie jest ograniczona. Rowerzystów jest jednak dużo
mniej niż identyfikatorów (nie bez powodu boją się dzikich zwierząt). Należy zaimplementować
wszystkie potrzebne struktury danych.
"""
from math import inf

""" 
tworzymy sobie słownik, gdzie kluczem jest ID rowerzysty a wartością następna osoba. O(n)
robimy tablice proceed, ktora okresla nam czy juz policzylismy danego rowerzyste O(n)
przechodzimy po tablicy rowerzystów jeszcze raz, i liczymy grupy az dojdziemy do -1, odznaczajac proceed O(n)

O(n)
"""


class Cyclist():
    def __init__(self, id, n):
        self.id = id
        self.n = n


def count(cyc_dictionary, key, counted, counter):
    counted[key] = True
    counter += 1

    if cyc_dictionary[key] == -1:
        return counter

    return count(cyc_dictionary, cyc_dictionary[key], counted, counter)


def smallest_group(cyclist):
    cyc_dictionary = {}
    min_val = inf
    counted = [False] * 109
    for i in range(len(cyclist)):
        cyc_dictionary[cyclist[i].id] = cyclist[i].n

    for i in range(len(cyclist)):
        if not counted[cyclist[i].id]:
            counter = count(cyc_dictionary, cyclist[i].id, counted, 0)
            if counter < min_val:
                min_val = counter

    return min_val


cyclists = [Cyclist(8, 108), Cyclist(7, 6), Cyclist(3, 2), Cyclist(5, 10), Cyclist(55, 82), Cyclist(108, 9), Cyclist(6, 5),
            Cyclist(2, 97), Cyclist(10, 11), Cyclist(82, 30), Cyclist(9, 1), Cyclist(5, 66), Cyclist(97, 107), Cyclist(11, 75),
            Cyclist(30, -1), Cyclist(1, 99), Cyclist(66, 100), Cyclist(107, -1), Cyclist(75, -1), Cyclist(99, 22), Cyclist(100, -1),
            Cyclist(22, -1)]
print(smallest_group(cyclists))