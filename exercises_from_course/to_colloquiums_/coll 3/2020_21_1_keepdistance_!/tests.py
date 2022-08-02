M1 = [[0, 1, 1, 0, 0, 0],
      [1, 0, 0, 1, 0, 0],
      [1, 0, 0, 0, 1, 0],
      [0, 1, 0, 0, 0, 1],
      [0, 0, 1, 0, 0, 1],
      [0, 0, 0, 1, 1, 0]]
x1 = 0
y1 = 5
d1 = 3
z1 = [0, 1, 0, 1, 2, 0, 2, 1, 3, 0, 2, 3, 1, 2, 0, 3, 2, 2, 1, 1, 0]

M2 = [[0, 5, 1, 0, 0, 0],
      [5, 0, 0, 5, 0, 0],
      [1, 0, 0, 1, 0, 0],
      [0, 5, 1, 0, 1, 0],
      [0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0]]
x2 = 0
y2 = 5
d2 = 4
z2 = [0, 5, 0, 1, 6, 0, 2, 5, 1, 0, 3, 6, 2, 1, 0, 4, 7, 3, 2, 1, 0]

M3 = [[0, 1, 6, 7, 7, 3, 7, 3],
      [1, 0, 8, 8, 9, 2, 6, 5],
      [6, 8, 0, 1, 4, 7, 8, 4],
      [7, 8, 1, 0, 5, 7, 8, 5],
      [7, 9, 4, 5, 0, 9, 12, 3],
      [3, 2, 7, 7, 9, 0, 4, 6],
      [7, 6, 8, 8, 12, 4, 0, 9],
      [3, 5, 4, 5, 3, 6, 9, 0]]
x3 = 6
y3 = 4
d3 = 9
z3 = [0, 1, 0, 6, 7, 0, 7, 8, 1, 0, 6, 7, 4, 5, 0, 3, 2, 7, 7, 9, 0, 7, 6, 8, 8, 12, 4, 0, 3, 4, 4, 5, 3, 6, 9, 0]

M4 = [[0, 1, 4, 0, 0, 0, 0, 0],
      [1, 0, 0, 4, 0, 0, 0, 4],
      [4, 0, 0, 0, 2, 0, 0, 0],
      [0, 4, 0, 0, 0, 0, 0, 1],
      [0, 0, 2, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 4],
      [0, 0, 0, 0, 0, 0, 0, 1],
      [0, 4, 0, 1, 0, 4, 1, 0]]
x4 = 5
y4 = 4
d4 = 4
z4 = [0, 1, 0, 4, 5, 0, 5, 4, 9, 0, 6, 7, 2, 11, 0, 9, 8, 13, 5, 15, 0, 6, 5, 10, 2, 12, 5, 0, 5, 4, 9, 1, 11, 4, 1, 0]

M5 = [[0, 2, 0, 0, 1, 0, 4, 0, 0, 0, 3, 4, 2, 4, 0, 0, 0, 0, 4, 0],
      [2, 0, 2, 0, 3, 0, 3, 0, 0, 4, 0, 0, 2, 0, 0, 0, 0, 2, 2, 3],
      [0, 2, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 3],
      [0, 0, 0, 0, 0, 3, 0, 0, 2, 3, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0],
      [1, 3, 0, 0, 0, 4, 4, 0, 0, 4, 2, 2, 2, 3, 0, 0, 0, 2, 0, 0],
      [0, 0, 0, 3, 4, 0, 0, 0, 4, 2, 4, 1, 3, 1, 3, 0, 0, 0, 0, 0],
      [4, 3, 4, 0, 4, 0, 0, 4, 4, 2, 0, 0, 2, 0, 3, 4, 2, 0, 0, 2],
      [0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 3],
      [0, 0, 0, 2, 0, 4, 4, 0, 0, 3, 0, 0, 0, 0, 1, 3, 4, 0, 0, 0],
      [0, 4, 0, 3, 4, 2, 2, 0, 3, 0, 0, 3, 2, 3, 1, 0, 4, 0, 0, 0],
      [3, 0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 3, 4, 3, 0, 0, 0, 3, 0, 0],
      [4, 0, 0, 0, 2, 1, 0, 0, 0, 3, 3, 0, 3, 0, 0, 0, 0, 4, 0, 0],
      [2, 2, 0, 0, 2, 3, 2, 0, 0, 2, 4, 3, 0, 3, 4, 0, 4, 3, 0, 4],
      [4, 0, 0, 4, 3, 1, 0, 0, 0, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 3, 0, 3, 3, 0, 1, 1, 0, 0, 4, 0, 0, 3, 3, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 4, 2, 3, 0, 0, 0, 0, 0, 3, 0, 2, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 2, 1, 4, 4, 0, 0, 4, 0, 3, 2, 0, 0, 0, 2],
      [0, 2, 4, 0, 2, 0, 0, 0, 0, 0, 3, 4, 3, 0, 0, 0, 0, 0, 4, 0],
      [4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4],
      [0, 3, 3, 0, 0, 0, 2, 3, 0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 4, 0]]
