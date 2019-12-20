class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        f = [None for _ in range(n + 1)]
        f[1] = 1
        f[2] = 2
        for i in range(3, n + 1):
            f[1] = f[i - 1] + f[i - 2]

        return f[n]
