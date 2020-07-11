from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * n
        stack = []

        def find(arr, l, r, target):
            while l <= r:
                m = l + (r - l) // 2
                if arr[m] >= target:
                    l = m + 1
                else:
                    r = m - 1
            return l

        for i in range(n-1,-1,-1):
            x = nums[i]
            idx = find(stack, 0, len(stack) - 1, x)
            count[i] = len(stack) - idx
            stack.insert(idx, x)

        return count
