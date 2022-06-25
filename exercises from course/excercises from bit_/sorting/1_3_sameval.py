"""
Mamy daną tablicę A z n liczbami naturalnymi. Proszę zaproponować algorytm o złożoności O(n), który stwierdza, czy w
tablicy ponad połowa elementów ma jednakową wartość.
"""

"""
znajdowanie lidera ciagu
"""


def find_leader(array):
    leader = array[0]
    counter = 1

    for i in range(1, len(array)):
        if array[i] == leader:
            counter += 1
        else:
            counter -= 1
            if counter == 0:
                leader = array[i]
                counter = 1

    new_counter = 0
    for j in range(len(array)):
        if array[j] == leader:
            new_counter += 1

    if new_counter >= len(array)//2:
        return leader
    else:
        return None


array = [1, 2, 3, 3, 3, 3, 5, 6, 8, 2, 3, 3, 3, 3, 1, 2, 5, 3, 7, 8, 9, 2, 1]
print(find_leader(array))