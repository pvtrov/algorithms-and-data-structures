from zad3testy import runtests
from math import inf

""" ile sie swiecilo max niebiskich na raz"""

"""
przechodze po lampkach m razy, ale tylko od a do b i zmieniam kolorki. tak jakby zapamietuje ile bylo ostatnio, i jesli
w nowej turze kolorek przed zmiana to niebieski, to odejmuje od licznika, jesli po zmianie to niebieski to dodaje, po
kazdej zmianie aktualizuje max ilosc swiecacych lampoek
złozonosc czasowa: O(mlogn)
pamieciowa: O(n) < tablica lamps_colours >
"""


def changing_colours(a):
    if a == 'g':
        return 'r'
    if a == 'r':
        return 'b'
    if a == 'b':
        return 'g'


def lamps( n,T ):
    lamps_colours = ['g' for _ in range(n)]
    blue_counter = 0
    max_blue_counter = -inf

    for i in range(len(T)):
        for j in range(T[i][0], T[i][1]+1, 1):   # rozwazamy tylko te co zmienia kolorek
            if lamps_colours[j] == "b":  # jesli jest niebieski to nie moze sie zmienic na niebieski wiec ta lampka nie bedzie juz niebieska wiec odejmuje
                blue_counter -= 1

            lamps_colours[j] = changing_colours(lamps_colours[j])
            if lamps_colours[j] == 'b':  # ta swieci na niebiesko wiec dodaje
                blue_counter += 1

        if blue_counter > max_blue_counter:
            max_blue_counter = blue_counter

    return max_blue_counter

    
runtests( lamps )


