class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res = []
        for i in range(m-2):
            cur = []
            for j in range(n-2):
                big = -1
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        big = max(big,grid[x][y])
                cur.append(big)
            res.append(cur)
        return res