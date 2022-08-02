"""
1. Szachownica NxN, ustawiono pewną ilość skoczków. Opisać algorytm który sprawdzi czy jest
możliwa sekwencja ruchów spełniająca:
- każdy ruch kończy się zbiciem skoczka
- sekwencja kończy się gdy zostanie jeden skoczek
"""

moves = [(-2, -1), (-1, -2), (1, 2), (2, 1), (2, -1), (-2, 1), (-1, 2), (1, -2)]


def does_it_beat(board, row, col):
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if is_in_board(board, new_row, new_col) and board[new_row][new_col] == 1:
            return True
    return False


def is_in_board(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board)


def lets_beat(board, row, column, counter):
    counter -= 1
    if counter == 1:
        return True

    for move in moves:
        new_row = row + move[0]
        new_col = column + move[1]
        if is_in_board(board, new_row, new_col) and board[new_row][new_col] == 1:
            board[row][column] = 0
            return lets_beat(board, new_row, new_col, counter)

    return False


# 0 - free field, 1 - field taken by chess jumper
def first_jumper(matrix):
    if len(matrix) < 3:
        print("too small chess board")
        return -1

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 1:   # jumper found
                if not does_it_beat(matrix, row, col):
                    return False

    return True


def second_jumper(matrix, jumper_number):
    if len(matrix) < 3:
        print("too small chess board")
        return -1

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 1:   # jumper found
                if lets_beat(matrix, row, col, jumper_number):
                    return True

    return False


board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0]]
# print(first_jumper(board))
print(second_jumper(board, 9))