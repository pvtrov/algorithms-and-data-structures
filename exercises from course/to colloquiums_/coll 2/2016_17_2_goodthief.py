"""
Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
int goodThief( int A[], int n );
która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
kodeksem moralnym oraz wypisuje numery przedmiotów które powinien wybrać. Proszę uzasadnić
poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny).
"""

"""
f(i) -  najwiekszy zysk jaki mozna uzyskac wubierjac od 0 do i-tego przedmiotu nie biorac dwoch obok siebie
f(0) = P[0]
f(i) = max( f(i-1), f(i-2) + P[i] ) 
"""


def print_path(last_stolen, index, result):
    if last_stolen[index] == -1:
        result.append(index)
        return result
    result = print_path(last_stolen, last_stolen[index], result)
    result.append(index)
    return result


def get_stolen_items(values, last_stolen):
    if values[-1] > values[-2]:
        return print_path(last_stolen, len(values)-1, [])
    else:
        return print_path(last_stolen, len(values)-2, [])


def get_right_index(values, index):
    while values[index] == values[index-1]:
        index = index-1
        if index < 0:
            break

    return index


def good_thief(things, n):
    values = [0] * n
    values[0] = things[0]
    last_stolen = [-1] * n
    if things[0] > things[1]:
        values[1] = things[0]
        last_stolen[1] = 0

    for i in range(2, n):
        if values[i-1] > values[i-2] + things[i]:
            values[i] = values[i-1]
            last_stolen[i] = last_stolen[i-1]
        else:
            values[i] = values[i-2] + things[i]
            last_stolen[i] = get_right_index(values, i-2)

    stolen_items = get_stolen_items(values, last_stolen)
    return stolen_items, max(values)


things = [15, 2, 6, 18, 9, 5, 13, 14, 17, 8, 3, 24]
print(good_thief(things, 12))
