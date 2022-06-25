"""
Otrzymujemy na wejściu listę par ludzi, które się wzajemnie znają. Osoby są reprezentowane przez liczby od 0 do n - 1.
Dnia pierwszego osoba 0 przekazuje pewną wiadomość wszystkim swoim znajomym. Dnia drugiego każdy ze znajomych przekazuje
tę wiadomość wszystkim swoim znajomym, którzy jej jeszcze nie znali, i tak dalej.
Napisz algorytm, który zwróci dzień, w którym najwięcej osób poznało wiadomość oraz ilość osób, które tego dnia ją otrzymały.
"""
"""
zapisuje sobie w krawedzi pomiedzy osobami dzien w ktrym powiedzieli, korzystam z bfs, zeby okreslic dzien to
sprawdzam wczesniejsza krawdz z rodzicem i jaki tam bym dzien
"""

from queue import Queue


def BFS(network, first_person):
    queue = Queue()
    these_who_knows = [False for _ in range(len(network[0]))]
    days = [0 for _ in range(len(network[0]))]
    who_told_you_so = [None for _ in range(len(network[0]))]

    these_who_knows[first_person] = True
    who_told_you_so[first_person] = 0
    days[0] = 1
    queue.put(first_person)

    while queue.qsize():
        person = queue.get()
        for friend in range(len(network[person])):
            if network[person][friend] != 0:
                if not these_who_knows[friend]:
                    these_who_knows[friend] = True
                    day = network[person][who_told_you_so[person]]
                    network[person][friend] = day + 1
                    network[friend][person] = day + 1
                    who_told_you_so[friend] = person
                    queue.put(friend)

    for i in range(len(network)):
        for j in range(i, len(network[i])):
            if network[i][j] >= 1:
                days[network[i][j]] += 1

    maximum = -256
    day = 0
    for i in range(len(days)):
        if days[i] > maximum:
            day = i
            maximum = days[i]

    return day, maximum


network = [[0, -1, 0, 0, -1, 0, 0],
           [-1, 0, -1, -1, 0, 0, 0],
           [0, -1, 0, 0, 0, 0, -1],
           [0, -1, 0, 0, -1, -1, -1],
           [-1, 0, 0, -1, 0, -1, 0],
           [0, 0, 0, -1, -1, 0, 0],
           [0, 0, -1, -1, 0, 0, 0]]
print(BFS(network, 0))
