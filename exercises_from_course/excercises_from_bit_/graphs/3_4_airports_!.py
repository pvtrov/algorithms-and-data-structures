"""
Dostajemy na wejściu listę trójek (miastoA, miastoB, koszt). Każda z nich oznacza, że możemy zbudować drogę między
miastem A i B za podany koszt. Ponadto, w dowolnym mieście możemy zbudować lotnisko za koszt K, niezależny od miasta.
Na początku w żadnym mieście nie ma lotniska, podobnie między żadnymi dwoma miastami nie ma wybudowanej drogi.
Naszym celem jest zbudować lotniska i drogi za minimalny łączny koszt, tak aby każde miasto miało dostęp do lotniska.
Miasto ma dostęp do lotniska, jeśli:
1) jest w nim lotnisko, lub
2) można z niego dojechać do innego miasta, w którym jest lotnisko
Jeżeli istnieje więcej niż jedno rozwiązanie o minimalnym koszcie, należy wybrać to z największą ilością lotnisk.
"""

