from queue import PriorityQueue

from tests import runtests

neibs = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def is_inside(ropes, index_x, index_y):
    return 0 <= index_x < len(ropes) and 0 <= index_y < len(ropes[0]) and ropes[index_x][index_y] > 0


def take_rope(ropes, x, y, cap):
    cap += ropes[x][y]
    ropes[x][y] = 0
    new_x = [x - 1, x + 1, x, x]
    new_y = [y, y, y+1, y-1]
    for i in range(len(new_y)):
        if 0 <= new_x[i] < len(ropes) and 0 <= new_y[i] < len(ropes[0]):
            if ropes[new_x[i]][new_y[i]] != 0:
                cap += take_rope(ropes, new_x[i], new_y[i], cap)
    return cap


def go_to_next_step(curr, dest, stops, rope_queue):
    if dest > len(stops):
        return len(stops)-1, rope_queue
    while curr <= dest:
        if stops[curr] > 0:
            rope_queue.put((-stops[curr], curr))
        curr += 1
    return dest, rope_queue


def plan(T):
    stops = []
    result = [0]
    rope_queue = PriorityQueue()

    for i in range(len(T)):
        rope = 0
        if T[0][i] > 0:
            rope = take_rope(T, 0, i, rope)
        stops.append(rope)

    curr = 0
    cap = stops[0]
    stops[0] = 0
    next_ = curr + cap
    curr, rope_queue = go_to_next_step(curr, next_, stops, rope_queue)

    while curr <= len(stops)-1 and not rope_queue.empty():
        cap, index = rope_queue.get()
        result.append(index)
        cap = abs(cap)
        curr, rope_queue = go_to_next_step(curr, curr+cap, stops, rope_queue)
        if curr >= len(stops)-1:
            break

    result.sort()
    return result


runtests(plan)