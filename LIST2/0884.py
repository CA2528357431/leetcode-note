class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        res = [0]*n
        for i in range(n):
            e = edges[i]
            res[e]+=i
        re = 0
        for i in range(n):
            if res[i]>res[re]:
                re = i
        return re