class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dic1 = {}
        for li in grid:
            t = tuple(li)
            dic1[t] = dic1.get(t, 0) + 1
        print(dic1)
        res = 0
        for i in range(n):
            li = tuple(x[i] for x in grid)
            if li in dic1:
                res += dic1[li]
        return res
