from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = self.count_alive(board, i, j)
                if board[i][j] and cnt in [2, 3]:
                    board[i][j] = 3
                if not board[i][j] and cnt == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

    def count_alive(self, board, i, j):
        m, n = len(board), len(board[0])
        cnt = 0
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if not (0 <= x < m and 0 <= y < n):
                continue
            cnt += board[x][y] & 1

        return cnt
