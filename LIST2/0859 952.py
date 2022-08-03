class UnionFind:
    def __init__(self, li):
        self.parent = [x for x in range(li)]
        self.rank = [0 for x in range(li)]
    def find(self, x):
        if self.parent[x]!=x:
            return self.find(self.parent[x])
        else:
            return x
    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        if self.rank[x]<self.rank[y]:
            self.parent[x] = y
        elif self.rank[x]>self.rank[y]:
            self.parent[y] = x
        else:
            self.rank[x]+=1
            self.parent[y] = x


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        for num in nums:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    uf.merge(num, i)
                    uf.merge(num, num // i)
                i += 1
        li = {}
        res = 0
        for x in nums:
            r = uf.find(x)
            if r not in li:
                li[r]=0
            li[r]+=1
            res = max(res,li[r])
        return res