"""
Zaproponuj klasę reprezentującą strukturę danych, która w konstruktorze dostaje tablicę liczb naturalnych długości n o
zakresie wartości [0, k]. Ma ona posiadać metodę count_num_in_range(a, b) - ma ona zwracać informację o tym, ile liczb
w zakresie [a, b] było w tablicy, ma działać w czasie O(1).
Można założyć, że zawsze a >= 1, b <= k.
"""


def count_these_facking_numbers(array):
    k = max(array)
    counters_array = [0] * (k+1)
    for i in range(len(array)):
        counters_array[array[i]] += 1

    for j in range(1, k):
        counters_array[j] += counters_array[j-1]

    return counters_array


class struct:
    def __init__(self, array):
        self.array = array
        self.counters_array = count_these_facking_numbers(array)

    def count_num_in_range(self, a, b):
        return self.counters_array[b] - self.counters_array[a]


array = [1, 2, 2, 3, 3, 3, 5, 5]
x = struct(array)
print(x.count_num_in_range( 2, 4))
