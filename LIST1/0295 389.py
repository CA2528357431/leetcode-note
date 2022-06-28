class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for c in s:
            dic[c] = dic.get(c,0)+1
        for c in t:
            if c not in dic or dic[c]==0:
                return c
            else:
                dic[c]-=1