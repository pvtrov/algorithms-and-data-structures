

def knap_sack(costs, profits, max_cost):       #O(n*max_weight)
    n = len(costs)
    # O( n * p )
    DP = [[0] * (max_cost+1) for _ in range(n)]
    for w in range(costs[0], max_cost+1):
        DP[0][w] = profits[0]

    for i in range(1, n):
        for cost in range(1, max_cost+1):
            DP[i][cost] = DP[i-1][cost]
            if cost >= costs[i]:
                DP[i][cost] = max(DP[i][cost], DP[i-1][cost - costs[i]] + profits[i])
    return DP[n-1][max_cost]


def get_solution(result_array, array_of_weights, array_of_things, i, w):        #zwraca indeksy przedmiotw
    if i < 0:
        return []

    if i == 0:
        if w >= array_of_weights[0]:
            return 0
        return []

    if w >= array_of_weights[i] and result_array[i][w] == result_array[i-1][w-array_of_weights[i]+array_of_things[i]]:
        return get_solution(result_array, array_of_weights, array_of_things, i-1, w - array_of_weights[i]) + i

    return get_solution(result_array, array_of_weights, array_of_things, i-1, w)


W = [1, 2, 1, 4]
P = [2, 3, 2, 5]
max_ = 5
print(knap_sack(W, P, max_))