from egzP9btesty import runtests


def find_euler_cycle(graph):
	edge_count = dict()

	for i in range(len(graph)):
		edge_count[i] = len(graph[i])

	if len(graph) == 0:
		return

	curr_path = []
	circuit = []
	curr_path.append(0)
	curr_vertex = 0

	while len(curr_path):
		if edge_count[curr_vertex]:
			curr_path.append(curr_vertex)
			next_v = graph[curr_vertex][-1]
			edge_count[curr_vertex] -= 1
			graph[curr_vertex].pop()
			curr_vertex = next_v
		else:
			circuit.append(curr_vertex)
			curr_vertex = curr_path[-1]
			curr_path.pop()

	circuit.reverse()
	return circuit


def remove_roads(G, begin, dest):
	G[begin].remove(dest)


def dyrektor( G, R ):
	for i in range(len(R)):
		for neib in R[i]:
			remove_roads(G, i, neib)

	res = find_euler_cycle(G)
	return res
	
runtests(dyrektor, all_tests=True)
