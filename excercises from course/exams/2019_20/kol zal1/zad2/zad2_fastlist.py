from zad2testy import runtests
import copy
"""
W szybkiej liscie odsyłaczowej i-ty element posiada referencje (odsyłacze) do elementów: i+2^0, i+2^1,i + 2^2, . . . 
(lista odsyłaczy z i-tego elementu kończy się na ostatnim elemencie o numerze postaci i + 2^k, 
który występuje w liście). Lista ta przechowuje liczby całkowite w kolejności niemalejącej.
Przykładową szybką listę przedstawia poniższy rysunek:
Napisz funkcję fast list prepend:
def fast_list_prepend(L, a):
...
która przyjmuje referencję na pierwszy węzeł szybkiej listy (L) oraz liczbę całkowitą (a) mniejszą
od wszystkich liczb w przekazanej liście i wstawia tę liczbę na początek szybkiej listy (jako nowy
węzeł). W wyniku dodania nowego elementu powinna powstać prawidłowa szybka lista. W szczególności każdy węzeł powinien 
mieć poprawne odsyłacze do innych węzłów. Funkcja powinna zwrócić
referencję na nowy pierwszy węzeł szybkiej listy"""


class FastListNode:
    def __init__(self, a):
        self.a = a  # przechowywana liczba calkowita
        self.next = []  # lista odnosnikow do innych elementow; poczatkowo pusta

    def __str__(self):  # zwraca zawartosc wezla w postaci napisu
        res = 'a: ' + str(self.a) + '\t' + 'next keys: '
        res += str([n.a for n in self.next])
        return res


def fast_list_prepend(L, a):
    new_element = FastListNode(a)

    new_element.next.append(L)
    result = new_element
    S = new_element
    index = 0
    k = 1

    while S != None:
         if index == 2**k:
             result.next.append(S)
             S = S.next[0]
             index += 1
             k += 1
         else:
            S = S.next[0]
            index += 1


    return result


runtests( fast_list_prepend ) 
