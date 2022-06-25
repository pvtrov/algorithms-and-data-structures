"""Proszę napisać funkcję bool possible( char* u, char* v, char* w ), która zwraca prawdę
jeśli z liter słów u i v da się ułożyć słowo w (nie jest konieczne wykorzystanie wszystkich liter)
oraz fałsz w przeciwnym wypadku. Można założyć, że w i v składają się wyłącznie z małych liter
alfabetu łacińskiego. Proszę krótko uzasadnić wybór zaimplementowanego algorytmu"""

""" najpierw zliczamy z dwóch słów ile jakich liter mamy, potem przechodimy po chcianym slowie i 
 na kazdej litery usuwamy ja z policzonych liter, nastepnie przechodzimy po policzonej, jesli cos ma <0 to zwracamy 
 false, jak wszytskie są dodatnie lub 0 to zwracamy true
 """


def possible(u, v, w):
    checker = [0] * 1000
    for i in range(len(u)):
        checker[ord(u[i])] += 1

    for j in range(len(v)):
        checker[ord(v[j])] += 1

    for s in range(len(w)):
        checker[ord(w[s])] -= 1

    for p in range(len(checker)):
        if checker[p] < 0:
            return False
    return True


if __name__ == '__main__':
    u = "aga"
    v = "marta"
    w = "umart"
    print(possible(u, v, w))