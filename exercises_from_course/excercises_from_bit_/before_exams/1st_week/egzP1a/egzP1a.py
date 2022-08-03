from math import inf

from egzP1atesty import runtests


def recurse(DP, i, dictionary, word):
    if DP[i] is not None:
        return DP[i]

    if i < 4:
        key = ''
        for j in range(i + 1):
            key += word[j]
        if dictionary.get(key) is not None:
            DP[i] = 1
            return 1

    minimum = inf
    temp_ = ''
    for j in range(i, max(-1, i - 4), -1):
        temp_ = word[j] + temp_
        if dictionary.get(temp_) is not None:
            minimum = min(minimum, recurse(DP, j - 1, dictionary, word))

    DP[i] = minimum + 1
    return minimum + 1


def titanic(W, M, D):
    dictionary = {}

    for i in range(len(D)):
        dictionary[M[D[i]][1]] = True

    word = ""
    for j in range(len(W)):
        word += M[ord(W[j]) - 65][1]

    DP = [None] * len(word)
    DP[0] = 1

    return recurse(DP, len(word) - 1, dictionary, word)


runtests(titanic, recursion=True)
