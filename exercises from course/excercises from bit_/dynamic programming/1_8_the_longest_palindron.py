"""
Dostając na wejściu string złożony z liter a-z, zwrócić najdłuższy jego fragment, który jest palindromem.
Palindrom to ciąg znaków, który wygląda tak samo czytany zarówno od lewej, jak i od prawej strony.
"""


def find_max_length(string):
    useful_table = [[False for _ in range(len(string))] for _ in range(len(string))]

    max_length = 1
    for i in range(len(string)):
        useful_table[i][i] = True

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            useful_table[i][i + 1] = True
            max_length = 2

    for counter in range(3, len(string) + 1):
        for i in range(0, len(string) - counter + 1):
            j = i + counter - 1
            if useful_table[i + 1][j - 1] and string[i] == string[j]:
                useful_table[i][j] = True
                if counter > max_length:
                    max_length = counter

    return max_length


string = "forgeeksskeegfor"
print(find_max_length(string))
