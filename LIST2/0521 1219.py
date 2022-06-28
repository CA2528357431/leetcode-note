class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        copy = [x.copy() for x in grid]

        def deal(cur, x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return cur
            if grid[x][y] == 0:
                return cur
            neo = grid[x][y]
            grid[x][y] = 0
            res = 0
            for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                z = deal(cur + neo, xx, yy)
                res = max(res, z)
            grid[x][y] = neo
            return res

        cur = 0
        for x in range(m):
            for y in range(n):
                res = deal(0, x, y)
                cur = max(res, cur)
        return cur