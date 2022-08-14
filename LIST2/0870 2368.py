class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        dic = [[] for _ in range(n)]
        for f, t in edges:
            if f in restricted or t in restricted:
                continue
            dic[f].append(t)
            dic[t].append(f)
        res = 0
        cur = [0]
        used = {0}
        while cur:
            res += len(cur)
            nxt = []
            for x in cur:
                for y in dic[x]:
                    if y in used:
                        continue
                    nxt.append(y)
                    used.add(y)
            cur = nxt
        return res

