from zad1testy import runtests

"""
Mówimy, że punkt (x, y) słabo dominuje punkt (x′, y′) jeśli x ≤ x′ oraz y ≤ y′
(w szczególności każdy punkt słabo dominuje samego siebie). Dana jest tablica P zawierająca n punktów. 
Proszę zaimplementować funkcję dominance(P), która zwraca tablicę S taką, że:
1. elementami S są indeksy punktów z P,
2. dla każdego punktu z P, S zawiera indeks punktu, który go słabo dominuje,
3. S zawiera minimalną liczbę elementów
"""

"""
przechodze po tablicy P i dla kazdego jej elementu przechodze znowu po jej elemenatch i szukam dominującego elementu.
wkładam dominujace elementy do tablicy helper. zwracam te indexy dla których tablica helper była pusta:
jeśli jest pusta to znaczy że dominuje ja tylko ona sama. te które nie są puste maja inne liczby dominujace, a jesli
x <= y oraz y <= z  to  x <= z
np. dla pierwszego testu, tablica helper: 
[[1], [], [], [0, 1, 2], []] czyli jesli np P[3] jest zdominowane przez P[0], idziemy do P[0] ktore jest zdominowane 
przez P[1], która jest zdominowana przez nią sama wiec dla P[0], P[1], P[3] odpowiedzią jest index 1 bo P[1] dominuje 
siebie, P[0] i P[3] itd. By oszczedzic pamiec i czas zamienilam tablice helper na licznik który liczy czy jakas liczba 
ma jakis dominujace liczby poza nia sama, ale zosatwilam helpera w komentarzu zeby bylo widac o co mi chodzilo :)

złożoność czasowa: O(n^2) 
 """


def dominance(P):
    # helper = [[] for _ in range(len(P))]
    result = []
    for i in range(len(P)):
        x_prim, y_prim = P[i][0], P[i][1]
        counter = 0
        for j in range(len(P)):
            if j != i:
                x, y = P[j][0], P[j][1]
                if x_prim >= x and y_prim >= y:
                    # helper.append(j)
                    counter += 1
                    break
        if counter == 0:
            result.append(i)

    # for i in range(len(helper)):
    #     if len(helper[i]) == 0:
    #         result.append(i)

    return result


runtests( dominance ) 
