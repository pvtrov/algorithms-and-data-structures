from egzP5atesty import runtests 

# O(n^2)


def find_min(DP, T, a, b):
    if a == b:
        DP[a][b] = T[a]
    elif DP[a][b] != -1:
        return DP[a][b]
    else:
        DP[a][b] = min(T[b], find_min(DP, T, a, b-1))
    return DP[a][b]


def inwestor ( T ):
    DP = [[-1] * len(T) for _ in range(len(T))]

    real_max = -1
    for i in range(len(T)):
        for j in range(i, len(T)):
            max = (j - i + 1) * find_min(DP, T, i, j)
            if max > real_max:
                real_max = max
    return real_max


runtests ( inwestor, all_tests=True )
T = [2, 1, 5, 6, 2, 3]
print(inwestor(T))