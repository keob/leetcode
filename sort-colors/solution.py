from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        point0 = curr = 0
        point2 = len(nums) - 1

        while curr <= point2:
            if nums[curr] == 0:
                nums[point0], nums[curr] = nums[curr], nums[point0]
                point0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[point2] = nums[point2], nums[curr]
                point2 -= 1
            else:
                curr += 1
