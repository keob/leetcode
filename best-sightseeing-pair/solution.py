from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        length = len(A)

        if length == 0:
            return 0
        if length == 1:
            return A[0]

        dp = A[0]*2
        res =0

        for i in range(1, length):
            dp = max(dp - A[i-1] + A[i] -1, A[i-1] + A[i] -1)
            res = max(res, dp)

        return res
