class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def fact(n):
            ret = 1
            while n:
                ret *= n
                n -= 1
            return ret

        def dfs(remain, path, k):
            if not remain:
                return path

            l = len(remain)

            count = fact(l-1)

            for i in range(l):
                if k > count:
                    k -= count
                else:
                    return dfs(remain[:i]+remain[i+1:], path+remain[i], k)

        return dfs([str(i) for i in range(1, n+1)], '', k)
