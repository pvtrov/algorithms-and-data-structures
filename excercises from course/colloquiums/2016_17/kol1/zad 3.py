"""Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
ciąg składa się wyłącznie z liter a i b.
Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność."""

""" iteruje po ciągu znakow, zapisuje nie pojawiające sie wczesniej podcigi do krotek, a te które sie pojawiły to
ich licznik zwikeszam o jeden
"""


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        variable = bucket[i][1]
        j = i - 1
        while j >= 0 and variable < bucket[j][1]:
            temporary = bucket[j + 1]
            bucket[j + 1] = bucket[j]
            bucket[j] = temporary
    return bucket


def substrings(word, k):
    strings = [[0, 0]] * (len(word) - (k - 1))
    helping_index = 0
    for i in range(len(word) - (k - 1)):
        for j in range(helping_index + 1):
            if strings[j][0] == word[i:i + k]:
                strings[j][1] += 1
                break
        strings[helping_index] = [word[i:i + k], 1]
        helping_index += 1

    sorted = insertion_sort(strings)
    return sorted[-1][0]


if __name__ == '__main__':
    word = 'ababaaaabb'
    k = 3
    substrings(word, k)
    print(substrings(word, 2))
