"""
W jednej z chińskich prowincji postanowiono wybudować serię maszyn chroniących ludność przed koronawirusem. Prowincję
można zobrazować jako tablicę wartości 1 i 0, gdzie arr[i] = 1 oznacza, że w mieście i można zbudować maszynę, a wartość 0,
że nie można. Dana jest również liczba k, która oznacza, że jeśli postawimy maszynę w mieście i, to miasta o indeksach j
takich, że abs(i-j) < k są przez nią chronione. Należy zaproponować algorytm, który stwierdzi ile minimalnie maszyn potrzeba
aby zapewnić ochronę w każdym mieście, lub -1 jeśli jest to niemożliwe.
"""
"""
pomyusl git ale cos nie dziala w kodzie
"""

def chineese_cities(cities, k):
    protected_ranges = []

    for i in range(len(cities)):
        if cities[i] == 1:
            start = i - k
            end = i + k
            if start >= 0 and end < len(cities):
                protected_ranges.append([start, end])
            elif start < 0:
                protected_ranges.append([0, end])
            elif end >= len(cities):
                protected_ranges.append([start, len(cities)-1])

    protected_ranges.sort()
    counter = 1
    if protected_ranges[0][0] != 0:
        return -1

    index = 1
    last_end = protected_ranges[0][1]

    while index < len(protected_ranges):
        if protected_ranges[index][0] <= last_end:
            prob_new_end = protected_ranges[index][1]
            almost_idx = index
        else:
            return -1
        check_index = index + 1
        while check_index < len(protected_ranges) and protected_ranges[check_index][0] <= last_end:
            if protected_ranges[check_index][1] > prob_new_end:
                prob_new_end = protected_ranges[check_index][1]
                almost_idx = check_index
            check_index += 1
        if check_index == almost_idx:
            index = almost_idx
        counter += 1
        index += 1

    return counter


cicteis = [0, 0, 1, 0, 0, 1, 1, 0]
print(chineese_cities(cicteis, 2))


