class Solution:
    def solveNQueens(self, n):
        ans = []

        def dfs(nums, row):
            if row == n:
                ans.append(nums[:])
                return
            for col in range(n):
                nums[row] = col
                if valid(nums, row):
                    dfs(nums, row + 1)

        def valid(nums, row):
            for i in range(row):
                if abs(nums[i] - nums[row]) == abs(row -
                                                   i) or nums[i] == nums[row]:
                    return False
            return True

        dfs([None for _ in range(n)], 0)

        result = [[] for _ in range(len(ans))]
        for i in range(len(ans)):
            for col in ans[i]:
                tmp = '.' * n
                result[i].append(tmp[:col] + 'Q' + tmp[col + 1:])

        return result
