# Dany jest zbiór punktów X = {x1, . . . , xn} na
# prostej. Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
# potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch
# przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).

def ranges(X, index, result):
    if len(X) == 1:
        return result + 1

    if X[len(X)-1]-X[index] <= 1:
        return result + 1

    upper_limit = X[index] + 1
    result += 1
    new_index = index

    while X[new_index] <= upper_limit:
        temporary = index
        new_index = temporary + 1
        index = new_index

    if new_index == len(X)-1:
        return result+1
    else:
        return ranges(X, new_index, result)


if __name__ == '__main__':
    #X = [0.3, 0.75, 1.2, 1.4, 1.9, 2.5]
    X = [0.25, 0.5, 1.6]
    result = 0
    print(ranges(X, 0, result))