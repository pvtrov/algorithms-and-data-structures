from egzP2btesty import runtests
from math import log10


class Point:
    def __init__(self):
        self.number = 0
        self.left = None
        self.right = None


def add_item(string, point):
    point.number += 1

    for i in range(len(string)-1, -1, -1):
        if string[i] == '1':
            if point.right is not None:
                point = point.right
            else:
                point.right = Point()
                point = point.right
        else:
            if point.left is not None:
                point = point.left
            else:
                point.left = Point()
                point = point.left
        point.number += 1


def count_words(string, point):
    if string is None:
        return point.number

    for i in range(len(string)-1, -1, -1):
        if string[i] == '1':
            if point.right is not None:
                point = point.right
        else:
            if point.left is not None:
                point = point.left

    return point.number


def kryptograf( D, Q ):
    tree = Point()

    for item in D:
        curr_tree = tree
        add_item(item, curr_tree)

    almost_result = 0
    for sufix in Q:
        count_tree = tree
        almost_result += log10(count_words(sufix, count_tree))

    return almost_result




# D = ['0', '100', '1100', '1101', '1111']
# Q = ['', '1', '11', '0', '1101']
# print(kryptograf(D, Q))
# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 3)