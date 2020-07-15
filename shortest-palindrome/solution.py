from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def get_table(p):

            table = [0] * len(p)
            i = 1
            j = 0

            while i < len(p):
                if p[i] == p[j]:
                    j += 1
                    table[i] = j
                    i += 1
                else:
                    if j > 0:
                        j = table[j - 1]
                    else:
                        i += 1
                        j = 0
            return table

        table = get_table(s + "#" + s[::-1])
        return s[table[-1]:][::-1] + s
