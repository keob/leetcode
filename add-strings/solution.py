class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num = num1 + num2
        j = []
        n = 0
        x = ''
        y = ''

        for i in num:
            if i != '"':
                j.append(i)
        while n <= len(num1) - 1:
            x += j[n]
            j[n] = ''
            n += 1
        for m in j:
            y += m

        return str(int(x)+int(y))
