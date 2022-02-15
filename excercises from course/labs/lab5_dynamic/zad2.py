"""
Dana jest tablica n liczb naturalnych A. Proszę podać i zaimplementować algorytm, który sprawdza, czy da się wybrać
podciąg liczb z A, które sumują się do zadanej wartości T.
"""

"""
f(A, n, T) = czy można znaleźć tak podciąg który który sumuje się do sumy T

rozbijamy to na dwa przypadki, kiedy odejmujemy od sumy aktualny element lub nie

f(A, n, 0) == True
f(A, n<0, T) lub f(A, n, T<0) == False
f(A, n, T) = f(A, n-1, T) lub f(A, n-1, T-A[n])
"""


def sub_sum(A, n, T):
    if T == 0:
        return True

    if n < 0 or T < 0:
        return False

    first = sub_sum(A, n-1, T)
    second = sub_sum(A, n-1, T-A[n])

    return first or second


if __name__ == '__main__':
    A = [1, 2, 5, 8, 13, 2, 4, 5]
    T = 100
    if sub_sum(A, len(A)-1, T):
        print(True)
    else:
        print(False)