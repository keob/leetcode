from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length
        res[0] = 1
        num = 1

        for i in range(1, length):
            res[i] = nums[i - 1] * res[i - 1]

        for i in reversed(range(length)):
            res[i] = res[i] * num
            num *= nums[i]

        return res
