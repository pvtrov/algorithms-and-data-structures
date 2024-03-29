"""
Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
(wartość przekąski dodaje się do aktualnej energii Zbigniewa).

Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie.
Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do
n-1 lub −1 jeśli nie jest to możliwe.

Podpowiedź. Warto rozważyć funkcję f(i, y) zwracającą minimalną liczbę skoków potrzebną by
dotrzeć do liczby i mieć w zapasie dokładnie y jednostek energii.
Przykład. Dla tablicy A = [2,2,1,0,0,0] wynikiem jest 3 (Zbigniew skacze z 0 na 1, z 1
na 2 i z 2 na 5, kończąc z zerową energią). Dla tablicy A = [4,5,2,4,1,2,1,0] wynikiem jest 2
(Zbigniew skacze z 0 na 3 i z 3 na 7, kończąc z jedną jednostką energii)
"""


def eat(prev, snaks, index):
    now = []
    for i in range(len(prev)):
        min_ = prev[i][0]
        kcals = prev[i][1]
        kcals += snaks[index] - 1
        if kcals > 0:
            now.append([min_ + 1, kcals])
    return now


def do_not_eat(prev, snaks, index):
    now = []
    for i in range(len(prev)):
        min_ = prev[i][0]
        kcals = prev[i][1] - 1
        if kcals > 0:
            now.append([min_, kcals])
    return now


def zbigniew(A):
    n = len(A)
    jumps = [[] for _ in range(n)]
    jumps[0].append([1, A[0]])
    for i in range(1, len(A)-1):
        if A[i] > 0:
            eaten = eat(jumps[i-1], A, i)
            not_eaten = do_not_eat(jumps[i-1], A, i)
            eaten.extend(not_eaten)
            jumps[i] = eaten
        else:
            not_eaten = do_not_eat(jumps[i-1], A, i)
            jumps[i] = not_eaten

    if not jumps[-2]:
        return -1
    else:
        return min(jumps[-2][i][0] for i in range(len(jumps[-2])))
