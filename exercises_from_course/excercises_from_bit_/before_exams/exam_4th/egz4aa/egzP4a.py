from egzP4atesty import runtests

# O(nlogn)

def f(T, l, r, value):
    while r - l > 1:
        m = l + (r-l)//2
        if T[m] >= value:
            r = m
        else:
            l = m
    return r


def mosty ( T ):
    # O(nlogn)
    T.sort()
    cities = []
    for bridge in T:
        cities.append(bridge[1])

    # O(nlogn)
    n = len(cities)
    DP = [0] * (n)
    len_ = 0

    DP[0] = cities[0]
    len_ = 1
    for i in range(1, n):
        if cities[i] < DP[0]:
            DP[0] = cities[i]
        elif cities[i] > DP[len_-1]:
            DP[len_] = cities[i]
            len_ += 1
        else:
            DP[f(DP, -1, len_-1, cities[i])] = cities[i]

    return len_


runtests ( mosty, all_tests=True )


