class RecentCounter:

    def __init__(self):
        self.li = []
        self.s = 0

    def ping(self, t: int) -> int:
        self.li.append(t)
        self.s+=1
        l = len(self.li)
        while self.li[l-self.s]<t-3000:
            self.s-=1
        return self.s


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)