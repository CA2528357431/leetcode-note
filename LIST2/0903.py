class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def do(s):
            res = [0, 0, 0]
            for c in s:
                if c == "M":
                    res[0] += 1
                elif c == "P":
                    res[1] += 1
                elif c == "G":
                    res[2] += 1
            return res

        typ = [do(s) for s in garbage]
        ms = [x[0] for x in typ]
        ps = [x[1] for x in typ]
        gs = [x[2] for x in typ]

        def do(li):
            n = len(li)
            res = [True] * n
            for i in range(n - 1, -1, -1):
                if li[i] != 0:
                    break
                else:
                    res[i] = False
            return res

        mt = do(ms)
        pt = do(ps)
        gt = do(gs)

        def cnt(s, t):
            if t[0] == False:
                return 0
            n = len(s)
            res = 0
            for i in range(n):
                res += s[i]
                if i < n - 1:
                    if t[i + 1] == True:
                        res += travel[i]
                    else:
                        break
            return res

        mm = cnt(ms, mt)
        pp = cnt(ps, pt)
        gg = cnt(gs, gt)
        return mm + pp + gg
