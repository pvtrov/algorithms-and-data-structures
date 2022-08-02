"""
Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami. Każde miasto jest otoczone murem i
ma tylko dwie bramy. Z każdej bramy prowadzi dokładnie jedna droga do jednej oazy (ale do danej oazy może dochodzić
dowolnie wiele dróg; oazy mogą też być połączone drogami między sobą). Prawo Algocji wymaga, że jeśli ktoś wjechał do
miasta jedną bramą, to musi go opuścić drugą.
Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju odczyta zakaz formułowania zadań “o szachownicy”
(obraza majestatu). Szach chce, żeby goniec odwiedził każde miasto dokładnie raz (ale nie ma ograniczeń na to ile razy
odwiedzi każdą z oaz). Goniec wyjeżdża ze stolicy Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić.
Proszę przedstawić (bez implementacji) algorytm, który stwierdza czy odpowiednia trasa gońca istnieje.
Proszę uzasadnić poprawność algorytmu oraz oszacować jego złożoność czasową.
"""
from queue import Queue

"""
oazy, do których można dotrzeć z innej oazy bez wchodzenia do miasta łączymy w jeden wierzchloek, nastepnie sprawdzamy
czy istnieje droga eulera
"""

def DFS(u, graph, deleted, cycle, vertex_counter):
    for v in graph[u]:      # przechodze po sasiadach
        if deleted[u][v] is False:      # jesli nie krawedz jest nie usunieta to ja usuwam
            deleted[u][v] = True
            deleted[v][u] = True
            cycle = DFS(v, graph, deleted, cycle, vertex_counter)
            cycle.append(u)
            if u not in vertex_counter:
                vertex_counter.append(u)
    return cycle


def euler(graph):
    for i in range(len(graph)):  # sprawdzam czy moze byc cykl
        if len(graph[i]) == 0 or len(graph[i]) % 2 != 0:
            return None

    deleted = [[False for _ in range(len(graph))] for _ in range(len(graph))] # macierz usunietych krawedzi
    cycle = [0]             # odpoweidnie wierzchołki cyklu
    vertex_counter = []         # użyte wierzchołki, pomoze w stwerdzeniu czy graf jest spojny
    cycle = DFS(0, graph, deleted, cycle, vertex_counter)
    if len(vertex_counter) != len(graph):   # jeśli liczba wierzchołkow w cyklu jest inna od liczby wierzchlkow w grafie
        return None                         # oznacza ze graf jest niespojny
    return cycle


def add_neib(new_neib, graph, vertex, is_this_city):
    for neib in graph[vertex]:
        if is_this_city[neib]:
            new_neib.add(neib)


def add_cities(neighbours, is_this_city):
    cities_neib = []
    for neib in neighbours:
        if is_this_city[neib]:
            cities_neib.append(neib)
    return cities_neib


def make_new_edges(almost_graph, counter, index_dict):
    new_graph = [[] for _ in range(counter+1)]

    for vertex in almost_graph:
        if len(vertex[0]) == 1:
            for j in range(len(vertex[1])):
                new_graph[index_dict[vertex[1][j]]].append(index_dict[vertex[0][0]])
                new_graph[index_dict[vertex[0][0]]].append(index_dict[vertex[1][j]])
        elif len(vertex[0]) > 1:
            for s in range(len(vertex[1])):
                new_graph[index_dict[vertex[1][s]]].append([vertex[2]])
                new_graph[vertex[2]].append(index_dict[vertex[1][s]])
    return new_graph


def make_new_vertex(graph, start, visited, is_this_city):
    new_vertex = []
    new_neib = set()
    queue = Queue()
    visited[start] = True
    queue.put(start)
    new_vertex.append(start)

    while queue.qsize():
        vertex = queue.get()
        for neib in graph[vertex]:
            if not visited[neib] and not is_this_city[neib]:
                visited[neib] = True
                new_vertex.append(neib)
                add_neib(new_neib, graph, neib, is_this_city)
                queue.put(neib)
    return new_vertex, list(new_neib), visited


def make_new_graph(graph, is_his_city):
    vertex_counter = 0
    visited = [False for _ in range(len(graph))]
    index_dict = dict()
    new_edges = []

    for i in range(len(graph)):
        if not is_his_city[i] and not visited[i]:
            new_vertex, new_neib, visited = make_new_vertex(graph, i, visited, is_his_city)
            index_dict[i] = vertex_counter
            vertex_counter += 1
            new_edges.append([new_vertex, new_neib, vertex_counter])
        elif is_his_city[i]:
            index_dict[i] = vertex_counter
            new_edges.append([[i], add_cities(graph[i], is_his_city)])
            vertex_counter += 1

    new_graph = make_new_edges(new_edges, vertex_counter, index_dict)
    return new_graph




graph = [[1, 6],
         [0, 2, 3],
         [1, 3, 7, 6, 5],
         [1, 2, 7],
         [5, 7],
         [4, 2, 6],
         [0, 2, 5],
         [2, 3, 4]]
is_his_city = [True, False, False, True, True, False, True, False]
print(make_new_graph(graph, is_his_city))


