class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0
        cur = 0
        for x in s:
            if x=="X":
                cur+=1
            else:
                if cur!=0:
                    cur+=1
            if cur==3:
                res+=1
                cur = 0
        if cur!=0:
            res+=1
        return res