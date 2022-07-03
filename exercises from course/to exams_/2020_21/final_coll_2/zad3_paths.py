from zad3testy import runtests
"""
Dany jest nieskierowany graf G = (V, E) oraz dwa wierzchołki, s i t. Proszę zaimplementować
funkcję:
def paths( G,s,t ):
...
która zwraca liczbę krawędzi e takich, że e występuje na pewnej najkrótszej ścieżce z s do t. Graf
dany jest jako lista list sąsiedztwa w postaci [(v 0 , w 0 ), (v 1 , w 1 ), ...], gdzie: v i to numer wierzchołka,
w i to waga krawędzi prowadzącej do wierzchołka v i . Wagi krawędzi są dodatnie.
Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
użytego algorytmu.

Przykład.
Dla listy sąsiedztwa postaci:
G = [ [(1,2),(2,4)],
[(0,2),(3,11),(4,3)],
[(0,4),(3,13)],
[(1,11),(2,13),(5,17),(6,1)],
[(1,3),(5,5)],
[(3,17),(4,5),(7,7)],
[(3,1),(7,3)],
[(5,7),(6,3)] ],
s = 0, t = 7
# sąsiedzi i wagi wierzchołka nr 0
# sąsiedzi i wagi wierzchołka nr 1
# itd.
funkcja powinna zwrócić wartość 7. Krawędzie 0-1, 1-4, 4-5, 5-7, 1-3, 3-6, 6-7.
"""

def paths(G,s,t):
    """tu prosze wpisac wlasna implementacje"""
    return None

    
runtests( paths )


