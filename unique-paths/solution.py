class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                res[j] += res[j-1]

        return res[-1]