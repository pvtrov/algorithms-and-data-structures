"""
Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm,
 który oblicza minimalną ilość monet potrzebną do wydania kwoty T (algorytm zachłanny, wydający najpierw największą
 monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5
"""
"""
f(coins, sum) - funkcja zwraca najmniejsza ilosc monet jakie potrzeba do wydania reszty

f(coins, 0) - return min_coin
f(coins, sum, min) - jeśli nie "bierzemy" monety do wydania reszty
f(coins, sum - coins[n], min + 1) - jeśli "bierzemy" monete do wydania reszty 
"""

from math import inf


def sum_change(coins, sum):
    if sum == 0:
        return 0

    if sum < 0:
        return inf

    min_coins = inf
    for i in range(len(coins)):
        result = sum_change(coins, sum - coins[i])
        if result != inf:
            min_coins = min(result + 1, min_coins)

    return min_coins


if __name__ == '__main__':
    coins = [1, 5, 8]
    print(sum_change(coins, 15))