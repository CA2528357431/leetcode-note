class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 有确定状态的时候用此方法维护各个状态下的值
        '''
        pos = [0]*len(prices)
        neg = [0]*len(prices)
        pos[0] = -prices[0]
        for x in range(1,len(prices)):
            pos[x] = max(pos[x-1],neg[x-1]-prices[x])
            neg[x] = max(pos[x-1]+prices[x],neg[x-1])
        return max(neg)
        '''

        # 滚动优化
        '''
        neg = 0
        pos = -prices[0]
        big = 0
        for x in range(1,len(prices)):
            neg,pos = max(neg,pos+prices[x]),max(pos,neg-prices[x])
            big = max(big,neg)
        return big
        '''

        # 吃满每一次上涨

        profit = 0
        for x in range(1,len(prices)):
            profit += max(0,prices[x]-prices[x-1])
        return profit