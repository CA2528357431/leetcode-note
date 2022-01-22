class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:
        cur = [start]
        m = len(grid)
        n = len(grid[0])
        res = []

        used = {(start[0], start[1])}

        while cur and len(res) < k:
            cur.sort(key=lambda x: (grid[x[0]][x[1]], x[0], x[1]))
            i = 0
            while i < len(cur) and len(res) < k:
                x, y = cur[i]
                if grid[x][y] < pricing[0]:
                    grid[x][y] = 0
                    i += 1
                    continue
                if grid[x][y] > pricing[1]:
                    break
                res.append(cur[i])
                i += 1
                grid[x][y] = 0
            if len(res) == k:
                return res
            while i < len(cur):
                x, y = cur[i]
                grid[x][y] = 0
                i += 1

            nxt = []
            for x, y in cur:
                for xx, yy in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                    if xx < 0 or xx >= m or yy < 0 or yy >= n or grid[xx][yy] == 0 or (xx, yy) in used:
                        continue
                    nxt.append([xx, yy])
                    used.add((xx, yy))

            cur = nxt

        return res