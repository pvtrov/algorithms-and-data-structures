from zad2testy import runtests
from math import inf
"""
Dany jest ciąg klocków (a1, b1), . . . (an, bn). Każdy klocek zaczyna się na pozycji ai
i ciągnie się
do pozycji bi
. Klocki mogą spadać w kolejności takiej jak w ciągu. Proszę zaimplementować funkcję
tower(A), która wybiera możliwie najdłuższy podciąg klocków taki, że spadając tworzą wieżę i
żaden klocek nie wystaje poza którykolwiek z wcześniejszych klocków. Do funkcji przekazujemy
tablicę A zawierającą pozycje klocków ai,bi
. Funkcja powinna zwrócić maksymalną wysokość wieży
jaką można uzyskać w klocków w tablicy A.
"""
"""
działam na tablicy heights, w której zawiera sie najwyzsza mozliwa wysokosc dla i-tego elementu, oraz a i b najdłuższego
klocka w danej wiezy

heights[i] = jeśli: ai >= aj i bi <= bj: heights[i] = [heights[j][0] + 1, (aj, bj)]
jeśli nie zjadnuje takiego klocka poprzedniegpo to
heights[i] = [1, (ai, bi)]
złożonosc czasowa: O(n^2)
pamieciowa: O(n)
"""


def tower(A):
    height = [[] for _ in range(len(A))]
    height[0] = [1, (A[0][0], A[0][1])]

    for i in range(1, len(A)):
        max_value = -inf
        counter = 0
        for j in range(i):
            if A[i][0] >= height[j][1][0] and A[i][1] <= height[j][1][1]:
                counter += 1
                if height[j][0] > max_value:
                    max_value = height[j][0]

        height[i] = [max_value + 1, (A[i][0], A[i][1])]

        if counter == 0:
            height[i] = [1, (A[i][0], A[i][1])]

    result = max(height)
    return result[0]


runtests( tower )
