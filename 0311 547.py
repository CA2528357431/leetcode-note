class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        used = set()
        res = 0
        cur = []
        for x in range(n):
            if x in used:
                continue
            cur = [x]
            used.add(x)
            res+=1
            while cur:
                neo = []
                for p in cur:
                    connect = isConnected[p]
                    for c in range(n):
                        if c not in used and connect[c]==1:
                            used.add(c)
                            neo.append(c)
                cur = neo
        return res