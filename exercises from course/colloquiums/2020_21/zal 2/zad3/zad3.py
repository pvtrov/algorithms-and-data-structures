# Agnieszka Patro

# algorytm dijkstry z mądrym wykorzystaniem poprzednikow.
# pozniej wyluskujemy wynik DFS'em

# Złozonosc pamieciowa: O(E + VlogE)
# Zlozonosc czasowa: O(ElogV)

import queue
from zad3testy import runtests


def DFS(P, t, V):
    if V[t] == True:
        return 0
    res = len(P[t])
    V[t] = True

    for e in P[t]:
        res += DFS(P, e, V)
    return res


def paths(G,s,t):
    """tu prosze wpisac wlasna implementacje"""

    D = [] # dystanse
    P = [] # skad
    V = [] # odwiedzone (wykorzystywane pozniej)
    for i in range(len(G)):
        D.append(1000000000 if i != s else 0)
        P.append([])
        V.append(False)

    kolejka = queue.PriorityQueue()
    kolejka.put_nowait((0, s))

    while kolejka.empty() is False:
        d, wierzcholek = kolejka.get_nowait()

        for i in range(len(G[wierzcholek])):
            sasiad, waga = G[wierzcholek][i]

            lhs, rhs = D[wierzcholek] + waga, D[sasiad]

            if lhs < rhs:
                kolejka.put_nowait((-lhs, sasiad))
                P[sasiad] = []
                D[sasiad] = lhs
                P[sasiad].append(wierzcholek)

            elif rhs == lhs:
                P[sasiad].append(wierzcholek)

    
    return DFS(P, t, V)

    
runtests( paths )


