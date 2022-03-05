class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

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