x5 = 3
y5 = 2
d5 = 7
z5 = [0, 2, 0, 4, 2, 0, 7, 7, 9, 0, 1, 3, 5, 6, 0, 4, 5, 7, 3, 3, 0, 4, 3, 4, 5, 4, 4, 0, 7, 6, 6, 7, 7, 7, 3, 0, 6, 6,
      8, 2, 6, 4, 4, 5, 0, 4, 4, 6, 3, 4, 2, 2, 5, 2, 0, 3, 5, 7, 7, 2, 4, 6, 9, 8, 6, 0, 3, 5, 7, 4, 2, 1, 5, 8, 5, 3,
      3, 0, 2, 2, 4, 5, 2, 3, 2, 5, 4, 2, 4, 3, 0, 4, 5, 7, 4, 3, 1, 5, 8, 5, 3, 3, 2, 3, 0, 5, 5, 7, 3, 5, 3, 3, 4, 1,
      1, 7, 4, 3, 4, 0, 8, 7, 7, 5, 8, 6, 4, 2, 3, 4, 10, 7, 6, 7, 3, 0, 6, 5, 5, 6, 6, 6, 2, 1, 4, 4, 8, 7, 4, 7, 3, 2,
      0, 3, 2, 4, 8, 2, 5, 5, 8, 7, 5, 3, 4, 3, 5, 6, 9, 7, 0, 4, 2, 1, 9, 5, 7, 5, 7, 8, 6, 7, 7, 4, 7, 7, 8, 6, 4, 0,
      5, 3, 3, 7, 6, 6, 2, 3, 6, 4, 8, 7, 4, 7, 5, 4, 2, 5, 4, 0]

M6 = [[0, 9, 6, 10, 15, 11, 7, 10, 8, 0, 7, 14, 7, 18, 7, 11, 8, 9, 11, 14],
      [9, 0, 15, 9, 6, 10, 7, 14, 12, 16, 11, 12, 9, 10, 13, 11, 6, 10, 17, 15],
      [6, 15, 0, 14, 7, 9, 10, 13, 17, 7, 15, 10, 8, 15, 18, 0, 12, 0, 8, 13],
      [10, 9, 14, 0, 8, 12, 7, 7, 8, 11, 12, 12, 11, 8, 0, 8, 18, 8, 10, 0],
      [15, 6, 7, 8, 0, 11, 9, 13, 13, 9, 12, 14, 9, 10, 6, 7, 0, 0, 0, 9],
      [11, 10, 9, 12, 11, 0, 0, 8, 7, 8, 11, 11, 14, 0, 6, 9, 6, 17, 15, 12],
      [7, 7, 10, 7, 9, 0, 0, 12, 14, 12, 11, 8, 13, 7, 9, 0, 11, 14, 7, 0],
      [10, 14, 13, 7, 13, 8, 12, 0, 16, 11, 0, 6, 8, 9, 8, 6, 17, 9, 12, 8],
      [8, 12, 17, 8, 13, 7, 14, 16, 0, 8, 11, 10, 9, 10, 9, 12, 11, 12, 13, 13],
      [0, 16, 7, 11, 9, 8, 12, 11, 8, 0, 12, 7, 0, 0, 17, 7, 0, 0, 0, 10],
      [7, 11, 15, 12, 12, 11, 11, 0, 11, 12, 0, 9, 6, 11, 0, 12, 13, 11, 7, 0],
      [14, 12, 10, 12, 14, 11, 8, 6, 10, 7, 9, 0, 15, 11, 8, 11, 17, 13, 13, 0],
      [7, 9, 8, 11, 9, 14, 13, 8, 9, 0, 6, 15, 0, 12, 9, 0, 7, 12, 11, 0],
      [18, 10, 15, 8, 10, 0, 7, 9, 10, 0, 11, 11, 12, 0, 8, 6, 9, 11, 7, 9],
      [7, 13, 18, 0, 6, 6, 9, 8, 9, 17, 0, 8, 9, 8, 0, 11, 8, 7, 16, 10],
      [11, 11, 0, 8, 7, 9, 0, 6, 12, 7, 12, 11, 0, 6, 11, 0, 10, 11, 8, 13],
      [8, 6, 12, 18, 0, 6, 11, 17, 11, 0, 13, 17, 7, 9, 8, 10, 0, 12, 7, 7],
      [9, 10, 0, 8, 0, 17, 14, 9, 12, 0, 11, 13, 12, 11, 7, 11, 12, 0, 12, 9],
      [11, 17, 8, 10, 0, 15, 7, 12, 13, 0, 7, 13, 11, 7, 16, 8, 7, 12, 0, 0],
      [14, 15, 13, 0, 9, 12, 0, 8, 13, 10, 0, 0, 0, 9, 10, 13, 7, 9, 0, 0]]
