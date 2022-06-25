"""
Dana jest tablica A mająca n liczb naturalnych przyjmujących wartości z zakresu [0..n]. Proszę napisać
algorytm znajdujący rozmiar najwiekszego podzbioru liczb z A, takiego, że ich GCD jest różny od 1.
<najwiekszy wspolny dzielnik >
Algorytm powinien działać jak najszybciej
"""

"""
robie sobie buckety z dzielnikami
"""


def gcd(array):
    n = len(array)

    counter = [0] * n
