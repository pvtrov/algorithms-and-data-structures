from zad2testy import runtests
"""
Na osi liczbowej znajduje się N punktów większych od M = 10^K . Z punktu A można przeskoczyć
na punkt B wtedy i tylko wtedy gdy A%10^K == B//10^K . Proszę zaimplementować funkcję:
def order( L,K ):
...
porządkującą punkty, tak aby możliwe było przejście od najwcześniejszego punktu w tym porządku,
kolejno przez wszystkie punkty, do ostatniego. Funkcja otrzymuje listę wartości określającą położe-
nie punktów na osi liczbowej i powinna zwrócić listę punktów w kolejności ich odwiedzania. Jeżeli
uporządkowanie punktów nie jest możliwe, funkcja powinna zwrócić N one.
Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
użytego algorytmu.

Przykład.
Dla danych:
L = [56,15,31,43,54,35,12,23], K = 1
przykładowym, prawidłowym wynikiem jest lista:
L = [12,23,31,15,54,43,35,56]
"""
"""
zauwazmy ze liczby to krawedzie, i pykamy cykl eulera, za chuj nie wiem czemu nie przechodzi dwoch ostatnich testow
"""


def make_extra_edge(out_, in_):
    extra, lack = None, None

    for i in range(len(out_)):
        diff = out_[i] - in_[i]
        if diff == 0:
            continue
        elif diff == -1:
            if extra is None:
                extra = i
        elif diff == 1:
            if lack is None:
                lack = i

    if extra is None and lack is None:
        return None
    if extra is not None and lack is not None:
        return (extra, lack)
    return False


def add_vertex(graph, x, y):
    graph[x].append(y)


def make_graph(numbers, K):
    M = 10**K
    edges = []
    out_ = [0] * M
    in_ = [0] * M
    for i in range(len(numbers)):
        x = numbers[i]%M
        y = numbers[i]//M
        edges.append((x, y))
        out_[x] += 1
        in_[y] += 1

    extra_edge = make_extra_edge(out_, in_)

    if extra_edge is not None:
        edges.append(extra_edge)

    graph = [[] for _ in range(M)]
    for edge in edges:
        add_vertex(graph, edge[0], edge[1])

    return graph, edges, extra_edge


def order(L, K):
    graph, edges, extra_edge = make_graph(L, K)
    res = []
    s = [edges[0][0]]
    while len(s) > 0:
        u = s[-1]

        if len(graph[u]) > 0:
            # edge exists
            w = graph[u][-1]
            graph[u].pop()
            s.append(w)
        else:
            # doesnt exist
            s.pop()
            res.append(u)

    result = []
    for i in range(len(res)-1):
        one = str(res[i])
        sec = str(res[i+1])
        res_ = one + sec
        res_ = int(res_)
        result.append(res_)

    added = extra_edge[1] * 10**K + extra_edge[0]
    for i in range(len(result)):
        if result[i] == added:
            result = result[i+1:] + result[:i]
            break

    if len(result) == len(L):
        return result
    else:
        return None

    
runtests( order )

# K = 1
# L = [56, 15, 31, 43, 54, 35, 12, 23]
# print(order(L, K))

