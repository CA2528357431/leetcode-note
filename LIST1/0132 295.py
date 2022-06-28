import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.big = []
        self.small = []

    def addNum(self, num: int) -> None:
        if not self.big or num < self.big[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.big, num)

        if len(self.big) - len(self.small) > 1:
            neo = heapq.heappop(self.big)
            heapq.heappush(self.small, -neo)
        elif len(self.big) - len(self.small) < -1:
            neo = -heapq.heappop(self.small)
            heapq.heappush(self.big, neo)

    def findMedian(self) -> float:
        if len(self.big) == len(self.small):
            return (-self.small[0] + self.big[0]) / 2
        elif len(self.big) < len(self.small):
            return -self.small[0]
        else:
            return self.big[0]