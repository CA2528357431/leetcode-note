class Solution:
    def minCostClimbingStairs(self, cost):
        if len(cost)>2:
            la = cost[0]
            cur = cost[1]
            par = 1
            while par<len(cost)-1:
                par+=1
                la,cur = cur,min(cur,la)+cost[par]
            return min(la,cur)
        else:
            return min(cost)

sol = Solution()
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
