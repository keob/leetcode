class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(len(num) // 2):
            a = num[:i + 1]
            for j in range(i + 1, len(num) - 1):
                b = num[i + 1:j + 1]
                num1 = num[j + 1:]
                if self.tracetrack(a, b, num1):
                    return True
        return False

    def tracetrack(self, a, b, num1):
        if a[0] == '0' and len(a) >= 2:
            return False
        if b[0] == '0' and len(b) >= 2:
            return False
        s = int(a) + int(b)
        s = str(s)
        ls = len(s)
        c = num1[:ls]
        if c[0] == '0' and len(c) > 2:
            return False
        if s == c:
            num1 = num1[ls:]
            return True if not num1 else self.tracetrack(b, c, num1)
        else:
            return False
