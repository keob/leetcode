class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def addNum(self, num: int) -> None:
        if not self.store:
            self.store.append(num)
        else:
            bisect.insort_left(self.store, num)

    def findMedian(self) -> float:
        n = len(self.store)

        if n & 1 == 1:
            return self.store[n // 2]
        else:
            return (self.store[n // 2] + self.store[n // 2 - 1]) / 2
