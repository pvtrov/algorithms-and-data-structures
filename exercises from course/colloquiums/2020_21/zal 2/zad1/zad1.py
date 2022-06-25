# Agnieszka Patro

# zlozonosc: 
# czasowa - zauwazmy ze w kazdy obrot petli wykonuje
# sie w czasie O(1), a obrotow jest O(n), wiec zlozonosc
# czasowa jest O(N)

# pamieciowa - procz danych D, zuzywamy O(1) dodatkowej pamieci

# rozwiązanie: patrzymy co sie dzieje dla wszystkich prostokatow.
# Następnie patrzymy co się dzieje po usunieciu kazdego z nich.


from zad1testy import runtests


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

        best = max(best, (area_for_rec(
            cur_max_x, cur_max_y,
            cur_min_x, cur_min_y
        ), -i))

    return -best[1]


runtests(rect)
