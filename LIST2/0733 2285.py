class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        dic = {}
        for i in range(n):
            dic[i] = 0
        for a,b in roads:
            dic[a]+=1
            dic[b]+=1
        li = [i for i in range(n)]
        li.sort(key = lambda i:dic[i])
        res = 0
        for i in range(n):
            neo = dic[li[i]]*(i+1)
            res+=neo
        return res