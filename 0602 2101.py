class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        n = len(bombs)
        mapp = [[] for x in range(n)]
        for i in range(n):
            x, y, r = bombs[i]
            for ii in range(n):
                if ii == i:
                    continue
                xx, yy, rr = bombs[ii]
                distance = (x - xx) ** 2 + (y - yy) ** 2
                if distance <= r ** 2:
                    mapp[i].append(ii)

        def do(i):
            used = [False] * n
            used[i] = True
            done = 1
            cur = [i]
            while cur:
                neo = []
                for ii in cur:
                    for j in mapp[ii]:
                        if used[j]:
                            continue
                        neo.append(j)
                        done += 1
                        used[j] = True

                cur = neo
            return done

        res = 1
        for i in range(n):
            res = max(res, do(i))
        return res
