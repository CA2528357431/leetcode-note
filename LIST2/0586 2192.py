class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 整体迭代
        '''
        cur = [set() for _ in range(n)]
        for f, t in edges:
            cur[f].add(t)

        i = 1
        while i < n:
            neo = [x.copy() for x in cur]
            for f in range(n):
                if len(neo[f]) == n - 1:
                    continue
                for t in cur[f]:
                    neo[f] = neo[f] | cur[t]
                    if len(neo[f]) == n - 1:
                        break
            cur = neo
            i = i * 2

        res = [[] for _ in range(n)]
        for f in range(n):
            for t in cur[f]:
                res[t].append(f)

        return res
        '''
        # 局部迭代
        class Solution:
            def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
                fathers = [set() for _ in range(n)]
                ori = [set() for _ in range(n)]
                for f, t in edges:
                    fathers[t].add(f)

                for i in range(n):
                    cur = fathers[i].copy()
                    while cur:
                        neo = cur.pop()
                        cur.update(fathers[neo])
                        # 取并集
                        # 快于 | 运算
                        ori[i].add(neo)
                res = [list(x) for x in ori]
                for x in res:
                    x.sort()
                return res