"""
Dany jest ważony graf nieskierowany reprezentowany przez macierz T o rozmiarach n × n (dla
każdych i, j zachodzi T[i][j] = T[j][i]; wartość T[i][j] > 0 oznacza, że istnieje krawędź między
wierzchołkiem i a wierzchołkiem j z wagą T[i][j]). Dana jest także liczba rzeczywista d. Każdy
wierzchołek w G ma jeden z kolorów: zielony lub niebieski. Zaproponuj algorytm, który wyznacza
największą liczbę naturalną `, taką że w grafie istnieje ` par wierzchołków (p, q) ∈ V × V spełniających warunki:
1. q jest zielony, zaś p jest niebieski,
2. odległość między p i q (liczona jako suma wag krawędzi najkrótszej ścieżki) jest nie mniejsza
niż d,
3. każdy wierzchołek występuje w co najwyżej jednej parze.
Rozwiązanie należy zaimplementować w postaci funkcji:
def BlueAndGreen(T, K, D):
...
która przyjmuje:
T: graf reprezentowany przez kwadratową macierz sąsiedztwa, gdzie wartość 0 oznacza brak
krawędzi, a liczba większa od 0 przedstawia odległość pomiędzy wierzchołkami,
K: listę przedstawiającą kolory wierzchołków,
D: odległość o której mowa w warunku 2 opisu zadania.
Funkcja powinna zwrócić liczbę ` omawianą w treści zadania.
"""

T = [[0, 1, 1, 0, 1],
     [1, 0, 0, 1, 0],
     [1, 0, 0, 0, 1],
     [0, 1, 0, 0, 1],
     [1, 0, 1, 1, 0]]

K = ["B", "B", "G", "G", "B"]
D = 2

# wynikiem jest wartość 2.