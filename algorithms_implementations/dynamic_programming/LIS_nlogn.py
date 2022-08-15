

def f(T, l, r, value):
    while r - l > 1:
        m = l + (r-l)//2
        if T[m] >= value:
            r = m
        else:
            l = m
    return r


def lis(T):
    n = len(T)
    DP = [0] * (n+1)
    len_ = 0

    DP[0] = T[0]
    len_ = 1
    for i in range(1, n):
        if T[i] < DP[0]:
            DP[0] = T[i]
        elif T[i] > DP[len_-1]:
            DP[len_] = T[i]
            len_ += 1
        else:
            DP[f(DP, -1, len_-1, T[i])] = T[i]

    return len_


A = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
print(lis(A))