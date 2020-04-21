from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans, cnt, odd = 0, 0, [-1]
        for i, v in enumerate(nums):
            if v & 1:
                odd.append(i)
        odd.append(len(nums))
        for i in range(k, len(odd) - 1):
            l = odd[i - k + 1] - odd[i - k]
            r = odd[i + 1] - odd[i]
            ans += l * r
        return ans
