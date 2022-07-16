class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        inf = 99999999
        n = len(grid)
        f = [[-inf] * n for _ in range(n)]
        f[0][0] = grid[0][0]
        for k in range(1, n * 2 - 1):
            for x1 in range(min(k, n - 1), max(k - n, -1), -1):
                for x2 in range(min(k, n - 1), x1 - 1, -1):
                    y1, y2 = k - x1, k - x2
                    if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                        f[x1][x2] = -inf
                        continue
                    res = f[x1][x2]  # 都往右
                    if x1:
                        res = max(res, f[x1 - 1][x2])  # 往下，往右
                    if x2:
                        res = max(res, f[x1][x2 - 1])  # 往右，往下
                    if x1 and x2:
                        res = max(res, f[x1 - 1][x2 - 1])  # 都往下
                    res += grid[x1][y1]
                    if x2 != x1:  # 避免重复摘同一个樱桃
                        res += grid[x2][y2]
                    f[x1][x2] = res
        return max(f[-1][-1], 0)