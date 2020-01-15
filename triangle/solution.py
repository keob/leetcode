from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mini, M = triangle[-1], len(triangle)

        for i in range(M - 2, -1, -1):
            for j in range(len(triangle[i])):
                mini[j] = triangle[i][j] + min(mini[j], mini[j + 1])

        return mini[0]
