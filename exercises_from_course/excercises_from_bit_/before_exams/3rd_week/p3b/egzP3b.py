from egzP3btesty import runtests 
from queue import PriorityQueue


def delete_edges(G, u, v, w):
    G[u].remove((v, w))
    G[v].remove((u, w))


def lufthansa ( G ):
    all_flies = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            all_flies += G[i][j][1]
    all_flies //= 2

    pq = PriorityQueue()
    chosen_vertex = [False] * len(G)
    taken = 1
    chosen_vertex[0] = True
    sum_ = 0

    for neib in G[0]:
        pq.put((-neib[1], (neib[0], 0)))

    while taken < len(G) and not pq.empty():
        wage, (vertex, last) = pq.get()
        if not chosen_vertex[vertex]:
            chosen_vertex[vertex] = True
            taken += 1
            sum_ += abs(wage)
            delete_edges(G, vertex, last, abs(wage))

            for neib in G[vertex]:
                pq.put((-neib[1], (neib[0], vertex)))

    last_wage = -1
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j][1] > last_wage:
                last_wage = G[i][j][1]

    sum_ += last_wage

    return all_flies-sum_


runtests ( lufthansa, all_tests=True )

# G = [
#     [(1, 15), (2, 5),  (3, 10)],
#     [(0, 15), (2, 8),  (4, 5),  (5, 12)],
#     [(0, 5),  (1, 8),  (3, 5),  (4, 6)],
#     [(0, 10), (2, 5),  (4, 2),  (5, 11)],
#     [(1, 5),  (2, 6),  (3, 2),  (5, 2)],
#     [(1, 12), (4, 2),  (3, 11)]]
# G = [
#     [(3, 12), (2, 8)],
#     [(3, 4), (6, 5)],
#     [(4, 9), (0, 8)],
#     [(0, 12), (1, 4)],
#     [(5, 8), (2, 9)],
#     [(6, 2), (4, 8)],
#     [(1, 5), (5, 2)]]
# print(lufthansa(G))