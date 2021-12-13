class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        l = [0]*n
        u = [0]*n
        for i in range(n):
            for j in range(n):
                u[j] = max(u[j],grid[i][j])
                l[i] = max(l[i],grid[i][j])
        res = 0
        for i in range(n):
            for j in range(n):
                delta = min(u[j],l[i])-grid[i][j]
                res+=delta
        return res