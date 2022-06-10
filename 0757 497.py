class Solution:

    def __init__(self, rects: List[List[int]]):
        self.li = rects
        s = 0
        for a, b, x, y in rects:
            s += (x - a + 1) * (y - b + 1)
        self.s = s

    def pick(self) -> List[int]:
        s = random.randint(0, self.s - 1)
        aa, bb, xx, yy = 0, 0, 0, 0

        for a, b, x, y in self.li:
            neo = (x - a + 1) * (y - b + 1)
            if s < neo:
                aa, bb, xx, yy = a, b, x, y
                break
            else:
                s -= neo
        w = xx - aa + 1
        x = aa + s % w
        y = bb + s // w
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()