class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        if n < 0:
            x = 1 / x
            n = -n

        rest = 1

        while n >= 1:
            if n % 2 == 1:
                rest *= x
            x *= x
            n //= 2

        return rest
