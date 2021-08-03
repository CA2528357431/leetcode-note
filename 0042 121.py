class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 动态规划

        '''
        if len(prices)==1:
            return 0
        res = [0]*(len(prices)-1)
        for x in range(len(prices)-1):
            res[x] = prices[x+1]-prices[x]
        cur = res[0]
        ma = cur
        p = 0
        while p <= len(res)-2:
            p+=1
            cur = max(res[p],res[p]+cur)
            ma = max(cur,ma)
        return max(ma,0)
        '''

        # 双指针

        b = prices[0]
        profit = 0
        for s in range(len(prices)):
            if prices[s]<b:
                b = prices[s]
            profit = max(profit,prices[s]-b)
        return profit

        # b记录此前的最低价格
        # s遍历当前价格
        # profit记录当前价格
