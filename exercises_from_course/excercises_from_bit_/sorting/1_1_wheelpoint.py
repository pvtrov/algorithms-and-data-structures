"""
Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn. 0 <= x2 + y2 <= k, które są w nim równomiernie
rozłożone, tzn. prawdopodobieństwo znalezienia punktu na danym obszarze jest proporcjonalne do pola tego obszaru.
Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości do punktu (0, 0), tzn.
d = sqrt(x2 + y2).
"""
from math import sqrt


def insertion_sort(array):
    for i in range(1, len(array)):
        variable = array[i][0]
        j = i-1
        while j >= 0 and variable < array[j][0]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = [variable, i]
    return array


def wheel_point(points, k):     # O(5n + k) ~ O(n+k) -> liniowo
    distance = [[0, 0] for _ in range(len(points))]     # O(n)
    for i in range(len(points)):    # distance, index in input array    # O(n)
        distance[i] = [round(sqrt((points[i][0])**2 + (points[i][1]**2)), 4), i]

    buckets = [[] for _ in range(k)]    # O(n)
    for i in range(len(distance)):      # O(n)
        buckets[int(distance[i][0])].append(distance[i])

    almost_res = []
    for bucket in buckets:      # O(k)
        bucket = insertion_sort(bucket)
        almost_res.extend(bucket)

    result = [0] * len(points)
    for i in range(len(almost_res)):    # O(n)
        result[i] = points[almost_res[i][1]]

    return result, almost_res


points = [[-3, 0], [-1, 1], [-1, 3], [1, 3], [2, 1], [1, -2], [-2, -2]]
print(wheel_point(points, 4))


