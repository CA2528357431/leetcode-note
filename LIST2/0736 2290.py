class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = [[m * n] * n for _ in range(m)]
        cnt[0][0] = True
        used = [[False] * n for _ in range(m)]
        used[0][0] = True

        used[0][0] = True

        def orifill(cur, cost):
            res = cur.copy()
            while cur:
                neo = []
                for x, y in cur:
                    for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if xx >= m or xx < 0 or yy >= n or yy < 0 or used[xx][yy] or grid[xx][yy] != grid[x][y]:
                            continue
                        neo.append((xx, yy))
                        res.append((xx, yy))
                        used[xx][yy] = True
                        cnt[xx][yy] = cost
                cur = neo
            return res

        def getfill0(cur, cost):
            res = []
            while cur:
                neo = []
                for x, y in cur:
                    for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if xx >= m or xx < 0 or yy >= n or yy < 0 or used[xx][yy] or grid[xx][yy] == 1:
                            continue
                        neo.append((xx, yy))
                        res.append((xx, yy))
                        used[xx][yy] = True
                        cnt[xx][yy] = cost
                cur = neo
            return res
        def getfill1(cur, cost):
                neo = []
                for x, y in cur:
                    for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if xx >= m or xx < 0 or yy >= n or yy < 0 or used[xx][yy] or grid[xx][yy] == 0:
                            continue
                        neo.append((xx, yy))
                        used[xx][yy] = True
                        cnt[xx][yy] = cost
                return neo

        cur = [(0, 0)]
        cur = orifill(cur, 0)
        step = 0
        while cur:
            step += 1
            cur1 = getfill1(cur, step)
            cur2 = getfill0(cur1, step)
            cur = cur2+cur1
        return cnt[-1][-1]