from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        x = len(matrix)
        y = len(matrix[0])
        dp = [[1 for __ in range(y)] for __ in range(x)]
        numsSort = sorted(sum([[(matrix[i][j], i, j) for j in range(y)] for i in range(x)], []))

        for i, j, k in numsSort:
            dp[j][k] = 1 + max(
                            dp[j-1][k] if j and matrix[j-1][k] < i else 0, 
                            dp[j][k-1] if k and matrix[j][k-1] < i else 0, 
                            dp[j+1][k] if j != x-1 and matrix[j+1][k] < i else 0, 
                            dp[j][k+1] if k != y-1 and matrix[j][k+1] < i else 0
                            )

        return max(sum(dp, []))
