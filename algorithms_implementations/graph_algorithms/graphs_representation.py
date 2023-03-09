# na słowniku


graph = {'1': ['2', '3'],
         '2': ['1', '4', '5'],
         '3': ['1', '6'],
         '4': ['2'],
         '5': ['2', '6'],
         '6': ['3', '5']}


# na class liście

class adj_node:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edges(self, start, end):
        node = adj_node(end)
        node.next = self.graph[start]
        self.graph[start] = node

        node = adj_node(start)
        node.next = self.graph[end]
        self.graph[end] = node

    def print_graph(self):

        for i in range(self.V):
            print("for {}\n".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edges(0, 1)
    graph.add_edges(0, 4)
    graph.add_edges(1, 2)
    graph.add_edges(1, 3)
    graph.add_edges(1, 4)
    graph.add_edges(2, 3)
    graph.add_edges(3, 4)

    graph.print_graph()


# na macierzy

def matrix_graph(number_of_vertices):
    matrix_of_edges = [[0] * number_of_vertices for i in range(number_of_vertices)]

    matrix_of_edges[0][1] = 1
    matrix_of_edges[0][2] = 1
    matrix_of_edges[1][0] = 1
    matrix_of_edges[1][3] = 1
    matrix_of_edges[1][4] = 1
    matrix_of_edges[2][0] = 1
    matrix_of_edges[2][3] = 1
    matrix_of_edges[3][3] = 1
    matrix_of_edges[3][1] = 1
    matrix_of_edges[3][4] = 1
    matrix_of_edges[3][2] = 1
    matrix_of_edges[4][3] = 1
    matrix_of_edges[4][1] = 1

    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            print(matrix_of_edges[i][j])
        print("\n")
