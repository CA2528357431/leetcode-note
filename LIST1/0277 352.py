class SummaryRanges:

    def __init__(self):
        self.res = []

    def addNum(self, val: int) -> None:
        if not self.res:
            self.res.append([val, val])
        else:
            if val < self.res[0][0]:
                if val == self.res[0][0] - 1:
                    self.res[0][0] -= 1
                else:
                    self.res.insert(0, [val, val])
            elif val >= self.res[-1][0] - 1:
                if val == self.res[-1][0] - 1:
                    if len(self.res) > 1 and self.res[-2][1] == self.res[-1][0] - 2:
                        self.res[-2][1] = self.res[-1][-1]
                        self.res.pop()
                    else:
                        self.res[-1][0] -= 1
                elif val <= self.res[-1][1]:
                    pass
                elif val == self.res[-1][1] + 1:
                    self.res[-1][1] += 1
                else:
                    self.res.append([val, val])
            else:

                l = 0
                r = len(self.res) - 1
                while l < r:
                    mid = (l + r) // 2 + 1
                    if val < self.res[mid][0]:
                        r = mid - 1
                    elif self.res[mid][0] < val:
                        l = mid
                    else:
                        return

                if val <= self.res[l][1]:

                    pass
                else:

                    if self.res[l + 1][0] == self.res[l][1] + 2:
                        self.res[l][1] = self.res[l + 1][1]
                        self.res.pop(l + 1)
                    elif val == self.res[l][1] + 1:
                        self.res[l][1] += 1
                    elif val == self.res[l + 1][0] - 1:
                        self.res[l + 1][0] -= 1
                    else:
                        self.res.insert(l + 1, [val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.res

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()