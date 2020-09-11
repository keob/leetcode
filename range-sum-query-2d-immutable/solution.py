from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.res = [[0] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.res[i].append(self.res[i][-1]+matrix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for i in range(row1,row2+1):
            result+=self.res[i][col2+1] - self.res[i][col1]
        return result
