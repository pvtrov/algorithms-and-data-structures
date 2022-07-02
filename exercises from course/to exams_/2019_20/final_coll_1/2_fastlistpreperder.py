"""
W szybkiej liscie odsyłaczowej i-ty element posiada referencje (odsyłacze) do elementów: i+2^0, i+2^1, i + 2^2, . . .
(lista odsyłaczy z i-tego elementu kończy się na ostatnim elemencie o numerze postaci i + 2^k, który występuje w liście).
Lista ta przechowuje liczby całkowite w kolejności niemalejącej.

Napisz funkcję fast list prepend:
def fast_list_prepend(L, a):
...

która przyjmuje referencję na pierwszy węzeł szybkiej listy (L) oraz liczbę całkowitą (a) mniejszą
od wszystkich liczb w przekazanej liście i wstawia tę liczbę na początek szybkiej listy (jako nowy
węzeł). W wyniku dodania nowego elementu powinna powstać prawidłowa szybka lista. W szczególności każdy węzeł powinien mieć poprawne odsyłacze do innych węzłów. Funkcja powinna zwrócić
referencję na nowy pierwszy węzeł szybkiej listy.
Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj
złożoność obliczeniową. Węzły szybkiej listy reprezentowane są w postaci:

"""


class FastListNode:
    def __init__(self, a):
        self.a = a # przechowywana liczba całkowita
        self.next = [] # lista odsyłaczy do innych elementów; początkowo pusta

    def __str__(self): # zwraca zawartość węzła w postaci napisu
        res = "a: " + str(self.a) + "\t" + "next keys: "
        res += str([n.a for n in self.next])
        return res


def fast_list_prepend(L, a):
    new_element = FastListNode(a)

    almost_head = L
    counter = 1
    power_counter = 0
    while almost_head is not None:
        if counter == 2**power_counter:
            new_element.next.append(almost_head)
            power_counter += 1
        almost_head = almost_head.next[0]
        counter += 1

    return new_element.__str__()


A = FastListNode(3)
B = FastListNode(4)
C = FastListNode(9)
D = FastListNode(12)
E = FastListNode(21)
F = FastListNode(103)
G = FastListNode(107)
H = FastListNode(119)
A.next = [B, C, E]
B.next = [C, D, F]
C.next = [D, E, G]
D.next = [E, F, H]
E.next = [F, G]
F.next = [G, H]
G.next = [H]
H.next = [None]

print(fast_list_prepend(A, 2))