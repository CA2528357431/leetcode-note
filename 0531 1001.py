class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        points = set()
        lr = {}
        ud = {}
        plus = {}
        minus = {}
        for x, y in lamps:
            if (x, y) in points:
                continue
            points.add((x, y))

            if x not in lr:
                lr[x] = 0
            lr[x] += 1

            if y not in ud:
                ud[y] = 0
            ud[y] += 1

            if x + y not in plus:
                plus[x + y] = 0
            plus[x + y] += 1

            if x - y not in minus:
                minus[x - y] = 0
            minus[x - y] += 1

        res = []
        for x, y in queries:
            if (x in lr and lr[x]) or (y in ud and ud[y]) or (x + y in plus and plus[x + y]) or (
                    x - y in minus and minus[x - y]):
                res.append(1)
                for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x, y), (x + 1, y + 1), (x - 1, y - 1),
                               (x - 1, y + 1), (x + 1, y - 1)]:
                    if (xx, yy) in points:
                        lr[xx] -= 1
                        ud[yy] -= 1
                        plus[xx + yy] -= 1
                        minus[xx - yy] -= 1
                        points.remove((xx, yy))

            else:
                res.append(0)

        return res