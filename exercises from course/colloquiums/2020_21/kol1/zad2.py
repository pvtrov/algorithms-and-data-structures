from zad2testy import runtests


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def SortH(p,k):
    result = p

    while p is not None:
        checker = p
        counter = 0
        while checker is not None and counter <= k:
            if checker.val < p.val:
                temporary = checker.val
                checker.val = p.val
                p.val = temporary
            checker = checker.next
            counter += 1

        p = p.next

    return result


runtests( SortH )
