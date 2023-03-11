# determinant
def my_determinant(a, b, c):
    """
    Determines the determinant
    :param a: point a
    :param b: point b
    :param c: point c
    :return:
    """
    a_x, a_y = a
    b_x, b_y = b
    c_x, c_y = c
    return a_x * b_y + b_x * c_y + a_y * c_x - b_y * c_x - c_y * a_x - a_y * b_x


def gt(point_1, point_2, point_0, e):
    if my_determinant(point_0, point_2, point_1) > e:
        return True
    return False


def partition(tab, l, r, point_0, e):
    pivot = tab[r]
    smaller = l
    for i in range(l, r):
        if gt(pivot, tab[i], point_0, e):
            tab[i], tab[smaller] = tab[smaller], tab[i]
            smaller += 1
    tab[smaller], tab[r] = tab[r], tab[smaller]
    return smaller


# quicksort
def qsort(tab, l, r, point_0, e):
    if l >= r:
        return
    p = partition(tab, l, r, point_0, e)
    qsort(tab, l, p - 1, point_0, e)
    qsort(tab, p + 1, r, point_0, e)


# point and comparison
def eq(point_1, point_2, point_0, e):
    if -e <= my_determinant(point_0, point_1, point_2) <= e:
        return True
    return False


# array sorting
def sort(points, p0, e):
    qsort(points, 0, len(points) - 1, p0, e)


def remove_same_angles(points, point_0, e):
    counter = 0
    for i in range(1, len(points)):
        if eq(points[counter], points[i], point_0, e):
            if dist(point_0, points[counter]) > dist(points[i], point_0):
                points[i] = None
            else:
                points[counter] = None
                counter = i
        else:
            counter = i

    res = []
    for p in points:
        if p is not None:
            res.append(p)
    return res


def dist(p_1, p_2):
    """
    Counts distance between two points
    :param p_1: first point
    :param p_2: second point
    :return:
    """
    return (p_1[0] - p_2[0]) ** 2 + (p_1[1] - p_2[1]) ** 2


# find lowest y (x) and delete it
def find_lowest(tab):
    """
    Function finds the lowest point
    :param tab: list of points (x, y)
    :return: founded point
    """
    res = tab[0]
    for point in tab:
        if point[1] < res[1]:
            res = point
        elif point[1] == res[1] and point[0] < res[0]:
            res = point
    tab.remove(res)
    return res


def graham_algorithm(points_set, e=10 ** (-10)):
    """
    Determines the convex hull
    :param points_set:
    :param e:
    :return:
    """
    if len(points_set) <= 2:
        return points_set

    points = points_set.copy()
    p_0 = find_lowest(points)
    sort(points, p_0, e)
    points = remove_same_angles(points, p_0, e)
    result = [p_0, points[0], points[1]]

    i = 2
    while i < len(points):
        while len(result) >= 2 and my_determinant(result[-2], result[-1], points[i]) < e:
            result.pop()

        result.append(points[i])
        i += 1

    return result
