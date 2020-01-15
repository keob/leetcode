from typing import List


class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        broken_map = dict()

        for b in broken:
            if b[0] not in broken_map:
                broken_map[b[0]] = dict()

            broken_map[b[0]][b[1]] = True

        def is_broken(a, b):
            if a in broken_map and b in broken_map[a]:
                return True
            else:
                return False

        def next_state(state, put):
            state = ~(1 << (m - 1)) & state

            if put == 0:
                return state << 1
            elif put == 1:
                return ((state | 1) << 1) | 1
            elif put == 2:
                return (state << 1) | 1
            else:
                return (state << 1) | 1

        dp = [-1] * (1 << m)
        dp[(1 << m) - 1] = 0

        for i in range(n):
            for j in range(m):
                next_dp = [-1] * (1 << m)
                for state in range(1 << m):
                    if dp[state] == -1:
                        continue

                    if is_broken(i, j):
                        next_dp[next_state(state, 3)] = max(
                            next_dp[next_state(state, 3)], dp[state])
                        continue

                    next_dp[next_state(state,
                                       0)] = max(next_dp[next_state(state, 0)],
                                                 dp[state])

                    if i != 0 and (1 << (m - 1)) & state == 0:
                        next_dp[next_state(state, 2)] = max(
                            next_dp[next_state(state, 2)], dp[state] + 1)

                    if j != 0 and 1 & state == 0:
                        next_dp[next_state(state, 1)] = max(
                            next_dp[next_state(state, 1)], dp[state] + 1)

                dp = next_dp

        return max(dp)
