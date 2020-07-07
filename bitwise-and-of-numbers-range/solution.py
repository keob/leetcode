class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = 0   

        while m < n:
            m = m >> 1
            n = n >> 1
            res += 1
        return m << res
