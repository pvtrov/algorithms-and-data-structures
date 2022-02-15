"""Napisać funkcję: void sortString(string A[]); Funkcja sortuje tablicę n stringów różnej
długości. Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego."""

""" robie radix sorta"""

def radix(A, n, d):
    for j in range(1, n):
        while j > 0:
            if A[j][d] < A[j - 1][d]:
                A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A

def sortstring(A):
    bucket = []
    for i in A:
        while len(i) >= len(bucket):
            bucket.append([])
        bucket[len(i)].append(i)

    for i in range(len(bucket) - 1, 0, -1):
        q = len(bucket[i])
        C = radix(bucket[i], q, i - 1)
        bucket[i - 1] = bucket[i] + bucket[i - 1]
    return C


if __name__ == '__main__':
    A = ["agusia", "martynka", "marcelka", "karolinka", "bartus", "rafalek"]
    print(sortstring(A))