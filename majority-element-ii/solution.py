from typing import List



class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a, b, count_a, count_b = 0, 0, 0, 0
        res = []

        for i in nums:
            if a == i:
                count_a += 1
                continue
            if b == i:
                count_b += 1
                continue
            if count_a == 0:
                a = i
                count_a = 1
                continue
            if count_b == 0:
                b = i
                count_b = 1
                continue
            count_a -= 1
            count_b -= 1        

        count_a, count_b = 0, 0

        for j in nums:
            if j == a:
                count_a += 1
            elif j == b:
                count_b += 1
        if count_a > len(nums)/3:
            res.append(a)
        if count_b > len(nums)/3:
            res.append(b)

        return res
