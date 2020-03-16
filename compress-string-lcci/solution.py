from typing import List


class Solution:
    def compressString(self, S: str) -> str:
        length = len(S)
        res = ''
        i = 0
        while i < length:
            j = i
            while j < length and S[j] == S[i]:
                j += 1
            res += S[i] + str(j - i)
            i = j

        if len(res) < len(S):
            return res
        else:
            return S
