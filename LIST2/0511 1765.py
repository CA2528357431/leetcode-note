class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        cur = []

        m = len(isWater)
        n = len(isWater[0])

        res = [[0] * n for _ in range(m)]
        used = isWater.copy()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    cur.append([i, j])

        i = 1
        while cur:

            nxt = []
            for x, y in cur:
                for xx, yy in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                    if xx >= m or xx < 0 or yy >= n or yy < 0 or used[xx][yy] == 1:
                        continue
                    used[xx][yy] = 1
                    res[xx][yy] = i
                    nxt.append([xx, yy])
            cur = nxt
            i += 1

        return res