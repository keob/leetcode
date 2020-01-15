from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l, t = 10001, 10001
                if matrix[i][j] != 0:
                    if i > 0:
                        t = matrix[i - 1][j]

                    if j > 0:
                        l = matrix[i][j - 1]

                    matrix[i][j] = min(l, t) + 1

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                r, b = 10001, 10001
                if matrix[i][j] != 0:
                    if i < len(matrix) - 1:
                        b = matrix[i + 1][j]

                    if j < len(matrix[0]) - 1:
                        r = matrix[i][j + 1]

                    matrix[i][j] = min(matrix[i][j], min(r, b) + 1)

        return matrix
