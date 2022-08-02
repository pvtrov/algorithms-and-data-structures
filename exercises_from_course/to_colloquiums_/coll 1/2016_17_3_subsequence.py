"""
Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
ciąg składa się wyłącznie z liter a i b.
Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.
"""

from math import inf


def subsequence(letters, k):
    words = []

    for i in range(len(letters)-k+1):   # O(n)
        slice = letters[i:i+k]
        if slice not in words:
            words.append(slice)

    counting = [0] * len(words)
    for i in range(len(letters)-k+1):   
        slice = letters[i:i+k]
        for j in range(len(words)):
            if words[j] == slice:
                counting[j] += 1
                break

    max_ = -inf
    index = 0
    for s in range(len(counting)):
        if counting[s] > max_:
            max_ = counting[s]
            index = s

    return words[index]


letters = "ababaaaabb"
print(subsequence(letters, 3))
