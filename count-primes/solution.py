class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        signs = [1] * n
        signs[0] = signs[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if signs[i]:
                signs[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(signs)
