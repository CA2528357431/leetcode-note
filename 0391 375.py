class Solution:
    def getMoneyAmount(self, n: int) -> int:
        li = [[0]*(n+1) for _ in range(n+1)]
        for l in range(n-1,0,-1):
            for r in range(l+1,n+1):
                li[l][r] = n*n
                for guess in range(l,r+1):
                    lnum = 0
                    if l<=guess-1:
                        lnum = li[l][guess-1]
                    rnum = 0
                    if guess+1<=n:
                        rnum = li[guess+1][r]
                    li[l][r] = min(max(lnum,rnum)+guess,li[l][r])
        return li[1][n]