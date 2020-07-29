from typing import List
from queue import Queue



class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(x, y, maze, m, n):
            ret = [[-1]*n for _ in range(m)]
            ret[x][y] = 0
            q = Queue()
            q.put((x,y))

            while q.qsize():
                curx, cury = q.get()
                for dx, dy in dd:
                    nx = curx + dx
                    ny = cury + dy
                    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != '#' and ret[nx][ny] == -1:
                        ret[nx][ny] = ret[curx][cury] + 1
                        q.put((nx, ny))
            return ret

        m = len(maze)
        n = len(maze[0])
        startX = -1
        startY = -1
        endX = -1
        endY = -1
        buttons = []
        stones = []

        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'S':
                    startX = i
                    startY = j
                elif maze[i][j] == 'T':
                    endX = i
                    endY = j
                elif maze[i][j] == 'O':
                    stones.append((i,j))
                elif maze[i][j] == 'M':
                    buttons.append((i,j))
                else:
                    pass

        nb = len(buttons)
        ns = len(stones)
        startToAnyPos = bfs(startX, startY, maze, m, n)

        if nb == 0:
            return startToAnyPos[endX][endY]

        dist = [[-1]*(nb+2) for _ in range(nb)]
        buttonsToAnyPos = []

        for i in range(nb):
            bx, by = buttons[i]
            iToAnyPos = bfs(bx, by, maze, m, n)
            buttonsToAnyPos.append(iToAnyPos)
            dist[i][nb + 1] = iToAnyPos[endX][endY]

        for i in range(nb):
            tmp = -1
            for j in range(ns):
                sx, sy = stones[j]
                if buttonsToAnyPos[i][sx][sy] != -1 and startToAnyPos[sx][sy] != -1:
                    if tmp == -1 or tmp > buttonsToAnyPos[i][sx][sy] + startToAnyPos[sx][sy]:
                        tmp = buttonsToAnyPos[i][sx][sy] + startToAnyPos[sx][sy]

            dist[i][nb] = tmp

            for j in range(i+1, nb):
                mn = -1
                for k in range(ns):
                    sx, sy = stones[k]
                    if buttonsToAnyPos[i][sx][sy] != -1 and buttonsToAnyPos[j][sx][sy] != -1:
                        if mn == -1 or mn > buttonsToAnyPos[i][sx][sy] + buttonsToAnyPos[j][sx][sy]:
                            mn = buttonsToAnyPos[i][sx][sy] + buttonsToAnyPos[j][sx][sy]
                dist[i][j] = mn
                dist[j][i] = mn

        for i in range(nb):
            if dist[i][nb] == -1 or dist[i][nb+1] == -1:
                return -1

        dp = [[-1]*nb for _ in range(1 << nb)]

        for i in range(nb):
            dp[1 << i][i] = dist[i][nb]

        for mask in range(1, (1 << nb)):
            for i in range(nb):
                if mask & (1 << i) != 0:
                    for j in range(nb):
                        if mask & (1 << j) == 0:
                            nextMask = mask | (1 << j)
                            if dp[nextMask][j] == -1 or dp[nextMask][j] > dp[mask][i] + dist[i][j]:
                                dp[nextMask][j] = dp[mask][i] + dist[i][j]

        ans = -1
        finalMask = (1 << nb) - 1

        for i in range(nb):
            if ans == -1 or ans > dp[finalMask][i] + dist[i][nb + 1]:
                ans = dp[finalMask][i] + dist[i][nb + 1]

        return ans
