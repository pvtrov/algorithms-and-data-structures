from math import inf

from zad3testy import runtests
"""
f(i, y, index) - funkcja zwraca minimalna ilosc tankowac do stacji i (włącznie) y (il. paliwa) starczyla na dojazd do 
stacji i+1, index to ostatnio tankowana stacja 
zła implementacja i niektorych nie przechodzi
"""


def create_path(stops, index, prev_min, path):
    if index == 0:
        path.append(0)
        return path
    min_ = prev_min - 1
    curr_idx = 0
    for j in range(len(stops[index])):
        if stops[index][j][0] == min_:
            curr_idx = j
    if stops[index][curr_idx][2] == stops[index][curr_idx][3]:
        return create_path(stops, stops[index][curr_idx][3], min_, path)
    else:
        path.append(stops[index][curr_idx][2])
        return create_path(stops, stops[index][curr_idx][3], min_, path)


def give_me_path(stops):
    min_ = inf
    index = 0
    path = []
    for i in range(len(stops[-2])):
        if stops[-2][i][0] < min_:
            min_ = stops[-2][i][0]
            index = i
    path.append(stops[-2][index][2])
    return create_path(stops, stops[-2][index][3], min_, path)


def iamlate(T, V, q, l):
    def tank(prev, index):
        now = []
        for i in range(len(prev)):
            min_ = prev[i][0]
            prev_cap = prev[i][1]
            prev_tank_idx = prev[i][2]
            cap_after_ride = prev_cap - (T[index] - T[index-1])
            if cap_after_ride + V[index] > q:
                cap_after_tank = q
            elif cap_after_ride + V[index] < T[index + 1] - T[index]:
                break
            else:
                cap_after_tank = cap_after_ride + V[index]
            now.append([min_ + 1, cap_after_tank, index, prev_tank_idx])
        return now

    def do_not_tank(prev, index):
        now = []
        for i in range(len(prev)):
            min_ = prev[i][0]
            prev_cap = prev[i][1]
            prev_tank_index = prev[i][2]
            cap_after_ride = prev_cap - (T[index] - T[index-1])
            if cap_after_ride <= 0 or cap_after_ride < T[index+1] - T[index]:
                break
            else:
                now.append([min_, cap_after_ride, prev_tank_index, prev_tank_index])
        return now

    T.append(l)
    stops = [[] for _ in range(len(T))]
    stops[0].append([1, V[0], 0, 0])  # min, curr_cap, index_tank, prev_index_tank

    for i in range(1, len(T)-1):
        if T[i+1] - T[i] > q:
            return []
        else:
            tanked = tank(stops[i-1], i)
            not_tanked = do_not_tank(stops[i-1], i)
            tanked.extend(not_tanked)
        stops[i] = tanked
    print(stops)
    if not stops[-2]:
        return []
    else:
        stops_path = give_me_path(stops)
        return stops_path[::-1]


runtests( iamlate )

