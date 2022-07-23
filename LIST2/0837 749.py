class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:

        m = len(isInfected)
        n = len(isInfected[0])

        def do(ps):
            cnt = []
            for x, y in ps:
                for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xx >= m or xx < 0 or yy >= n or yy < 0:
                        continue
                    if isInfected[xx][yy] == 0:
                        cnt.append((xx, yy))
            return cnt

        ii = 0
        cnt = 0
        while True:
            virtus = []
            used = set()

            for i in range(m):
                for j in range(n):
                    p = (i, j)
                    if p in used:
                        continue

                    if isInfected[i][j] != 1:
                        continue
                    res = [p]
                    cur = [p]
                    used.add(p)
                    while cur:
                        nxt = []
                        for x, y in cur:
                            for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                                pp = (xx, yy)
                                if xx >= m or xx < 0 or yy >= n or yy < 0:
                                    continue
                                if pp in used:
                                    continue
                                if isInfected[xx][yy] != 1:
                                    continue

                                nxt.append(pp)
                                res.append(pp)
                                used.add(pp)
                        cur = nxt
                    virtus.append(res)
            if len(virtus) == 0:
                return cnt

            neo = [do(ps) for ps in virtus]

            ind = 0
            for i in range(len(neo)):

                if len(set(neo[i])) > len(set(neo[ind])):
                    ind = i

            if len(neo[ind]) == 0:
                return cnt
            else:
                for i in range(len(neo)):
                    if i == ind:
                        for x, y in virtus[i]:
                            isInfected[x][y] = -1
                        cnt += len(neo[i])
                    else:

                        for x, y in neo[i]:
                            isInfected[x][y] = 1