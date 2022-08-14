class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        sell = [0] * (k + 1)
        buy = [-prices[0]] * (k + 1)
        for p in prices[1:]:
            neosell = sell.copy()
            neobuy = buy.copy()
            for i in range(1, k + 1):
                neosell[i] = max(sell[i], buy[i] + p)
                neobuy[i] = max(buy[i], sell[i - 1] - p)
            sell = neosell
            buy = neobuy
        return max(sell)

