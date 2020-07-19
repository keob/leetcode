from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]
        res = [[0] * (n + 2) for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += res[i][k] + res[k][j]
                    res[i][j] = max(res[i][j], total)

        return res[0][n + 1]
