from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                res += 2
                for dx,dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] < grid[i][j]:
                            res += grid[i][j] - grid[x][y]
                    else:
                        res += grid[i][j]
        return res
