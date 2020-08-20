from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        self.m = len(board)
        self.n = len(board[0])
        around = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))
        def check (i,j):
            num = 0
            for x,y in around:
                if 0<=x+i<self.m and 0<=y+j<self.n and board[x+i][y+j]=='M':
                    num += 1
            return num

        def dfs(i,j):
            num = check(i,j)
            if num :
                board[i][j] = str(num)
            else:
                board[i][j] = 'B'
                for x,y in around:
                    if 0<=x+i<self.m and 0<=y+j<self.n and board[x+i][y+j]=='E':
                        dfs(x+i,y+j)

        dfs(click[0],click[1])

        return board
