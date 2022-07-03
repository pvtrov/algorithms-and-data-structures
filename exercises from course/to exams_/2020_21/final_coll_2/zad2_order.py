from zad2testy import runtests
"""
Na osi liczbowej znajduje się N punktów większych od M = 10 K . Z punktu A można przeskoczyć
na punkt B wtedy i tylko wtedy gdy A%10 K == B//10 K . Proszę zaimplementować funkcję:
def order( L,K ):
...
porządkującą punkty, tak aby możliwe było przejście od najwcześniejszego punktu w tym porządku,
kolejno przez wszystkie punkty, do ostatniego. Funkcja otrzymuje listę wartości określającą położe-
nie punktów na osi liczbowej i powinna zwrócić listę punktów w kolejności ich odwiedzania. Jeżeli
uporządkowanie punktów nie jest możliwe, funkcja powinna zwrócić N one.
Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
użytego algorytmu.

Przykład.
Dla danych:
L = [56,15,31,43,54,35,12,23], K = 1
przykładowym, prawidłowym wynikiem jest lista:
L = [12,23,31,15,54,43,35,56]
"""

def order(L,K):
    """tu prosze wpisac wlasna implementacje"""
    return None

    
runtests( order )


