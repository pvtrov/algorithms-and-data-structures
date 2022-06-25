"""
Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć
długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n**2)).
"""

"""
f(A, B, n, R, I) = zwraca długość njadłuższeo wspólnego podciągu z A i B na n-tym indeksie tablicy A. czyli dla każdego
indeksu A przechodzimy po tablicy B, stąd O(n**2). < tab A, tab B, max indeks, tablica wyników, tablica indeks na którym
 się skończył podciąg w B > 

f(A, B, n, R, I) = { I[n] == n-1, return max(R)
                    f(A, B, n-1, R[n]+1) , A[n] == <B[I[n-1]] - B[len(B)-1]>
                    f(A, B, n-1, R[n], A[n] != <B[I[n-1]] - B[len(B)-1]>
                    }
"""



def longest_common(A, B, n, R, I):
    if n == 0:
        return max(R)

    if I[n-1] == len(B)-1:
        return max(R)

    for index in range(len(B)-1, I[n-1], -1):
        if A[n] == B[index]:
            if n == len(B) - 1:
                R[n] = 1
                I[n] = index
                return longest_common(A, B, n - 1, R, I)

            else:
                R[n] += R[n+1] + 1
                I[n] = index
                return longest_common(A, B, n-1, R, I)

        else:
            continue

    if n == len(B) - 1:
        R[n] = 0
        I[n-1] = I[n]
        longest_common(A, B, n-1, R, I)
    else:
        I[n-1] = I[n]
        R[n] = R[n+1]
        longest_common(A, B, n-1, R, I)
    return max(R)


if __name__ == '__main__':
    A = [2, 3, 8, 9, 1, 5, 2]
    B = [3, 8, 2, 1, 2, 9, 0]
    R = [0 for _ in range(len(A))]
    I = [0 for _ in range(len(B))]
    print(longest_common(A, B, len(A)-1, R, I))