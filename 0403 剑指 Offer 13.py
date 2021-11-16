class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def get(x):
            s = 0
            while x:
                s += (x % 10)
                x = x // 10
            return s

        def check(x, y):
            if x >= m or x < 0 or y >= n or y < 0:
                return False
            xs = get(x)
            ys = get(y)
            if xs + ys > k:
                return False
            return True

        res = 0
        used = [[False] * n for _ in range(m)]
        used[0][0] = True
        cur = [(0, 0)]
        while cur:
            res += len(cur)
            neo = []
            for x, y in cur:
                for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if check(xx, yy) and not used[xx][yy]:
                        used[xx][yy] = True
                        neo.append((xx, yy))
            cur = neo
        return res