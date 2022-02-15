from zad1testy import runtests

"""
Żaba Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
(wartość przekąki dodaje się do aktualnej energii Zbigniewa).
Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie. Funkcja powinna 
zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do n-1 lub −1 jeśli nie jest to możliwe
"""
"""
zadanie rozwiazuje za pomoca tablicy kcals która przechowuje w sobie dla kazdego indeksu tablice z minimalna liczba 
skoków i poprzedniej liczby
kcals[i] = [min_jumps, energy, prev_number] -> minimalna ilość skoków które zrobił zbigniew, ilość energi po zjedzeniu 
                i-tej przekąski, liczba z której skoczył
                
iteruje po tablicy A i szukam liczby j z której moge doskoczyć do liczby i, każda znaleziona dodaje do kcals[i]:

kcals[i] = [kcals[j][0] + 1, kcals[j][1] - (i-j) + A[i], j]

dla ostatniej liczby, wybieram z krotek tą która ma minimalną liczbe skoków i tą liczbe zwracam

O(n^3)
"""


def zbigniew( A ):
    n = len(A)
    kcals = [[] for _ in range(n)]

    kcals[0].append((0, A[0], -1))

    for i in range(1, n):
        counter = 0     # counter służy by sprawdzic czy z którejś liczby sie doskoczyło
        for j in range(i):
            for k in range(len(kcals[j])):
                if kcals[j][k][1] >= i-j:  # czy da sie skoczyć
                    counter += 1
                    kcals[i].append((kcals[j][k][0]+1, kcals[j][k][1]-(i-j)+A[i], j))
        if counter == 0:
            return -1

    solution = kcals[n-1][0][0]
    return solution


       

runtests( zbigniew ) 
