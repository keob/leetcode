class Solution:
    def calculate(self, s: str) -> int:
        num ,stack ,sign = 0 , [] , '+'

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in "+-*/" or i == len(s)-1:
                if sign == "+" :
                    stack.append(num)
                elif sign == "-" :
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = ch

        return sum(stack)
