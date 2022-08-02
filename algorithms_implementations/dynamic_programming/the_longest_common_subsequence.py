
def lis(array):         #O(n^2)
    n = len(array)
    matrix = [1] * n
    helping_matrix = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if array[j] < array[i] and matrix[j] + 1 > matrix[i]:
                matrix[i] = matrix[j] + 1
                helping_matrix[i] = j

    return max(helping_matrix), helping_matrix, matrix


def print_solution(array, helping_matrix, i):
    if helping_matrix[i] != -1:
        print_solution(array, helping_matrix, helping_matrix[i])

    print(array[i])
