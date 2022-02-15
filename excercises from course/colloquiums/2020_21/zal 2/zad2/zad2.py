# Agnieszka Patro

# trzeba zauważyć, że liczby to krawędzie i znajdujemy ścieżkę eulera
# złożność czasowa jak i pamięciowa O(N + M), gdzie M to 10^k, a N to liczba krawędzi (bo tyle mamy liczb)

from zad2testy import runtests


def get_graph(edges, M):
    '''dziala w czasie O(M + N), gdzie N to liczba krawedzi'''
    g = [[] for i in range(M)]
    for x, y in edges:
        g[x].append(y)
    return g


def get_extra_edge(edges, M):

    indeg = [0 for i in range(M)]
    outdeg = [0 for i in range(M)]

    for x, y in edges:
        indeg[y] += 1
        outdeg[x] += 1
    
    lack, extra = None, None
    for i in range(M):
        diff = outdeg[i] - indeg[i]
        if diff == 0:
            continue
        elif diff == 1:
            if extra is not None:
                return False
            extra = i
        elif diff == -1:
            if lack is not None:
                return False
            lack = i
    
    if lack is None and extra is None:
        return None
    if lack is not None and extra is not None:
        return (lack, extra)
    return False




def order(L, K):
    M = 10 ** K
    node1 = lambda x : x % M
    node2 = lambda x : x // M
    edges = [(node1(e), node2(e)) for e in L]

    extra_edge = get_extra_edge(edges, M)
    
    if extra_edge is False:
        return None
    if extra_edge is not None:
        edges.append(extra_edge)
    g = get_graph(edges, M)

    s = [edges[0][0]]
    
    res = []
    while len(s) > 0:
        u = s[-1]
        
        if len(g[u]) > 0: # jest
            w = g[u][-1]
            g[u].pop()
            s.append(w)
        else: # nie ma
            s.pop()
            res.append(u)


    res = [M * res[i] + res[i + 1] for i in range(len(res) - 1)]
    if extra_edge is None:
        return res if len(res) == len(L) else None
    
    added = extra_edge[1] * M + extra_edge[0]
    for i in range(len(res)):
        if res[i] == added:
            res = res[i+1:] + res[:i]
            break
    return res if len(res) == len(L) else None 
    

    
runtests( order )


