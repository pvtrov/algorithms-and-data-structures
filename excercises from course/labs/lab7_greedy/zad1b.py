# Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
# dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
# do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi; A
# jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
# (2) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodatkowo cenę za
# litr paliwa). Na każdej stacji możemy tankować dowolną ilość paliwa.

def min_prize(number_of_station, petrol_stations, full_capacity, current_capacity, result):
    if petrol_stations[len(petrol_stations)-1][0] <= full_capacity:
        return "żadnych tankowan, moje pieniadze"

    if number_of_station != len(petrol_stations)-1:
        distance = petrol_stations[number_of_station+1][0] - petrol_stations[number_of_station][0]

        if distance > full_capacity:
            return "chuj nie jade dalej"


        if current_capacity < distance:
            if petrol_stations[number_of_station+1][1] < petrol_stations[number_of_station]:
                result.append(number_of_station)
                min_prize(number_of_station+1, petrol_stations, full_capacity, current_capacity+distance, result)
            else:
                result.append(number_of_station)
                min_prize(number_of_station+1, petrol_stations, full_capacity, full_capacity, result)

        if current_capacity >= distance:
            if petrol_stations[number_of_station+1][1] < petrol_stations[number_of_station][1]:
                min_prize(number_of_station+1, petrol_stations, full_capacity, current_capacity, result)
            else:
                result.append(number_of_station)
                min_prize(number_of_station+1, petrol_stations, full_capacity, full_capacity, result)
    return result




if __name__ == '__main__':
    petrol_stations = [(0, 0), (11, 5), (23, 2), (30, 5), (42, 5), (50, 0)]
    result = []
    print(min_prize(0, petrol_stations, 30, 30, result))