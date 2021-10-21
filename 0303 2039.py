class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        used = [False] * len(edges)
        dic = [set() for _ in range(n)]
        dis = {0: 0}
        dis[0] = 0
        cur = [0]
        length = 0
        for x, y in edges:
            dic[x].add(y)
            dic[y].add(x)

        while cur:
            length += 1
            neo = []
            for x in cur:
                li = dic[x]
                for y in li:
                    if y not in dis:
                        dis[y] = length
                        neo.append(y)
            cur = neo

        def time(l, p):
            app = 0
            if l * 2 % p == 0:
                app = l * 4 - p
            else:
                app = l * 4 - l * 2 % p
            return app

        res = 0
        for i in range(1, n):
            neo = time(dis[i], patience[i])
            res = max(res, neo)
        return res + 1