from typing import List


def max_column(n: int, column: int, grid: List[List[int]]) -> int:
    result = []
    for i in range(n):
        result.append(grid[i][column])
    return max(result)


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    n = len(grid[0])
    result = 0
    for i in range(n):
        max_row = max(grid[i])
        for j in range(n):
            max_col = max_column(n, j, grid)
            diff = min(max_row, max_col) - grid[i][j]
            result += diff
    return result
