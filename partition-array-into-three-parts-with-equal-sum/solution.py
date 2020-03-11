from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        asum = sum(A)
        if asum % 3 > 0:
            return False
        part = asum // 3
        n = len(A)
        left, right = 0, n - 1
        pl, pr = A[0], A[n - 1]
        while left < right - 1:
            if pr == part and pl == part:
                return True
            if pl != part:
                left += 1
                pl += A[left]
            if pr != part:
                right -= 1
                pr += A[right]
        return False
