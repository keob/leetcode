from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        ans = []

        def backtrack(path, summ, index):
            if summ == target:
                ans.append(path)
            elif summ > target:
                return 
            elif summ < target:
                for i in range(index, len(candidates)):
                    backtrack(path + [candidates[i]], summ + candidates[i], i)

        backtrack([], 0, 0)

        return ans
