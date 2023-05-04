class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:

        dic = {}
        deg = {}
        for a, b in edges:
            if a not in dic:
                dic[a] = set()
            if b not in dic:
                dic[b] = set()
            dic[a].add(b)
            dic[b].add(a)
            if a not in deg:
                deg[a] = 0
            if b not in deg:
                deg[b] = 0
            deg[a] += 1
            deg[b] += 1

        nocoin = {k for k in dic if deg[k] == 1 and coins[k] == 0}

        while nocoin:
            nxt = set()

            for k in nocoin:
                deg[k] = 0
                for kk in dic[k]:
                    if deg[kk] != 0:
                        deg[kk] -= 1
                        if deg[kk] == 1 and coins[kk] == 0:
                            nxt.add(kk)

            nocoin = nxt

        for _ in range(2):
            zeros = {k for k in dic if deg[k] == 1}

            for k in zeros:
                deg[k] = 0
                for kk in dic[k]:
                    if deg[kk] != 0:
                        deg[kk] -= 1
        # print(dic)

        res = 0
        for k in dic:
            res += deg[k]
        return res