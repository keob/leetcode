from typing import List


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, K + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + 1
            if dp[i][K] >= N:
                return i
