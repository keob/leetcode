from typing import List


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        length = len(cont)
        res = [cont[length - 1], 1]
        for i in range(length - 2, -1, -1):
            cur = cont[i]
            left = cur * res[0]
            res = [res[1] + left, res[0]]

        return res
