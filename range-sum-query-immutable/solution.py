from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0]
        for i in range(len(nums)):
            self.arr.append(self.arr[i]+nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.arr[j+1] - self.arr[i]
