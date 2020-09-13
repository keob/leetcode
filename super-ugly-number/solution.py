from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        pointer = [0] * len(primes)
        dp[0] = 1

        for i in range(1, n):
            dp[i] = min(x * dp[y] for x, y in zip(primes, pointer))
            for j in range(len(primes)):
                if dp[i] == primes[j] * dp[pointer[j]]:
                    pointer[j] += 1

        return dp[-1]
