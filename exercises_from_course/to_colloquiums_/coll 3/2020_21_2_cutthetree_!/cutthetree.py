"""
Dane jest drzewo BST zbudowane z węzłów
class BNode:
def __init__( self, value ):
self.left = None
self.right = None
self.parent = None
self.value = value
Klucze w tym drzewie znajdują się w polach value i są liczbami całkowitymi. Mogą zatem mieć
wartości zarówno dodatnie, jak i ujemne. Proszę napisać funkcję, która zwraca wartość będącą
minimalną możliwą sumą kluczy zbioru wierzchołków oddzielających wszystkie liście od korzenia
w taki sposób, że na każdej ścieżce od korzenia do liścia znajduje się dokładnie jeden wierzchołek z
tego zbioru. Zakładamy że korzeń danego drzewa nie jest bezpośrednio połączony z żadnym liściem
(ścieżka od korzenia do każdego liścia prowadzi przez co najmniej jeden dodatkowy węzeł). Jako
liść jest rozumiany węzeł W typu BNode such that W.left = W.right = None.
Rozwiązanie należy zaimplementować w postaci funkcji:
def cutthetree(T):
...
która przyjmuje korzeń danego drzewa BST i zwraca wartość rozwiązania. Nie wolno zmieniać
definicji class BNode.
"""

from tests import runtests

# Dla drzewa BST, utworzonego przez dodawanie do pustego drzewa kolejno elementów
# z kluczami 10, 3, 15, 11, 17, -1, -5, 0 wynikiem jest 14 (usuwamy węzły o wartośćiach -1 oraz 15).

