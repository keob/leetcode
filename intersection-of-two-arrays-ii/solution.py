from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        if m == 0 or n == 0:
            return []

        dicts = {}
        for i in nums1:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1

        ret = []
        for j in nums2:
            if j in dicts and dicts[j] > 0:
                ret.append(j)
                dicts[j] -= 1

        return ret
