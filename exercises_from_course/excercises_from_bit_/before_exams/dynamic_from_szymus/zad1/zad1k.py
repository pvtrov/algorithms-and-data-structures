from zad1ktesty import runtests


def roznica( S ):
    DP = [[0] * len(S) for _ in range(len(S))]

    for i in range(1, len(S)):
        for j in range(i, len(S)):
            if S[j] == "0":
                DP[i][j] = DP[i][j-1] + 1
            else:
                DP[i][j] = DP[i][j-1] - 1

    max_ = -1
    for i in range(len(S)):
        for j in range(i, len(S)):
            if DP[i][j] > max_:
                max_ = DP[i][j]

    if max_ <= 0:
        return -1
    return max_


# S = '110001'
# print(roznica(S))
runtests ( roznica )