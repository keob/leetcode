from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def find(m, k, nums):
            res = m
            for i in range(m+1, m+k):
                if nums[i] > nums[res]:
                    res = i
            return res

        m = find(0, k, nums)
        res = [nums[m]]

        for i in range(k, len(nums)):
            if i-k+1 > m:  
                m = find(i-k+1, k, nums)
            elif nums[m] < nums[i]:
                m = i
            res.append(nums[m])

        return res
