"""
Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci
, jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
John znajdzie optymalny plan wycinki.
"""

"""
    f(i) - max zysk jaki mozna uzyskac scinajac i-te drzewo
    f(i) = max ( f(0), f(1)...f(i-2), f(i-1) ) + zysk[i], 
    tylko nie wymyslilam jak to ladnie zapisac rekurencyjnie w programie wiec zrobilam to na tablicy:
    result[i] = max[ result[:i-1] ] + profit[i] < max zysk z poprzednich scinek + zysk i-tego drzewa >
"""


def black_forest(profits, result, parents):     # O (n^2)
    if len(profits) == 0:
        return None

    if len(profits) == 1:
        return profits[0]

    result[0] = profits[0]
    parents[0] = -1
    parents[1] = -1
    result[1] = profits[1]

    for i in range(2, len(profits)):
        result[i] = max(result[:(i-1)]) + profits[i]
        for j in range(i-1):
            if result[j] == (result[i] - profits[i]):
                parents[i] = j

    for i in range(len(result)):
        if result[i] == max(result):
            return i, max(result), parents


def get_result(parents, path, point):
    if parents[point] == -1:
        path.append(point)
        return path.reverse()

    path.append(point)
    get_result(parents, path, parents[point])
    return path


if __name__ == '__main__':
    profits = [5, 6, 4, 5, 5, 6, 2, 2, 7, 3]
    parents = [-1 for _ in range(len(profits))]
    result = [0 for _ in range(len(profits))]
    i, result, parents = black_forest(profits, result, parents)
    tree_plan = get_result(parents, [], i)
    print(tree_plan, result)