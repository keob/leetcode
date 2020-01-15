class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            n = sum([int(i)**2 for i in str(n)])

            if n == 4:
                return False
            if n == 1:
                return True
