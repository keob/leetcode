from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int],
                     D: List[int]) -> int:
        assert (len(A) == len(B) == len(C) == len(D))

        memo = dict()
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] + B[j] in memo:
                    memo[A[i] + B[j]] += 1
                else:
                    memo[A[i] + B[j]] = 1

        ret = 0
        for i in range(len(C)):
            for j in range(len(D)):
                if -C[i] - D[j] in memo:
                    ret += memo[-C[i] - D[j]]

        return ret
