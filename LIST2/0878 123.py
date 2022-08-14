class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nothing = 0
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0
        for p in prices[1:]:
            neo_nothing = 0
            neo_buy1 = max(nothing - p, buy1)
            neo_sell1 = max(buy1 + p, sell1)
            neo_buy2 = max(buy2, sell1 - p)
            neo_sell2 = max(sell2, buy2 + p)

            nothing = neo_nothing
            buy1 = neo_buy1
            sell1 = neo_sell1
            buy2 = neo_buy2
            sell2 = neo_sell2
        return max(nothing, sell1, sell2)