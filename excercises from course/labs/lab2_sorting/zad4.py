# Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami.
# Pojemniki maja kształty prostokątów, rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest
# przez współrzędne lewego górnego rogu i prawego dolnego rogu.
# Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła do najniźszych
# pojemników). Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanych


def bubble_sort(array_of_containers):
    length_of_array = len(array_of_containers)
    for right in range(length_of_array - 1):
        for left in range(0, length_of_array - right - 1):
            if array_of_containers[left][1][1] > array_of_containers[left + 1][1][1]:
                array_of_containers[left], array_of_containers[left + 1] = \
                    array_of_containers[left + 1], array_of_containers[left]

    return array_of_containers


def all_fields(containers):
    sum_of_fields = 0
    for i in range(len(containers)):
        field = (containers[i][1][0] - containers[i][0][0]) * (containers[i][0][1] - containers[i][1][1])
        sum_of_fields += field
    return sum_of_fields


def checking(sorted_containers, i):
    return (sorted_containers[i][0][1] - sorted_containers[i + 1][0][1]) \
           * (sorted_containers[i][1][0] - sorted_containers[i][0][0])


def summing(sorted_containers, A):
    sum_of_fields = all_fields(sorted_containers)
    if A >= sum_of_fields:
        return len(sorted_containers)

    counter = 0
    checked = 0
    second_counter = 0
    for i in range(len(sorted_containers) - 1):
        checked += checking(sorted_containers, i)
        if sorted_containers[i][0][1] < sorted_containers[i + 1][0][1]:
            A -= (sorted_containers[i][1][0] - sorted_containers[i][0][0]) \
                 * (sorted_containers[i][0][1] - sorted_containers[i][1][1])
            if A >= 0:
                counter += 1
        else:
            second_counter += 1
            if A >= sum_of_fields - checked:
                return len(sorted_containers) - second_counter

    return counter


if __name__ == '__main__':
    # array_of_containers = [
    #     [(2, 5), (4, 2)],
    #     [(10, 6), (12, 5)],
    #     [(13, 10), (15, 7)],
    #     [(14, 9), (16, 0)]
    # ]
    # A = 30
    array_of_containers = [[(1, 4), (3, 1)],
                           [(4, 6), (6, 2)],
                           [(7, 8), (8, 4)],
                           [(10, 6), (12, 2)],
                           [(13, 4), (15, 1)]]
    A = 26
    # array_of_containers = [[(1, 4), (3, 1)],
    #                        [(5, 6), (7, 0)],
    #                        [(8, 8), (12, 4)],
    #                        [(10, 2), (12, 0)]]
    # A = 20
    # array_of_containers = [[(5, 7), (7, 0)],
    #                        [(8, 6), (10, 0)],
    #                        [(2, 4), (4, 0)],
    #                        [(4, 7), (6, 1)]]
    # A = 32
    sorted_containers = bubble_sort(array_of_containers)
    print(summing(sorted_containers, A))
