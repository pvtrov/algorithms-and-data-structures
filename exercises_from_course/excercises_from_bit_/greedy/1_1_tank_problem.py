"""
W problemie tankowania paliwa nasz pojazd musi przemieścić się z punktu 0 do punktu F, a po drodze ma stacje do tankowania
paliwa si, przy czym 0 < s1 < s2 < ... < sn < F. Każda stacja jest identyfikowana przez jej odległość od punktu 0,
tzn. si to odległość pomiędzy i-tą stacją a punktem 0. Pojazd potrafi przejechać odległość d bez potrzeby tankowania.
Podaj algorytm, który obliczy, na ilu minimalnie stacjach musi zatrzymać się pojazd na drodze od punktu 0 do punktu F.
Uwaga: jeżeli zdarzy się, że odległość d jest zbyt mała, żeby dojechać do kolejnej stacji, to należy zwrócić wartość None
"""
"""
wybieramy najdalsza stacje do której da sie dojechac z d 
"""


def tank(stops, d):
    result = [0]
    last_tank = 0
    i = 0

    while last_tank < len(stops)-1:
        if stops[i+1] - stops[i] > d:
            return None

        while i+1 < len(stops) and stops[i+1] - stops[last_tank] <= d:
            i = i+1
        result.append(i)
        last_tank = i

    return result


stops = [0, 2, 5, 7, 10, 12]
print(tank(stops, 2))
