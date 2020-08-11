class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        k = 1

        if n<= 0:
            return 0

        while k <= n:
            count += (n//(10*k))*k + min(max(n%(10*k)-k+1, 0), k)
            k *= 10

        return count
