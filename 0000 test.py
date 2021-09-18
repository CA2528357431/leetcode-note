class Solution:
    def maxTaxiEarnings(self, n: int, rides) -> int:
        for li in rides:
            li[2] = li[2] + li[1] - li[0]
        rides.sort(key=lambda a:a[0])
        i = len(rides)
        res = [0]*(n+1)
        for index in range(n-1,0,-1):

            while rides[i-1][0]>=index and i>0:
                i-=1


            neo = 0
            for ride in rides[i:]:
                nn = res[ride[1]]+ride[2]
                neo = max(nn,neo)
            res[index] = max(res[index+1],neo)

        return res[1]
sol = Solution()
x = sol.maxTaxiEarnings(20,[[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]])
print(x)