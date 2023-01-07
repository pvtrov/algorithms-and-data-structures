class Node:
    def __init__(self, id):
        self.id = id
        self.out = set()
        self.RN = set()
        self.parent = None

    def connect_to(self, neib):
        self.out.add(neib)


def lex_BFS(graph):
    visited = []
    vertices = [set(range(1, len(graph)))]

    while len(visited) < len(graph) - 1:
        curr_ver = vertices[-1].pop()
        visited.append(curr_ver)
        idx = 0
        while idx < len(vertices):
            i = 0
            neighbour = vertices[idx] & graph[curr_ver].out
            not_neighbour = vertices[idx] - neighbour
            if len(neighbour) > 0:
                vertices.insert(idx+1, neighbour)
                i += 1
            if len(not_neighbour) > 0:
                vertices.insert(idx+1, not_neighbour)
                i += 1
            vertices.remove(vertices[idx])
            idx += 1

        new_vertices = []
        intersection = set()
        for v in visited:
            new_vertices.append(v)
            intersection.add(v)

        graph[curr_ver].RN = intersection & graph[curr_ver].out
        found = False
        while len(new_vertices) > 0 and not found:
            if {new_vertices[-1]} & graph[curr_ver].RN == set():
                new_vertices.pop(-1)
            else:
                found = True

        if found:
            graph[curr_ver].parent = new_vertices[-1]

    return visited