class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for v, w in items1:
            if v not in dic:
                dic[v] = 0
            dic[v] += w
        for v, w in items2:
            if v not in dic:
                dic[v] = 0
            dic[v] += w

        res = []
        for k in dic:
            res.append([k, dic[k]])
        res.sort(key=lambda x: x[0])
        return res