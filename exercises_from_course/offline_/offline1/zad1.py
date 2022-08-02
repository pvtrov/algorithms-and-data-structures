
from zad1testy import Node, runtests

"""
Agnieszka Patro

Żeby rozwiązać to zadanie wykonuje insertion sorta z tym że przechodze "wprzód" tylko 
k elementów
złożoność czasowa: O(n*k)
złożoność pamięciowa O(n)

dla k = 1: TC: O(n)
dla k = logn TC: O(nlogn)
dla k = n TC: O(n^2)
"""


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
