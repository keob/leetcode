from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=[]

        for i in range(len(nums)):
            if nums[i]==target:
                a.append(i)

        if target not in nums:
            return [-1,-1]
        else:
            return a[0],a[-1]
