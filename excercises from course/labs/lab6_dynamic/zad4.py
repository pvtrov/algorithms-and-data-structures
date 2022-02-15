"""
Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
każdej z liczb.
"""
"""
    wyniki zapisuje w tablicy i ta tablicą bede sie posługiwac
    result[i] = [min ilość skoków by się dostać na i-ty kamien, kcale po zjedzeniu i-tej przekąski 
                (uwzgleniajac spalenie energi w trakcie skoku)]  <----- to jest dwupolowa tablica w tablicy
    
    result[i] = bierzemy kamien o najmniejszej liczbie skokow { na przykład j (j<i) } i sprawdzamy czy z niego doskoczymy na i-ty kamien
                * tak -> result[i] = [result[j][0]+1, result[j][1] - (i-j) + kcal[i] ]
                * nie to sprawdzamy dalej (iterujemy po tablicy wyników)
"""
from math import inf


def zbigniew_hungry_frog(kcals, result):
    result[0] = [0, kcals[0][1]]

    for i in range(1, len(result)):
        min = inf
        for j in range(i):
            if result[j][1] - (kcals[i][0] - kcals[j][0]) >= 0:
                if result[j][0] < min:
                    min = result[j][0]
                    energy = result[j][1] - (kcals[i][0] - kcals[j][0]) + kcals[i][1]
        result[i] = [min + 1, energy]

    return result[len(result)-1][0]


if __name__ == '__main__':
    numbers_and_kcals = [(0, 5), (3, 5), (7, 3), (9, 6), (13, 2), (15, 4)]
    result = [[0, 0] for _ in range(len(numbers_and_kcals))]
    number_of_jumps = zbigniew_hungry_frog(numbers_and_kcals, result)
    print(number_of_jumps)