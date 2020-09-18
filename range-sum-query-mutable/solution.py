class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.n = len(nums)
        d = {}
        def pre(l = 0, r = self.n - 1):
            if l < r:
                m = (l + r) // 2
                d[l, r] = pre(l, m) + pre(m + 1, r)
                return d[l, r]
            else:
                d[l, l] = nums[l]
                return nums[l]
        pre()
        self.d = d

    def update(self, i: int, val: int) -> None:
        d = self.d
        def upd(l = 0, r = self.n-1):
            if l == i== r:
                d[i, i] = val
                return d[i, i]
            elif l <= i <= r:
                m = (l + r) // 2
                d[l, r] = upd(l, m) + upd(m + 1, r)
                return d[l, r]
            else:
                return d[l, r]
        upd()

    def sumRange(self, i: int, j: int) -> int:
        d = self.d
        def sumK(k, l = 0, r = self.n - 1):
            m = (l + r) // 2
            if k == r:
                return d[l, r]
            elif k > m:
                return d[l, m] + sumK(k, m + 1, r)
            else:
                return sumK(k, l, m)
        return sumK(j) - sumK(i) + d[i, i]
