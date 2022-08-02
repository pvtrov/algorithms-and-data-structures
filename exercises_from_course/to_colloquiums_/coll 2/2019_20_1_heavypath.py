"""
Proszę zaimplementować funkcję heavy path(T), która na wejściu otrzymuje drzewo T z ważonymi krawędziami (wagi to liczby
całkowite—mogą być zarówno dodatnie, ujemne, jak i o wartości zero) i zwraca długość (wagę) najdłuższej ścieżki prostej
w tym drzewie. Drzewo reprezentowane jest za pomocą obiektów typu Node:

class Node:
def __init__( self ):
self.children = 0 # liczba dzieci węzła
self.child = [] # lista par (dziecko, waga krawędzi)
... # wolno dopisać własne pola

Poniższy kod tworzy drzewo z korzeniem A, który ma dwoje dzieci, węzły B i C, do których
prowadzą krawędzie o wagach 5 i −1:
A = Node()
B = Node()
C = Node()
A.children = 2
A.child = [ (B,5), (C,-1) ]

Rozwiązaniem dla drzewa A jest 5 (osiągnięte przez ścieżkę A-B; ścieżka B-A-C ma wagę
5 − 1 = 4. Proszę skrótowo wyjaśnić ideę algorytmu oraz oszacować jego złożoność czasową
"""
from math import inf


class Node:
    def __init__(self):
        self.children = 0
        self.child = []


def go_down(node, wages, sum):
    if node.children == 0:
        wages.append(sum)

    for child in node.child:
        go_down(child[0], wages, sum + child[1])


def heavy_path(T):
    wages = []
    first_val = -inf
    sec_val = -inf

    for child in T.child:
        go_down(child[0], wages, child[1])

    for i in range(len(wages)):
        if wages[i] > sec_val:
            sec_val = wages[i]
        if sec_val > first_val:
            sec_val, first_val = first_val, sec_val

    wages.append(sec_val + first_val)
    return max(wages)


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
A.children = 2
B.children = 1
C.children = 2
B.child = [(D, 3)]
C.child = [(E, 8), (F, -2)]
A.child = [ (B,5), (C,-1) ]
print(heavy_path(A))
