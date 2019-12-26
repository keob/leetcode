from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        symbol = ["+", "-", "*", "/"]
        recList = []

        if len(tokens) == 0:
            return 0
        else:
            for c in tokens:
                if c not in symbol:
                    recList.append(c)
                else:
                    b = int(recList.pop())
                    a = int(recList.pop())
                    if c == "+":
                        recList.append(str(a + b))
                    elif c == "-":
                        recList.append(str(a - b))
                    elif c == "*":
                        recList.append(str(a * b))
                    elif c == "/":
                        recList.append(str(int(a / b)))

            return recList[0]
