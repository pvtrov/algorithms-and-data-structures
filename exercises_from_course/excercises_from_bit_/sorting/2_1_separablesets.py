"""
Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, gdzie m jest znacznie mniejsze od n.
Zaproponuj algorytm, który sprawdzi, czy zbiory są rozłączne.
"""


def check_if_separable(n, m):  # O(n+m)
    k = max(m)
    counters = [0] * (k + 1)

    for i in range(len(m)):
        counters[m[i]] += 1

    for j in range(len(n)):
        if n[j] <= k:
            counters[n[j]] -= 1
            if counters[n[j]] >= 0:
                return False

    return True


m = [1, 2, 4]
n = [5, 6, 7, 8, 9, 0, 5, 7, 6, 5, 5, 6, 7, 9, 9]
print(check_if_separable(n, m))
