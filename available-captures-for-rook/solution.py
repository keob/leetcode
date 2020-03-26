from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res, st, ed = 0, 0, 0
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    st, ed = i, j
        for i in range(4):
            step = 0
            while True:
                tx = st + step * dx[i]
                ty = ed + step * dy[i]
                if tx < 0 or tx >= 8 or ty < 0 or ty >= 8 or board[tx][ty] == "B":
                    break
                if board[tx][ty] == "p":
                    res += 1
                    break
                step += 1
        return res
