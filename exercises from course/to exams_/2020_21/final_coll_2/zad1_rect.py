from zad1testy import runtests
"""
Dany jest zbiór N prostokątów o bokach równoległych do osi układu współrzędnych. Proszę zaim-
plementować funkcję:
def rect( D ):
...
która wskaże, który prostokąt należy usunąć tak, żeby przecięcie pozostałych miało jak największe
pole. Każdy prostokąt opisuje czwórka liczb całkowitych (x 1 , y 1 , x 2 , y 2 ) określających współrzędne
lewego dolnego i prawego górnego rogu prostokąta. Funkcja otrzymuje listę takich czwórek i powinna
zwrócić najmniejszy numer prostokąta, który należy usunąć.
Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
użytego algorytmu.

Przykład.
Dla listy:
D = [(2,3,10,6),(3,1,8,8),(5,4,9,7)]
prawidłowym wynikiem jest liczba 2.
"""


def area_for_rec(x1, y1, x2, y2):
    diff_x = x2 - x1
    diff_y = y2 - y1

    if diff_x < 0 or diff_y < 0:
        return 0
    else:
        return diff_x * diff_y


def rect(D):
    if len(D) <= 1:
        return None
    """tu prosze wpisac wlasna implementacje"""
    max_x, max_y, min_x, min_y = [], [], [], []

    for x1, y1, x2, y2 in D:
        max_x.append(x1)
        max_y.append(y1)
        min_x.append(x2)
        min_y.append(y2)

        # sortowanie działa w czasie O(1), bo listy zawieraja maks. 3 elementy
        max_x, max_y, min_x, min_y = [
            sorted(max_x), sorted(max_y),
            sorted(min_x), sorted(min_y)
        ]

        # wyrzucamy max 1 element
        max_x = max_x[-2:]
        max_y = max_y[-2:]

        min_x = min_x[:2]
        min_y = min_y[:2]

    best = (0, 0)
    for i in range(len(D)):
        x1, y1, x2, y2 = D[i]

        cur_max_x = (max_x[0] if max_x[1] == x1 else max_x[1])
        cur_max_y = (max_y[0] if max_y[1] == y1 else max_y[1])

        cur_min_x = (min_x[1] if min_x[0] == x2 else min_x[0])
        cur_min_y = (min_y[1] if min_y[0] == y2 else min_y[0])

        best = max(best, (area_for_rec(cur_max_x, cur_max_y, cur_min_x, cur_min_y), -i))

    return -best[1]


runtests( rect )


