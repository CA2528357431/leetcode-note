class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        space = 0
        froze = 0
        big = 0
        for x in range(1,len(prices)):
            hold = max(space-prices[x],hold)
            space = froze
            froze = max(hold+prices[x],froze)
            big = max(space,froze)
        return big

    # 有确定状态的时候用此方法维护各个状态下的值

    # 卖出的当天和后一天不交易
