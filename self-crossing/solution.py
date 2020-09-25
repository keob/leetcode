from typing import List


class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        if len(x) < 4:
            return False
        for i in range(2, len(x)):
            if x[i] <= x[i-2]:
                break
        if i>=4 and x[i]+x[i-4]>=x[i-2] or i==3 and x[i]==x[i-2]:
            x[i-1] -= x[i-3]
        for j in range(i+1, len(x)):
            if x[j] >= x[j-2]:
                return True
        return False
