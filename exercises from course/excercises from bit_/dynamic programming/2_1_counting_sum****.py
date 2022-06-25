"""
Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą być zarówno dodatnie jak
i ujemne). Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej kolejności, by
największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji dodawania; wartość końcowej sumy również
traktujemy jak wynik tymczasowy) był możliwie jak najmniejszy.

Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie wybiera kolejność dodawań. Napisz
funkcję opt sum, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie; zakładamy,
że tablica zawiera co najmniej dwie liczby) i zwraca największą wartość bezwzględną wyniku tymczasowego w optymalnej
kolejności dodawań.

Na przykład dla tablicy wejściowej: [1,−5, 2] funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie
dodaniu 1 do wyniku. Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową.
"""
"""
zapytac kogos kto ogarnia
"""

from math import inf

"""
sum(i,j) - suma liczb od ni do nj, możemy ją obliczać w O(1) jeśli zapamiętamy sumy prefiksowe

f(i, j) = najwieksza wartosc bezwzgledna wyniku tymczasowego z dodawania liczb od Ni do Nj
f(i, i+1) = abs(Ni + N(i+1))
f(i, j) = max( sum(i, j), min(f(i+1, j), f(i, j-1)))
"""


def opt_sum(array):
    prefix = [0] * (len(array) + 1)
    for i in range(len(array)):
        prefix[i + 1] = prefix[i] + array[i]

    dp = [[0] * len(array) for _ in range(len(array))]
    for i in range(1, len(array)):
        for j in range(len(array) - i):
            dp[j][i + j] = prefix[i + j + 1] - prefix[j]
            best_value = inf
            for k in range(j, i + j):
                best_value = min(max(abs(dp[j][k]), abs(dp[k + 1][i + j])), abs(best_value))
            dp[j][i + j] = max(abs(best_value), abs(dp[j][i + j]))
    return abs(dp[0][len(array) - 1])


array = [1, -5, 2]
print(opt_sum(array))