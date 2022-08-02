"""
Dana jest zawsze działająca w czasie O(1) funkcja dict(word), która mówi, czy słowo word jest poprawnym słowem danego
języka. Dostajemy na wejściu stringa bez spacji. Podaj algorytm, który stwierdzi, czy da się tak powstawiać spacje do
wejściowego stringa, że ciąg słów który otrzymamy tworzą słowa z danego języka. Np. “alamakotainiemapsa” możemy zapisać
jako “ala ma kota i nie ma psa”. Podaj również, jak wykorzystać algorytm, aby uzyskać przykładowe poprawne rozdzielenie
stringa spacjami, jeśli oczywiście ono istnieje. Algorytm ma być szybki, ale najważniejsze, żeby był poprawny!!!.
"""

langauge = ["ala", "ma", "kota", "i", "nie", "ma", "psa"]


def dict(word):
    return word in langauge


def does_it_split_to_words(string):
    spaces = [False] * (len(string)+1)
    spaces[0] = True

    for i in range(len(string) + 1):
        for j in range(i, -1, -1):
            if spaces[i]:
                break
            current_word = string[j:i]
            if dict(current_word):
                spaces[i] = spaces[j]
    return spaces[-1]


string = "alamakotainiemapda"
print(does_it_split_to_words(string))



