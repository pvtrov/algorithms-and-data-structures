"""
Dana jest tablica z n liczbami całkowitymi. Zawiera ona bardzo dużo powtórzeń - co więcej,
zaledwie O(log(n)) liczb jest unikatowe. Napisz algorytm, który w czasie O(n log(logn)) posortuje
taką tablicę
"""


def nloglogn(array):
    uniq = []
    for i in range(len(array)):
        if array[i] not in uniq:
            uniq.append(array[i])


"""
mordo wiesz jak dalej a to tylko klepniecie implemetacnji a nie chce ci sie
"""