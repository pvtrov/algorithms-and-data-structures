"""
struct field {
int value;
int long j;
int short j;
};
Z każdego pola można skakać tylko o ilość pól zapisaną w long j lub short j. Napisać program
który zwróci maksymalną wartość jaką możemy osiągnąć poprzez przejście z pola 0 do n-1.
Można założyć że z każdego pola da się dojść do pola n-1.
"""
from math import inf


def is_in_tab(values, position):
    return 0 <= position < len(values)


def find_max(values, new, position, max_val):
    if not is_in_tab(values, position):
        return -inf

    if position == len(values)-1:
        return max_val + values[position]

    return max_val + max(find_max(values, new, position + new[0], values[position]),
                         find_max(values, new, position + new[1], values[position]))


def field(values, long, short):
    new = [long, short]
    return find_max(values, new, 0, 0)


values = [0, 2, 3, 1, 4, 0]
print(field(values, 2, 1))