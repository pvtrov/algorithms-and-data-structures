from zad2ktesty import runtests

# TODO napisac funcke do odbierania palindromu

def palindrom( S ):
    DP = [[0] * len(S) for _ in range(len(S))]

    DP[0][0] = 1
    indexes = [[[0, 0]] * len(DP) for _ in range(len(DP))]

    for j in range(1, len(S)):
        for i in range(j, -1, -1):
            if i == j:
                DP[i][j] = 1
            elif i + 1 == j:
                if S[i] == S[j]:
                    DP[i][j] = 2
                else:
                    DP[i][j] = 1
            else:
                if S[i] == S[j]:
                    DP[i][j] = DP[i+1][j-1] + 2
                else:
                    DP[i][j] = max(1, DP[i+1][j])

    max_ = -1
    for i in range(len(DP)):
        for j in range(len(DP)):
            if max_ < DP[i][j]:
                max_ = DP[i][j]
                index = indexes[i][j]

    return [max_]


# S = "acca"
# print(palindrom(S))
runtests ( palindrom )