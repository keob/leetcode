from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        root = 0

        while root != slow:
            root = nums[root]
            slow = nums[slow]

        return slow
