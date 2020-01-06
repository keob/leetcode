class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # return bin(int(a, 2) + int(b, 2))[2:]

        if len(a) < len(b):
            a, b = b, a
        n = len(a)
        b = '0' * (n - len(b)) + b
        result = ''
        summ = 0
        for i in range(n):
            a_1 = int(a[-i - 1])
            b_1 = int(b[-i - 1])
            result = str((a_1 + b_1 + summ) % 2) + result
            summ = (a_1 + b_1 + summ) // 2
        if summ == 1:
            result = '1' + result
        return result
