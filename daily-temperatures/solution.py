from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        next = [float('inf')] * 102
        ans = [0] * len(T)

        for i in range(len(T) - 1, -1, -1):
            warmerIndex = min(next[t] for t in range(T[i] + 1, 102))
            if warmerIndex < float('inf'):
                ans[i] = warmerIndex - i
            next[T[i]] = i

        return ans
