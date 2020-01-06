from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        r = len(matrix)
        c = len(matrix[0])
        diags = [[] for _ in range(r + c + 1)]

        for i in range(r):
            for j in range(c):
                diags[i + j].append(matrix[i][j])

        result = []

        for k in range(r + c + 1):
            if k % 2 == 1:
                result += diags[k]
            else:
                result += diags[k][::-1]

        return result
