class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 or n == 1:
            return 0

        cur = []
        for i in range(m):
            if grid[i][0]:
                cur.append([i, 0])
                grid[i][0] = 0
            if grid[i][n - 1]:
                cur.append([i, n - 1])
                grid[i][n - 1] = 0
        for i in range(1, n - 1):
            if grid[0][i]:
                cur.append([0, i])
                grid[0][i] = 0
            if grid[m - 1][i]:
                cur.append([m - 1, i])
                grid[m - 1][i] = 0
        while cur:
            nxt = []
            for x, y in cur:
                for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xx < 0 or xx >= m or yy < 0 or yy >= n or grid[xx][yy] == 0:
                        continue
                    nxt.append([xx, yy])
                    grid[xx][yy] = 0
            cur = nxt
        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    res += 1
        return res