from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        res = 0

        while fresh:
            if not rotten: return -1
            rotten = {(i + di, j + dj) for i, j in rotten for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)] if (i + di, j + dj) in fresh}
            fresh -= rotten
            res += 1
        return res
