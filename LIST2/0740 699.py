class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        n = len(positions)
        res = [0]*n
        for i in range(n):
            l,s = positions[i]
            r = l+s-1
            res[i] = s
            for j in range(i):
                ll,ss = positions[j]
                rr = ll+ss-1
                if r >= ll and rr >= ll:
                    res[i] = max(res[i],res[j]+s)
        for i in range(1,n):
            res[i] = max(res[i],res[i-1])
        return res