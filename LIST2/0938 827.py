class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        used = [[False] * n for _ in range(n)]
        island = 0

        dic = {}
        sizes = {0: 0}

        for i in range(n):
            for j in range(n):

                if grid[i][j] == 0:
                    continue
                if used[i][j]:
                    continue

                used[i][j] = True
                island += 1

                num = 0
                cur = [(i, j)]
                while cur:
                    num += len(cur)
                    neo = []
                    for x, y in cur:
                        dic[(x, y)] = island
                        for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                            if xx >= n or xx < 0 or yy >= n or yy < 0:
                                continue
                            if grid[xx][yy] == 0 or used[xx][yy]:
                                continue
                            neo.append([xx, yy])
                            used[xx][yy] = True
                    cur = neo
                sizes[island] = num

        res = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                iss = [0] * 4
                li = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                for x in range(4):
                    xx, yy = li[x]
                    if xx >= n or xx < 0 or yy >= n or yy < 0:
                        continue

                    if grid[xx][yy] == 0:
                        continue
                    island = dic[(xx, yy)]
                    iss[x] = island
                iss = list(set(iss))
                neo = 1
                for x in iss:
                    neo += sizes[x]
                res = max(res, neo)

        if res == 0:
            return n ** 2

        return res






