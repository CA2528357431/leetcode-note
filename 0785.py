class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        dic = {}
        for a, b in edges:
            if a not in dic:
                dic[a] = []
            if b not in dic:
                dic[b] = []
            dic[a].append(b)
            dic[b].append(a)

        used = set()
        for i in range(n):
            if i not in dic:
                dic[i] = []

        def find(i):
            res = {i}
            cur = [i]
            while cur:
                nxt = []
                for a in cur:
                    for b in dic[a]:
                        if b in used:
                            continue
                        used.add(b)
                        res.add(b)
                        nxt.append(b)
                cur = nxt
            return res

        group = []

        for i in range(n):
            if i in used:
                continue
            used.add(i)
            ss = find(i)
            group.append(len(ss))

        res = 0
        for i in group:
            neo = i * (n - i)
            res += neo
        return res // 2
