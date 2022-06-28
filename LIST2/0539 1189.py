class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {}
        for t in text:
            dic[t] = dic.get(t,0)+1
        res = 9999
        for c in "ban":
            res = min(dic.get(c,0),res)
        for c in "ol":
            res = min(dic.get(c,0)//2,res)
        return res