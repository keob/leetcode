from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sum_indices = {}
        results = set()

        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:]):
                j += i + 1
                sum_ = a + b
                sum_indices[sum_] = {
                    *sum_indices.get(sum_, set()), ((i, j), (a, b))
                }
                deviation = target - sum_
                implements = sum_indices.get(deviation, set())
                for (k, l), (c, d) in implements:
                    if len({i, j, k, l}) == 4:
                        indices = tuple(sorted([a, b, c, d]))
                        results.add(indices)

        results = [list(i) for i in results]

        return results
