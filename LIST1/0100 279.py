class Solution:
    def numSquares(self, n: int) -> int:

        res = [99999]*(n+1)
        res[0] = 0
        for x in range(1,n+1):
            limit = int(x**0.5)
            for y in range(1,limit+1):
                res[x] = min(res[x],res[x-y**2]+1) 
        return res[-1]
