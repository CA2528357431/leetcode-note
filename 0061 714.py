class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pos = -prices[0]
        neg = 0
        big = 0
        for x in range(1,len(prices)):
            pos,neg = max(pos,neg-prices[x]),max(neg,pos+prices[x]-fee)
            big = max(big,neg)
        return big