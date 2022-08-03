

import sys

def minimumCost(grid, i, j):
    if (i < 0 or j < 0):
        return sys.maxsize
    elif i == 3 or j == 3:
        return grid[i][j]
    else:
        return grid[i][j] + min(minimumCost(grid, i + 1, j + 1), minimumCost(grid, i + 1, j - 1), minimumCost(grid, i + 1, j))


def maxCoins(grid):
    return min(minimumCost(grid, 0, 0), minimumCost(grid, 0, 1), minimumCost(grid, 0, 2), minimumCost(grid, 0, 3))
