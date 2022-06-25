"""
Bajtocja jest krainą zawierającą N miast, N-1 dwukierunkowych dróg i układ dróg tworzy graf spójny. Mając listę K miast
do których musimy dostarczyć przesyłki i mogąc wystartować i zakończyć trasę w dowolnym mieście, podaj minimalny dystans,
który musimy przebyć, że zrealizować to zadanie
"""

"""
Bajtocja jest drzewem, 
usuwamy liscie ktore nie sa w liscie K, potem puszczamy dfs z jakiegoś liścia i szukamy srednicy, potem nasza szukana 
odleglosc to 2*waga drzewa - srednica
"""

from queue import Queue


def BFS(graph, start):
    queue = Queue()
    visited = [False for _ in range(len(graph))]
    distance = [-1 for _ in range(len(graph))]
    parent = [None for _ in range(len(graph))]

    distance[start] = 0
    visited[start] = True
    queue.put(start)

    while queue.qsize():
        u = queue.get()
        for v in graph[u]:
            if not visited[v] and graph[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.put(v)

    return max(distance)


def remove_vertex(byteland, first, second):
    byteland[first].remove(second)
    byteland[second].remove(first)
    return byteland


def delete_leafs(byteland, pack_list):
    for i in range(len(byteland)):
        if len(byteland[i]) == 1 and i not in pack_list:
            byteland = remove_vertex(byteland, i, byteland[i][0])
    return byteland


def get_farest_vertex(distances):
    max_val = -1
    vertex = None
    for i in range(len(distances)):
        if distances[i] > max_val:
            max_val = distances[i]
            vertex = i
    return vertex, max_val


def postman_distance(byteland, pack_list):
    byteland = delete_leafs(byteland, pack_list)
    start = 0

    for i in range(len(byteland)):
        if len(byteland[i]) == 1:
            start = i
            break

    far_length = BFS(byteland, start)
    counter = 0
    for i in range(len(byteland)):
        if len(byteland[i]) > 0:
            counter += 1
    return 2*(counter-1) - far_length


byteland = [[1, 2],
            [0, 3, 4],
            [0, 5],
            [1, 6],
            [1],
            [2, 7, 8],
            [3],
            [5],
            [5]]
pack_list = [0, 3, 4, 5]
print(postman_distance(byteland, pack_list))