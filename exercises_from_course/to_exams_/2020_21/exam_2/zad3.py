from zad3testy import runtests


def lamps(n, T):
    max_ = 0
    lamps_ = ["z"] * n

    sum_ = 0
    for switch in T:
        start = switch[0]
        end = switch[1]
        for lamp in range(start, end + 1):
            if lamps_[lamp] == "z":
                lamps_[lamp] = "c"
            elif lamps_[lamp] == "c":
                lamps_[lamp] = "n"
                sum_ += 1
            else:
                lamps_[lamp] = "z"
                sum_ -= 1

        if max_ < sum_:
            max_ = sum_

    return max_


runtests(lamps)
# print(lamps(8, [(0, 4), (2, 6)]))

