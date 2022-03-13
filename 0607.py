class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        way = {}
        weight = {}
        for f, t, w in edges:
            if f not in way:
                way[f] = set()
            way[f].add(t)
            if (f, t) not in weight:
                weight[(f, t)] = w
            else:
                weight[(f, t)] = min(w, weight[(f, t)])

        def deal(li, i):
            tensor = i
            cnt = 1
            used = {i}
            for _ in range(n - 1):
                if tensor in way:
                    for x in way[tensor]:
                        if x in used:
                            continue
                        elif li[x] == -1:
                            li[x] = weight[(tensor, x)] + li[tensor]
                        else:
                            li[x] = min(li[x], weight[(tensor, x)] + li[tensor])
                used.add(tensor)
                nxt = -1
                for i in range(n):
                    if i not in used and li[i] >= 0:
                        if nxt == -1:
                            nxt = i
                        elif li[nxt] > li[i]:
                            nxt = i
                tensor = nxt

        to1 = [-1] * n
        to1[src1] = 0
        to2 = [-1] * n
        to2[src2] = 0
        deal(to1, src1)
        deal(to2, src2)

        wayb = {}
        weightb = {}
        for f, t, w in edges:
            if t not in wayb:
                wayb[t] = set()
            wayb[t].add(f)
            if (f, t) not in weightb:
                weightb[(f, t)] = w
            else:
                weightb[(f, t)] = min(w, weightb[(f, t)])

        def dealb(li, i):
            tensor = i
            cnt = 1
            used = {i}
            for _ in range(n - 1):
                if tensor in wayb:
                    for x in wayb[tensor]:

                        if x in used:
                            continue
                        elif li[x] == -1:
                            li[x] = weightb[(x, tensor)] + li[tensor]
                            do = True
                        else:
                            li[x] = min(li[x], weightb[(x, tensor)] + li[tensor])
                            do = True
                used.add(tensor)
                nxt = -1
                for i in range(n):
                    if i not in used and li[i] >= 0:
                        if nxt == -1:
                            nxt = i
                        elif li[nxt] > li[i]:
                            nxt = i
                tensor = nxt

        to3 = [-1] * n
        to3[dest] = 0
        dealb(to3, dest)

        res = -1
        for i in range(n):
            if to1[i] >= 0 and to2[i] >= 0 and to3[i] >= 0:
                if res < 0:
                    res = to1[i] + to2[i] + to3[i]
                else:
                    res = min(res, to1[i] + to2[i] + to3[i])

        return res



