"""
Dostajemy liczbę naturalną n. Naszym zadaniem jest policzenie wszystkich binarnych (0/1) stringów o długości n
bez jedynek obok siebie
"""

"""
czyli tworzymy sobie rekrencyjnie te wszytskie liczby dodajac 1/0 gdy mamy 0 lub 0 gdy mamy 1, gdy dochodzimy do ilosci 
n to zwiekszamy couter o 1 i go zwracamy
"""


def create_binary(counter, n, actual_length, last_digit):
    if n == actual_length:
        counter += 1
        return counter

    if last_digit == "1":
        counter = create_binary(counter, n, actual_length + 1, "0")
    else:
        counter = create_binary(counter, n, actual_length + 1, "1")
        counter = create_binary(counter, n, actual_length + 1, "0")
    return counter


def binary_counting(n):
    counter = 0
    return create_binary(counter, n, 1, "1") + create_binary(counter, n, 1, "0")



print(binary_counting(5))


