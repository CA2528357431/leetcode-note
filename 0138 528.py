class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.source = [0] * (n+1)
        for x in range(1, n+1):
            self.source[x] = self.source[x - 1] + w[x - 1]

    def pickIndex(self) -> int:
        total = self.source[-1]
        ran = random.randint(0,total-1)
        l = 0
        r = len(self.source)-1
        while l<r-1:
            mid = (l+r)//2
            if self.source[mid]<=ran:
                l = mid
            else:
                r = mid
        return l