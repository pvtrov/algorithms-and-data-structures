from zad3testy import runtests
"""
Dany jest zbiór przedziałów A = {(a0, b0), . . . , (an−1, bn−1)}. Proszę zaimplementować funkcję:
def kintersect( A, k ):
...
która wyznacza k przedziałów, których przecięcie jest jak najdłuższym przedziałem. Zbiór A jest
reprezentowany jako lista par. Końce przedziałów to liczby całkowite. Można założyć, że k ≥ 1 oraz
k jest mniejsze lub równe łącznej liczbie przedziałów w A. Funkcja powinna zwracać listę numerów
przedziałów, które należą do rozwiązania.
Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
użytego algorytmu.
"""


def kintersect( A, k ):
  """Miejsce na Twoją implementację"""
  return list(range(k))

runtests( kintersect )