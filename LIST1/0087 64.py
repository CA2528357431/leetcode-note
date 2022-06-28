class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res = [0]*len(grid[0])
        res[0] = grid[0][0]
        for y in range(1,len(grid[0])):
                res[y] = res[y-1] + grid[0][y]
        for x in range(1,len(grid)):
            res[0] = res[0] + grid[x][0]
            for y in range(1,len(grid[0])):
                res[y] = min(res[y-1],res[y])+grid[x][y]
        return res[-1]