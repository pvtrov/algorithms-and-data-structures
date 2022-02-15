# Proszę zaimplementować algorytm BFS tak, żeby znajdował
# najkrótsze ścieżki w grafie i następnie, żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego
# do wskazanego wierzchołka

def findShortestPath(G, s, t, path=[]):
    path = path + [s]
    if s == t:
        return path

    if len(G[s]) == 0:
        return None

    shortest = None
    for node in G[s]:
        if node not in path:
            new_path = findShortestPath(G, node, t, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest

if __name__ == '__main__':
    path = []
    graph = [[1, 2, 4],
             [0, 2, 3],
             [0, 1, 3],
             [1, 2, 4],
             [3, 0]]
    print(findShortestPath(graph, 0, 3, path))