x6 = 3
y6 = 2
d6 = 14
z6 = [0, 9, 0, 6, 13, 0, 10, 9, 14, 0, 13, 6, 7, 8, 0, 11, 10, 9, 12, 11, 0, 7, 7, 10, 7, 9, 15, 0, 10, 14, 13, 7, 13,
      8, 12, 0, 8, 12, 14, 8, 13, 7, 14, 15, 0, 13, 15, 7, 11, 9, 8, 12, 11, 8, 0, 7, 11, 13, 12, 12, 11, 11, 14, 11,
      12, 0, 14, 12, 10, 12, 14, 11, 8, 6, 10, 7, 9, 0, 7, 9, 8, 11, 9, 13, 13, 8, 9, 15, 6, 14, 0, 14, 10, 15, 8, 10,
      14, 7, 9, 10, 13, 11, 11, 12, 0, 7, 12, 13, 14, 6, 6, 9, 8, 9, 14, 14, 8, 9, 8, 0, 11, 11, 14, 8, 7, 9, 13, 6, 12,
      7, 12, 11, 14, 6, 11, 0, 8, 6, 12, 15, 12, 6, 11, 14, 11, 14, 13, 16, 7, 9, 8, 10, 0, 9, 10, 15, 8, 13, 13, 14, 9,
      12, 18, 11, 13, 12, 11, 7, 11, 12, 0, 11, 13, 8, 10, 15, 13, 7, 12, 13, 15, 7, 13, 11, 7, 15, 8, 7, 12, 0, 14, 13,
      13, 15, 9, 12, 16, 8, 13, 10, 20, 14, 14, 9, 10, 13, 7, 9, 14, 0]

M7 = [[0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
      [2, 0, 2, 0, 0, 0, 0, 0, 0, 0],
      [0, 2, 0, 2, 0, 0, 0, 0, 0, 0],
      [0, 0, 2, 0, 1, 4, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 5, 0, 0, 0],
      [0, 0, 0, 4, 0, 0, 4, 0, 0, 0],
      [0, 0, 0, 0, 5, 4, 0, 2, 0, 0],
      [0, 0, 0, 0, 0, 0, 2, 0, 2, 0],
      [0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
      [0, 0, 0, 0, 0, 0, 0, 0, 2, 0]]
x7 = 0
y7 = 9
d7 = 5
z7 = [0, 2, 0, 4, 2, 0, 6, 4, 2, 0, 7, 5, 3, 1, 0, 10, 8, 6, 4, 5, 0, 12, 10, 8, 6, 5, 4, 0, 14, 12, 10, 8, 7, 6, 2, 0,
      16, 14, 12, 10, 9, 8, 4, 2, 0, 18, 16, 14, 12, 11, 10, 6, 4, 2, 0]

TESTS = [(M1, x1, y1, z1, d1),
         (M2, x2, y2, z2, d2),
         (M3, x3, y3, z3, d3),
         (M4, x4, y4, z4, d4),
         (M5, x5, y5, z5, d5),
         (M6, x6, y6, z6, d6),
         (M7, x7, y7, z7, d7),
         ]


def verify(L, M, x, y, z, d):
    p, q = L[0]
    if p != x or q != y: return False
    q, p = L[-1]
    if p != x or q != y: return False

    n = len(M)
    for i in range(len(L) - 1):
        p, q = L[i]
        r, s = L[i + 1]
        if ((M[p][r] == 0 and p != r) or
                (M[q][s] == 0 and q != s)):
            return False
        if r == q and s == p: return False
        (r, s) = (r, s) if r > s else (s, r)
        if z[(r + 1) * r // 2 + s] < d:
            return False
    return True


def runtests(f):
    OK = True
    for (M, x, y, z, d) in TESTS:
        print("----------------------")
        print("M:[")
        for r in M:
            print(r)
        print("]\n")
        print("x: ", x)
        print("y: ", y)
        print("d: ", d)
        L = f(M, x, y, d)
        print("uzyskany wynik:\n", L)
        if not verify(L, M, x, y, z, d):
            print("PROBLEM!!!!!! Sciezki nie spelniaja warunkow zadania.")
            OK = False

    print("----------------------")
    if not OK:
        print("PROBLEMY!")
    else:
        print("OK")