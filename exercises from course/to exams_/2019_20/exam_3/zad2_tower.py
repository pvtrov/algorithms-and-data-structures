from zad2testy import runtests
"""
Dany jest ciąg klocków (a1, b1), . . . (an, bn). Każdy klocek zaczyna się na pozycji ai
i ciągnie się do pozycji bi. Klocki mogą spadać w kolejności takiej jak w ciągu. Proszę zaimplementować funkcję
tower(A), która wybiera możliwie najdłuższy podciąg klocków taki, że spadając tworzą wieżę i
żaden klocek nie wystaje poza którykolwiek z wcześniejszych klocków. Do funkcji przekazujemy
tablicę A zawierającą pozycje klocków ai,bi. Funkcja powinna zwrócić maksymalną wysokość wieży
jaką można uzyskać w klocków w tablicy A.
"""
"""
troche nie dziala
"""


def tower(A):
    towers = [[] for _ in range(len(A))]
    towers[0].append((1, A[0][0], A[0][1]))

    for i in range(1, len(A)):
        for j in range(0, i):
            min_ = towers[j][-1][0]
            x = towers[j][-1][1]
            y = towers[j][-1][2]
            if A[i][0] >= x and A[i][1] <= y:
                towers[j].append((min_ + 1, A[i][0], A[i][1]))
        towers[i].append((1, A[i][0], A[i][1]))

    max_ = max(len(towers[i]) for i in range(len(A)))
    return max_


runtests( tower )
