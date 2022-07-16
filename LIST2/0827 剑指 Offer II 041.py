class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.li = [0]*size
        self.i = 0

    def next(self, val: int) -> float:
        self.li[self.i%len(self.li)] = val
        self.i += 1
        res = sum(self.li)/min(self.i,len(self.li))
        return res


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)