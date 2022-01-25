class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        res = 0
        n = len(cost)
        for i in range(n-1,-1,-1):
            if (n-i)%3!=0:
                res+=cost[i]
        return res