from zad3testy import runtests

# Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie
# zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). Proszę zaimplementować
# funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
# z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest
# zawsze prawidłowa.)

"""
pracuje na tablicy result
w result[i] przechowuje:
[ [tablica dotychczasowego ciagu], jego długość ]

dla i sparwdzam czy jak dodam A[i] do result[j][0] to czy k sie zwiekszy
i na podstawie tego jakosn to licze < jak wiudac na załączonym kodzie >

złożonosc:  czasowa O(n*max dlugość) 
            pamieciowa taka sama
"""


def cutting(last_section):
    first_number = last_section[0]
    for i in range(len(last_section)-1, -1, -1):
        if last_section[i] == first_number:
            new_sect = last_section[i+1:]
            return [new_sect, len(new_sect) + 1]


def longest_incomplete(A, k):
    result = [[[]] for _ in range(len(A))]
    result[0] = [[A[0]], 1]
    for i in range(1, len(A)):
        last_sect = result[i-1][0].copy()
        length = result[i-1][1]
        if A[i] in result[i - 1][0]:
            result[i] = [last_sect, len(last_sect)+1]
            result[i][0].append(A[i])
        else:
            if len(result[i - 1][0]) + 1 < k:
                result[i] = [last_sect, len(last_sect)+1]
                result[i][0].append(A[i])
            else:
                result[i] = cutting(result[i - 1][0])
                result[i][0].append(A[i])
                result[i][1] = len(result[i][0])

    max_lenth = -1
    for i in range(len(A)):
        if result[i][1] > max_lenth:
            max_lenth = result[i][1]

    return max_lenth


runtests(longest_incomplete)
