"""
Carol musi przewieźć pewne niebezpieczne substancje z laboratorium x do laboratorium y, podczas
gdy Max musi zrobić to samo, ale w przeciwną stronę. Problem polega na tym, że jeśli substancje
te znajdą się zbyt blisko siebie, to nastąpi reakcja w wyniku której absolutnie nic się nie stanie (ale
szefowie Carol i Max nie chcą do tego dopuścić, by nie okazało się, że ich praca nie jest nikomu
potrzebna). Zaproponuj, uzasadnij i zaimplementuj algorytm planujący jednocześnie trasy Carol
i Maxa tak, by odległość między nimi zawsze wynosiła co najmniej d. Mapa połączeń dana jest
jako graf nieskierowany, w którym każda krawędź ma dodatnią wagę (x i y to wierzchołki w tym
grafie). W jednostce czasu Carol i Max pokonują dokładnie jedną krawędź. Jeśli trzeba, dowolne z
nich może się w danym kroku zatrzymać (wówczas pozostaje w tym samym wierzchołku). Carol i
Max nie mogą równocześnie poruszać się tą samą krawędzią (w przeciwnych kierunkach).
Rozwiązanie należy zaimplementować w postaci funkcji:

def keep_distance(M, x, y, d):
...
która przyjmuje numery wierzchołków x oraz y, minimalną odległość d i graf reprezentowany przez
kwadratową, symetryczną macierz sąsiedztwa M. Wartość M[i][j] == M[j][i] to długość krawędzi
między wierzchołkami i oraz j, przy czym M[i][j] == 0 oznacza brak krawędzi między wierzchołkami.
W macierzy nie ma wartości ujemnych. Funkcja powinna zwrócić listę krotek postaci:
[(x, y), (u1, v1), (u2, v2), ..., (uk, vk), (y, x)]
reprezentującą ścieżki Carol i Max. W powyższej liście element (ui, vi) oznacza, że Carol znajduje
się w wierzchołku ui, zaś Max w wierzchołku vi. Można założyć, że rozwiązanie istnieje.

Podpowiedź. Proszę rozważyć nowy graf, być może z dużo większą liczbą wierzchołków niż graf
wejściowy.
"""
from tests.py import runtests

# M = [
#     [0, 1, 1, 0],
#     [1, 0, 0, 1],
#     [1, 0, 0, 1],
#     [0, 1, 1, 0],
# ]
# x = 0
# y = 3
# d = 2
# wynikiem jest na przykład lista: [(0, 3), (1, 2), (3, 0) ]