"""
W problemie coin change mamy daną kwotę X i chcemy ją rozmienić na monety o wartości 1, 5, 10, 25 i 100.
Podaj algorytm, który obliczy, ile minimalnie monet trzeba użyć do wydania reszty oraz ile sztuk każdej monety będzie trzeba użyć.
Można założyć, że każdej monety mamy nieskończenie wiele sztuk.
Czy algorytm zachłanny działa dla zestawu monet 1, 2, 7, 10? Jeśli tak, uzasadnij dlaczego. Jeśli nie, podaj kontrprzykład.
"""

"""
wybieramy co najwieksza monete i odejmujemy wartosc od X, i tak w kólko az X == 0
"""


def coin_change(X, coins):
    coins.sort()
    i = len(coins) - 1
    coin = coins[i]
    result = []

    while X > 0:
        while coin > X:
            i -= 1
            coin = coins[i]
        X -= coin
        result.append(coin)

    return result


coins = [7, 5, 3, 2, 1, 25, 4]
print(coin_change(30, coins))