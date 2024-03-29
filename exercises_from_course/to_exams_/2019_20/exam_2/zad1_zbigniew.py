from zad1testy import runtests
"""
Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
(wartość przekąki dodaje się do aktualnej energii Zbigniewa).
Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie. 
Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do
n-1 lub −1 jeśli nie jest to możliwe.
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


def yes(previous, val):
    current = []
    for i in range(len(previous)):
        min_ = previous[i][0] + 1
        new_val = previous[i][1] + val - 1
        if new_val > 0:
            current.append([min_, new_val])
    return current


def no(previous):
    current = []
    for i in range(len(previous)):
        if previous[i][1] - 1 > 0:
            current.append([previous[i][0], previous[i][1]-1])
    return current


def function(A):
    steps = [[] for _ in range(len(A))]
    steps[0].append([1, A[0]])

    for i in range(1, len(A)):
        yes_table = []
        if A[i] > 0:
            yes_table = yes(steps[i-1], A[i])
        no_table = no(steps[i-1])
        yes_table.extend(no_table)
        steps[i] = yes_table

    if not steps[-2]:
        return None
    else:
        return min(steps[-2][i][0] for i in range(len(steps[-2])))


runtests(function)
