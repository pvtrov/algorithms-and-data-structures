from egzP6btesty import runtests

moves = {
    'LU': [-2, 1],
    'UL': [-1, 2],
    'UR': [1, 2],
    'RU': [2, 1],
    'RD': [2, -1],
    'DR': [1, -2],
    'DL': [-1, -2],
    'LD': [-2, -1]
}


# 1 -> świeci, -1 -> nie świeci
def jump(M):
    fields = {}
    fields[(0, 0)] = 1
    current_move = [0, 0]

    for move in M:
        to = moves.get(move)
        current_move[0] += to[0]
        current_move[1] += to[1]
        siup = tuple(current_move)
        if siup in fields.keys():
            fields[siup] = -(fields.get(siup))
        else:
            fields[siup] = 1
        current_move = list(siup)

    values = fields.values()
    counter = 0
    for val in values:
        if val == 1:
            counter += 1

    return counter


runtests(jump, all_tests=True)

# M = ['UL', 'RD', 'LU', 'LU', 'RD', 'DL', 'UR', 'DR']
# print(jump(M))
