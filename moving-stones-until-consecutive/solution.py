from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        data=sorted([a, b, c])
        l, r= data[1] - data[0] - 1, data[2] - data[1] -1
        return [1 if l == 1 or r == 1 else bool(l) + bool(r), l + r]
