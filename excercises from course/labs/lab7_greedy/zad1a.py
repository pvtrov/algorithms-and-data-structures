# Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
# dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
# do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi; A
# jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
# (1) Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna.


def min_tank(number_of_station, distance_array, capacity, full_capacity, result):
    if number_of_station != len(distance_array) - 1:
        distance = distance_array[number_of_station + 1] - distance_array[number_of_station]
        if distance > full_capacity:
            print("nie da sie")
            return -1

        if capacity >= distance:
            min_tank(number_of_station + 1, distance_array, capacity - distance, full_capacity, result)

        else:
            result.append(number_of_station)
            min_tank(number_of_station + 1, distance_array, full_capacity, full_capacity, result)



if __name__ == '__main__':
    distance_array = [0, 11, 23, 30, 42, 50]  # 0 dla stacji A
    result = []
    min_tank(0, distance_array, 13, 13, result)
    print(result)
