from egzP3atesty import runtests
from math import inf


class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None


def make_me_arrays(field):
    costs = []
    profits = []
    max_cost = field.fundusze

    while field is not None:
        costs.append(field.koszt)
        profits.append(field.wyborcy)
        field = field.next

    return costs, profits, max_cost


# O(n*p)
def choose_the_best_fields(first_field):
    # O(n)
    costs, profits, max_cost = make_me_arrays(first_field)
    n = len(costs)

    # O( n * p )
    DP = [[0] * (max_cost*n) for _ in range(n)]
    for w in range(costs[0], max_cost+1):
        DP[0][w] = profits[0]

    for i in range(1, n):
        for cost in range(1, max_cost+1):
            DP[i][cost] = DP[i-1][cost]
            if cost >= costs[i]:
                DP[i][cost] = max(DP[i][cost], DP[i-1][cost - costs[i]] + profits[i])
    return DP[n-1][max_cost]


def wybory(T):
    best_choice = 0

    # O(m*n*p)
    for i in T:
        best_choice += choose_the_best_fields(i)
    return best_choice


runtests(wybory, all_tests = True)

# wyb1okr1 = Node(3, 8, 15)
# wyb1okr2 = Node(2, 7, 15)
# wyb1okr3 = Node(4, 5, 15)
# wyb1okr1.next = wyb1okr2
# wyb1okr2.next = wyb1okr3
# wyb2okr1 = Node(4, 7, 8)
# wyb2okr2 = Node(5, 2, 8)
# wyb2okr1.next = wyb2okr2
# wyb3okr1 = Node(3, 5, 10)
# wyb3okr2 = Node(3, 5, 10)
# wyb3okr1.next = wyb3okr2
# T = [wyb1okr1, wyb2okr1, wyb3okr1]
# print(wybory(T))