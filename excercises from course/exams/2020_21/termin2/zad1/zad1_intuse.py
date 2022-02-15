from zad1testy import runtests

"""
2gi sposób, chyba idzie szybcij niz 1szy
złożonosc czasowa: O(n^2)
pamieciowa: dodatkowe O(n) pamieci 

wyzanczam przedzialy ktore mieszcza sie x-y, oraz obok nich zapisuje ich poczatkowy index.
dla kazdego elementu nowej tablicy przechodze po tablicy i szukam odpowiedznich przedziałow.
w parentach zapisuje które przedzialy z którymi maja punkt wspólny i na podstawie
 parentów odtwarzam liste wynikowa """


def get_solution(result, parent, index):
    if parent[index] == [None]:
        return result

    if parent[index] == [-1]:
        if index not in result:
            result.append(index)
        return result

    if index not in result:
        result.append(index)

    for j in range(len(parent[index])):
        if parent[index][j] != [None]:
            get_solution(result, parent, parent[index][j])
    return result


def intuse(I, x, y):
    to_check = []

    for i in range(len(I)):
        if I[i][0] >= x and I[i][1] <= y:
            to_check.append([I[i], i])
        else:
            continue
    n = len(to_check)

    parent = [[] for _ in range(len(I))]

    for i in range(n):
        if to_check[i][0][0] == x:
            parent[to_check[i][1]].append(-1)
            continue
        counter = 0
        for j in range(n):
            if i != j:
                if to_check[i][0][0] == to_check[j][0][1] and parent[j] != [None]:
                    counter += 1
                    parent[to_check[i][1]].append(to_check[j][1])

        if counter == 0:
            parent[to_check[i][1]].append(None)

    true_result = []
    for i in range(n):
        if to_check[i][0][1] == y:
            true_result = get_solution(true_result, parent, to_check[i][1])

    return true_result


runtests(intuse)