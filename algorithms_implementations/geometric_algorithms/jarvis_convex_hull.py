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


def dist(p_1, p_2):
    """
    Counts distance between two points
    :param p_1: first point
    :param p_2: second point
    :return:
    """
    return (p_1[0] - p_2[0]) ** 2 + (p_1[1] - p_2[1]) ** 2


def find_next_angle(p_1, points, e):
    result = points[0]
    for p in points:
        if -e < my_determinant(p_1, result, p) < e and dist(p_1, p) > dist(result, p_1):
            result = p
        elif my_determinant(p_1, result, p) < -e:
            result = p

    return result


def jarvis_algorithm(tab, e=10 ** (-10)):
    """
    Determines the convex hull
    :param tab:
    :param e:
    :return:
    """
    points = tab.copy()
    p0 = find_lowest(points)
    res = [p0]
    points = [p0] + points
    p = None

    while p is not p0:
        p = find_next_angle(res[-1], points, e)
        res.append(p)

    res = res[:-1]
    return res
